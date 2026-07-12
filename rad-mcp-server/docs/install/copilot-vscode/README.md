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
Quick combined verify: agent mode → tools picker shows rad-mcp · `/rad` autocompletes the skills.
