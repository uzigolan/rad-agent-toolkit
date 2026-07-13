<#
Install rad-mcp (MCP + skills) for the GitHub Copilot VS Code extension.

  .\install-copilot-vscode.ps1                                   # interactive prompts
  .\install-copilot-vscode.ps1 -Http [-Url <url>] -Token <token> # http client
  .\install-copilot-vscode.ps1 -Reconfigure                      # force replace an existing entry

Writes/merges VS Code user MCP config (Windows:
%APPDATA%\Code\User\mcp.json, root key "servers") and copies the skills to
~\.copilot\skills. If rad-mcp is already configured (and no flags force a
mode), offers to keep the existing configuration. Afterwards: reload the VS
Code window, accept the trust dialog, use agent mode.
#>
param(
    [switch]$Http,
    [string]$Url,
    [string]$Token,
    [switch]$Reconfigure
)
. (Join-Path $PSScriptRoot '..\_common.ps1')

$cfgPath = Join-Path $env:APPDATA 'Code\User\mcp.json'
New-Item -ItemType Directory -Force (Split-Path $cfgPath) | Out-Null
Backup-JsonConfig -Path $cfgPath

$explicit = $Http -or $Url -or $Token -or $Reconfigure
if ((-not $explicit) -and (Test-KeepExisting -Path $cfgPath -RootKey 'servers')) {
    Write-Host "  mcp   -> kept existing rad-mcp entry in $cfgPath"
    Copy-SkillsTo "$env:USERPROFILE\.copilot\skills"
    Write-Host ""
    Write-Host "Done. Existing MCP config kept; skills refreshed. Reload the VS Code window."
    return
}

if (-not ($Http -or $Url -or $Token)) {
    # Interactive transport prompt when no flags given
    $transport = Invoke-TransportPrompt
    if ($transport.Mode -eq 'http') {
        $entry = New-HttpEntry -Url $transport.Url -Token $transport.Token
    } else {
        Assert-CommonSetup
        $entry = New-StdioEntry -WithType
    }
} elseif ($Http -or $Url -or $Token) {
    if ($Http) {
        $u, $t = Resolve-HttpArgs $Url $Token
        $entry = New-HttpEntry -Url $u -Token $t
    } else {
        Assert-CommonSetup
        $entry = New-StdioEntry -WithType
    }
} else {
    Assert-CommonSetup
    $entry = New-StdioEntry -WithType
}

Set-JsonMcpEntry -Path $cfgPath -RootKey 'servers' -Entry $entry
Copy-SkillsTo "$env:USERPROFILE\.copilot\skills"

Write-Host ""
Write-Host "Done. Now: reload the VS Code window, accept the MCP trust dialog,"
Write-Host "switch Copilot Chat to AGENT mode, and try: 'list the managed devices'."
if ($Http) { Write-Host "http mode: make sure the shared server is running, and its token matches this client's." }
