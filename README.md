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

Intended for reuse: install the kit into consumer repositories and run Agent Builder from `.github/agents/`.
