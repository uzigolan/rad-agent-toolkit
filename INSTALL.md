# INSTALL/UPDATE: Copilot/Codex/Claude + rad-mcp

This guide is the root install and update entrypoint for GitHub Copilot, OpenAI Codex, and Anthropic Claude users.

Use the same flows both for a first installation and for later updates after
`git pull`. Re-running the relevant installer refreshes MCP configuration,
skills, and local stdio prerequisites as needed.

Choose one main AI product section below, then one variant flow under it.

## 1. Before you start

1. Download and install the latest IDE you work with.
1.1 VS Code: https://code.visualstudio.com/download
1.2 IntelliJ IDEA: https://lp.jetbrains.com/intellij-idea-promo
2. Download and install Git: https://git-scm.com/install/windows
3. Use only the official GitHub Copilot, ChatGPT Codex, or Anthropic Claude product for your IDE.
4. Clone or update the repository.
5. Run all installer commands from the repository root.

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

### 2.3 Copilot CLI + MCP stdio

For the `copilot` terminal CLI (also read by the embedded Copilot CLI agent
in JetBrains IDEs).

Run:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-copilot-cli.ps1
```

When prompted for transport, choose `stdio` (the default).

After install:

1. Restart the `copilot` session (skills and MCP load at startup only).
2. Verify with `/mcp show` and `/skills list`.
3. On the first tool call, answer the permission prompt with `yes, always`.
4. Test with: `rad agent, list the managed devices`.

What it does:

1. Prepares the local stdio MCP server.
2. Writes/merges `~\.copilot\mcp-config.json` and `~\.copilot\mcp.json` (kept in sync).
3. Copies the skills to `~\.copilot\skills` in served mode.

### 2.4 VS Code + MCP HTTP

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

### 2.5 IntelliJ + MCP HTTP

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

### 2.6 Copilot CLI + MCP HTTP

Step 1: start or prepare the shared HTTP MCP server:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\mcp_server\install-and-start-http-mcp-server.ps1
```

Step 2: install Copilot CLI MCP config + skills in HTTP mode:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-copilot-cli.ps1 -Http -Url http://127.0.0.1:8080/mcp -Token <token>
```

Or run without flags and choose `http` at the transport prompt, then provide
your MCP URL and matching token.

After install:

1. Make sure the shared HTTP server is running and its token matches this client's.
2. Restart the `copilot` session.
3. Verify with `/mcp show` and `/skills list`.
4. Test with: `rad agent, list the managed devices`.

### 2.7 Generic + MCP stdio

First prepare local stdio MCP prerequisites:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\mcp_server\install-stdio-mcp-server.ps1
```

Then run the generic helper:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-generic.ps1
```

Use this when your target client is not the supported VS Code or IntelliJ Copilot flow.

### 2.8 Generic + MCP HTTP

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

## 4. Claude (main)

Use one Claude variant below. All Claude variants use stdio MCP only — Claude
launches the local server itself (full toolset including staged writes).

### 4.1 Claude Desktop + MCP stdio

Run:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-claude-desktop.ps1
```

What it does:

1. Prepares the local stdio MCP server.
2. Backs up the Claude Desktop config (Windows Store or traditional path), then merges the `rad-mcp` entry under `mcpServers`.
3. Rebuilds the skill zips and opens the zip folder for manual upload.

After install (two manual steps):

1. FULLY restart Claude Desktop: system-tray icon -> Quit (closing the window is NOT enough), then relaunch.
2. Sidebar Customize -> Skills -> upload the skill zips from the Explorer folder the installer opens (replace existing ones if already uploaded).
3. Test with: `rad agent, list the managed devices`.

Useful options:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-claude-desktop.ps1 -Reconfigure
```

### 4.2 Claude VS Code + MCP stdio

Requires the `claude` CLI on PATH (install Claude Code first:
https://claude.com/claude-code). The VS Code extension and the CLI read the
same plugin/config.

Run:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-claude-code.ps1
```

When prompted for transport, choose `stdio` (the default plugin mode).

What it does:

1. Prepares the local stdio MCP server.
2. Installs the `rad-mcp@rad-marketplace` plugin (MCP registration + skills + slash commands).

After install:

1. Reload the VS Code window with `Ctrl + Shift + P` -> `Developer: Reload Window`.
2. Verify with `/mcp` and try `/rad-health <device-name>`.
3. Test with: `rad agent, list the managed devices`.

### 4.3 Claude CLI + MCP stdio

Same installer as the VS Code flow — Claude Code CLI and the VS Code
extension share the plugin/config.

Run:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-claude-code.ps1
```

When prompted for transport, choose `stdio` (the default plugin mode).

After install:

1. Start a new `claude` session.
2. Verify with `/mcp` and try `/rad-health <device-name>`.
3. Test with: `rad agent, list the managed devices`.

## 5. Problems

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

## 6. Verify with one prompt per technology

1. Device management: `rad agent, add my device: name lab-etx2, host 172.17.163.205, family etx2, group lab, user su, password 1234`
2. Manual knowledge: `rad agent, according to the ETX-2 manual, explain ERP failover timers and revertive behavior`
3. CLI operations: `abayev, show the active alarms on sf-163-187`
4. SNMP operations: `rad agent, check SNMP on etx2v-1 and report its exact firmware, sysObjectID, and detected family`
5. MEA commands: `rad agent, list all MEA util fctl commands from stored data`
6. Altera knowledge: `rad agent, in Altera docs explain AWVALID/WVALID timing expectations and point to the relevant figure`

## 7. Detailed references

1. `rad-mcp-server/docs/INSTALL-locations.md` — where each flow installs MCP config, skills, and plugins
2. `rad-mcp-server/scripts/install/mcp_server/INSTALL-http-mcp-server.md`
3. `rad-mcp-server/scripts/install/mcp_server/INSTALL-stdio-mcp-server.md`
4. `rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-copilot-vscode-mcp-skills.md`
5. `rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-copilot-intellij-mcp-skills.md`
6. `rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-generic-mcp-skills.md`
7. `rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-codex-mcp-skills.md`
8. `rad-mcp-server/scripts/install/skills_and_mcp/README.md`
9. `rad-mcp-server/docs/examples.md`
