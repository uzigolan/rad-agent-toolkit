# MCP install — Claude Desktop

**Prerequisite:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine)
— once per machine. Skills are the separate [skills.md](skills.md).

## stdio (the default — and the only write-capable mode)

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
same backup archive and audit log as the other clients.

## http client (joining a shared server; read-only)

⚠ **Desktop's config file is stdio-only** — a `"type": "http"` entry is
silently ignored (verified 2026-07-10: Desktop never attempts to start it).
Two working routes:

- **Option A — Connectors UI:** Customize → Connectors → add custom
  connector → URL (+ Authorization header if the dialog offers advanced
  settings; if it only supports OAuth, use option B).
- **Option B — the stdio→http bridge** (file-only, python-based; verified
  2026-07-12): a stdio-shaped entry whose command is
  [`scripts/desktop_http_bridge.py`](../../../scripts/desktop_http_bridge.py) —
  Desktop spawns the bridge, the bridge connects onward with the bearer
  header. Sample:
  [claude_desktop_config.http-bridge.sample.json](claude_desktop_config.http-bridge.sample.json).

**http mode reminder:** neither route starts the server — it must already
be running ([connecting-local-mcp.md](../../connecting-local-mcp.md) /
[connecting-remote-mcp.md](../../connecting-remote-mcp.md)).

**Switching modes = disabling the previous config:** one `rad-mcp` — remove
the old entry/connector before adding the new one.

## Restart + verify

**Fully restart via tray-quit** (window close is NOT enough — the config is
read only at launch), relaunch, then the tools icon near the message box
should list rad-mcp. Ask in plain language: *"run a health check on
<device-name>"*.

**Cowork sessions:** local stdio servers are bridged into the sandboxed VM
in current builds, but this isn't officially documented — test before
relying on it; the Connectors route is the documented alternative.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Server missing after config edit | You closed the window instead of tray-Quit; config is read only at launch. Logs: `%APPDATA%\Claude\logs\mcp*.log` |

Credentials / hangs: [INSTALL.md → Troubleshooting](../../../INSTALL.md#troubleshooting-all-targets).

## Files / pointers

- [claude_desktop_config.sample.json](claude_desktop_config.sample.json) — stdio entry, fix paths
- [claude_desktop_config.http-bridge.sample.json](claude_desktop_config.http-bridge.sample.json) — the bridge entry (option B)
- Install script (MCP + zip build together): [`scripts/install/install-claude-desktop.ps1`](../../../scripts/install/install-claude-desktop.ps1)
