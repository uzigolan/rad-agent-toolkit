# Installing rad-mcp

One codebase, six agent targets. **Part 1** below explains the principles —
true for every client. **Part 2** maps them to your specific target
(full per-target guides in [docs/install/](docs/install/)). For all the
project's principles beyond installation, see
[docs/CONCEPTS.md](docs/CONCEPTS.md).

---

# Part 1 — Principles (the same for every client)

## The three artifact kinds (used throughout these docs)

| Artifact | What it is | How it activates | Portability |
|---|---|---|---|
| **MCP server** (tools) | The *verbs* — executable device operations (`run_show`, `health_check`, `stage_config`, …) | Agent calls tools during a task; wired per client via an MCP config entry | Any MCP client — all six targets |
| **Skills** | The *knowledge* — `rad-core` (safety rules), `rad-cli-operations` (CLI expertise + personas), `rad-device-mng` (inventory workflow) | Auto-loads when the conversation matches the skill description | Agent Skills open standard — Claude, Copilot, Codex, unmodified |
| **Slash commands** | The *procedures* — `/rad-health`, `/rad-backup`, `/rad-harvest`, `/rad-load-manual` | Only when explicitly typed | Claude Code only (elsewhere: ask in plain language) |

Rule of thumb: tools **do**, skills **know**, commands **orchestrate**.

**Skill vs slash command — the pair people mix up:** a skill is knowledge
that should *always be on* — it loads itself whenever the conversation is
relevant, and you never type its name (`skills/<name>/SKILL.md` folders,
Agent Skills standard, portable to Copilot/Codex). A slash command is a
procedure you *deliberately fire* — nothing happens until you type
`/rad-harvest <device>` (`commands/<name>.md` files with `$ARGUMENTS`
templating, Claude-plugin format, Claude Code only). That's why
`/rad-harvest` never appears in a skills listing: it's a command, and on
Copilot/Codex you get its effect by asking in plain language instead.

## Choose a deployment mode first

| Mode | What runs where | Writes | Setup |
|---|---|---|---|
| **1. Local (stdio)** — the default | each client launches its own server process on your machine | ✅ staged commits | common setup + your target's guide |
| **2. Shared server, hosted by you (HTTPS)** | you run one HTTP(S) server; colleagues connect by URL + bearer token | ❌ read-only, forced in code | common setup + [docs/remote-server.md](docs/remote-server.md) |
| **3. Client to someone else's server** | a colleague hosts mode 2; you just add a URL | ❌ read-only | no venv, no repo, no credentials — [see below](#connect-to-a-shared-remote-server-someone-else-is-hosting-rad-mcp) |

**Mode 1 — Local (stdio).** The client spawns the server as its own child
process; nothing listens on the network. The only mode with the full
toolset (staged writes, `save_startup`, inventory writes). Choose it when
you operate devices yourself.

**Mode 2 — Shared server, hosted by you.** One long-running
`RAD_MCP_TRANSPORT=http` process, many clients by URL. Two interlocks are
enforced in code: no start without bearer tokens (`RAD_MCP_TOKENS`, one per
consumer), and read-only — write tools are never registered. Set
`RAD_MCP_TLS_CERT`/`RAD_MCP_TLS_KEY` for native **https**. Internal network
only — never bind to a public interface.

**Mode 3 — Client to someone else's server.** URL + your personal token in
your client, nothing else. Modes 2 and 3 are the same server — the only
difference is which side of the URL you're on. Skills remain a client-side
install (the URL provides tools, not knowledge).

### Same MCP in several clients = several separate instances (mode 1)

The same stdio entry in several clients does NOT connect them to one
server — **each client spawns and owns its own process**. In practice:

- **Shared via disk:** `inventory.yaml` (re-read every call), `.env`
  credentials (new keys picked up automatically), backups, audit log.
- **Per-instance:** staged configs (stage and commit must happen in the
  same client) and SSH sessions.
- **Restarts are per-client** — reconnecting in one client doesn't touch
  the others.

One genuinely shared instance = mode 2 on localhost, at the cost of writes.

### Config anatomy: who runs the server

An MCP entry has exactly two shapes:

- **stdio — "how do I LAUNCH it":** `command`/`args`/`cwd`/`env`. The
  client owns the process (spawn, kill, restart). You never run the server.
