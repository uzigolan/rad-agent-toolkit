# Install target: Claude Code — CLI

Verified live 2026-07-11 on Linux: user-home install, rad-mcp connected
from a non-repo folder — the "works in any project" usage shape.

| Capability | Status | Guide |
|---|---|---|
| MCP tools | ✅ `claude mcp add -s user` (stdio or http) | **[mcp.md](mcp.md)** |
| Skills + slash commands | ✅ `~/.claude/` or plugin | **[skills.md](skills.md)** |

**Prerequisite for MCP:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine)
— once per machine (Linux venv build is in mcp.md). Skills need only the
repo files.

The two installs are independent; install both — tools without the skills
lose the safety rules, skills without tools still answer syntax/manual
questions.

Scripted (both at once, Windows): [`scripts/install/install-claude-code.ps1`](../../../scripts/install/install-claude-code.ps1).

## Verify (both installs)

| Check | How |
|---|---|
| MCP connected | shell: **`claude mcp list`** → rad-mcp ✔ Connected; in-session: **`/mcp`** (14 tools = stdio; 8 = http) |
| Skills loaded | say ***"rad agent, list the managed devices"*** — the skill must load by trigger (no menu lists skills; they self-activate) |
| Slash commands | type **`/rad`** → the four `/rad-*` commands autocomplete; run `/rad-health <device>` |

Sigils here: **`/` = slash commands and built-ins**; skills have no sigil —
they trigger on conversation content.
