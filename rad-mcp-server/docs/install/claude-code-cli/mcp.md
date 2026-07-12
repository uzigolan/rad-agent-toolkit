# MCP install — Claude Code CLI

Linux shell shown (the CLI's usual home); on Windows the only change is the
venv path (`.venv\Scripts\python.exe`). Examples assume the repo at
`$HOME/rad-agent-toolkit`. Skills/commands are the separate
[skills.md](skills.md).

**Prerequisite:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine).
Linux venv build:

```bash
cd $HOME/rad-agent-toolkit/rad-mcp-server/server
python3.11 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -e .
```

## stdio, user scope (primary — works in ANY project)

```bash
claude mcp add -s user rad-mcp --env RAD_MCP_INVENTORY=$HOME/rad-agent-toolkit/rad-mcp-server/inventory.yaml -- $HOME/rad-agent-toolkit/rad-mcp-server/server/.venv/bin/python -m rad_mcp.server
```

The entry lands in `~/.claude.json`; the repo stays the engine room (venv,
`.env`, inventory, backups) — you never need to run `claude` inside it.
Project-local alternative: run `claude` from the repo root — it reads the
repo's `.mcp.json` (rewrite its paths first; it ships with the committing
machine's).

## The other mode: http client (server runs manually, not by Claude)

Works for a colleague's server
([connecting-remote-mcp.md](../../connecting-remote-mcp.md)) or one you host
yourself — read-only tools, no venv needed on the client side.

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

**http mode reminder:** an http entry never starts anything — the server
must already be running, started by you, even on the same machine
([connecting-local-mcp.md](../../connecting-local-mcp.md) /
[connecting-remote-mcp.md](../../connecting-remote-mcp.md)). Only stdio
entries auto-start.

## Verify

`claude mcp list`, then `/mcp` inside a session.

## Troubleshooting

See [INSTALL.md → Troubleshooting](../../../INSTALL.md#troubleshooting-all-targets)
(credentials, hangs, missing write tools).

## Files / pointers

- No sample files — this target is command-driven; the blocks above are the artifacts
- Install script (Windows, does MCP + skills together): [`scripts/install/install-claude-code.ps1`](../../../scripts/install/install-claude-code.ps1)
