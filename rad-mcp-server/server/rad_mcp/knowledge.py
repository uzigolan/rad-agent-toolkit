"""Offline MIB-knowledge access layer (Phase 3 of snmp-mib-catalog-design.md).

Opens rad-knowledge.sqlite READ-ONLY (URI mode=ro), one short-lived connection
per call (sqlite is cheap to open; FastMCP runs sync tools in worker threads).
Never contacts a device; parameterized SQL only; every result is bounded.

Ranking contract (deterministic for a given catalog):
  exact symbol/name/OID match  >  prefix match  >  FTS5 text match (bm25).

DB location: RAD_MCP_KNOWLEDGE_DB env override, else <repo>/build/
rad-knowledge.sqlite (produced by scripts/build_knowledge_catalog.py).
"""
from __future__ import annotations

import json
import os
import re
import sqlite3
from pathlib import Path

_RAD = Path(__file__).resolve().parents[2]           # rad-mcp-server/
DEFAULT_DB = _RAD / "build" / "rad-knowledge.sqlite"
REPORT_PATH = _RAD / "build" / "mib-catalog-report.json"

_OID_RE = re.compile(r"^\d+(\.\d+)+$")


class KnowledgeUnavailable(RuntimeError):
    pass


def _db_path() -> Path:
    p = Path(os.environ.get("RAD_MCP_KNOWLEDGE_DB") or DEFAULT_DB)
    if not p.exists():
        raise KnowledgeUnavailable(
            f"knowledge catalog not found at {p} — build it with: "
            "python scripts/build_knowledge_catalog.py "
            '--mib-root "MIBs2:priority=200" --mib-root "MIBS:priority=100"'
        )
    return p


