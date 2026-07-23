# INSTALL: VS Code or IntelliJ Copilot

This guide consolidates the two main Copilot install flows in one place.
Use one path only, based on your IDE:
- VS Code + GitHub Copilot extension
- IntelliJ (JetBrains) + GitHub Copilot plugin

For all other install flows, use:
- `rad-mcp-server/scripts/install/`

## 1) Mandatory first step (official Copilot only)

Before anything else:
- Choose your IDE path: VS Code or IntelliJ.
- Download/install (or update) only the IDE you plan to use.
- Install only the official GitHub Copilot add-on for each IDE:
  - VS Code: `GitHub Copilot` + `GitHub Copilot Chat` by GitHub (verified publisher).
  - IntelliJ: `GitHub Copilot` by GitHub from JetBrains Marketplace.
- For Copilot update checks and management, use Copilot extension/plugin update actions and Copilot settings/UI in each IDE.
- Do not use non-Copilot AI plugins for this flow (for example JetBrains AI Assistant / Junie).

## 2) Clone the repository

```bash
git clone https://github.com/uzigolan/rad-agent-toolkit.git
cd rad-agent-toolkit
```

## 3) Install MCP server first (command only)

Run from repo root:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\mcp_server\install-and-start-http-mcp-server.ps1
```

## 4) Interactive choices (recommended)

When the MCP server installer asks questions, use these recommendations:
- Transport/bind usage: use HTTP mode (shared server flow).
- TLS: choose `No TLS` for local/internal lab usage.
- Tokens: create at least one token (required). Keep read-write token private.
- MIBs prompt:
  - Choose `N` if you do not need MIB catalog tools right now.
  - Choose `Y` only if you need `mib_*` tools (`mib_search`, `mib_describe`, etc.).

Important safety note:
- This installer creates and uses a Python virtual environment under the repo (`rad-mcp-server/server/.venv`, and portable Python may be placed under `server/.python` on Windows).
- It does not install system-wide Python components and should not harm your PC.

## 5) Install skills + MCP config (choose one IDE path)

### 5a) VS Code Copilot

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-copilot-vscode.ps1
```

Recommended answers:
- Knowledge mode: `bundled` (default, easiest) or `served` (if you want catalog served by MCP).
- Transport: `http`
- URL: use your MCP URL (example: `http://127.0.0.1:8080/mcp`)
- Token: paste the same bearer token configured for the MCP server.

### 5b) IntelliJ Copilot

```powershell
PowerShell -ExecutionPolicy Bypass -File .\rad-mcp-server\scripts\install\skills_and_mcp\install-copilot-intellij.ps1
```

Recommended answers:
- Knowledge mode: `bundled` (or `served` if you intentionally use served knowledge)
- Transport: `http`
- URL/token: same MCP URL and token as above.

## 6) Verify in Copilot (for your chosen IDE)

Do these checks in Copilot chat and/or Copilot settings/UI tools for the IDE you chose.
Using the Copilot UI is fully supported for this flow.

VS Code:
1. Run Command Palette -> `Developer: Reload Window`.
2. Open Copilot Chat and switch to `Agent` mode.
3. In Copilot UI (Agent Customizations -> MCP Servers), verify `rad-mcp` appears/runs.
4. In Copilot UI (Agent Customizations -> Skills), verify the 3 rad skills are listed.
5. Test prompt: `rad agent, list the managed devices`.

IntelliJ:
1. Restart the IDE.
2. Open GitHub Copilot Chat, switch to Agent mode, and start a new chat.
3. In Copilot Chat, click the settings gear, then choose `Customizations`.
4. In Agent Customizations -> `MCP Servers`, verify `rad-mcp` appears/runs.
5. In Agent Customizations -> `Skills`, verify the rad skills are loaded.
6. Test prompt: `rad agent, list the managed devices`.

Where not to look:
- IntelliJ: `Settings -> Tools -> AI Assistant` is not the Copilot path and does not show this MCP/skills setup.

If needed:
- VS Code: run `MCP: Open User Configuration` or `MCP: Reset Trust`.
- IntelliJ: re-run the installer with the same URL/token and restart the IDE.

## 7) Usage prompts from examples

Use these ready prompts after install (copied from `rad-mcp-server/docs/examples.md`):

Start with device management (section 1):
```text
rad agent, add my device: name lab-etx2, host 172.17.163.205, family etx2, group lab, user su, password 1234
```

Then one prompt from each core area:

From section 2 (User manual knowledge):
```text
rad agent, how does zero-touch provisioning work on the MiNID, and what are its limits?
```

From section 4 (CLI operations):
```text
abayev, show the active alarms on sf-163-187
```

From section 5 (SNMP operations):
```text
rad agent, check SNMP on etx2v-1 and report its exact firmware, sysObjectID, and detected family
```

Full prompt catalog:
- `rad-mcp-server/docs/examples.md`

---

Based on:
- `rad-mcp-server/scripts/install/mcp_server/INSTALL-http-mcp-server.md`
- `rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-copilot-vscode-mcp-skills.md`
- `rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-copilot-intellij-mcp-skills.md`
