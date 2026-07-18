# SNMP support per family — manual + CLI-harvest evidence

Future semantic MIB compilation, prepared SQLite catalog, MCP lookup, and
poll-plan design are specified in
[snmp-mib-catalog-design.md](snmp-mib-catalog-design.md). This document remains
the record of current family evidence and observed live behavior.

Groundwork for the SNMP knowledge layer (device data fusion: CLI reference ↔
manual ↔ SNMP). Compiled 2026-07-16 from the ingested manuals
(`manual-<family>/`) cross-checked against the harvested CLI references
(`cli-reference-<family>.md`). **Documentation evidence only — no live SNMP
probe has been run yet**; treat "Versions" as what the manual claims, to be
verified per unit before relying on it. Source MIB files live in the workspace `MIBS/` and `MIBs2/` directories
(`MIBs2/` = the fuller, newer RAD kit — 288 files incl. legacy product MIBs;
module-level superset of `MIBS/`).

| Family | SNMP | Versions (per manual) | Model | CLI surface (harvested) | Evidence |
|---|---|---|---|---|---|
| `secflow` | ✅ yes | v1, v2c, **v3** | communities + USM/v3 framework | full `configure management snmp` context + `snmp-profile` (78 snmp lines) | manual ch. 6 (mgmt & security), 231 SNMP mentions, 36× SNMPv3 |
| `etx1p` | ✅ yes | v1, v2c, **v3** | same as secflow (manuals share structure) | full `configure management snmp` + `snmp-profile` (78 lines) | manual ch. 6, 210 mentions, 36× SNMPv3 |
| `etx2` | ✅ yes | v1, v2c, **v3** | USM/v3 framework: `notify`/`target`/`target-params` objects | full `configure management snmp` context (56 lines) | manual (feature ref. ch. 3), 302 mentions, 58× SNMPv3 |
| `mp4100` | ✅ yes | v1, v2c, **v3** | v3 framework incl. `snmp-engine-id` | `configure management snmp` context (25 lines) | manual ch. 6, 335 mentions, 66× SNMPv3 |
| `mp1` | ✅ yes | v1, v2c, **v3** | same v3 framework as etx2 (`notify NAME` etc.) | `configure management snmp` context (67 lines) | manual ch. 6, 201 mentions, 34× SNMPv3 |
| `minid` | ✅ yes — **v1/v2c ONLY** | v1, v2c (manual: communities "used for SNMPv1/v2"; **zero** v3 mentions) | flat community model: one command `snmp {community} {rw\|ronly\|trap} <name>` + `snmp-read-only` access toggle | single `snmp` leaf under `configure management` (10 lines — no v3 objects) | manual §3.8 (SNMP-based mgmt / RADview) + §6.7 (SNMP communities), 132 mentions |
| `etx2v` | ✅ yes (CLI evidence; manual silent) | *unverified* — its manual is hardware/BIOS-only (0 SNMP mentions); CLI shows the same v3-style framework as etx2 | USM/v3 framework per CLI (`notify NAME` etc.) | full `configure management snmp` context (74 lines) | CLI harvest only — **probe the live unit to confirm versions** |

## Key consequences for the SNMP layer design

- **mp4100**: answers **SNMPv1 only** with the factory-default `public`
  community (v2c/v3 GETs time out on marks-mp4 despite the manual's v3 claims
  — version support must be verified per unit, not assumed from docs). The
  client supports this via `RAD_MCP_<NAME>_SNMP_V1_COMMUNITY`.
- **minid**: community-based v1/v2c only — an SNMP backend must not assume v3.
  This is also the family where SNMP matters most (fragile SSH): stateless
  UDP reads sidestep the session-drop problem entirely.
- **etx2v**: the only family where the manual can't answer (HW/BIOS doc);
  version claims must come from a live probe (`sysObjectID`/`sysDescr` GET).
- All other families advertise v1/v2c/v3; org policy (ISO 27001) favors v3
  where available — verify per unit which is actually *enabled*.
- Every family's manual references RADview as the SNMP NMS; the `MIBS/` set
  is the RADview-style RAD private MIB collection.

