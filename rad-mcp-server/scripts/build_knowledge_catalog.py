"""Build the semantic MIB catalog (rad-knowledge.sqlite) — Phases 1-2 of
references/snmp-mib-catalog-design.md.

Phase 1: deterministic source selection over prioritized MIB roots, PySMI
semantic compilation (genTexts), normalization into SQLite (+FTS5),
capability/transport-profile seeding from verified facts, fixture validation,
and a machine+human build report.

Phase 2: regenerate the flat compatibility map (snmp-oid-map.json) from the
database and diff it against the currently shipped map; --apply-compat
replaces the shipped map when the diff is reviewed.

Usage (server venv python, from the repo root):
  python rad-mcp-server/scripts/build_knowledge_catalog.py \
    [--mib-root "MIBs2:priority=200" --mib-root "MIBS:priority=100"] \
      [--output rad-mcp-server/build/rad-knowledge.sqlite] \
      [--report rad-mcp-server/build/mib-catalog-report.json] \
      [--apply-compat] [--strict]

The build never contacts a device. A failed build leaves any previously
packaged database untouched (temp file + atomic replace).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]          # workspace root (fusion-cli)
RAD = REPO / "rad-mcp-server"
REFS = RAD / "skills" / "rad-cli-operations" / "references"
MODULE_RE = re.compile(r"^\s*([A-Za-z][\w-]*)\s+DEFINITIONS\s*(?:[\w\s]*)?::=\s*BEGIN", re.M)

SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE catalog_meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE source_files (
  id INTEGER PRIMARY KEY, root TEXT NOT NULL, path TEXT NOT NULL,
  sha256 TEXT NOT NULL, priority INTEGER NOT NULL, module TEXT,
  selected INTEGER NOT NULL, reason TEXT NOT NULL);
CREATE TABLE mib_modules (
  module TEXT PRIMARY KEY, identity_oid TEXT, organization TEXT, contact TEXT,
  description TEXT, last_updated TEXT, source_file_id INTEGER REFERENCES source_files(id),
  compile_status TEXT NOT NULL, raw_meta TEXT);
CREATE TABLE mib_imports (
  module TEXT NOT NULL REFERENCES mib_modules(module),
  from_module TEXT NOT NULL, symbol TEXT NOT NULL);
CREATE TABLE mib_objects (
  id INTEGER PRIMARY KEY, module TEXT NOT NULL REFERENCES mib_modules(module),
  symbol TEXT NOT NULL, name TEXT NOT NULL, oid TEXT, kind TEXT NOT NULL,
  parent_oid TEXT, declared_type TEXT, base_type TEXT, textual_convention TEXT,
  display_hint TEXT, access TEXT, status TEXT, description TEXT, reference TEXT,
  units TEXT, default_json TEXT, table_name TEXT, entry_name TEXT,
  augments_module TEXT, augments_object TEXT, raw_json TEXT NOT NULL,
  UNIQUE(module, symbol));
CREATE INDEX ix_obj_oid ON mib_objects(oid);
CREATE INDEX ix_obj_name ON mib_objects(name);
CREATE INDEX ix_obj_symbol_lc ON mib_objects(lower(symbol));
CREATE INDEX ix_obj_parent ON mib_objects(parent_oid);
CREATE INDEX ix_obj_kind ON mib_objects(kind);
CREATE TABLE mib_enum_values (
  object_id INTEGER NOT NULL REFERENCES mib_objects(id),
  label TEXT NOT NULL, value INTEGER NOT NULL);
CREATE INDEX ix_enum_obj ON mib_enum_values(object_id);
CREATE TABLE mib_ranges (
  object_id INTEGER NOT NULL REFERENCES mib_objects(id),
  kind TEXT NOT NULL, min INTEGER, max INTEGER);
CREATE TABLE mib_table_indexes (
  object_id INTEGER NOT NULL REFERENCES mib_objects(id),   -- the row object
  position INTEGER NOT NULL, index_module TEXT NOT NULL,
  index_object TEXT NOT NULL, implied INTEGER NOT NULL);
CREATE TABLE mib_augments (
  object_id INTEGER NOT NULL REFERENCES mib_objects(id),
  base_module TEXT NOT NULL, base_object TEXT NOT NULL);
CREATE TABLE mib_notification_objects (
  object_id INTEGER NOT NULL REFERENCES mib_objects(id),   -- the notification
  position INTEGER NOT NULL, payload_module TEXT NOT NULL,
  payload_object TEXT NOT NULL);
CREATE TABLE mib_textual_conventions (
  module TEXT NOT NULL, name TEXT NOT NULL, base_type TEXT,
  display_hint TEXT, description TEXT, raw_json TEXT, UNIQUE(module, name));
-- capability evidence (design: MIB-defined != implemented)
CREATE TABLE family_snmp_profile (
  family TEXT PRIMARY KEY, versions_verified TEXT NOT NULL,
  versions_claimed TEXT NOT NULL, credential_model TEXT NOT NULL,
  read_strategy TEXT NOT NULL, bulk_supported INTEGER NOT NULL,
  end_of_view TEXT NOT NULL, provenance TEXT NOT NULL);
CREATE TABLE capability_runs (
  run_id TEXT PRIMARY KEY, run_type TEXT NOT NULL, ran_at TEXT NOT NULL,
  environment TEXT NOT NULL, notes TEXT);
CREATE TABLE capability_observations (
  run_id TEXT NOT NULL REFERENCES capability_runs(run_id),
  family TEXT NOT NULL, device TEXT NOT NULL, oid TEXT, subject TEXT NOT NULL,
  observed TEXT NOT NULL, support_state TEXT NOT NULL, evidence_type TEXT NOT NULL);
CREATE VIRTUAL TABLE obj_fts USING fts5(
  name, symbol_words, description, enum_labels, content='');
-- Phase 5: CLI references + manuals + curated reference docs (one DB,
-- domain-distinct tables, per-file provenance)
CREATE TABLE knowledge_sources (
  id INTEGER PRIMARY KEY, domain TEXT NOT NULL, family TEXT, path TEXT NOT NULL,
  sha256 TEXT NOT NULL);
CREATE TABLE cli_help (
  id INTEGER PRIMARY KEY, family TEXT NOT NULL, kind TEXT NOT NULL,
  context TEXT NOT NULL, prefix TEXT NOT NULL, body TEXT NOT NULL,
  source_id INTEGER NOT NULL REFERENCES knowledge_sources(id));
CREATE INDEX ix_cli_family_ctx ON cli_help(family, context);
CREATE VIRTUAL TABLE cli_fts USING fts5(family, context, prefix, body, content='');
CREATE TABLE manual_sections (
  id INTEGER PRIMARY KEY, family TEXT NOT NULL, file TEXT NOT NULL,
  chapter TEXT NOT NULL, section TEXT NOT NULL, pages TEXT, body TEXT NOT NULL,
  source_id INTEGER NOT NULL REFERENCES knowledge_sources(id));
CREATE INDEX ix_man_family ON manual_sections(family);
CREATE VIRTUAL TABLE manual_fts USING fts5(family, chapter, section, body, content='');
CREATE TABLE reference_docs (
  id INTEGER PRIMARY KEY, name TEXT NOT NULL, section TEXT NOT NULL,
  body TEXT NOT NULL, source_id INTEGER NOT NULL REFERENCES knowledge_sources(id));
CREATE VIRTUAL TABLE refdoc_fts USING fts5(name, section, body, content='');
-- Datasheets: third knowledge domain (hardware specs / interfaces / variants /
-- ordering). family is NULL for standalone products with no inventory family;
-- kind is 'system' (standalone device), 'card' (chassis module) or 'accessory'.
CREATE TABLE datasheet_sections (
  id INTEGER PRIMARY KEY, family TEXT, product TEXT NOT NULL, kind TEXT NOT NULL,
  file TEXT NOT NULL, section TEXT NOT NULL, pages TEXT, body TEXT NOT NULL,
  source_id INTEGER NOT NULL REFERENCES knowledge_sources(id));
CREATE INDEX ix_ds_family ON datasheet_sections(family);
CREATE INDEX ix_ds_product ON datasheet_sections(product);
CREATE VIRTUAL TABLE datasheet_fts USING fts5(family, product, section, body, content='');
"""

