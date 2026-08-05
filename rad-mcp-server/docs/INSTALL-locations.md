# INSTALL locations: where each flow puts MCP config, skills, and plugins

Companion to [INSTALL.md](../../INSTALL.md), same layout. For every install flow it
lists: where the MCP registration lands, where the skills land and how they
get there, and the plugin name when a plugin system is used.

All targets are **global (user-level)** — no flow writes into a workspace.
Paths shown for Windows; `~` = `%USERPROFILE%`.

## 1. Common to all flows

| Piece | Location | Notes |
|---|---|---|
| MCP server (stdio) | `rad-mcp-server\server\.venv` (repo-local Python venv) | Launched by the client via `python.exe -m rad_mcp.server`; nothing system-wide |
| MCP server (http) | external process you start via `install-and-start-http-mcp-server.ps1` | Clients only get URL + bearer token (read-only toolset) |
| Inventory | `rad-mcp-server\inventory.yaml` (via `RAD_MCP_INVENTORY` env) | Shared by all clients |
| Config backups | `<config>.bak.<yyyyMMdd-HHmmss>` next to each modified config | Written before every change |

Skills come in two knowledge modes: **served** (thin skills, knowledge via MCP
catalog tools — default) or **bundled** (skills carry their `references/`,
~14 MB, work without MCP).

## 2. GitHub Copilot (main)

All Copilot variants share one skills folder: skills are installed **once**
and read by VS Code Copilot, IntelliJ Copilot, and the Copilot CLI alike.

### 2.1 VS Code + MCP stdio / 2.4 VS Code + MCP http

| Piece | How / Where |
|---|---|
| MCP config | `%APPDATA%\Code\User\mcp.json` — root key `servers`, entry `rad-mcp` (user profile, all workspaces) |
| Skills | copied to `~\.copilot\skills\rad-*` |
| Plugin | none — plain MCP config + skill folders |

### 2.2 IntelliJ + MCP stdio / 2.5 IntelliJ + MCP http

| Piece | How / Where |
|---|---|
| MCP config (classic agent) | `%LOCALAPPDATA%\github-copilot\intellij\mcp.json` — root key `servers`, entry `rad-mcp` |
| MCP config (embedded CLI agent) | `~\.copilot\mcp-config.json` + `~\.copilot\mcp.json` — root key `mcpServers`, entry `rad-mcp` (both kept in sync) |
| Skills | copied to `~\.copilot\skills\rad-*` |
| Plugin | none |

### 2.3 Copilot CLI + MCP stdio / 2.6 Copilot CLI + MCP http

| Piece | How / Where |
|---|---|
| MCP config | `~\.copilot\mcp-config.json` + `~\.copilot\mcp.json` — root key `mcpServers`, entry `rad-mcp` (stdio uses `type: "local"`) |
| Skills | copied to `~\.copilot\skills\rad-*` |
| Plugin | none |

## 3. ChatGPT Codex (main)

One shared config for all Codex surfaces (CLI, VS Code extension, desktop app).

### 3.1–3.3 Codex (stdio, http, shared installer)

| Piece | How / Where |
|---|---|
| MCP config | `~\.codex\config.toml` — TOML table `[mcp_servers.rad-mcp]` |
| Skills | copied to `~\.agents\skills\rad-*` |
| Plugin | none (the "shared installer" is one config file, not a plugin) |

### 3.4 Codex desktop app (HTTPS)

Same `~\.codex\config.toml` + `~\.agents\skills`; TLS trust steps are in
`rad-mcp-server/scripts/install/skills_and_mcp/INSTALL-codex-mcp-skills.md`.

## 4. Claude (main)

### 4.1 Claude Desktop + MCP stdio

| Piece | How / Where |
|---|---|
| MCP config | `claude_desktop_config.json` — root key `mcpServers`, entry `rad-mcp`. Store install: `%LOCALAPPDATA%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\`; traditional: `%APPDATA%\Claude\` |
| Skills | built as **zips** in `rad-mcp-server\dist\claude-desktop-skills\`, uploaded **manually** (Customize -> Skills) — Desktop offers no automation |
| Plugin | none |

### 4.2 Claude VS Code + MCP stdio / 4.3 Claude CLI + MCP stdio

The CLI and the VS Code extension read the same plugin/config.

| Piece | How / Where |
|---|---|
| Plugin | **`rad-mcp@rad-marketplace`**, installed at **user scope** (global, every project) via `claude plugin install` |
| Marketplace | `rad-marketplace` — the local `rad-mcp-server\` folder registered via `claude plugin marketplace add`; the installer generates the machine-local manifests (`.claude-plugin\plugin.json`, `.claude-plugin\marketplace.json`, `.mcp.json`) — they are gitignored because they carry absolute venv paths |
| MCP config | carried **inside the plugin** (`rad-mcp-server\.mcp.json`, root key `mcpServers`, entry `rad-mcp`) — no separate client config to edit |
| Skills | carried **inside the plugin** (`skills/` at plugin root) — `~\.claude\skills` stays **empty** in this mode, that is normal |
| Slash commands | carried inside the plugin (`/rad-health`, `/rad-backup`, `/rad-harvest`, `/rad-load-manual`, ...) |

Claude Code **http** mode (no plugin): `claude mcp add --scope user` registers
`rad-mcp` globally in `~\.claude.json`, and skills are copied client-side to
`~\.claude\skills\rad-*` (slash commands still need the plugin).

## 5. Generic (any other MCP client)

| Piece | How / Where |
|---|---|
| MCP config | **nothing written** — `install-generic.ps1` prints ready-to-paste snippets for each client shape (`servers` vs `mcpServers` root keys) |
| Skills | **not copied** — the helper prints the source folder (`rad-mcp-server\skills\`) and the per-client scope targets to copy into |
| Plugin | none |

## 6. Quick reference table

| Flow | MCP config | Skills | Plugin |
|---|---|---|---|
| Copilot VS Code | `%APPDATA%\Code\User\mcp.json` (`servers`) | `~\.copilot\skills` | — |
| Copilot IntelliJ | `%LOCALAPPDATA%\github-copilot\intellij\mcp.json` (`servers`) + `~\.copilot\mcp-config.json` | `~\.copilot\skills` | — |
| Copilot CLI | `~\.copilot\mcp-config.json` + `mcp.json` (`mcpServers`) | `~\.copilot\skills` | — |
| Codex (all surfaces) | `~\.codex\config.toml` (`[mcp_servers.rad-mcp]`) | `~\.agents\skills` | — |
| Claude Desktop | `claude_desktop_config.json` (`mcpServers`) | manual zip upload from `rad-mcp-server\dist\claude-desktop-skills` | — |
| Claude Code (VS Code + CLI, stdio) | inside plugin (`.mcp.json`) | inside plugin | `rad-mcp@rad-marketplace` (user scope) |
| Claude Code (http) | `~\.claude.json` (user scope) | `~\.claude\skills` | — |
| Generic | printed snippet only | printed instructions only | — |
