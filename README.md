# Agent Engineering Blueprint

Copyable kit for building agentic systems with the **Agent Engineering Blueprint**: conversational Agent Builder + artifact rules + fill-in templates.

**Repo:** https://github.com/raphranadoor/blueprint

## What you get

| Path | Role |
|------|------|
| `Agent Builder.agent.md` | Custom agent prompt (process + short artifact blurbs) |
| `as-rules/` | Authoritative requirements per artifact (purpose, sections, gates, boundary, bridge) |
| `templates/` | Fill-in skeletons completed from conversation answers |
| `BLUEPRINT-KIT.md` | Index of all 17 artifacts → rule + template |
| `_generate_blueprint_kit.py` | Regenerates `as-rules/` and `templates/` from one data table |

## Quick start (consumer repo)

1. In your project, create `.github/agents/`.
2. Copy from this repo into that folder:
   - `Agent Builder.agent.md`
   - `as-rules/`
   - `templates/`
   - optionally `BLUEPRINT-KIT.md`
3. In GitHub Copilot, Cursor, Windsurf, or Claude Code, select **Agent Builder**.
4. Discuss what to build. Approve each artifact gate before advancing.

Recommended consumer layout:

```text
your-repo/
  .github/agents/
    Agent Builder.agent.md
    as-rules/
    templates/
  artifacts/                 # your versioned filled outputs
```

## Lifecycle (17 artifacts, 5 stages)

1. **Problem Definition** — Problem Definition → PRD → SRS  
2. **System Design** — Domain Model → Formal System Specification (TLA+) → Component Architecture  
3. **Architecture Specification** — Tool Contracts → Memory and Data Model → Execution Graph → Agent Architecture  
4. **Behavioral Specification and Governance** — Agent Behavior Specification → Escalation/HITL → Governance (Policy-as-Code)  
5. **Implementation, Deployment, and Validation** — Implementation Plan → Evaluation Plan & Failure Taxonomy → Simulation Scenarios → Deployment Architecture & Observability  

## Regenerate rules/templates

After editing the artifact table in `_generate_blueprint_kit.py`:

```bash
python _generate_blueprint_kit.py
```

## License / use

Intended for reuse: copy the kit into consumer repositories and run Agent Builder from `.github/agents/`.
