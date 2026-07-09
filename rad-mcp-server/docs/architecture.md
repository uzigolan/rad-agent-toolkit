# rad-mcp architecture

**What this is:** the official-vendor MCP server + Claude Code plugin for
operating RAD Data Communications devices in natural language — health checks,
config backup, syntax discovery, and guarded provisioning. Modeled on the
precedent set by `Juniper/junos-mcp-server` and Cisco's RADkit MCP server;
as of July 2026 no RAD MCP server exists anywhere, so this is RAD's entry
into the MCP ecosystem.

> The `rad-mcp-server/` directory is the **full toolkit** — MCP server +
> skills + commands + plugin — not only the server; the name is kept for path
> stability (venv, configs, Desktop). The umbrella repo is `rad-agent-toolkit`.

## The stack

```
 Claude surfaces          Claude Code (VS Code / CLI)  ·  Claude Desktop chat  ·  Cowork
        │
 knowledge layer          skills (rad-core, rad-cli-operations)
        │                 + references/ (harvested command trees)
        │                 + slash commands (/rad-health, /rad-backup — Code only)
        │
 MCP server               rad_mcp.server  (Python, FastMCP, stdio)
        │                 tools: list_devices · test_connectivity · run_show ·
        │                 run_show_in_context · cli_help · get_config ·
        │                 health_check · backup_config · stage_config ·
        │                 commit_config · save_startup
        │                 resources: rad://inventory · rad://backups[/name] ·
        │                 rad://command-tree/{family}
        │
 backends (transport)     ssh (Netmiko, device_type rad_etx)   [now]
        │                 radview northbound API                [planned]
        │
 drivers (CLI dialect)    radcli.py — shared context-CLI dialect
        │                   ├── secflow  (SF-1p — verified live)
        │                   └── etx2     (ETX-203AX/205A/220A — pending live check)
        │                 etx1, mp4100/Megaplex — different CLIs, own drivers [planned]
        │
 devices                  inventory.yaml (name/host/family/groups; creds in server/.env)
```

**Why backend × driver?** Transport and dialect vary independently across the
RAD portfolio. SSH now and RADview later must both drive a SecFlow; one SSH
session must be able to drive both a SecFlow and (different dialect) a
Megaplex. Tools stay product-agnostic verbs; the device's `family` field
picks the driver, config picks the backend.

## Safety model (the core design constraint)

Network gear is production infrastructure; every write is treated as
dangerous until a human approves it.

1. **Read whitelist** — `run_show`/`run_show_in_context` accept only
   driver-whitelisted read prefixes; context navigation is validated against
   known contexts and a strict token charset.
2. **Staged commits** — writes go `stage_config` (returns preview, touches
   nothing) → human reviews the diff → `commit_config(stage_id, confirm=true)`.
   The confirm flag is required and the skill forbids setting it without
   explicit user approval in-conversation.
3. **Automatic pre-commit backup** — every commit first snapshots the running
   config to `server/backups/`; the commit output includes the restore path.
4. **`cli_help` never executes** — it relays the CLI's interactive `?` help by
   typing `<prefix>?` and then clearing the pending line (Ctrl-U); newlines
   and control characters in the prefix are refused.
