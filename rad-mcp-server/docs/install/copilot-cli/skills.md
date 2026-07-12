# Skills install — GitHub Copilot CLI

Native Agent Skills — the RAD skill folders load unmodified, **no zips**.
The MCP server is the separate [mcp.md](mcp.md).

## Pick one

- **Running `copilot` inside this repo?** Nothing to do — the CLI reads the
  repo's `.claude/skills/` natively.
- **Anywhere else — user-level:**

  ```bash
  copilot skill add $HOME/rad-agent-toolkit/rad-mcp-server/skills/rad-core
  copilot skill add $HOME/rad-agent-toolkit/rad-mcp-server/skills/rad-cli-operations
  copilot skill add $HOME/rad-agent-toolkit/rad-mcp-server/skills/rad-device-mng
  ```

  (or copy the folders whole into `~/.copilot/skills/`). Re-copy after repo
  updates.

> ⚠ **Skills load only at CLI startup** — restart the session after adding
> or changing them.

## Verify

`/skills list` — the three rad skills present. Then:
*"rad agent, list the managed devices"* (verified live 2026-07-11: skill
trigger, six-field intake gate, inventory auto-create all worked on a
fresh Linux clone).

## Troubleshooting

| Symptom | Fix |
|---|---|
| Skills not appearing | Added mid-session — restart `copilot`; check `/skills list` |

## Files / pointers

- Skills source (folders only): [`rad-mcp-server/skills/`](../../../skills/)
