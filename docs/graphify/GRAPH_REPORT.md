# Graph Report - developer-agent  (2026-10-05)

## Corpus Check
- 54 files · ~75,362 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 4 file(s) not represented in the graph (top: .example 1, (none) 1, .jsonl 1)

## Summary
- 414 nodes · 790 edges · 24 communities (8 shown, 16 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 45 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- AgentEvent
- main.py
- get_secrets()
- models.py
- test_agent.py
- GitHubIntegration
- test_security.py
- ConversationMemory
- graphify_pipeline.py
- confluence.py
- GmailIntegration
- chat.py
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

## Communities (24 total, 16 thin omitted)

### Community 0 - "AgentEvent"
Cohesion: 0.06
Nodes (13): EventBus, AgentEvent, TestAgentEvent, TestEventBus, TestLoadWorkflow, TestWorkflowAction, TestWorkflowEngine, _is_coroutine() (+5 more)

### Community 1 - "main.py"
Cohesion: 0.05
Nodes (15): LLMClient, Orchestrator, Planner, SlackIntegration, _agent_summarize(), _build_orchestrator(), chat(), cli() (+7 more)

### Community 3 - "get_secrets()"
Cohesion: 0.09
Nodes (13): EventSource, get_secrets(), verify_webhook_signature(), TestVerifyWebhookSignature, client(), TestGitHubWebhook, TestHealthEndpoint, TestSlackWebhook (+5 more)

### Community 4 - "models.py"
Cohesion: 0.11
Nodes (12): Base, CachedSummary, Event, get_engine(), get_session(), ToolOutput, WorkflowRun, db_session() (+4 more)

### Community 5 - "test_agent.py"
Cohesion: 0.08
Nodes (6): ToolRegistry, ActionPlan, PlanStep, TestPlanModels, TestToolCallPattern, TestToolRegistry

### Community 6 - "GitHubIntegration"
Cohesion: 0.13
Nodes (3): GitHubIntegration, TestGitHubIntegration, TestSlackIntegration

### Community 7 - "test_security.py"
Cohesion: 0.13
Nodes (6): AppSecrets, redact(), RedactingFilter, TestAppSecrets, TestRedact, TestRedactingFilter

### Community 12 - "chat.py"
Cohesion: 0.21
Nodes (4): _chat_loop(), _print_banner(), start_chat(), TestCLIChat

## Knowledge Gaps
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_secrets()` connect `get_secrets()` to `main.py`, `secrets.py`, `models.py`, `GitHubIntegration`, `test_security.py`, `graphify_pipeline.py`, `confluence.py`, `GmailIntegration`, `JiraIntegration`, `JenkinsIntegration`?**
  _High betweenness centrality (0.146) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `AgentEvent` (e.g. with `EventBus` and `TestAgentEvent`) actually correct?**
  _`AgentEvent` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Should `AgentEvent` be split into smaller, more focused modules?**
  _Cohesion score 0.05901639344262295 - nodes in this community are weakly interconnected._
- **Why does `Orchestrator` connect `main.py` to `ConversationMemory`, `secrets.py`, `models.py`, `test_agent.py`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `EventBus` (e.g. with `Event` and `AgentEvent`) actually correct?**
  _`EventBus` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Should `main.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05075187969924812 - nodes in this community are weakly interconnected._
- **Why does `WorkflowEngine` connect `AgentEvent` to `main.py`, `models.py`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._