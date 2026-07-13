# Connecting to a LOCAL rad-mcp (stdio or http)

The server runs on the **same machine** as the client(s). Two ways to wire
it — and the choice is really "who owns the server process":

| | stdio (the default) | http on localhost |
|---|---|---|
| Who starts the server | **The client** — spawns it from the config entry, kills/restarts it with the client | **You** — a terminal window/task you launch and keep alive |
| Instances | one private instance **per client** | ONE instance shared by every local client |
| Writes | ✅ full toolset (staged commits, inventory writes) | ❌ read-only, forced in code |
| Config entry shape | "how do I LAUNCH it": `command`/`args`/`cwd`/`env` | "where do I FIND it": `url` + `Authorization` header |

For a server on **another machine**, see
[connecting-remote-mcp.md](connecting-remote-mcp.md).

## stdio — the default

Each client launches its own private instance over stdin/stdout; nothing
listens on the network. This is the only mode with the write tools, and the
right choice for a single-user machine. Your client's section in the
[install guide](../scripts/install/skills_and_mcp_clients/README.md) has the
exact entry syntax (root key and quirks
differ per client; every section shows it).

What multiple stdio clients share vs. don't
([full principle](../INSTALL.md#same-mcp-in-several-clients--several-separate-instances-mode-1)):
disk state is common (`inventory.yaml` re-read every call, `.env` — new keys
picked up automatically, backups, audit log); process state is not (staged
configs and SSH sessions live in one client's instance; restarts are
per-client). **Code changes always need the client to respawn the server**
(reload window / reconnect); inventory and new `.env` keys never do.

## http on localhost — one shared local instance

When several local clients should share ONE server process (single set of
SSH sessions, one instance to restart), run it yourself and point every
client at the loopback URL. The price: the http interlock makes it
read-only — keep one stdio client (or Desktop) if you still need writes.

```powershell
$env:RAD_MCP_TRANSPORT = "http"
$env:RAD_MCP_HOST      = "127.0.0.1"
$env:RAD_MCP_PORT      = "8080"
$env:RAD_MCP_TOKENS    = "<your-token>"
$env:RAD_MCP_INVENTORY = "<repo>/rad-mcp-server/inventory.yaml"
& "<repo>/rad-mcp-server/server/.venv/Scripts/python.exe" -m rad_mcp.server
```

- Generate the token: `python -c "import secrets; print(secrets.token_urlsafe(32))"`
- Every client then uses its guide's **http shape** with
  `http://127.0.0.1:8080/mcp` + the token.
- **The client never starts this server** — if the terminal window closes,
  every local client loses rad-mcp until you relaunch. (An http entry only
  says where to find a server; only stdio entries auto-start one.)
- Claude Desktop can join via the
  [stdio→http bridge](../scripts/install/skills_and_mcp_clients/README.md#claude-desktop--chat--cowork) (its config file
  can't hold http entries).
- Binding `127.0.0.1` means nothing outside this machine can connect — to
  serve colleagues too, switch to the
  [remote hosting flow](connecting-remote-mcp.md) (bind + firewall + TLS).

## Which to pick

Single user, wants writes → **stdio everywhere** (the default install).
Many local clients, reads suffice, one process to manage → **localhost
http**. A good hybrid (field-tested): Desktop on stdio for the write path,
everything else on the shared http instance.
