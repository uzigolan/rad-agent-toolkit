---
description: Onboard a brand-new RAD device FAMILY end-to-end (driver → probe → CLI harvest → manual → MIBs/catalog → registration → docs). Orchestrates the pipeline skills — it CALLS /rad-harvest and /rad-load-manual, never replaces them. Also use when addressed via "abayev" / "noam" / "rad agent" — e.g. "rad agent, onboard a new device family minid at 172.17.166.55"
argument-hint: <family> <device-name> <host> [notes: manual PDF path, MIB files, SSH quirks]
---

Onboard a new RAD device family: $ARGUMENTS

## ⛔ PREREQUISITES — onboarding cannot run without both

1. **A reachable, live device of the new family** — the probe (dialect/SSH)
   and the CLI harvest read the real unit; there is no offline substitute.
   Confirm you have its host + credentials before starting.
2. **The family's user-manual PDF** — the concept layer (limits, alarm
   meanings, procedures) comes from it; drop it in `manuals/`.

If either is missing, STOP and ask the user for it — do not attempt a
partial onboarding. (MIB files are recommended but optional; without them the
SNMP semantic layer for the family is just thinner.)

This is the ONE-TIME per-family conductor. Each knowledge pipeline it invokes
stays independently runnable for its own lifetime trigger (firmware upgrade →
`/rad-harvest` alone; manual revision → `/rad-load-manual` alone; new MIB kit
→ catalog rebuild alone) — this command composes them, it does not own them.
Distilled from the minid + etx2v onboardings (2026-07-15..18).

## A. Unit + driver (code change — human-reviewed)

1. **Intake gate** (via the `rad-device-mng` skill rules): all six facts —
   name, host, family, group, username, password. Facts → `inventory.yaml`
   (both trees if the deployed toolkit tree is in play); credentials →
   `server/.env` only (`RAD_MCP_<NAME>_USERNAME/_PASSWORD`), append-only.
2. **Driver scaffold**: new `server/rad_mcp/drivers/<family>.py` on
   `RadCliDriver` with an honest "NOT YET VERIFIED LIVE — starting
   assumption" docstring + register in `drivers/__init__.py`. If the user
   flagged fragile/slow SSH, ship the patient connect profile
   (`ssh_connect_options`, `connect_attempts`, `connect_backoff` — copy the
   minid pattern). Verify both trees import the registry.
3. **PROBE BEFORE HARVEST** (read-only, cheap, corrects assumptions early):

   ```
   rad-mcp-server\server\.venv\Scripts\python.exe rad-mcp-server\scripts\harvest_cli.py probe <device>
   ```

   From the probe decide, and record in the driver docstring:
   - prompt + dialect: shared context CLI? If navigation/`exit all`/`info`
     misbehave, STOP — a genuinely different dialect needs its own driver
     base, not a forced onboarding.
   - **candidate-DB model?** If root help shows `commit` /
     `discard-changes` / `sanity-check` globals → the family follows the
     mandatory MP write recipe (discard-changes → configure → sanity-check →
     commit → save; `stage_config` enforces it — add the family to that
     check in `server.py`).
   - SSH behavior: drops, pagers (`--More--` vs bare `more...`), pacing.

## B. Knowledge pipelines (each is its own skill — call them)

4. **CLI reference** → run **`/rad-harvest <device>`** and follow THAT
   skill's review steps (diff, temp-object rollbacks, device-clean check).
   Fragile-SSH family → branch-by-branch (`--branch` per subtree, small→big,
   `--tree-cache` to capture the tree once); a full run on a fragile link
   WILL drop mid-crawl.
5. **Manual** → drop the PDF in `manuals/` and run
   **`/rad-load-manual <pdf> <family>`**; follow that skill's quality checks
   (chapter completeness, cross-links, no mojibake).
5b. **Datasheet(s)** → drop the family's datasheet PDF(s) in `datasheets/`,
   add an entry per PDF to `references/datasheet-map.yaml` (product slug,
   family, `kind` system/card/accessory — read the sheet's own first-page
   banner, don't trust filenames), then run **`/rad-load-datasheet`**;
   follow that skill's quality checks (index completeness, clean `##`
   subject headings, no mojibake).
6. **MIBs + SNMP registration**:
   - Copy any family-specific MIB files into the workspace MIB set
     (`MIBs2/`; sources stay gitignored).
   - If the unit answers SNMP (or after enabling it — see snmp-support.md's
     v1ro recipe), `snmp_probe` it and add the family block to
     **`references/family-profiles.yaml`** (sysObjectID, versions_verified
     vs claimed, credential model, read strategy, quirks). That yaml is the
     SINGLE SOURCE — no code change; snmp.py and the catalog build both
     read it. Add the unit's `RAD_MCP_<NAME>_SNMP_*` key to `server/.env`.
    - **Coverage gate for all families (mandatory):** after adding the new
       family, run the coverage checker and fix any gaps before proceeding:

    ```
    rad-mcp-server\server\.venv\Scripts\python.exe rad-mcp-server\scripts\check_snmp_support_coverage.py
    ```

    The command must return `SNMP support coverage check: OK`.
7. **Catalog rebuild** (folds steps 4-6 into the served-mode database):

   ```
   rad-mcp-server\server\.venv\Scripts\python.exe rad-mcp-server\scripts\build_knowledge_catalog.py --mib-root "MIBs2:priority=200" --mib-root "MIBS:priority=100" --apply-compat
   ```

   Must end `OK` with fixtures passing (Phase 5 gates: the new family needs
   BOTH cli_help rows and manual sections). Review the report's compat diff.

## C. Registration + coverage (the part no pipeline skill covers)

8. Update every family-enumeration site — grep for an existing family name
   (e.g. `mp1`) to find them all; the known set: `README.md` (family table
   incl. Version column + intro line), `docs/VERSIONS.md` (driver row),
   `docs/architecture.md` (driver tree), `skills/rad-core/SKILL.md` (family
   bullet), `skills/rad-cli-operations/SKILL.md` (**description frontmatter
   — routing breaks without it** — plus the family-notes paragraph; bump the
   skill version), `references/verified-commands.md` (the not-covered-by-
   `all` note), `references/snmp-support.md` (family row + live table).
9. Driver docstring: replace the starting-assumption note with VERIFIED
   facts (prompt, SW, contexts from the live tree, SSH profile, write model).

## D. Delivery

10. Mirror to the deployed toolkit tree (drivers, references, docs, catalog
    DB) + sync the home/workspace skill copies; the served HTTP server needs
    a restart to load new code.
11. Nothing is committed unless the user explicitly says so. When they do:
    ONE commit for the family (drivers + references + docs; PDFs and MIB
    sources stay gitignored, `build/` stays gitignored except the report).

Safety notes: probe and harvest are read-only except the harvester's
short-lived temp objects (rolled back + device-clean verified by the
/rad-harvest flow). Never navigate `admin`/`file` danger contexts. All the
usual gates apply — this command adds orchestration, not exemptions.
