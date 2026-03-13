"""Tests for security/secrets.py."""

import hashlib
import hmac
import logging

import pytest

from security.secrets import AppSecrets, RedactingFilter, get_secrets, redact, verify_webhook_signature


class TestAppSecrets:
    def test_defaults(self, monkeypatch):
        monkeypatch.delenv("DATABASE_URL", raising=False)
        monkeypatch.delenv("OPENCLAW_PROVIDER", raising=False)
        monkeypatch.delenv("WEBHOOK_PORT", raising=False)
        secrets = AppSecrets()
        assert secrets.openclaw_provider == "openrouter"
        assert secrets.webhook_port == 8080
        assert secrets.database_url == "sqlite:///data/agent.db"

    def test_loads_from_env(self, env_secrets):
        secrets = get_secrets()
        assert secrets.openclaw_provider == "openai"
        assert secrets.openclaw_api_key == "sk-test-key-123"
        assert secrets.slack_bot_token == "xoxb-test-token"

    def test_get_secrets_returns_same_instance(self, env_secrets):
        s1 = get_secrets()
        s2 = get_secrets()
        assert s1 is s2


class TestRedact:
    def test_redacts_slack_bot_token(self):
        assert "<REDACTED>" in redact("token is xoxb-1234-abcd")

    def test_redacts_github_token(self):
        assert "<REDACTED>" in redact("ghp_abcdef1234567890")

    def test_preserves_normal_text(self):
        assert redact("Normal log line") == "Normal log line"


class TestVerifyWebhookSignature:
    def test_valid_signature(self):
        secret = "my-secret"
        payload = b'{"hello": "world"}'
        mac = hmac.new(secret.encode(), payload, hashlib.sha256)
        signature = f"sha256={mac.hexdigest()}"
        assert verify_webhook_signature(payload, signature, secret) is True

    def test_invalid_signature(self):
        assert verify_webhook_signature(b"payload", "sha256=bad", "secret") is False


class TestRedactingFilter:
    def test_filter_redacts_msg(self):
        f = RedactingFilter()
        record = logging.LogRecord(
            name="test", level=logging.INFO, pathname="", lineno=0,
            msg="Token is ghp_abc123xyz789", args=(), exc_info=None,
        )
        f.filter(record)
        assert "ghp_" not in record.msg
        assert "<REDACTED>" in record.msg
