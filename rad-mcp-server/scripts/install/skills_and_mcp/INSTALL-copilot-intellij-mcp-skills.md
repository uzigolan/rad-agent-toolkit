# GitHub Copilot — JetBrains IDEs (IntelliJ): install rad-mcp (MCP + skills)

This guide walks through `install-copilot-intellij.ps1` / `.sh`: what to
run, what it writes, and how to verify. One run wires **both** JetBrains
agent paths (field-tested 2026-07-19 on Windows, shared http). Applies to
IntelliJ IDEA, PyCharm, WebStorm, … — the config is shared by ALL
JetBrains IDEs.

## 0) Prerequisites — the OFFICIAL plugin only

- The **latest IntelliJ IDEA** (or other JetBrains IDE) — Help → Check
  for Updates — agent mode, MCP and Agent Skills evolve fast; an
  outdated IDE is the most common reason something here is missing.
- Install the **latest "GitHub Copilot" by GitHub** from the JetBrains
  Marketplace (`plugins.jetbrains.com/plugin/17718`) — agent mode + MCP
  shipped mid-2025; Agent Skills late-2025, so old plugin versions lack
  everything this guide relies on.
- Do **NOT** use the IDE's default/bundled AI plugins (JetBrains
  **AI Assistant** / Junie) for this — different product: they read none of
  these configs, load no Agent Skills, and their settings pages stay empty
  for everything installed here.
- The toolkit repo on this machine — first time:

  ```bash
  git clone https://github.com/uzigolan/rad-agent-toolkit.git
  ```

  Already cloned? `git pull` inside it first, so you run the latest
  installers. (No git: GitHub → Code → Download ZIP and extract.)
