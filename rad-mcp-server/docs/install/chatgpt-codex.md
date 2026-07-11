# Install target: OpenAI Codex (CLI, IDE extension, ChatGPT desktop)

| Capability | Status |
|---|---|
| MCP tools | ✅ `~/.codex/config.toml` — one config shared by CLI, IDE extension, and ChatGPT desktop |
| Skills | ✅ native Agent Skills via `.agents/skills/` |
| Slash commands | `$skill-name` / `/skills` |

**Prerequisite:** the [common setup](../../INSTALL.md#common-setup-once-per-machine)
(venv, `server\.env`, `inventory.yaml`, smoke test) — once per machine.

Codex adopted the open **Agent Skills** standard, so the RAD skills load
unmodified — but note Codex reads **`.agents/skills/`**, *not*
`.claude/skills/` (unlike Copilot), so they must be copied once.

## 1. MCP server

All three local surfaces share `~/.codex/config.toml` — configure once.
Add:

Linux paths shown (the CLI's usual home); on Windows — e.g. for the ChatGPT
desktop app — the venv python is `<repo>/rad-mcp-server/server/.venv/Scripts/python.exe`
instead of `.../.venv/bin/python`:

```toml
[mcp_servers.rad-mcp]
command = "<repo>/rad-mcp-server/server/.venv/bin/python"
args = ["-m", "rad_mcp.server"]
cwd = "<repo>/rad-mcp-server/server"
env = { RAD_MCP_INVENTORY = "<repo>/rad-mcp-server/inventory.yaml" }
startup_timeout_sec = 20
```

(`cwd` is supported here. `startup_timeout_sec` raised from the 10 s default
— venv Python + inventory load can be slow on first spawn.)

Or from the terminal:

```bash
codex mcp add rad-mcp --env RAD_MCP_INVENTORY=<repo>/rad-mcp-server/inventory.yaml -- <repo>/rad-mcp-server/server/.venv/bin/python -m rad_mcp.server
codex mcp list
```

**The other mode — http client** (server runs manually, not by Codex;
read-only). Same section name, different body:

```toml
[mcp_servers.rad-mcp]
url = "https://<host>:8080/mcp"
http_headers = { Authorization = "Bearer <your-token>" }
```

**Switching modes = disabling the previous config:** one `[mcp_servers.rad-mcp]`
section — replace its body, or keep both shapes under two names with
`enabled = false` on the inactive one (avoids duplicate tools):

```toml
[mcp_servers.rad-mcp-local]
enabled = false
# ... stdio body ...
```

(`codex mcp remove rad-mcp` deletes an entry from the CLI.)

**Restart Codex** (CLI session / IDE extension) — config is read at startup
after any mode switch.

## 2. Skills

Copy the three folders from `rad-mcp-server/skills/` (`rad-core`,
`rad-cli-operations`, `rad-device-mng`) — whole, `references/` included —
into one of:

- `~/.agents/skills/` — user-level, applies everywhere (recommended)
- `<your-repo>/.agents/skills/` — per-project

Skills trigger implicitly by description, or explicitly: `$rad-cli-operations`.
`/skills` lists what's loaded. Restart Codex after adding/changing skills.

## Behavioral caveat (observed live, 2026-07-11)

MCP tools work, but **don't rely on skill-level safety rules on Codex**: in
a ChatGPT-desktop session, the skill file failed to load and Codex executed
a device read without the skill's mandatory "Run this on the device now?"
confirmation — it treated the user's request as authorization. The code
interlocks (read-only http, staged writes, whitelists) still held. Two
mitigations, use both:

1. Add the gate to `~/.codex/AGENTS.md` — Codex re-reads it every run,
   unlike skills:
   *"RAD devices: before executing ANY device command — read-only included —
   show the command and ask for explicit confirmation."*
2. Say it explicitly at session start when it matters.

## 3. Verify

In a Codex session: `/mcp` (or `codex mcp list`) shows rad-mcp; `/skills`
shows the three rad skills. Then ask: *"run a health check on
<device-name>"*. Write tools (`stage_config`/`commit_config`) will trigger
Codex approval prompts — expected, keep them.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Server/skills missing after edits | Configs are read at startup — restart the Codex session / IDE extension |
| Skills in `.claude/skills/` ignored | Codex only reads `.agents/skills/` (repo) and `~/.agents/skills/` (user) — copy them over |
| Server times out on start | Raise `startup_timeout_sec` (default 10) |
| Windows: server won't spawn | Native Windows Codex is still labeled experimental — use full paths (no `~`), or run under WSL2 (then use Linux-side paths for the venv) |

Credentials / hangs: [INSTALL.md → Troubleshooting](../../INSTALL.md#troubleshooting-all-targets).
