# Connecting to a REMOTE rad-mcp (http only)

The server runs on **another machine**; clients reach it by URL + bearer
token. This is deployment **modes 2 and 3** of
[INSTALL.md](../INSTALL.md#choose-a-deployment-mode-first): "Host it" below
is mode 2, "Connect a client" is mode 3. **Internal-network use only.**
For a server on the *same* machine as the client — stdio or localhost
http — see [connecting-local-mcp.md](connecting-local-mcp.md).

## Security model (built into the code, not just docs)

- **Read-only, enforced.** `RAD_MCP_TRANSPORT=http` forces `READONLY` on — the
  write tools (`stage_config`, `commit_config`, `save_startup`, inventory
  writes) are never registered. Remote clients get reads only: `cli_help`,
  `run_show`, `run_show_in_context`, `get_config`, `backup_config`,
  `health_check`, `test_connectivity`, `list_devices`.
- **Auth required, fail-closed.** HTTP refuses to start without
  `RAD_MCP_TOKENS`. Every request needs `Authorization: Bearer <token>`;
  missing/wrong token → HTTP 401 (verified).
- **Internal only.** The server reaches devices on 172.17.x.x, so it lives
  inside RAD's network. **Do not** bind it to a public interface or put it
  behind a public tunnel. Bind internal and rely on network perimeter + the
  token.
- Device credentials in `server/.env` stay on the host: a token holder
  inherits (read-only) device access, never the credentials. Give each
  consumer a distinct token; rotate by editing `RAD_MCP_TOKENS` + restart.

## Host it (mode 2)

Generate a token per consumer:

```
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Launch — bind beyond loopback so others can reach you (`0.0.0.0` = all
interfaces, keeps your own localhost clients working too; or the specific
internal IP):

```powershell
$env:RAD_MCP_TRANSPORT = "http"
$env:RAD_MCP_HOST      = "0.0.0.0"        # or this host's internal IP — never a public one
$env:RAD_MCP_PORT      = "8080"
$env:RAD_MCP_TOKENS    = "<token-alice>,<token-bob>"
$env:RAD_MCP_INVENTORY = "<repo>/rad-mcp-server/inventory.yaml"
& "<repo>/rad-mcp-server/server/.venv/Scripts/python.exe" -m rad_mcp.server
```

Open the Windows firewall once (admin PowerShell):

```powershell
New-NetFirewallRule -DisplayName "rad-mcp shared" -Direction Inbound -Protocol TCP -LocalPort 8080 -Action Allow
```

Endpoint: `http://<host>:<port>/mcp`. The terminal window IS the server —
closing it cuts every consumer off; for standing service register the launch
as a scheduled task ("At log on", hidden).

## HTTPS (native TLS — recommended once tokens cross the LAN)

Set a cert + key pair and the same launch serves `https://` directly (no
reverse proxy needed):

```powershell
$env:RAD_MCP_TLS_CERT = "<path>/cert.pem"
$env:RAD_MCP_TLS_KEY  = "<path>/key.pem"
```

- Both together or it refuses to start; missing file refuses too
  (fail-closed, like the token interlock).
- Endpoint becomes `https://<host>:<port>/mcp`.
- Prefer an internal-CA cert; quick self-signed (clients must then trust it
  or skip verification):

  ```
  openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "//CN=<host>"
  ```

- Verified live: TLS handshake + 401-without-token / 200-with-token (2026-07-10).

## Connect a client (mode 3)

You need three things from the host: **network reach** (RAD network/VPN),
the **URL**, and **your own bearer token**. Each
[install guide](install/) shows your client's exact http config. Two
special cases:

**Claude Desktop** — its config file is stdio-only (http entries silently
ignored, verified 2026-07-10). Use Customize → Connectors (URL +
Authorization header), or the file-only route: the
[stdio→http bridge](install/claude-desktop/README.md).

**Cloud clients (ChatGPT etc.)** — OUTSIDE RAD's network; they cannot reach
an internal-only URL, and the server must never be exposed publicly to
satisfy them. Any on-network MCP client (Cursor, Zed, Gemini CLI, custom)
connects with URL + Authorization header.

## Quick auth check

```
# 401 without a token:
curl -sL -o /dev/null -w "%{http_code}\n" -X POST http://<host>:8080/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
# 200 with a valid token + initialize.
```

## Not covered yet (future)

- Remote *write* access (staged commits over HTTP) — deliberately excluded;
  higher risk tier, revisit with per-token scopes if needed.
- External/cloud reach — needs a hardened gateway + likely OAuth, not a tunnel.
