"""Tests for events/types.py and events/bus.py."""

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from events.types import AgentEvent, EventSource


class TestAgentEvent:
    def test_create_event(self):
        event = AgentEvent(event_type="github.pull_request.opened", source=EventSource.GITHUB, payload={"pr": 123})
        assert event.event_type == "github.pull_request.opened"
        assert event.source == EventSource.GITHUB
        assert event.id
        assert event.timestamp

    def test_all_event_sources(self):
        sources = [s.value for s in EventSource]
        assert "github" in sources
        assert "jira" in sources
        assert "slack" in sources


class TestEventBus:
    @pytest.fixture
    def bus(self):
        from events.bus import EventBus
        return EventBus()

    @pytest.mark.asyncio
    async def test_subscribe_and_publish(self, bus):
        handler = AsyncMock()
        bus.subscribe("test.event", handler)
        event = AgentEvent(event_type="test.event", source=EventSource.SYSTEM)
        with patch("events.bus.get_session") as mock_session:
            mock_session.return_value = MagicMock()
            await bus.publish(event)
        handler.assert_called_once_with(event)

    @pytest.mark.asyncio
    async def test_no_match(self, bus):
        handler = AsyncMock()
        bus.subscribe("other.event", handler)
        event = AgentEvent(event_type="test.event", source=EventSource.SYSTEM)
        with patch("events.bus.get_session") as mock_session:
            mock_session.return_value = MagicMock()
            await bus.publish(event)
        handler.assert_not_called()
