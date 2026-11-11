# Realtime Voice AI Platform

A production-oriented real-time voice AI platform built with Python and LiveKit.

The current version establishes the real-time conversational foundation: microphone audio is streamed through speech recognition, semantic turn detection, LLM reasoning, and text-to-speech before being returned to the user as spoken audio.

The project is being developed incrementally toward a fault-tolerant voice AI platform with tool execution, provider failover, persistent state, observability, and telephony support.

## Current Version

**v0.1 — Real-Time Voice Foundation**

Current conversation pipeline:

```text
User Microphone
      ↓
LiveKit Real-Time Audio
      ↓
Audio Enhancement
      ↓
AssemblyAI STT
      ↓
Semantic Turn Detection
      ↓
Gemma LLM
      ↓
Fish Audio TTS
      ↓
LiveKit Audio Output
      ↓
User
```

## Current Features

- Real-time microphone-based voice conversations
- Streaming speech-to-text
- LLM-based conversational reasoning
- Streaming text-to-speech
- Semantic turn detection
- Preemptive response generation
- Audio enhancement and background-noise reduction
- Automatic session greeting
- Persistent agent identity
- Voice-oriented prompt design
- Domain-specific STT keyterms
- Expressive speech generation
- LiveKit Cloud integration
- Conversation transcripts and session traces
- Automated prompt contract tests with Pytest
- Ruff linting and formatting
- Docker configuration
- GitHub Actions workflows
- LiveKit conversation simulation support

## Agent Identity

The assistant identifies itself as:

> Anurag's Voice Agent

The agent is instructed to maintain a consistent identity throughout the conversation and to identify Anurag Mahajan as its creator when asked.

Prompt configuration is separated from runtime orchestration so behavior can be maintained and tested independently.

## Architecture

```text
                   ┌──────────────────────┐
                   │        User          │
                   │     Microphone       │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │       LiveKit        │
                   │   Real-Time Audio    │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │  Audio Enhancement   │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │      AssemblyAI      │
                   │         STT          │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │   Turn Detection     │
                   │ + Preemptive Gen.    │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │        Gemma         │
                   │         LLM          │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │     Fish Audio       │
                   │         TTS          │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │       LiveKit        │
                   │    Audio Output      │
                   └──────────┬───────────┘
                              │
                              ▼
                           User
```

## Technology Stack

### Core

- Python 3.14
- LiveKit Agents
- LiveKit Cloud
- LiveKit Inference

### Speech-to-Text

- AssemblyAI Universal-3-6-Pro

### Language Model

- Google Gemma 4 31B IT

### Text-to-Speech

- Fish Audio S2.1 Pro

### Voice Processing

- LiveKit semantic turn detection
- LiveKit AI Acoustics audio enhancement
- Preemptive generation
- STT keyterm detection

### Engineering

- uv
- Pytest
- Ruff
- Docker
- GitHub Actions

## Project Structure

```text
realtime-voice-ai-platform/
│
├── .github/
│   ├── assets/
│   └── workflows/
│       ├── ruff.yml
│       └── simulations.yml
│
├── src/
│   ├── __init__.py
│   ├── agent.py
│   └── prompts.py
│
├── tests/
│   └── test_prompts.py
│
├── .dockerignore
├── .env.example
├── .gitignore
├── .python-version
├── Dockerfile
├── Makefile
├── README.md
├── pyproject.toml
├── scenarios.yaml
└── uv.lock
```

### `src/agent.py`

Contains the real-time application orchestration:

- LiveKit agent server
- Agent session configuration
- STT configuration
- LLM configuration
- TTS configuration
- turn handling
- audio enhancement
- session lifecycle

### `src/prompts.py`

Contains the LLM behavior configuration:

- agent identity
- creator identity
- conversational style
- reliability rules
- automatic greeting instructions

Keeping prompts separate from runtime code makes the system easier to maintain, test, and evolve.

### `tests/test_prompts.py`

Contains contract tests that protect important prompt behavior such as:

- agent identity
- creator identity
- greeting identity

