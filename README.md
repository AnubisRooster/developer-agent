# Claw Agent — Developer Automation Agent

A local AI developer automation agent that integrates with Slack, GitHub, Jira, Confluence, Jenkins, and Gmail. Uses a direct LLM client (OpenRouter, OpenAI, or Ollama) for reasoning and SQLite for persistence.

## Features

- **Interactive chat** — Natural-language requests via CLI
- **Webhook server** — Receives events from GitHub, Jira, Jenkins, Slack
- **Event-driven workflows** — YAML-defined automations triggered by webhooks
- **Tool registry** — Extensible tools for each integration
- **LLM support** — OpenRouter, OpenAI, or Ollama

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CLAW AGENT                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│  CLI Chat          Webhook Server (FastAPI)                                 │
│  ┌──────────┐      ┌─────────────────────────────────────────────────────┐  │
│  │ User     │      │ /webhooks/github  /webhooks/jira                     │  │
│  │ Input    │      │ /webhooks/jenkins /webhooks/slack                     │  │
│  └────┬─────┘      └─────────────────────┬───────────────────────────────┘  │
│       │                                  │                                  │
│       ▼                                  ▼                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    Orchestrator (LLM + Tool Registry)                │   │
│  │  LLMClient (OpenRouter/OpenAI/Ollama)  │  ToolRegistry                │   │
│  └───────────────────────────────────────┬─────────────────────────────┘   │
│                                          │                                  │
│       ┌──────────────────────────────────┼────────────────────────────────┐ │
│       ▼                                  ▼                                ▼ │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  EventBus  ┌─────────────────────┐ │
│  │ Slack   │  │ GitHub  │  │ Jira    │  ◄────────►  │ WorkflowEngine      │ │
│  │ Gmail   │  │ Jenkins │  │Confluence│             │ (YAML workflows)    │ │
│  └─────────┘  └─────────┘  └─────────┘             └─────────────────────┘ │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  SQLite (events, workflow_runs, tool_outputs, cached_summaries)      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

See [docs/architecture.md](docs/architecture.md) for detailed diagrams.

---

## Install

### Prerequisites

- Python 3.10+
- pip or uv

### 1. Clone and enter the project

```bash
cd developer-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

For development and tests:

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

### 4. Configure environment

```bash
cp .env.example .env
# Edit .env with your API keys and tokens
```

Required for basic chat:

- `OPENCLAW_PROVIDER` — `openrouter` | `openai` | `ollama`
- `OPENCLAW_API_KEY` — API key for the chosen provider
- `OPENCLAW_MODEL` — Model identifier (e.g. `gpt-4o`, `openai/gpt-4o`)

Optional integrations (add tokens to enable tools):

- Slack: `SLACK_BOT_TOKEN`
- GitHub: `GITHUB_TOKEN`
- Jira: `JIRA_URL`, `JIRA_USER`, `JIRA_API_TOKEN`
- Confluence: `CONFLUENCE_URL`, `CONFLUENCE_USER`, `CONFLUENCE_API_TOKEN`
- Jenkins: `JENKINS_URL`, `JENKINS_USER`, `JENKINS_API_TOKEN`
- Gmail: `GMAIL_CREDENTIALS_FILE`, `GMAIL_TOKEN_FILE` (OAuth flow)

### 5. Initialize the database

The database is created automatically on first run. Ensure the `data/` directory exists if using the default SQLite path:

```bash
mkdir -p data
```

---

## Usage

### Interactive chat

```bash
python main.py chat
```

Type natural-language requests. The agent will call tools (Slack, GitHub, etc.) as needed. Type `/quit` to exit.

### Webhook server

Start the server to receive webhooks from GitHub, Jira, Jenkins, and Slack:

```bash
python main.py webhook-server
# Or: python main.py run
```

Default: `http://0.0.0.0:8080`

Configure webhook URLs in each service:

- **GitHub**: Settings → Webhooks → Add webhook → `https://your-host:8080/webhooks/github`
- **Jira**: Settings → System → WebHooks → `https://your-host:8080/webhooks/jira`
- **Jenkins**: Job → Configure → Build Triggers → Generic Webhook Trigger
- **Slack**: Event Subscriptions → Request URL `https://your-host:8080/webhooks/slack`

### Health check

```bash
curl http://localhost:8080/health
```

---

## Project structure

```
developer-agent/
├── main.py              # CLI entry (chat, webhook-server, run)
├── agent/               # Orchestrator, LLM client, memory, planner
├── cli/                 # Interactive chat UI
├── database/            # SQLAlchemy models, SQLite session
├── events/              # Event bus, event types
├── integrations/        # Slack, GitHub, Jira, Confluence, Jenkins, Gmail
├── security/            # Secrets, redaction, webhook verification
├── webhooks/            # FastAPI webhook endpoints
├── workflows/           # YAML workflow definitions + engine
├── tests/
├── docs/                # Architecture diagrams
└── requirements.txt
```

---

## Workflows

Workflows are YAML files in `workflows/`. Each defines a trigger and a sequence of tool calls.

Example (`workflows/pr_opened.yaml`):

```yaml
name: pr_opened_workflow
trigger: github.pull_request.opened
description: When a PR is opened — summarize it and post to Slack.
enabled: true

actions:
  - tool: github.summarize_pull_request
    description: Summarize the pull request
  - tool: slack.send_message
    args:
      channel: "#dev-notifications"
    on_failure: continue
```

---

## Tests

```bash
pip install -r requirements-dev.txt
python -m pytest tests/ -v
```

---

## License

Internal use. See your organization's policy.
