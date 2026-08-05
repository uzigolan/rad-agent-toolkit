# INSTALL/UPDATE: Copilot/Codex + rad-mcp

This guide is the root install and update entrypoint for GitHub Copilot and OpenAI Codex users.

Use the same flows both for a first installation and for later updates after
`git pull`. Re-running the relevant installer refreshes MCP configuration,
skills, and local stdio prerequisites as needed.

Choose one main AI product section below, then one variant flow under it.

## 1. Before you start

1. Use only the official GitHub Copilot product for your IDE.
2. Clone or update the repository.
3. Run all installer commands from the repository root.

```bash
git clone https://github.com/uzigolan/rad-agent-toolkit.git
cd rad-agent-toolkit
```

If you already have the repo:

```bash
git pull
```

## 2. GitHub Copilot (main)

Use one Copilot variant below.

### 2.1 VS Code + MCP stdio (default)

This is the default and simplest local install path.

Run:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-stdio-copilot-vscode.ps1
```

What it does:

1. Reload the VS Code window with `Ctrl + Shift + P` -> `Developer: Reload Window`.
2. Open Copilot Settings ⚙.
3. In `MCP Servers`, make sure `rad-mcp` appears and click Start or Restart if needed.
4. In `Skills`, search for `rad-` and verify you see 8 or more skills.
5. Switch Copilot Chat to Agent mode.
6. Test with: `rad agent, list the managed devices`.

What it does:

1. Prepares the local stdio MCP server.
2. Builds or reuses the local catalog as needed.
3. Installs VS Code Copilot MCP config.
4. Installs Copilot skills in served mode.

Useful options:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-stdio-copilot-vscode.ps1 -MibDir C:\MIBS
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-stdio-copilot-vscode.ps1 -SkipCatalog
```

### 2.2 IntelliJ + MCP stdio

Run:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-stdio-copilot-intellij.ps1
```

What it does:

1. Restart the IDE.
2. Open Copilot Settings ⚙.
3. In `MCP Servers`, make sure `rad-mcp` appears and click Start or Restart if needed.
4. In `Skills`, search for `rad-` and verify you see 8 or more skills.
5. Switch Copilot Chat to Agent mode.
6. Test with: `rad agent, list the managed devices`.

What it does:

1. Prepares the local stdio MCP server.
2. Builds or reuses the local catalog as needed.
3. Installs JetBrains Copilot MCP config.
4. Installs Copilot skills in served mode.

Useful options:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-stdio-copilot-intellij.ps1 -MibDir C:\MIBS
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-stdio-copilot-intellij.ps1 -SkipCatalog
```

### 2.3 VS Code + MCP HTTP

First start or prepare the HTTP MCP server:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\mcp_server\install-and-start-http-mcp-server.ps1
```

Then install VS Code Copilot MCP config and skills:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-copilot-vscode.ps1
```

Recommended answers:

1. Knowledge mode: `served`.
2. Transport: `http`.
3. URL: your MCP URL.
4. Token: the matching server bearer token.

After install:

1. Reload the VS Code window.
2. Open Copilot Settings and verify `rad-mcp` appears under MCP Servers.
3. Start or Restart the MCP server entry if needed.
4. Switch Copilot Chat to Agent mode.
5. Test with: `rad agent, list the managed devices`.

Detailed guides:

1. `rad-mcp-server/scripts/install/mcp_server/INSTALL-http-mcp-server.md`
2. `rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-copilot-vscode-mcp-skills.md`

### 2.4 IntelliJ + MCP HTTP

First start or prepare the HTTP MCP server:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\mcp_server\install-and-start-http-mcp-server.ps1
```

Then install JetBrains Copilot MCP config and skills:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-copilot-intellij.ps1
```

Recommended answers:

1. Knowledge mode: `served`.
2. Transport: `http`.
3. URL: your MCP URL.
4. Token: the matching server bearer token.

After install:

1. Restart the IDE.
2. Open Copilot Settings and verify `rad-mcp` appears under MCP Servers.
3. Start or Restart the MCP server entry if needed.
4. Switch Copilot Chat to Agent mode.
5. Test with: `rad agent, list the managed devices`.

Detailed guides:

1. `rad-mcp-server/scripts/install/mcp_server/INSTALL-http-mcp-server.md`
2. `rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-copilot-intellij-mcp-skills.md`

### 2.5 Generic + MCP stdio

First prepare local stdio MCP prerequisites:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\mcp_server\install-stdio-mcp-server.ps1
```

Then run the generic helper:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-generic.ps1
```

Use this when your target client is not the supported VS Code or IntelliJ Copilot flow.

### 2.6 Generic + MCP HTTP

First start or prepare the HTTP MCP server:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\mcp_server\install-and-start-http-mcp-server.ps1
```

Then run the generic helper:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-generic.ps1
```