- **stdio mode** (default): Python 3.10+ (the installer bootstraps the
  server venv automatically). No Python on the
  machine? On Windows the installer downloads a **portable CPython into
  the repo** (`server\.python\`) — nothing is installed system-wide, no
  PATH or registry changes; deleting the repo removes it all. **http mode**: a running shared rad-mcp HTTP
  server + its bearer token (read-only toolset). Use a concrete client URL —
  `127.0.0.1` or the host's IP, never `0.0.0.0` (that's a server bind
  address, not a destination).
- Business/Enterprise: the org policy **"MCP servers in Copilot"** gates
  everything.

## 1) Run the installer

Windows (one-off execution-policy bypass):

```powershell
cd <repo>\rad-mcp-server\scripts\install\skills_and_mcp
PowerShell -ExecutionPolicy Bypass -File ./install-copilot-intellij.ps1
```

Linux/macOS:

```bash
cd <repo>/rad-mcp-server/scripts/install/skills_and_mcp
./install-copilot-intellij.sh
```

> **Windows: "running scripts is disabled on this system"** — you ran the
> `.ps1` directly and the machine's PowerShell execution policy blocks it.
> Use the one-off bypass shown above (`PowerShell -ExecutionPolicy Bypass
> -File ./<script>.ps1`) — nothing needs fixing and no policy change
> persists.

Prompts and non-interactive flags are identical to the VS Code installer:
knowledge mode (`served` default / `bundled`), transport (`stdio` default /
`http` URL + token), `-Http -Url <u> -Token <t>`, `-Knowledge`, `-Reconfigure`
(bash: `--http --url --token --knowledge --reconfigure`).

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
rad-mcp is already configured in C:\Users\<you>\AppData\Local\github-copilot\intellij\mcp.json:
    http  url=http://172.17.160.73:8080/mcp  token=ivsR...Pfzo
  1) Keep existing configuration (leave it unchanged)
  2) Reconfigure from scratch (re-run setup and replace it)
Choice [1]: 1
```

Answer `1` to keep it (the skills still get refreshed); answer `2` when
changing the URL or token.

## 2) What the script writes — TWO agent paths, THREE files

Recent plugin versions run **two** agents with **separate MCP configs**;
the installer wires both:

1. **Classic agent mode** → global
   `%LOCALAPPDATA%\github-copilot\intellij\mcp.json` (Windows) /
   `~/.config/github-copilot/intellij/mcp.json` (macOS/Linux), root key
   **`servers`**. ⚠ http auth nests under **`requestInit.headers`** — the
   VS Code top-level `headers` shape is the #1 mistake copying a config
   here:

   ```json
   "rad-mcp": {
     "type": "http",
     "url": "http://172.17.160.73:8080/mcp",
     "requestInit": { "headers": { "Authorization": "Bearer ivsR3iMeOxKbmVWOjh7f4Aj9RpjEjFNF_fmm2FmPfzo" } }
   }
   ```

   (stdio entries: `"type": "stdio"` + `command`/`args`/`cwd`/`env`, same
   as VS Code.)

2. **Embedded Copilot CLI agent** (the chat whose `/` menu has `/mcp`,
   `/skills`, `/context`, …) → `~/.copilot/mcp-config.json` **and**
   `~/.copilot/mcp.json` (kept in sync; the embedded agent reads
   `mcp-config.json`), root key **`mcpServers`**, plus `"tools": ["*"]`;
   stdio type is `"local"`, no `cwd`:

   ```json
   "rad-mcp": {
     "type": "http",
     "url": "http://172.17.160.73:8080/mcp",
     "headers": { "Authorization": "Bearer ivsR3iMeOxKbmVWOjh7f4Aj9RpjEjFNF_fmm2FmPfzo" },
     "tools": ["*"]
   }
   ```

3. **Skills** → `~/.copilot/skills/` (`rad-core`, `rad-cli-operations`,
   `rad-device-mng`) — both agent paths read this same folder.

Each existing config gets a timestamped `.bak` first; other servers in the
files survive the merge. The plugin seeds `mcp.json` with a `//`-commented
template — the installer tolerates the comments (they're dropped on
rewrite; the `.bak` keeps them).

## 3) Enable Agent Skills (preview toggle)

Settings → **GitHub Copilot → Chat → Agent** → enable **Agent Skills**.
Without it, `~/.copilot/skills` is silently ignored.

## 4) Restart + verify — ONLY inside the Copilot chat

1. Restart the IDE, switch Copilot Chat to **AGENT mode**, and start a
   **NEW chat** — the embedded CLI agent loads MCP + skills at session
   start only.
2. Accept the MCP trust/permission prompts.
3. Verify with the chat commands:

```text
/mcp list        -> rad-mcp next to the builtin github-mcp-server
/skills list     -> the three rad skills
/env             -> whole loaded environment in one view
```

- Typing `/` alone does **NOT** list personal skills — that popup shows
  built-in commands. Invoke a skill by naming it in the prompt, or just
  ask: *"rad agent, list the managed devices"*.
- **Where NOT to look:** Settings → Tools → AI Assistant (JetBrains AI)
  shows NOTHING about Copilot — its MCP/skills pages belong to JetBrains'
  own product (its MCP client may even probe rad-mcp and log odd
  open/close sessions — harmless).

## 5) Quirks and limits

- **1024-char skill-description limit:** this loader silently drops any
  skill whose frontmatter `description` exceeds 1024 characters (bit us
  with rad-cli-operations 1.4.1; fixed in 1.4.2). Symptom: skill missing
  from `/skills list`, no error anywhere.
- **Half-configured symptom:** idea.log shows `[mcpGateway] registered
  mount 'rad-mcp' … [ready]` yet `/mcp list` shows only github-mcp-server →
  the CLI-side config is missing; re-run the installer.
- The same config file serves ALL JetBrains IDEs — install once, every
  IDE gets it.
- The config is also editable in-IDE: Settings → Tools → GitHub Copilot →
  Model Context Protocol → Configure (or agent mode → Tools icon → Add
  More Tools).
- **http mode**: you start the listener yourself (see
  [`../mcp_server/`](../mcp_server/README.md)); the IDE never starts an
  external HTTP listener — only stdio entries auto-start.

## 6) Security reminder

Do not paste live bearer tokens into chats, commits, or shared docs. Three
config files hold the token after an http install — all are user-home
files, outside any repo; keep them that way.

**⚠ This copy embeds the lab's shared token on purpose** (internal doc).
If it ever leaks or lands in a public repo, rotate it on the server
(`RAD_MCP_TOKENS`) and update every client.
