# Generic manual installer: skills + MCP snippets

This guide covers `install-generic.ps1` / `.sh`, a manual helper that does not
modify client config files.

Use it when you want interactive guidance and ready-to-paste snippets instead
of automatic wiring.

Meaning of "generic": you manually place the skills files and MCP
configuration wherever your AI client application, IDE, or CLI expects them.
This helper only prints what to copy and where.

## What it does

- Skills mode `served`: shows where to take `SKILL.md` only (not full directories)
- Skills mode `embedded`: builds desktop skill zip packages (same flow as Claude Desktop)
- MCP mode `stdio`: prints stdio configuration snippets
- MCP mode `http`: prints http configuration snippets with interactive URL/token prompts

## Run

```powershell
.\install-generic.ps1
.\install-generic.ps1 -Http -Url http://127.0.0.1:8080/mcp -Token <token>
.\install-generic.ps1 -SkillMode embedded
```

```bash
./install-generic.sh
./install-generic.sh --http --url http://127.0.0.1:8080/mcp --token <token>
./install-generic.sh --skill-mode embedded
```

> Windows execution-policy note:
>
> ```powershell
> PowerShell -ExecutionPolicy Bypass -File .\install-generic.ps1
> ```

## Interactive flow

1. Choose skills delivery mode:
   - served: source `SKILL.md` paths are printed; use only `SKILL.md` for each skill
   - embedded: zip artifacts are built into `dist/claude-desktop-skills/`
   - no extra knowledge prompt is shown
2. If a previous setup exists, choose whether to keep it:
   - saved at `server/.rad-mcp-generic-config`
   - keeps the RAD skills settings (delivery mode + knowledge) and MCP settings
   - in http mode this keeps both URL and token
3. If you do not keep the saved configuration, the installer asks everything again:
   - skills delivery mode
   - MCP transport
   - http URL/token (when http is selected)
4. Choose MCP transport (only when not keeping saved config):
   - stdio: local launch configuration snippets
   - http: URL/token prompt and read-only transport snippets
5. Copy the shown snippet into your client config file with the correct root key.

## Output snippets include

- VS Code Copilot (`servers` root)
- JetBrains Copilot classic MCP path (`servers` root; `requestInit` in http mode)
- JetBrains embedded Copilot CLI agent (`mcpServers` root)
- Claude Code / Claude Desktop shape (`mcpServers` root)

Tokens are masked in the displayed output.

## Notes

- This script does not write or merge config files.
- You manually place skills and MCP config in your chosen target locations per client.
- For fully automated target-specific setup, use the dedicated installers in this folder.
- Optional advanced override: `-Knowledge served|bundled` (PowerShell) or `--knowledge served|bundled` (bash).
- It writes local transport state to `server/.rad-mcp-generic-config` to support keep/reuse prompts.
