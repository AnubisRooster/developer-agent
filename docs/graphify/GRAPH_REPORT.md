# Graph Report - developer-agent  (2026-10-26)

## Corpus Check
- 54 files · ~51,326 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 4 file(s) not represented in the graph (top: .example 1, (none) 1, .jsonl 1)

## Summary
- 480 nodes · 882 edges · 26 communities (11 shown, 15 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- AgentEvent
- orchestrator.py
- get_secrets()
- main.py
- integrations
- test_webhooks.py
- models.py
- ToolRegistry
- test_workflows.py
- SlackIntegration
- confluence.py
- GitHubIntegration
- GmailIntegration
- build_failed.yaml
- jira_created.yaml
- pr_opened.yaml
- JiraIntegration

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
- `TestConversationMemory` --uses--> `ConversationMemory`  [INFERRED]
  tests/test_agent.py → agent/memory.py
- `_agent_summarize()` --calls--> `LLMClient`  [EXTRACTED]
  main.py → agent/orchestrator.py

## Import Cycles
- None detected.

## Communities (26 total, 15 thin omitted)

### Community 0 - "AgentEvent"
Cohesion: 0.05
Nodes (17): get_engine(), get_session(), EventBus, AgentEvent, EventSource, verify_webhook_signature(), TestAgentEvent, TestEventBus (+9 more)

### Community 1 - "orchestrator.py"
Cohesion: 0.05
Nodes (11): ConversationMemory, LLMClient, Orchestrator, ActionPlan, Planner, PlanStep, TestConversationMemory, TestLLMClient (+3 more)

### Community 2 - "get_secrets()"
Cohesion: 0.06
Nodes (7): AppSecrets, get_secrets(), redact(), RedactingFilter, TestAppSecrets, TestRedact, TestRedactingFilter

### Community 3 - "main.py"
Cohesion: 0.06
Nodes (12): JenkinsIntegration, _agent_summarize(), _build_orchestrator(), chat(), cli(), run(), _setup_logging(), _setup_workflow_engine() (+4 more)

### Community 4 - "integrations"
Cohesion: 0.06
Nodes (32): agent, log_file, log_level, name, version, enabled, database, url (+24 more)

### Community 5 - "test_webhooks.py"
Cohesion: 0.08
Nodes (8): _chat_loop(), _print_banner(), start_chat(), TestCLIChat, client(), TestGitHubWebhook, TestHealthEndpoint, TestSlackWebhook

### Community 6 - "models.py"
Cohesion: 0.16
Nodes (10): Base, CachedSummary, Event, ToolOutput, WorkflowRun, db_session(), TestCachedSummaryModel, TestEventModel (+2 more)

### Community 8 - "test_workflows.py"
Cohesion: 0.20
Nodes (6): TestLoadWorkflow, TestWorkflowAction, load_all_workflows(), load_workflow(), WorkflowAction, WorkflowDefinition

### Community 13 - "build_failed.yaml"
Cohesion: 0.18
Nodes (10): actions, args, description, on_failure, tool, channel, description, enabled (+2 more)

### Community 14 - "jira_created.yaml"
Cohesion: 0.18
Nodes (10): actions, args, description, on_failure, tool, channel, description, enabled (+2 more)

### Community 15 - "pr_opened.yaml"
Cohesion: 0.18
Nodes (10): actions, args, description, on_failure, tool, channel, description, enabled (+2 more)

## Knowledge Gaps
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_secrets()` connect `get_secrets()` to `AgentEvent`, `orchestrator.py`, `main.py`, `test_webhooks.py`, `models.py`, `SlackIntegration`, `confluence.py`, `GitHubIntegration`, `GmailIntegration`, `JiraIntegration`?**
  _High betweenness centrality (0.109) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `AgentEvent` (e.g. with `EventBus` and `TestAgentEvent`) actually correct?**
  _`AgentEvent` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Should `AgentEvent` be split into smaller, more focused modules?**
  _Cohesion score 0.05405405405405406 - nodes in this community are weakly interconnected._
- **Why does `Orchestrator` connect `orchestrator.py` to `main.py`, `models.py`, `ToolRegistry`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `EventBus` (e.g. with `Event` and `AgentEvent`) actually correct?**
  _`EventBus` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Should `orchestrator.py` be split into smaller, more focused modules?**
  _Cohesion score 0.053939714436805924 - nodes in this community are weakly interconnected._
- **Why does `WorkflowEngine` connect `AgentEvent` to `test_workflows.py`, `main.py`, `models.py`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._