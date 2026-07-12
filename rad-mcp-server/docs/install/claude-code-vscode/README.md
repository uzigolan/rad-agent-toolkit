# Install target: Claude Code — VS Code extension

| Capability | Status | Guide |
|---|---|---|
| MCP tools | ✅ project `.mcp.json` (stdio or http) | **[mcp.md](mcp.md)** |
| Skills + slash commands | ✅ plugin or `~/.claude/` | **[skills.md](skills.md)** |

**Prerequisite for MCP:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine)
(venv, `server\.env`, `inventory.yaml`) — once per machine. Skills need no
setup, only the repo files.

The two installs are independent — skills answer syntax/manual questions
even with no MCP wired, and the MCP tools work without skills (but then
nothing teaches the agent the safety rules — install both).

Scripted (both at once): [`scripts/install/install-claude-code.ps1`](../../../scripts/install/install-claude-code.ps1).
Quick combined verify: `/mcp` shows rad-mcp · `/rad-health <device>` runs.
