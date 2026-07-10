# Install target: Claude Code — CLI

| Capability | Status |
|---|---|
| MCP tools | ✅ |
| Skills (rad-core, rad-cli-operations, rad-device-mng) | ✅ via plugin |
| Slash commands | ✅ `/rad-health`, `/rad-backup`, `/rad-harvest`, `/rad-load-manual` |

**Prerequisite:** the [common setup](../../INSTALL.md#common-setup-once-per-machine)
(venv, `server\.env`, `inventory.yaml`, smoke test) — once per machine.

## Everything at once (plugin)

```bash
claude plugin marketplace add <path-to-this-repo>
claude plugin install rad-mcp@rad-marketplace
```

The plugin carries the MCP server registration, the skills, and the slash
commands in one unit.

## MCP server only (no plugin system)

```bash
claude mcp add rad-mcp -- <repo>/server/.venv/Scripts/python.exe -m rad_mcp.server
```

## The other mode: http client (server runs manually, not by Claude)

Works for a colleague's server ([remote-server.md](../remote-server.md)) or
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

See [INSTALL.md → Troubleshooting](../../INSTALL.md#troubleshooting-all-targets)
(credentials, hangs, missing write tools).