## Live config state per lab unit (CLI `info` sweep, 2026-07-16 — read-only)

What each inventory unit actually has configured under its SNMP context
(`configure management snmp` → `info`; minid: `configure management` → `info`).
`info` shows non-default config — "baseline only" = factory engine-id/view,
nothing operator-configured.

| Unit | Family | SNMP config state | Pollable today? |
|---|---|---|---|
| minid-1 | minid | **fully configured v1/v2c**: `snmp community ronly public`, `rw private`, `trap public`; access lists permit snmp (static + loaned-ip `auto`); `no snmp-read-only` (SNMP writes allowed — we still never SET) | ✅ **VERIFIED LIVE 2026-07-16** — v2c `public` GET answered |
| etx2v-1 | etx2v | **active SNMPv3**: USM `security name "initial"` at `no-auth-no-priv` (enabled), trap target "RV" → udp 172.17.240.87 (a RADview station), `config-change-notification` + `bootstrap-notification` on, trap-sync-group 1 | ✅ **VERIFIED LIVE 2026-07-16** — v3 user `initial` no-auth GET answered |
| asafs-etx | etx1p | v1ro community chain configured 2026-07-16 | ✅ **VERIFIED LIVE** — v1 `public` |
| sf-163-187 | secflow | v1ro community chain configured 2026-07-16 | ✅ **VERIFIED LIVE** — v1 `public` |
| EliadSF-1p64 | secflow | v1ro community chain configured 2026-07-16 | ✅ **VERIFIED LIVE** — v1 `public` |
| ehud1p | etx1p | v1ro community chain configured 2026-07-16 | ✅ **VERIFIED LIVE** — v1 `public` |
| marks-mp4 | mp4100 | engine-id only in `info` — but a factory-default **v1 `public`** community answers | ✅ **VERIFIED LIVE 2026-07-16** — SNMPv1 `public` GET answered (v2c times out: **v1-only**) |
| Raviv-Etx | etx2 | v1ro community chain configured 2026-07-16 | ✅ **VERIFIED LIVE** — v1 `public` |
| mp-one | mp1 | v1ro chain configured 2026-07-16 (via discard-changes → configure → sanity-check → commit) | ✅ **VERIFIED LIVE** — v1 `public` |
| yossi-etx2 | etx2 | *not checked* — standing override: never execute on the ETX-2I; run the paste-ready block manually | ? |

Security note (lab): minid-1 carries the classic default communities
(`public`/`private`) with SNMP writes enabled (`no snmp-read-only`) — fine for
the lab, but `private`-rw is a well-known default; flag before any production
use. The toolkit's SNMP layer stays GET/WALK-only regardless.

## Live probe results (2026-07-16, pysnmp 7.1.27 GETs — read-only)

First end-to-end SNMP contact, MIB-II system group. **Enterprise 164 = RAD
Data Communications**; `sysObjectID` is a per-product identifier — the seed of
a sysObjectID → family auto-detect map for `add_device`.

| Unit | Auth used | sysDescr | sysObjectID | sysName |
|---|---|---|---|---|
| minid-1 | v2c community `public` | `MiNID Hw: 1.2, Sw: 2.6.0(0.28)` | `1.3.6.1.4.1.164.6.1.6.36` | MiNID |
| etx2v-1 | v3 USM `initial`, no-auth-no-priv | `uCPE-OS Hw: 1.0, Sw: 5.0.0.825` | `1.3.6.1.4.1.164.6.1.6.55` | uCPE-OS |
| marks-mp4 | **v1** community `public` | `MP-4100, HW: 0, SW: 4.91.70` | `1.3.6.1.4.1.164.6.1.3.120` | mp4100 |

sysObjectID → family map (grows as units are probed):

| sysObjectID (under 1.3.6.1.4.1.164) | family |
|---|---|
| `.6.1.6.36` | minid |
| `.6.1.6.55` | etx2v |
| `.6.1.6.68` | etx1p |
| `.6.1.6.79` | etx2 |
| `.6.1.10.7` | secflow |
| `.6.1.3.120` | mp4100 (`.6.1.3` = the older product sub-arc) |
| `.6.1.3.179` | mp1 |

