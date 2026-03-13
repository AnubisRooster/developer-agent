"""Tests for webhooks/server.py."""

import hashlib
import hmac
import json
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client(env_secrets):
    with patch("webhooks.server.event_bus") as mock_bus:
        mock_bus.publish = AsyncMock()
        from webhooks.server import app
        yield TestClient(app), mock_bus


class TestHealthEndpoint:
    def test_health(self, client):
        tc, _ = client
        resp = tc.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


class TestGitHubWebhook:
    def test_valid_request_no_secret(self, client, monkeypatch):
        tc, _ = client
        monkeypatch.setenv("GITHUB_WEBHOOK_SECRET", "")
        from security.secrets import get_secrets
        get_secrets.cache_clear()
        payload = {"action": "opened", "pull_request": {"number": 1}}
        resp = tc.post("/webhooks/github", json=payload, headers={"x-github-event": "pull_request"})
        assert resp.status_code == 200
        assert resp.json()["event_type"] == "github.pull_request.opened"


class TestSlackWebhook:
    def test_url_verification(self, client, monkeypatch):
        tc, _ = client
        monkeypatch.setenv("SLACK_SIGNING_SECRET", "")
        from security.secrets import get_secrets
        get_secrets.cache_clear()
        payload = {"type": "url_verification", "challenge": "abc123"}
        resp = tc.post("/webhooks/slack", json=payload)
        assert resp.status_code == 200
        assert resp.json()["challenge"] == "abc123"
