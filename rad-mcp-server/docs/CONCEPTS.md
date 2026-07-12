# rad-mcp concepts — every principle in one place

The one-file digest of how this toolkit thinks. Each section states the
principles and links to the doc that owns the details. Nothing here is new —
it is gathered from the READMEs, INSTALL.md, the docs/, and the skills.

## 1. The idea

**The knowledge is the product; the server is its hands.** The main asset
is the skill layer: firmware-exact CLI truth harvested live from real
units, user manuals ingested into greppable chapters with CLI cross-links,
a verified command map, personas, and safety rules — expertise no generic
model has, captured once and loaded by any Agent-Skills client unmodified.
The MCP server matters as the execution arm (staged writes, whitelisted
reads, live `?` relay) — as important as hands are, and still second
fiddle to the brain. Surface both through whatever integration each AI app
supports: skills, plugin, zips, URL; only thin per-app wrappers differ.
→ [root README](../../README.md)

## 2. Three artifact kinds

**Tools do, skills know, commands orchestrate.**

- **MCP tools** — executable device verbs (`run_show`, `health_check`,
  `stage_config`, …); work in any MCP client.
- **Skills** — auto-loading knowledge (Agent Skills open standard — Claude,
  Copilot, and Codex all load the same `SKILL.md` folders unmodified).
- **Slash commands** — procedures fired deliberately by typing
  (`/rad-health …`); Claude-plugin format, Claude Code only. A skill loads
  itself; a command never runs until typed — that's why `/rad-harvest` is
  absent from skills listings.
