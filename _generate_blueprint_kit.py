#!/usr/bin/env python3
"""Generate merged Blueprint templates (Normative + Instance in one file per artifact)."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "templates"

ARTIFACTS = [
    {
        "id": "1.1",
        "slug": "problem-definition",
        "name": "Problem Definition",
        "stage": "1 — Problem Definition",
        "short": "Defines the problem, who is blocked, barrier usecases, and desired outcomes",
        "purpose": "Define the problem as clearly as possible with full context. Include usecases where the problem blocks the user from moving forward.",
        "sections": [
            "Problem statement — clear definition with organizational or team context",
            "Barrier usecases — situations where the problem blocks progress",
            "Users — who feels the pain (primary and secondary where relevant)",
            "Desired outcomes — end-states",
            "Existing solutions gap",
            "Out of scope — explicit exclusions"
        ],
        "gate": [
            "Problem stated clearly?",
            "Users who feel the pain named?",
            "Organizational or team context stated?",
            "Desired outcomes are end-states only?",
            "Out of scope stated?",
            "Solution approach left unspecified?"
        ],
        "boundary": "Problem space.",
        "bridge": "→ Product Requirements Document (PRD).",
        "out": null
    },
    {
        "id": "1.2",
        "slug": "prd",
        "name": "Product Requirements Document (PRD)",
        "stage": "1 — Problem Definition",
        "short": "Commits to the product concept: goals, personas, workflows, features, FR/NFR, and binary success metrics mapped to the Problem Definition.",
        "purpose": "Commit to a product design concept. Translate PD into goals, personas, workflows, features, FR/NFR, assumptions/dependencies, and success metrics. Map each product goal to PD outcomes.",
        "sections": [
            "Product overview",
            "Organizational commitment (fund, scope, accept)",
            "Goals and objectives (mapped to PD)",
            "User personas",
            "User workflows",
            "Features",
            "Functional requirements (FR)",
            "Non-functional requirements (NFR)",
            "Assumptions and dependencies",
            "Success metrics — YES/NO questions with binary answers",
            "Out-of-scope"
        ],
        "gate": [
            "Product description, requirements, and organizational commitment stated?",
            "Goals stated as desired outcomes?",
            "Personas named?",
            "Workflows described at user level?",
            "Success metrics are YES/NO with binary answers?",
            "Every product goal maps to ≥1 PD problem/outcome?",
            "Both FR and NFR stated?",
            "Out-of-scope defined explicitly?"
        ],
        "boundary": "Product intent and requirements.",
        "bridge": "→ System Requirements Specification (SRS).",
        "out": null
    },
    {
        "id": "1.3",
        "slug": "srs",
        "name": "System Requirements Specification (SRS)",
        "stage": "1 — Problem Definition",
        "short": "Turns the PRD into testable system/technical requirements with platform categories, acceptance criteria, and traceability back to PD.",
        "purpose": "Turn PRD into precise, testable system/technical requirements. Each requirement traces to a PRD goal → PD. Consider each platform/integration category (require if applicable; N/A needs one-line justification): CI/CD; Deployment/runtime; Versioned deployable registry; IAM; VCS; Durable artifact storage; External integrations; Model/inference interface; Secrets store; Network/egress; Tenancy/isolation.",
        "sections": [
            "Technical platform and integration categories (each: requirement or N/A + justification)",
            "Interfaces and integration contracts",
            "Testable functional system requirements (trace to PRD goal)",
            "Testable non-functional system requirements (measurable; same trace)",
            "System constraints",
            "Assumptions and dependencies",
            "Acceptance criteria (pass/fail against built system)",
            "Scope and actors — thin: system boundary + actors as interfaces (PRD pointers)",
            "Traceability — SRS item → PRD goal → Problem Definition"
        ],
        "gate": [
            "Translates PRD goals into clear, buildable technical requirements?",
            "States testable system and technical requirements?",
            "Stakeholders and actors named?",
            "Functional requirements in testable engineering form?",
            "Non-functional requirements in testable engineering form?",
            "Constraints, assumptions, and acceptance criteria stated?",
            "Every platform/integration category considered (required or N/A + justification)?"
        ],
        "boundary": "Engineering contract: what the system must satisfy so design/build can begin.",
        "bridge": "Stage 1 exit (when set consistent) → Stage 2 Domain Model.",
        "out": null
    },
    {
        "id": "2.1",
        "slug": "domain-model",
        "name": "Domain Model",
        "stage": "2 — System Design",
        "short": "Shared conceptual ontology: entities, attributes, relationships, state, invariants, and domain events",
        "purpose": "Shared conceptual ontology of the problem domain. Grounds state, invariants, and events for TLA+.",
        "sections": [
            "Domain overview",
            "Core entities",
            "Entity attributes (conceptual)",
            "Relationships between entities",
            "System state",
            "Domain invariants",
            "Domain events"
        ],
        "gate": [
            "Shared conceptual ontology established?",
            "Core entities derived from SRS concepts?",
            "Attributes stated as domain meaning?",
            "Relationships defined?",
            "System state explicitly modeled?",
            "Domain invariants stated?",
            "Domain events stated?"
        ],
        "boundary": "Conceptual ontology.",
        "bridge": "→ Formal System Specification (TLA+) v1.",
        "out": "schemas, call catalogs, code, component diagrams, wire formats, TLA+ specs",
        "optional": "Domain operations / legal state transitions"
    },
    {
        "id": "2.2",
        "slug": "formal-system-specification-tla",
        "name": "Formal System Specification (TLA+)",
        "stage": "2 — System Design",
        "short": "Living cumulative Temporal Logic of Actions Spec with PASS evidence; verification backbone for stage-exit from Stage 2 onward.",
        "purpose": "Living cumulative checkable model in Temporal Logic of Actions. v1 formalizes Domain Model before Component Architecture. Later stages update and re-check the same Spec.",
        "sections": [
            "Specification overview — living cumulative model; named inputs; stage scope",
            "State variables",
            "Initial state",
            "Actions (state transitions)",
            "Safety properties",
            "Liveness properties",
            "System behavior specification (composed Spec)",
            "Model-checking configuration — tool, properties, finite bounds/assumptions",
            "Model-checking results — PASS evidence for this version under §8",
            "Version and stage-scope record — Spec version id; stage scope; later stages extend this Spec"
        ],
        "gate": [
            "TLA+ named and expanded (Temporal Logic of Actions) in usable form?",
            "Inputs named (Domain Model for v1; plus EG/other as applicable later)?",
            "State variables defined for this version's scope?",
            "Initial state specified?",
            "Actions specified for this version's scope?",
            "Properties to be checked stated?",
            "Verification approach stated?",
            "Contents §9 records PASS under §8 configuration?",
            "Version record states stage scope and that later dynamics extend this Spec?"
        ],
        "gate_hard": "FAIL ⇒ Gate NO. v1 PASS before Component Architecture. Stage 2+ exit needs Spec PASS for cumulative scope. EG acceptance needs Spec v2+ PASS for execution-layer scope.",
        "boundary": "Formal dynamics + PASS evidence; others reference Spec versions.",
        "bridge": "v1 PASS → Component Architecture; later PASS → stage-exit / EG acceptance.",
        "out": "Tool Contracts detail, prompts, CA diagrams, EG topology, schemas/APIs/code"
    },
    {
        "id": "2.3",
        "slug": "component-architecture",
        "name": "Component Architecture",
        "stage": "2 — System Design",
        "short": "Runtime structure: components, interfaces, stores/services, and reasoning points grounded in Domain Model and Spec PASS.",
        "purpose": "Concrete runtime structure from PRD+SRS, Domain Model, and accepted TLA+ property-set. Decide components, interfaces, stores/external services, and reasoning points.",
        "sections": [
            "Components — each cites PRD/SRS need(s), Domain Model ground(s), TLA+ property(ies)",
            "Interfaces between components (structure-level)",
            "Stores and external services",
            "Reasoning points"
        ],
        "gate": [
            "PRD and SRS used as paired inputs?",
            "Accepted Domain Model version named?",
            "Accepted TLA+ Spec version with PASS named?",
            "Components decided?",
            "Interfaces decided?",
            "Stores and external services decided?",
            "Reasoning points decided?"
        ],
        "gate_hard": "no Spec PASS ⇒ C3 NO.",
        "boundary": "Runtime structure and reasoning-point markers.",
        "bridge": "Completes Stage 2 → Stage 3 Tool Contracts.",
        "out": "agent roles, coordination protocols, Tool Contracts detail, prompts, schemas/code"
    },
    {
        "id": "3.1",
        "slug": "tool-contracts",
        "name": "Tool Contracts",
        "stage": "3 — Architecture Specification",
        "short": "Living inventory of call and attach capability contracts bound to Component Architecture pieces (no parallel registry).",
        "purpose": "Living inventory of capability contracts: what may be invoked, and what the agent binds/fills/configures on CA pieces and reasoning points. Sole capability inventory.",
        "sections": [
            "Capability overview",
            "Living capability inventory (sole named list; call + attach)",
            "Interface specification per entry",
            "Input validation rules",
            "Output / effect schema",
            "Access permissions",
            "Failure modes",
            "Invocation and binding policies",
            "Observability and logging"
        ],
        "gate": [
            "Accepted CA version named?",
            "Living inventory of capability contracts maintained?",
            "Inventory covers invoke + bind/fill/configure?",
            "Sole inventory (no parallel registry)?",
            "Each entry named/specified (interface, I/O, permissions, failures, policies)?",
            "Call and attach vocabulary decided?",
            "Each contract bound to CA pieces?"
        ],
        "boundary": "Call and attach capability surface.",
        "bridge": "→ Memory and Data Model.",
        "out": "CA structure diagrams, Domain Model ontology, ABS, TLA+ dynamics, prompts/code"
    },
    {
        "id": "3.2",
        "slug": "memory-and-data-model",
        "name": "Memory and Data Model",
        "stage": "3 — Architecture Specification",
        "short": "Persistence, schemas, access paths, context management, engineering/run artifact store, and caching obligations for Tool Contract data.",
        "purpose": "How the system holds/serves data Tool Contracts read/write, including caching obligations where used.",
        "sections": [
            "Memory architecture overview",
            "Data entities",
            "Data schemas",
            "Engineering and run artifact store",
            "Memory access patterns",
            "Context management (Domain Model grounded; windowed/bounded; injected into runs)",
            "Persistence strategy",
            "Data integrity rules",
            "Data lifecycle management",
            "Caching requirements (tiers; TTL; invalidation; allowed and disallowed; TC-aligned) — or explicit no-cache + justification"
        ],
        "gate": [
            "Accepted Tool Contracts version named?",
            "How data is held stated (entities, schemas, persistence including engineering/run artifact store)?",
            "How data is accessed stated (architecture, patterns, context with domain grounding)?",
            "Caching requirements stated (or explicit no-cache + justification)?"
        ],
        "boundary": "Data plane for Tool Contract reads and writes.",
        "bridge": "→ Execution Graph Specification.",
        "out": "TC detail, Domain Model ontology, CA topology, EG control flow, ABS/prompts/code, TLA+ dynamics, SRS deployable registry"
    },
    {
        "id": "3.3",
        "slug": "execution-graph-specification",
        "name": "Execution Graph Specification",
        "stage": "3 — Architecture Specification",
        "short": "Pictorial runtime control graph (nodes/edges/routing) referencing Spec v2+ PASS; places stores/caches and multi-repo context.",
        "purpose": "Pictorial runtime control graph from CA + Memory/Data Model. References Spec v2+ PASS for execution-layer properties.",
        "sections": [
            "Execution graph overview (named Spec version referenced)",
            "Graph nodes (CA; memory stores/caches; repo/project context; TC annotations)",
            "Graph edges (CA interfaces/relationships; routing; multi-repo/project crossings)",
            "Conditional routing (cache outcomes; repo/project selection)",
            "Execution state",
            "Execution termination conditions",
            "Execution observability"
        ],
        "gate": [
            "Accepted CA named?",
            "Accepted Memory and Data Model named?",
            "Accepted TLA+ Spec with PASS named (v2+, execution-layer scope)?",
            "Components appear as nodes?",
            "Edges reflect CA interfaces/relationships and routing?",
            "Memory stores/caches as interaction points; cache outcomes affect routing where applicable?",
            "Multi-repo/multi-project selection explicit in routing and execution state?",
            "Termination and observability specified?"
        ],
        "boundary": "Control-graph topology and routing.",
        "bridge": "→ Agent Architecture. Acceptance requires Spec PASS for execution-layer scope.",
        "out": "parallel execution model; error handling/recovery (later); TC schema detail; agent roles; formal Spec dynamics (referenced)"
    },
    {
        "id": "3.4",
        "slug": "agent-architecture",
        "name": "Agent Architecture (including Multi-Agent Coordination Protocol)",
        "stage": "3 — Architecture Specification",
        "short": "Places agents at reasoning points with roles, Multi-Agent Coordination Protocol, tool bindings, HITL tiers, and provider/routing architecture.",
        "purpose": "Place agents at CA reasoning points on the EG. Define roles, interaction, and Multi-Agent Coordination Protocol. Structural failure paths and HITL gates; detailed behavior deferred to Stage 4.",
        "sections": [
            "Architectural overview",
            "Agent roles",
            "Agent interaction model",
            "Multi-Agent Coordination Protocol (required)",
            "Reasoning model",
            "Context engineering architecture",
            "Model provider and routing architecture",
            "Inference control surface (allowed temperature/top_p ranges; defaults; override authority)",
            "Tool integration via Tool Contracts",
            "Memory architecture (agent-facing)",
            "Execution graph (agent-facing)",
            "Failure handling strategy (structural paths)",
            "Risk-tiered HITL gates",
            "Versioning and rollback for routing/context policy artifacts"
        ],
        "gate": [
            "Every CA reasoning point has an assigned agent role?",
            "Every role maps to a defined position on the agent-facing EG?",
            "Tool bindings per role limited to named Tool Contract entries?",
            "Risk-tiered HITL tiers cover every action class with repo-write, deploy, or external side effects?",
            "Rollback for routing/context policy artifacts defined so in-flight state is not orphaned?"
        ],
        "boundary": "Agent placement and coordination; prompts deferred to Agent Behavior Specification.",
        "bridge": "Completes Stage 3 → Stage 4 Agent Behavior Specification.",
        "out": "exact per-task temperature/top_p; detailed handoff dialogue (Stage 4); TC schema detail; EG redraw; memory persistence detail; Spec dynamics (referenced)"
    },
    {
        "id": "4.1",
        "slug": "agent-behavior-specification",
        "name": "Agent Behavior Specification",
        "stage": "4 — Behavioral Specification and Governance",
        "short": "System-prompt spine per role plus prompt-grounded policies for reasoning, tools, stop/escalate, and output validation.",
        "purpose": "How each agent role operates: system prompt spine per role plus reasoning, decision/tool policies, failure/stop rules, and inference defaults within AA envelopes.",
        "sections": [
            "Agent behavior overview (prompt vs companion policy)",
            "System prompts (per agent / per AA role)",
            "Reasoning framework",
            "Agent decision policy",
            "Tool selection strategy (only TC bound to role)",
            "Interaction protocol",
            "Reflection and self-correction",
            "Inference parameter defaults (within AA envelopes)",
            "Failure handling behavior",
            "Stopping conditions (when to stop or escalate)",
            "Output validation"
        ],
        "gate": [
            "Every AA role has a system prompt and matching prompt-grounded policy layers?",
            "Inference defaults stay within AA temperature/top_p envelopes?",
            "Tool selection uses only Tool Contracts bound to that role?",
            "Pause/stop/escalate rules respect AA risk-tiered HITL tiers?",
            "Output validation covers each role's declared outputs on the EG?"
        ],
        "boundary": "System prompts and prompt-grounded behavior; handoff mechanics → Escalation/HITL.",
        "bridge": "→ Escalation and Human-in-the-Loop Handoff Specification.",
        "out": "escalation handoff mechanics; governance policies; TC schemas; EG topology; Spec dynamics (referenced)"
    },
    {
        "id": "4.2",
        "slug": "escalation-hitl-handoff",
        "name": "Escalation and Human-in-the-Loop Handoff Specification",
        "stage": "4 — Behavioral Specification and Governance",
        "short": "Operable handoff protocol when autonomy stops: payload, human decisions, resume/timeouts, and escalation audit logging.",
        "purpose": "How a run hands off to a human when ABS stop/escalate rules fire against AA HITL gates. ABS decides when; this artifact decides how.",
        "sections": [
            "Escalation triggers (map from ABS + AA risk tiers)",
            "Handoff protocol (payload, channel, form)",
            "Human decision points and required responses",
            "Resume / continue rules after human input",
            "Timeouts and fallback if human does not respond",
            "Escalation logging mechanisms (what/where/who/retention)"
        ],
        "gate": [
            "Every AA risk-tiered HITL gate has a defined handoff path?",
            "Every ABS stop/escalate rule maps to a handoff or resume path?",
            "Handoff payload and required human responses stated?",
            "Resume/continue rules and timeouts/fallback stated?",
            "Escalation logging mechanisms stated?"
        ],
        "boundary": "Operable handoff mechanics for human checkpoints.",
        "bridge": "→ Governance and Safety Policies.",
        "out": "system prompts/full behavior policies; Policy-as-Code detail; TC schemas; system-wide Observability Plan"
    },
    {
        "id": "4.3",
        "slug": "governance-and-safety-policies",
        "name": "Governance and Safety Policies (including Policy-as-Code Bridge)",
        "stage": "4 — Behavioral Specification and Governance",
        "short": "Human-readable safety/governance rules plus Policy-as-Code Bridge, enforcement points, and SRC/EG change-control (hard six + conditional seventh).",
        "purpose": "Human-readable rules bounding autonomy and Policy-as-Code Bridge to machine-checkable controls. States hard-six (+ conditional seventh) change-control for SRC/EG under git.",
        "sections": [
            "Governance and safety policy statements (human-readable)",
            "Policy-as-Code Bridge (required)",
            "Enforcement points in lifecycle and runtime",
            "Audit, approval, and exception handling",
            "Alignment with enterprise compliance constraints"
        ],
        "gate": [
            "Human-readable governance/safety statements stated?",
            "Policy-as-Code Bridge maps statements to machine-checkable controls?",
            "Enforcement points named?",
            "Audit, approval, and exception paths stated?",
            "Policies encode Escalation/HITL protocol, decision points, resume/timeout, escalation audit?",
            "SRC-edit jurisdiction = hard six + git, plus conditional seventh (DA+Obs) for instrumentation/logging/observability tests?",
            "Living EG enrichment restricted to new EG versions under change-control?"
        ],
        "boundary": "Enforceable policy and change-control jurisdiction.",
        "bridge": "Completes Stage 4 → Stage 5 Implementation Plan.",
        "out": "Implementation Plan procedure detail; system prompts; EG redraw; TC schemas"
    },
    {
        "id": "5.1",
        "slug": "implementation-plan",
        "name": "Implementation Plan",
        "stage": "5 — Implementation, Deployment, and Validation",
        "short": "Engineering roadmap under Governance change-control: phases, repo structure, framework/platform integration, test/deploy/release.",
        "purpose": "Engineering roadmap under git versioning applying Governance change-control (hard six + conditional seventh).",
        "sections": [
            "Implementation overview",
            "Development phases",
            "Repository structure",
            "Core framework integration",
            "Cloud / platform integration",
            "Configuration management",
            "Testing strategy",
            "Deployment strategy",
            "Release strategy"
        ],
        "gate": [
            "Framework and platform integration paths stated?",
            "Testing, deployment, and release strategies stated?"
        ],
        "boundary": "Engineering roadmap under approved design.",
        "bridge": "→ Evaluation Plan and Failure Taxonomy.",
        "out": "Evaluation Plan and Failure Taxonomy detail; Observability dashboards"
    },
    {
        "id": "5.2",
        "slug": "evaluation-plan-and-failure-taxonomy",
        "name": "Evaluation Plan and Failure Taxonomy",
        "stage": "5 — Implementation, Deployment, and Validation",
        "short": "Merged evaluation case set/metrics/pass-fail rules with failure categories, severity, signals, and remediation owners.",
        "purpose": "How the system is judged and how failures are classified for accountable remediation.",
        "sections": [
            "Evaluation Plan — objectives",
            "Evaluation Plan — case set (coverage, inventory, labels, inclusion/exclusion, versioning/refresh)",
            "Evaluation Plan — metrics and thresholds",
            "Evaluation Plan — procedures and environments",
            "Evaluation Plan — pass/fail decision rules linked to case-set versions",
            "Failure Taxonomy — categories (reasoning, orchestration, tool, data, governance, operational)",
            "Failure Taxonomy — severity levels",
            "Failure Taxonomy — detectability and signals",
            "Failure Taxonomy — example instances",
            "Failure Taxonomy — mapping to remediation owners"
        ],
        "gate": null,
        "gate_note": "No separate YES/NO checklist. Accept when all required sections are complete, consistent with Implementation Plan sequencing, and the approver confirms.",
        "boundary": "Evaluation judgment and failure classification.",
        "bridge": "→ Simulation Scenarios.",
        "out": "Simulation Scenarios detail; Observability Plan dashboards"
    },
    {
        "id": "5.3",
        "slug": "simulation-scenarios",
        "name": "Simulation Scenarios",
        "stage": "5 — Implementation, Deployment, and Validation",
        "short": "Runnable adverse/recovery scenarios mapped to the Failure Taxonomy with setup, expected behavior, and pass criteria.",
        "purpose": "Runnable exercises that stress the system against the Evaluation Plan and Failure Taxonomy before deployment architecture is finalized.",
        "sections": [
            "Scenario inventory",
            "Mapping to Failure Taxonomy entries",
            "Setup and inputs",
            "Expected failure or recovery behavior",
            "Pass criteria for simulation runs"
        ],
        "gate": null,
        "gate_note": "No separate YES/NO checklist. Accept when sections are complete, scenarios exercise the case space/taxonomy, and the approver confirms.",
        "boundary": "Adverse/recovery scenarios before finalizing deployment architecture.",
        "bridge": "→ Deployment Architecture and Observability Plan.",
        "out": "Deployment Architecture topology; Observability Plan dashboards"
    },
    {
        "id": "5.4",
        "slug": "deployment-architecture-and-observability",
        "name": "Deployment Architecture and Observability Plan",
        "stage": "5 — Implementation, Deployment, and Validation",
        "short": "Merged runtime topology/environments with logs/traces/metrics, alerting, retention, and conditional EG/SRC enrichment for instrumentation.",
        "purpose": "Where the system runs and how runtime is visible/operable. May authorize EG/SRC enrichment for instrumentation under Governance change-control.",
        "sections": [
            "Deployment Architecture — runtime topology",
            "Deployment Architecture — environments (development, staging, production)",
            "Deployment Architecture — scaling and availability",
            "Deployment Architecture — security and access boundaries",
            "Deployment Architecture — rollback and release integration",
            "Observability Plan — logs, traces, and metrics inventory",
            "Observability Plan — instrumentation points across agents, tools, and graphs",
            "Observability Plan — alerting and escalation to operators",
            "Observability Plan — retention and audit access"
        ],
        "gate": null,
        "gate_note": "No separate YES/NO checklist. Accept when sections are complete, support proven simulation paths, and the approver confirms. Completing this artifact completes the Blueprint protocol when Stage 5's required set is consistent.",
        "boundary": "Runtime topology + observability controls (including conditional EG/SRC enrichment for instrumentation).",
        "bridge": "Blueprint protocol complete (Stage 5 exit on set consistency).",
        "out": null
    }
]


def template_md(a: dict) -> str:
    lines = [
        f"# {a['name']}",
        "",
        f"**Id:** `{a['id']}` · **Stage:** {a['stage']} · **Version:** `v0.1-DRAFT`",
        "",
        "## Normative",
        "",
        "### Purpose",
        a["purpose"],
        "",
        "### Required sections",
    ]
    for i, s in enumerate(a["sections"], 1):
        lines.append(f"{i}. {s}")
    if a.get("optional"):
        lines += ["", f"**Optional:** {a['optional']}"]
    if a.get("out"):
        lines += ["", f"**Excluded:** {a['out']}"]
    lines += ["", "### Acceptance gate"]
    if a.get("gate"):
        lines.append("All answers must be YES to approve:")
        for i, g in enumerate(a["gate"], 1):
            lines.append(f"{i}. {g}")
        if a.get("gate_hard"):
            lines += ["", f"**Hard rules:** {a['gate_hard']}"]
    else:
        lines.append(a.get("gate_note", "Approver confirms completeness."))
    lines += [
        "",
        "### Boundary",
        a["boundary"],
        "",
        "### Bridge",
        a["bridge"],
        "",
        "## Instance",
        "",
        "Mark gaps `[TBD]`. Fill from confirmed conversation answers only.",
        "",
        "### Purpose (project-specific)",
        "",
        "_…_",
        "",
        "### Contents",
        "",
    ]
    for s in a["sections"]:
        heading = s.split(" — ")[0].split(" (")[0]
        lines += [f"#### {heading}", "", f"<!-- {s} -->", "", "_…_", ""]
    if a.get("optional"):
        lines += ["#### Optional", "", f"<!-- {a['optional']} -->", "", "_…_", ""]
    lines += [
        "### Upstream inputs (accepted versions)",
        "",
        "| Artifact | Version |",
        "|---|---|",
        "| _name_ | _id_ |",
        "",
        "### Gate checklist",
        "",
    ]
    if a.get("gate"):
        for i, g in enumerate(a["gate"], 1):
            lines.append(f"- [ ] C{i}. {g}")
    else:
        lines.append(f"- [ ] Approver confirm: {a.get('gate_note', 'complete and consistent')}")
    lines += [
        "",
        "### Approval",
        "",
        "- Status: `DRAFT` | `ACCEPTED` | `REJECTED`",
        "- Approver:",
        "- Date:",
        "- Version id if accepted:",
        "",
    ]
    return "\n".join(lines)


def index_md() -> str:
    lines = [
        "# Blueprint kit index",
        "",
        "**Source repo:** https://github.com/raphranadoor/blueprint",
        "",
        "Each file under `templates/` embeds Normative requirements and an Instance block to fill.",
        "Copy `Agent Builder.agent.md` and `templates/` into a consumer repo under `.github/agents/`.",
        "",
        "| Id | Artifact | Template |",
        "|---|---|---|",
    ]
    for a in ARTIFACTS:
        base = f"{a['id']}-{a['slug']}.md"
        lines.append(f"| {a['id']} | {a['name']} | [`templates/{base}`](templates/{base}) |")
    lines += ["", "## Short descriptions", ""]
    for a in ARTIFACTS:
        lines.append(f"- **{a['id']} {a['name']}** — {a['short']}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    if TEMPLATES.exists():
        for p in TEMPLATES.glob("*.md"):
            p.unlink()
    else:
        TEMPLATES.mkdir(parents=True)
    rules = ROOT / "as-rules"
    if rules.exists():
        shutil.rmtree(rules)
    for a in ARTIFACTS:
        base = f"{a['id']}-{a['slug']}.md"
        (TEMPLATES / base).write_text(template_md(a), encoding="utf-8")
    (ROOT / "BLUEPRINT-KIT.md").write_text(index_md(), encoding="utf-8")
    print(f"Wrote {len(ARTIFACTS)} merged templates")


if __name__ == "__main__":
    main()
