# GitHub Copilot — VS Code extension: install rad-mcp (MCP + skills)

This guide walks through `install-copilot-vscode.ps1` / `.sh`: what to run,
what it writes, and how to verify. One run wires **both** artifacts — the
`rad-mcp` MCP server entry and the three rad skills — into Copilot for
VS Code.

## 0) Prerequisites

- The **latest VS Code** (Help → Check for Updates — agent mode, MCP and
  Agent Skills evolve fast; an outdated IDE is the most common reason
  something here is missing) with the **latest** **GitHub Copilot** +
  **Copilot Chat** extensions (Dec-2025 or newer for native Agent
  Skills; older VS Code ~1.100: see
  [fallback-older-vscode.md](fallback-older-vscode.md)).
- The toolkit repo on this machine — first time:

  ```bash
  git clone https://github.com/uzigolan/rad-agent-toolkit.git
  ```

  Already cloned? `git pull` inside it first, so you run the latest
  installers. (No git: GitHub → Code → Download ZIP and extract.)
- **stdio mode** (default): Python 3.10+ on the machine — the installer
  bootstraps the server venv automatically on first run. No Python on the
  machine? On Windows the installer downloads a **portable CPython into
  the repo** (`server\.python\`) — nothing is installed system-wide, no
  PATH or registry changes; deleting the repo removes it all.
- **http mode**: a running shared rad-mcp HTTP server + its bearer token
  (see [`../mcp_server/`](../mcp_server/README.md)). The http toolset is
  read-only.
- Business/Enterprise: the org policy **"MCP servers in Copilot"** must be
  enabled, or nothing here will load.

## 1) Run the installer

Windows (one-off execution-policy bypass, no policy change persists):

```powershell
cd <repo>\rad-mcp-server\scripts\install\skills_and_mcp
PowerShell -ExecutionPolicy Bypass -File ./install-copilot-vscode.ps1
```

Linux/macOS:

```bash
cd <repo>/rad-mcp-server/scripts/install/skills_and_mcp
./install-copilot-vscode.sh
```

> **Windows: "running scripts is disabled on this system"** — you ran the
> `.ps1` directly and the machine's PowerShell execution policy blocks it.
> Use the one-off bypass shown above (`PowerShell -ExecutionPolicy Bypass
> -File ./<script>.ps1`) — nothing needs fixing and no policy change
> persists.

The script prompts for:

1. **Knowledge mode** — `served` (default; thin skills; knowledge served by
  the MCP catalog tools — needs a server with the catalog built) or
  `bundled` (skills carry their references, ~14 MB, works with no MCP
  connection).
2. **Transport** — `stdio` (default; VS Code launches the server locally,
   full toolset) or `http` (URL + bearer token; blank token = auto-generate,
   then configure the SAME value on the server via `RAD_MCP_TOKENS` /
   `RAD_MCP_WRITE_TOKENS`).

Note: a missing local `build/rad-knowledge.sqlite` warning is relevant only
for local MCP usage (`stdio` or localhost HTTP). If your MCP server is remote,
the catalog is expected on that server machine, not on this client PC.

Checker terms used by installers:
- `OK`: setup is valid for the selected mode/transport.
- `DEGRADED`: served mode selected but local catalog is missing in a local MCP setup.
  Core MCP usage still works, but catalog-backed knowledge is limited until the catalog is built.

Non-interactive flags (PowerShell shown; bash uses `--http --url --token
--knowledge --reconfigure`):

```powershell
./install-copilot-vscode.ps1 -Knowledge served -Http -Url http://127.0.0.1:8080/mcp -Token <token>
./install-copilot-vscode.ps1 -Reconfigure   # force-replace an existing rad-mcp entry
```

If rad-mcp is already configured and no flags force a mode, the script
offers to **keep the existing entry** and only refresh the skills.

### This lab's setup — what to answer at the prompts

Served knowledge + the shared http server. Interactive run:

```text
Knowledge distribution mode:
  1) bundled  - skills carry their references (~14 MB); works with no MCP connection
  2) served   - thin skills; all knowledge served by the rad-mcp catalog tools [default]
Choice [2]:

Select MCP transport:
  1) stdio  - local; the client launches the server via command/args (full toolset)
  2) http   - remote; connect to an http(s) server by URL + bearer token (read-only)
