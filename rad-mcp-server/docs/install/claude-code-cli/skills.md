# Skills install — Claude Code CLI

Delivers the three skills and the four `/rad-*` slash commands. The MCP
server is the separate [mcp.md](mcp.md). Linux shell shown; repo assumed at
`$HOME/rad-agent-toolkit`.

## User home (primary — works in ANY project)

Same pattern as every other CLI dist (`~/.copilot`, `~/.agents`):

```bash
mkdir -p ~/.claude/skills ~/.claude/commands
cp -r $HOME/rad-agent-toolkit/rad-mcp-server/skills/rad-core $HOME/rad-agent-toolkit/rad-mcp-server/skills/rad-cli-operations $HOME/rad-agent-toolkit/rad-mcp-server/skills/rad-device-mng ~/.claude/skills/
cp $HOME/rad-agent-toolkit/rad-mcp-server/commands/*.md ~/.claude/commands/
```

Re-run the copy after repo updates — home copies don't self-update.

## Alternatives

- **Plugin** (skills + commands + MCP as one managed unit):
  `claude plugin marketplace add $HOME/rad-agent-toolkit/rad-mcp-server`
  (the marketplace manifest lives in the `rad-mcp-server/` subdir, not the
  repo root), then `claude plugin install rad-mcp@rad-marketplace`.
- **Project-local:** run `claude` from the repo root — it reads the repo's
  `.claude/skills/` and `.claude/commands/` directly, nothing to copy.

## Verify

`/rad-health <device-name>` runs; *"rad agent, list the managed devices"*
triggers the skill.

## Files / pointers

- Skills + commands source: [`rad-mcp-server/skills/`](../../../skills/) · [`commands/`](../../../commands/)
