# Install target: Claude Desktop (chat + Cowork)

| Capability | Status | Guide |
|---|---|---|
| MCP tools | ✅ config file (stdio) · shared server via Connectors UI or the bridge | **[mcp.md](mcp.md)** |
| Skills | ✅ zip upload (manual refresh) | **[skills.md](skills.md)** |
| Slash commands | ❌ — plain language only | — |

**Prerequisite for MCP:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine)
— once per machine. Skills need only the built zips.

The two installs are independent; install both. Desktop specifics to
remember: config changes need a **tray-quit** restart, and skill zips are
snapshots needing re-upload after repo updates.

Scripted (MCP + zips): [`scripts/install/install-claude-desktop.ps1`](../../../scripts/install/install-claude-desktop.ps1).
Quick combined verify: tools icon lists rad-mcp · *"run a health check on <device>"* works in plain language.
