# MCP install — GitHub Copilot, VS Code (agent mode)

**Prerequisite:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine)
— once per machine. Skills are the separate [skills.md](skills.md).
MCP tools exist **only in agent mode** (invisible in Ask/Edit).

In the workspace root, create/merge `.vscode/mcp.json`.

> ⚠ The root key is **`servers`**, not `mcpServers` — the #1 mistake when
> copying a Claude config.

```json
{
  "servers": {
    "rad-mcp": {
      "type": "stdio",
      "command": "<repo>\\server\\.venv\\Scripts\\python.exe",
      "args": ["-m", "rad_mcp.server"],
      "cwd": "<repo>\\server",
      "env": { "RAD_MCP_INVENTORY": "<repo>\\inventory.yaml" }
    }
  }
}
```

On first start VS Code shows a **trust dialog** — accept it ("MCP: Reset
Trust" clears decisions).

> A Claude `.mcp.json` in the same workspace is fine — each client spawns
> its own instance ([details](../../../INSTALL.md#same-mcp-in-several-clients--several-separate-instances-mode-1)).

That's the **stdio shape** (Copilot launches the server). The **http shape**
connects to a server you run manually — read-only:

```json
{
  "servers": {
    "rad-mcp": {
      "type": "http",
      "url": "https://<host>:8080/mcp",
      "headers": { "Authorization": "Bearer <your-token>" }
    }
  }
}
```

**http mode reminder:** an http entry never starts anything — the server
must already be running, started by you, even on the same machine
([connecting-local-mcp.md](../../connecting-local-mcp.md) /
[connecting-remote-mcp.md](../../connecting-remote-mcp.md)). Only stdio
entries auto-start.

**Switching modes = disabling the previous config:** one `rad-mcp` entry in
`.vscode/mcp.json` — replace its body. Also check the user-level file
("MCP: Open User Configuration") for a duplicate; if a ghost copy appears,
`chat.mcp.discovery.enabled` may be re-importing a Claude config. Restart
the server ("MCP: List Servers" → Restart) or reload the window after.

## Verify

"MCP: List Servers" → rad-mcp running; in **agent mode**, the tools picker
lists the rad-mcp tools.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Server missing | Root key is `servers` not `mcpServers`; check MCP: List Servers → logs; restart server after config edits |
| Server configured but no tools in chat | You're in Ask/Edit mode — switch to **agent mode** |
| Everything gated/greyed out | Copilot Business/Enterprise: org policy "MCP servers in Copilot" must be enabled (an MCP-registry allowlist may also apply) |
| Tools disappear on large setups | VS Code caps a chat request at **128 tools** total — deselect unused servers in the tools picker |

Credentials / hangs: [INSTALL.md → Troubleshooting](../../../INSTALL.md#troubleshooting-all-targets).

## Files / pointers

- [mcp.stdio.sample.json](mcp.stdio.sample.json) / [mcp.http.sample.json](mcp.http.sample.json) — copy into the workspace as `.vscode/mcp.json`, fix paths
- Install script (does MCP + skills together): [`scripts/install/install-copilot-vscode.ps1`](../../../scripts/install/install-copilot-vscode.ps1)
