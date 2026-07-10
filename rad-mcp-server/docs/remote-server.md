# Running rad-mcp as a shared remote server (internal, read-only)

One server, many clients (Claude Desktop, ChatGPT, Cursor, ...) connect by URL
instead of each installing the local venv. **Internal-network use only.**

This is deployment **modes 2 and 3** of the three in
[INSTALL.md](../INSTALL.md#choose-a-deployment-mode-first): "Run it" below
is hosting (mode 2), "Connect a client" is the client side (mode 3).

## Security model (built into the code, not just docs)

- **Read-only, enforced.** `RAD_MCP_TRANSPORT=http` forces `READONLY` on — the
  write tools (`stage_config`, `commit_config`, `save_startup`) are never
  registered. Remote clients get reads only: `cli_help`, `run_show`,
  `run_show_in_context`, `get_config`, `backup_config`, `health_check`,
  `test_connectivity`, `list_devices`. Config changes stay on local stdio.
- **Auth required, fail-closed.** HTTP refuses to start without
  `RAD_MCP_TOKENS`. Every request needs `Authorization: Bearer <token>`;
  missing/wrong token → HTTP 401 (verified).
- **Internal only.** The server needs to reach devices on 172.17.x.x, so it
  lives inside RAD's network. **Do not** bind it to a public interface or put
  it behind a public tunnel — that is a direct path from the internet to
  device access. Bind to the internal interface and rely on network perimeter
  + the token.
- Device credentials in `server/.env` are shared behind the server: anyone
  holding a valid token inherits (read-only) device access. Rotate tokens by
  editing `RAD_MCP_TOKENS` and restarting; give each consumer a distinct token
  so one can be revoked without disturbing others.

## Run it

Generate a token per consumer:

```
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Launch (bind to the host's INTERNAL-network IP so colleagues can reach it;
127.0.0.1 = local test only):

```
$env:RAD_MCP_TRANSPORT = "http"
$env:RAD_MCP_HOST      = "172.17.x.y"     # this host's internal IP (NOT a public one)
$env:RAD_MCP_PORT      = "8080"
$env:RAD_MCP_TOKENS    = "<token-alice>,<token-bob>"
$env:RAD_MCP_INVENTORY = "<repo>/rad-mcp-server/inventory.yaml"
& "<repo>/rad-mcp-server/server/.venv/Scripts/python.exe" -m rad_mcp.server
```

Endpoint: `http://<host>:<port>/mcp`

## HTTPS (native TLS — recommended)

Set a cert + key pair and the same launch serves `https://` directly (no
reverse proxy needed); tokens then never travel in cleartext:

```
$env:RAD_MCP_TLS_CERT = "<path>/cert.pem"
$env:RAD_MCP_TLS_KEY  = "<path>/key.pem"
```

- Both must be set together — one without the other refuses to start; a
  missing file refuses to start (fail-closed, same philosophy as the token
  interlock).
- Endpoint becomes `https://<host>:<port>/mcp`.
- Use a certificate from your internal CA if you have one. For a quick
  self-signed cert (clients must then trust it or skip verification):

  ```
  openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "//CN=<host>"
  ```

- Verified live: TLS handshake + 401-without-token / 200-with-token on
  https (2026-07-10).

## Connect a client

The server speaks streamable-HTTP MCP with bearer auth. Give each client the
URL + its token.

Each [install guide](install/) shows its client's exact http config. Two
special cases:

**Claude Desktop** — UI only (Customize -> Connectors -> URL + Authorization
header): an http entry in `claude_desktop_config.json` is silently ignored
(stdio-only file, verified 2026-07-10). If the connector dialog offers no
custom-header field (OAuth only), Desktop cannot connect to a bearer-token
rad-mcp — run it stdio there instead.

**Cloud clients (ChatGPT etc.)** — they are OUTSIDE RAD's network and cannot
reach an internal-only URL; do not expose the server publicly to satisfy
them. Any on-network MCP client (Cursor, Zed, Gemini CLI, custom) connects
with URL + Authorization header.

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
