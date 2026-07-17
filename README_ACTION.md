# RAD Agent Toolkit

**Talk to RAD network devices in plain language — inspect, query, and safely
reconfigure them through any AI assistant.**

The toolkit gives AI agents (Claude, Copilot, Codex) a complete knowledge base
of RAD devices and a live MCP connection to real equipment. It combines
firmware-exact CLI references, ingested device manuals, SNMP knowledge, and a
guarded change-execution engine in one package.

> **Internal RAD pilot — lab equipment only.** Do not connect to production devices.

---

## What you can ask

Trigger the agent by addressing it as **"rad agent"**, **"abayev"**, or **"noam"** in your AI chat:

| Category | Example prompt |
|---|---|
| Device management | `"rad agent, add my ETX-2 to the lab inventory"` |
| Live device state | `"abayev, show the active alarms on sf-163-187"` |
| Configuration change | `"abayev, change the location of sf-163-187 to TLV lab rack 3"` |
| Manual / concept lookup | `"rad agent, explain zero-touch provisioning on the MiNID"` |
| Network design | `"abayev, design an ERP ring using three ETX-2 units"` |
| SNMP | `"abayev, walk IF-MIB on etx2v-1 and summarize interface errors"` |
| Knowledge upkeep | `"rad agent, harvest the CLI reference for the new device"` |

See the full [prompt library](rad-mcp-server/docs/examples.md) (18 ready-to-paste examples).

---

## How it works

```
Your prompt
   │
   ├─► Skills  ─── device knowledge, CLI references, manuals, safety rules
   │
   ├─► MCP tools ─ live SSH/SNMP connection to the device
   │
   └─► Your RAD device
```

The **skill layer** decides what is valid for the selected device family — it
carries firmware-exact CLI references, ingested manuals, and SNMP maps. The
**MCP server** is the execution arm that puts that knowledge to work on real
devices.

Every configuration change follows a guarded, multi-step workflow — nothing
touches a device silently:

```
backup → stage → preview → your approval → commit → verify
```

---

## Supported devices

| Family | Products | Firmware | Status |
|---|---|---|---|
| `secflow` | SF-1p and SecFlow gateways | 6.5.0 | ✅ Verified live |
| `etx1p` | ETX-1p demarcation units | 6.5.0 | ✅ Verified live |
| `etx2` | ETX-203AX, ETX-205A, ETX-220A, ETX-2I | 6.8.5 | ✅ Verified live |
| `mp4100` | Megaplex-4100 multiservice access nodes | 4.91 | ✅ Verified live |
| `mp1` | MP-1 | 2.20 | ✅ Verified live |
| `minid` | MiNID miniature NID | 2.6 | ✅ Verified live |
| `etx2v` | ETX-2V / uCPE-OS | 5.0.0 | ✅ Verified live |
| `etx1` | Legacy ETX-1 (menu CLI) | — | 🔲 Planned |

Each family has its own driver and harvested knowledge set. The agent never
assumes a command from one family exists on another.

---

## Prerequisites

- Python **3.11+** (3.10 minimum). On RHEL/Rocky/Alma the system `python3` is
  often 3.6 — install `python3.11` separately.
- SSH reachability to your RAD devices from the machine running the server.
- One supported AI client: Claude Code, Claude Desktop, GitHub Copilot (VS Code
  agent mode), or OpenAI Codex.

---

## Quick start

```bash
# 1. Clone
git clone https://github.com/uzigolan/rad-agent-toolkit
cd rad-agent-toolkit

# 2. Add device credentials (never committed)
cp rad-mcp-server/inventory.example.yaml rad-mcp-server/inventory.yaml
# edit inventory.yaml to add your device(s)
# create rad-mcp-server/server/.env with RAD_MCP_USERNAME and RAD_MCP_PASSWORD

# 3. Run the installer for your AI client
#    (Claude Code, Claude Desktop, Copilot, or Codex)
#    See rad-mcp-server/INSTALL.md

# 4. Restart the client and ask:
rad agent, list the managed devices
```

Full setup: [Installation guide](rad-mcp-server/INSTALL.md) |
Per-client scripts: [scripts/install/](rad-mcp-server/scripts/install/skills_and_mcp/README.md)

---

## Safety

| Guarantee | How it's enforced |
|---|---|
| No silent changes | Every write is staged, previewed, and requires explicit approval |
| Safe reads only | `run_show` accepts only a per-family whitelist of read commands |
| SNMP is read-only | GET/GETNEXT only — no SET operations |
| Credentials are never exposed | Stored only in gitignored `server/.env`; redacted from audit logs |
| Dangerous ops refused | Reboot, factory-default, file delete — out of scope by design |
| Global read-only mode | `RAD_MCP_READONLY=true` removes all write tools at startup |

Full model: [docs/architecture.md](rad-mcp-server/docs/architecture.md)

---

## Project map

| Path | Purpose |
|---|---|
| [`rad-mcp-server/`](rad-mcp-server/) | Everything: MCP server, drivers, skills, references, scripts |
| [`rad-mcp-server/server/rad_mcp/`](rad-mcp-server/server/rad_mcp/) | Python package — FastMCP server, device drivers, inventory |
| [`rad-mcp-server/skills/`](rad-mcp-server/skills/) | SKILL.md files loaded by the AI agent |
| [`rad-mcp-server/skills/rad-cli-operations/references/`](rad-mcp-server/skills/rad-cli-operations/references/) | Harvested CLI references, command trees, manuals, SNMP maps |
| [`rad-mcp-server/scripts/`](rad-mcp-server/scripts/) | CLI harvester, manual ingestion, eval harness, install scripts |
| [`rad-mcp-server/commands/`](rad-mcp-server/commands/) | Slash commands: `/rad-health`, `/rad-backup`, `/rad-harvest` |
| [`rad-mcp-server/INSTALL.md`](rad-mcp-server/INSTALL.md) | Installation and client setup |
| [`rad-mcp-server/docs/examples.md`](rad-mcp-server/docs/examples.md) | 18 ready-to-paste prompts |
| [`rad-mcp-server/docs/CONCEPTS.md`](rad-mcp-server/docs/CONCEPTS.md) | Operating model, artifact kinds, deployment modes |
| [`TODO.md`](TODO.md) | Roadmap and open work |

For the full MCP tool reference and server configuration, see the
[rad-mcp-server README](rad-mcp-server/README.md).