## Getting Started

### 1. Install dependencies

This project uses `uv` for Python dependency management.

```bash
uv sync
```

### 2. Configure LiveKit

Authenticate with LiveKit:

```bash
lk cloud auth
```

Create your local environment configuration:

```bash
lk app env --write --destination .env.local
```

The local environment file is excluded from version control.

The public `.env.example` contains only the required variable names:

```text
LIVEKIT_URL=
LIVEKIT_API_KEY=
LIVEKIT_API_SECRET=
```

Never commit real API credentials.

### 3. Run the agent

Start the development worker:

```bash
lk agent dev
```

The agent can then be accessed through the LiveKit Agent Console.

## Development Commands

Install dependencies:

```bash
make install
```

Run the development agent:

```bash
make dev
```

Run tests:

```bash
make test
```

Run linting:

```bash
make lint
```

Format the codebase:

```bash
make format
```

Run the full local quality gate:

```bash
make check
```

Equivalent commands can also be run directly:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest -v
```

## Testing

The current automated test suite includes prompt contract tests.

Run:

```bash
uv run pytest -v
```

The project also contains `scenarios.yaml` for full conversational simulations through LiveKit.

Run simulations locally with:

```bash
lk agent simulate text --scenarios scenarios.yaml
```

The GitHub simulation workflow requires LiveKit credentials to be configured as repository secrets before cloud simulations can run successfully.

## Code Quality

Ruff is used for linting and formatting.

Lint:

```bash
uv run ruff check .
```

Formatting check:

```bash
uv run ruff format --check .
```

## Security

Secrets are intentionally kept outside version control.

The project ignores local environment configuration such as:

```text
.env.local
```

Only `.env.example` is committed.

Production credentials should be supplied through environment variables or an appropriate secrets-management system.

## Roadmap

### Phase 1 — Real-Time Voice Foundation

- [x] Real-time audio
- [x] Speech-to-text
- [x] LLM reasoning
- [x] Text-to-speech
- [x] Semantic turn detection
- [x] Preemptive generation
- [x] Audio enhancement
- [x] Agent identity and greeting
- [x] Prompt separation
- [x] Basic automated testing

### Phase 2 — Tool Execution

- [ ] Structured function/tool calling
- [ ] Order-status lookup
- [ ] Support-ticket creation
- [ ] Appointment operations
- [ ] Human-agent escalation

### Phase 3 — Backend and State

- [ ] FastAPI service layer
- [ ] PostgreSQL persistence
- [ ] Redis caching/session state
- [ ] Conversation persistence
- [ ] Tool-call history

### Phase 4 — Reliability

- [ ] Multi-provider STT fallback
- [ ] Multi-provider LLM fallback
- [ ] Multi-provider TTS fallback
- [ ] Provider health tracking
- [ ] Retry policies
- [ ] Failure recovery

### Phase 5 — Observability

- [ ] Structured application logging
- [ ] STT latency measurements
- [ ] LLM time-to-first-token
- [ ] TTS time-to-first-audio
- [ ] End-to-end response latency
- [ ] Tool-call latency
- [ ] Provider failure metrics
- [ ] OpenTelemetry
- [ ] Prometheus
- [ ] Grafana dashboards

### Phase 6 — Production Engineering

- [ ] Expanded automated test suite
- [ ] Load testing
- [ ] Failure-injection testing
- [ ] Performance benchmarks
- [ ] Production deployment configuration

### Phase 7 — Telephony

- [ ] SIP integration
- [ ] Inbound phone calls
- [ ] Call routing
- [ ] Human transfer
- [ ] Production call workflows

## Design Goals

This project is intentionally being developed beyond a simple voice-chat demo.

The long-term focus is on:

- low conversational latency
- reliable turn-taking
- provider fault tolerance
- safe tool execution
- persistent conversation state
- observability
- measurable performance
- production-oriented architecture

## Status

The current release establishes the real-time voice foundation.

Tool execution, persistence, provider failover, production observability, and SIP telephony are planned future milestones and are not represented as completed functionality.