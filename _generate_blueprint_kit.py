#!/usr/bin/env python3
"""Generate merged Blueprint templates (Normative + Instance in one file per artifact).

Source of truth: latex-thesis/thesis.tex Chapter 3 artifact catalogue
(clauses, PREFIX-C⟨n⟩ gates, Spec PASS, stage names).
"""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "templates"

S1 = "1 — Problem and requirements"
S2 = "2 — Domain and structure"
S3 = "3 — Tools, memory, and graph"
S4 = "4 — Behavior, handoff, and policy"
S5 = "5 — Build, simulate, and deploy"


def sec(name, text, diagram=False):
    return {"name": name, "text": text, "diagram": diagram}


ARTIFACTS = [
    {
        "id": "1.1",
        "slug": "problem-definition",
        "prefix": "PD",
        "name": "Problem Definition (PD)",
        "stage": S1,
        "short": "States the problem, the background needed to understand it, and situations in which that problem blocks the user's progress. Stage 1 proceeds from a version that has passed PD-C1 through PD-C5.",
        "purpose": "Problem Definition (PD) states the problem to be solved, the background required to understand it, and situations in which that problem blocks the user's progress. PD is the first artifact of the Blueprint, and Stage 1 proceeds from a version that has passed PD-C1 through PD-C5.",
        "sections": [
            sec("Problem statement", "the current problem and the organizational or team setting in which it occurs."),
            sec("Barrier use cases", "instances in which the problem blocks the user's progress in the project or in development."),
            sec("Users", "primary users who experience the problem, and secondary users where they are relevant."),
            sec("Desired outcomes", "solution-neutral end-states for what should be better."),
            sec("Existing solutions gap", "what already exists and why it is insufficient for this problem."),
            sec("Out of scope", "the bounds of this problem."),
        ],
        "gate": [
            "Is the problem specified independently of a decision to build an agent, a system, or a product?",
            "Are the users who experience the problem named, including who is blocked or harmed by it?",
            "Is the organizational or team setting stated, and is the problem plausibly solvable with available resources?",
            "Are the desired outcomes specified as solution-neutral end-states for what should be better?",
            "Are the bounds of this problem specified?",
        ],
        "boundary": "Understand the problem without presupposing a solution.",
        "bridge": "→ Product Requirements Document (PRD).",
    },
    {
        "id": "1.2",
        "slug": "prd",
        "prefix": "PRD",
        "name": "Product Requirements Document (PRD)",
        "stage": S1,
        "short": "Turns the PD problem statement and desired outcomes into a committed product design. Each product goal traces to a PD problem or outcome.",
        "purpose": "Product Requirements Document (PRD) turns the PD problem statement and desired outcomes into a committed product design. It defines the offering and the requirements against which the engineering handoff can be tested. Each product goal traces to a PD problem or outcome.",
        "sections": [
            sec("Product overview", "designated product offering, the users who interact with it, and the value created for those users."),
            sec("Organizational commitment", "the funding, scope, and acceptance the organization commits to for this product."),
            sec("Goals and objectives", "desired outcomes, each mapped to a PD problem or outcome."),
            sec("User personas", "roles, responsibilities, motivations, and typical tasks."),
            sec("User workflows", "the interaction sequences through which users work with the product."),
            sec("Features", "the capabilities the product offers to users."),
            sec("Functional requirements (FR)", "the functions the product must perform."),
            sec("Quality attributes and constraints", "the quality attributes and constraints under which the product must operate."),
            sec("Assumptions and dependencies", "assumptions the design treats as given (a user population, a delivery channel, or a regulatory envelope) and external dependencies it requires (another system, a vendor, or a data source)."),
            sec("Success metrics", "success checks as YES/NO questions with a direct binary answer (whether a stated goal is met, or whether a named constraint holds)."),
            sec("Out-of-scope", "product capabilities and claims outside this design's scope (a capability that is not funded, a user group that is not served, or a claim the organization does not accept)."),
        ],
        "gate": [
            "Can a named offering, the requirements it must satisfy, and the fund-scope-accept bound each be read as an inspectable statement that is not only implied?",
            "Can each persona be identified as a user of the offering from role, responsibilities, motivations, and typical tasks?",
            "Can every user workflow be carried out as a user flow without a system procedure making up for a missing step?",
            "Can each product goal be paired with a named PD problem or a named PD outcome?",
            "Can each FR be read as a function the product must perform, and can each quality attribute and constraint be read as an operating bound?",
        ],
        "boundary": "Product intent and requirements, not engineering design.",
        "bridge": "→ System Requirements Specification (SRS).",
    },
    {
        "id": "1.3",
        "slug": "srs",
        "prefix": "SRS",
        "name": "System Requirements Specification (SRS)",
        "stage": S1,
        "short": "Turns the committed PRD design into testable system requirements. Each requirement traces to a PRD goal, and each goal traces to PD.",
        "purpose": "System Requirements Specification (SRS) turns the committed PRD design into testable system requirements. It sets the engineering conditions for implementation, including the interfaces, platform choices, constraints, assumptions, and pass/fail conditions. Each requirement traces to a PRD goal, and each goal traces to PD.",
        "sections": [
            sec(
                "Technical platform and integration categories",
                "for each applicable category, the requirement, or N/A with a one-line justification: Automated build and promotion (CI/CD); Deployment / runtime method; Versioned deployable registry; Machine identity + least privilege through Identity and Access Management (IAM); Version-control system (VCS) as the source of truth; Durable object storage for artifacts; External system integrations; Model / inference interface; Secrets / credential store; Network / egress control; Tenancy / isolation.",
            ),
            sec("Interfaces and integration contracts", "for example, an API with another system, an inference endpoint, or a credential-store protocol."),
            sec("Testable functional system requirements", "each traced to a PRD goal, which capture system inputs and the operations and responses for normal and abnormal cases."),
            sec("Testable non-functional system requirements", "measurable, each traced to a PRD goal (for example, performance, usability, or a reliability bound)."),
            sec("System constraints and limits", "that the implementation must respect (for example, a mandated standard or a hardware bound)."),
            sec("Assumptions and dependencies", "the implementation treats as given (for example, a runtime, a vendor API, or a data source)."),
        ],
        "gate": [
            "Can each PRD goal be paired with a technical requirement that states what the system must satisfy?",
            "Can each functional requirement be read as system inputs and the operations and responses for normal and abnormal cases?",
            "Can each non-functional requirement be read as a measurable bound?",
            "Can each system constraint be named as a limit the implementation has to obey?",
            "Can each assumption or dependency be named as a given the implementation is counting on?",
        ],
        "boundary": "Engineering contract: what the system must satisfy so design and build can begin.",
        "bridge": "Stage 1 exit (when the Stage 1 set is consistent) → Stage 2 Domain Model (DM). First Spec PASS is required after DM (R3).",
    },
    {
        "id": "2.1",
        "slug": "domain-model",
        "prefix": "DM",
        "name": "Domain Model (DM)",
        "stage": S2,
        "short": "Gives SRS concepts a common representation of the problem domain as entities, attributes, relationships, states, invariants, and events.",
        "purpose": "Domain Model (DM) gives the SRS concepts a common representation of the problem domain. It provides terms and relationships that domain experts, system-building agents, and agents within the system can use consistently. DM then expresses those concepts as the entities, attributes, relationships, states, invariants, and events of the system.",
        "sections": [
            sec("Domain overview", "a description of the domain, including the problem domain that this ontology represents, its boundaries, and the knowledge of the domain used by the system."),
            sec("Core entities", "the identifiable object types of the domain ontology, whose instances persist across state change.", diagram=True),
            sec("Entity attributes", "the characterizing properties of each core entity as they hold in the domain."),
            sec("Relationships between entities", "the named associations that hold among core entities.", diagram=True),
            sec("System state", "the configuration of entity instances and their attribute values at a moment.", diagram=True),
            sec("Domain invariants", "properties that must hold in every valid system state."),
            sec("Domain events", "named occurrences that change system state, or that record that a change occurred, and the states in which each occurrence is enabled.", diagram=True),
        ],
        "gate": [
            "Can each of the named concepts have the same interpretation for the experts, the agents constructing the system, and the agents that are part of the system?",
            "Can each core entity be paired with a specific SRS concept?",
            "Can each entity attribute be read as a characterizing property as it holds in the domain?",
            "Can each relationship be read as a named association that holds among core entities?",
            "Can system state be read as the configuration of entity instances and their attribute values at a moment?",
        ],
        "boundary": "Domain ontology shared by experts and agents.",
        "bridge": "→ Formal System Specification (SPEC). First mandatory Spec PASS follows this artifact (R3).",
    },
    {
        "id": "2.2",
        "slug": "formal-system-specification-tla",
        "prefix": "SPEC",
        "name": "Formal System Specification (SPEC)",
        "stage": S2,
        "short": "Living cumulative TLA+ model of system dynamics, checked for the scope of each Spec version. Later stages extend or revise it and re-check PASS.",
        "purpose": "Formal System Specification (SPEC) is the living cumulative model of system dynamics, written in Temporal Logic of Actions (TLA+) and checked for the scope of each Spec version. SPEC translates Domain Model state, invariants, and domain events into variables, an initial state, actions, and safety and liveness properties. Each later stage extends or revises the Spec, which is then checked against the cumulative scope covered by that version.",
        "sections": [
            sec("Version scope", "the actions allowable according to this version of the specification's formula, the dynamics left unaccounted for, and the artifacts assumed from the predecessor."),
            sec("State variables", "variables that represent the state in the current version of this specification."),
            sec("Initial state", "the state variable assignment that will allow the behavior of this Spec version to start taking place."),
            sec("Actions", "the next-state relations of this Spec version."),
            sec("Safety properties", "the states that no behavior admitted by this Spec version may enter."),
            sec("Liveness properties", "a condition that a behavior admitted by this Spec version must exhibit eventually."),
            sec("Configuration for model checking", "the model checker, the properties being verified, and the finite ranges in which the present version of Spec is analyzed."),
            sec("Model checking results", "PASS or FAIL for the current version of Spec with respect to the selected configuration."),
            sec("Version record", "the code for this version of the specification and the stage range it covers."),
        ],
        "gate": None,
        "gate_note": "The TLA+ of the present Spec version runs under the stated configuration and records PASS.",
        "gate_hard": "FAIL ⇒ Gate NO. v1 PASS before Component Architecture. From Stage 2 onwards, a stage exits only when the Spec covering its cumulative scope records PASS (R3, R4).",
        "boundary": "Formal dynamics plus PASS evidence. Other artifacts refer to the latest validated Spec version (R4).",
        "bridge": "v1 PASS → Component Architecture (CA). Later PASS → stage-exit / later artifact acceptance.",
    },
    {
        "id": "2.3",
        "slug": "component-architecture",
        "prefix": "CA",
        "name": "Component Architecture (CA)",
        "stage": S2,
        "short": "Defines the runtime components, interfaces, data sources, external services, and reasoning points. Linked to PRD, SRS, DM, and the PASS-recorded Spec.",
        "purpose": "Component Architecture (CA) defines the runtime components, interfaces, data sources, external services, and reasoning points that make up the system. Its structure must satisfy PRD and SRS requirements, respect Domain Model concepts, and remain linked to the PASS-recorded Spec.",
        "sections": [
            sec("Components", "the runtime parts of this architecture, each related to a PRD or SRS requirement, a Domain Model concept, and a property of the Spec version that records PASS.", diagram=True),
            sec("Interfaces", "the interfaces those components possess."),
            sec("Data sources and external services", "the data sources and external services on which those components depend."),
            sec("Reasoning points", "the points at which agent logic is anchored (if it is needed)."),
        ],
        "gate": [
            "Can each component be related to a PRD or SRS requirement, a Domain Model concept, and a property of the Spec version that records PASS?",
            "Can each interface be read as belonging to the components it connects, and can each data source and external service be read as a dependency of those components?",
            "Can each stated reasoning point be read as a point at which agent logic is anchored?",
        ],
        "gate_hard": "The TLA+ of the present Spec version is updated to include this runtime architecture and records PASS. Once the PASS is recorded, the process proceeds to the next stage and artifact.",
        "boundary": "Runtime arrangement and reasoning-point markers.",
        "bridge": "Completes Stage 2 → Stage 3 Tool Contracts (TC).",
    },
    {
        "id": "3.1",
        "slug": "tool-contracts",
        "prefix": "TC",
        "name": "Tool Contracts (TC)",
        "stage": S3,
        "short": "Evolving catalogue of named capability contracts used to invoke and configure tools for CA components and reasoning points.",
        "purpose": "Tool Contracts (TC) is the evolving catalogue of named capability contracts used to invoke and configure tools for CA components and reasoning points. Each contract defines its call and attachment vocabulary, interface, inputs, outputs, permissions, failure behavior, and policies. TC binds each contract to the CA components that use it and records the corresponding calls and attachments.",
        "sections": [
            sec("Catalog scope", "the invocation capabilities and the filling and configuring commitments on CA components and reasoning points."),
            sec("Capability catalog", "the named list of contracts in this TC version, with the call vocabulary and the attachment vocabulary."),
            sec("Contract fields", "the interface, input, output, permissions, failures, and policies of each contract."),
            sec("Component binding", "the CA components each contract connects to."),
            sec("Observability", "what is recorded for call and attach."),
        ],
        "gate": [
            "Can the catalog scope be read as invocation capabilities and as filling and configuring commitments on CA components and reasoning points?",
            "Can each contract in the named list be identified with its call vocabulary and its attachment vocabulary?",
            "Can each contract be read as stating its interface, input, output, permissions, failures, and policies, and can it be connected to the CA components relevant to its capabilities?",
        ],
        "boundary": "Capability surface (call and attach) bound to CA.",
        "bridge": "→ Memory and Data Model (MDM). Spec PASS covering the TC catalog is recorded together with the MDM data plane.",
    },
    {
        "id": "3.2",
        "slug": "memory-and-data-model",
        "prefix": "MDM",
        "name": "Memory and Data Model (MDM)",
        "stage": S3,
        "short": "Defines how the system stores and provides the data consumed and produced by TC, including persistence, schemas, access routes, context, system state, and caching.",
        "purpose": "Memory and Data Model (MDM) defines how the system stores and provides the data consumed and produced by TC across components and nodes. It anchors stored entities in the Domain Model and records the persistence, schemas, access routes, transformations, context, system state, and caching rules that govern that data. When caching is used, MDM specifies what may be cached, for how long, and how consistency with the actual data store is maintained.",
        "sections": [
            sec("Data model at components and nodes", "the data model as described for each component and each node.", diagram=True),
            sec("Transformation rules", "the rules that transform between those models."),
            sec("Persistence", "the persistence mechanism of the data TC consumes and produces."),
            sec("Schemas", "the schema definition of those stored entities."),
            sec("Access routes", "the access routes by which TC consumes and produces that data."),
            sec("Context", "the context assembled for a run, anchored in the Domain Model."),
            sec("System state", "how system state is stored and provided."),
            sec("Caching", "what may be cached, for how long, and how cached access stays consistent with the actual data store (if caching is used)."),
        ],
        "gate": None,
        "gate_note": "The TLA+ of the present Spec version is updated to include the TC catalog and this data plane and records PASS. Once the PASS is recorded, the process proceeds to the next artifact.",
        "boundary": "Data plane for TC reads and writes.",
        "bridge": "→ Execution Graph Specification (EG).",
    },
    {
        "id": "3.3",
        "slug": "execution-graph-specification",
        "prefix": "EG",
        "name": "Execution Graph Specification (EG)",
        "stage": S3,
        "short": "Runtime control graph: CA components as nodes, interfaces and relations as edges, MDM stores and caches as interaction points, with TC capabilities and Spec PASS for execution-layer properties.",
        "purpose": "Execution Graph Specification (EG) is the runtime control graph of the system. CA components become nodes in this graph, while their interfaces and relations define its edges and conditional routing rules. MDM stores and caches appear as interaction points whose state can affect routing. Nodes, routes, and execution states represent the context of multiple repositories and projects as one execution topology. EG records the TC capabilities used by each node and the accepted Spec version whose PASS covers the execution-layer properties.",
        "sections": [
            sec("Execution graph", "the control graph of this EG version.", diagram=True),
            sec("Graph nodes", "CA components as nodes of this EG version, MDM stores and caches as interaction points, repository and project context, and the TC capabilities each node uses."),
            sec("Graph edges", "CA interfaces and relations, as well as relationships between repositories and projects, as the edges of this graph, in addition to routing."),
            sec("Conditional routing", "the rules by which cache outcomes and repository and project selection determine which edge is taken."),
            sec("Execution state", "the repository and project context of a run, and the execution variables that run carries."),
            sec("Execution termination", "the conditions that end a run on this graph."),
            sec("Execution observability", "the traces recorded for nodes, edges, and runs of this graph, including cache outcomes and repository and project selection."),
        ],
        "gate": None,
        "gate_note": "The TLA+ of the present Spec version is updated to include the execution-layer properties of this graph and records PASS. Once the PASS is recorded, the process proceeds to the next artifact.",
        "boundary": "Control-graph topology and routing.",
        "bridge": "→ Agent Architecture (AA).",
    },
    {
        "id": "3.4",
        "slug": "agent-architecture",
        "prefix": "AA",
        "name": "Agent Architecture (AA)",
        "stage": S3,
        "short": "Places agents on the Execution Graph at CA reasoning points, assigns TC capabilities to roles, and specifies coordination, reasoning, routing, memory views, rollback, failure handling, and human-in-the-loop controls.",
        "purpose": "Agent Architecture (AA) places agents on the Execution Graph at the reasoning points defined by CA and at the EG nodes between them. AA assigns named TC capabilities to each role and defines how roles coordinate on the graph, including delegation, handoff, and collaboration. It also specifies the reasoning model, the views of memory and the execution graph available to each role, model-provider routing, context supply, rollback, failure handling, and human-in-the-loop controls.",
        "sections": [
            sec("Agent placement", "the agents of this AA version on the EG instance, at the CA reasoning points and on the EG nodes that fall between such points.", diagram=True),
            sec("Agent roles", "the agent roles of this AA version, and the named TC capabilities assigned to each role."),
            sec("Agent interaction", "the interactions among the agent roles of this AA version on that graph."),
            sec("Multi-Agent Coordination Protocol", "delegation, handoff, and collaboration policy for work across that graph."),
            sec("Reasoning model", "the structure of the reasoning model of this AA version."),
            sec("Model-provider routing", "which model provider and model class each role or workflow of this AA version uses, how that model is invoked, and the fallback order when routing by latency, cost, and quality."),
            sec("Agent views of memory", "the agent-facing views of MDM stores for the roles of this AA version."),
            sec("Agent views of the execution graph", "how each role of this AA version sees the EG instance.", diagram=True),
            sec("Context supplied to a role", "how this AA version gives each role its context from MDM stores, the EG instance, and assigned TC capabilities, including budget, provenance, and freshness."),
            sec("Versioning and rollback", "how the routing and context policy components of this AA are versioned and how a rollback ensures that workflow state is not orphaned."),
            sec("Handling failure structures", "the failure structures of this AA version."),
            sec("Human in the loop controls", "the human in the loop controls of this AA version."),
        ],
        "gate": None,
        "gate_note": "The TLA+ of the present Spec version is updated to include this agent architecture and records PASS. Once the PASS is recorded, the process proceeds to the next stage and artifact.",
        "boundary": "Placement, roles, coordination, and controls on the graph. Prompts belong in Agent Behavior Specification (ABS).",
        "bridge": "Completes Stage 3 → Stage 4 Agent Behavior Specification (ABS).",
    },
    {
        "id": "4.1",
        "slug": "agent-behavior-specification",
        "prefix": "ABS",
        "name": "Agent Behavior Specification (ABS)",
        "stage": S4,
        "short": "Defines how each AA role operates during a run: prompt, context, schema, capabilities, reasoning, decisions, EG interaction, reflection, failure handling, termination, validation, and model-parameter defaults.",
        "purpose": "Agent Behavior Specification (ABS) defines how each AA role operates during an execution run. It gives each role the prompt, context, schema, capabilities, and model settings required for that run. ABS also specifies how the role reasons, makes decisions, interacts with the Execution Graph, reflects on its output, handles failures, terminates, and validates its results.",
        "sections": [
            sec("System prompt", "the ongoing system prompt for each AA role of this ABS version, which is that role's identity, responsibilities, and operational parameters."),
            sec("Data model and schema", "the data model and schema provided to each AA role of this ABS version, and how that context is encapsulated within the window."),
            sec("Reasoning loop", "the reasoning loop that the prompt of each AA role in this version of the ABS must execute."),
            sec("Decision-making", "when each AA role of this ABS version reasons, invokes tools, pauses, or stops."),
            sec("Capability selection", "how each AA role of this ABS version selects among the TC capabilities assigned to it."),
            sec("EG interaction", "how each AA role of this ABS version interacts on the EG instance."),
            sec("Reflection", "the revise and retry behavior required of each AA role of this ABS version."),
            sec("Failure handling", "what each AA role of this ABS version does on tool, reasoning, or validation failure."),
            sec("Termination conditions", "when each AA role of this ABS version ends its turn or run."),
            sec("Output validation", "the checks applied to each AA role's outputs of this ABS version before those results return upstream."),
            sec("Model-parameter defaults", "the default values of temperature, top_p, and other changeable model settings and parameters for each role or workflow of this ABS version."),
        ],
        "gate": None,
        "gate_note": "The TLA+ of the current version of the Spec is revised to incorporate the schema of outcomes that have been decided for this behavior specification and PASS. This schema of outcomes is the schema that has been decided by the decisions and prompts of this ABS. After recording PASS, the process moves on to the next artifact.",
        "boundary": "System prompts and run-time behavior for each AA role. Handoff mechanics belong in HITL.",
        "bridge": "→ Escalation and Human-in-the-Loop Handoff Specification (HITL).",
    },
    {
        "id": "4.2",
        "slug": "escalation-hitl-handoff",
        "prefix": "HITL",
        "name": "Escalation and Human-in-the-Loop Handoff Specification (HITL)",
        "stage": S4,
        "short": "Defines when an agent run pauses for human intervention and how execution resumes: decision points, ABS triggers, handover procedure, resume, and timeouts.",
        "purpose": "Escalation and Human-in-the-Loop Handoff Specification (HITL) defines when an agent run pauses for human intervention and how execution resumes afterward. HITL extends the ABS stop and escalation rules with the handover information, human decision points, resume conditions, timeouts, and audit trail required for that intervention.",
        "sections": [
            sec("Human decision points", "the human decision points of this HITL version and the corresponding actions."),
            sec("Escalation triggers", "the ABS stop and escalation rules that apply to the AA human-in-the-loop for this HITL version."),
            sec("Handover procedure", "the payload, channel, and form passed to the human in this HITL version, and the logging mechanisms for those escalations."),
            sec("Resume and continue", "the rules to resume and continue execution based on human input for this HITL version, including the timeouts."),
        ],
        "gate": None,
        "gate_note": "The TLA+ of the current version of the Spec is revised to incorporate this HITL version's handover as wait, human decision, and resume, including timeout, and PASS. After recording PASS, the process moves on to the next artifact.",
        "boundary": "Operable handoff mechanics for human checkpoints.",
        "bridge": "→ Governance and Safety Policies (GOV).",
    },
    {
        "id": "4.3",
        "slug": "governance-and-safety-policies",
        "prefix": "GOV",
        "name": "Governance and Safety Policies (GOV)",
        "stage": S4,
        "short": "Sets the limits under which agents may act and turns HITL handover into enforceable policies, including change control for the Execution Graph and source code.",
        "purpose": "Governance and Safety Policies (GOV) sets the limits under which agents may act, including safety, compliance, tool use, cost, and approval requirements. GOV turns the HITL handover into enforceable policies at specified enforcement points throughout the lifecycle and at runtime. It also specifies which artifact versions may change the Execution Graph or source code. Source-code changes require corresponding updates to GOV, AA, EG, ABS, TC, and the Spec with PASS. GOV defines the audit, approval, and exception procedures.",
        "sections": [
            sec("Rules", "the rules of this GOV version that constrain the autonomy of agents in regards to safety, compliance, tool, and cost limits, as well as requirements for approval."),
            sec("Encoding", "the encoding of the stated rules of this GOV version into enforceable policies at specified enforcement points throughout the lifecycle and at runtime."),
            sec("Change control", "which artifact versions can make changes to the EG versus source code, that those artifacts are versioned using Git, and that source-code changes require a change in GOV, AA, EG, ABS, TC, and the Spec with PASS."),
            sec("Procedures", "audit, approval, and exception for this GOV version."),
        ],
        "gate": None,
        "gate_note": "Accept when the four required clauses are complete and consistent. Completing GOV completes Stage 4 when the Stage 4 set is consistent and the Spec covering cumulative scope records PASS (R3).",
        "boundary": "Enforceable policy and change-control jurisdiction.",
        "bridge": "Completes Stage 4 → Stage 5 Implementation Plan (IP).",
    },
    {
        "id": "5.1",
        "slug": "implementation-plan",
        "prefix": "IP",
        "name": "Implementation Plan (IP)",
        "stage": S5,
        "short": "Stage 5 plan for building, integrating, testing, and deploying the agent, with source-code change controlled in Git.",
        "purpose": "Implementation Plan (IP) is the Stage 5 plan for building, integrating, testing, and deploying the agent, with source-code change controlled in Git. IP covers the development process, repository structure, integration in the framework, and configuration management.",
        "sections": [
            sec("Engineering architecture", "building, integration, testing, and deployment of the agent through Git version control."),
            sec("Described process", "development process, repository structure, integration in the framework, and configuration management."),
            sec("Stage-4 Spec", "the final Spec version upon completion of Stage 4, referenced while this IP version is implemented."),
        ],
        "gate": None,
        "gate_note": "Accept when the three required clauses are complete and consistent with GOV change-control.",
        "boundary": "Roadmap bound to the approved design.",
        "bridge": "→ Evaluation (EVAL).",
    },
    {
        "id": "5.2",
        "slug": "evaluation-plan-and-failure-taxonomy",
        "prefix": "EVAL",
        "name": "Evaluation (EVAL)",
        "stage": S5,
        "short": "Defines how the agent system is judged (Evaluation Plan) and how failures are classified when judgment fails (Failure Taxonomy).",
        "purpose": "Evaluation (EVAL) defines how the agent system is judged and how failures are classified when judgment fails. The Evaluation Plan states evaluation objectives, the versioned case set, metrics and thresholds, procedures and environments, and pass/fail rules linked to those cases, bound to the IP build and test sequencing. The Failure Taxonomy states failure categories, severity, detectability and signals, example instances, and remediation owners.",
        "sections": [
            sec("Evaluation Plan", "evaluation objectives, the versioned case set, metrics and thresholds, procedures and environments, and pass/fail rules linked to those cases, bound to the IP build and test sequencing."),
            sec("Failure Taxonomy", "failure categories, severity, detectability and signals, example instances, and remediation owners."),
        ],
        "gate": None,
        "gate_note": "Accept when both required clauses are complete and consistent with Implementation Plan sequencing.",
        "boundary": "Evaluation judgment and failure classification.",
        "bridge": "→ Simulation Scenarios (SIM).",
    },
    {
        "id": "5.3",
        "slug": "simulation-scenarios",
        "prefix": "SIM",
        "name": "Simulation Scenarios (SIM)",
        "stage": S5,
        "short": "Runnable exercises that stress the agent system against EVAL, mapped to Failure Taxonomy entries, with setup, expected behavior, and pass criteria.",
        "purpose": "Simulation Scenarios (SIM) defines runnable exercises that stress the agent system against EVAL. Each scenario states setup and inputs, maps to Failure Taxonomy entries, and records expected failure or recovery behavior with pass criteria.",
        "sections": [
            sec("Runnable exercises", "exercises that stress the agent system against EVAL, and tests such as unit tests."),
            sec("Scenario contents", "setup and inputs, mapping to Failure Taxonomy entries, expected failure or recovery behavior, and pass criteria."),
        ],
        "gate": None,
        "gate_note": "Accept when both required clauses are complete and the scenarios exercise the EVAL case space and Failure Taxonomy.",
        "boundary": "Adverse and recovery scenarios before finalizing deployment architecture.",
        "bridge": "→ Deployment Architecture and Observability Plan (DEP).",
    },
    {
        "id": "5.4",
        "slug": "deployment-architecture-and-observability",
        "prefix": "DEP",
        "name": "Deployment Architecture and Observability Plan (DEP)",
        "stage": S5,
        "short": "Defines where the agent system runs and how that runtime is made visible and operable, including optional EG and source-code enrichment under GOV change-control.",
        "purpose": "Deployment Architecture and Observability Plan (DEP) defines where the agent system runs and how that runtime is made visible and operable. The Deployment Architecture is the runtime layout that hosts the adverse and recovery paths proven in SIM. The Observability Plan is how deployed runs are recorded and operated. When observability requires new control-flow or logging methods and tests, DEP authorizes enrichment of the EG and source code.",
        "sections": [
            sec("Runtime layout", "topology, environments, scaling and availability, security and access boundaries, and rollback and release integration."),
            sec("Observability", "logs, traces, and metrics inventory, instrumentation points across agents, tools, and graphs, alerting and escalation to operators, and retention and audit access."),
            sec("Enrichment", "through GOV change-control and Git versioning, via newer EGs and controlled source-code modifications."),
        ],
        "gate": None,
        "gate_note": "Accept when the three required clauses are complete and support the paths proven in SIM. Completing DEP completes the Blueprint protocol when Stage 5's required set is consistent and the Spec covering cumulative scope records PASS (R3).",
        "boundary": "Runtime topology and observability controls, including enrichment of the EG and source code under GOV change-control.",
        "bridge": "Blueprint protocol complete (Stage 5 exit on set consistency plus Spec PASS for cumulative scope).",
    },
]


