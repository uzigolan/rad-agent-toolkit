# Running rad-mcp as a shared remote server (internal, read-only)

One server, many clients (Claude Desktop, ChatGPT, Cursor, ...) connect by URL
instead of each installing the local venv. **Internal-network use only.**

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
setx RAD_MCP_TRANSPORT http
$env:RAD_MCP_TRANSPORT = "http"
$env:RAD_MCP_HOST      = "172.17.x.y"     # this host's internal IP (NOT a public one)
$env:RAD_MCP_PORT      = "8080"
$env:RAD_MCP_TOKENS    = "<token-alice>,<token-bob>"
$env:RAD_MCP_INVENTORY = "<repo>/rad-mcp-server/inventory.yaml"
& "<repo>/rad-mcp-server/server/.venv/Scripts/python.exe" -m rad_mcp.server
```

Endpoint: `http://<host>:<port>/mcp`

## Connect a client

The server speaks streamable-HTTP MCP with bearer auth. Give each client the
URL + its token.

**Claude Desktop** — Customize -> Connectors -> add a custom/remote MCP server:
- URL: `http://<host>:8080/mcp`
- Header: `Authorization: Bearer <token>`

**ChatGPT** (Pro/Enterprise custom connector, where available): add an MCP
connector with the same URL + Authorization header. NOTE: cloud ChatGPT is
OUTSIDE RAD's network — it cannot reach an internal-only URL. It works only
from a client on the internal network/VPN. Do not expose the server publicly
to satisfy a cloud client.

**Generic MCP client** (Cursor, Zed, Gemini CLI, custom): point its HTTP/SSE
MCP config at the URL and set the Authorization header.

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
- TLS: put the server behind an internal reverse proxy for https:// if tokens
  must not travel in cleartext even internally.
