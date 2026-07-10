# Install target: GitHub Copilot CLI (`copilot` terminal agent)

| Capability | Status |
|---|---|
| MCP tools | ✅ `~/.copilot/mcp-config.json` (user-level only) |
| Skills | ✅ native Agent Skills (same `SKILL.md` format, no translation) |
| Slash commands | ✅ skills invocable by name; `/skills` to manage |

**Prerequisite:** the [common setup](../../INSTALL.md#common-setup-once-per-machine)
(venv, `server\.env`, `inventory.yaml`, smoke test) — once per machine.

## 1. MCP server

Either run `/mcp add` inside a `copilot` session and fill the form, or
create/merge `~/.copilot/mcp-config.json` directly:

```json
{
  "mcpServers": {
    "rad-mcp": {
      "type": "local",
      "command": "<repo>\\server\\.venv\\Scripts\\python.exe",
      "args": ["-m", "rad_mcp.server"],
      "env": { "RAD_MCP_INVENTORY": "<repo>\\inventory.yaml" },
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
| Server missing from `/mcp show` | JSON root key must be `mcpServers`; config is user-level (`~/.copilot/mcp-config.json`), there is no per-repo MCP file for the CLI |
| Skills not appearing | Added mid-session — restart `copilot`; check `/skills list` |
| Everything gated | Copilot Business/Enterprise: org policy "MCP servers in Copilot" applies to the CLI too |
| Tool calls silently skipped in `-p` mode | Non-interactive runs need `--allow-tool` / `--allow-all-tools` |

Credentials / hangs: [INSTALL.md → Troubleshooting](../../INSTALL.md#troubleshooting-all-targets).
