# Skills install — GitHub Copilot, VS Code

Copilot adopted the open **Agent Skills** standard (GA Dec 2025) — the RAD
skills load as-is, the same folders Claude uses, byte for byte. **No zips**:
folders are the artifact. The MCP server is the separate [mcp.md](mcp.md).

Native Agent Skills needs a **Dec-2025+ Copilot Chat** (`chat.useAgentSkills`).
On older VS Code (e.g. 1.100), use the field-tested
[fallback via instructions files](fallback-older-vscode.md) instead.

## Pick one

- **Working inside this repo?** Nothing to do — Copilot reads the repo's
  `.claude/skills/` directory natively (`chat.useAgentSkills`, on by default).
- **Your own workspace:** copy the three folders from
  `rad-mcp-server/skills/` (`rad-core`, `rad-cli-operations`,
  `rad-device-mng`) into `.github/skills/` of your workspace.
- **All workspaces (user-level):** copy them to `~/.copilot/skills/` (or
  `~/.claude/skills/` — VS Code reads both).

Copy the folders **whole** — `rad-cli-operations` needs its `references/`
knowledge files next to its `SKILL.md`. Re-copy after repo updates.

> The Claude plugin's slash commands (`/rad-health`, …) are a Claude-only
> format; here the skills themselves are invocable as `/rad-core`,
> `/rad-cli-operations`, `/rad-device-mng`, and cover the same ground
> conversationally ("run a health check on <device>").

## Verify

Type `/rad` in Copilot Chat — the three skills autocomplete. Then:
*"rad agent, list the managed devices"*.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Skill never triggers, no error | Invalid frontmatter makes skills **fail silently** — `name` must be lowercase/hyphens and **match the folder name** |
| Skills missing entirely | Copilot Chat predates Agent Skills — use the [fallback](fallback-older-vscode.md) |

## Files / pointers

- [fallback-older-vscode.md](fallback-older-vscode.md) — instructions-files route for pre-Agent-Skills builds (field-tested 2026-07-12)
- Skills source: [`rad-mcp-server/skills/`](../../../skills/)