→ [INSTALL.md, Part 1](../INSTALL.md#the-three-artifact-kinds-used-throughout-these-docs)

## 3. Three MCP / connector deployment modes

1. **Local (stdio)** — the client spawns and owns its own server process.
   The only mode with writes.
2. **Shared server you host (HTTPS)** — one `RAD_MCP_TRANSPORT=http`
   process; bearer token per consumer; read-only forced in code; native TLS.
3. **Client to someone else's server** — URL + token, zero install.

Corollaries: the same stdio entry in N clients = N independent processes
(disk state shared: inventory, `.env`, backups, audit log; memory state
per-instance: staged configs, SSH sessions; restarts per-client). A config
entry has two shapes — stdio = "how do I launch it" (client owns process),
http = "where do I find it" (you run the server manually; the client can't
start or stop it).
→ [INSTALL.md, Part 1](../INSTALL.md#choose-a-deployment-mode-first) ·
[connecting-remote-mcp.md](connecting-remote-mcp.md)

## 4. The safety model

- **Look before you touch** — health/connectivity check before config work.
- **Staged writes only:** backup → `stage_config` → diff preview → **explicit
  human approval** → `commit_config` → verify. No exceptions, no shortcuts.
- **Execution gate:** any device command that answers the user — reads
  included — is shown first and waits for "Run this on the device now?".
- **Reads are whitelisted;** `admin` (reboot/factory-default) and `file`
  delete commands are out of scope by design; `clear-*`/`delete` tokens are
  writes.
- **Interlocks in code, not config:** http transport forces read-only and
  refuses to start without tokens; TLS is fail-closed (cert XOR key =
  refuse); write tools simply don't exist remotely.
- **Check documented limits before additive writes** (key counts, server
  counts — the manual knows, the `?` help doesn't).

**Code guarantees vs behavioral rules — know which is which.** The
interlocks live in code and cannot be talked around: http transport is
read-only and token-gated, writes need `commit_config(confirm=true)`, reads
are whitelisted. The **execution gate** ("Run this on the device now?") is
a *skill* rule — it works only if the agent loads and honors the skill,
which varies by model and app (observed 2026-07-11: Codex in the ChatGPT
desktop app ran a device read without asking after its skill load failed).
On non-Claude surfaces, back the gate up explicitly: say at session start
*"ask my confirmation before ANY device command, reads included"* — and on
Codex also put that line in `~/.codex/AGENTS.md`, which is re-read every
run, unlike skills.
→ [rad-core skill](../skills/rad-core/SKILL.md) ·
[architecture.md](architecture.md) (7-point safety model)

## 5. Credentials and inventory

- **Facts and secrets never share a file:** `inventory.yaml` holds
  name/host/family/port/groups only; credentials live **only** in
  `server/.env` (`RAD_MCP_<NAME>_USERNAME/_PASSWORD`, or the globals) and
  never pass through an MCP tool argument or response.
- **The inventory is personal:** gitignored; a clone starts empty
  (`inventory.example.yaml` is the template); the first `add_device`
  creates the file automatically. "Inventory file not found" on a fresh
  install means *empty*, not *broken*.
- **Adding a device requires all six facts from the user** (name, host,
  family, group, username, password) — the intake gate; nothing is written
  until all are given.
- **Restart semantics:** inventory is re-read every call (no restart);
  NEW `.env` keys are picked up automatically (no restart); only a CHANGED
  value of an already-loaded key, or a code change, needs a restart.
→ [rad-device-mng skill](../skills/rad-device-mng/SKILL.md) ·
[INSTALL.md common setup](../INSTALL.md#common-setup-once-per-machine)

## 6. The knowledge layers

Device `?`-help harvested live → canonical jsonl → grep-friendly
`cli-reference-<family>.md` + command tree + `rad://` MCP resources; user
manuals ingested → per-chapter markdown + cross-links. Lookup order: recipes
in the skill → `verified-commands.md` (the growing, family-annotated command
map) → the full CLI reference → live `cli_help` only for drift or pre-write
verification. **Commands are family-specific** — a row must state which
families it was verified on (e.g. `show resources` exists on secflow/etx1p,
not etx2); never claim `all` unchecked. Syntax comes from the reference;
concepts, limits, and alarm meanings come from the manual.

**Lexical retrieval — deliberately NOT (yet) RAG.** Strict RAG means
embedding the corpus into vectors and retrieving by semantic similarity.
The manual layer is the simpler, more auditable cousin: **structured
lexical retrieval** — the PDF is split along its own TOC into per-chapter
markdown plus a CLI-topic → chapter cross-link index, and at answer time
the model greps, it doesn't vector-search. For one bounded, well-structured
manual this is the right tool: exact-match retrieval is auditable (you see
which lines were pulled), free, offline, and drift-proof (re-ingest simply
replaces the markdown). It graduates to real RAG (planned layer 6) when the
corpus spans many manuals/firmwares or users ask conceptual questions whose
wording never lexically appears — the lexical layer is the foundation RAG
builds on, not a throwaway.
→ [rad-cli-operations skill](../skills/rad-cli-operations/SKILL.md) ·
[architecture.md](architecture.md) ("How the manual layer contributes —
and is it RAG?") · [manual-quality.md](manual-quality.md) ·
[performance.md](performance.md)

## 7. The skills and how to drive them

Three skills: `rad-core` (safety contract), `rad-cli-operations` (CLI
expert: personas Abayev/Noam/"rad agent", spoken toggles for verbosity and
reference-trust, five operation categories — syntax lookup, device inquiry,
device changes, manual questions, knowledge upkeep), `rad-device-mng`
(inventory CRUD + onboarding). Skills answer to plain language; the four
slash commands package recurring procedures.
→ [root README, skills section](../../README.md) · the three
[skills/](../skills/) SKILL.md files

## 8. Cross-client truths (verified, not assumed)

- User-level config lives in the same `~/.<tool>` dotfolders on Windows and
  Linux; only GUI apps differ (`%APPDATA%` vs `~/.config`).
- Per-client MCP config differs only cosmetically (root key `mcpServers` vs
  `servers`, JSON vs TOML) — each install guide shows both modes in its
  client's exact syntax.
- Claude Desktop's config file is **stdio-only** (http entries silently
  ignored — remote goes via the Connectors UI). Copilot CLI **discovers
  `.mcp.json` in the launch directory** — a repo-shipped one with foreign
  paths fails to spawn until rewritten. Skills load at session start on
  Copilot/Codex; Desktop only sees re-uploaded zips.
A target counts as **verified** only after a real end-to-end session on
real hardware — configuration written by hand is not verification. Current
status:

| Target | Type | Status | Client version | Model | Proven by |
|---|---|---|---|---|---|
| Claude Code — VS Code extension | IDE ext | ✅ | 1.128.0 | Claude Fable 5 (also Opus 4.x in earlier sessions) | daily development driver through 2026-07-11; both stdio and shared-http modes (Windows) |
| Claude Code — CLI | CLI | ✅ | *to record* (`claude --version`) | *to record* | live session 2026-07-11 on Linux: user-home install (`claude mcp add -s user` + `~/.claude/skills` + `~/.claude/commands`) — the "any project" usage shape; rad-mcp connected from a non-repo folder |
| Claude Desktop | Desktop | ✅ | 1.20 | Claude Fable 5 | stdio MCP + uploaded skill zips in production use; config file proven stdio-only, 2026-07-10 |
| GitHub Copilot — VS Code | IDE ext | ✅ | 0.41 | GPT-5.3-Codex | live session 2026-07-10: agent mode, MCP tools, skills from `.claude/skills/`. Second machine 2026-07-12 (VS Code 1.100): http client to a remote server + the older-VS-Code skills fallback — both worked |
| GitHub Copilot — CLI (Linux) | CLI | ✅ | 1.0.70 | Claude Sonnet 4.6 | live session 2026-07-11 on Rocky 8.9: fresh-clone flow end to end — skill triggers, intake gate, inventory auto-create, restart-free credentials |
| Codex — ChatGPT desktop app | Desktop | ✅ | 27.7 (engine 0.144.0-alpha.4) | GPT-5.6 Sol (session; config.toml default gpt-5.4, reasoning medium) | live session 2026-07-11: MCP tools via the shared http server; Plugins → MCPs UI honored `enabled` flags. **Caveat stands:** first session skipped the skill's execution gate (skill failed to load) — now backstopped by `~/.codex/AGENTS.md`, re-verified working |
| Codex — IDE extension | IDE ext | ⏳ | — | — | shares the verified config.toml; no dedicated session test yet |

No **web** row by design: browser/cloud surfaces (ChatGPT web, Codex cloud,
claude.ai) run outside your network and cannot reach an internal-only
rad-mcp — see [connecting-remote-mcp.md](connecting-remote-mcp.md)'s cloud-clients note.

Versions and models matter here: the Codex gate failure was a *behavioral*
issue, and behavior shifts across model/client updates — a ✅ is a statement
about the recorded combination, not the target forever.

→ [INSTALL.md](../INSTALL.md) (matrix with the same status) ·
[docs/install/](install/) per-target guides

## 9. Where everything else is

- [architecture.md](architecture.md) — the full design: stack, drivers,
  knowledge strategy, distribution roadmap.
- [connecting-remote-mcp.md](connecting-remote-mcp.md) — hosting the shared server (mode 2).
- [tests/README.md](../tests/README.md) — the knowledge-coverage eval
  harness; [tests/eval-report.md](../tests/eval-report.md) and
  [tests/RESULTS.md](../tests/RESULTS.md) — its findings.
- [vendor-mcp-baseline.md](../../vendor-mcp-baseline.md) — the vendor-MCP
  survey this project is modeled on.
- [TODO.md](../../TODO.md) — the living task list.
