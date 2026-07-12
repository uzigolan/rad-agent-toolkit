# Install target: Claude Code — VS Code extension

| Capability | Status |
|---|---|
| MCP tools | ✅ project `.mcp.json` |
| Skills (rad-core, rad-cli-operations, rad-device-mng) | ✅ via plugin |
| Slash commands | ✅ `/rad-health`, `/rad-backup`, `/rad-harvest`, `/rad-load-manual` |

**Prerequisite:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine)
(venv, `server\.env`, `inventory.yaml`, smoke test) — once per machine.

Two pieces: the MCP server (project `.mcp.json`) and the plugin
(skills + slash commands).

## 1. MCP server

In the workspace root, create/merge `.mcp.json`:

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

That's the **stdio shape** (Claude launches the server). The **http shape**
connects to a server you run manually — read-only
([anatomy](../../../INSTALL.md#config-anatomy-who-runs-the-server)):

```json
{
  "mcpServers": {
    "rad-mcp": {
      "type": "http",
      "url": "https://<host>:8080/mcp",
      "headers": { "Authorization": "Bearer <your-token>" }
    }
  }
}
```

**Switching modes = disabling the previous config:** one `rad-mcp` entry in
`.mcp.json` — replace its body with the other shape (don't keep both under
two names unless you want duplicate tools), check `claude mcp list` for a
stray user-scope duplicate (`claude mcp remove rad-mcp -s user`), then
reload the window.

## 2. Plugin (skills + commands)

In `.claude/settings.json` of the workspace:

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

## 3. Reload

Reload the VS Code window (Ctrl+Shift+P → "Developer: Reload Window").

## Verify

Type `/mcp` in the Claude panel — `rad-mcp` should be connected with its
tools. Then try `/rad-health <device-name>`.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Server missing in `/mcp` | Reload window; check Output panel → "Claude Code" channel for launch errors |

Credentials / hangs / missing write tools: [INSTALL.md → Troubleshooting](../../../INSTALL.md#troubleshooting-all-targets).

**http mode reminder:** an http entry never starts anything — the server must already be running as a separate process, started by you, even when it lives on the same machine as this client. Launch block: [remote-server.md](../../remote-server.md). Only stdio entries auto-start.

## In this folder / pointers

- [mcp.stdio.sample.json](mcp.stdio.sample.json) / [mcp.http.sample.json](mcp.http.sample.json) — copy into the workspace as `.mcp.json`, fix paths
- Install script: [`scripts/install/install-claude-code.ps1`](../../../scripts/install/install-claude-code.ps1)
- Skills + commands source: [`rad-mcp-server/skills/`](../../../skills/) · [`commands/`](../../../commands/) (plugin delivers both)
