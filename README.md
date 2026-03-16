# AgentLoopGen 2.0

**AgentLoopGen** is an enterprise-grade AI Workflow Operating System designed to provide deterministic execution, stability enforcement, governance controls, and intelligent scaling for autonomous agent systems.

It acts as a runtime control layer for AI agents, ensuring reliability, containment, observability, and compliance in production environments.

## 🚀 Core Capabilities

- **Stability & Containment**: Deterministic state machine, loop stability engine, distributed circuit breaker, resource quotas, SLA-aware scheduler.
- **Durable Execution**: Persistent workflow engine, DB-backed retries, idempotent step processing, failure recovery & replay.
- **Observability & Audit**: Immutable telemetry ledger, session replay API, Prometheus metrics, risk heatmaps & stability scoring.
- **Governance & Control Plane**: Human approval system, policy-as-code engine, agent registry & lifecycle management, admin & audit APIs.
- **Predictive Scaling**: Dynamic worker auto-scaling, ML-based predictive load modeling, Kubernetes HPA integration.

## 🏗 Architecture

AgentLoopGen follows a modular architecture:

- **Kernel** → Orchestration Core
- **Stability Manager** → Containment Logic
- **Workflow Engine** → Durable Task Execution
- **Telemetry** → Event Ledger & Replay
- **Governance** → Human Oversight
- **Infrastructure** → Redis + PostgreSQL
- **API Layer** → External Interfaces

## 🛠 Tech Stack

- **FastAPI** – Async Python web framework
- **PostgreSQL** – Primary database (with asyncpg)
- **Redis** – Distributed caching, locks, pub/sub
- **Prometheus** – Metrics collection
- **Kubernetes** – Container orchestration & HPA
- **SQLAlchemy 1.4+** (async) – ORM
- **Alembic** – Migrations
- **Pydantic** – Settings & validation

## 📁 Repository Structure
