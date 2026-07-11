# Install target: GitHub Copilot CLI (`copilot` terminal agent)

Verified live 2026-07-11 on Linux (Rocky 8.9, Python 3.11): skills trigger,
intake gate, fresh-clone inventory flow, restart-free `.env` pickup.

| Capability | Status |
|---|---|
| MCP tools | ✅ `~/.copilot/mcp-config.json` (+ discovers a `.mcp.json` in the launch directory) |
| Skills | ✅ native Agent Skills (same `SKILL.md` format, no translation) |
| Slash commands | ✅ skills invocable by name; `/skills` to manage |

**Prerequisite:** the [common setup](../../INSTALL.md#common-setup-once-per-machine)
— once per machine.

## Linux quick start (complete, exactly as verified)

Every command below is from the verified Rocky 8.9 run. Watch the
directories — each block starts where the previous one ended.

```bash
sudo dnf install -y python3.11
cd $HOME
git clone https://github.com/uzigolan/rad-agent-toolkit.git
cd $HOME/rad-agent-toolkit/rad-mcp-server/server
python3.11 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -e .
.venv/bin/python -c "import rad_mcp; print('server import OK')"
```

(RHEL-family default `python3` is often 3.6 — too old, its pip can't even
read `pyproject.toml`; hence `python3.11` explicitly. Never move/rename the
repo after creating the venv — `.venv/bin/python` is a symlink and breaks.)

```bash
cat > .env <<'EOF'
RAD_MCP_USERNAME=<user>
RAD_MCP_PASSWORD=<password>
EOF
```

```bash
cd ../..
mkdir -p ~/.copilot
cat > ~/.copilot/mcp-config.json <<EOF
{
  "mcpServers": {
    "rad-mcp": {
      "type": "local",
      "command": "$(pwd)/rad-mcp-server/server/.venv/bin/python",
      "args": ["-m", "rad_mcp.server"],
      "env": { "RAD_MCP_INVENTORY": "$(pwd)/rad-mcp-server/inventory.yaml" },
      "tools": ["*"]
    }
  }
}
EOF
mkdir -p ~/.copilot/skills
cp -r rad-mcp-server/skills/rad-core rad-mcp-server/skills/rad-cli-operations rad-mcp-server/skills/rad-device-mng ~/.copilot/skills/
```

If you'll launch `copilot` from the repo root, also rewrite the repo's
`.mcp.json` (it ships with the committing machine's paths — see the
launch-directory note below):

```bash
cat > .mcp.json <<EOF
{
  "mcpServers": {
    "rad-mcp": {
      "command": "$(pwd)/rad-mcp-server/server/.venv/bin/python",
      "args": ["-m", "rad_mcp.server"],
      "cwd": "$(pwd)/rad-mcp-server/server",
      "env": { "RAD_MCP_INVENTORY": "$(pwd)/rad-mcp-server/inventory.yaml" }
    }
  }
}
EOF
```

Then `copilot` → `/mcp show`, `/skills list`, and the fresh-clone flow:
*"rad agent, list the managed devices"* (expect "no inventory yet"), *"rad
agent, add my device"* (six-field intake; the add creates `inventory.yaml`
automatically), *"test connectivity to <name>"* (works with no restart).

## 1. MCP server

Either run `/mcp add` inside a `copilot` session and fill the form, or
create/merge `~/.copilot/mcp-config.json` directly. Windows command path:
`<repo>\server\.venv\Scripts\python.exe`; Linux shown here:

```json
{
  "mcpServers": {
    "rad-mcp": {
      "type": "local",
      "command": "<repo>/rad-mcp-server/server/.venv/bin/python",
      "args": ["-m", "rad_mcp.server"],
      "env": { "RAD_MCP_INVENTORY": "<repo>/rad-mcp-server/inventory.yaml" },
      "tools": ["*"]
    }
  }
}
```

Notes:
- Root key here **is** `mcpServers` (unlike VS Code's `servers`) and the
  stdio type is `"local"`.
- **No `cwd` support** — same situation as Claude Desktop, and safe for the
  same reason: all rad-mcp server paths (`.env`, backups, logs) are
  module-anchored, and the inventory comes from the env var.
- `tools: ["*"]` exposes all tools; you can list specific ones instead
  (e.g. only the read tools).
- **Launch-directory discovery** (verified 2026-07-11): the CLI also picks
  up an `.mcp.json` in the directory you launch `copilot` from. This repo
  ships one wired for the machine it was committed on — launching from the
  repo root on another machine fails to spawn ("No such file or directory")
  until you rewrite that file with local paths (or launch from elsewhere).

**The other mode — http client** (server runs manually, not by Copilot;
read-only). Same file, same entry name, different body:

```json
{
  "mcpServers": {
    "rad-mcp": {
      "type": "http",
      "url": "https://<host>:8080/mcp",
      "headers": { "Authorization": "Bearer <your-token>" },
      "tools": ["*"]
    }
  }
}
```

**Switching modes = disabling the previous config:** one `rad-mcp` entry —
replace its body (or `/mcp` → remove the old one first), then **restart the
`copilot` session** (config is read at startup).

## 2. Skills

Pick one:

- **Running `copilot` inside this repo?** Nothing to do — the CLI reads the
  repo's `.claude/skills/` directory natively.
- **Anywhere else:** install them user-level:

  ```bash
  copilot skill add <repo>/rad-mcp-server/skills/rad-core
  copilot skill add <repo>/rad-mcp-server/skills/rad-cli-operations
  copilot skill add <repo>/rad-mcp-server/skills/rad-device-mng
  ```

  (or copy the folders whole into `~/.copilot/skills/`).

> ⚠ **Skills load only at CLI startup** — restart the session after
> adding or changing them.

## 3. Verify

- `/mcp show` — `rad-mcp` listed and running.
- `/skills list` — the three rad skills present.
- Ask: *"run a health check on <device-name>"*. First tool call prompts for
  permission — answer "yes, always" to persist the approval.

For scripted / non-interactive runs (`copilot -p "..."`), tools won't execute
without pre-approval — pass e.g. `--allow-tool 'rad-mcp(*)'` (or list only
the read tools).

## Troubleshooting

| Symptom | Fix |
|---|---|
| Server missing from `/mcp show` | JSON root key must be `mcpServers`; check both sources: `~/.copilot/mcp-config.json` and an `.mcp.json` in the launch directory |
| "failed to spawn MCP server process: No such file or directory" | The `command` path doesn't exist here — commonly a repo-shipped `.mcp.json` with another machine's paths (rewrite it locally), or a venv that was moved/renamed after creation (rebuild it) |
| Skills not appearing | Added mid-session — restart `copilot`; check `/skills list` |
| Everything gated | Copilot Business/Enterprise: org policy "MCP servers in Copilot" applies to the CLI too |
| Tool calls silently skipped in `-p` mode | Non-interactive runs need `--allow-tool` / `--allow-all-tools` |

Credentials / hangs: [INSTALL.md → Troubleshooting](../../INSTALL.md#troubleshooting-all-targets).
