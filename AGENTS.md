# AGENTS.md — RAD Agent Toolkit

Guidance for AI agents working on this repository.

> **Lab-only pilot.** Never connect tooling in this repository to production
> RAD devices. Use lab equipment exclusively.

---

## What this repository is

`rad-agent-toolkit` is RAD Data Communications' first entry in the MCP
ecosystem: an MCP server plus a skill layer that lets AI agents (Claude Code,
Claude Desktop, GitHub Copilot, OpenAI Codex) operate the full RAD device
portfolio in natural language. Everything lives under `rad-mcp-server/`.

The **knowledge layer** (skills) is the primary asset. The **MCP server** is
the execution arm. They are independent: skills load knowledge in any
Agent-Skills-compatible client; the server provides live device tools.

---

## Repository layout

```
rad-agent-toolkit/
├── AGENTS.md                    ← this file
├── README.md                    ← project overview and quick start
├── TODO.md                      ← living roadmap
└── rad-mcp-server/              ← the full toolkit
    ├── INSTALL.md               ← setup hub for all six agent targets (start here)
    ├── docs/
    │   ├── CONCEPTS.md          ← every design principle in one file (read first)
    │   ├── architecture.md      ← stack, safety model, knowledge layers
    │   ├── workflows.md         ← end-to-end execution flows
    │   └── examples.md          ← 18 ready-to-paste prompts
    ├── server/
    │   ├── pyproject.toml       ← Python package (rad-mcp, FastMCP + Netmiko + pysnmp)
    │   └── rad_mcp/
    │       ├── server.py        ← FastMCP entrypoint (tools + resources, stdio)
    │       ├── smoke.py         ← manual smoke test against one live device
    │       ├── inventory.py     ← YAML inventory reader/writer
    │       ├── audit.py         ← append-only audit log (JSONL, secrets redacted)
    │       ├── backends/        ← transport: ssh.py (Netmiko), snmp.py (pysnmp)
    │       └── drivers/         ← CLI dialect per product family (see below)
    ├── skills/
    │   ├── rad-core/SKILL.md           ← safety rules, staged-commit workflow
    │   ├── rad-cli-operations/SKILL.md ← main operations expertise (CLI + SNMP)
    │   └── rad-device-mng/SKILL.md     ← inventory management workflow
    ├── commands/                ← slash commands (Claude Code only)
    │   ├── rad-health.md
    │   ├── rad-backup.md
    │   ├── rad-harvest.md
    │   └── rad-load-manual.md
    ├── scripts/
    │   ├── harvest_cli.py       ← live CLI harvester (updates references/)
    │   ├── ingest_manual.py     ← PDF → manual markdown (PyMuPDF)
    │   └── install/             ← per-target install scripts (PowerShell + sh)
    ├── tests/                   ← eval harness output (not a unit-test suite)
    └── inventory.example.yaml   ← device inventory template (no credentials)
```

---

## Development environment

**Prerequisites:** Python **3.11+**, SSH reachability to lab devices (for live
operations only — not required for code changes).

```bash
cd rad-mcp-server/server
python3.11 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -e .                   # runtime deps (fastmcp, netmiko, pyyaml, pysnmp)
pip install -e ".[tooling]"        # also install pymupdf (for ingest_manual.py)
```

**Credentials** (for live device work only — not needed for code changes):

```bash
cp ../inventory.example.yaml ../inventory.yaml   # edit with your lab devices
# Create server/.env (gitignored) and add SSH credentials:
#   RAD_SSH_USERNAME=...
#   RAD_SSH_PASSWORD=...
```

Credentials go **only** in `server/.env` (gitignored). Never put credentials in
`inventory.yaml`, source code, or any committed file.

---

## Running the server

```bash
# Start in stdio mode (default — the MCP client launches it automatically)
rad-mcp

# Start in HTTP mode (shared server)
RAD_MCP_TRANSPORT=http RAD_MCP_TOKENS=mytoken rad-mcp

# Read-only mode (disables all write tools)
RAD_MCP_READONLY=true rad-mcp

# Manual smoke test against one device (requires .env + SSH access)
python rad_mcp/smoke.py <device-name>
```

---

## Testing and validation

There is no automated unit-test suite. Validation is done at three levels:

1. **Smoke test** — `rad_mcp/smoke.py <device>` (run from `rad-mcp-server/server/`):
   connects to a single lab device and exercises the core tool set live.
   Requires SSH credentials and a reachable lab device.

2. **Eval harness** (reference-only, no device contact) — `scripts/check_eval_coverage.py`
   checks the harvested CLI reference against a known prompt set. Results land
   in `tests/RESULTS.md`. Run from `rad-mcp-server/`:
   ```bash
   python scripts/check_eval_coverage.py
   ```