# ── verified seed data: family profiles come from the SINGLE SOURCE yaml ───
def _load_family_profiles_yaml():
    import yaml
    doc = yaml.safe_load((REFS / "family-profiles.yaml").read_text(encoding="utf-8"))
    prov = doc.get("provenance", "")
    rows = []
    for fam, prof in sorted((doc.get("families") or {}).items()):
        rows.append((fam,
                     prof.get("versions_verified", "unknown"),
                     prof.get("versions_claimed", "unknown"),
                     prof.get("credential_model", "unknown"),
                     prof.get("read_strategy", "walk-ok"),
                     1 if prof.get("bulk_supported") else 0,
                     prof.get("end_of_view", "silence")))
    return rows, prov


FAMILY_PROFILES, PROFILE_PROVENANCE = _load_family_profiles_yaml()
CAPABILITY_RUNS = [
    ("run-2026-07-16-probe", "live-snmp", "2026-07-16",
     "pysnmp 7.1.27 GETs, lab LAN", "MIB-II system-group identity probes, all reachable units"),
    ("run-2026-07-16-walk", "live-snmp", "2026-07-16",
     "pysnmp 7.1.27 GETNEXT walks, row-capped", "capability walks -> snmp-map-minid.md / snmp-map-etx2v.md"),
]
PROBE_OBSERVATIONS = [
    # family, device, oid, subject, observed
    ("minid", "minid-1", "1.3.6.1.2.1.1.1.0", "sysDescr", "MiNID Hw: 1.2, Sw: 2.6.0(0.28)"),
    ("minid", "minid-1", "1.3.6.1.2.1.1.2.0", "sysObjectID", "1.3.6.1.4.1.164.6.1.6.36"),
    ("etx2v", "etx2v-1", "1.3.6.1.2.1.1.1.0", "sysDescr", "uCPE-OS Hw: 1.0, Sw: 5.0.0.825"),
    ("etx2v", "etx2v-1", "1.3.6.1.2.1.1.2.0", "sysObjectID", "1.3.6.1.4.1.164.6.1.6.55"),
    ("mp4100", "marks-mp4", "1.3.6.1.2.1.1.1.0", "sysDescr", "MP-4100,  HW: 0,  SW: 4.91.70"),
    ("mp4100", "marks-mp4", "1.3.6.1.2.1.1.2.0", "sysObjectID", "1.3.6.1.4.1.164.6.1.3.120"),
    ("mp1", "mp-one", "1.3.6.1.2.1.1.1.0", "sysDescr", "MP-1,  HW: /0.0,  SW: 2.20(0.61)"),
    ("mp1", "mp-one", "1.3.6.1.2.1.1.2.0", "sysObjectID", "1.3.6.1.4.1.164.6.1.3.179"),
    ("secflow", "sf-163-187", "1.3.6.1.2.1.1.1.0", "sysDescr", "SF-1p Hw: 0.2, Sw: 6.5.0.35"),
    ("secflow", "sf-163-187", "1.3.6.1.2.1.1.2.0", "sysObjectID", "1.3.6.1.4.1.164.6.1.10.7"),
    ("secflow", "EliadSF-1p64", "1.3.6.1.2.1.1.1.0", "sysDescr", "SF-1p Hw: 0.5, Sw: 9.9.9.9.319"),
    ("etx1p", "asafs-etx", "1.3.6.1.2.1.1.1.0", "sysDescr", "ETX-1p Hw: 0.4, Sw: 6.4.0.165"),
    ("etx1p", "ehud1p", "1.3.6.1.2.1.1.1.0", "sysDescr", "ETX-1p Hw: 0.4, Sw: 6.5.0.43"),
    ("etx1p", "asafs-etx", "1.3.6.1.2.1.1.2.0", "sysObjectID", "1.3.6.1.4.1.164.6.1.6.68"),
    ("etx2", "Raviv-Etx", "1.3.6.1.2.1.1.1.0", "sysDescr", "ETX-2i-10G-E-8SFPP Hw: 0.1/, Sw: 6.8.5(1.137)"),
    ("etx2", "Raviv-Etx", "1.3.6.1.2.1.1.2.0", "sysObjectID", "1.3.6.1.4.1.164.6.1.6.79"),
]
WALK_OBSERVATIONS = [
    ("minid", "minid-1", "1.3.6.1.2.1", "mib-2 walk", "53 varbinds, 39 object groups; agent silent after entPhysicalSerialNum.1001"),
    ("minid", "minid-1", "1.3.6.1.4.1.164", "RAD arc walk", "31 varbinds; sparse NEXT chain — walks under-report, poll by GET"),
    ("etx2v", "etx2v-1", "1.3.6.1.2.1", "mib-2 walk", "1156 varbinds, 237 object groups; silent after entPhysicalDescr.1001"),
    ("etx2v", "etx2v-1", "1.3.6.1.4.1.164", "RAD arc walk", "3753 varbinds, 403 object groups, complete (incl. 258-entry alarm dictionary)"),
]

