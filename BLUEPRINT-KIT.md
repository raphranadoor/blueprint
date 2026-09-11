# Blueprint kit index

**Source repo:** https://github.com/raphranadoor/blueprint

Artifact clauses, prefixes, and acceptance gates match the Agent Engineering Blueprint catalogue in the thesis methods chapter.
Each file under `templates/` embeds Normative requirements and an Instance block to fill.
Copy `Agent Builder.agent.md` and `templates/` into a consumer repo under `.github/agents/`.

| Id | Artifact | Template |
|---|---|---|
| 1.1 | Problem Definition (PD) | [`templates/1.1-problem-definition.md`](templates/1.1-problem-definition.md) |
| 1.2 | Product Requirements Document (PRD) | [`templates/1.2-prd.md`](templates/1.2-prd.md) |
| 1.3 | System Requirements Specification (SRS) | [`templates/1.3-srs.md`](templates/1.3-srs.md) |
| 2.1 | Domain Model (DM) | [`templates/2.1-domain-model.md`](templates/2.1-domain-model.md) |
| 2.2 | Formal System Specification (SPEC) | [`templates/2.2-formal-system-specification-tla.md`](templates/2.2-formal-system-specification-tla.md) |
| 2.3 | Component Architecture (CA) | [`templates/2.3-component-architecture.md`](templates/2.3-component-architecture.md) |
| 3.1 | Tool Contracts (TC) | [`templates/3.1-tool-contracts.md`](templates/3.1-tool-contracts.md) |
| 3.2 | Memory and Data Model (MDM) | [`templates/3.2-memory-and-data-model.md`](templates/3.2-memory-and-data-model.md) |
| 3.3 | Execution Graph Specification (EG) | [`templates/3.3-execution-graph-specification.md`](templates/3.3-execution-graph-specification.md) |
| 3.4 | Agent Architecture (AA) | [`templates/3.4-agent-architecture.md`](templates/3.4-agent-architecture.md) |
| 4.1 | Agent Behavior Specification (ABS) | [`templates/4.1-agent-behavior-specification.md`](templates/4.1-agent-behavior-specification.md) |
| 4.2 | Escalation and Human-in-the-Loop Handoff Specification (HITL) | [`templates/4.2-escalation-hitl-handoff.md`](templates/4.2-escalation-hitl-handoff.md) |
| 4.3 | Governance and Safety Policies (GOV) | [`templates/4.3-governance-and-safety-policies.md`](templates/4.3-governance-and-safety-policies.md) |
| 5.1 | Implementation Plan (IP) | [`templates/5.1-implementation-plan.md`](templates/5.1-implementation-plan.md) |
| 5.2 | Evaluation (EVAL) | [`templates/5.2-evaluation-plan-and-failure-taxonomy.md`](templates/5.2-evaluation-plan-and-failure-taxonomy.md) |
| 5.3 | Simulation Scenarios (SIM) | [`templates/5.3-simulation-scenarios.md`](templates/5.3-simulation-scenarios.md) |
| 5.4 | Deployment Architecture and Observability Plan (DEP) | [`templates/5.4-deployment-architecture-and-observability.md`](templates/5.4-deployment-architecture-and-observability.md) |

## Short descriptions

- **1.1 Problem Definition (PD)** — States the problem, the background needed to understand it, and situations in which that problem blocks the user's progress. Stage 1 proceeds from a version that has passed PD-C1 through PD-C5.
- **1.2 Product Requirements Document (PRD)** — Turns the PD problem statement and desired outcomes into a committed product design. Each product goal traces to a PD problem or outcome.
- **1.3 System Requirements Specification (SRS)** — Turns the committed PRD design into testable system requirements. Each requirement traces to a PRD goal, and each goal traces to PD.
- **2.1 Domain Model (DM)** — Gives SRS concepts a common representation of the problem domain as entities, attributes, relationships, states, invariants, and events.
- **2.2 Formal System Specification (SPEC)** — Living cumulative TLA+ model of system dynamics, checked for the scope of each Spec version. Later stages extend or revise it and re-check PASS.
- **2.3 Component Architecture (CA)** — Defines the runtime components, interfaces, data sources, external services, and reasoning points. Linked to PRD, SRS, DM, and the PASS-recorded Spec.
- **3.1 Tool Contracts (TC)** — Evolving catalogue of named capability contracts used to invoke and configure tools for CA components and reasoning points.
- **3.2 Memory and Data Model (MDM)** — Defines how the system stores and provides the data consumed and produced by TC, including persistence, schemas, access routes, context, system state, and caching.
- **3.3 Execution Graph Specification (EG)** — Runtime control graph: CA components as nodes, interfaces and relations as edges, MDM stores and caches as interaction points, with TC capabilities and Spec PASS for execution-layer properties.
- **3.4 Agent Architecture (AA)** — Places agents on the Execution Graph at CA reasoning points, assigns TC capabilities to roles, and specifies coordination, reasoning, routing, memory views, rollback, failure handling, and human-in-the-loop controls.
- **4.1 Agent Behavior Specification (ABS)** — Defines how each AA role operates during a run: prompt, context, schema, capabilities, reasoning, decisions, EG interaction, reflection, failure handling, termination, validation, and model-parameter defaults.
- **4.2 Escalation and Human-in-the-Loop Handoff Specification (HITL)** — Defines when an agent run pauses for human intervention and how execution resumes: decision points, ABS triggers, handover procedure, resume, and timeouts.
- **4.3 Governance and Safety Policies (GOV)** — Sets the limits under which agents may act and turns HITL handover into enforceable policies, including change control for the Execution Graph and source code.
- **5.1 Implementation Plan (IP)** — Stage 5 plan for building, integrating, testing, and deploying the agent, with source-code change controlled in Git.
- **5.2 Evaluation (EVAL)** — Defines how the agent system is judged (Evaluation Plan) and how failures are classified when judgment fails (Failure Taxonomy).
- **5.3 Simulation Scenarios (SIM)** — Runnable exercises that stress the agent system against EVAL, mapped to Failure Taxonomy entries, with setup, expected behavior, and pass criteria.
- **5.4 Deployment Architecture and Observability Plan (DEP)** — Defines where the agent system runs and how that runtime is made visible and operable, including optional EG and source-code enrichment under GOV change-control.
