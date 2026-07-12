# MCP install — Codex IDE extension (VS Code / Cursor / Windsurf / JetBrains)

> **One config, both surfaces:** the Codex IDE extension and Codex in the
> ChatGPT desktop app read the SAME `~/.codex/config.toml` and
> `~/.agents/skills/`. Installing here also installs for the other — only
> the restart step and the UI differ (each surface's folder covers its
> specifics).

**Prerequisite:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine).
Skills are the separate [skills.md](skills.md).

## stdio

Linux paths shown; on Windows the venv python is `.../.venv/Scripts/python.exe`.
In the TOML use expanded absolute paths — TOML does not resolve `$HOME`/`~`.

```toml
[mcp_servers.rad-mcp]
command = "<repo>/rad-mcp-server/server/.venv/bin/python"
args = ["-m", "rad_mcp.server"]
cwd = "<repo>/rad-mcp-server/server"
env = { RAD_MCP_INVENTORY = "<repo>/rad-mcp-server/inventory.yaml" }
startup_timeout_sec = 20
```

## http client (server runs manually, not by Codex; read-only)

```toml
[mcp_servers.rad-mcp]
url = "https://<host>:8080/mcp"
http_headers = { Authorization = "Bearer <your-token>" }
```

**http mode reminder:** an http entry never starts anything — the server
must already be running, started by you, even on the same machine
([connecting-local-mcp.md](../../connecting-local-mcp.md) /
[connecting-remote-mcp.md](../../connecting-remote-mcp.md)). Only stdio
entries auto-start.

**Switching modes = disabling the previous config:** one
`[mcp_servers.rad-mcp]` section — replace its body, or keep both shapes
under two names with `enabled = false` on the inactive one.
`codex mcp remove rad-mcp` deletes an entry.


## Restart + verify (this surface)

**reload the ide window / restart the extension** (config + skills load at startup). Then: `/mcp` and `/skills` in the Codex panel composer.

The extension shares everything with the CLI and desktop app — there is no IDE-specific config file.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Server missing after edits | Config is read at startup — do this surface's restart step |
| Server times out on start | Raise `startup_timeout_sec` (default 10) |

Credentials / hangs: [INSTALL.md → Troubleshooting](../../../INSTALL.md#troubleshooting-all-targets).

## Files / pointers

- [config.sample.toml](config.sample.toml) — append to `~/.codex/config.toml`, fix paths (both modes, one disabled)
- Install script (Windows, MCP + skills together): [`scripts/install/install-codex.ps1`](../../../scripts/install/install-codex.ps1)
- Skills source: [`rad-mcp-server/skills/`](../../../skills/)
