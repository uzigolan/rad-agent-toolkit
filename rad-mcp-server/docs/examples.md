# Example prompts — what to ask, exactly as you'd type it

Ready-to-paste prompts across the six usage categories, each addressed to
one of the agent's trigger names — **"rad agent"** (generic), **"abayev"** or
**"noam"** (the CLI-expert personas; same rules, personal sign-off). Every
device action still passes the safety flow: reads wait for your "run it now?"
confirmation, writes go backup → preview → **your explicit approval** →
commit → verify. Unit names below are the lab inventory — substitute yours.

## 1. Device management

**1.1 Add a device**
> rad agent, add my device: name lab-etx2, host 172.17.163.205, family etx2, group lab, user su, password 1234

The intake gate requires all six facts before anything is written; facts go
to `inventory.yaml`, credentials only to `server/.env`. If you omit a field,
the agent asks for all missing ones in a single question.

**1.2 List devices**
> noam, show the list of devices

Credential-free summaries (name/host/family/groups); filterable: *"noam,
list only the mp1 family"*.

**1.3 Change a device**
> abayev, marks-mp4 moved — update its host to 172.17.161.95

Partial update: only the named field changes. Changing `family` is treated
as suspicious (usually a mis-registration) and asked back.

**1.4 Remove a device**
> rad agent, remove lab-etx2 from the list

Requires explicit confirmation; only forgets the inventory entry — never
touches the device, its backups, or its audit history.

## 2. CLI operations

**2.1 Active alarms**
> abayev, show the active alarms on sf-163-187

Navigates `configure reporting` → `show active-alarms` and interprets
severity (a major/critical alarm blocks config work by policy).

**2.2 Ports status**
> noam, show the ports status on ehud1p

`configure port` → `show summary`. Port naming is family-specific (secflow
`ethernet 3`, etx1p `ethernet lan1`, etx2 `ethernet 0/2`) — the agent uses
the target family's convention.

**2.3 Suggest a certificate + MQTT server configuration**
> rad agent, suggest the CLI configuration for a device certificate and an MQTTS server on the ETX-1p

Answered from the harvested reference + manual with **no device contact**:
key generation (⚠ the ETX-1p holds max ONE key pair — stated up front),
self-signed or CA-enrolled certificate, and the MQTT server binding
(`certificate <name> trusted-ca <ca>` — the trusted-ca is required).

**2.4 Change configuration on a device**
> abayev, change the location of sf-163-187 to "TLV lab rack 3"

The staged flow: backup → `stage_config` preview → your explicit approval →
commit → verify. On **mp1/mp4100** the mandatory MP recipe applies and is
server-enforced: `discard-changes` → configure → `sanity-check` → `commit` →
`save`.

**2.5 Download (back up) configuration**
> noam, back up the configuration of minid-1 and diff it against the previous backup

Full `info` export to the local archive (`server/backups/`), with diffs
against any earlier snapshot.

## 3. SNMP operations

SNMP tools are read-only. As with CLI reads, the agent shows the exact live
action and waits for confirmation before contacting the device.

**3.1 Probe device identity**
> rad agent, check SNMP on etx2v-1 and report its exact firmware, sysObjectID, and detected family

Uses `snmp_probe` to read the MIB-II system identity and compare the returned
`sysObjectID` with the toolkit's family map. This is a quick way to confirm
device identity and firmware without opening an SSH session.

**3.2 Read exact OIDs**
> noam, read sysName, sysLocation, and sysUpTime from minid-1 using exact SNMP GETs

Uses `snmp_get` with symbolic names resolved through the portfolio OID map.
Exact GETs are preferred on MiNID because its sparse GETNEXT chain can
under-report objects during discovery walks.

**3.3 Walk an SNMP table**
> abayev, walk IF-MIB on etx2v-1, cap it at 100 rows, and summarize interface status and error counters

Uses the row-capped `snmp_walk` GETNEXT path, then turns the returned IF-MIB
rows into an operator-friendly summary. The toolkit never performs SNMP SET.

**3.4 Rich MIB catalog — the two "gold-standard" prompts**

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

## 4. Network engineering

**4.1 Inquire about a topic**
> rad agent, how does zero-touch provisioning work on the MiNID, and what are its limits?

Concept questions come from the ingested manual (per-chapter markdown +
cross-links), syntax from the CLI reference — cited per layer.

**4.2 Design: 3 × ETX-2 ring with ERP**
> abayev, I have three ETX-2 units in a ring running ERP — give me the configuration for all three

Grounded in the etx2 reference (`configure protection erp`) + manual chapter:
ring-port roles, RPL owner/neighbor placement, per-unit paste-ready blocks,
and the verification reads (`show erp status`) — staged per unit only after
your approval.

**4.3 Observability (not just monitoring) for QA on 2 × MP-1**
> noam, suggest a way for QA to monitor our two MP-1 units and produce a report that gives observability, not just monitoring

Combines the layers: SNMPv1 polling (sysDescr/IF-MIB counters — stateless,
scriptable), the SNMP alarm dictionary + `show active-alarms` for events,
config-drift detection via scheduled `backup_config` diffs, and
`health_check` sweeps — i.e. state + events + trends + drift, with meanings
from the manual, not just up/down pings.

## 5. Advanced

**5.1 Compare two device types on a topic**
> rad agent, compare the ETX-2 and the ETX-2V on QoS capabilities

Capability grounding rule: each family answers ONLY from its own harvested
reference + manual — no cross-family inference. Differences arrive as a
table with the evidence (context paths / manual sections) per side.

**5.2 Propose a CLI feature based on another family's implementation**
> abayev, the MiNID has no TWAMP responder like the ETX-2 does — draft a feature proposal for adding it to the MiNID CLI, modeled on the ETX-2 implementation

Cross-family reference diff: the ETX-2's harvested `configure oam twamp`
tree becomes the model; the proposal maps it onto MiNID's compact context
set with what exists / what's missing / suggested syntax.

**5.3 Compare competitive devices to RAD ones**
> noam, compare a competitor's carrier-Ethernet demarcation device against the RAD ETX-2 for an ERP-based rollout

RAD's side is grounded in harvested references + manuals; the competitor's
side needs public sources (web/datasheets) — the agent says plainly which
claims are verified from our knowledge base and which are external.

## 6. Onboarding a new device type

**6.1 Harvest its CLI**
> rad agent, harvest the CLI of the new device I just added

`/rad-harvest <device>`: probe first (prompt + dialect + SSH behavior),
then the full `?`-help crawl → `cli-reference-<family>.md` + command tree.
Fragile-SSH units go branch-by-branch; temp objects are rolled back and the
device is verified clean afterwards.

**6.2 Ingest its user manual**
> noam, here is the user manual PDF for the new family — ingest it

Drop the PDF in `manuals/`, then `/rad-load-manual <pdf> <family>`:
per-chapter markdown + CLI-topic cross-links. The PDF stays gitignored;
the extracted markdown is the committed knowledge.

**6.3 Add its MIBs**
> abayev, here are the MIB files for the new family — add them to the SNMP layer

Drop them in the workspace MIB directory and recompile
`snmp-oid-map.json` (the map is portfolio-wide); then one `snmp_probe`
captures the family's `sysObjectID` for the auto-detect map and a capped
walk produces its `snmp-map-<family>.md` capability map.
