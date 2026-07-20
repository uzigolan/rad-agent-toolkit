# Example prompts — what to ask, exactly as you'd type it

Ready-to-paste prompts across the nine usage categories — knowledge-first
(user manual, datasheets), then device work, and a closing **fusion** set
that spans every layer in one prompt — each addressed to
one of the agent's trigger names — **"rad agent"** (generic), **"abayev"** or
**"noam"** (the CLI-expert personas; same rules, personal sign-off). Every
device action still passes the safety flow: reads wait for your "run it now?"
confirmation, writes go backup → preview → **your explicit approval** →
commit → verify. Unit names below are the lab inventory — substitute yours.

## Contents

1. [User manual — feature & concept knowledge](#1-user-manual--feature--concept-knowledge)
2. [Datasheets — hardware & product knowledge](#2-datasheets--hardware--product-knowledge)
3. [Device management](#3-device-management)
4. [CLI operations](#4-cli-operations)
5. [SNMP operations](#5-snmp-operations)
6. [Network engineering](#6-network-engineering)
7. [Advanced](#7-advanced)
8. [Onboarding a new device type](#8-onboarding-a-new-device-type)
9. [Fusion — every layer in one prompt](#9-fusion--every-layer-in-one-prompt)

## 1. User manual — feature & concept knowledge

"How does it work?" questions are answered offline from each family's
ingested user manual (per-chapter markdown + CLI-topic cross-links):
concepts from the manual, matching syntax from the harvested CLI
reference — cited per layer, with no device contact.

**1.1 Inquire about a topic**
> rad agent, how does zero-touch provisioning work on the MiNID, and what are its limits?

Concept questions come from the ingested manual (per-chapter markdown +
cross-links), syntax from the CLI reference — cited per layer.

**1.2 Understand a mechanism in depth**
> noam, according to the ETX-2 manual, what happens on an ERP ring when a link fails — which timers are involved, and is the recovery revertive?

Answered from the manual's protection chapter, with the matching
`configure protection erp` verbs cited from the harvested reference — a
design-grade explanation, not a generic textbook answer.

## 2. Datasheets — hardware & product knowledge

Specs, interfaces, variants and ordering come from the **datasheet layer**
(39 products: every family's system datasheets + the Megaplex-4 card set),
answered offline via `datasheet_search` / `references/datasheets/`. `kind`
matters in every answer: `system` is a standalone device, `card` is a
plug-in module for its family's chassis, `accessory` is non-traffic
hardware.

**2.1 Pick the right card**
> noam, which Megaplex-4 card gives me 16 E1 ports, and what are its ordering options?

The M16E1/M16T1 card's interface specs and its RECOMMENDED CONFIGURATIONS
ordering block — and because its `kind` is `card`, the answer says it plugs
into a Megaplex-4 chassis (configuration happens on the `mp4100` CLI).

**2.2 Compare product variants**
> rad agent, how do the ETX-2i 10G and 100G variants differ — ports, timing, ordering?

Side-by-side from the two variants' datasheet sections (INTERFACES, TIMING
AND SYNCHRONIZATION, ORDERING OPTIONS) — same family (`etx2`), so the CLI
reference applies to both; only the hardware differs.

**2.3 Spec lookup on one product**
> abayev, what is the operating temperature range and power options of the SecFlow-1p?

A bounded read of the `secflow-1p` sheet's ENVIRONMENTAL/PHYSICAL sections —
cited with the section and page, no device contact and no web search.

**2.4 Ingest new or updated datasheets**
> rad agent, here are the datasheet PDFs for the new family — add them to the knowledge

Drop the PDFs in `datasheets/`, add each one's entry to
`references/datasheet-map.yaml` (product slug, family, `kind` —
system/card/accessory, read off the sheet's own first-page banner), then
`/rad-load-datasheet --all`. Specs, variants and ordering become searchable
per subject section; PDFs stay gitignored.

## 3. Device management

**3.1 Add a device**
> rad agent, add my device: name lab-etx2, host 172.17.163.205, family etx2, group lab, user su, password 1234

The intake gate requires all six facts before anything is written; facts go
to `inventory.yaml`, credentials only to `server/.env`. If you omit a field,
the agent asks for all missing ones in a single question.

**3.2 List devices**
> noam, show the list of devices

Credential-free summaries (name/host/family/groups); filterable: *"noam,
list only the mp1 family"*.

**3.3 Change a device**
> abayev, marks-mp4 moved — update its host to 172.17.161.95

Partial update: only the named field changes. Changing `family` is treated
as suspicious (usually a mis-registration) and asked back.

**3.4 Remove a device**
> rad agent, remove lab-etx2 from the list

Requires explicit confirmation; only forgets the inventory entry — never
touches the device, its backups, or its audit history.

## 4. CLI operations

**4.1 Active alarms**
> abayev, show the active alarms on sf-163-187

Navigates `configure reporting` → `show active-alarms` and interprets
severity (a major/critical alarm blocks config work by policy).

**4.2 Ports status**
> noam, show the ports status on ehud1p

`configure port` → `show summary`. Port naming is family-specific (secflow
`ethernet 3`, etx1p `ethernet lan1`, etx2 `ethernet 0/2`) — the agent uses
the target family's convention.

**4.3 Suggest a certificate + MQTT server configuration**
> rad agent, suggest the CLI configuration for a device certificate and an MQTTS server on the ETX-1p

Answered from the harvested reference + manual with **no device contact**:
key generation (⚠ the ETX-1p holds max ONE key pair — stated up front),
self-signed or CA-enrolled certificate, and the MQTT server binding
(`certificate <name> trusted-ca <ca>` — the trusted-ca is required).

**4.4 Change configuration on a device**
> abayev, change the location of sf-163-187 to "TLV lab rack 3"

The staged flow: backup → `stage_config` preview → your explicit approval →
commit → verify. On **mp1/mp4100** the mandatory MP recipe applies and is
server-enforced: `discard-changes` → configure → `sanity-check` → `commit` →
`save`.

**4.5 Download (back up) configuration**
> noam, back up the configuration of minid-1 and diff it against the previous backup

Full `info` export to the local archive (`server/backups/`), with diffs
against any earlier snapshot.

## 5. SNMP operations

SNMP tools are read-only. As with CLI reads, the agent shows the exact live
action and waits for confirmation before contacting the device.

**5.1 Probe device identity**
> rad agent, check SNMP on etx2v-1 and report its exact firmware, sysObjectID, and detected family

Uses `snmp_probe` to read the MIB-II system identity and compare the returned
`sysObjectID` with the toolkit's family map. This is a quick way to confirm
device identity and firmware without opening an SSH session.

**5.2 Read exact OIDs**
> noam, read sysName, sysLocation, and sysUpTime from minid-1 using exact SNMP GETs

Uses `snmp_get` with symbolic names resolved through the portfolio OID map.
Exact GETs are preferred on MiNID because its sparse GETNEXT chain can
under-report objects during discovery walks.

**5.3 Walk an SNMP table**
> abayev, walk IF-MIB on etx2v-1, cap it at 100 rows, and summarize interface status and error counters

Uses the row-capped `snmp_walk` GETNEXT path, then turns the returned IF-MIB
rows into an operator-friendly summary. The toolkit never performs SNMP SET.

**5.4 Rich MIB catalog — the two "gold-standard" prompts**

These ask for **RAD-proprietary** MIB content no general model has memorized, so
a correct, detailed answer can *only* come from the MCP knowledge catalog
(`mib_search` / `mib_describe` over `rad-knowledge.sqlite`) — they're the way to
prove the catalog is really being used, in either bundled or served mode.

> rad agent, describe RAD-EthIf-MIB::erpNodeState — give the exact OID, syntax, enum values, description, and source provenance

> rad agent, search the MIB catalog for RAD-proprietary ATM objects and describe one with its full definition

A real answer returns the enterprise OID (`1.3.6.1.4.1.164.*`), enum values,
table context, and a source `sha256` — none of which is guessable. To *verify*
the catalog served it (not training memory), tail `server/logs/audit.jsonl`:
each call logs a `mib_search` / `mib_describe` line. A thin, name-only reply
means the MCP server isn't connected and it fell back to the static OID map.

## 6. Network engineering

**6.1 Design: 3 × ETX-2 ring with ERP**
> abayev, I have three ETX-2 units in a ring running ERP — give me the configuration for all three

Grounded in the etx2 reference (`configure protection erp`) + manual chapter:
ring-port roles, RPL owner/neighbor placement, per-unit paste-ready blocks,
and the verification reads (`show erp status`) — staged per unit only after
your approval.

**6.2 Observability (not just monitoring) for QA on 2 × MP-1**
> noam, suggest a way for QA to monitor our two MP-1 units and produce a report that gives observability, not just monitoring

Combines the layers: SNMPv1 polling (sysDescr/IF-MIB counters — stateless,
scriptable), the SNMP alarm dictionary + `show active-alarms` for events,
config-drift detection via scheduled `backup_config` diffs, and
`health_check` sweeps — i.e. state + events + trends + drift, with meanings
from the manual, not just up/down pings.

## 7. Advanced

**7.1 Compare two device types on a topic**
> rad agent, compare the ETX-2 and the ETX-2V on QoS capabilities

Capability grounding rule: each family answers ONLY from its own harvested
reference + manual — no cross-family inference. Differences arrive as a
table with the evidence (context paths / manual sections) per side.

**7.2 Propose a CLI feature based on another family's implementation**
> abayev, the MiNID has no TWAMP responder like the ETX-2 does — draft a feature proposal for adding it to the MiNID CLI, modeled on the ETX-2 implementation

Cross-family reference diff: the ETX-2's harvested `configure oam twamp`
tree becomes the model; the proposal maps it onto MiNID's compact context
set with what exists / what's missing / suggested syntax.

**7.3 Compare competitive devices to RAD ones**
> noam, compare a competitor's carrier-Ethernet demarcation device against the RAD ETX-2 for an ERP-based rollout

RAD's side is grounded in harvested references + manuals; the competitor's
side needs public sources (web/datasheets) — the agent says plainly which
claims are verified from our knowledge base and which are external.

## 8. Onboarding a new device type

**8.1 Harvest its CLI**
> rad agent, harvest the CLI of the new device I just added

`/rad-harvest <device>`: probe first (prompt + dialect + SSH behavior),
then the full `?`-help crawl → `cli-reference-<family>.md` + command tree.
Fragile-SSH units go branch-by-branch; temp objects are rolled back and the
device is verified clean afterwards.

**8.2 Ingest its user manual**
> noam, here is the user manual PDF for the new family — ingest it

Drop the PDF in `manuals/`, then `/rad-load-manual <pdf> <family>`:
per-chapter markdown + CLI-topic cross-links. The PDF stays gitignored;
the extracted markdown is the committed knowledge.

**8.3 Add its MIBs**
> abayev, here are the MIB files for the new family — add them to the SNMP layer

Drop them in the workspace MIB directory and recompile
`snmp-oid-map.json` (the map is portfolio-wide); then one `snmp_probe`
captures the family's `sysObjectID` for the auto-detect map and a capped
walk produces its `snmp-map-<family>.md` capability map.

## 9. Fusion — every layer in one prompt

Capstone prompts that deliberately span the whole toolkit — datasheets,
manual knowledge, inventory, CLI, SNMP, and backups — in a single request.
Each step still passes the same safety flow: reads wait for your
confirmation, writes go backup → preview → approval → commit → verify.

**9.1 Commission a new unit, zero to managed**
> rad agent, we just unboxed a SecFlow-1p — confirm its power and temperature specs from the datasheet, add it to the inventory as sf-new at 172.17.163.200 (family secflow, group lab, user su, password 1234), run a health check, verify its identity over SNMP, and set its location to "OT cabinet 2"

One prompt, every layer in order: datasheet lookup (offline) → the six-fact
intake gate → `health_check` → `snmp_probe` identity cross-check → the
staged config flow for the location write.

**9.2 Full-stack status report**
> noam, give me a full status report on marks-mp4 — what its active alarms mean per the manual, port status from the CLI, IF-MIB error counters over SNMP, and whether the config drifted since the last backup

Fuses events (`show active-alarms` + the manual's alarm meanings), live
state (CLI port reads), trends (SNMP counters), and drift (backup diff)
into one operator-grade report.

**9.3 From datasheet to running ring**
> abayev, we're rolling out a 3-unit ETX-2 ERP ring — pick the right ETX-2i variant from the datasheets, design the ring from the manual and CLI reference, stage the configuration for each unit, and after I approve verify the ring by CLI and SNMP

Hardware selection (datasheet variants/ordering) → grounded design (manual
chapter + `configure protection erp` reference) → per-unit staged commits,
each with your explicit approval → post-commit verification via
`show erp status` and an IF-MIB walk.
