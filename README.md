# RAD Agent Toolkit

**Talk to RAD devices in plain language. Inspect with CLI or SNMP. Make
changes through a guarded workflow.**

The toolkit gives AI agents practical knowledge of RAD devices and a safe MCP
connection to real equipment. It combines firmware-exact CLI references,
device manuals, product datasheets, SNMP knowledge, and live device tools in
one package.

> **Lab use only.** Use lab equipment only. Do not connect this project
> to production devices.

## What can I ask?

- **Device management:** `"rad agent, add my ETX-2 to the lab inventory"` or
  `"noam, show the list of managed devices"`.
- **CLI operations:** `"abayev, show the active alarms on sf-163-187"` or
  `"abayev, change the location of sf-163-187 to TLV lab rack 3"`.
- **Network engineering:** `"rad agent, explain zero-touch provisioning on the
  MiNID"` or `"abayev, design an ERP ring using three ETX-2 units"`.
- **Advanced:** `"rad agent, compare ETX-2 and ETX-2V QoS"` or
  `"noam, compare a competitor with ETX-2 for an ERP rollout"`.
- **SNMP operations:** `"rad agent, check SNMP on etx2v-1"` or
  `"abayev, walk IF-MIB on etx2v-1 and summarize interface errors"`.
- **Hardware & product selection (datasheets):** `"noam, which Megaplex-4 card
  gives me 16 E1 ports, and what are its ordering options?"`.
- **Onboarding a new device type:** `"rad agent, harvest the new device CLI"` or
  `"abayev, add these MIB files to the SNMP knowledge layer"`.

The agent answers from family-specific CLI references, manuals, product
datasheets (hardware specs, interfaces, variants, ordering), and SNMP maps.
When live access is needed, it can inspect device state, perform read-only SNMP
checks, back up configurations, and prepare guarded configuration changes.

Live access uses two independent paths: the device **CLI over SSH _or_ telnet**
(chosen per device by its inventory `transport` — SSH by default, telnet for
units where SSH isn't available), and a **separate, read-only SNMP** path
(GET/GETNEXT only, never SET) for identity, counters, and MIB lookups.

See [more ready-to-paste prompts](rad-mcp-server/docs/examples.md).

## How it works

```text
Your question
    |
    +-- Skills: RAD device knowledge and safety rules
    |
    +-- MCP tools: CLI, SNMP, inventory, backup, and staged changes
    |
    +-- Your RAD device
```

The skill decides what is valid for the selected device family. The MCP server
provides the live connection. Read operations require confirmation, and writes
follow:

```text
backup -> stage -> preview -> approve -> commit -> verify
```

No configuration change is committed without explicit approval.

## Supported devices

| Family | Products | Status |
|---|---|---|
| `secflow` | SF-1p and SecFlow gateways | Verified live |
| `etx1p` | ETX-1p | Verified live |
| `etx2` | ETX-203AX, ETX-205A, ETX-220A, ETX-2I | Verified live |
| `mp4100` | Megaplex-4100 | Verified live |
| `mp1` | MP-1 | Verified live |
| `minid` | MiNID | Verified live |
| `etx2v` | ETX-2V / uCPE-OS | Verified live |
| `etx1` | Legacy ETX-1 menu CLI | Planned |

Each supported family has its own driver and knowledge set. The agent does not
assume that a command or feature from one family exists on another.

## Quick start

1. Clone the repository.
2. Create `rad-mcp-server/server/.env` with your device credentials.
3. Run the installer for your AI client.
4. Restart the client and ask:

```text
rad agent, list the managed devices
```

Installers are available for Claude Code, Claude Desktop, GitHub Copilot, and
OpenAI Codex.

Start with the [installation guide](rad-mcp-server/INSTALL.md), or go directly
to the [client installer scripts](rad-mcp-server/scripts/install/skills_and_mcp/README.md).

## Safety

- Device commands are shown before they run and require confirmation.
- SNMP access is read-only.
- CLI reads are restricted to approved commands.
- Configuration writes are backed up, staged, previewed, approved, and verified.
- Reboot, factory-default, and similar dangerous operations are out of scope.
- Credentials stay in the gitignored `.env` file and are redacted from logs.
- `RAD_MCP_READONLY=true` removes all write tools.

See the full [safety and architecture model](rad-mcp-server/docs/architecture.md).

## Project map

| Path | Purpose |
|---|---|
| [`rad-mcp-server/`](rad-mcp-server/) | MCP server, device drivers, skills, references, and scripts |
| [`rad-mcp-server/skills/`](rad-mcp-server/skills/) | RAD operations, safety, and device-management skills |
| [`rad-mcp-server/INSTALL.md`](rad-mcp-server/INSTALL.md) | Installation and client setup |
| [`rad-mcp-server/docs/examples.md`](rad-mcp-server/docs/examples.md) | More prompts and workflows |
| [`rad-mcp-server/docs/CONCEPTS.md`](rad-mcp-server/docs/CONCEPTS.md) | Concepts and operating model |
| [`TODO.md`](TODO.md) | Roadmap |

For server tools and technical details, continue to the
[rad-mcp-server README](rad-mcp-server/README.md).
