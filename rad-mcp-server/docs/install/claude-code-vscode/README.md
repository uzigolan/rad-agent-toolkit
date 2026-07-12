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

## Verify (both installs)

| Check | How — in the Claude panel |
|---|---|
| MCP connected | type **`/mcp`** → rad-mcp listed as connected, with its tools (14 = stdio full set; 8 = read-only http) |
| Skills loaded | say ***"rad agent, list the managed devices"*** — the skill must load by trigger (skills never appear in the `/` menu; they self-activate) |
| Slash commands | type **`/rad`** → `/rad-health`, `/rad-backup`, … autocomplete; run `/rad-health <device>` |

Sigils here: **`/` = slash commands and built-ins** (`/mcp`, `/rad-health`);
skills have no sigil — they trigger on conversation content.
