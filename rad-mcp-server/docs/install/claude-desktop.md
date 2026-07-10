# Install target: Claude Desktop (chat + Cowork)

| Capability | Status |
|---|---|
| MCP tools | ✅ `claude_desktop_config.json` |
| Skills | ✅ zip upload (Customize → Skills) |
| Slash commands | ❌ — use plain language |

**Prerequisite:** the [common setup](../../INSTALL.md#common-setup-once-per-machine)
(venv, `server\.env`, `inventory.yaml`, smoke test) — once per machine.

## 1. MCP server

Edit `%APPDATA%\Claude\claude_desktop_config.json` (Windows) /
`~/Library/Application Support/Claude/claude_desktop_config.json` (macOS),
add under the top-level key:

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

**The other mode — http client** (server runs manually in a terminal, not
by Desktop; read-only). ⚠ **Desktop's config file is stdio-only** — a
`"type": "http"` entry in `claude_desktop_config.json` is silently ignored
(verified 2026-07-10: Desktop never attempts to start it; nothing in the
logs). Remote servers are added through the **UI instead**: Customize →
Connectors → add custom connector → URL (+ Authorization header if the
dialog offers advanced settings; if it only supports OAuth, a bearer-token
rad-mcp cannot be connected from Desktop — use stdio).

**Switching modes = disabling the previous config:** stdio lives in the
config file, http lives in Connectors — make sure only ONE of the two
exists (remove the `rad-mcp` config entry before adding the connector, or
vice versa), then **fully restart via tray-quit** (the config file is read
only at launch).

## 2. Fully restart Desktop

System-tray icon → Quit (closing the window is NOT enough), then relaunch.

## 3. Skills

Sidebar **Customize → Skills → upload** the zips from
`dist/claude-desktop-skills/` (`rad-core.zip`, `rad-cli-operations.zip`).

> Building the zips yourself? Use `python scripts/build_desktop_skills.py` or
> Python's `zipfile` — **not** PowerShell `Compress-Archive`, which writes
> backslash entry paths that the upload rejects ("invalid character").

## Verify

The tools icon near the message box lists rad-mcp. Ask in plain language:
*"Run a health check on <device-name>"*. Desktop has **no slash commands** —
plain language only.

## Cowork sessions

- **Skills:** the same Customize → Skills uploads apply in Cowork sessions
  automatically — nothing extra to do.
- **MCP tools:** Cowork runs in a sandboxed VM; local stdio servers from
  `claude_desktop_config.json` are bridged in by Desktop in current builds,
  but this is not yet officially documented — test before relying on it. If
  tools don't appear in Cowork, run device operations from Desktop chat or
  Claude Code instead, or connect to a shared remote server: Customize →
  Connectors → add a custom/remote MCP server → URL + header
  `Authorization: Bearer <token>` (see [remote-server.md](../remote-server.md)).

## Troubleshooting

| Symptom | Fix |
|---|---|
| Server missing after config edit | You closed the window instead of tray-Quit; config is read only at launch. Logs: `%APPDATA%\Claude\logs\mcp*.log` |
| Skill zip upload: "invalid character" | Zip built with `Compress-Archive` — rebuild with Python `zipfile` (forward-slash paths) |

Credentials / hangs: [INSTALL.md → Troubleshooting](../../INSTALL.md#troubleshooting-all-targets).