FIXTURES = [
    # (module, symbol, checks) — checks: oid / kind / enum:{label:val} / index0 / augments / payload_len_min
    ("SNMPv2-MIB", "sysDescr", {"oid": "1.3.6.1.2.1.1.1", "kind": "scalar"}),
    ("SNMPv2-MIB", "sysObjectID", {"oid": "1.3.6.1.2.1.1.2", "kind": "scalar"}),
    ("IF-MIB", "ifTable", {"oid": "1.3.6.1.2.1.2.2", "kind": "table"}),
    ("IF-MIB", "ifOperStatus", {"kind": "column", "enum": {"up": 1, "down": 2}}),
    ("RAD-EthIf-MIB", "erpTable", {"oid": "1.3.6.1.4.1.164.3.1.6.1.4.2.1", "kind": "table"}),
    ("RAD-EthIf-MIB", "erpEntry", {"kind": "row", "index0": "erpIdx"}),
    ("RAD-EthIf-MIB", "erpNodeState", {"oid": "1.3.6.1.4.1.164.3.1.6.1.4.2.1.1.4", "kind": "column",
                                       "enum": {"init": 1, "idle": 2, "protected": 3,
                                                "manualSwitch": 4, "forcedSwitch": 5, "pending": 6}}),
    ("RAD-EthIf-MIB", "erpPortRapsRxValidMsg", {"kind": "column"}),
    ("RAD-EthIf-MIB", "dot3OamXEntry", {"kind": "row", "augments": ("RAD-EthIf-MIB", "dot3OamEntry")}),
    ("RAD-EthIf-MIB", "adminDown", {"oid": "1.3.6.1.4.1.164.3.1.6.1.0.34", "kind": "notification",
                                    "payload_len_min": 2}),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def oid_key(oid: str):
    return [int(x) for x in oid.split(".")]


def select_sources(roots: list[tuple[Path, int]], report: dict):
    """Scan roots (high priority first); one file wins per module name."""
    selected: dict[str, dict] = {}
    files_seen = []
    for root, prio in sorted(roots, key=lambda r: -r[1]):
        for f in sorted(root.iterdir()):
            if f.suffix.lower() not in (".mib", ".txt", ".my"):
                continue
            text = f.read_text(encoding="utf-8", errors="replace")
            m = MODULE_RE.search(text)          # full-file scan (long headers OK)
            # Store a repo-relative path when the MIB root lives inside the repo;
            # otherwise (a user-supplied directory anywhere on disk) store the
            # absolute path. Both reconstruct via `REPO / path` later — an absolute
            # right-hand side wins the join, so copyfile still finds the source.
            try:
                rel_path = str(f.relative_to(REPO))
            except ValueError:
                rel_path = str(f)
            rec = {"root": root.name, "path": rel_path, "sha256": sha256(f),
                   "priority": prio, "module": m.group(1) if m else None}
            if not m:
                rec.update(selected=0, reason="no ASN.1 module header found")
            elif m.group(1) in selected:
                prev = selected[m.group(1)]
                rec.update(selected=0,
                           reason=f"shadowed by {prev['root']}/{Path(prev['path']).name} (priority {prev['priority']})")
            else:
                rec.update(selected=1, reason=f"highest-priority definition of {m.group(1)}")
                selected[m.group(1)] = rec
            files_seen.append(rec)
    report["source_files"] = files_seen
    report["modules_selected"] = len(selected)
    return selected, files_seen


def compile_modules(selected: dict, stage: Path, jout: Path, report: dict):
    if not selected:
        stage.mkdir(parents=True, exist_ok=True)
        jout.mkdir(parents=True, exist_ok=True)
        report["pysmi_version"] = "not-run (no MIB roots selected)"
        report["compile_results"] = {}
        report["modules_compiled"] = 0
        report["modules_failed"] = {}
        return {}

    from pysmi.reader import FileReader, HttpReader
    from pysmi.writer import FileWriter
    from pysmi.parser import SmiStarParser
    from pysmi.codegen import JsonCodeGen
    from pysmi.compiler import MibCompiler
    import pysmi

    stage.mkdir(parents=True, exist_ok=True)
    jout.mkdir(parents=True, exist_ok=True)
    for mod, rec in selected.items():
        shutil.copyfile(REPO / rec["path"], stage / f"{mod}.mib")
    compiler = MibCompiler(SmiStarParser(), JsonCodeGen(),
                           FileWriter(str(jout)).set_options(suffix=".json"))
    compiler.add_sources(FileReader(str(stage)))
    compiler.add_sources(HttpReader("https://mibs.pysnmp.com/asn1/@mib@"))
    results = compiler.compile(*sorted(selected), **{"ignoreErrors": True, "genTexts": True})
    status = {k: str(v) for k, v in sorted(results.items())}
    report["pysmi_version"] = pysmi.__version__
    report["compile_results"] = status
    ok = [k for k, v in status.items() if v in ("compiled", "untouched")]
    fail = {k: v for k, v in status.items() if v not in ("compiled", "untouched")}
    report["modules_compiled"] = len(ok)
    report["modules_failed"] = fail
    return status


KIND_MAP = {"moduleidentity": "module-identity", "objectidentity": "identity",
            "notificationtype": "notification", "objectgroup": "group",
            "notificationgroup": "group", "modulecompliance": "compliance",
            "agentcapabilities": "capabilities"}


def normalize(jout: Path, selected: dict, compile_status: dict, con: sqlite3.Connection, report: dict):
    cur = con.cursor()
    # source_files rows
    src_ids = {}
    for rec in report["source_files"]:
        cur.execute("INSERT INTO source_files(root,path,sha256,priority,module,selected,reason) "
                    "VALUES (?,?,?,?,?,?,?)",
                    (rec["root"], rec["path"], rec["sha256"], rec["priority"],
                     rec["module"], rec["selected"], rec["reason"]))
        if rec["selected"]:
            src_ids[rec["module"]] = cur.lastrowid

    counts = {"objects": 0, "enums": 0, "ranges": 0, "indexes": 0, "augments": 0,
              "notifications": 0, "notif_objects": 0, "tcs": 0, "imports": 0}
    oid_owner: dict[str, str] = {}
    conflicts = []

    for jf in sorted(jout.glob("*.json")):
        mod = jf.stem
        try:
            doc = json.loads(jf.read_text(encoding="utf-8"))
        except Exception as exc:
            report.setdefault("json_parse_failures", []).append(f"{mod}: {exc}")
            continue
        # module row (identity from any moduleidentity member)
        ident = next((v for v in doc.values() if isinstance(v, dict)
                      and v.get("class") == "moduleidentity"), {})
        cur.execute("INSERT OR REPLACE INTO mib_modules(module,identity_oid,organization,contact,"
                    "description,last_updated,source_file_id,compile_status,raw_meta) VALUES (?,?,?,?,?,?,?,?,?)",
                    (mod, ident.get("oid"), ident.get("organization"), ident.get("contactinfo"),
                     ident.get("description"), ident.get("lastupdated"),
                     src_ids.get(mod), compile_status.get(mod, "dependency"),
                     json.dumps(doc.get("meta", {}))))
        for from_mod, syms in (doc.get("imports") or {}).items():
            if not isinstance(syms, list):
                continue
            for s in syms:
                cur.execute("INSERT INTO mib_imports(module,from_module,symbol) VALUES (?,?,?)",
                            (mod, from_mod, s))
                counts["imports"] += 1
        # entry->table map for column table_name/entry_name resolution
        rows = {v["oid"]: v for v in doc.values() if isinstance(v, dict) and v.get("nodetype") == "row" and v.get("oid")}
        tables = {v["oid"]: v for v in doc.values() if isinstance(v, dict) and v.get("nodetype") == "table" and v.get("oid")}
        for name, v in sorted(doc.items()):
            if not isinstance(v, dict) or name in ("imports", "meta"):
                continue
            cls = v.get("class")
            if cls == "textualconvention":
                cur.execute("INSERT OR IGNORE INTO mib_textual_conventions(module,name,base_type,"
                            "display_hint,description,raw_json) VALUES (?,?,?,?,?,?)",
                            (mod, name, (v.get("type") or {}).get("type") if isinstance(v.get("type"), dict) else v.get("type"),
                             v.get("displayhint"), v.get("description"), json.dumps(v)))
                counts["tcs"] += 1
                continue
            oid = v.get("oid")
            if cls == "objecttype":
                kind = v.get("nodetype") or "scalar"
            elif cls in KIND_MAP:
                kind = KIND_MAP[cls]
            elif oid:
                kind = cls or "node"
            else:
                continue  # value/type helpers without OIDs
            if not oid:
                continue
            syntax = v.get("syntax") if isinstance(v.get("syntax"), dict) else {}
            declared = syntax.get("type")
            parent = ".".join(oid.split(".")[:-1]) if oid and "." in oid else None
            # table/entry context for columns
            tbl = ent = None
            if kind == "column" and parent in rows:
                ent = rows[parent]["name"]
                t_oid = ".".join(parent.split(".")[:-1])
                if t_oid in tables:
                    tbl = tables[t_oid]["name"]
            aug = v.get("augmention") or {}
            cur.execute(
                "INSERT INTO mib_objects(module,symbol,name,oid,kind,parent_oid,declared_type,"
                "base_type,textual_convention,display_hint,access,status,description,reference,"
                "units,default_json,table_name,entry_name,augments_module,augments_object,raw_json) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (mod, name, f"{mod}::{name}", oid, kind, parent, declared,
                 declared, None, v.get("displayhint"), v.get("maxaccess"), v.get("status"),
                 v.get("description"), v.get("reference"), v.get("units"),
                 json.dumps(v.get("default")) if v.get("default") is not None else None,
                 tbl, ent, aug.get("module"), aug.get("object"), json.dumps(v)))
            obj_id = cur.lastrowid
            counts["objects"] += 1
            # OID conflict tracking (same OID, different symbol)
            owner = oid_owner.get(oid)
            if owner and owner.split("::", 1)[1] != name:
                conflicts.append({"oid": oid, "a": owner, "b": f"{mod}::{name}"})
            else:
                oid_owner.setdefault(oid, f"{mod}::{name}")
            enum = ((syntax.get("constraints") or {}).get("enumeration")
                    if isinstance(syntax.get("constraints"), dict) else None)
            labels = []
            if isinstance(enum, dict):
                for label, val in sorted(enum.items(), key=lambda kv: kv[1]):
                    cur.execute("INSERT INTO mib_enum_values(object_id,label,value) VALUES (?,?,?)",
                                (obj_id, label, int(val)))
                    labels.append(label)
                    counts["enums"] += 1
            cons = syntax.get("constraints") or {}
            for ckind in ("range", "size"):
                for r in cons.get(ckind, []) if isinstance(cons.get(ckind), list) else []:
                    if isinstance(r, dict):
                        cur.execute("INSERT INTO mib_ranges(object_id,kind,min,max) VALUES (?,?,?,?)",
                                    (obj_id, ckind, r.get("min"), r.get("max")))
                        counts["ranges"] += 1
            for pos, ix in enumerate(v.get("indices") or [], start=1):
                cur.execute("INSERT INTO mib_table_indexes(object_id,position,index_module,"
                            "index_object,implied) VALUES (?,?,?,?,?)",
                            (obj_id, pos, ix.get("module", mod), ix.get("object", ""),
                             int(ix.get("implied", 0))))
                counts["indexes"] += 1
            if aug:
                cur.execute("INSERT INTO mib_augments(object_id,base_module,base_object) VALUES (?,?,?)",
                            (obj_id, aug.get("module", mod), aug.get("object", "")))
                counts["augments"] += 1
            if kind == "notification":
                counts["notifications"] += 1
                for pos, ob in enumerate(v.get("objects") or [], start=1):
                    cur.execute("INSERT INTO mib_notification_objects(object_id,position,"
                                "payload_module,payload_object) VALUES (?,?,?,?)",
                                (obj_id, pos, ob.get("module", mod), ob.get("object", "")))
                    counts["notif_objects"] += 1
            words = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", name).replace("-", " ").replace("_", " ")
            cur.execute("INSERT INTO obj_fts(rowid,name,symbol_words,description,enum_labels) VALUES (?,?,?,?,?)",
                        (obj_id, f"{mod}::{name}", words, v.get("description") or "", " ".join(labels)))
    con.commit()
    report["counts"] = counts
    report["oid_conflicts"] = conflicts
    return counts, conflicts