- **http — "where do I FIND it":** `url` + `Authorization` header. The
  server is started **manually by you** (terminal, task, or service — see
  [docs/remote-server.md](docs/remote-server.md)), never by the client,
  which cannot start/stop/restart it.

In Claude Code's `.mcp.json`:

```json
{ "mcpServers": { "rad-mcp": {
    "command": "<repo>\\server\\.venv\\Scripts\\python.exe",
    "args": ["-m", "rad_mcp.server"],
    "cwd": "<repo>\\server",
    "env": { "RAD_MCP_INVENTORY": "<repo>\\inventory.yaml" }
} } }
```

```json
{ "mcpServers": { "rad-mcp": {
    "type": "http",
    "url": "https://<host>:8080/mcp",
    "headers": { "Authorization": "Bearer <your-token>" }
} } }
```

Other clients use the same two shapes with cosmetic differences (Copilot
VS Code: root key `servers`; Copilot CLI: `mcpServers` + `type: "local"`;
Codex: TOML) — each guide shows its client's exact syntax for **both**
modes. Never commit a real token — these config files are often tracked.

## Two install scopes: workspace vs user home

Every client offers the same choice for both MCP config and skills:

| Scope | Lives in | Applies to | Typical files |
|---|---|---|---|
| **Workspace** | the project folder | only sessions opened in that project | `.mcp.json`, `.vscode/mcp.json`, `.github/skills/`, repo `.claude/` |
| **User home** | your `~` dotfolders | every project on the machine | `~/.claude/`, `~/.copilot/`, `~/.agents/skills/`, `claude mcp add -s user`, `~/.codex/config.toml` |

Workspace scope suits a shared repo (committed wiring, per-project); user
home suits "install once, use everywhere" — the typical shape for this
toolkit. When both define `rad-mcp`, the workspace entry wins/duplicates —
keep one.

## Where user-level config lives (Windows ↔ Linux)

CLI/agent tools use the same dotfolder names under the home directory on
both OSes — every `~/...` path in these docs works verbatim on Linux. Only
the GUI apps (last two rows) follow per-OS conventions:

| Purpose | Windows | Linux |
|---|---|---|
| Claude Code user-level (skills, settings, `~/.claude.json`) | `C:\Users\<you>\.claude\` | `~/.claude/` |
| Copilot CLI (mcp-config, skills, permissions) | `C:\Users\<you>\.copilot\` | `~/.copilot/` |
| Codex (config.toml, auth) | `C:\Users\<you>\.codex\` | `~/.codex/` |
| Cross-vendor Agent Skills | `C:\Users\<you>\.agents\skills\` | `~/.agents/skills/` |
| Claude Desktop config | `%APPDATA%\Claude\` | `~/.config/Claude/` |
| VS Code user-level `mcp.json` | `%APPDATA%\Code\User\` | `~/.config/Code/User/` |

(`~`/`$HOME` may not be `/home/<user>` — corporate boxes often map it
elsewhere — but the tools resolve it correctly, which is why the docs use
`~/...` rather than absolute paths.)

## Common setup (once per machine)

Required for every target that runs the server locally.
Requirements: Python 3.11+, SSH reachability to your RAD devices.

```powershell
cd rad-mcp-server\server
python -m venv .venv
.venv\Scripts\pip install -e .
```

Linux: same steps with `.venv/bin/` instead of `.venv\Scripts\`, and use
`python3.11` explicitly on RHEL-family distros (default `python3` is often
3.6 — too old). Verified on Rocky 8.9.

Create `server\.env` (gitignored — never commit credentials):

```
RAD_MCP_USERNAME=...
RAD_MCP_PASSWORD=...
# optional per-device override: RAD_MCP_<NAME>_USERNAME / _PASSWORD
# optional: RAD_MCP_READONLY=true  (disables all write tools)
```

Create your inventory — also gitignored (a clone never contains anyone
else's devices): copy `inventory.example.yaml` to `inventory.yaml`, or let
the `add_device` tool create it on first use. Then smoke-test one device:

```powershell
.venv\Scripts\python -m rad_mcp.smoke <device-name>
```

## Connect to a shared remote server (someone else is hosting rad-mcp)

You need three things from the host:

1. **Network reach** — the server is internal-only (RAD network / VPN).
2. The **URL**, e.g. `https://<host>:8080/mcp` (`http://` if the host runs
   without TLS; a self-signed cert must be trusted by your client).
