# Install target: Codex IDE extension (VS Code / Cursor / Windsurf / JetBrains)

> **One config, both surfaces:** the Codex IDE extension and Codex in the
> ChatGPT desktop app read the SAME `~/.codex/config.toml` and
> `~/.agents/skills/`. Installing here also installs for the other — only
> the restart step and the UI differ (each surface's folder covers its
> specifics).

| Capability | Status | Guide |
|---|---|---|
| MCP tools | ✅ `~/.codex/config.toml` | **[mcp.md](mcp.md)** |
| Skills | ⚠ `~/.agents/skills/` — loads unreliably; `AGENTS.md` backstop | **[skills.md](skills.md)** |
| Slash commands | `$skill-name` / `/skills` | [skills.md](skills.md) |

**Surface verification:** ⏳ config shared with the verified desktop surface; no dedicated IDE session test yet.

**Prerequisite for MCP:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine)
— once per machine. Skills need only the repo folders. The two installs are
independent; install both, plus the `AGENTS.md` backstop (skills.md).

**Restart for this surface:** **reload the IDE window / restart the extension** (config + skills load at startup).
Quick verify: `/mcp` and `/skills` in the Codex panel composer.

Scripted (both at once, Windows): [`scripts/install/install-codex.ps1`](../../../scripts/install/install-codex.ps1).
