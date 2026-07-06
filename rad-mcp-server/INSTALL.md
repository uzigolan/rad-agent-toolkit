# Installing rad-mcp

One codebase, four Claude surfaces. Do the **common setup** once, then follow
the section for each surface you use.

| Surface | MCP tools | Skills | Slash commands |
|---|---|---|---|
| Claude Code — VS Code extension | ✅ | ✅ | ✅ `/rad-health`, `/rad-backup` |
| Claude Code — CLI | ✅ | ✅ | ✅ |
| Claude Desktop — chat | ✅ | ✅ (zip upload) | ❌ (use plain language) |
| Claude Desktop — Cowork | see notes | ✅ (same uploads) | ❌ |

---

## Common setup (once per machine)

Requirements: Python 3.11+, SSH reachability to your RAD devices.

```powershell
cd rad-mcp-server\server
python -m venv .venv
.venv\Scripts\pip install -e .
```

Create `server\.env` (gitignored — never commit credentials):

```
RAD_MCP_USERNAME=...
RAD_MCP_PASSWORD=...
# optional per-device override: RAD_MCP_<NAME>_USERNAME / _PASSWORD
# optional: RAD_MCP_READONLY=true  (disables all write tools)
```

Add your devices to `inventory.yaml` (name, host, family, groups — no
credentials). Then smoke-test one device end-to-end:

```powershell
.venv\Scripts\python -m rad_mcp.smoke <device-name>
```

---

## Claude Code — VS Code extension

Two pieces: the MCP server (project `.mcp.json`) and the plugin
(skills + slash commands).

**1. MCP server** — in the workspace root, create/merge `.mcp.json`:

```json
{
  "mcpServers": {
    "rad-mcp": {
      "command": "<repo>\\server\\.venv\\Scripts\\python.exe",
      "args": ["-m", "rad_mcp.server"],
      "cwd": "<repo>\\server",
      "env": { "RAD_MCP_INVENTORY": "<repo>\\inventory.yaml" }
    }
  }
}
```

**2. Plugin** — in `.claude/settings.json` of the workspace:

```json
{
  "extraKnownMarketplaces": {
    "rad-marketplace": {
      "source": { "source": "directory", "path": "<absolute-path-to-repo>" }
    }
  },
  "enabledPlugins": { "rad-mcp@rad-marketplace": true }
}
```

**3. Reload the VS Code window** (Ctrl+Shift+P → "Developer: Reload Window").

**Verify:** type `/mcp` in the Claude panel — `rad-mcp` should be connected
with its tools. Then try `/rad-health <device-name>`.

## Claude Code — CLI

```bash
claude plugin marketplace add <path-to-this-repo>
claude plugin install rad-mcp@rad-marketplace
```

Or without the plugin system, register just the MCP server:

```bash
claude mcp add rad-mcp -- <repo>/server/.venv/Scripts/python.exe -m rad_mcp.server
```

**Verify:** `claude mcp list`, then `/mcp` inside a session.

## Claude Desktop — chat

**1. MCP server** — edit `%APPDATA%\Claude\claude_desktop_config.json`
(Windows) / `~/Library/Application Support/Claude/claude_desktop_config.json`
(macOS), add under the top-level key:

```json
{
  "mcpServers": {
    "rad-mcp": {
      "command": "<repo>\\server\\.venv\\Scripts\\python.exe",
      "args": ["-m", "rad_mcp.server"],
      "env": { "RAD_MCP_INVENTORY": "<repo>\\inventory.yaml" }
    }
  }
}
```

Note: no `cwd` key (Desktop doesn't support it) — all server paths (`.env`,
backups, logs) are module-anchored, so this is safe, and Desktop shares the
same backup archive and audit log as Claude Code.

**2. Fully restart Desktop** — system-tray icon → Quit (closing the window is
NOT enough), then relaunch.

**3. Skills** — sidebar **Customize → Skills → upload** the zips from
`dist/desktop-skills/` (`rad-core.zip`, `rad-cli-operations.zip`).

> Building the zips yourself? Use `python scripts/build_desktop_skills.py` or
> Python's `zipfile` — **not** PowerShell `Compress-Archive`, which writes
> backslash entry paths that the upload rejects ("invalid character").

**Verify:** the tools icon near the message box lists rad-mcp. Ask in plain
language: *"Run a health check on <device-name>"*. Desktop has **no slash
commands** — plain language only.

## Claude Desktop — Cowork

- **Skills:** the same Customize → Skills uploads apply in Cowork sessions
  automatically — nothing extra to do.
- **MCP tools:** Cowork runs in a sandboxed VM; local stdio servers from
  `claude_desktop_config.json` are bridged in by Desktop in current builds,
  but this is not yet officially documented — test before relying on it. If
  tools don't appear in Cowork, run device operations from Desktop chat or
  Claude Code instead. (A future remote-MCP/`.mcpb` packaging of rad-mcp will
  make this first-class.)

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Server missing in `/mcp` (Code) | Reload window; check Output panel → "Claude Code" channel for launch errors |
| Server missing in Desktop | You closed the window instead of tray-Quit; config is read only at launch. Logs: `%APPDATA%\Claude\logs\mcp*.log` |
| "No username/password" errors | `server\.env` missing or misnamed vars |
| Skill zip upload: "invalid character" | Zip built with `Compress-Archive` — rebuild with Python `zipfile` (forward-slash paths) |
| Tool calls hang | Device unreachable — check SSH to the host in `inventory.yaml` |
| Write tools missing | `RAD_MCP_READONLY=true` is set — intentional guard |