Choose HTTP mode in the helper and provide the server URL and token.

After install:

1. Apply the generated MCP snippet in your target client config.
2. Restart that client/session.
3. Verify the client can see `rad-mcp` tools.

## 3. ChatGPT Codex (main)

Use one Codex variant below.

### 3.1 VS Code Codex + MCP stdio

Run:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-stdio-codex-vscode.ps1
```

What it does:

1. Prepares the local stdio MCP server.
2. Builds or reuses the local catalog as needed.
3. Installs Codex MCP config (`~/.codex/config.toml`).
4. Installs skills for Codex (`~/.agents/skills`) in served mode.

After install:

1. Fully restart VS Code (or the Codex extension host/session).
2. Open a local Codex session and run `/mcp` and `/skills`.
3. Test with: `rad agent, list the managed devices`.

Useful options:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-stdio-codex-vscode.ps1 -MibDir C:\MIBS
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-stdio-codex-vscode.ps1 -SkipCatalog
```

### 3.2 VS Code Codex + MCP HTTP

Step 1: start or prepare the shared HTTP MCP server:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\mcp_server\install-and-start-http-mcp-server.ps1
```

Step 2: install Codex MCP config + skills in HTTP mode:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-http-codex-vscode.ps1
```

Recommended answers/flags:

1. Knowledge mode: `served`.
2. URL: your MCP URL.
3. Token: the matching server bearer token.

After install:

1. Fully restart VS Code (or the Codex extension host/session).
2. Open a local Codex session and run `/mcp` and `/skills`.
3. Test with: `rad agent, list the managed devices`.

Non-interactive example:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-http-codex-vscode.ps1 -Url http://127.0.0.1:8080/mcp -Token <token>
```

### 3.3 Codex shared installer (CLI/IDE/Desktop)

Use the shared Codex installer when you want one config for all Codex surfaces
(`~/.codex/config.toml`):

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-codex.ps1
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-codex.ps1 -Http -Url http://127.0.0.1:8080/mcp -Token <token>
```

### 3.4 ChatGPT Codex desktop app (HTTPS guide)

For the desktop-app-focused HTTPS flow, follow:

1. `rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-codex-mcp-skills.md`

## 4. Problems

### `'PowerShell' is not recognized`

If you are already inside a PowerShell prompt, do not launch `PowerShell` again.
Run the script directly:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-stdio-copilot-vscode.ps1
```

If execution policy blocks it:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-stdio-copilot-vscode.ps1
```

If your machine has PowerShell 7:

```powershell
pwsh -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-stdio-copilot-vscode.ps1
```

If you want Windows PowerShell specifically:

```powershell
powershell.exe -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-stdio-copilot-vscode.ps1
```

Check what is available:

```powershell
Get-Command pwsh, powershell.exe
```

### MCP installed but Copilot does not see it

1. Reload or restart the IDE.
2. Accept the MCP trust prompt.
3. Use Agent mode, not Ask or Edit mode.
4. Re-run the installer with `-Reconfigure` if an old config was kept.

### Skills are missing or stale

1. Re-run the relevant installer.
2. Remove duplicate old skill copies if your client loaded stale ones.
3. In served mode, remember that skills are thin and knowledge comes from MCP tools.

### Data exists in the repo but the assistant says it is missing

1. Bundled mode may read only shipped skill references under `skills/.../references/`.
2. Served mode must use MCP knowledge tools, not arbitrary workspace disk search.
3. If the tracked reference artifact is missing, update the repo and reinstall.

## 5. Verify with one prompt per technology

1. Device management: `rad agent, add my device: name lab-etx2, host 172.17.163.205, family etx2, group lab, user su, password 1234`
2. Manual knowledge: `rad agent, according to the ETX-2 manual, explain ERP failover timers and revertive behavior`
3. CLI operations: `abayev, show the active alarms on sf-163-187`
4. SNMP operations: `rad agent, check SNMP on etx2v-1 and report its exact firmware, sysObjectID, and detected family`
5. MEA commands: `rad agent, list all MEA util fctl commands from stored data`
6. Altera knowledge: `rad agent, in Altera docs explain AWVALID/WVALID timing expectations and point to the relevant figure`

## 6. Detailed references

1. `rad-mcp-server/scripts/install/mcp_server/INSTALL-http-mcp-server.md`
2. `rad-mcp-server/scripts/install/mcp_server/INSTALL-stdio-mcp-server.md`
3. `rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-copilot-vscode-mcp-skills.md`
4. `rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-copilot-intellij-mcp-skills.md`
5. `rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-generic-mcp-skills.md`
6. `rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-codex-mcp-skills.md`
7. `rad-mcp-server/scripts/install/skills_and_mcp/README.md`
8. `rad-mcp-server/docs/examples.md`
