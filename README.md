# Agent Engineering Blueprint

Copyable kit for building agentic systems with the **Agent Engineering Blueprint**: conversational Agent Builder + artifact rules + fill-in templates.

**Repo:** https://github.com/raphranadoor/blueprint

## What you get

| Path | Role |
|------|------|
| `install.sh` / `install.ps1` | Installs the kit into a consumer repo’s `.github/agents/` |
| `Agent Builder.agent.md` | Custom agent prompt (process + short artifact blurbs) |
| `templates/` | One file per artifact: **Normative** requirements + **Instance** fill-in |
| `BLUEPRINT-KIT.md` | Index of all 17 artifacts → template paths |
| `_generate_blueprint_kit.py` | Regenerates `templates/` from one data table |

## Quick start (consumer repo)

### 1. Install the kit

From a clone of this repo, point the installer at your project root (defaults to the current directory):

**Linux / macOS / Git Bash**

```bash
git clone https://github.com/raphranadoor/blueprint.git
cd blueprint
chmod +x install.sh
./install.sh /path/to/your-repo
```

**Windows PowerShell**

```powershell
git clone https://github.com/raphranadoor/blueprint.git
cd blueprint
.\install.ps1 -DestRepoRoot C:\path\to\your-repo
```

One-liner when your shell is already inside the consumer repo:

```bash
git clone --depth 1 https://github.com/raphranadoor/blueprint.git /tmp/blueprint \
  && /tmp/blueprint/install.sh .
```

```powershell
git clone --depth 1 https://github.com/raphranadoor/blueprint.git $env:TEMP\blueprint
& "$env:TEMP\blueprint\install.ps1" -DestRepoRoot (Get-Location)
```

The installer creates `.github/agents/` and copies `Agent Builder.agent.md`, `templates/`, and `BLUEPRINT-KIT.md`.

### 2. Invoke Agent Builder

In GitHub Copilot, Cursor, Windsurf, or Claude Code, select **Agent Builder**, discuss what to build, and approve each artifact gate before advancing.

Recommended consumer layout:

```text
your-repo/
  .github/agents/
    Agent Builder.agent.md
    templates/
  artifacts/                 # your versioned filled outputs
```

Clauses, prefixes (`PD`, `PRD`, …), and acceptance gates match the Agent Engineering Blueprint catalogue in the thesis methods chapter.

## Lifecycle (17 artifacts, 5 stages)

1. **Problem and requirements** — Problem Definition (PD) → Product Requirements Document (PRD) → System Requirements Specification (SRS)
2. **Domain and structure** — Domain Model (DM) → Formal System Specification (SPEC) → Component Architecture (CA)
3. **Tools, memory, and graph** — Tool Contracts (TC) → Memory and Data Model (MDM) → Execution Graph Specification (EG) → Agent Architecture (AA)
4. **Behavior, handoff, and policy** — Agent Behavior Specification (ABS) → Escalation and HITL Handoff (HITL) → Governance and Safety Policies (GOV)
5. **Build, simulate, and deploy** — Implementation Plan (IP) → Evaluation (EVAL) → Simulation Scenarios (SIM) → Deployment Architecture and Observability Plan (DEP)

## Regenerate templates

After editing the artifact table in `_generate_blueprint_kit.py`:

```bash
python _generate_blueprint_kit.py
```

## License / use

Intended for reuse: install the kit into consumer repositories and run Agent Builder from `.github/agents/`.