SECTION_RE = re.compile(r"^## +(.+?)\s*$", re.M)
PAGES_RE = re.compile(r"\*\(p\.([\d\u2013-]+)\)\*")
REFDOC_FILES = ("verified-commands.md", "snmp-support.md", "known-limitations.md")
DS_META_RE = re.compile(r"<!-- datasheet product=(\S+) family=(\S+) kind=(\S+) source=(\S+) -->")


def _split_sections(body: str):
    """Split a markdown doc on level-2 headings; yields (section_title, chunk)."""
    marks = list(SECTION_RE.finditer(body))
    if not marks:
        yield "(whole document)", body
        return
    if marks[0].start() > 0:
        yield "(intro)", body[:marks[0].start()]
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(body)
        yield m.group(1).strip(), body[m.start():end]


def ingest_references(con: sqlite3.Connection, report: dict):
    """Phase 5: CLI-help jsonl + manual chapters + curated reference docs."""
    cur = con.cursor()
    counts = {"cli_help": 0, "manual_sections": 0, "reference_docs": 0, "families_cli": 0, "families_manual": 0,
              "datasheet_sections": 0, "products_datasheet": 0}

    def src_row(domain, family, path: Path) -> int:
        cur.execute("INSERT INTO knowledge_sources(domain,family,path,sha256) VALUES (?,?,?,?)",
                    (domain, family, str(path.relative_to(REPO)), sha256(path)))
        return cur.lastrowid

    # CLI help (canonical jsonl per family)
    for jf in sorted(REFS.glob("cli-help-*.jsonl")):
        family = jf.stem.removeprefix("cli-help-")
        sid = src_row("cli", family, jf)
        counts["families_cli"] += 1
        for line in jf.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            cur.execute("INSERT INTO cli_help(family,kind,context,prefix,body,source_id) "
                        "VALUES (?,?,?,?,?,?)",
                        (family, rec.get("kind", ""), rec.get("context", ""),
                         rec.get("prefix", ""), rec.get("text", ""), sid))
            cur.execute("INSERT INTO cli_fts(rowid,family,context,prefix,body) VALUES (?,?,?,?,?)",
                        (cur.lastrowid, family, rec.get("context", ""),
                         rec.get("prefix", ""), rec.get("text", "")))
            counts["cli_help"] += 1

    # Manuals (per-chapter markdown, split into level-2 sections)
    for mdir in sorted(REFS.glob("manual-*/")):
        family = mdir.name.removeprefix("manual-").rstrip("/\\")
        counts["families_manual"] += 1
        for ch in sorted(mdir.glob("*.md")):
            if ch.name == "manual-index.md":
                continue
            body = ch.read_text(encoding="utf-8", errors="replace")
            first = body.lstrip().splitlines()[0] if body.strip() else ""
            chapter = first.lstrip("# ").strip() or ch.stem
            sid = src_row("manual", family, ch)
            for section, chunk in _split_sections(body):
                pm = PAGES_RE.search(section)
                pages = pm.group(1) if pm else None
                clean = PAGES_RE.sub("", section).strip()
                cur.execute("INSERT INTO manual_sections(family,file,chapter,section,pages,body,source_id) "
                            "VALUES (?,?,?,?,?,?,?)",
                            (family, ch.name, chapter, clean, pages, chunk, sid))
                cur.execute("INSERT INTO manual_fts(rowid,family,chapter,section,body) VALUES (?,?,?,?,?)",
                            (cur.lastrowid, family, chapter, clean, chunk))
                counts["manual_sections"] += 1

    # Datasheets (one md per product; '##' subject sections; datasheet-map.yaml
    # provenance is baked into each file's meta comment by ingest_datasheet.py)
    dsdir = REFS / "datasheets"
    if dsdir.is_dir():
        for f in sorted(dsdir.glob("*.md")):
            if f.name == "datasheet-index.md":
                continue
            body = f.read_text(encoding="utf-8", errors="replace")
            m = DS_META_RE.search(body)
            product = m.group(1) if m else f.stem
            family = None if (not m or m.group(2) == "-") else m.group(2)
            kind = m.group(3) if m else "system"
            sid = src_row("datasheet", family, f)
            counts["products_datasheet"] += 1
            for section, chunk in _split_sections(body):
                pm = PAGES_RE.search(section)
                pages = pm.group(1) if pm else None
                clean = PAGES_RE.sub("", section).strip()
                cur.execute("INSERT INTO datasheet_sections(family,product,kind,file,section,pages,body,source_id) "
                            "VALUES (?,?,?,?,?,?,?,?)",
                            (family, product, kind, f.name, clean, pages, chunk, sid))
                cur.execute("INSERT INTO datasheet_fts(rowid,family,product,section,body) VALUES (?,?,?,?,?)",
                            (cur.lastrowid, family or "", product, clean, chunk))
                counts["datasheet_sections"] += 1

    # Curated reference docs (family-agnostic knowledge) + snmp capability maps
    doc_files = [REFS / n for n in REFDOC_FILES if (REFS / n).exists()]
    doc_files += sorted(REFS.glob("snmp-map-*.md"))
    for doc in doc_files:
        sid = src_row("refdoc", None, doc)
        body = doc.read_text(encoding="utf-8", errors="replace")
        for section, chunk in _split_sections(body):
            cur.execute("INSERT INTO reference_docs(name,section,body,source_id) VALUES (?,?,?,?)",
                        (doc.name, section, chunk, sid))
            cur.execute("INSERT INTO refdoc_fts(rowid,name,section,body) VALUES (?,?,?,?)",
                        (cur.lastrowid, doc.name, section, chunk))
            counts["reference_docs"] += 1

    con.commit()
    report["reference_counts"] = counts
    return counts


