# TODO

Living task list. See [README.md](README.md) for the project overview and
[rad-mcp-server/docs/architecture.md](rad-mcp-server/docs/architecture.md)
for the full design.

## Done (2026-07-12 session)

- **mp4100 (Megaplex-4100) family support — end to end in one pass:**
  live probe overturned the "different CLI, own driver base" assumption
  (same context dialect; netmiko rad_etx + pager-disable work), new
  `drivers/mp4100.py` (one structural difference: candidate-DB config —
  staged sequences must end with the device's `commit`; `discard-changes`
  flagged as ambiguous/dangerous), smoke test passed (real SDH/TDM
  alarms), full CLI harvest (130 KB reference; 9 temp objects created +
  rolled back in the candidate DB; 62 parameterized gaps with reasons),
  1,202-page manual ingested (38 chapters; the etx2-built adaptive
  splitter fired automatically — validation recorded in
  `docs/manual-quality.md` along with the cross-link vocabulary gap:
  matcher topics are ETX-shaped, MP areas like cross-connect/pwe/
  teleprotection got no rows). Skills/READMEs updated; device
  `marks-mp4` registered.
- [ ] Cross-link matcher: per-family topic vocabulary (or derive from the
  family's command tree) — mp4100's headline areas are unmatched.
- [ ] Cross-check the verified-commands table against
  `cli-reference-mp4100.md` and extend its `Families` column to mp4100.

## Done (2026-07-10 session)

- **Per-target install guides for 6 agent surfaces.** ⚠️ **Written from
  official-docs research (July 2026), not yet verified against live
  Copilot/Codex installs.** `INSTALL.md` restructured into a hub (support
  matrix + common setup + remote-connect + shared troubleshooting) with
  per-target guides in `rad-mcp-server/docs/install/`: Claude Code
  (VS Code ext), Claude Code (CLI), Claude Desktop (chat + Cowork), GitHub
  Copilot (VS Code agent mode), GitHub Copilot CLI, and OpenAI Codex
  (CLI/IDE/desktop + cloud). Key findings baked into the guides:
  - Copilot and Codex both adopted the **Agent Skills** open standard
    (SKILL.md) — the RAD skills install unmodified. Copilot even reads the
    repo's `.claude/skills/` natively; Codex needs a copy into
    `.agents/skills/` (repo) or `~/.agents/skills/` (user).
  - MCP config root keys differ per client: VS Code Copilot = `servers`,
    Copilot CLI = `mcpServers` with `type: "local"` (no `cwd` — safe, the
    server is module-anchored), Codex = `[mcp_servers.<name>]` in
    `~/.codex/config.toml` (`cwd` supported; shared by CLI/IDE/desktop).
  - Codex **cloud** supports neither MCP nor LAN access — documented as
    knowledge-only via `AGENTS.md` + the portable bundle.
  - Root README integration table updated (Skills row now lists
    Copilot/Codex; roadmap bullet closed).

## Done (2026-07-09 session)

- **Device inventory CRUD + `rad-device-mng` skill.** ⚠️ **Built, not
  yet tested end-to-end via real conversation or a live device — only
  verified at the code level (direct `mcp.call_tool()` calls in isolation:
  add → update → list → remove round-trip on a scratch inventory file).
  Still needs a real session testing the skill actually loading on the
  right trigger phrases, and a real `add_device` → `.env` → restart →
  `test_connectivity` pass against a real device.** New MCP tools
  `add_device`/`update_device`/`remove_device` (write tools — local/stdio
  only, never over shared HTTP, same interlock as `stage_config`) alongside
  the existing read-only `list_devices`, so a user who receives this
  plugin/skill set can self-onboard their own equipment instead of being
  limited to the pre-shipped lab units. `inventory.py` gained
  `add_device_entry`/`update_device_entry`/`remove_device_entry` — text-based
  append/edit (not a YAML round-trip) so the file's own safety header
  comment and formatting survive untouched. New skill
  `skills/rad-device-mng/SKILL.md` documents the full workflow,
  especially the credentials split (inventory.yaml = facts only; `.env` =
  credentials, and the running server must be **restarted** to pick up new
  `.env` values — it loads once at process start). `rad-core/SKILL.md`
  updated to cross-reference it and fix stale family-status text (`etx1p`
  was missing from the list entirely; `etx2` still said "pending live
  verification").
- **ETX-2 live verification.** First live etx2 driver verification (ETX-2I,
  Hw 0.2/D, Sw 6.8.5(1.116)). Added to `inventory.yaml`. Found and fixed a
  real driver gap: `configure_contexts` was missing `"test"`, so
  `cli_help`/`run_show_in_context` refused the entire Y.1564/RFC2544/L3SAT
  subtree even though the harvester had already proven it real.
- **Harvester: numeric-indexed parameterized-context auto-create.**
  `scripts/harvest_cli.py`'s create-then-roll-back mechanism (previously
  string-named temp objects only, e.g. `zzz-hrvst`) now also covers
  numeric-indexed contexts: `mep`, `lag`, `pw`, `test`, `bridge`,
  `isakmp-policy`, `mirroring-session`, `ppp`, `tunnel-interface`
  (`NUMERIC_CREATE_ALLOW`). Two safeguards specific to numeric contexts:
  - Each addition is checked against the family's **user manual** for a
    stated "Factory Defaults" / default-configuration confirmation that the
    object is genuinely inert on creation, before it's added to the
    allow-list.
  - The CLI's own declared range is **not trusted as an upper bound** — on
    etx2i, `lag` advertised `[1..4]` but rejected 4 ("Invalid LAG ID"), and
    `test` (rfc2544) declared no range at all but only accepted 1-8. The
    harvester now tries up to 6 free indices ascending from the bottom of
    the declared range, and on every refusal captures the device's own
    error text (plus, for numeric attempts, one read-only `<name> <idx> ?`
    follow-up probe) — so a "not entered" gap always carries a
    device-confirmed reason (missing argument / license gate / no live
    instance), not a guess.
  - Full case study: `rad-mcp-server/tests/eval-report.md`.
- **Re-harvested** `etx2i`, `etx1p`, and `lab-sf1p` with the new logic.
  Device verified clean after every run (fresh-connection `get_config`
  grep for `zzz-hrvst` and every numeric index tried).
- **Knowledge-coverage eval harness** — checks the `rad-cli-operations`
  skill's harvested reference against 35 prompts a prior AI/tool ("RAD
  CLI") failed on, from a real spreadsheet test log
  (`ETX-2i_Show_Commands_enhanced.xlsx`). Zero device execution, pure
  reference lookup. New scripts: `build_eval_dataset.py`,
  `check_eval_coverage.py`, `build_results_md.py`, `build_results_html.py`.
  Results: `rad-mcp-server/tests/RESULTS.{md,html}`,
  `rad-mcp-server/tests/eval-report.md`.
- Docs updated: root `README.md`, `rad-mcp-server/README.md`,
  `rad-mcp-server/docs/architecture.md`, `rad-mcp-server/tests/README.md`.
- `.gitignore`: root-level `*.xlsx` (source test spreadsheets) and their
  Excel lock files.

## Open

### Device management
- [x] `rad-device-mng` tested for real (2026-07-10/11): skill loads on its
  trigger phrases (incl. "rad agent"), six-field intake gate enforced,
  `add_device` → `.env` → `test_connectivity` verified live — on Claude
  Code (Windows), Copilot CLI (Linux, fresh clone), and Claude CLI
  (Linux). Bonus fixes along the way: empty-inventory crash, missing-file
  auto-create, restart-free `.env` pickup.
- [ ] `update_device`/`remove_device` still untested outside code-level
  calls.
- [ ] Decide whether a slash command (e.g. `/rad-device`) is also wanted
  alongside the skill — currently skill-only (conversational trigger, no
  explicit command).

### Harvester / eval gaps (from the etx2i case study)
- [ ] Teach the harvester to supply a second argument for `pw` (`type
  <psn>`) and `twamp responder` (`[<number>] light [l2-probe]`) — currently
  refused at every index because only the first argument is supplied.
- [ ] `twamp controller`/`profile` are genuinely license-gated
  (device-confirmed `License required`) — not a code fix; needs an actual
  TWAMP license on the lab unit, or accept as permanently out of reach on
  this hardware.
- [ ] RFC2544's `test` has no dedicated manual chapter to directly confirm
  create-safety (unlike its y1564/L3SAT siblings) — currently allow-listed
  on architectural-similarity reasoning only.
- [ ] `NUMERIC_CREATE_ALLOW` is a flat, family-agnostic name set. Currently
  safe only because `crawl()` already gates all auto-create to paths
  starting with `"configure"` (confirmed via the `isakmp-policy` /
  `quick-setup vpn` collision this session) — but a future name collision
  might not be as lucky. Consider scoping by `(family, parent_context,
  name)` instead of bare name.
- [ ] Same manual-vetted numeric auto-create pass for `secflow`/`etx1p`'s
  own remaining gaps beyond what's already closed (`bridge`,
  `isakmp-policy`, `mirroring-session`, `ppp`, `tunnel-interface` are done —
  check for others via each family's `args-noenter` entries).

### New integration targets — ALL SIX VERIFIED LIVE (2026-07-11)
- [x] Full verification record (type/version/model per target):
  `docs/CONCEPTS.md` §8. Highlights per session:
  - **Copilot VS Code** 2026-07-10 (Windows, stdio + shared-http).
  - **Copilot CLI** 2026-07-11 (Linux, python3.11) — fresh-clone flow end
    to end; found: the CLI discovers `.mcp.json` in the launch directory
    (repo ships one with foreign paths → spawn failure until rewritten).
  - **Codex / ChatGPT desktop** 2026-07-11 — MCP via shared http; skill
    execution gate SKIPPED when the skill failed to load → behavioral
    caveat + `~/.codex/AGENTS.md` backstop documented in the guide.
  - **Claude Code CLI** 2026-07-11 (Linux) — user-home install
    (`-s user` + `~/.claude/skills` + `~/.claude/commands`), the "any
    project" usage shape, now the guide's primary route.
- [ ] `scripts/install/update-home-install.sh` — re-sync home-installed
  skills/commands after a repo update (copy-drift is the known cost of
  the home-install approach; hit once already on Windows).
- [ ] Ship `.mcp.json` as a portable-safe artifact (e.g. `.mcp.json.example`
  like the inventory, or document post-clone path editing) — the committed
  copy carries machine-specific absolute paths and breaks any other
  machine that launches Copilot CLI / Claude Code from the repo root.
- [ ] Linux install scripts (`scripts/install/*.sh`) — the PowerShell ones
  don't run there; the manual Linux flow is now documented in
  `copilot-cli.md`.
- [ ] **Verify the Codex guide live**: `~/.codex/config.toml` MCP entry +
  `~/.agents/skills/` on Codex CLI (native Windows is still experimental —
  test WSL2 fallback too, which needs Linux-side venv paths).
- [ ] Optional: mirror the `/rad-health`, `/rad-backup` slash commands as
  Copilot prompt files (`.github/prompts/*.prompt.md`) — skills cover the
  same ground conversationally, so low priority.

### Pre-existing roadmap (carried over, not from this session)
- [ ] `rad://cli-reference/{family}/{context}` keyed-lookup resource for
  Desktop.
- [ ] RADview northbound API backend alongside SSH (currently SSH/Netmiko
  only).
- [ ] Manuals RAG — semantic search/embeddings over the manual corpus.
  Lexical retrieval (layer 4) is done for all 3 families; this is the
  planned layer 6 in `docs/architecture.md`.
- [ ] `.mcpb` Desktop Extension format + Claude Code plugin marketplace
  listing.
