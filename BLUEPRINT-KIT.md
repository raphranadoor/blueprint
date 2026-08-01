# Blueprint kit index

**Source repo:** https://github.com/raphranadoor/blueprint

Copy `Agent Builder.agent.md`, `as-rules/`, and `templates/` into a consumer repo under `.github/agents/`.
Agent Builder loads the rule for the current artifact, then fills the matching template from conversation answers.

| Id | Artifact | Rule | Template |
|---|---|---|---|
| 1.1 | Problem Definition | [`as-rules/1.1-problem-definition.md`](as-rules/1.1-problem-definition.md) | [`templates/1.1-problem-definition.md`](templates/1.1-problem-definition.md) |
| 1.2 | Product Requirements Document (PRD) | [`as-rules/1.2-prd.md`](as-rules/1.2-prd.md) | [`templates/1.2-prd.md`](templates/1.2-prd.md) |
| 1.3 | System Requirements Specification (SRS) | [`as-rules/1.3-srs.md`](as-rules/1.3-srs.md) | [`templates/1.3-srs.md`](templates/1.3-srs.md) |
| 2.1 | Domain Model | [`as-rules/2.1-domain-model.md`](as-rules/2.1-domain-model.md) | [`templates/2.1-domain-model.md`](templates/2.1-domain-model.md) |
| 2.2 | Formal System Specification (TLA+) | [`as-rules/2.2-formal-system-specification-tla.md`](as-rules/2.2-formal-system-specification-tla.md) | [`templates/2.2-formal-system-specification-tla.md`](templates/2.2-formal-system-specification-tla.md) |
| 2.3 | Component Architecture | [`as-rules/2.3-component-architecture.md`](as-rules/2.3-component-architecture.md) | [`templates/2.3-component-architecture.md`](templates/2.3-component-architecture.md) |
| 3.1 | Tool Contracts | [`as-rules/3.1-tool-contracts.md`](as-rules/3.1-tool-contracts.md) | [`templates/3.1-tool-contracts.md`](templates/3.1-tool-contracts.md) |
| 3.2 | Memory and Data Model | [`as-rules/3.2-memory-and-data-model.md`](as-rules/3.2-memory-and-data-model.md) | [`templates/3.2-memory-and-data-model.md`](templates/3.2-memory-and-data-model.md) |
| 3.3 | Execution Graph Specification | [`as-rules/3.3-execution-graph-specification.md`](as-rules/3.3-execution-graph-specification.md) | [`templates/3.3-execution-graph-specification.md`](templates/3.3-execution-graph-specification.md) |
| 3.4 | Agent Architecture (including Multi-Agent Coordination Protocol) | [`as-rules/3.4-agent-architecture.md`](as-rules/3.4-agent-architecture.md) | [`templates/3.4-agent-architecture.md`](templates/3.4-agent-architecture.md) |
| 4.1 | Agent Behavior Specification | [`as-rules/4.1-agent-behavior-specification.md`](as-rules/4.1-agent-behavior-specification.md) | [`templates/4.1-agent-behavior-specification.md`](templates/4.1-agent-behavior-specification.md) |
| 4.2 | Escalation and Human-in-the-Loop Handoff Specification | [`as-rules/4.2-escalation-hitl-handoff.md`](as-rules/4.2-escalation-hitl-handoff.md) | [`templates/4.2-escalation-hitl-handoff.md`](templates/4.2-escalation-hitl-handoff.md) |
| 4.3 | Governance and Safety Policies (including Policy-as-Code Bridge) | [`as-rules/4.3-governance-and-safety-policies.md`](as-rules/4.3-governance-and-safety-policies.md) | [`templates/4.3-governance-and-safety-policies.md`](templates/4.3-governance-and-safety-policies.md) |
| 5.1 | Implementation Plan | [`as-rules/5.1-implementation-plan.md`](as-rules/5.1-implementation-plan.md) | [`templates/5.1-implementation-plan.md`](templates/5.1-implementation-plan.md) |
| 5.2 | Evaluation Plan and Failure Taxonomy | [`as-rules/5.2-evaluation-plan-and-failure-taxonomy.md`](as-rules/5.2-evaluation-plan-and-failure-taxonomy.md) | [`templates/5.2-evaluation-plan-and-failure-taxonomy.md`](templates/5.2-evaluation-plan-and-failure-taxonomy.md) |
| 5.3 | Simulation Scenarios | [`as-rules/5.3-simulation-scenarios.md`](as-rules/5.3-simulation-scenarios.md) | [`templates/5.3-simulation-scenarios.md`](templates/5.3-simulation-scenarios.md) |
| 5.4 | Deployment Architecture and Observability Plan | [`as-rules/5.4-deployment-architecture-and-observability.md`](as-rules/5.4-deployment-architecture-and-observability.md) | [`templates/5.4-deployment-architecture-and-observability.md`](templates/5.4-deployment-architecture-and-observability.md) |

## Short descriptions

- **1.1 Problem Definition** — Defines the problem, who is blocked, barrier usecases, and solution-neutral outcomes — without presupposing an agent or product.
- **1.2 Product Requirements Document (PRD)** — Commits to the product concept: goals, personas, workflows, features, FR/NFR, and binary success metrics mapped to the Problem Definition.
- **1.3 System Requirements Specification (SRS)** — Turns the PRD into testable system/technical requirements with platform categories, acceptance criteria, and traceability back to PD.
- **2.1 Domain Model** — Shared conceptual ontology: entities, attributes, relationships, state, invariants, and domain events — not implementation schema.
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
