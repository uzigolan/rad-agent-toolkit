# MCP install — GitHub Copilot CLI

**Prerequisite:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine)
— once per machine. Linux venv build (RHEL-family needs `python3.11`
explicitly; never move/rename the repo after — the venv symlink breaks):

```bash
cd $HOME/rad-agent-toolkit/rad-mcp-server/server
python3.11 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -e .
```

Skills are the separate [skills.md](skills.md).

## stdio (type "local")

Either run `/mcp add` inside a `copilot` session, or create/merge
`~/.copilot/mcp-config.json` directly. Windows command path:
`<repo>\server\.venv\Scripts\python.exe`; Linux shown here:

```json
{
  "mcpServers": {
    "rad-mcp": {
      "type": "local",
      "command": "<repo>/rad-mcp-server/server/.venv/bin/python",
      "args": ["-m", "rad_mcp.server"],
      "env": { "RAD_MCP_INVENTORY": "<repo>/rad-mcp-server/inventory.yaml" },
      "tools": ["*"]
    }
  }
}
```

Notes:
- Root key here **is** `mcpServers` (unlike VS Code's `servers`); stdio
  type is `"local"`.
- **No `cwd` support** — safe: all server paths are module-anchored, and
  the inventory comes from the env var.
- `tools: ["*"]` exposes all tools; list specific ones to narrow.
- **Launch-directory discovery** (verified 2026-07-11): the CLI also picks
  up an `.mcp.json` in the directory you launch `copilot` from. This repo
  ships one with the committing machine's paths — launching from the repo
  root elsewhere fails to spawn until you rewrite it with local paths.

## http client (server runs manually, not by Copilot; read-only)

Same file, same entry name, different body:

```json
{
  "mcpServers": {
    "rad-mcp": {
      "type": "http",
      "url": "https://<host>:8080/mcp",
      "headers": { "Authorization": "Bearer <your-token>" },
      "tools": ["*"]
    }
  }
}
```

**http mode reminder:** an http entry never starts anything — the server
must already be running, started by you, even on the same machine
([connecting-local-mcp.md](../../connecting-local-mcp.md) /
[connecting-remote-mcp.md](../../connecting-remote-mcp.md)). Only
stdio/local entries auto-start.

**Switching modes = disabling the previous config:** one `rad-mcp` entry —
replace its body (or `/mcp` → remove first), then **restart the session**
(config is read at startup).

## Verify

`/mcp show` — rad-mcp listed and running. First tool call prompts for
permission — "yes, always" persists it. Non-interactive runs
(`copilot -p "..."`) need `--allow-tool 'rad-mcp(*)'`.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Server missing from `/mcp show` | Root key must be `mcpServers`; check both sources: `~/.copilot/mcp-config.json` and a launch-directory `.mcp.json` |
| "failed to spawn MCP server process: No such file or directory" | The `command` path doesn't exist here — a repo-shipped `.mcp.json` with foreign paths (rewrite locally) or a moved/renamed venv (rebuild) |
| Everything gated | Org policy "MCP servers in Copilot" applies to the CLI too |
| Tool calls silently skipped in `-p` mode | Pass `--allow-tool` / `--allow-all-tools` |

Credentials / hangs: [INSTALL.md → Troubleshooting](../../../INSTALL.md#troubleshooting-all-targets).

## Files / pointers

- [mcp-config.stdio.sample.json](mcp-config.stdio.sample.json) / [mcp-config.http.sample.json](mcp-config.http.sample.json) — merge into `~/.copilot/mcp-config.json`, fix paths
- Install script (Windows, MCP + skills together): [`scripts/install/install-copilot-cli.ps1`](../../../scripts/install/install-copilot-cli.ps1)
