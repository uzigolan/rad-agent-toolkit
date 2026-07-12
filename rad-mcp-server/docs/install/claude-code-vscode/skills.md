# Skills install — Claude Code, VS Code extension

Delivers the three skills (`rad-core`, `rad-cli-operations`,
`rad-device-mng`) **and** the four slash commands (`/rad-health`,
`/rad-backup`, `/rad-harvest`, `/rad-load-manual`). The MCP server is the
separate [mcp.md](mcp.md).

## Via the plugin (workspace scope)

In `.claude/settings.json` of the workspace:

```json
{
  "extraKnownMarketplaces": {
    "rad-marketplace": {
      "source": { "source": "directory", "path": "<absolute-path-to-repo>" }
    }
  },
  "enabledPlugins": { "rad-mcp@rad-marketplace": true }
}
```

Then reload the window (Ctrl+Shift+P → "Developer: Reload Window").

## Alternative: user home (works in ANY project)

```bash
mkdir -p ~/.claude/skills ~/.claude/commands
cp -r <repo>/rad-mcp-server/skills/rad-core <repo>/rad-mcp-server/skills/rad-cli-operations <repo>/rad-mcp-server/skills/rad-device-mng ~/.claude/skills/
cp <repo>/rad-mcp-server/commands/*.md ~/.claude/commands/
```

(Same pattern as the other dists' home dotfolders; re-run the copy after
repo updates — home copies don't self-update.)

## Verify

Try `/rad-health <device-name>`, or say *"rad agent, list the managed
devices"* — the skill should load by trigger.

## Files / pointers

- Skills + commands source: [`rad-mcp-server/skills/`](../../../skills/) · [`commands/`](../../../commands/) (the plugin delivers both)
- Skill vs slash command, if the distinction is fuzzy: [INSTALL.md, Part 1](../../../INSTALL.md#the-three-artifact-kinds-used-throughout-these-docs)
