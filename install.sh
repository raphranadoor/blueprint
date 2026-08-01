#!/usr/bin/env bash
# Install Agent Engineering Blueprint kit into a consumer repo's .github/agents/
# Usage:
#   ./install.sh [DEST_REPO_ROOT]
# DEST defaults to the current working directory.
# Run from a clone of https://github.com/raphranadoor/blueprint
set -euo pipefail

KIT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_ROOT="${1:-$(pwd)}"
DEST_AGENTS="${DEST_ROOT}/.github/agents"

need=(
  "Agent Builder.agent.md"
  "templates"
)

for item in "${need[@]}"; do
  if [[ ! -e "${KIT_ROOT}/${item}" ]]; then
    echo "error: missing ${item} under ${KIT_ROOT}" >&2
    echo "Run this script from a clone of https://github.com/raphranadoor/blueprint" >&2
    exit 1
  fi
done

mkdir -p "${DEST_AGENTS}"

cp -f "${KIT_ROOT}/Agent Builder.agent.md" "${DEST_AGENTS}/"
rm -rf "${DEST_AGENTS}/as-rules" "${DEST_AGENTS}/templates"
cp -R "${KIT_ROOT}/templates" "${DEST_AGENTS}/templates"

if [[ -f "${KIT_ROOT}/BLUEPRINT-KIT.md" ]]; then
  cp -f "${KIT_ROOT}/BLUEPRINT-KIT.md" "${DEST_AGENTS}/BLUEPRINT-KIT.md"
fi

echo "Installed Blueprint kit into ${DEST_AGENTS}"
echo "Next: open your IDE, select Agent Builder, and start with Problem Definition."
