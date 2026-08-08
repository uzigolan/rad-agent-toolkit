"""knowledge group — offline searches over the knowledge catalog.

Phase 3/5 of references/snmp-mib-catalog-design.md: OFFLINE tools over the
read-only rad-knowledge.sqlite semantic catalog. They never contact a device
(no confirmation gate needed) and are available to RO and RW tokens alike.
MIB-DEFINED != device-implemented — answers carry capability evidence
separately. Future home: the rad-knowledge server (plan 09); collapsed to a
2-tool facade in plan 03.
"""
from __future__ import annotations

from ..audit import audit
from ..runtime import _kcall, _knowledge


def register_knowledge_tools(mcp) -> None:
    """Register the 10 offline knowledge-search tools."""

    @mcp.tool()
    def mib_search(query: str, module: str = "", kind: str = "", oid_prefix: str = "",
                   family: str = "", limit: int = 25) -> dict:
        """Search the semantic MIB catalog (offline) by concept, symbol, or OID.
        Deterministic ranking: exact > prefix/OID-subtree > full-text (descriptions
        + enum labels). Optional filters: module, kind (scalar/table/row/column/
        notification), oid_prefix; family adds that family's verified transport
        profile to the answer. Results are MIB-defined objects — NOT proof a
        family implements them."""
        k = _knowledge()
        out = _kcall(k.search, query, module=module, kind=kind,
                     oid_prefix=oid_prefix, family=family, limit=limit)
        audit("mib_search", "-", detail=query[:80])
        return out

    @mcp.tool()
    def mib_describe(ref: str) -> dict:
        """Full semantic definition of one MIB object (offline) by symbol,
        MODULE::symbol, or numeric OID: syntax + textual convention + display
        hint, access, description, enums, ranges, units, default, table/index
        context, augments, notification payload, module revision, source
        provenance (file + sha256), and live capability evidence when any exists."""
        k = _knowledge()
        out = _kcall(k.describe, ref)
        audit("mib_describe", "-", detail=ref[:80])
        return out

    @mcp.tool()
    def mib_table(ref: str) -> dict:
        """Complete table model (offline) for a table/row/column reference:
        table+entry OIDs, ordered indexes (with types and IMPLIED flags),
        instance-encoding rule, every column with access/type/units/enums, and
        suggested identifying columns — everything needed to plan a poll."""
        k = _knowledge()
        out = _kcall(k.table_model, ref)
        audit("mib_table", "-", detail=ref[:80])
        return out

    @mcp.tool()
    def mib_notifications(query: str, module: str = "", limit: int = 20) -> dict:
        """Find notifications/traps in the catalog (offline) by concept, with each
        notification's ordered payload objects."""
        k = _knowledge()
        out = _kcall(k.notifications, query, module=module, limit=limit)
        audit("mib_notifications", "-", detail=query[:80])
        return out

    @mcp.tool()
    def cli_search(query: str, family: str = "", context: str = "", limit: int = 15) -> dict:
        """Search the harvested CLI `?`-help knowledge (offline, Phase 5 — the
        served-mode equivalent of grepping cli-reference-<family>.md). Ranking:
        exact context/prefix > context prefix > full-text over help bodies.
        ALWAYS pass `family` when known — commands are family-specific."""
        k = _knowledge()
        out = _kcall(k.cli_search, query, family=family, context=context, limit=limit)
        audit("cli_search", "-", detail=f"{family}:{query[:60]}")
        return out

    @mcp.tool()
    def manual_search(query: str, family: str = "", limit: int = 10,
                      include_refdocs: bool = True) -> dict:
        """Search the ingested user manuals per-section (offline, Phase 5 — the
        served-mode equivalent of grepping manual-<family>/). Returns bounded
        excerpts with chapter/section/page provenance; optionally also searches
        the curated reference docs (verified-commands, snmp-support,
        known-limitations, snmp capability maps). Concepts/limits live here —
        exact syntax comes from cli_search."""
        k = _knowledge()
        out = _kcall(k.manual_search, query, family=family, limit=limit,
                     include_refdocs=include_refdocs)
        audit("manual_search", "-", detail=f"{family}:{query[:60]}")
        return out

    @mcp.tool()
    def datasheet_search(query: str, family: str = "", product: str = "",
                         kind: str = "", limit: int = 10) -> dict:
        """Search the ingested product datasheets per subject section (offline —
        the served-mode equivalent of grepping references/datasheets/). Third
        knowledge domain: hardware specs, interfaces, timing options, ordering and
        product variants live HERE; concepts/procedures in manual_search; exact
        command syntax in cli_search. Results carry `kind`: 'system' is a
        standalone device, 'card' a plug-in module for its family's chassis (e.g.
        every mp4100 card), 'accessory' non-traffic hardware. Filter by `family`
        (inventory family), `product` (datasheet slug, see rad://datasheet), or
        `kind`."""
        k = _knowledge()
        out = _kcall(k.datasheet_search, query, family=family, product=product,
                     kind=kind, limit=limit)
        audit("datasheet_search", "-", detail=f"{family or product or '*'}:{query[:60]}")
        return out

    @mcp.tool()
    def mea_search(query: str = "", device: str = "", version: str = "",
                   map_type: str = "", limit: int = 25) -> dict:
        """Search ingested FPGA MEA memory-map artifacts (offline).

        Source: skills/rad-cli-operations/references/fpga-mea/raw/*.json produced
        by scripts/ingest_mea.py. Matches across register addresses/names and
        parsed table rows. Optional filters: device, version, map_type.
        """
        k = _knowledge()
        out = _kcall(k.mea_search, query, device=device, version=version,
                     map_type=map_type, limit=limit)
        scope = f"{device or '*'}:{version or '*'}:{map_type or '*'}"
        audit("mea_search", "-", detail=f"{scope}:{(query or '')[:60]}")
        return out

    @mcp.tool()
    def mea_commands_search(query: str = "", category: str = "", limit: int = 100) -> dict:
        """Search the stored MEA command-catalog text (offline).

        Use this for questions like "list all MEA commands" or command-family
        lookups (`MEA util fctl`, `MEA oam`, etc.). This is distinct from:
            - debug_tree_history: session-captured menu/shell history
            - mea_search: register/memory-map artifacts
        """
        k = _knowledge()
        out = _kcall(k.mea_commands_search, query, category=category, limit=limit)
        scope = category or "*"
        audit("mea_commands_search", "-", detail=f"{scope}:{(query or '')[:60]}")
        return out

    @mcp.tool()
    def altera_search(query: str = "", doc: str = "", limit: int = 15) -> dict:
        """Search ingested Altera documentation (offline).

        Source: skills/rad-cli-operations/references/altera-docs/*.md produced by
        scripts/ingest_altera.py. Returns deterministic section-ranked excerpts
        (token overlap + phrase/protocol boosts + alias normalization such as
        aw_valid->awvalid), optionally doc-filtered, and includes nearby figure
        links plus confidence metadata.
        """
        k = _knowledge()
        out = _kcall(k.altera_search, query, doc=doc, limit=limit)
        audit("altera_search", "-", detail=f"{doc or '*'}:{(query or '')[:60]}")
        return out