def seed_evidence(con: sqlite3.Connection):
    cur = con.cursor()
    for fam, vv, vc, cm, rs, bulk, eov in FAMILY_PROFILES:
        cur.execute("INSERT INTO family_snmp_profile VALUES (?,?,?,?,?,?,?,?)",
                    (fam, vv, vc, cm, rs, bulk, eov, PROFILE_PROVENANCE))
    for run in CAPABILITY_RUNS:
        cur.execute("INSERT INTO capability_runs VALUES (?,?,?,?,?)", run)
    for fam, dev, oid, subj, obs in PROBE_OBSERVATIONS:
        cur.execute("INSERT INTO capability_observations VALUES (?,?,?,?,?,?,?,?)",
                    ("run-2026-07-16-probe", fam, dev, oid, subj, obs, "supported", "live-snmp"))
    for fam, dev, oid, subj, obs in WALK_OBSERVATIONS:
        cur.execute("INSERT INTO capability_observations VALUES (?,?,?,?,?,?,?,?)",
                    ("run-2026-07-16-walk", fam, dev, oid, subj, obs, "supported", "live-snmp"))
    con.commit()


def validate(con: sqlite3.Connection, report: dict, strict: bool):
    cur = con.cursor()
    problems = []
    assert cur.execute("PRAGMA integrity_check").fetchone()[0] == "ok", "sqlite integrity"
    fk = cur.execute("PRAGMA foreign_key_check").fetchall()
    if fk:
        problems.append(f"foreign key violations: {len(fk)}")
    # fixtures (MIB-specific)
    fixture_results = []
    mib_objects = cur.execute("SELECT count(*) FROM mib_objects").fetchone()[0]
    report["mib_objects"] = mib_objects
    if mib_objects > 0:
        for mod, sym, checks in FIXTURES:
            row = cur.execute("SELECT id,oid,kind FROM mib_objects WHERE module=? AND symbol=?",
                              (mod, sym)).fetchone()
            errs = []
            if not row:
                errs.append("MISSING")
            else:
                obj_id, oid, kind = row
                if "oid" in checks and oid != checks["oid"]:
                    errs.append(f"oid {oid} != {checks['oid']}")
                if "kind" in checks and kind != checks["kind"]:
                    errs.append(f"kind {kind} != {checks['kind']}")
                if "enum" in checks:
                    got = dict(cur.execute("SELECT label,value FROM mib_enum_values WHERE object_id=?",
                                           (obj_id,)).fetchall())
                    for lbl, val in checks["enum"].items():
                        if got.get(lbl) != val:
                            errs.append(f"enum {lbl}={got.get(lbl)} != {val}")
                if "index0" in checks:
                    got = cur.execute("SELECT index_object FROM mib_table_indexes WHERE object_id=? "
                                      "ORDER BY position LIMIT 1", (obj_id,)).fetchone()
                    if not got or got[0] != checks["index0"]:
                        errs.append(f"index0 {got} != {checks['index0']}")
                if "augments" in checks:
                    got = cur.execute("SELECT base_module,base_object FROM mib_augments WHERE object_id=?",
                                      (obj_id,)).fetchone()
                    if tuple(got or ()) != checks["augments"]:
                        errs.append(f"augments {got} != {checks['augments']}")
                if "payload_len_min" in checks:
                    n = cur.execute("SELECT count(*) FROM mib_notification_objects WHERE object_id=?",
                                    (obj_id,)).fetchone()[0]
                    if n < checks["payload_len_min"]:
                        errs.append(f"payload {n} < {checks['payload_len_min']}")
            fixture_results.append({"fixture": f"{mod}::{sym}", "ok": not errs, "errors": errs})
            if errs:
                problems.append(f"fixture {mod}::{sym}: {errs}")
    else:
        report["mib_validation_skipped"] = True
    report["fixtures"] = fixture_results
    # Phase 5 fixtures: every family carries CLI + manual knowledge, and two
    # known lookups answer.
    fams = [r[0] for r in cur.execute("SELECT DISTINCT family FROM cli_help")]
    for fam in fams:
        n = cur.execute("SELECT count(*) FROM cli_help WHERE family=?", (fam,)).fetchone()[0]
        if n < 50:
            problems.append(f"phase5: cli_help for {fam} suspiciously small ({n})")
    man_fams = [r[0] for r in cur.execute("SELECT DISTINCT family FROM manual_sections")]
    missing_man = set(fams) - set(man_fams)
    if missing_man:
        problems.append(f"phase5: families with CLI but no manual sections: {sorted(missing_man)}")
    if not cur.execute('SELECT 1 FROM cli_fts WHERE cli_fts MATCH ? LIMIT 1', ('"static-route"',)).fetchone():
        problems.append("phase5: cli_fts lookup 'static-route' returned nothing")
    if not cur.execute('SELECT 1 FROM manual_fts WHERE manual_fts MATCH ? LIMIT 1', ('"zero" "touch"',)).fetchone():
        problems.append("phase5: manual_fts lookup 'zero touch' returned nothing")
    # Datasheet fixtures (only when the datasheet layer has been ingested)
    ds_products = cur.execute("SELECT count(DISTINCT product) FROM datasheet_sections").fetchone()[0]
    if ds_products:
        if not cur.execute('SELECT 1 FROM datasheet_fts WHERE datasheet_fts MATCH ? LIMIT 1',
                           ('"teleprotection"',)).fetchone():
            problems.append("datasheets: fts lookup 'teleprotection' (TP card) returned nothing")
        if not cur.execute("SELECT 1 FROM datasheet_sections WHERE family='mp4100' AND kind='card' LIMIT 1").fetchone():
            problems.append("datasheets: no mp4100 card sections (expected ~19 card datasheets)")
    report["phase5_fixtures"] = {"cli_families": sorted(fams), "manual_families": sorted(man_fams),
                                 "datasheet_products": ds_products}
    # MIB FTS smoke (only when MIB objects exist)
    if mib_objects > 0:
        hits = cur.execute("SELECT count(*) FROM obj_fts WHERE obj_fts MATCH 'ring protection'").fetchone()[0]
        report["fts_smoke_hits"] = hits
        if hits == 0:
            problems.append("FTS smoke query returned 0 rows")
    else:
        report["fts_smoke_hits"] = 0
    # conflicts policy
    n_conf = len(report.get("oid_conflicts", []))
    if n_conf and strict:
        problems.append(f"{n_conf} OID conflicts (strict mode)")
    report["validation_problems"] = problems
    return problems


