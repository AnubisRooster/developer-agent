"""Tests for agent/memory.py, agent/planner.py, agent/orchestrator.py."""

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agent.memory import ConversationMemory
from agent.planner import ActionPlan, PlanStep, Planner
from agent.orchestrator import LLMClient, Orchestrator, ToolRegistry, TOOL_CALL_PATTERN


class TestConversationMemory:
    def test_add_and_get(self):
        mem = ConversationMemory()
        mem.add_message("user", "hello")
        mem.add_message("assistant", "hi there")
        ctx = mem.get_context()
        assert len(ctx) == 2
        assert ctx[0]["role"] == "user"
        assert ctx[1]["content"] == "hi there"

    def test_clear(self):
        mem = ConversationMemory()
        mem.add_message("user", "test")
        mem.clear()
        assert len(mem.get_context()) == 0

    def test_to_llm_messages(self):
        mem = ConversationMemory()
        mem.add_message("user", "hello")
        mem.add_message("assistant", "hi")
        msgs = mem.to_llm_messages()
        assert len(msgs) == 2
        assert msgs[0] == {"role": "user", "content": "hello"}


class TestPlanModels:
    def test_plan_step(self):
        step = PlanStep(tool_name="slack.send_message", tool_args={"channel": "#test"}, description="send msg")
        assert step.tool_name == "slack.send_message"

    def test_action_plan(self):
        plan = ActionPlan(
            goal="Summarize PR",
            reasoning="User asked",
            steps=[PlanStep(tool_name="github.summarize_pull_request", tool_args={"repo": "org/repo", "pr_number": 42})],
        )
        assert len(plan.steps) == 1


class TestToolRegistry:
    def test_register_and_get(self):
        reg = ToolRegistry()
        func = lambda x: x
        reg.register("my.tool", func, "A test tool")
        assert reg.get_tool("my.tool") is func

    def test_get_missing_tool(self):
        reg = ToolRegistry()
        assert reg.get_tool("nonexistent") is None

    def test_list_tools(self):
        reg = ToolRegistry()
        reg.register("a", lambda: None, "tool a")
        reg.register("b", lambda: None, "tool b")
        assert sorted(reg.list_tools()) == ["a", "b"]


class TestLLMClient:
    def test_openai_provider(self, env_secrets):
        client = LLMClient()
        assert client._base_url == "https://api.openai.com/v1"
        assert client._model == "gpt-4o"


class TestToolCallPattern:
    def test_matches_tool_call_block(self):
        text = 'Some text\n```tool_call\n{"tool_name": "slack.send_message", "tool_args": {"channel": "#test"}}\n```\nMore text'
        matches = TOOL_CALL_PATTERN.findall(text)
        assert len(matches) == 1
        parsed = json.loads(matches[0].strip())
        assert parsed["tool_name"] == "slack.send_message"

    def test_no_match_on_plain_text(self):
        matches = TOOL_CALL_PATTERN.findall("Just a normal response.")
        assert len(matches) == 0


class TestOrchestrator:
    @pytest.fixture
    def orchestrator(self, env_secrets):
        with patch("agent.orchestrator.get_session") as mock_gs:
            mock_gs.return_value = MagicMock()
            orch = Orchestrator()
            return orch

    def test_register_tool(self, orchestrator):
        orchestrator.register_tool("test.tool", lambda: "ok", "A test")
        assert "test.tool" in orchestrator._registry.list_tools()

    @pytest.mark.asyncio
    async def test_handle_message_no_tool_call(self, orchestrator):
        with patch.object(orchestrator._llm, "chat", new_callable=AsyncMock) as mock_chat:
            mock_chat.return_value = "Here is your answer."
            response = await orchestrator.handle_message("What is 2+2?")
            assert response == "Here is your answer."
