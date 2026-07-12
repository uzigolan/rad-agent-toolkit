# Install target: Codex in the ChatGPT desktop app

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

**Surface verification:** ✅ verified live 2026-07-11 (app 27.7, engine 0.144.0-alpha.4, GPT-5.6 Sol) — MCP via shared http server; Plugins → MCPs UI honored `enabled` flags.

**Prerequisite for MCP:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine)
— once per machine. Skills need only the repo folders. The two installs are
independent; install both, plus the `AGENTS.md` backstop (skills.md).

**Restart for this surface:** **fully quit and relaunch the app** (config + skills load at startup).

Scripted (both at once, Windows): [`scripts/install/install-codex.ps1`](../../../scripts/install/install-codex.ps1).

## Verify (both installs)

| Check | How — in the ChatGPT desktop app (Codex mode, NOT Work/chat) |
|---|---|
| MCP connected | **Settings → Plugins → MCPs** → rad-mcp with an enabled toggle (verified: toggles map to config.toml `enabled` flags); in-session **`/mcp`** also works |
| Skills loaded | **Settings → Plugins → Skills** → the three rad skills; in-session **`/skills`** |
| Round-trip | in a **local** Codex session: ***"rad agent, list the managed devices"*** — approve the tool prompt |

Sigils here: **`/` = built-ins**, **`$` = explicit skill invocation**
(`$rad-cli-operations`). Reminder: regular ChatGPT chat (Work mode) reads
neither config.toml nor skills.
