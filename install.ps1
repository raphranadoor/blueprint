# Install Agent Engineering Blueprint kit into a consumer repo's .github/agents/
# Usage:
#   .\install.ps1 [[-]DestRepoRoot] <path>
# Dest defaults to the current working directory.
# Run from a clone of https://github.com/raphranadoor/blueprint
[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$DestRepoRoot = (Get-Location).Path
)

$ErrorActionPreference = "Stop"

$KitRoot = $PSScriptRoot
$DestAgents = Join-Path $DestRepoRoot ".github\agents"

$need = @(
    "Agent Builder.agent.md",
    "as-rules",
    "templates"
)

foreach ($item in $need) {
    $path = Join-Path $KitRoot $item
    if (-not (Test-Path -LiteralPath $path)) {
        Write-Error "Missing $item under $KitRoot. Run this script from a clone of https://github.com/raphranadoor/blueprint"
    }
}

New-Item -ItemType Directory -Force -Path $DestAgents | Out-Null

Copy-Item -LiteralPath (Join-Path $KitRoot "Agent Builder.agent.md") -Destination $DestAgents -Force

$asRulesDest = Join-Path $DestAgents "as-rules"
$templatesDest = Join-Path $DestAgents "templates"
if (Test-Path -LiteralPath $asRulesDest) { Remove-Item -LiteralPath $asRulesDest -Recurse -Force }
if (Test-Path -LiteralPath $templatesDest) { Remove-Item -LiteralPath $templatesDest -Recurse -Force }
Copy-Item -LiteralPath (Join-Path $KitRoot "as-rules") -Destination $asRulesDest -Recurse -Force
Copy-Item -LiteralPath (Join-Path $KitRoot "templates") -Destination $templatesDest -Recurse -Force

$kitIndex = Join-Path $KitRoot "BLUEPRINT-KIT.md"
if (Test-Path -LiteralPath $kitIndex) {
    Copy-Item -LiteralPath $kitIndex -Destination (Join-Path $DestAgents "BLUEPRINT-KIT.md") -Force
}

Write-Host "Installed Blueprint kit into $DestAgents"
Write-Host "Next: open your IDE, select Agent Builder, and start with Problem Definition."