def clause_line(s: dict) -> str:
    mark = " [required diagram]" if s.get("diagram") else ""
    return f"{s['name']}{mark}: {s['text']}"


def heading(s: dict) -> str:
    name = s["name"]
    if s.get("diagram"):
        return f"{name} [required diagram]"
    return name


def template_md(a: dict) -> str:
    prefix = a["prefix"]
    lines = [
        f"# {a['name']}",
        "",
        f"**Id:** `{a['id']}` · **Prefix:** `{prefix}` · **Stage:** {a['stage']} · **Version:** `v0.1-DRAFT`",
        "",
        "## Normative",
        "",
        "### Purpose",
        a["purpose"],
        "",
        "### Required sections",
    ]
    for i, s in enumerate(a["sections"], 1):
        lines.append(f"{i}. {clause_line(s)}")
    lines += ["", "### Acceptance gate"]
    if a.get("gate"):
        lines.append("All answers must be YES to approve (R1):")
        for i, g in enumerate(a["gate"], 1):
            lines.append(f"{i}. {prefix}-C{i}  {g}")
        if a.get("gate_hard"):
            lines += ["", f"**Spec PASS:** {a['gate_hard']}"]
    else:
        lines.append(a.get("gate_note", "Approver confirms completeness."))
        if a.get("gate_hard"):
            lines += ["", f"**Hard rules:** {a['gate_hard']}"]
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
        lines += [f"#### {heading(s)}", "", f"<!-- {clause_line(s)} -->", "", "_…_", ""]
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
            lines.append(f"- [ ] {prefix}-C{i}. {g}")
        if a.get("gate_hard"):
            lines += ["", f"- [ ] Spec PASS: {a['gate_hard']}"]
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
        "Artifact clauses, prefixes, and acceptance gates match the Agent Engineering Blueprint catalogue in the thesis methods chapter.",
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
