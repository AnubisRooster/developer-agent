"""Tests for cli/chat.py and main.py."""

from unittest.mock import patch

import pytest
from click.testing import CliRunner


class TestCLIChat:
    def test_start_chat_function_exists(self):
        from cli.chat import start_chat
        assert callable(start_chat)


class TestMainCLI:
    @pytest.fixture
    def runner(self):
        return CliRunner()

    def test_cli_help(self, runner, env_secrets):
        from main import cli
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "chat" in result.output
        assert "webhook-server" in result.output

    def test_build_orchestrator(self, env_secrets):
        with patch("integrations.slack.WebClient"), \
             patch("integrations.github_integration.Github"), \
             patch("integrations.jira_integration.JIRA"), \
             patch("integrations.confluence.Confluence"), \
             patch("integrations.jenkins.jenkins.Jenkins"), \
             patch("integrations.gmail.os.path.exists", return_value=False):
            from main import _build_orchestrator
            orch = _build_orchestrator()
            tools = orch._registry.list_tools()
            assert len(tools) > 0
