"""Tests for integration connectors."""

from unittest.mock import MagicMock, patch

import pytest


class TestSlackIntegration:
    @pytest.fixture
    def slack(self, env_secrets):
        with patch("integrations.slack.WebClient") as MockClient:
            from integrations.slack import SlackIntegration
            instance = SlackIntegration()
            instance._client = MockClient.return_value
            return instance

    def test_send_message(self, slack):
        slack._client.chat_postMessage.return_value = {"ts": "123", "channel": "C1", "ok": True}
        result = slack.send_message("#general", "hello")
        assert result["ok"] is True
        slack._client.chat_postMessage.assert_called_once_with(channel="#general", text="hello")


class TestGitHubIntegration:
    @pytest.fixture
    def github(self, env_secrets):
        with patch("integrations.github_integration.Github") as MockGithub:
            from integrations.github_integration import GitHubIntegration
            instance = GitHubIntegration()
            instance._client = MockGithub.return_value
            return instance

    def test_create_issue(self, github):
        mock_repo = MagicMock()
        mock_issue = MagicMock(number=42, html_url="https://github.com/org/repo/issues/42", title="Bug")
        mock_repo.create_issue.return_value = mock_issue
        github._client.get_repo.return_value = mock_repo
        result = github.create_issue("org/repo", "Bug", "description")
        assert result["number"] == 42
        mock_repo.create_issue.assert_called_once_with(title="Bug", body="description")


class TestGmailIntegration:
    @pytest.fixture
    def gmail(self, env_secrets):
        with patch("integrations.gmail.os.path.exists", return_value=False):
            from integrations.gmail import GmailIntegration
            return GmailIntegration()

    def test_not_configured_read_emails(self, gmail):
        result = gmail.read_emails()
        assert len(result) == 1
        assert result[0]["ok"] is False
        assert "not configured" in result[0]["error"].lower()
