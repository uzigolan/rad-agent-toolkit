# Install target: Claude Code — CLI

Verified live 2026-07-11 on Linux: user-home install, rad-mcp connected
from a non-repo folder — the "works in any project" usage shape.

| Capability | Status |
|---|---|
| MCP tools | ✅ |
| Skills (rad-core, rad-cli-operations, rad-device-mng) | ✅ via plugin |
| Slash commands | ✅ `/rad-health`, `/rad-backup`, `/rad-harvest`, `/rad-load-manual` |

CLI installs typically live on Linux — all commands below are Linux shell.
(On Windows the only change is the venv path: `.venv\Scripts\python.exe`
instead of `.venv/bin/python`.)

**Prerequisite:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine)
— once per machine. Linux venv build:

Examples assume the repo cloned at `$HOME/rad-agent-toolkit` — adjust if
elsewhere.

```bash
cd $HOME/rad-agent-toolkit/rad-mcp-server/server
python3.11 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -e .
```

## Install to your user home (primary — works in ANY project)

The same pattern as every other CLI dist (`~/.copilot`, `~/.agents`):
install once into `~/.claude`, then `claude` finds it from any project
folder. The repo stays the engine room (venv, `.env`, `inventory.yaml`,
backups) — you never need to run claude inside it.

```bash
claude mcp add -s user rad-mcp --env RAD_MCP_INVENTORY=$HOME/rad-agent-toolkit/rad-mcp-server/inventory.yaml -- $HOME/rad-agent-toolkit/rad-mcp-server/server/.venv/bin/python -m rad_mcp.server
mkdir -p ~/.claude/skills ~/.claude/commands
cp -r $HOME/rad-agent-toolkit/rad-mcp-server/skills/rad-core $HOME/rad-agent-toolkit/rad-mcp-server/skills/rad-cli-operations $HOME/rad-agent-toolkit/rad-mcp-server/skills/rad-device-mng ~/.claude/skills/
cp $HOME/rad-agent-toolkit/rad-mcp-server/commands/*.md ~/.claude/commands/
```

All three artifact kinds land user-level: the MCP entry in `~/.claude.json`
(`-s user`), the three skills in `~/.claude/skills/`, the four `/rad-*`
commands in `~/.claude/commands/`.

## Alternatives

- **Plugin:** `claude plugin marketplace add $HOME/rad-agent-toolkit/rad-mcp-server`
  (the marketplace manifest lives in the `rad-mcp-server/` subdir, not the
  repo root) then `claude plugin install rad-mcp@rad-marketplace` — same
  three artifact kinds as one managed unit.
- **Project-local:** run `claude` from the repo root — it reads the repo's
  `.mcp.json`, `.claude/skills/`, and `.claude/commands/` directly; rewrite
  `.mcp.json` with local paths first (it ships with the committing
  machine's).

## The other mode: http client (server runs manually, not by Claude)

Works for a colleague's server ([remote-server.md](../../remote-server.md)) or
one you host yourself — read-only tools, no venv needed on the client side.

**Disable the previous config first** (one `rad-mcp` per scope; skip
whichever doesn't exist):

```bash
claude mcp remove rad-mcp
claude plugin uninstall rad-mcp@rad-marketplace
```

Then add the http entry:

```bash
claude mcp add --transport http rad-mcp https://<host>:8080/mcp --header "Authorization: Bearer <token>"
```

Switching back to stdio: `claude mcp remove rad-mcp` again, then re-add the
stdio form from above. Verify after any switch: `claude mcp list`.

## Verify

`claude mcp list`, then `/mcp` inside a session. Try
`/rad-health <device-name>`.

## Troubleshooting

See [INSTALL.md → Troubleshooting](../../../INSTALL.md#troubleshooting-all-targets)
(credentials, hangs, missing write tools).

**http mode reminder:** an http entry never starts anything — the server must already be running as a separate process, started by you, even when it lives on the same machine as this client. Launch block: [remote-server.md](../../remote-server.md). Only stdio entries auto-start.

## In this folder / pointers

- No sample files — this target is command-driven (`claude mcp add`, `cp` to `~/.claude/`); the blocks above are the artifacts
- Install script (Windows): [`scripts/install/install-claude-code.ps1`](../../../scripts/install/install-claude-code.ps1)
- Skills + commands source: [`rad-mcp-server/skills/`](../../../skills/) · [`commands/`](../../../commands/)
