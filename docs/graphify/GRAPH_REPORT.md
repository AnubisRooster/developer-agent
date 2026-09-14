# Graph Report - developer-agent  (2026-09-14)

## Corpus Check
- 54 files · ~67,136 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 4 file(s) not represented in the graph (top: .example 1, (none) 1, .jsonl 1)

## Summary
- 360 nodes · 636 edges · 30 communities (19 shown, 2 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 45 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- EventBus
- get_secrets()
- GitHubIntegration
- main.py
- models.py
- secrets.py
- ConversationMemory
- GmailIntegration
- test_agent.py
- ToolRegistry
- ConfluenceIntegration
- JiraIntegration
- ActionPlan
- JenkinsIntegration
- test_webhooks.py
- Planner
- Orchestrator
- Any
- conftest.py
- graphify_pipeline.py
- TestToolCallPattern

## God Nodes (most connected - your core abstractions)
1. `get_secrets()` - 32 edges
2. `AgentEvent` - 23 edges
3. `EventBus` - 18 edges
4. `ConversationMemory` - 16 edges
5. `WorkflowEngine` - 16 edges
6. `Orchestrator` - 14 edges
7. `GmailIntegration` - 14 edges
8. `_build_orchestrator()` - 14 edges
9. `ToolRegistry` - 13 edges
10. `GitHubIntegration` - 13 edges

## Surprising Connections (you probably didn't know these)
- `Orchestrator` --uses--> `ToolOutput`  [INFERRED]
  agent/orchestrator.py → database/models.py
- `EventBus` --uses--> `Event`  [INFERRED]
  events/bus.py → database/models.py
- `WorkflowEngine` --uses--> `WorkflowRun`  [INFERRED]
  workflows/engine.py → database/models.py
- `TestEventBus` --uses--> `EventBus`  [INFERRED]
  tests/test_events.py → events/bus.py
- `WorkflowEngine` --uses--> `AgentEvent`  [INFERRED]
  workflows/engine.py → events/types.py

## Import Cycles
- None detected.

## Communities (30 total, 2 thin omitted)

### Community 0 - "EventBus"
Cohesion: 0.07
Nodes (27): EventBus, Simple topic-based publish/subscribe event bus., Register a handler for a specific event type., Register a handler that receives every event., Publish an event — persists to DB and dispatches to subscribers., Write event to the local SQLite database., Path, Subscriber (+19 more)

### Community 1 - "get_secrets()"
Cohesion: 0.11
Nodes (26): Initialize client from secrets (provider, base_url, api_key)., Enum, AgentEvent, EventSource, BaseModel, Event type definitions for the internal event bus., Canonical event that flows through the internal bus., get (+18 more)

### Community 2 - "GitHubIntegration"
Cohesion: 0.09
Nodes (18): GitHubIntegration, Any, retry, GitHub integration using PyGithub., GitHub integration for issues, PRs, branches, and repository activity., Any, retry, Slack integration using slack_sdk WebClient. (+10 more)

### Community 3 - "main.py"
Cohesion: 0.09
Nodes (26): _chat_loop(), _print_banner(), Interactive CLI chat interface for the developer automation agent., start_chat(), command, group, _agent_summarize(), _build_orchestrator() (+18 more)

### Community 4 - "models.py"
Cohesion: 0.12
Nodes (20): Process a user message: add to memory, send to LLM, execute tools as needed.…, Look up tool, invoke it, store result in ToolOutput, return result string.…, Base, CachedSummary, Event, get_engine(), get_session(), SQLAlchemy models and database session management. (+12 more)

### Community 5 - "secrets.py"
Cohesion: 0.13
Nodes (13): BaseSettings, LogRecord, AppSecrets, Secure credential loading and redaction utilities., Logging filter that scrubs sensitive patterns from log records., Central secrets model — all values loaded from env vars / .env., Replace known secret patterns with <REDACTED>., redact() (+5 more)

### Community 6 - "ConversationMemory"
Cohesion: 0.12
Nodes (10): ConversationMemory, Any, Stores conversation history for the agent and provides context retrieval., Initialize empty conversation history., Add a message to the conversation history. Args: role: Message role (e.g.…, Return the most recent messages for context. Args: max_messages: Maximum number…, Return a one-line summary of the conversation so far. Returns: Brief summary…, Clear all conversation history. (+2 more)

### Community 7 - "GmailIntegration"
Cohesion: 0.25
Nodes (6): GmailIntegration, Any, retry, Gmail integration using google-api-python-client., Gmail integration for reading, sending, and summarizing emails., TestGmailIntegration

### Community 8 - "test_agent.py"
Cohesion: 0.23
Nodes (7): Conversation memory module for maintaining chat history and context., LLMClient, Main orchestrator — the brain of the Developer Automation Agent., Configurable LLM client supporting OpenRouter, OpenAI, and Ollama., Send messages to the LLM and return the assistant content. Args: messages: List…, Tests for agent/memory.py, agent/planner.py, agent/orchestrator.py., TestLLMClient

### Community 9 - "ToolRegistry"
Cohesion: 0.21
Nodes (6): Registry of available tools: name -> (callable, description)., Initialize empty registry., Return list of registered tool names., Return formatted string of all tool names and descriptions., ToolRegistry, TestToolRegistry

### Community 10 - "ConfluenceIntegration"
Cohesion: 0.27
Nodes (6): ConfluenceIntegration, Any, retry, Confluence integration using atlassian-python-api., Confluence integration for search, pages, and content., _strip_html()

### Community 11 - "JiraIntegration"
Cohesion: 0.29
Nodes (5): JiraIntegration, Any, retry, Jira integration using the jira Python SDK., Jira integration for tickets, updates, and remote links.

### Community 12 - "ActionPlan"
Cohesion: 0.31
Nodes (7): ActionPlan, PlanStep, BaseModel, Workflow planning module for decomposing user requests into tool steps., A single step in an action plan., Structured plan for executing a user request across multiple tool calls., TestPlanModels

### Community 13 - "JenkinsIntegration"
Cohesion: 0.29
Nodes (5): JenkinsIntegration, Any, retry, Jenkins integration using python-jenkins., Jenkins integration for triggering builds and fetching status/logs.

### Community 14 - "test_webhooks.py"
Cohesion: 0.20
Nodes (6): client(), fixture, Tests for webhooks/server.py., TestGitHubWebhook, TestHealthEndpoint, TestSlackWebhook

### Community 15 - "Planner"
Cohesion: 0.22
Nodes (6): Create LLMClient, Planner, ConversationMemory, and ToolRegistry., Planner, Any, Decomposes user requests into structured action plans using an LLM., Initialize the planner with an LLM client. Args: llm_client: Client with async…, Create an action plan from a user request using available tools. Args:…

### Community 16 - "Orchestrator"
Cohesion: 0.29
Nodes (5): Orchestrator, Main agent orchestrator: manages LLM, planner, memory, and tool execution., asyncio, fixture, TestOrchestrator

### Community 17 - "Any"
Cohesion: 0.29
Nodes (4): Any, Register a tool. Args: name: Unique tool name. func: Callable to invoke (sync…, Return the callable for the given tool name, or None., Delegate to ToolRegistry.

### Community 18 - "conftest.py"
Cohesion: 0.50
Nodes (4): env_secrets(), fixture, Shared fixtures for the test suite., _reset_secrets_cache()

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_secrets()` connect `get_secrets()` to `GitHubIntegration`, `main.py`, `models.py`, `secrets.py`, `GmailIntegration`, `test_agent.py`, `ConfluenceIntegration`, `JiraIntegration`, `JenkinsIntegration`, `test_webhooks.py`, `conftest.py`?**
  _High betweenness centrality (0.254) - this node is a cross-community bridge._
- **Why does `WorkflowEngine` connect `EventBus` to `get_secrets()`, `main.py`, `models.py`?**
  _High betweenness centrality (0.160) - this node is a cross-community bridge._
- **Why does `Orchestrator` connect `Orchestrator` to `main.py`, `models.py`, `ConversationMemory`, `test_agent.py`, `Planner`, `Any`?**
  _High betweenness centrality (0.152) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `AgentEvent` (e.g. with `EventBus` and `TestAgentEvent`) actually correct?**
  _`AgentEvent` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `EventBus` (e.g. with `Event` and `AgentEvent`) actually correct?**
  _`EventBus` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `ConversationMemory` (e.g. with `Orchestrator` and `TestConversationMemory`) actually correct?**
  _`ConversationMemory` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `WorkflowEngine` (e.g. with `TestWorkflowEngine` and `WorkflowRun`) actually correct?**
  _`WorkflowEngine` has 5 INFERRED edges - model-reasoned connections that need verification._