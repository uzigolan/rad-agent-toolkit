# Install target: GitHub Copilot CLI (`copilot` terminal agent)

Verified live 2026-07-11 on Linux (Rocky 8.9, Python 3.11): full
fresh-clone flow — skills trigger, intake gate, inventory auto-create,
restart-free `.env` pickup.

| Capability | Status | Guide |
|---|---|---|
| MCP tools | ✅ `~/.copilot/mcp-config.json` (local or http) | **[mcp.md](mcp.md)** |
| Skills | ✅ native Agent Skills (folders, no zips) | **[skills.md](skills.md)** |
| Slash commands | ✅ skills invocable by name; `/skills` to manage | [skills.md](skills.md) |

**Prerequisite for MCP:** the [common setup](../../../INSTALL.md#common-setup-once-per-machine)
(Linux venv build is in mcp.md). Skills need only the repo folders.

The two installs are independent; install both.

## Linux quick start (complete, exactly as verified)

```bash
sudo dnf install -y python3.11
cd $HOME
git clone https://github.com/uzigolan/rad-agent-toolkit.git
cd $HOME/rad-agent-toolkit/rad-mcp-server/server
python3.11 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -e .
cat > .env <<'EOF'
RAD_MCP_USERNAME=<user>
RAD_MCP_PASSWORD=<password>
EOF
cd ../..
mkdir -p ~/.copilot ~/.copilot/skills
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
cp -r rad-mcp-server/skills/rad-core rad-mcp-server/skills/rad-cli-operations rad-mcp-server/skills/rad-device-mng ~/.copilot/skills/
```

(If you'll launch `copilot` from the repo root, also rewrite the repo's
`.mcp.json` with local paths — see mcp.md's launch-directory note.)

Then `copilot` → `/mcp show` · `/skills list` · *"rad agent, list the
managed devices"* → *"rad agent, add my device"* (six-field intake, file
auto-created) → *"test connectivity to <name>"* (no restart needed).
