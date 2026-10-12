# Graph Report - developer-agent  (2026-10-12)

## Corpus Check
- 54 files · ~75,604 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 4 file(s) not represented in the graph (top: .example 1, (none) 1, .jsonl 1)

## Summary
- 414 nodes · 811 edges · 22 communities (9 shown, 13 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 66 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- ConversationMemory
- AgentEvent
- get_secrets()
- EventBus
- main.py
- GitHubIntegration
- orchestrator.py
- models.py
- graphify_pipeline.py
- GmailIntegration
- test_security.py
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

## Communities (22 total, 13 thin omitted)

### Community 0 - "ConversationMemory"
Cohesion: 0.06
Nodes (6): ConversationMemory, Orchestrator, ToolRegistry, TestConversationMemory, TestOrchestrator, TestToolRegistry

### Community 1 - "AgentEvent"
Cohesion: 0.07
Nodes (15): AgentEvent, EventSource, verify_webhook_signature(), TestAgentEvent, TestEventBus, TestVerifyWebhookSignature, client(), TestGitHubWebhook (+7 more)

### Community 2 - "get_secrets()"
Cohesion: 0.06
Nodes (5): ConfluenceIntegration, _strip_html(), AppSecrets, get_secrets(), TestAppSecrets

### Community 3 - "EventBus"
Cohesion: 0.07
Nodes (10): EventBus, TestLoadWorkflow, TestWorkflowAction, TestWorkflowEngine, _is_coroutine(), WorkflowEngine, load_all_workflows(), load_workflow() (+2 more)

### Community 4 - "main.py"
Cohesion: 0.08
Nodes (10): SlackIntegration, _agent_summarize(), _build_orchestrator(), chat(), cli(), run(), _setup_logging(), _setup_workflow_engine() (+2 more)

### Community 5 - "GitHubIntegration"
Cohesion: 0.08
Nodes (7): _chat_loop(), _print_banner(), start_chat(), GitHubIntegration, TestCLIChat, TestGitHubIntegration, TestSlackIntegration

### Community 6 - "orchestrator.py"
Cohesion: 0.09
Nodes (7): LLMClient, ActionPlan, Planner, PlanStep, TestLLMClient, TestPlanModels, TestToolCallPattern

### Community 7 - "models.py"
Cohesion: 0.14
Nodes (12): Base, CachedSummary, Event, get_engine(), get_session(), ToolOutput, WorkflowRun, db_session() (+4 more)

### Community 10 - "test_security.py"
Cohesion: 0.22
Nodes (4): redact(), RedactingFilter, TestRedact, TestRedactingFilter

## Knowledge Gaps
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_secrets()` connect `get_secrets()` to `AgentEvent`, `main.py`, `GitHubIntegration`, `orchestrator.py`, `models.py`, `graphify_pipeline.py`, `GmailIntegration`, `test_security.py`, `JiraIntegration`, `JenkinsIntegration`?**
  _High betweenness centrality (0.146) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `AgentEvent` (e.g. with `EventBus` and `TestAgentEvent`) actually correct?**
  _`AgentEvent` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Should `ConversationMemory` be split into smaller, more focused modules?**
  _Cohesion score 0.0573025856044724 - nodes in this community are weakly interconnected._
- **Why does `Orchestrator` connect `ConversationMemory` to `main.py`, `orchestrator.py`, `models.py`?**
  _High betweenness centrality (0.091) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `EventBus` (e.g. with `Event` and `AgentEvent`) actually correct?**
  _`EventBus` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Should `AgentEvent` be split into smaller, more focused modules?**
  _Cohesion score 0.06894049346879536 - nodes in this community are weakly interconnected._
- **Why does `WorkflowEngine` connect `EventBus` to `AgentEvent`, `main.py`, `models.py`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._