def _connect() -> sqlite3.Connection:
    con = sqlite3.connect(f"file:{_db_path()}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def _fts_query(text: str) -> str:
    """Quote tokens; OR-join so concept phrasing is forgiving."""
    toks = [t for t in re.split(r"[^\w-]+", text) if t and len(t) > 1]
    return " OR ".join(f'"{t}"' for t in toks[:12]) or '""'


def _tc_info(cur, declared_type: str | None):
    if not declared_type:
        return None
    row = cur.execute(
        "SELECT base_type, display_hint FROM mib_textual_conventions WHERE name=? LIMIT 1",
        (declared_type,)).fetchone()
    if row:
        return {"textual_convention": declared_type,
                "base_type": row["base_type"], "display_hint": row["display_hint"]}
    return None


def _brief(cur, r: sqlite3.Row) -> dict:
    enums = cur.execute("SELECT count(*) FROM mib_enum_values WHERE object_id=?",
                        (r["id"],)).fetchone()[0]
    d = (r["description"] or "").strip()
    return {
        "name": r["name"], "oid": r["oid"], "kind": r["kind"],
        "access": r["access"], "type": r["declared_type"],
        "table": r["table_name"], "enums": enums,
        "description": (d[:180] + "…") if len(d) > 180 else d,
    }


def status() -> dict:
    con = _connect()
    try:
        cur = con.cursor()
        meta = dict(cur.execute("SELECT key, value FROM catalog_meta").fetchall())
        counts = {t: cur.execute(f"SELECT count(*) FROM {t}").fetchone()[0]  # noqa: S608 — fixed table list
                  for t in ("mib_modules", "mib_objects", "mib_enum_values",
                            "mib_notification_objects", "mib_table_indexes",
                            "capability_observations", "family_snmp_profile",
                            "cli_help", "manual_sections", "reference_docs")}
        # older catalogs predate the datasheet layer — report 0, don't fail
        try:
            counts["datasheet_sections"] = cur.execute(
                "SELECT count(*) FROM datasheet_sections").fetchone()[0]
        except sqlite3.OperationalError:
            counts["datasheet_sections"] = 0
        roots = [dict(r) for r in cur.execute(
            "SELECT root, priority, count(*) AS files, sum(selected) AS selected "
            "FROM source_files GROUP BY root, priority ORDER BY priority DESC")]
        out = {"db": str(_db_path()), "meta": meta, "counts": counts, "source_roots": roots}
        if REPORT_PATH.exists():
            rep = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
            out["last_build"] = {"result": rep.get("result"),
                                 "fixtures_ok": sum(1 for f in rep.get("fixtures", []) if f.get("ok")),
                                 "fixtures_total": len(rep.get("fixtures", [])),
                                 "modules_failed": list(rep.get("modules_failed", {})),
                                 "compat_diff": rep.get("compat_diff", {})}
        return out
    finally:
        con.close()


def search(query: str, module: str = "", kind: str = "", oid_prefix: str = "",
           family: str = "", limit: int = 25) -> dict:
    limit = max(1, min(int(limit), 100))
    con = _connect()
    try:
        cur = con.cursor()
        filters, args = [], []
        if module:
            filters.append("o.module = ?"); args.append(module)
        if kind:
            filters.append("o.kind = ?"); args.append(kind)
        if oid_prefix:
            filters.append("(o.oid = ? OR o.oid LIKE ?)"); args.extend([oid_prefix, oid_prefix + ".%"])
        fsql = (" AND " + " AND ".join(filters)) if filters else ""

        results, seen = [], set()

        def take(rows, tier):
            for r in list(rows):   # materialize: _brief() reuses the cursor
                if r["id"] in seen:
                    continue
                seen.add(r["id"])
                b = _brief(cur, r); b["match"] = tier
                results.append(b)

        q = query.strip()
        # tier 0: exact (symbol, MODULE::symbol, OID)
        take(cur.execute(
            f"SELECT o.* FROM mib_objects o WHERE (lower(o.symbol)=lower(?) OR o.name=? OR o.oid=?){fsql} "
            "ORDER BY o.name LIMIT ?", ([q, q, q] + args + [limit])), "exact")
        # tier 1: prefix (symbol prefix, or OID subtree when query looks like an OID)
        if len(results) < limit:
            if _OID_RE.match(q):
                take(cur.execute(
                    f"SELECT o.* FROM mib_objects o WHERE o.oid LIKE ?{fsql} ORDER BY o.oid LIMIT ?",
                    ([q + ".%"] + args + [limit - len(results)])), "oid-subtree")
            else:
                take(cur.execute(
                    f"SELECT o.* FROM mib_objects o WHERE lower(o.symbol) LIKE lower(?){fsql} "
                    "ORDER BY length(o.symbol), o.name LIMIT ?",
                    ([q + "%"] + args + [limit - len(results)])), "prefix")
        # tier 2: FTS over names/descriptions/enum labels
        if len(results) < limit:
            take(cur.execute(
                f"SELECT o.* FROM obj_fts f JOIN mib_objects o ON o.id = f.rowid "
                f"WHERE obj_fts MATCH ?{fsql} ORDER BY bm25(obj_fts), o.oid LIMIT ?",
                ([_fts_query(q)] + args + [limit - len(results)])), "text")

        out = {"query": q, "returned": len(results), "limit": limit, "results": results,
               "note": ("results are MIB-DEFINED objects; definition is not proof a family "
                        "implements them — check capability evidence (mib_describe / snmp-support.md)")}
        if family:
            prof = cur.execute("SELECT * FROM family_snmp_profile WHERE family=?", (family,)).fetchone()
            out["family_profile"] = dict(prof) if prof else f"unknown family '{family}'"
        return out
    finally:
        con.close()


def _resolve(cur, ref: str) -> sqlite3.Row | None:
    ref = ref.strip()
    if _OID_RE.match(ref):
        return cur.execute("SELECT * FROM mib_objects WHERE oid=? ORDER BY name LIMIT 1", (ref,)).fetchone()
    if "::" in ref:
        return cur.execute("SELECT * FROM mib_objects WHERE name=? LIMIT 1", (ref,)).fetchone()
    return cur.execute("SELECT * FROM mib_objects WHERE lower(symbol)=lower(?) "
                       "ORDER BY (module LIKE 'RAD-%') DESC, module LIMIT 1", (ref,)).fetchone()


def describe(ref: str) -> dict:
    con = _connect()
    try:
        cur = con.cursor()
        r = _resolve(cur, ref)
        if not r:
            return {"error": f"no object matches '{ref}' (symbol, MODULE::symbol, or numeric OID)"}
        oid_id = r["id"]
        enums = {row["label"]: row["value"] for row in
                 cur.execute("SELECT label, value FROM mib_enum_values WHERE object_id=? ORDER BY value", (oid_id,))}
        ranges = [dict(x) for x in cur.execute(
            "SELECT kind, min, max FROM mib_ranges WHERE object_id=?", (oid_id,))]
        idx = [dict(x) for x in cur.execute(
            "SELECT position, index_module, index_object, implied FROM mib_table_indexes "
            "WHERE object_id=? ORDER BY position", (oid_id,))]
        payload = [dict(x) for x in cur.execute(
            "SELECT position, payload_module, payload_object FROM mib_notification_objects "
            "WHERE object_id=? ORDER BY position", (oid_id,))]
        mod = cur.execute("SELECT m.*, s.root AS src_root, s.path AS src_path, s.sha256 AS src_sha256 "
                          "FROM mib_modules m LEFT JOIN source_files s ON s.id = m.source_file_id "
                          "WHERE m.module=?", (r["module"],)).fetchone()
        # capability evidence: exact-OID or subtree observations
        ev = [dict(x) for x in cur.execute(
            "SELECT family, device, subject, observed, support_state, evidence_type "
            "FROM capability_observations WHERE oid=? OR ? LIKE (oid || '.%') "
            "ORDER BY family, device LIMIT 10", (r["oid"], r["oid"] or ""))]
        out = {
            "name": r["name"], "oid": r["oid"], "kind": r["kind"],
            "syntax": {"declared_type": r["declared_type"],
                       **(_tc_info(cur, r["declared_type"]) or {})},
            "access": r["access"], "status": r["status"],
            "description": r["description"], "reference": r["reference"],
            "units": r["units"],
            "default": json.loads(r["default_json"]) if r["default_json"] else None,
            "enums": enums, "ranges": ranges,
            "table_context": {"table": r["table_name"], "entry": r["entry_name"],
                              "indexes": idx} if (r["table_name"] or idx) else None,
            "augments": ({"module": r["augments_module"], "object": r["augments_object"]}
                         if r["augments_object"] else None),
            "notification_payload": payload or None,
            "module": {"name": r["module"],
                       "last_updated": mod["last_updated"] if mod else None,
                       "organization": mod["organization"] if mod else None},
            "source": ({"root": mod["src_root"], "path": mod["src_path"],
                        "sha256": mod["src_sha256"]} if mod and mod["src_root"] else
                       {"root": "web (standard import)", "path": None, "sha256": None}),
            "capability": {"state": "supported (see evidence)" if ev else "unknown",
                           "evidence": ev or ["mib-defined only — no live observation for this OID"]},
        }
        return out
    finally:
        con.close()


def table_model(ref: str) -> dict:
    con = _connect()
    try:
        cur = con.cursor()
        r = _resolve(cur, ref)
        if not r:
            return {"error": f"no object matches '{ref}'"}
        # climb to the table object
        if r["kind"] == "column":
            entry = cur.execute("SELECT * FROM mib_objects WHERE oid=? AND kind='row' LIMIT 1",
                                (r["parent_oid"],)).fetchone()
        elif r["kind"] == "row":
            entry = r
        elif r["kind"] == "table":
            entry = cur.execute("SELECT * FROM mib_objects WHERE parent_oid=? AND kind='row' LIMIT 1",
                                (r["oid"],)).fetchone()
        else:
            return {"error": f"'{ref}' resolves to kind={r['kind']} — not a table/row/column"}
        if not entry:
            return {"error": f"could not resolve the row entry for '{ref}'"}
        table = cur.execute("SELECT * FROM mib_objects WHERE oid=? LIMIT 1",
                            (".".join(entry["oid"].split(".")[:-1]),)).fetchone()
        idx = [dict(x) for x in cur.execute(
            "SELECT position, index_module, index_object, implied FROM mib_table_indexes "
            "WHERE object_id=? ORDER BY position", (entry["id"],))]
        # resolve each index object's syntax (needed to encode instance suffixes)
        for i in list(idx):
            io = cur.execute("SELECT declared_type, oid FROM mib_objects WHERE module=? AND symbol=? LIMIT 1",
                             (i["index_module"], i["index_object"])).fetchone()
            i["type"] = io["declared_type"] if io else None
            i["oid"] = io["oid"] if io else None
        aug = cur.execute("SELECT base_module, base_object FROM mib_augments WHERE object_id=?",
                          (entry["id"],)).fetchone()
        cols = []
        for c in cur.execute("SELECT * FROM mib_objects WHERE parent_oid=? AND kind='column' ORDER BY oid",
                             (entry["oid"],)).fetchall():   # materialize: enum lookup reuses the cursor
            enums = {row["label"]: row["value"] for row in cur.execute(
                "SELECT label, value FROM mib_enum_values WHERE object_id=? ORDER BY value", (c["id"],))}
            cols.append({"symbol": c["symbol"], "oid": c["oid"], "access": c["access"],
                         "type": c["declared_type"], "units": c["units"],
                         "enums": enums or None,
                         "description": (c["description"] or "")[:140]})
        ident = [c["symbol"] for c in cols
                 if c["access"] in ("read-only", "read-write", "read-create")
                 and (c["type"] in ("DisplayString", "SnmpAdminString", "OCTET STRING")
                      or "name" in c["symbol"].lower() or "descr" in c["symbol"].lower())][:3]
        return {
            "table": {"name": table["name"] if table else None,
                      "oid": table["oid"] if table else None,
                      "description": table["description"] if table else None},
            "entry": {"name": entry["name"], "oid": entry["oid"]},
            "indexes": idx,
            "augments": dict(aug) if aug else None,
            "instance_encoding": ("instance suffix = ordered index values appended to the column OID"
                                  + ("; IMPLIED last index omits its length prefix" if any(i["implied"] for i in idx) else "")),
            "columns": cols,
            "suggested_identifying_columns": ident or [i["index_object"] for i in idx],
            "note": "MIB-defined model; verify family support before polling (capability evidence)",
        }
    finally:
        con.close()


def notifications(query: str, module: str = "", limit: int = 20) -> dict:
    limit = max(1, min(int(limit), 50))
    con = _connect()
    try:
        cur = con.cursor()
        filters, args = "", []
        if module:
            filters = " AND o.module=?"; args.append(module)
        rows = cur.execute(
            f"SELECT o.* FROM obj_fts f JOIN mib_objects o ON o.id=f.rowid "
            f"WHERE obj_fts MATCH ? AND o.kind='notification'{filters} "
            "ORDER BY bm25(obj_fts), o.oid LIMIT ?",
            [_fts_query(query)] + args + [limit]).fetchall()
        out = []
        for r in rows:
            payload = [f'{x["payload_module"]}::{x["payload_object"]}' for x in cur.execute(
                "SELECT payload_module, payload_object FROM mib_notification_objects "
                "WHERE object_id=? ORDER BY position", (r["id"],))]
            out.append({"name": r["name"], "oid": r["oid"], "status": r["status"],
                        "description": (r["description"] or "")[:200],
                        "payload": payload})
        return {"query": query, "returned": len(out), "results": out}
    finally:
        con.close()


# ── Phase 4: offline poll plans + live-value decoding ───────────────────────

READABLE = ("read-only", "read-write", "read-create")


def decode_value(oid: str, value: str) -> dict | None:
    """Catalog semantics for one returned varbind: symbolic name, enum label,
    units, display hint. Returns None when the catalog adds nothing. Never
    raises (live tools must work without a catalog)."""
    try:
        con = _connect()
    except KnowledgeUnavailable:
        return None
    try:
        cur = con.cursor()
        parts = oid.split(".")
        r = None
        for i in range(len(parts), 1, -1):
            r = cur.execute("SELECT * FROM mib_objects WHERE oid=? LIMIT 1",
                            (".".join(parts[:i]),)).fetchone()
            if r:
                break
        if not r:
            return None
        out = {"symbol": r["name"], "type": r["declared_type"]}
        if r["units"]:
            out["units"] = r["units"]
        tc = _tc_info(cur, r["declared_type"])
        if tc and tc.get("display_hint"):
            out["display_hint"] = tc["display_hint"]
        try:
            label = cur.execute(
                "SELECT label FROM mib_enum_values WHERE object_id=? AND value=?",
                (r["id"], int(value))).fetchone()
            if label:
                out["meaning"] = label["label"]
        except (ValueError, TypeError):
            pass
        return out
    except Exception:
        return None
    finally:
        con.close()


def build_poll_plan(refs, family, max_rows_per_walk=200):
    """Offline poll plan (NEVER contacts a device).

    Resolves each ref (symbol / MODULE::symbol / OID / concept), expands tables
    to walks with identifying columns, excludes non-readable and
    notification-only objects, and honors the family's verified transport
    profile. Operations use only the guarded snmp_get / snmp_walk tools; the
    caller shows them and asks the confirmation question before executing.
    """
    max_rows_per_walk = max(1, min(int(max_rows_per_walk), 2000))
    con = _connect()
    try:
        cur = con.cursor()
        prof_row = cur.execute("SELECT * FROM family_snmp_profile WHERE family=?",
                               (family,)).fetchone()
        profile = dict(prof_row) if prof_row else None
        get_preferred = bool(profile and "get-preferred" in (profile["read_strategy"] or ""))

        operations, decode, excluded, notes = [], [], [], []
        planned_walks = set()

        def add_decode(r):
            enums = {row["label"]: row["value"] for row in cur.execute(
                "SELECT label,value FROM mib_enum_values WHERE object_id=? ORDER BY value",
                (r["id"],)).fetchall()}
            decode.append({"oid": r["oid"], "symbol": r["name"],
                           "type": r["declared_type"], "units": r["units"],
                           "enums": enums})

        def plan_column_walk(r, reason):
            if r["oid"] in planned_walks:
                return
            planned_walks.add(r["oid"])
            operations.append({"tool": "snmp_walk", "oid": r["oid"],
                               "max_rows": max_rows_per_walk, "reason": reason})
            add_decode(r)

        def handle(r):
            kind = r["kind"]
            if kind == "notification":
                excluded.append({"ref": r["name"], "why": "notification-only (arrives as a trap, not pollable)"})
                return
            if kind in ("table", "row"):
                entry = r if kind == "row" else cur.execute(
                    "SELECT * FROM mib_objects WHERE parent_oid=? AND kind='row' LIMIT 1",
                    (r["oid"],)).fetchone()
                if not entry:
                    excluded.append({"ref": r["name"], "why": "table without resolvable row entry"})
                    return
                cols = cur.execute("SELECT * FROM mib_objects WHERE parent_oid=? AND kind='column' "
                                   "ORDER BY oid", (entry["oid"],)).fetchall()
                readable = [c for c in cols if c["access"] in READABLE]
                if not readable:
                    excluded.append({"ref": r["name"], "why": "no readable columns"})
                    return
                if get_preferred:
                    notes.append(r["name"] + ": family is get-preferred (sparse GETNEXT chain) — walk the "
                                 "first identifying column to discover instances, then snmp_get explicit "
                                 "instance OIDs for the rest")
                    plan_column_walk(readable[0], "discover " + r["name"] + " instances (identifying column)")
                    for c in readable[1:]:
                        add_decode(c)
                else:
                    operations.append({"tool": "snmp_walk", "oid": entry["oid"],
                                       "max_rows": max_rows_per_walk,
                                       "reason": "walk " + r["name"] + " rows (all readable columns)"})
                    planned_walks.add(entry["oid"])
                    for c in readable:
                        add_decode(c)
                return
            if kind == "scalar":
                if r["access"] not in READABLE:
                    excluded.append({"ref": r["name"], "why": "not readable (access=" + str(r["access"]) + ")"})
                    return
                operations.append({"tool": "snmp_get", "oids": [r["oid"] + ".0"],
                                   "reason": "read scalar " + r["name"]})
                add_decode(r)
            elif kind == "column":
                if r["access"] not in READABLE:
                    excluded.append({"ref": r["name"], "why": "not readable (access=" + str(r["access"]) + ")"})
                    return
                plan_column_walk(r, "walk column " + r["name"] + " (instances unknown offline)")
            else:
                excluded.append({"ref": r["name"], "why": "kind=" + str(kind) + " is not pollable"})

        unresolved = []
        for ref in refs[:32]:
            r = _resolve(cur, ref)
            if r:
                handle(r)
                continue
            hits = search(ref, limit=5)["results"]
            hit_rows = [_resolve(cur, h["name"]) for h in hits]
            hit_rows = [h for h in hit_rows if h]
            if not hit_rows:
                unresolved.append(ref)
                continue
            notes.append("'" + ref + "' resolved by concept search to: "
                         + ", ".join(h["name"] for h in hit_rows[:3]))
            for h in hit_rows[:3]:
                handle(h)

        merged, gets = [], []
        for op in operations:
            if op["tool"] == "snmp_get":
                gets.extend(op["oids"])
            else:
                merged.append(op)
        if gets:
            merged.insert(0, {"tool": "snmp_get", "oids": gets[:64],
                              "reason": "read planned scalars in one call"})

        evidence = [dict(x) for x in cur.execute(
            "SELECT device, subject, observed FROM capability_observations "
            "WHERE family=? LIMIT 6", (family,))]
        catalog_version = dict(cur.execute("SELECT key,value FROM catalog_meta").fetchall())
        transport_notes = [
            "GETNEXT/GET only — RAD agents mishandle GETBULK (the backend never uses it)",
            "a mid-walk timeout after one retry is END-OF-VIEW on RAD agents, not an outage",
        ]
        if profile:
            transport_notes.append("family '" + family + "' answers ONLY: " + profile["versions_verified"])
        return {
            "catalog_build": catalog_version.get("built_at"),
            "target_family": family,
            "transport_profile": profile or ("unknown family '" + family
                                             + "' — no verified profile; verify before polling"),
            "transport_notes": transport_notes,
            "confidence": ("live-snmp evidence exists for this family (see evidence); individual "
                           "objects remain mib-defined unless observed"
                           if evidence else
                           "mib-defined only; live support not verified for this family"),
            "family_evidence": evidence,
            "operations": merged,
            "decode": decode,
            "excluded": excluded,
            "unresolved": unresolved,
            "notes": notes,
            "next_step": ("Show the exact operations to the user and ask the confirmation "
                          "question, then execute via the existing snmp_get/snmp_walk tools "
                          "(device chosen at execution time). This plan itself contacts nothing."),
        }
    finally:
        con.close()


# ── Phase 5: CLI-reference + manual retrieval (one service, distinct domains) ─

def _excerpt(body: str, query: str, width: int = 240) -> str:
    """Excerpt around the first query-token hit (contentless FTS cannot
    snippet(); bodies are stored in the domain tables instead)."""
    body = " ".join((body or "").split())
    toks = [x.lower() for x in re.split(r"[^\w-]+", query) if len(x) > 2]
    pos = -1
    low = body.lower()
    for tk in toks:
        pos = low.find(tk)
        if pos >= 0:
            break
    if pos < 0:
        return body[:width] + ("…" if len(body) > width else "")
    start = max(0, pos - width // 3)
    end = min(len(body), pos + width)
    return ("…" if start else "") + body[start:end] + ("…" if end < len(body) else "")


def cli_search(query: str, family: str = "", context: str = "", limit: int = 15) -> dict:
    """Search the harvested CLI `?`-help. Ranking: exact context/prefix match >
    context prefix > FTS over help text. `family` narrows to one family
    (strongly recommended — commands are family-specific)."""
    limit = max(1, min(int(limit), 50))
    con = _connect()
    try:
        cur = con.cursor()
        filters, args = [], []
        if family:
            filters.append("c.family=?"); args.append(family)
        if context:
            filters.append("(c.context=? OR c.context LIKE ?)")
            args.extend([context, context + " %"])
        fsql = (" AND " + " AND ".join(filters)) if filters else ""
        results, seen = [], set()

        def take(rows, tier):
            for r in list(rows):
                if r["id"] in seen:
                    continue
                seen.add(r["id"])
                body = (r["body"] or "").strip()
                results.append({
                    "family": r["family"], "context": r["context"],
                    "prefix": r["prefix"], "kind": r["kind"], "match": tier,
                    "help": (body[:700] + "…") if len(body) > 700 else body,
                })

        q = query.strip()
        take(cur.execute(
            f"SELECT c.* FROM cli_help c WHERE (c.prefix=? OR c.context=?){fsql} "
            "ORDER BY c.family, c.context LIMIT ?", ([q, q] + args + [limit])), "exact")
        if len(results) < limit:
            take(cur.execute(
                f"SELECT c.* FROM cli_help c WHERE (c.context LIKE ? OR c.prefix LIKE ?){fsql} "
                "ORDER BY length(c.context), c.family LIMIT ?",
                (["% " + q + "%", q + "%"] + args + [limit - len(results)])), "prefix")
        if len(results) < limit:
            ftsf, fargs = "", []
            if family:
                ftsf += " AND c.family=?"; fargs.append(family)
            if context:
                ftsf += " AND (c.context=? OR c.context LIKE ?)"; fargs.extend([context, context + " %"])
            take(cur.execute(
                f"SELECT c.* FROM cli_fts f JOIN cli_help c ON c.id=f.rowid "
                f"WHERE cli_fts MATCH ?{ftsf} ORDER BY bm25(cli_fts) LIMIT ?",
                ([_fts_query(q)] + fargs + [limit - len(results)])), "text")
        return {"query": q, "family": family or "(all — narrow it: commands are family-specific)",
                "returned": len(results), "results": results,
                "note": "harvested `?`-help; the CLI reference is the syntax truth for its harvest firmware"}
    finally:
        con.close()


def manual_search(query: str, family: str = "", limit: int = 10,
                  include_refdocs: bool = True) -> dict:
    """Search the ingested user manuals (per-section) and, optionally, the
    curated reference docs (verified-commands, snmp-support, known-limitations,
    snmp capability maps). Returns bounded excerpts with chapter/section/pages
    provenance — concepts and limits live here; exact syntax lives in cli_search."""
    limit = max(1, min(int(limit), 30))
    con = _connect()
    try:
        cur = con.cursor()
        fq = _fts_query(query)
        results = []
        fsql, args = "", []
        if family:
            fsql = " AND m.family=?"; args.append(family)
        rows = cur.execute(
            f"SELECT m.* FROM manual_fts f JOIN manual_sections m ON m.id=f.rowid "
            f"WHERE manual_fts MATCH ?{fsql} ORDER BY bm25(manual_fts) LIMIT ?",
            [fq] + args + [limit]).fetchall()
        for r in rows:
            results.append({"domain": "manual", "family": r["family"],
                            "chapter": r["chapter"], "section": r["section"],
                            "pages": r["pages"], "file": r["file"],
                            "excerpt": _excerpt(r["body"], query)})
        if include_refdocs and len(results) < limit:
            for r in cur.execute(
                    "SELECT d.* FROM refdoc_fts f JOIN reference_docs d ON d.id=f.rowid "
                    "WHERE refdoc_fts MATCH ? ORDER BY bm25(refdoc_fts) LIMIT ?",
                    (fq, limit - len(results))).fetchall():
                results.append({"domain": "refdoc", "family": None,
                                "doc": r["name"], "section": r["section"],
                                "excerpt": _excerpt(r["body"], query)})
        return {"query": query, "returned": len(results), "results": results,
                "note": "concepts/limits/procedures from the manual layer; "
                        "exact command syntax comes from cli_search"}
    finally:
        con.close()


def datasheet_search(query: str, family: str = "", product: str = "",
                     kind: str = "", limit: int = 10) -> dict:
    """Search the ingested product datasheets (per-subject-section). Third
    knowledge domain: hardware specs, interfaces, timing, ordering options and
    product variants live here — concepts/procedures are manual_search's job,
    exact command syntax is cli_search's. `kind` in results distinguishes a
    standalone device ('system') from a plug-in chassis module ('card')."""
    limit = max(1, min(int(limit), 30))
    con = _connect()
    try:
        cur = con.cursor()
        try:
            cur.execute("SELECT 1 FROM datasheet_sections LIMIT 1")
        except sqlite3.OperationalError:
            return {"query": query, "returned": 0, "results": [],
                    "note": "catalog predates the datasheet layer — rebuild it "
                            "with scripts/build_knowledge_catalog.py"}
        fsql, args = "", []
        if family:
            fsql += " AND d.family=?"; args.append(family)
        if product:
            fsql += " AND d.product=?"; args.append(product)
        if kind:
            fsql += " AND d.kind=?"; args.append(kind)
        rows = cur.execute(
            f"SELECT d.* FROM datasheet_fts f JOIN datasheet_sections d ON d.id=f.rowid "
            f"WHERE datasheet_fts MATCH ?{fsql} ORDER BY bm25(datasheet_fts) LIMIT ?",
            [_fts_query(query)] + args + [limit]).fetchall()
        results = [{"domain": "datasheet", "family": r["family"],
                    "product": r["product"], "kind": r["kind"],
                    "section": r["section"], "pages": r["pages"],
                    "file": r["file"], "excerpt": _excerpt(r["body"], query)}
                   for r in rows]
        return {"query": query, "returned": len(results), "results": results,
                "note": "hardware specs/interfaces/ordering from the datasheet layer; "
                        "kind=card means a module for its family's chassis, not a "
                        "standalone device; procedures live in manual_search, syntax "
                        "in cli_search"}
    finally:
        con.close()
