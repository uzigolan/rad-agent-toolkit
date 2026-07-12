# Install target: GitHub Copilot — VS Code extension (Copilot Chat, agent mode)

| Capability | Status | Guide |
|---|---|---|
| MCP tools | ✅ `.vscode/mcp.json` — **agent mode only** | **[mcp.md](mcp.md)** |
| Skills | ✅ native Agent Skills (folders, no zips) | **[skills.md](skills.md)** |
| Slash commands | ✅ skills invocable as `/rad-core` etc. (Claude's `/rad-health` format isn't read) | [skills.md](skills.md) |

**Prerequisite for MCP:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine)
— once per machine. Skills need only the repo folders (and inside this repo,
nothing at all — `.claude/skills/` is read natively).

The two installs are independent; install both. Verified live 2026-07-10
(Windows) + 2026-07-12 (second machine: remote http + the older-VS-Code
skills fallback).

Scripted (both at once): [`scripts/install/install-copilot-vscode.ps1`](../../../scripts/install/install-copilot-vscode.ps1).

## Verify (both installs)

| Check | How — Copilot Chat in **agent mode** (MCP is invisible in Ask/Edit) |
|---|---|
| MCP connected | Command Palette → **"MCP: List Servers"** → rad-mcp running; in chat, the **tools picker** (wrench icon) lists the rad-mcp tools |
| Skills loaded | type **`/rad`** → `/rad-core`, `/rad-cli-operations`, `/rad-device-mng` autocomplete; **`/skills`** opens the skills menu |
| Round-trip | say ***"rad agent, list the managed devices"*** |

Sigils here — different from Claude: **`/` = skills and prompt files**,
**`#` = attach files/context** (incl. `.instructions.md` in the fallback
route), **`@` = chat participants** (not skills). Claude's `/rad-health`
command format doesn't exist here.
