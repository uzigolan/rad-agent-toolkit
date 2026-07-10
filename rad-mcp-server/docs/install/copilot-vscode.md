# Install target: GitHub Copilot — VS Code extension (Copilot Chat, agent mode)

| Capability | Status |
|---|---|
| MCP tools | ✅ `.vscode/mcp.json` — **agent mode only** |
| Skills | ✅ native Agent Skills (same `SKILL.md` format, no translation) |
| Slash commands | ✅ skills are invocable as `/rad-core`, `/rad-cli-operations`, `/rad-device-mng` (the Claude plugin's `/rad-health`-style commands are not read; see note below) |

**Prerequisite:** the [common setup](../../INSTALL.md#common-setup-once-per-machine)
(venv, `server\.env`, `inventory.yaml`, smoke test) — once per machine.

Copilot adopted the open **Agent Skills** standard (GA Dec 2025), so the RAD
skills load as-is — the same folders Claude uses, byte for byte.

## 1. MCP server

In the workspace root, create/merge `.vscode/mcp.json`.

> ⚠ The root key is **`servers`**, not `mcpServers` — the #1 mistake when
> copying a Claude config.

```json
{
  "servers": {
    "rad-mcp": {
      "type": "stdio",
      "command": "<repo>\\server\\.venv\\Scripts\\python.exe",
      "args": ["-m", "rad_mcp.server"],
      "cwd": "<repo>\\server",
      "env": { "RAD_MCP_INVENTORY": "<repo>\\inventory.yaml" }
    }
  }
}
```

On first start VS Code shows a **trust dialog** — accept it (declining means
the server never starts; "MCP: Reset Trust" from the Command Palette clears
the decision).

> A Claude `.mcp.json` in the same workspace is fine — each client spawns
> its own instance ([details](../../INSTALL.md#same-mcp-in-several-clients--several-separate-instances-mode-1)).

That's the **stdio shape** (Copilot launches the server). The **http shape**
connects to a server you run manually — read-only
([anatomy](../../INSTALL.md#config-anatomy-who-runs-the-server)):

```json
{
  "servers": {
    "rad-mcp": {
      "type": "http",
      "url": "https://<host>:8080/mcp",
      "headers": { "Authorization": "Bearer <your-token>" }
    }
  }
}
```

**Switching modes = disabling the previous config:** one `rad-mcp` entry in
`.vscode/mcp.json` — replace its body with the other shape. Also check the
user-level file ("MCP: Open User Configuration") for a duplicate, and if a
ghost copy still appears, `chat.mcp.discovery.enabled` may be re-importing a
Claude config — disable that setting. Restart the server ("MCP: List
Servers" → Restart) or reload the window after the switch.

## 2. Skills

Pick one:

- **Working inside this repo?** Nothing to do — Copilot reads the repo's
  `.claude/skills/` directory natively (setting `chat.useAgentSkills`, on by
  default).
- **Your own workspace:** copy the three folders from
  `rad-mcp-server/skills/` (`rad-core`, `rad-cli-operations`,
  `rad-device-mng`) into `.github/skills/` of your workspace.
- **All workspaces (user-level):** copy them to `~/.copilot/skills/` (or
  `~/.claude/skills/` — VS Code reads both).

Copy the folders **whole** — `rad-cli-operations` needs its `references/`
knowledge files next to its `SKILL.md`.

> The Claude plugin's slash commands (`/rad-health`, `/rad-backup`) are a
> Claude-only format. Copilot's equivalent is prompt files
> (`.github/prompts/*.prompt.md`) — not shipped yet; the skills cover the
> same ground conversationally ("run a health check on <device>").

## 3. Reload / verify

- **"MCP: List Servers"** (Command Palette) → `rad-mcp` should be running;
  restart it there after any `mcp.json` edit.
- Open Copilot Chat in **agent mode** (MCP tools are invisible in Ask/Edit
  modes), click the tools picker — the rad-mcp tools should be listed.
- Type `/rad` — the three skills should autocomplete. Then try:
  *"run a health check on <device-name>"*.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Server missing | Root key is `servers` not `mcpServers`; check MCP: List Servers → logs; restart server after config edits |
| Server configured but no tools in chat | You're in Ask/Edit mode — switch to **agent mode** |
| Skill never triggers, no error | Invalid frontmatter makes skills **fail silently** — `name` must be lowercase/hyphens and **match the folder name** |
| Everything gated/greyed out | Copilot Business/Enterprise: org policy "MCP servers in Copilot" must be enabled (an MCP-registry allowlist may also apply) |
| Tools disappear on large setups | VS Code caps a chat request at **128 tools** total — deselect unused servers in the tools picker |

Credentials / hangs: [INSTALL.md → Troubleshooting](../../INSTALL.md#troubleshooting-all-targets).
