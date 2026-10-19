# Graph Report - developer-agent  (2026-10-19)

## Corpus Check
- 54 files · ~50,474 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 4 file(s) not represented in the graph (top: .example 1, (none) 1, .jsonl 1)

## Summary
- 414 nodes · 820 edges · 24 communities (8 shown, 16 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- get_secrets()
- AgentEvent
- main.py
- orchestrator.py
- engine.py
- test_webhooks.py
- models.py
- ConversationMemory
- ToolRegistry
- graphify_pipeline.py
- confluence.py
- GmailIntegration
- GitHubIntegration
- JiraIntegration
- JenkinsIntegration

## God Nodes (most connected - your core abstractions)
1. `get_secrets()` - 32 edges
2. `AgentEvent` - 23 edges
3. `EventBus` - 18 edges
4. `ConversationMemory` - 16 edges
5. `WorkflowEngine` - 16 edges
6. `_build_orchestrator()` - 15 edges
7. `Orchestrator` - 14 edges
8. `GmailIntegration` - 14 edges
9. `ToolRegistry` - 13 edges
10. `GitHubIntegration` - 13 edges

## Surprising Connections (you probably didn't know these)
- `Orchestrator` --uses--> `ToolOutput`  [INFERRED]
  agent/orchestrator.py → database/models.py
- `TestOrchestrator` --uses--> `Orchestrator`  [INFERRED]
  tests/test_agent.py → agent/orchestrator.py
- `EventBus` --uses--> `Event`  [INFERRED]
  events/bus.py → database/models.py
- `WorkflowEngine` --uses--> `WorkflowRun`  [INFERRED]
  workflows/engine.py → database/models.py
- `TestWorkflowEngine` --uses--> `EventBus`  [INFERRED]
  tests/test_workflows.py → events/bus.py

## Import Cycles
- None detected.

## Communities (24 total, 16 thin omitted)

### Community 0 - "get_secrets()"
Cohesion: 0.06
Nodes (7): AppSecrets, get_secrets(), redact(), RedactingFilter, TestAppSecrets, TestRedact, TestRedactingFilter

### Community 1 - "AgentEvent"
Cohesion: 0.07
Nodes (12): EventBus, AgentEvent, EventSource, verify_webhook_signature(), TestAgentEvent, TestEventBus, TestVerifyWebhookSignature, github_webhook() (+4 more)

### Community 2 - "main.py"
Cohesion: 0.07
Nodes (12): Orchestrator, SlackIntegration, _agent_summarize(), _build_orchestrator(), chat(), cli(), run(), _setup_logging() (+4 more)

### Community 3 - "orchestrator.py"
Cohesion: 0.08
Nodes (7): LLMClient, ActionPlan, Planner, PlanStep, TestLLMClient, TestPlanModels, TestToolCallPattern

### Community 4 - "engine.py"
Cohesion: 0.11
Nodes (9): TestLoadWorkflow, TestWorkflowAction, TestWorkflowEngine, _is_coroutine(), WorkflowEngine, load_all_workflows(), load_workflow(), WorkflowAction (+1 more)

### Community 5 - "test_webhooks.py"
Cohesion: 0.08
Nodes (8): _chat_loop(), _print_banner(), start_chat(), TestCLIChat, client(), TestGitHubWebhook, TestHealthEndpoint, TestSlackWebhook

### Community 6 - "models.py"
Cohesion: 0.12
Nodes (12): Base, CachedSummary, Event, get_engine(), get_session(), ToolOutput, WorkflowRun, db_session() (+4 more)

### Community 7 - "ConversationMemory"
Cohesion: 0.11
Nodes (3): ConversationMemory, TestConversationMemory, TestOrchestrator

## Knowledge Gaps
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_secrets()` connect `get_secrets()` to `AgentEvent`, `main.py`, `orchestrator.py`, `test_webhooks.py`, `models.py`, `graphify_pipeline.py`, `confluence.py`, `GmailIntegration`, `GitHubIntegration`, `JiraIntegration`, `JenkinsIntegration`?**
  _High betweenness centrality (0.146) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `AgentEvent` (e.g. with `EventBus` and `TestAgentEvent`) actually correct?**
  _`AgentEvent` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Should `get_secrets()` be split into smaller, more focused modules?**
  _Cohesion score 0.05587808417997097 - nodes in this community are weakly interconnected._
- **Why does `Orchestrator` connect `main.py` to `ToolRegistry`, `orchestrator.py`, `models.py`, `ConversationMemory`?**
  _High betweenness centrality (0.089) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `EventBus` (e.g. with `Event` and `AgentEvent`) actually correct?**
  _`EventBus` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Should `AgentEvent` be split into smaller, more focused modules?**
  _Cohesion score 0.07329462989840348 - nodes in this community are weakly interconnected._
- **Why does `WorkflowEngine` connect `engine.py` to `AgentEvent`, `main.py`, `models.py`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._