3. A **bearer token** — your own, so it can be revoked independently.

Then use the **http section of your target's guide** — every guide shows
its client's exact http config. One exception worth knowing: **Claude
Desktop** takes remote servers only via Customize → Connectors (an http
entry in `claude_desktop_config.json` is silently ignored — stdio-only
file, verified 2026-07-10).

You get the read-only tools + `rad://` resources; config-change tools are
never exposed remotely. Skills are a separate client-side install.

---

# Part 2 — Your target (per-client specifics)

## The six targets

Copilot and Codex adopted the Agent Skills standard, so the skills install
everywhere unmodified — only the folder they load from differs.

| Target | MCP tools | Skills | Slash commands | Verified live | Guide |
|---|---|---|---|---|---|
| Claude Code — VS Code extension | ✅ `.mcp.json` | ✅ plugin | ✅ `/rad-health`, … | ✅ daily driver (stdio + http, Windows) | [claude-code-vscode.md](docs/install/claude-code-vscode/) |
| Claude Code — CLI | ✅ `claude mcp add -s user` (or plugin) | ✅ `~/.claude/skills/` | ✅ `~/.claude/commands/` | ✅ 2026-07-11 (Linux, user-home install) | [claude-code-cli.md](docs/install/claude-code-cli/) |
| Claude Desktop — chat + Cowork | ✅ `claude_desktop_config.json` | ✅ zip upload | ❌ plain language | ✅ stdio + skills (config file proven stdio-only, 2026-07-10) | [claude-desktop.md](docs/install/claude-desktop/) |
| GitHub Copilot — VS Code (agent mode) | ✅ `.vscode/mcp.json` | ✅ `.claude/skills/` read natively | ✅ skills as `/name` | ✅ 2026-07-10 (Windows, stdio + shared http) | [copilot-vscode.md](docs/install/copilot-vscode/) |
| GitHub Copilot — CLI | ✅ `~/.copilot/mcp-config.json` | ✅ `copilot skill add` | ✅ | ✅ 2026-07-11 (Linux Rocky 8.9, full fresh-clone flow) | [copilot-cli.md](docs/install/copilot-cli/) |
| OpenAI Codex — CLI / IDE / desktop | ✅ `~/.codex/config.toml` | ⚠ `~/.agents/skills/` — loads unreliably; back rules up in `AGENTS.md` | `$skill-name` | ✅ 2026-07-11 (ChatGPT desktop, shared http; gate via `AGENTS.md` backstop — see guide's behavioral caveat) | [chatgpt-codex.md](docs/install/chatgpt-codex/) |

## Scripted install (repo already cloned on this machine)

After the common setup, one script per target does the MCP wiring + skills
install (PowerShell; each replaces a previous rad-mcp entry rather than
duplicating it; each ends by printing its client's restart/verify step):

| Target | Script | Modes |
|---|---|---|
| Claude Code (CLI + VS Code ext) | `scripts\install\install-claude-code.ps1` | plugin/stdio (default), `-Http -Token <t>` |
| Claude Desktop | `scripts\install\install-claude-desktop.ps1` | stdio only; zip upload stays manual |
| Copilot VS Code | `scripts\install\install-copilot-vscode.ps1 [-Workspace <dir>]` | stdio (default), `-Http -Token <t>` |
| Copilot CLI | `scripts\install\install-copilot-cli.ps1` | stdio (default), `-Http -Token <t>` |
| Codex (CLI/IDE/desktop) | `scripts\install\install-codex.ps1` | stdio (default), `-Http -Token <t>` |

`-Http` defaults the URL to `http://127.0.0.1:8080/mcp` (override with
`-Url`). The guides remain the reference for trust dialogs, org-policy
gates, and troubleshooting.

## Troubleshooting (all targets)

Target-specific tables live in each guide. Common to every surface:

| Symptom | Fix |
|---|---|
| "No username/password" errors | `server\.env` missing or misnamed vars |
| Tool calls hang | Device unreachable — check SSH to the host in `inventory.yaml` |
| Write tools missing | `RAD_MCP_READONLY=true`, or you're on the remote HTTP transport — both intentional guards |
| Config edits not picked up | MCP config is read at client startup — fully restart the client/session (Desktop needs tray-Quit) |