Choice [1]: 2
Server URL [http://127.0.0.1:8080/mcp]: http://172.17.160.73:8080/mcp
Bearer token (leave blank to auto-generate one): ivsR3iMeOxKbmVWOjh7f4Aj9RpjEjFNF_fmm2FmPfzo
```

If rad-mcp is already configured, you get this instead:

```text
rad-mcp is already configured in %APPDATA%\Code\User\mcp.json:
    http  url=http://172.17.160.73:8080/mcp  token=ivsR...Pfzo
  1) Keep existing configuration (leave it unchanged)
  2) Reconfigure from scratch (re-run setup and replace it)
Choice [1]: 1
```

Answer `1` to keep it (the skills still get refreshed); answer `2` when
changing the URL or token.

## 2) What the script writes

- **MCP entry** → VS Code *user* MCP config, root key **`servers`** (NOT
  `mcpServers` — the #1 mistake copying a Claude config):
  - Windows: `%APPDATA%\Code\User\mcp.json`
  - macOS: `~/Library/Application Support/Code/User/mcp.json`
  - Linux: `~/.config/Code/User/mcp.json`

  stdio shape / http shape:

  ```json
  "rad-mcp": {
    "type": "stdio",
    "command": "<repo>/rad-mcp-server/server/.venv/.../python",
    "args": ["-m", "rad_mcp.server"],
    "cwd": "<repo>/rad-mcp-server/server",
    "env": { "RAD_MCP_INVENTORY": "<repo>/rad-mcp-server/inventory.yaml" }
  }
  ```

  ```json
  "rad-mcp": {
    "type": "http",
    "url": "http://172.17.160.73:8080/mcp",
    "headers": { "Authorization": "Bearer ivsR3iMeOxKbmVWOjh7f4Aj9RpjEjFNF_fmm2FmPfzo" }
  }
  ```

- **Skills** → `~/.copilot/skills/` (`rad-core`, `rad-cli-operations`,
  `rad-device-mng`) — the same folder Copilot CLI reads. In served mode the
  `rad-cli-operations/references/` folder is omitted and the SKILL.md is
  stamped `<!--rad-mode:served-->`.
- A timestamped backup `mcp.json.bak.<yyyyMMdd-HHmmss>` of any existing
  config. Existing entries in the file (other servers) survive the merge;
  `//` comments in a JSONC file are tolerated but dropped on rewrite.

## 3) Remove duplicate skill copies FIRST (Copilot quirk)

VS Code Copilot can hold several copies of the same rad skill at once —
from `~/.copilot/skills`, `~/.claude/skills`, a workspace `.github/skills`,
or a previous install — and may load a **stale** one. Open the Copilot
**Skills UI** (Settings → Skills) and delete a rad skill: if it **stays
listed**, another copy exists — delete every copy until it disappears,
then install fresh.

## 4) Restart + trust

1. Reload the VS Code window (`Developer: Reload Window`).
2. Accept the MCP **trust dialog** on first server start
   (`MCP: Reset Trust` clears previous decisions).
3. Switch Copilot Chat to **AGENT mode** — MCP tools are invisible in
   Ask/Edit modes.

## 5) Verify

- `MCP: List Servers` → rad-mcp running (Start/Restart here manages only
  Copilot's connection — it never starts an external HTTP listener).
- Type `/rad` in chat → the three skills autocomplete (`/rad-core`, …).
- Ask: *"rad agent, list the managed devices"* → approve the
  tool-permission prompt.

## 6) Quirks and limits

- VS Code caps a chat request at **128 tools** — deselect unused servers in
  the tools picker if you exceed it.
- Invalid skill frontmatter fails **silently** (`name` must be lowercase
  and match the folder; `description` must be ≤ 1024 characters).
- Ghost duplicate MCP entries: check the user-level file
  (`MCP: Open User Configuration`) and `chat.mcp.discovery.enabled`
  re-importing a Claude config.
- **http mode**: you start the listener yourself (e.g.
  `../mcp_server/install-and-start-http-mcp-server.ps1` / `.sh`).

## 7) Security reminder

Do not paste live bearer tokens into chats, commits, or shared docs. The
config file holds the token — keep it out of version control (user-level
config, not the workspace file, when the token is real).

**⚠ This copy embeds the lab's shared token on purpose** (internal doc).
If it ever leaks or lands in a public repo, rotate it on the server
(`RAD_MCP_TOKENS`) and update every client.
