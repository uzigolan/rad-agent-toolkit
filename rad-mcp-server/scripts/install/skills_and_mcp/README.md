# Installing skills + MCP into the clients

One script per target wires **both** artifacts — the MCP server entry and
the skills — into that client (each replaces a previous rad-mcp entry rather
than duplicating it, and ends by printing its client's restart/verify step).
Prerequisite: the
[common setup](../../../INSTALL.md#common-setup-once-per-machine), once per
machine. Principles (stdio vs http, who-starts-the-server, artifact kinds):
[INSTALL.md, Part 1](../../../INSTALL.md).

| Target | Script | Modes |
|---|---|---|
| [Claude Code](#claude-code--cli--vs-code-extension) (CLI + VS Code ext) | `install-claude-code.ps1` / `.sh` | plugin/stdio (default), `-Http -Token <t>` |
| [Claude Desktop](#claude-desktop--chat--cowork) | `install-claude-desktop.ps1` / `.sh` | stdio only; zip upload stays manual |
| [Copilot VS Code](#github-copilot--vs-code-agent-mode) | `install-copilot-vscode.ps1` / `.sh` | stdio (default), `-Http -Token <t>` |
| [Copilot CLI](#github-copilot--cli) | `install-copilot-cli.ps1` / `.sh` | stdio (default), `-Http -Token <t>` |
| [Codex](#openai-codex--ide-extension--chatgpt-desktop-app) (IDE + ChatGPT desktop) | `install-codex.ps1` / `.sh` | stdio (default), `-Http -Token <t>` |

> **Windows: "running scripts is disabled on this system"** — the machine's
> PowerShell execution policy blocks `.ps1` files. Run the script through a
> one-off bypass instead (no policy change persists):
>
> ```powershell
> PowerShell -ExecutionPolicy Bypass -File .\install-copilot-vscode.ps1
> ```

`-Http` defaults the URL to `http://127.0.0.1:8080/mcp` (override with
`-Url`) and requires a server you run yourself — see
[`../mcp_server/`](../mcp_server/README.md). **http entries never start a
server and the http toolset is read-only**; only stdio entries auto-start.
For Copilot specifically: running the MCP listener process is separate from
Copilot's MCP UI actions. `MCP: List Servers` -> Start/Restart manages only
the Copilot-side server lifecycle/connection and does not start or restart
an external HTTP listener process.
Switching modes = replacing the previous rad-mcp entry, then doing the
client's restart step.

The sections below carry each client's specifics: config file + shape,
restart step, verify, quirks. Common troubleshooting (credentials, hangs,
missing write tools):
[INSTALL.md → Troubleshooting](../../../INSTALL.md#troubleshooting-all-targets).

---

## Claude Code — CLI + VS Code extension

**Config:** user scope via
`claude mcp add -s user rad-mcp --env RAD_MCP_INVENTORY=<repo>/rad-mcp-server/inventory.yaml -- <venv-python> -m rad_mcp.server`
(lands in `~/.claude.json`, works in ANY project), or a workspace `.mcp.json`
(root key `mcpServers`, stdio or `"type": "http"` + `url` + `headers`).
http switch: `claude mcp remove rad-mcp` (and
`claude plugin uninstall rad-mcp@rad-marketplace` if installed), then
`claude mcp add --transport http rad-mcp https://<host>:8080/mcp --header "Authorization: Bearer <token>"`.

**Skills + slash commands:** copy `skills/rad-*` → `~/.claude/skills/` and
`commands/*.md` → `~/.claude/commands/`; or the plugin
(`claude plugin marketplace add <repo>/rad-mcp-server`, then
`claude plugin install rad-mcp@rad-marketplace`); or run `claude` from the
repo root (reads `.claude/` directly). This is the only target with the
`/rad-health`, `/rad-backup`, `/rad-harvest`, `/rad-load-manual` commands.

**Restart + verify:** CLI — restart the session; extension — reload the
window. Then `claude mcp list` / `/mcp` (14 tools = stdio; 8 = read-only
http); `/rad` autocompletes the five commands; *"rad agent, list the managed
devices"* triggers the skill. Launch errors (extension): Output panel →
"Claude Code" channel.

## Claude Desktop — chat + Cowork

**Config (stdio-only file):** `%APPDATA%\Claude\claude_desktop_config.json`
(Windows) / `~/Library/Application Support/Claude/claude_desktop_config.json`
(macOS), root key `mcpServers`, **no `cwd` key** (unsupported — safe, server
paths are module-anchored). ⚠ A `"type": "http"` entry is **silently
ignored** (verified 2026-07-10). For this toolkit, Claude Desktop is
**local stdio only** for `rad-mcp`.

**Skills (zip upload, the one manual-refresh target):** sidebar Customize →
Skills → upload the three zips from `dist/claude-desktop-skills/`. Build
them with `python scripts/build_desktop_skills.py` — **not**
`Compress-Archive` (backslash entry paths → "invalid character" on upload).
Zips are snapshots: rebuild + re-upload after every skill/reference update.
The same uploads apply in Cowork automatically. No slash commands — plain
language only.

**Restart + verify:** **tray-Quit** and relaunch (window close is NOT
enough; config is read only at launch). Tools icon near the message box
lists rad-mcp; Customize → Skills shows the three skills; ask *"run a health
check on <device>"*. Logs: `%APPDATA%\Claude\logs\mcp*.log`.

## GitHub Copilot — VS Code (agent mode)

**Config:** workspace `.vscode/mcp.json` — root key is **`servers`**, not
`mcpServers` (the #1 mistake copying a Claude config). Entry: stdio
(`"type": "stdio"`, `command`/`args`/`cwd`/`env`) or http (`"type": "http"`,
`url`, `headers.Authorization`). Accept the trust dialog on first start
("MCP: Reset Trust" clears decisions). Ghost duplicate entries: check the
user-level file ("MCP: Open User Configuration") and
`chat.mcp.discovery.enabled` re-importing a Claude config.

**Skills:** native Agent Skills (Dec-2025+ Copilot Chat,
`chat.useAgentSkills`) — inside this repo nothing to do (`.claude/skills/`
is read natively); own workspace: copy the three folders (whole,
`references/` included) into `.github/skills/`; user-level:
`~/.copilot/skills/` or `~/.claude/skills/`. Skills are invocable as
`/rad-core` etc. Older VS Code (~1.100):
[fallback-older-vscode.md](fallback-older-vscode.md) (instructions-files
route, field-tested 2026-07-12).

> **⚠ Remove DUPLICATE skill copies BEFORE reinstalling (Copilot quirk).**
> VS Code Copilot can hold **several copies of the same rad skill loaded at
> once** — from `~/.copilot/skills`, `~/.claude/skills`, a workspace
> `.github/skills`, or a leftover from a previous install. When copies
> collide, Copilot may load a **stale** one, so a freshly installed
> served/1.4.x skill can still report as an old bundled version. **The tell:**
> open the Copilot **Skills UI** (Settings → Skills) and click the trash icon
> on a rad skill — if the skill **stays listed** after deleting, there is more
> than one copy loaded. **Delete every copy** until it disappears, *then*
> install the new rad skills → Reload Window → start a new chat. (Confirmed
> 2026-07-18.)

**Restart + verify:** restart the server ("MCP: List Servers" → Restart) or
reload the window. MCP tools exist **only in agent mode** (invisible in
Ask/Edit). "MCP: List Servers" → rad-mcp running; `/rad` autocompletes the
three skills; *"rad agent, list the managed devices"*. Quirks: org policy
"MCP servers in Copilot" gates everything on Business/Enterprise; VS Code
caps a chat request at **128 tools** (deselect unused servers); invalid
skill frontmatter fails **silently** (`name` lowercase and matching the
folder).

**Important (http mode):** you must start the MCP listener yourself (for
example via `scripts/install/mcp_server/install-and-start-http-mcp-server.ps1`
or `.sh`). Copilot's Start/Restart action does not launch that listener; it
only controls Copilot's local MCP runtime/connection state.

## GitHub Copilot — CLI

**Config:** `~/.copilot/mcp-config.json` — root key **is** `mcpServers`,
stdio type is `"local"`, **no `cwd` support** (safe — inventory comes from
the env var), add `"tools": ["*"]`. Or `/mcp add` inside a session. http:
same entry, `"type": "http"` + `url` + `headers`. ⚠ **Launch-directory
discovery:** the CLI also reads an `.mcp.json` in the directory you launch
`copilot` from — this repo ships one with the committing machine's paths;
rewrite it locally or launch elsewhere. Linux venv: RHEL-family needs
`python3.11` explicitly; never move/rename the repo after (venv symlinks
break).

**Skills:** `copilot skill add <repo>/rad-mcp-server/skills/<name>` per
skill (or copy the folders into `~/.copilot/skills/`); inside this repo
nothing to do. Skills load **only at CLI startup**.

**Restart + verify:** restart the `copilot` session. `/mcp show` → rad-mcp
running; `/skills list` → the three skills; *"rad agent, list the managed
devices"* — answer the first tool-permission prompt "yes, always".
Non-interactive runs (`copilot -p`) need `--allow-tool 'rad-mcp(*)'`.
(Full fresh-clone flow verified 2026-07-11 on Rocky 8.9.)

**Important (http mode):** the listener process is external to Copilot CLI.
Start it separately (see [`../mcp_server/`](../mcp_server/README.md));
Copilot commands do not start that listener for you.

## OpenAI Codex — IDE extension + ChatGPT desktop app

> **One config, both surfaces:** both read the SAME `~/.codex/config.toml`
> and `~/.agents/skills/` — installing for one installs for the other; only
> the restart step and UI differ.

**Config:** `[mcp_servers.rad-mcp]` in `~/.codex/config.toml` — stdio:
`command`/`args`/`cwd`/`env`, `startup_timeout_sec = 20` (default 10 can
time out); http: `url` + `http_headers = { Authorization = "Bearer <t>" }`.
Absolute expanded paths only — TOML does not resolve `$HOME`/`~`. Keep one
active entry (or two names with `enabled = false` on the inactive);
`codex mcp remove rad-mcp` deletes one. The desktop app also manages entries
visually: Settings → Plugins → MCPs (toggles map to `enabled` flags).

**Skills:** copy the three folders (whole) into `~/.agents/skills/` —
Codex reads `.agents/skills/`, **NOT** `.claude/skills/`. ⚠ **Skills load
unreliably on Codex** (observed live 2026-07-11: a device read executed
without the confirmation gate — code interlocks still held). Mitigate with
the `~/.codex/AGENTS.md` backstop, re-read every run: *"RAD devices: before
executing ANY device command — read-only included — show the command and ask
for explicit confirmation."* Treat it as part of the install.

**Restart + verify:** IDE — reload the window / restart the extension;
desktop app — fully quit and relaunch. Then `/mcp` and `/skills` in the
Codex composer (desktop: Settings → Plugins lists both), and *"rad agent,
list the managed devices"* in a **local** Codex session (`$rad-cli-operations`
forces the skill). Use **Codex mode**, not Work/chat — regular ChatGPT chat
reads neither config.toml nor skills; cloud tasks have no MCP/LAN access.
