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

## Verify (both installs)

| Check | How — in the Desktop app |
|---|---|
| MCP connected | click the **tools icon** near the message box → rad-mcp listed with its tools (config problems: `%APPDATA%\Claude\logs\mcp*.log`) |
| Skills loaded | sidebar **Customize → Skills** → the three rad skills present and enabled |
| Round-trip | ask in plain language: ***"run a health check on <device>"*** — no slash commands exist on Desktop |

Sigils here: **none** — Desktop is plain-language only; `/` does nothing.
