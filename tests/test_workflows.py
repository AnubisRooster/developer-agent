"""Tests for workflows/loader.py and workflows/engine.py."""

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from workflows.loader import WorkflowAction, WorkflowDefinition, load_all_workflows, load_workflow


class TestWorkflowAction:
    def test_defaults(self):
        action = WorkflowAction(tool="slack.send_message")
        assert action.args == {}
        assert action.on_failure == "stop"


class TestLoadWorkflow:
    def test_load_valid_yaml(self, tmp_path):
        yaml_content = """
name: test_workflow
trigger: github.pull_request.opened
description: Test workflow
enabled: true
actions:
  - tool: github.summarize_pull_request
    description: Summarize PR
  - tool: slack.send_message
    args:
      channel: "#dev"
    on_failure: continue
"""
        f = tmp_path / "test.yaml"
        f.write_text(yaml_content)
        wf = load_workflow(f)
        assert wf.name == "test_workflow"
        assert wf.trigger == "github.pull_request.opened"
        assert len(wf.actions) == 2


class TestWorkflowEngine:
    @pytest.fixture
    def engine(self):
        from events.bus import EventBus
        from workflows.engine import WorkflowEngine
        bus = EventBus()
        engine = WorkflowEngine(bus=bus, workflow_dir="workflows")
        return engine, bus

    def test_load_registers_triggers(self, engine):
        eng, bus = engine
        with patch("workflows.engine.get_session") as mock_gs:
            mock_gs.return_value = MagicMock()
            eng.load()
        assert len(bus._subscribers) > 0

    def test_register_tool(self, engine):
        eng, _ = engine
        eng.register_tool("test", lambda: "ok")
        assert "test" in eng._tool_registry