3. **Manual session testing** — install the skills and server in your AI
   client and run conversational tests. The conversation scenarios in
   `docs/examples.md` are the canonical acceptance criteria.

Before committing Python changes, verify that the server starts cleanly:
```bash
echo '{}' | rad-mcp   # should start without error
```

---

## Three artifact types

Changes affect one or more of these three distinct artifacts. Keep them in
mind when making changes:

| Artifact | Location | What it does | Portability |
|---|---|---|---|
| **MCP tools** | `server/rad_mcp/` | Executable device operations | Any MCP client |
| **Skills** | `skills/*/SKILL.md` | Auto-loading knowledge (Agent Skills standard) | Claude, Copilot, Codex — unmodified |
| **Slash commands** | `commands/*.md` | Procedures fired by typing `/rad-*` | Claude Code only |

Tools **do**, skills **know**, commands **orchestrate**.

---

## Driver pattern

Each product family maps to one driver file under `server/rad_mcp/drivers/`.
All drivers inherit from `radcli.py` (the shared RAD context-CLI dialect), which
inherits from `base.py` (abstract interface).

To add a new product family:
1. Create `drivers/<family>.py` — subclass `RadCliDriver` (or `RadDriver` for
   a completely different CLI dialect), set `family`, `show_whitelist`,
   `configure_contexts`, `health_commands`, and implement `detect()`.
2. Add a device entry in `inventory.yaml` with `family: <family>`.
3. Register the driver in `drivers/__init__.py`.
4. Update `skills/rad-core/SKILL.md` to list the new family.
5. Harvest the CLI reference: `/rad-harvest <device>` (or `scripts/harvest_cli.py <device>`).
6. Ingest the manual if available: `/rad-load-manual` (or `scripts/ingest_manual.py`).

Two config models exist among current drivers — note which your new driver uses:
- **Direct-write** (`secflow`, `etx1p`, `etx2`, `minid`, `etx2v`): edits apply
  immediately; `save` persists to startup config.
- **Candidate-DB** (`mp4100`, `mp1`): edits land in a candidate database and
  require the device's own `commit` global before applying. The server's
  `stage_config` enforces this shape; never omit `commit` for these families.

---

## Safety rules (non-negotiable)

These rules are enforced in code and in the skills. Do not change them:

1. **Staged writes only.** All config changes must go through
   `backup_config` → `stage_config` → show diff to user → `commit_config(confirm=True)`
   only after explicit user approval. No shortcuts.
2. **Read whitelist.** `run_show` / `run_show_in_context` accept only
   driver-whitelisted command prefixes. Do not widen whitelists without
   understanding why a prefix was excluded.
3. **No dangerous commands.** The `admin` context (reboot, factory-default,
   file deletes) is excluded from all drivers by design. Do not add it.
4. **Credentials in `.env` only.** Never write credentials to inventory,
   source code, or any committed file. The audit log explicitly redacts secrets.
5. **`RAD_MCP_READONLY=true`** removes every write tool at registration time.
   This must be respected; do not add write tools that bypass the readonly flag.

---

## Skill conventions

- Each skill is a `SKILL.md` file in `skills/<name>/` with YAML frontmatter
  (`name`, `description`, `version`).
- **Bump the `version:` field and the version line in the body on every
  change.** Version drift between deployed copies and source is the primary
  way stale skills are detected.
- The `description:` field is what the AI client uses to decide when to load
  the skill. Keep it specific and accurate — it is a functional field, not
  documentation prose.
- Skills load automatically; slash commands require explicit user input
  (`/rad-harvest …`). Do not put auto-loaded behavior in commands or vice versa.

---

## Key docs to read before making changes

| File | Read when |
|---|---|
| `rad-mcp-server/docs/CONCEPTS.md` | Starting anything — every design principle |
| `rad-mcp-server/docs/architecture.md` | Changing the server or driver layer |
| `rad-mcp-server/INSTALL.md` | Changing install scripts or deployment modes |
| `rad-mcp-server/skills/rad-core/SKILL.md` | Changing safety or workflow rules |
| `rad-mcp-server/skills/rad-cli-operations/SKILL.md` | Changing CLI/SNMP operations knowledge |
| `rad-mcp-server/docs/workflows.md` | Understanding end-to-end tool flows |

---

## Codex cloud (knowledge-only mode)

OpenAI Codex cloud supports neither MCP nor LAN access. When working with this
repository from a Codex cloud session, the MCP tools are not available. Use the
skill knowledge directly:

- Skills (`skills/*/SKILL.md`) and their `references/` trees provide complete
  CLI and SNMP knowledge for all verified families without a live device.
- The portable bundle (`scripts/build_portable_bundle.py`) packages this
  knowledge for offline or cloud use.
- For device operations from a cloud context, ask a team member with local MCP
  access to run the commands.
