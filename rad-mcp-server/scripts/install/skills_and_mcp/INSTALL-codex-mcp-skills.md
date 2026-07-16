# Windows: ChatGPT Codex app - MCP (HTTPS) + project skills plugin

This guide is for Codex in the ChatGPT desktop app on Windows when you want:

- `rad-mcp` as an HTTPS MCP client
- a project-local `project-skills` plugin

## 1) Make `codex` available in the current PowerShell session

```powershell
$env:Path = 'C:\Users\<you>\AppData\Local\OpenAI\Codex\bin\<version>;' + $env:Path
codex --help
```

## 2) Register `rad-mcp` as an HTTPS MCP server in Codex

Store bearer token in Codex user env file:

```powershell
'RAD_MCP_TOKEN=<your_token>' | Set-Content C:\Users\<you>\.codex\.env
```

Add server:

```powershell
codex mcp add rad-mcp --url https://127.0.0.1:8080/mcp --bearer-token-env-var RAD_MCP_TOKEN
```

Verify:

```powershell
codex mcp list
codex mcp get rad-mcp
Get-Content C:\Users\<you>\.codex\config.toml
```

Expected config entry:

```toml
[mcp_servers.rad-mcp]
url = "https://127.0.0.1:8080/mcp"
bearer_token_env_var = "RAD_MCP_TOKEN"
```

## 3) TLS requirements for `https://127.0.0.1:8080/mcp`

Server certificate should include:

- `CN = MCP-1`
- SAN `IP = 127.0.0.1`
- SAN `DNS = localhost`
- `extendedKeyUsage = serverAuth`

On Windows, import trust chain with `certlm.msc`:

- root CA -> `Trusted Root Certification Authorities\Certificates`
- intermediate/subordinate CA -> `Intermediate Certification Authorities\Certificates`

Without a valid trust chain, Codex may fail TLS validation even if the listener is running.

## 4) Add project marketplace and install plugin

Use the project root as marketplace path (not `.agents\plugins` itself):

```powershell
codex plugin marketplace add <project_root>
codex plugin marketplace list
codex plugin list
```

Install plugin:

```powershell
codex plugin add project-skills@personal
codex plugin list
```

## 5) Restart and verify in a new task

1. Restart ChatGPT Codex desktop app.
2. Start a new task in the project folder.
3. Verify with prompts:
   - `list MCP resources`
   - `show me the rad-mcp tools available in this task`
   - `show me the skills available in this chat`

Expected resources include `rad://inventory` and `rad://backups`.

## 6) Listener ownership reminder

Codex does not start your external HTTPS MCP listener. Start/restart the listener separately, for example with:

- `scripts/install/mcp_server/install-and-restart-mcp-server.ps1`
- `scripts/install/mcp_server/install-and-restart-mcp-server.sh`

## 7) Security reminder

Do not hardcode live bearer tokens in project `.mcp.json`, chat messages, or shared docs. Prefer `C:\Users\<you>\.codex\.env`.
