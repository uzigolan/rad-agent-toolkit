# rad-mcp HTTP server: install & run

This guide walks through `install-and-start-http-mcp-server.ps1` / `.sh`: what
to run, what to answer at each prompt, what it writes, and how to connect a
client. The script sets up the server venv (once), then **runs rad-mcp as a
manually-launched HTTP process** — the window/terminal running the script **is**
the server; closing it (or Ctrl-C) stops it. It configures **no** client — wire
clients separately (see step 3).

> You only need this for the **shared-server** modes — one local instance for
> several clients, or hosting for other machines. The default stdio install
> needs no server script at all (the client spawns the server itself).

## 0) Prerequisites

- **Python 3.10+** on PATH (3.11+ recommended). The script auto-creates the
  server venv on first run; if no suitable Python is found it falls back to a
  repo-local portable CPython download.
- **Network / PyPI access** on first run only (to `pip install` the server and
  its dependencies into the venv). Behind a corporate proxy, set
  `HTTP_PROXY`/`HTTPS_PROXY` first, or configure pip's index/trusted-host.
- Run from this directory: `rad-mcp-server/scripts/install/mcp_server/`.

## 1) Run the installer

Interactive (prompts for anything not passed as a flag):

```
.\install-and-start-http-mcp-server.ps1        # Windows PowerShell
./install-and-start-http-mcp-server.sh         # Linux / macOS
```

Non-interactive examples:

```
.\install-and-start-http-mcp-server.ps1 -BindHost 0.0.0.0 -Port 8080 -WriteToken <token>
.\install-and-start-http-mcp-server.ps1 -ReadToken <t> -WriteToken <t> -TlsCert cert.pem -TlsKey key.pem
```

> **Windows: "running scripts is disabled on this system"** — run it through a
> one-off bypass (no persistent policy change):
> ```
> PowerShell -ExecutionPolicy Bypass -File .\install-and-start-http-mcp-server.ps1
> ```

### What to answer at the prompts

| Prompt | Options | Guidance |
|---|---|---|
| **Devices** (only when `inventory.yaml` already has devices) | `use` / `reset` | `use` (default) keeps the existing inventory untouched. `reset` removes **all devices AND all their secrets** — usernames, passwords, SNMP communities — from `server/.env` (server config keys like tokens/TLS are preserved; both files get a timestamped `.bak` first). Non-interactive: `-KeepDevices` / `-ResetDevices` (`--keep-devices` / `--reset-devices`). Re-add devices afterwards with `add_device` + `set_device_credentials`. |
| **Bind address** | `127.0.0.1` / this host's LAN IP / `0.0.0.0` | `127.0.0.1` = this machine only. Anything reachable beyond loopback also needs the firewall/TLS steps — **internal networks only, never a public interface.** |
| **Token(s)** | read-write / read-only / **both** | At least one token is required (http refuses to start unauthenticated). "both" gives one read-write + one read-only so you can hand out whichever role per client. |
| **TLS** | No TLS / Self-signed / Imported | Plain HTTP works for local clients (VS Code / Codex / Copilot). **Claude Desktop and most hosted clients require HTTPS** — pick self-signed (fastest) or import your own PEM cert + key. |
| **MIBs (knowledge catalog)** | present → *Rebuild?* / absent → *Add MIBs?* [y/N] | Optional. `N` keeps/skips it — the server still runs; the `mib_*` tools are just disabled. `y` prompts for a MIB directory and builds the catalog (auto-installs `pysmi`, a few minutes). |

On a **re-run**, a saved configuration is shown (bind host, port, name, TLS,
tokens, MIBs) and you're asked **"Keep this configuration (incl. MIBs)? [Y/n]"**
— `Y` reuses everything (including the MIB catalog as-is) and skips every prompt;
`n` reconfigures from scratch.

## 2) What the script writes

Both files live in `server/` and are **gitignored** (reused on the next start):

- `server/.rad-mcp-tokens` — the bearer token(s). Pass `-NewTokens` /
  `--new-tokens` to rotate.
- `server/.rad-mcp-http-config` — bind host / port / name / TLS paths.

Then it starts the server in the foreground: `Starting rad-mcp on
http(s)://<host>:<port>/mcp`. **Keep the window open** — it *is* the server;
`Ctrl-C` stops it. (A `GET /mcp → 404` from a browser is normal — MCP uses
`POST`.)

## 3) Connect a client (http mode)

This script only runs the **server**. Point a client at it with the matching
installer in **http mode**, using the URL + one of the tokens:

```
.\install-copilot-vscode.ps1 -Http -Url http://<host>:8080/mcp -Token <token>
```

See [../skills_and_mcp/README.md](../skills_and_mcp/README.md) for every client.
A client's `Authorization: Bearer <value>` must match a token **exactly**, or it
gets `401 Unauthorized`; the role (read-only vs read-write) follows the token it
uses. Over http the toolset is **read-only** unless the client presents a
read-write token.

## 4) Security reminder

- **At least one token, always** — the server refuses to start unauthenticated.
  Give clients the **read-only** token by default; keep the read-write one
  (device management + staged config) restricted.
- **Bind scope** — `127.0.0.1` unless a remote client genuinely needs it. LAN /
  `0.0.0.0` on **internal networks only**, never a public interface.
- **TLS** for anything beyond localhost, and always for Claude Desktop.
- Tokens live only in the gitignored `.rad-mcp-tokens`; if one leaks, rotate
  with `-NewTokens` and update every client.

## 5) Troubleshooting

- **`ModuleNotFoundError: No module named 'fastmcp'` / venv issues** — a prior
  interrupted run can leave a half-built venv. The installer now detects this
  (verifies `rad_mcp` imports) and **rebuilds the venv clean** automatically on
  the next run. If the venv python is locked (a server is still running from
  it), stop that server first, then re-run.
- **`pip install failed`** — pip's actual error is printed above the message:
  no PyPI access / proxy (`Connection timed out`, `ProxyError`), SSL
  interception (`CERTIFICATE_VERIFY_FAILED` → `--trusted-host` / your CA), or a
  dependency needing build tools. Fix that, then re-run.
- **Port already in use** — the script stops any existing server on the port
  before starting, so re-running just restarts it.
- **`knowledge catalog: skipped`** — expected if you answered `N` to MIBs; CLI +
  bundled knowledge still work, only the `mib_*` catalog tools are off. Re-run
  and answer `y` (or drop a prebuilt `rad-knowledge.sqlite` into `build/`) to
  enable them.