5. **Read-only mode** — `RAD_MCP_READONLY=true` removes every write tool at
   registration time (they don't exist in the session at all).
6. **Append-only audit** — every tool call lands in `server/logs/audit.jsonl`
   with secrets redacted.
7. **Defense in depth** — the same rules live in the skills (Claude refuses
   before trying) and in the server (the tool refuses if asked anyway).
   Dangerous CLI areas (`admin` reboot/factory-default, `file` delete) are
   documented as no-go zones and are not whitelisted.

## Knowledge layers (how Claude "knows" the CLI)

The RAD CLI is huge (2,000+ nodes on SF-1p alone) and context-based — `show`
commands only exist inside contexts. No static prompt could hold it, so
knowledge is layered from cheap/static to live/exact:

| Layer | What | When Claude uses it |
|---|---|---|
| 1. Skill | `rad-cli-operations/SKILL.md`: CLI model, verified command map, **common config recipes**, safety rules | always loaded for RAD work; recipes answer frequent asks with zero lookups |
| 2. References | `references/cli-help-<family>.jsonl` (canonical) → `cli-reference-<family>.md` (rendered) + `command-tree-<family>.md`: the device's **complete `?` help**, every context incl. parameterized ones under `NAME` placeholders | syntax questions answered by grepping a `## <context path>` header — zero device I/O |
| 3. Live `?` help | `cli_help` tool: firmware-exact ground truth (~1 s warm) | firmware drift, pre-write verification, contexts the harvest can't enter |
| 4. Manual | `references/manual-<family>/` (per-chapter markdown + index), via `scripts/ingest_manual.py`; resources `rad://manual/{family}[/{chapter}]` | **concepts, procedures, limits, alarm meanings** the `?` help can't give (e.g. "max 2 MQTT servers", enrollment workflow) — cross-linked to CLI contexts |
| 5. MCP resources | `rad://inventory`, `rad://backups`, `rad://command-tree/{family}`, `rad://cli-reference/{family}[/{context}]`, `rad://manual/{family}[/{chapter}]` | surfaces without filesystem access (Desktop) |
| 6. Manuals RAG | `search_docs` — semantic search / embeddings over the manual corpus | planned — layer 4 already makes the text greppable; RAG adds fuzzy recall at fleet scale |

The layers reinforce each other: skills teach the *method* (recipe → reference
grep → manual for concepts → live verify → stage), references give the *map*,
the manual gives the *meaning*, and `cli_help` gives ground truth that can
never drift from the firmware. New verified findings are folded back into
layers 1–2 after each session.

Two ingest pipelines feed the knowledge layers, independent and
non-overwriting. **Layer 2 (syntax)** is produced by `scripts/harvest_cli.py`
(driven by **`/rad-harvest`**): it crawls every context live, enters
parameterized contexts through an existing instance or a `zzz-hrvst` temp
object rolled back immediately, and rewrites the references with an
ADDED/REMOVED/CHANGED diff — git history is the record of CLI evolution across
firmware. **Layer 4 (concepts)** is produced by `scripts/ingest_manual.py`: it
splits a user-manual PDF along its TOC into per-chapter markdown plus a
CLI-topic → chapter cross-link index. The PDF is gitignored (large binary);
the extracted markdown is committed and greppable.

**Numeric-indexed parameterized contexts** (`mep`, `lag`, `pw`, `test`,
`bridge`, `isakmp-policy`, `mirroring-session`, `ppp`, `tunnel-interface` —
`NUMERIC_CREATE_ALLOW` in `harvest_cli.py`) get the same create-then-roll-back
treatment as string-named ones, but only after two safeguards a plain
string-name temp object doesn't need:

1. **The manual vets the addition, not just the code.** Before a name is
   added to the allow-list, its manual chapter is checked for a stated
   "Factory Defaults" / default-configuration section confirming the object
   is genuinely inert on creation (no bound flow, admin-down or equivalent)
   — the same lexical-retrieval mechanism layer 4 already provides, applied
   to a safety decision instead of an answer. A name that can't be confirmed
   inert this way stays off the list (e.g. `twamp` controller/responder were
   held out pending this check).
2. **The declared range in the CLI's own `?` help is not trusted as an upper
   bound.** On etx2i, `lag` advertised `[1..4]` but rejected 4 ("Invalid LAG
   ID"), and `test` (rfc2544) declared no range at all but only accepted
   1-8 — real license/hardware limits are frequently lower than the generic
   syntax range. The harvester tries up to 6 free indices ascending from the
   bottom of the declared range rather than one guess from the top, and on
   every refusal captures the device's own error text (not just detects
   *that* it was refused) plus, for numeric attempts, one read-only
   `<name> <idx> ?` follow-up probe — so a "not entered" reference entry
   always carries a device-confirmed reason (a genuine `License required`
   gate vs. a missing second argument the harvester doesn't supply yet vs.
   no live instance existing), not a guess. See `tests/eval-report.md` for
   the etx2i case study that drove this (`pw`/`twamp responder` need a
   second argument; `twamp controller`/`profile` are a real license gate;
   `mep`/`lag`/`test` closed cleanly).

## Performance model

Two rules keep tool calls at the device-bound floor (~0.1–1 s warm):

1. **One persistent CLI session per device** (`SSHBackend`): SSH connect costs
   ~5–7 s and RAD units refuse a new session while the old one tears down, so
   sessions are cached, re-grounded with `exit all` per call, liveness-probed
   only after 60 s idle, and replaced transparently when dead.
2. **Prompt-anchored reads, never quiet-timers**: every read terminates the
   moment the device prompt reappears. Quiet-gap timeouts are last-resort
   fallbacks only — the SF-1p deterministically pauses >3 s mid-`info` dump,
   so any short quiet threshold silently truncates output (this once hid
   `router 1` from the harvester and cost the whole router subtree).

Measured warm (SF-1p over lab LAN): health ping 0.14 s, `cli_help` three
contexts deep 0.7 s, root help 0.4 s. `get_config` ~7 s — the device generates
the export that slowly; not addressable client-side.

**A third lever lives at the skill-instruction level, not the backend:**
`rad-cli-operations/SKILL.md` defines two configurable behavior modes —
response verbosity (`concise` default vs. `verbose`) and reference trust
(`trust-reference` default vs. `always-verify-live`, which skips redundant
live `cli_help` re-confirmation of answers the harvested reference already
gives completely). Both default to the faster behavior; either reverts for
the rest of a session via a spoken phrase (see SKILL.md's *"Response &
verification modes"* section for the exact switch phrases). This was added
after `docs/performance.md` §4 showed a skill run 2-3x longer than its peers,
driven by output length and a redundant live-verification call — config
knobs the backend rewrite above can't reach, since they're about how the
model itself behaves, not how the transport performs.

## The maintenance loop

```
operate live → verify a new command/behavior → update SKILL.md + references
      ↑                                                        │
      └── next session (any user, any surface) inherits it ←──┘
```

After a firmware upgrade (or whenever the reference misses a context), run
`/rad-harvest <device> [subtree]` — background harvest, diff review, temp-object
rollback verification, device-cleanliness check, and skill-copy sync in one step.

Skill copies: `skills/` in this repo is the **source of truth**; copies go to
workspace `.claude/skills/` (Claude Code), `~/.claude/skills/` (user-level),
and `dist/claude-desktop-skills/*.zip` (Desktop uploads, built by
`scripts/build_desktop_skills.py`). Sync all four when the source changes.

**Non-Claude targets:** `scripts/build_portable_bundle.py` emits
`dist/portable-agent/` — the reusable pieces for any MCP-capable client
(ChatGPT/OpenAI, Cursor, ...): the knowledge files plus a README on wiring the
MCP server (open protocol, works unchanged) and adapting SKILL.md into agent
instructions. The Claude skill/plugin format itself is not portable; the server
and the knowledge are.

## How the manual layer contributes (and is it RAG?)

For a per-family breakdown of manual quality — which source PDFs worked
out of the box vs. which needed fixes, and why — see `docs/manual-quality.md`.

**What gap it fills.** The harvested CLI reference is *complete* on syntax and
*silent* on meaning. It can tell you `certificate <name> trusted-ca <ca-name>`
is a valid line; it cannot tell you *why* `trusted-ca` is mandatory, that the
box caps you at **two** MQTT servers, what a `los` alarm signifies, or the
ordered steps of certificate enrollment. Those facts exist only in prose, in
the user manual. So the manual is a **complementary layer, not an overlap**:

| Question shape | Layer that answers | Source of truth |
|---|---|---|
| "What's the exact command / arguments?" | CLI reference (layer 2) / live `cli_help` (3) | the device |
| "What does it mean, why, how many, what order?" | **Manual (layer 4)** | the vendor manual |

**Is it RAG? Not yet — and that's deliberate.** RAG (retrieval-augmented
generation) in the strict sense means *embed the corpus into vectors, embed the
question, retrieve by semantic similarity*. The manual layer today is the
simpler, more auditable cousin: **structured lexical retrieval.**

- `scripts/ingest_manual.py` splits the PDF along its own table-of-contents
  bookmarks into one markdown file per chapter, and builds `manual-index.md` —
  a chapter list plus a **CLI-topic → chapter cross-link table** (e.g.
  `configure system mqtt → §6.9 MQTT Server`).
- At answer time the model does **keyword retrieval, not vector search**: open
  the index, follow the cross-link to the right chapter, `grep` the chapter for
  the term. Same mechanic as the CLI reference — deterministic, greppable, no
  embedding model, no vector store, no similarity threshold to tune.

**Why lexical first.** For a bounded, well-structured single manual it is the
right tool: exact-match retrieval is *auditable* (you can see precisely which
lines were pulled and cite the page), *free* (no embedding calls or index to
maintain), *offline*, and *drift-proof* (re-ingest and the markdown is simply
replaced). Vector RAG shines when the corpus is large, cross-document, and the
user's phrasing won't lexically match the text — none of which bites yet with
one 726-page manual whose own TOC already segments it by topic.

**How it affects an answer.** Concretely, in a single turn Claude can now:
grep the CLI reference for the command shape → grep the manual chapter for the
constraint/procedure → compose a paste-ready sequence that is *both* syntactically
correct *and* respects documented limits — citing the manual for the "why". None
of that touches the device. It also makes the assistant **safer on writes**: a
documented limit ("max 2 servers", "key store full") is caught before staging,
not after a commit fails.

**When it graduates to real RAG (layer 6, planned).** The lexical layer is the
foundation the RAG layer builds on, not a throwaway. Promote when: (a) the
corpus grows to *many* manuals across families/firmwares where a keyword can
match the wrong document; (b) users ask conceptual questions whose wording
doesn't lexically appear ("how do I make the link survive a fibre cut?" →
"Ethernet Ring Protection"); or (c) fleet scale makes chapter-grep too coarse.
At that point `search_docs` embeds the *already-extracted* chapter markdown
(the ingest step is unchanged) and adds semantic recall *alongside* — not
instead of — the exact cross-link lookups. Lexical stays the precise path;
RAG adds the fuzzy one.

