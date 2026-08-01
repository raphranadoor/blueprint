# Blueprint kit index

**Source repo:** https://github.com/raphranadoor/blueprint

Each file under `templates/` embeds Normative requirements and an Instance block to fill.
Copy `Agent Builder.agent.md` and `templates/` into a consumer repo under `.github/agents/`.

| Id | Artifact | Template |
|---|---|---|
| 1.1 | Problem Definition | [`templates/1.1-problem-definition.md`](templates/1.1-problem-definition.md) |
| 1.2 | Product Requirements Document (PRD) | [`templates/1.2-prd.md`](templates/1.2-prd.md) |
| 1.3 | System Requirements Specification (SRS) | [`templates/1.3-srs.md`](templates/1.3-srs.md) |
| 2.1 | Domain Model | [`templates/2.1-domain-model.md`](templates/2.1-domain-model.md) |
| 2.2 | Formal System Specification (TLA+) | [`templates/2.2-formal-system-specification-tla.md`](templates/2.2-formal-system-specification-tla.md) |
| 2.3 | Component Architecture | [`templates/2.3-component-architecture.md`](templates/2.3-component-architecture.md) |
| 3.1 | Tool Contracts | [`templates/3.1-tool-contracts.md`](templates/3.1-tool-contracts.md) |
| 3.2 | Memory and Data Model | [`templates/3.2-memory-and-data-model.md`](templates/3.2-memory-and-data-model.md) |
| 3.3 | Execution Graph Specification | [`templates/3.3-execution-graph-specification.md`](templates/3.3-execution-graph-specification.md) |
| 3.4 | Agent Architecture (including Multi-Agent Coordination Protocol) | [`templates/3.4-agent-architecture.md`](templates/3.4-agent-architecture.md) |
| 4.1 | Agent Behavior Specification | [`templates/4.1-agent-behavior-specification.md`](templates/4.1-agent-behavior-specification.md) |
| 4.2 | Escalation and Human-in-the-Loop Handoff Specification | [`templates/4.2-escalation-hitl-handoff.md`](templates/4.2-escalation-hitl-handoff.md) |
| 4.3 | Governance and Safety Policies (including Policy-as-Code Bridge) | [`templates/4.3-governance-and-safety-policies.md`](templates/4.3-governance-and-safety-policies.md) |
| 5.1 | Implementation Plan | [`templates/5.1-implementation-plan.md`](templates/5.1-implementation-plan.md) |
| 5.2 | Evaluation Plan and Failure Taxonomy | [`templates/5.2-evaluation-plan-and-failure-taxonomy.md`](templates/5.2-evaluation-plan-and-failure-taxonomy.md) |
| 5.3 | Simulation Scenarios | [`templates/5.3-simulation-scenarios.md`](templates/5.3-simulation-scenarios.md) |
| 5.4 | Deployment Architecture and Observability Plan | [`templates/5.4-deployment-architecture-and-observability.md`](templates/5.4-deployment-architecture-and-observability.md) |

## Short descriptions

- **1.1 Problem Definition** — Defines the problem, who is blocked, barrier usecases, and desired outcomes
- **1.2 Product Requirements Document (PRD)** — Commits to the product concept: goals, personas, workflows, features, FR/NFR, and binary success metrics mapped to the Problem Definition.
- **1.3 System Requirements Specification (SRS)** — Turns the PRD into testable system/technical requirements with platform categories, acceptance criteria, and traceability back to PD.
- **2.1 Domain Model** — Shared conceptual ontology: entities, attributes, relationships, state, invariants, and domain events
- **2.2 Formal System Specification (TLA+)** — Living cumulative Temporal Logic of Actions Spec with PASS evidence; verification backbone for stage-exit from Stage 2 onward.
- **2.3 Component Architecture** — Runtime structure: components, interfaces, stores/services, and reasoning points grounded in Domain Model and Spec PASS.
- **3.1 Tool Contracts** — Living inventory of call and attach capability contracts bound to Component Architecture pieces (no parallel registry).
- **3.2 Memory and Data Model** — Persistence, schemas, access paths, context management, engineering/run artifact store, and caching obligations for Tool Contract data.
- **3.3 Execution Graph Specification** — Pictorial runtime control graph (nodes/edges/routing) referencing Spec v2+ PASS; places stores/caches and multi-repo context.
- **3.4 Agent Architecture (including Multi-Agent Coordination Protocol)** — Places agents at reasoning points with roles, Multi-Agent Coordination Protocol, tool bindings, HITL tiers, and provider/routing architecture.
- **4.1 Agent Behavior Specification** — System-prompt spine per role plus prompt-grounded policies for reasoning, tools, stop/escalate, and output validation.
- **4.2 Escalation and Human-in-the-Loop Handoff Specification** — Operable handoff protocol when autonomy stops: payload, human decisions, resume/timeouts, and escalation audit logging.
- **4.3 Governance and Safety Policies (including Policy-as-Code Bridge)** — Human-readable safety/governance rules plus Policy-as-Code Bridge, enforcement points, and SRC/EG change-control (hard six + conditional seventh).
- **5.1 Implementation Plan** — Engineering roadmap under Governance change-control: phases, repo structure, framework/platform integration, test/deploy/release.
- **5.2 Evaluation Plan and Failure Taxonomy** — Merged evaluation case set/metrics/pass-fail rules with failure categories, severity, signals, and remediation owners.
- **5.3 Simulation Scenarios** — Runnable adverse/recovery scenarios mapped to the Failure Taxonomy with setup, expected behavior, and pass criteria.
- **5.4 Deployment Architecture and Observability Plan** — Merged runtime topology/environments with logs/traces/metrics, alerting, retention, and conditional EG/SRC enrichment for instrumentation.