def compat_map(con: sqlite3.Connection, report: dict, current_path: Path, out_path: Path, apply: bool):
    cur = con.cursor()
    rows = cur.execute("SELECT oid, name FROM mib_objects WHERE oid IS NOT NULL "
                       "ORDER BY module, symbol").fetchall()
    old = {}
    if current_path.exists():
        old = {k: v for k, v in json.loads(current_path.read_text(encoding="utf-8")).items()
               if not k.startswith("_")}
    # Stability-first tie-break: a compatibility map should not re-attribute a
    # shared OID to a different module between builds. When several modules
    # name the same OID, keep the previously published name if it is still a
    # valid candidate; otherwise take the deterministic (sorted) first.
    candidates: dict[str, list] = {}
    for oid, name in rows:
        candidates.setdefault(oid, []).append(name)
    newmap = {}
    for oid, names in candidates.items():
        prev = old.get(oid)
        newmap[oid] = prev if prev in names else names[0]
    added = sorted(set(newmap) - set(old), key=oid_key)
    removed = sorted(set(old) - set(newmap), key=oid_key)
    changed = sorted((k for k in set(old) & set(newmap) if old[k] != newmap[k]), key=oid_key)
    report["compat_diff"] = {
        "old_count": len(old), "new_count": len(newmap),
        "added": len(added), "removed": len(removed), "changed": len(changed),
        "added_sample": [f"{k} -> {newmap[k]}" for k in added[:20]],
        "removed_sample": [f"{k} ({old[k]})" for k in removed[:20]],
        "changed_sample": [f"{k}: {old[k]} -> {newmap[k]}" for k in changed[:20]],
    }
    meta = {"_meta": {
        "source": "regenerated from rad-knowledge.sqlite (build_knowledge_catalog.py, Phase 2)",
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "objects": len(newmap)}}
    payload = {**meta, **{k: newmap[k] for k in sorted(newmap, key=oid_key)}}
    out_path.write_text(json.dumps(payload, indent=0), encoding="utf-8")
    if apply:
        shutil.copyfile(out_path, current_path)
    return report["compat_diff"]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mib-root", action="append", default=[],
                    help='optional, e.g. "MIBs2:priority=200" (repo-relative). '
                         'When omitted, build a baseline catalog with CLI/manual/datasheet/refdoc data only.')
    ap.add_argument("--output", default=str(RAD / "build" / "rad-knowledge.sqlite"))
    ap.add_argument("--report", default=str(RAD / "build" / "mib-catalog-report.json"))
    ap.add_argument("--work", default=str(RAD / "build" / "work"))
    ap.add_argument("--apply-compat", action="store_true",
                    help="replace references/snmp-oid-map.json with the regenerated map")
    ap.add_argument("--strict", action="store_true", help="OID conflicts fail the build")
    args = ap.parse_args()

    roots = []
    for spec in args.mib_root:
        path, _, prio = spec.partition(":priority=")
        roots.append((REPO / path, int(prio or 100)))
    report = {"build_started": datetime.now(timezone.utc).isoformat(),
              "python": sys.version.split()[0],
              "sqlite": sqlite3.sqlite_version,
              "roots": [{"path": str(r), "priority": p} for r, p in roots]}

    work = Path(args.work)
    if work.exists():
        shutil.rmtree(work)
    stage, jout = work / "stage", work / "json"

    selected, files_seen = select_sources(roots, report)
    corpus_hash = hashlib.sha256("".join(sorted(f["sha256"] for f in files_seen if f["selected"]))
                                 .encode()).hexdigest()
    report["corpus_sha256"] = corpus_hash
    print(f"selected {len(selected)} modules "
          f"({sum(1 for f in files_seen if not f['selected'])} shadowed/skipped files)")
    if not roots:
        print("no --mib-root provided: building baseline catalog without MIB semantic content")

    status = compile_modules(selected, stage, jout, report)
    print(f"compiled {report['modules_compiled']} modules "
          f"({len(report['modules_failed'])} failed)")

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(suffix=".sqlite", dir=str(out.parent))
    os.close(fd)                       # Windows: keep no open handle on the temp file
    tmp = Path(tmp_name)
    con = None
    try:
        con = sqlite3.connect(tmp)
        con.executescript(SCHEMA)
        counts, conflicts = normalize(jout, selected, status, con, report)
        ref_counts = ingest_references(con, report)
        print(f"references ingested: {ref_counts}")
        seed_evidence(con)
        print(f"normalized: {counts} | oid conflicts: {len(conflicts)}")
        problems = validate(con, report, args.strict)
        # meta
        cur = con.cursor()
        for k, v in [("schema_version", "1"), ("corpus_sha256", corpus_hash),
                     ("built_at", report["build_started"]),
                     ("pysmi", report["pysmi_version"]),
                     ("objects", str(counts["objects"]))]:
            cur.execute("INSERT INTO catalog_meta VALUES (?,?)", (k, v))
        con.commit()
        diff = compat_map(con, report,
                          REFS / "snmp-oid-map.json",
                          out.parent / "snmp-oid-map.generated.json", args.apply_compat)
        print(f"compat map: old={diff['old_count']} new={diff['new_count']} "
              f"added={diff['added']} removed={diff['removed']} changed={diff['changed']}")
        con.close(); con = None
        report["result"] = "FAIL" if problems else "OK"
        Path(args.report).write_text(json.dumps(report, indent=1), encoding="utf-8")
        if problems:
            print("BUILD FAILED — previous database left untouched:")
            for prob in problems:
                print("  -", prob)
            sys.exit(1)
        if out.exists():
            out.unlink()               # Windows: move can't overwrite
        shutil.move(str(tmp), out)
        db_hash = sha256(out)
        print(f"OK -> {out} ({out.stat().st_size // 1024} KB, sha256 {db_hash[:16]}...)")
        print(f"report -> {args.report}")
    finally:
        if con is not None:
            con.close()
        tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
