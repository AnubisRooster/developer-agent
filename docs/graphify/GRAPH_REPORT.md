# Graph Report - developer-agent  (2026-09-28)

## Corpus Check
- 54 files · ~75,373 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 4 file(s) not represented in the graph (top: .example 1, (none) 1, .jsonl 1)

## Summary
- 414 nodes · 776 edges · 23 communities (14 shown, 9 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 45 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- secrets.py
- AgentEvent
- test_agent.py
- main.py
- test_webhooks.py
- get_secrets()
- models.py
- ToolRegistry
- graphify_pipeline.py
- GmailIntegration
- GitHubIntegration
- ConfluenceIntegration
- JiraIntegration
- JenkinsIntegration

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
- `TestAgentEvent` --uses--> `EventSource`  [INFERRED]
  tests/test_events.py → events/types.py
- `TestEventBus` --uses--> `EventSource`  [INFERRED]
  tests/test_events.py → events/types.py

## Import Cycles
- None detected.

## Communities (23 total, 9 thin omitted)

### Community 0 - "secrets.py"
Cohesion: 0.05
Nodes (48): Conversation memory module for maintaining chat history and context., Main orchestrator — the brain of the Developer Automation Agent., Planner, Any, Workflow planning module for decomposing user requests into tool steps., Decomposes user requests into structured action plans using an LLM., Initialize the planner with an LLM client. Args: llm_client: Client with async…, asyncio (+40 more)

### Community 1 - "AgentEvent"
Cohesion: 0.06
Nodes (36): EventBus, Simple topic-based publish/subscribe event bus., Register a handler for a specific event type., Register a handler that receives every event., Publish an event — persists to DB and dispatches to subscribers., Write event to the local SQLite database., AgentEvent, BaseModel (+28 more)

### Community 2 - "test_agent.py"
Cohesion: 0.06
Nodes (25): ConversationMemory, Any, Stores conversation history for the agent and provides context retrieval., Initialize empty conversation history., Add a message to the conversation history. Args: role: Message role (e.g.…, Return the most recent messages for context. Args: max_messages: Maximum number…, Return a one-line summary of the conversation so far. Returns: Brief summary…, Clear all conversation history. (+17 more)

### Community 3 - "main.py"
Cohesion: 0.07
Nodes (31): Orchestrator, Main agent orchestrator: manages LLM, planner, memory, and tool execution., click, command, dotenv, Any, retry, Slack integration for messaging and channel history. (+23 more)

### Community 4 - "test_webhooks.py"
Cohesion: 0.06
Nodes (28): _chat_loop(), _print_banner(), Interactive CLI chat interface for the developer automation agent., start_chat(), click_testing, fastapi_testclient, group, cli() (+20 more)

### Community 5 - "get_secrets()"
Cohesion: 0.09
Nodes (26): BaseSettings, Enum, EventSource, LogRecord, post, Request, AppSecrets, get_secrets() (+18 more)

### Community 6 - "models.py"
Cohesion: 0.12
Nodes (21): Process a user message: add to memory, send to LLM, execute tools as needed.…, Look up tool, invoke it, store result in ToolOutput, return result string.…, Base, CachedSummary, Event, get_engine(), get_session(), SQLAlchemy models and database session management. (+13 more)

### Community 7 - "ToolRegistry"
Cohesion: 0.13
Nodes (10): Any, Registry of available tools: name -> (callable, description)., Initialize empty registry., Register a tool. Args: name: Unique tool name. func: Callable to invoke (sync…, Return the callable for the given tool name, or None., Return list of registered tool names., Return formatted string of all tool names and descriptions., Delegate to ToolRegistry. (+2 more)

### Community 8 - "graphify_pipeline.py"
Cohesion: 0.12
Nodes (15): graphify_analyze, graphify_build, graphify_cluster, graphify_detect, graphify_export, graphify_extract, graphify_llm, graphify_report (+7 more)

### Community 9 - "GmailIntegration"
Cohesion: 0.31
Nodes (5): GmailIntegration, Any, retry, Gmail integration for reading, sending, and summarizing emails., TestGmailIntegration

### Community 10 - "GitHubIntegration"
Cohesion: 0.27
Nodes (5): GitHubIntegration, Any, retry, GitHub integration for issues, PRs, branches, and repository activity., TestGitHubIntegration

### Community 11 - "ConfluenceIntegration"
Cohesion: 0.33
Nodes (5): ConfluenceIntegration, Any, retry, Confluence integration for search, pages, and content., _strip_html()

### Community 12 - "JiraIntegration"
Cohesion: 0.39
Nodes (4): JiraIntegration, Any, retry, Jira integration for tickets, updates, and remote links.

### Community 13 - "JenkinsIntegration"
Cohesion: 0.39
Nodes (4): JenkinsIntegration, Any, retry, Jenkins integration for triggering builds and fetching status/logs.

## Knowledge Gaps
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_secrets()` connect `get_secrets()` to `secrets.py`, `test_agent.py`, `main.py`, `test_webhooks.py`, `models.py`, `graphify_pipeline.py`, `GmailIntegration`, `GitHubIntegration`, `ConfluenceIntegration`, `JiraIntegration`, `JenkinsIntegration`?**
  _High betweenness centrality (0.154) - this node is a cross-community bridge._
- **Why does `Orchestrator` connect `main.py` to `secrets.py`, `test_agent.py`, `models.py`, `ToolRegistry`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Why does `WorkflowEngine` connect `AgentEvent` to `main.py`, `models.py`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `AgentEvent` (e.g. with `EventBus` and `TestAgentEvent`) actually correct?**
  _`AgentEvent` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `EventBus` (e.g. with `Event` and `AgentEvent`) actually correct?**
  _`EventBus` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `ConversationMemory` (e.g. with `Orchestrator` and `TestConversationMemory`) actually correct?**
  _`ConversationMemory` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `secrets.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05499735589635114 - nodes in this community are weakly interconnected._