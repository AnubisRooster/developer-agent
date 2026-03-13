# Claw Agent — Architecture Diagrams

This document describes the architecture and data flows using Mermaid diagrams. Render in GitHub, VS Code (with Mermaid extension), or [mermaid.live](https://mermaid.live).

---

## 1. System Overview

```mermaid
flowchart TB
    subgraph External["External Services"]
        GH[GitHub]
        J[Jira]
        JK[Jenkins]
        SL[Slack]
        GM[Gmail]
    end

    subgraph ClawAgent["Claw Agent"]
        subgraph Entry["Entry Points"]
            CLI[CLI Chat]
            WH[Webhook Server]
        end

        subgraph Core["Core"]
            ORCH[Orchestrator]
            EB[Event Bus]
            WE[Workflow Engine]
        end

        subgraph Tools["Integrations"]
            SL_I[Slack]
            GH_I[GitHub]
            J_I[Jira]
            CF[Confluence]
            JK_I[Jenkins]
            GM_I[Gmail]
        end

        subgraph Persistence["Persistence"]
            DB[(SQLite)]
        end
    end

    User((User)) --> CLI
    CLI --> ORCH
    ORCH --> Tools

    GH -->|webhook| WH
    J -->|webhook| WH
    JK -->|webhook| WH
    SL -->|webhook| WH
    WH --> EB
    EB --> WE
    WE --> Tools
    EB --> DB
    WE --> DB
    ORCH --> DB
```

---

## 2. Component Diagram

```mermaid
flowchart LR
    subgraph Agent["agent/"]
        ORCH[Orchestrator]
        LLM[LLMClient]
        MEM[ConversationMemory]
        PLAN[Planner]
        REG[ToolRegistry]
    end

    subgraph Events["events/"]
        EB[EventBus]
        ET[AgentEvent]
    end

    subgraph Workflows["workflows/"]
        LOAD[Loader]
        ENG[WorkflowEngine]
    end

    subgraph Integrations["integrations/"]
        SL[slack]
        GH[github_integration]
        JI[jira_integration]
        CF[confluence]
        JK[jenkins]
        GM[gmail]
    end

    subgraph Data["database/"]
        MOD[models]
        SES[get_session]
    end

    subgraph Web["webhooks/"]
        APP[FastAPI app]
    end

    subgraph Security["security/"]
        SEC[secrets]
    end

    ORCH --> LLM
    ORCH --> MEM
    ORCH --> REG
    REG --> Integrations
    ORCH --> PLAN
    APP --> EB
    EB --> ENG
    ENG --> REG
    LOAD --> ENG
    EB --> MOD
    ENG --> MOD
    ORCH --> MOD
    SEC --> ORCH
    SEC --> Integrations
```

---

## 3. Webhook → Workflow Flow

```mermaid
sequenceDiagram
    participant GH as GitHub
    participant WH as Webhook Server
    participant EB as Event Bus
    participant DB as SQLite
    participant WE as Workflow Engine
    participant Slack as Slack Integration

    GH->>WH: POST /webhooks/github (pull_request.opened)
    WH->>WH: Verify signature (if secret set)
    WH->>EB: publish(AgentEvent)
    EB->>DB: Persist event
    EB->>WE: _handle_event (subscribed to trigger)
    WE->>WE: run_workflow(pr_opened)
    WE->> DB: Create WorkflowRun
    loop For each action
        WE->>Slack: github.summarize_pull_request
        Slack-->>WE: result
        WE->>Slack: slack.send_message
        Slack-->>WE: result
    end
    WE->>DB: Update WorkflowRun (completed)
    WH-->>GH: 200 OK
```

---

## 4. Chat Flow (Orchestrator)

```mermaid
sequenceDiagram
    participant User
    participant CLI as CLI Chat
    participant ORCH as Orchestrator
    participant MEM as ConversationMemory
    participant LLM as LLMClient
    participant DB as SQLite
    participant Tool as Integration

    User->>CLI: "Summarize PR #42 in org/repo"
    CLI->>ORCH: handle_message(msg)
    ORCH->>MEM: add_message("user", msg)
    ORCH->>MEM: to_llm_messages()
    ORCH->>LLM: chat(messages)

    alt LLM returns tool call
        LLM-->>ORCH: ```tool_call\n{"tool_name":"github.summarize_pull_request",...}
        ORCH->>ORCH: parse TOOL_CALL_PATTERN
        ORCH->>Tool: execute_tool(tool_name, tool_args)
        Tool-->>ORCH: result
        ORCH->>DB: ToolOutput (persist)
        ORCH->>MEM: add_message("user", "[Tool result]...")
        loop Until no more tool calls
            ORCH->>LLM: chat(messages)
            LLM-->>ORCH: response or tool_call
        end
    end

    LLM-->>ORCH: Final text response
    ORCH->>MEM: add_message("assistant", response)
    ORCH-->>CLI: response
    CLI-->>User: Display response
```

---

## 5. Event Bus (Pub/Sub)

```mermaid
flowchart TB
    subgraph Publishers["Publishers"]
        WH[Webhook Server]
    end

    subgraph EventBus["EventBus"]
        subgraph Subscribers["Subscribers by trigger"]
            S1["github.pull_request.opened"]
            S2["jira.issue.created"]
            S3["jenkins.build.failed"]
            S4["slack.*"]
        end
    end

    subgraph Handlers["Handlers"]
        WE[WorkflowEngine._handle_event]
    end

    WH -->|publish| EventBus
    EventBus -->|match trigger| S1
    EventBus -->|match trigger| S2
    EventBus -->|match trigger| S3
    S1 --> WE
    S2 --> WE
    S3 --> WE
    EventBus -->|persist| DB[(SQLite)]
```

---

## 6. Data Model

```mermaid
erDiagram
    Event {
        int id PK
        string event_type
        string source
        text payload
        datetime created_at
    }

    WorkflowRun {
        int id PK
        string workflow_name
        string trigger_event
        string status
        text result
        datetime started_at
        datetime finished_at
    }

    ToolOutput {
        int id PK
        string tool_name
        text input_data
        text output_data
        datetime created_at
    }

    CachedSummary {
        int id PK
        string key UK
        text summary
        datetime created_at
    }

    Event ||--o{ WorkflowRun : "triggers"
```

---

## 7. Supported Event Types

| Source   | Example triggers                          |
|----------|-------------------------------------------|
| GitHub   | `github.pull_request.opened`, `github.issues.opened` |
| Jira     | `jira.issue.created`, `jira.issue.updated` |
| Jenkins  | `jenkins.build.failed`, `jenkins.build.completed` |
| Slack    | `slack.message.received`, `slack.command.received` |

Workflows subscribe to these triggers via `workflows/*.yaml` `trigger` fields.