## Distribution path

- **Now (internal pilot):** absolute venv paths in `.mcp.json` / Desktop
  config on the pilot machine.
- **Now also available — shared remote server (internal, read-only):**
  `RAD_MCP_TRANSPORT=http` serves one authenticated read-only endpoint that
  many clients connect to by URL (no per-user local install). Read-only and
  bearer-auth are enforced in code; internal-network hosting only. See
  `docs/remote-server.md`.
- **Next:** publish the `rad-mcp` Python package internally → configs become
  `uvx rad-mcp` (self-contained installs); package an `.mcpb` Desktop
  Extension for one-click NOC installs; plugin marketplace moves from local
  directory to a git URL.
- **Later:** RADview backend for fleet-scale operations; remote *write* access
  with per-token scopes; external/cloud reach via a hardened gateway;
  manuals-RAG (`search_docs`) as the vendor-exclusive differentiator.

## Roadmap snapshot (July 2026)

- [x] SecFlow driver verified live (SF-1p, Sw 6.5.0.35) — reads, staged
      writes, backups, health, `cli_help`
- [x] Claude Code plugin (skills + commands) and Desktop deployment
- [ ] Git version control + internal repo
- [ ] ETX-2 live verification (driver written, needs lab time)
- [ ] Packaging: `uvx rad-mcp`, `.mcpb`, marketplace via git
- [ ] ETX-1 and MP-4100/Megaplex dialect drivers
- [ ] RADview northbound backend
- [x] Device manual layer (ETX-1p): PDF → per-chapter markdown + CLI cross-links
- [ ] Manuals RAG (semantic search over the manual corpus)
