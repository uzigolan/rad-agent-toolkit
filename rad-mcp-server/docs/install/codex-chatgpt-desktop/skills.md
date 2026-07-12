# Skills install — Codex in the ChatGPT desktop app

> **One config, both surfaces:** the Codex IDE extension and Codex in the
> ChatGPT desktop app read the SAME `~/.codex/config.toml` and
> `~/.agents/skills/`. Installing here also installs for the other — only
> the restart step and the UI differ (each surface's folder covers its
> specifics).

Native Agent Skills — the RAD skill folders load unmodified, no zips. The
MCP server is the separate [mcp.md](mcp.md).

## Copy the folders

From `rad-mcp-server/skills/` (`rad-core`, `rad-cli-operations`,
`rad-device-mng`) — whole, `references/` included — into one of:

- `~/.agents/skills/` — user-level, applies everywhere (recommended)
- `<your-repo>/.agents/skills/` — per-project

Note: Codex reads `.agents/skills/`, NOT `.claude/skills/` (unlike
Copilot). Re-copy after repo updates.

## Behavioral caveat (Codex engine-wide; observed live 2026-07-11)

**Don't rely on skill-level safety rules on Codex:** in a ChatGPT-desktop
session the skill failed to load and Codex executed a device read without
the mandatory "Run this on the device now?" confirmation. The code
interlocks (read-only http, staged writes, whitelists) still held. Two
mitigations, use both:

1. Add the gate to `~/.codex/AGENTS.md` — re-read every run, unlike skills:
   *"RAD devices: before executing ANY device command — read-only included —
   show the command and ask for explicit confirmation."*
2. Say it explicitly at session start when it matters.

## Restart + verify (this surface)

**fully quit and relaunch the app** (config + skills load at startup). Then: Settings → **Plugins → MCPs** lists rad-mcp with an enabled toggle; **Plugins → Skills** lists the three rad skills; then a local Codex session: *\"rad agent, list the managed devices\"*.

## Files / pointers

- Skills source: [`rad-mcp-server/skills/`](../../../skills/) → `~/.agents/skills/`
- The `~/.codex/AGENTS.md` backstop (above) — treat it as part of the skills install on Codex
