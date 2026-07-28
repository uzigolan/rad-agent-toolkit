# rad-mcp stdio preparation: install dependencies and build catalog

This guide walks through `install-stdio-mcp-server.ps1` / `.sh`: what it does,
what to run, and what it writes.

This script prepares local stdio usage only. It does not start an HTTP server
and it does not configure any IDE client entry.

What it prepares:

- Bootstraps `server/.venv` if missing
- Installs server dependencies (`pip install -e server`)
- Reuses saved MIB configuration by default and asks whether to keep it
- Keeps the existing catalog unless you choose to rebuild
- Optionally rebuilds the catalog from baseline or your MIB directory

## 0) Prerequisites

- Run from `rad-mcp-server/scripts/install/mcp_server/`
- Internet/PyPI access on first run (for venv dependency install)
- If your MIBs are outside the repo, know the full path to that directory

## 1) Run the stdio preparation script

Interactive/default:

```powershell
.\install-stdio-mcp-server.ps1
```

```bash
./install-stdio-mcp-server.sh
```

With a custom MIB directory:

```powershell
.\install-stdio-mcp-server.ps1 -MibDir C:\MIBS
```

```bash
./install-stdio-mcp-server.sh --mib-dir /path/to/MIBS
```

Dependencies only (skip catalog build):

```powershell
.\install-stdio-mcp-server.ps1 -SkipCatalog
```

```bash
./install-stdio-mcp-server.sh --skip-catalog
```

### Keep previous MIB configuration (default flow)

When `server/.rad-mcp-stdio-config` exists and no flags are passed, the script
shows the saved MIB setup and asks:

`Keep this configuration (MIBs)? [Y/n]`

- `Y` (default): keep current catalog as-is (no rebuild)
- `n`: reconfigure and optionally rebuild MIB catalog

If you choose rebuild, the script asks for build mode:

- baseline (no extra MIB roots)
- custom MIB directory

> Windows execution-policy note:
>
> ```powershell
> PowerShell -ExecutionPolicy Bypass -File .\install-stdio-mcp-server.ps1
> ```

## 2) What the script writes

- `server/.venv/` (if not already present)
- Installed editable package from `server/`
- `server/.rad-mcp-stdio-config` (saved MIB mode and optional MIB root)
- `build/rad-knowledge.sqlite` (when kept existing or rebuilt)

No HTTP token/config files are created by this script.

## 3) Next step: configure your IDE for stdio

After preparation, run your client installer in stdio mode (for example,
Copilot VS Code installer with stdio/default transport) so the IDE can launch
`rad_mcp.server` directly from `server/.venv`.

Client installers are documented in:

- `../skills_and_mcp/README.md`

## 4) Troubleshooting

- `MIB directory not found`:
  - Verify the directory path and rerun with `-MibDir` / `--mib-dir`.
- `pip install failed`:
  - Usually network/proxy/PyPI access. Fix connectivity and rerun.
- Catalog build failed:
  - Check script output above the failure for parser/dependency details.
  - Rerun with `-SkipCatalog` if you want stdio runtime ready first, then
    build the catalog later.

## 5) Reset to a fresh-clone state

If you want to rebuild from scratch as if the repo was just cloned, remove the
local runtime/build artifacts below.

Required for a clean rebuild:

- `server/.venv/`
- `build/rad-knowledge.sqlite`

Recommended (remove previous generated/build state):

- `build/mib-catalog-report.json`
- `build/snmp-oid-map.generated.json`
- `build/work/`
- `server/.rad-mcp-stdio-config`
- `server/.rad-mcp-http-config`
- `server/.rad-mcp-tokens`

Optional (remove local credentials/device configuration too):

- `server/.env`
- `inventory.yaml`

PowerShell example (from repo root):

```powershell
Remove-Item -Recurse -Force "rad-mcp-server/server/.venv" -ErrorAction SilentlyContinue
Remove-Item -Force "rad-mcp-server/build/rad-knowledge.sqlite","rad-mcp-server/build/mib-catalog-report.json","rad-mcp-server/build/snmp-oid-map.generated.json" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "rad-mcp-server/build/work" -ErrorAction SilentlyContinue
Remove-Item -Force "rad-mcp-server/server/.rad-mcp-stdio-config","rad-mcp-server/server/.rad-mcp-http-config","rad-mcp-server/server/.rad-mcp-tokens" -ErrorAction SilentlyContinue
# Optional:
# Remove-Item -Force "rad-mcp-server/server/.env","rad-mcp-server/inventory.yaml" -ErrorAction SilentlyContinue
```
