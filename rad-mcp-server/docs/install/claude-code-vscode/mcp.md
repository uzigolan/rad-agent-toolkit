# MCP install — Claude Code, VS Code extension

**Prerequisite:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine)
— once per machine. Skills/commands are the separate [skills.md](skills.md).

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

**http mode reminder:** an http entry never starts anything — the server
must already be running, started by you, even on the same machine. Launch
it per [connecting-local-mcp.md](../../connecting-local-mcp.md) (same
machine) or [connecting-remote-mcp.md](../../connecting-remote-mcp.md)
(another machine). Only stdio entries auto-start.

**Switching modes = disabling the previous config:** one `rad-mcp` entry in
`.mcp.json` — replace its body with the other shape (don't keep both under
two names unless you want duplicate tools), check `claude mcp list` for a
stray user-scope duplicate (`claude mcp remove rad-mcp -s user`), then
reload the window.

## Verify

Reload the window (Ctrl+Shift+P → "Developer: Reload Window"), then type
`/mcp` in the Claude panel — `rad-mcp` connected with its tools.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Server missing in `/mcp` | Reload window; check Output panel → "Claude Code" channel for launch errors |

Credentials / hangs / missing write tools: [INSTALL.md → Troubleshooting](../../../INSTALL.md#troubleshooting-all-targets).

## Files / pointers

- [mcp.stdio.sample.json](mcp.stdio.sample.json) / [mcp.http.sample.json](mcp.http.sample.json) — copy into the workspace as `.mcp.json`, fix paths
- Install script (does MCP + skills together): [`scripts/install/install-claude-code.ps1`](../../../scripts/install/install-claude-code.ps1)