**COMPLETE: all 7 families mapped, verified live 2026-07-16.** The v1
enablement (read-only community `public`, read-view `internet`, NO write-view)
was applied to the 6 quiet units via the staged flow with pre-change backups
(`server/backups/*-pre-snmpv1.cfg`); mp-one additionally proved the MP write
recipe: discard-changes → configure → sanity-check → commit → save.

Note: sysDescr gives the EXACT firmware (`2.6.0(0.28)`, `5.0.0.825`) — more
precise than the manual-derived versions, useful for reference-freshness
checks without an SSH session.

Tooling: `pysnmp` (7.x, asyncio API) installed in the server venv — a
tooling dependency like pymupdf; not yet in pyproject extras.

## SNMP knowledge artifacts (this directory)

The OID map is **portfolio-wide**: it names objects for ALL families (legacy
sets included), independent of whether a given unit has SNMP enabled today —
the moment a unit's SNMP is configured, probes/walks render symbolically with
no further work. Both snmp-map files were re-rendered 2026-07-16 with the
union map (etx2v's RAD arc sharpened from 323 to 403 distinct object groups
on identical walk data).

| File | Contents |
|---|---|
| `snmp-oid-map.json` | Flat `{oid: MODULE::name}` map — **35,977 objects** compiled (pysmi 2.0) from the `MIBS/` + `MIBs2/` **union** (330 modules incl. web-pulled standard imports). `MIBs2/` (288 files, 19 MB) is a module-level SUPERSET of `MIBS/` with newer/larger revisions (e.g. RadGen 380→699 KB), so its copy wins every overlap; only RFC-1212/RFC-1215 failed (SMIv1 macro modules, no OIDs) and 2 third-party Channelot MIBs were skipped. Notably resolves RAD product identities (`sysObjectID .36 = RAD-GEN-MIB::radMiNID`) and the agent-silence spot (`entPhysicalSerialNum.1001`) |
| `snmp-map-minid.md` | Live walk of minid-1 (v2c): mib-2 53 objs + RAD arc 31. **Sparse-NEXT agent** — poll by explicit OID, not discovery walks (see the file's caveat) |
| `snmp-map-etx2v.md` | Live walk of etx2v-1 (v3): mib-2 1,156 objs (236 groups) + **RAD arc 3,753 objs (323 groups, complete)** — includes RAD-GEN-MIB's 258-entry alarm dictionary (`alarmEventAttrName/Description/DefaultSeverity`), SNMP-readable alarm semantics |

Agent lessons (verified live 2026-07-16, both units):
- **Use GETNEXT, not GETBULK** — the minid agent's GETBULK jumps arcs and
  mis-orders; both agents answer GETNEXT correctly.
- **minid answers unknown OIDs with `tooBig`** instead of noSuchInstance
  (observed live 2026-07-18 on GETs for nonexistent instances) — treat a
  `tooBig` from minid as "object not implemented", not as a message-size issue.
- **End-of-view = silence, not endOfMibView** — BOTH agents stop responding
  at the same spot (ENTITY-MIB `entPhysical*.1001`) instead of answering;
  treat a mid-walk timeout after a pause-retry as end-of-view, not an outage.

## Next steps

1. ~~sysObjectID/sysDescr probe~~ — DONE (two green units).
2. ~~Compile `MIBS/` → symbolic OID map~~ — DONE (`snmp-oid-map.json`).
3. ~~Harvest `snmp-map-<family>.md` for the verified units~~ — DONE
   (minid, etx2v). Repeat per unit as SNMP gets enabled on the others.
4. ~~`backends/snmp.py` + read-only tool surface~~ — DONE (server 0.2.0):
   `snmp_probe` (identity + family hint), `snmp_get` (explicit OIDs — the
   minid path), `snmp_walk` (capped GETNEXT, silence-tolerant). Env creds:
   `RAD_MCP_<NAME>_SNMP_COMMUNITY` / `_SNMP_V3_USER`. Never SET.
5. Fusion cross-links: alarm dictionary ↔ manual alarm chapters ↔
   `configure reporting`; IF-MIB rows ↔ `configure port`.
