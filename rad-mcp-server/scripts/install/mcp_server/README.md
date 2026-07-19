# Server scripts — run rad-mcp over HTTP

Scripts that install (venv + deps, via the common setup check) and **run the
rad-mcp server as a manually-launched HTTP process**. The window running the
script IS the server — closing it stops it. They configure no client; wire
clients with the scripts in
[`../skills_and_mcp/`](../skills_and_mcp/README.md) (http
mode).

You only need these for the **shared-server** modes — one local instance for
several clients ([connecting-local-mcp.md](../../../docs/connecting-local-mcp.md))
or hosting for other machines
([connecting-remote-mcp.md](../../../docs/connecting-remote-mcp.md)).
The default stdio install needs no server script at all: the client spawns
the server itself.

| Script | What it does |
|---|---|
| `install-and-start-http-mcp-server.ps1` / `.sh` | Verify common setup, then stop any existing server on the port and start the HTTP server (interactive prompts for anything not passed as flags) |

```powershell
.\install-and-start-http-mcp-server.ps1                            # interactive prompts
.\install-and-start-http-mcp-server.ps1 -BindHost 0.0.0.0 -Port 8080 -WriteToken <t>
.\install-and-start-http-mcp-server.ps1 -ReadToken <t> -WriteToken <t> -TlsCert c.pem -TlsKey k.pem
```

Key behaviors:

- **At least one token is required** — http refuses to start unauthenticated.
  `-ReadToken` → `RAD_MCP_TOKENS` (read-only clients); `-WriteToken` →
  `RAD_MCP_WRITE_TOKENS` (read-write: manage devices + config).
- **Tokens persist** in the gitignored `server/.rad-mcp-tokens`, so a restart
  reuses the same values and clients keep working. Delete the file or pass
  `-NewTokens` to rotate.
- **Bind address** — `127.0.0.1` (this machine only), the host's LAN IP, or
  `0.0.0.0`; prompted interactively when `-BindHost` isn't given. Anything
  beyond loopback also needs the firewall/TLS steps in
  [connecting-remote-mcp.md](../../../docs/connecting-remote-mcp.md).
- **TLS** — pass `-TlsCert`/`-TlsKey` to serve https.
- **Knowledge catalog (optional)** — `build/rad-knowledge.sqlite` (the MIB
  catalog the `mib_*` tools + served-mode clients read) is a **gitignored build
  artifact**. The script **always asks about it interactively** (a y/N
  question, never only a flag): if a catalog is **present** it asks *"Rebuild
  the MIB catalog from a MIB directory? (keep current if no) [y/N]"* (default
  keeps it); if **absent** it asks *"Add MIBs now — build the catalog from a MIB
  directory? [y/N]"* (default skips — server still runs, MIB tools disabled, CLI
  + bundled knowledge still work). Answering **y** prompts for a MIB directory
  and builds it (auto-installs `pysmi`, single `--mib-root <dir>`, a few
  minutes). `-BuildCatalog` / `--build-catalog` is only an optional
  non-interactive shortcut (auto-answers y). Already have a prebuilt catalog?
  Drop it at `build/rad-knowledge.sqlite` before starting — it'll be detected
  as present.

## Example run

A typical interactive restart (tokens shown are placeholders — the script
prints your real ones; give the read-only token to clients, keep the
read-write one restricted):

```text
.\install-and-start-http-mcp-server.ps1
Bind address (RAD_MCP_HOST):
  1) 127.0.0.1     (this machine only)
  2) 192.168.56.1     (this host's LAN address - reachable by other machines)
  3) 0.0.0.0       (all interfaces)
Choice [1]: 3
Reusing saved tokens from <repo>\rad-mcp-server\server\.rad-mcp-tokens (-NewTokens to regenerate):
    read-write (RAD_MCP_WRITE_TOKENS):  <write-token>
    read-only  (RAD_MCP_TOKENS):        <read-token>

Port 8080 already in use - stopping existing server (PID 34060) ...
Starting rad-mcp on http://0.0.0.0:8080/mcp  (Ctrl-C to stop)
Reachable on the LAN - internal networks only, never a public interface.

[07/13/26 19:11:10] INFO     Starting MCP server 'rad-mcp' with transport 'http' on
                             http://0.0.0.0:8080/mcp
INFO:     Started server process [2744]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     127.0.0.1:53073 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:53074 - "POST /mcp HTTP/1.1" 200 OK
```

The FastMCP banner appears between the launch line and the INFO log. The
`POST /mcp ... 200 OK` lines are clients connecting — this window IS the
server; keep it open, Ctrl-C stops it.
