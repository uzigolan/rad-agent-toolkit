"""Ingest RAD release-note PDFs into the release-notes knowledge layer.

Release notes are the FOURTH knowledge domain (CLI reference = syntax, manuals
= concepts/procedures, datasheets = hardware specs). What sets them apart is
that every fact is VERSION-SCOPED: a limitation is known in 7.2.2 and solved
in 7.2.3, and the natural queries are temporal ("was TRS-91234 fixed?", "what
is still broken in this release?", "upgrade path from 7.1?"). So ingestion is
row-per-item, not page-chunked: solved/known-limitation tables become one
record per TRS number; features/compatibility/upgrade sections become
section-level records.

Two product axes share the schema:
  * NMS release notes (RADview service packs)      -> --product-kind nms
  * device firmware release notes (per family)     -> --product-kind device --family etx2

Output: skills/rad-cli-operations/references/release-notes/
  rn-<product>-<version>.jsonl   first line = doc meta, then one item per line
  release-notes-index.md         human-readable roster

The jsonl is what scripts/build_knowledge_catalog.py ingests into the
`release_notes` table (+ rn_fts) that release_notes_search answers from.

NOTE: the table/heading parser was written from the RADview SP 7.2.3 (v6e)
document structure and verified against a synthetic fixture; review the jsonl
after the first run on each new document vintage (parse fallbacks degrade to
section-level records, never silently drop content).

Usage (server venv python):
  python scripts/ingest_release_notes.py "release-notes/RADview_SP_7.2.3.pdf" \
      --product radview --product-kind nms --version 7.2.3 --doc-rev v6e
  python scripts/ingest_release_notes.py <pdf> --product etx2 \
      --product-kind device --family etx2 --version 6.8.5
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import fitz  # pymupdf

REPO = Path(__file__).resolve().parents[1]
PDF_DIR = REPO / "release-notes"
REFERENCE_DIR = REPO / "skills" / "rad-cli-operations" / "references"
OUT_DIR = REFERENCE_DIR / "release-notes"

# Canonical section vocabulary (the schema's `section` column).
SECTIONS = ("feature", "compatibility", "upgrade", "solved", "known-new",
            "known", "other")

# heading keyword -> canonical section; matched on candidate headings,
# most-specific first (a "new known limitations" heading must not hit "new").
HEADING_MAP = [
    (re.compile(r"new\s+known\s+limitation|known\s+limitations?\s+.*new|"
                r"limitations?\s+introduced", re.I), "known-new"),
    (re.compile(r"solved|fixed|resolved|corrected", re.I), "solved"),
    (re.compile(r"known\s+(limitation|issue|problem)|open\s+issues", re.I), "known"),
    (re.compile(r"new\s+feature|enhancement|what'?s\s+new", re.I), "feature"),
    (re.compile(r"compatib|interoperab|supported\s+(version|platform|device|agent)|"
                r"requirement", re.I), "compatibility"),
    (re.compile(r"upgrade|installation|migration", re.I), "upgrade"),
]

TRS_RE = re.compile(r"\b(?:TRS[-\s]?)?(\d{4,7})\b")
VERSION_RE = re.compile(r"\b(\d+\.\d+(?:\.\d+)?(?:\.\d+)?)\b")
NOISE_RE = re.compile(
    r"^(release notes?|page \d+( of \d+)?|www\.rad\.com.*|"
    r".*all rights reserved.*|the access company|\d{1,3})$", re.I)


def classify_heading(text: str) -> str | None:
    for rx, section in HEADING_MAP:
        if rx.search(text):
            return section
    return None


def page_lines(page) -> list[tuple[str, float, bool]]:
    out = []
    for block in page.get_text("dict").get("blocks", []):
        for line in block.get("lines", []):
            spans = line.get("spans", [])
            text = "".join(s.get("text", "") for s in spans).strip()
            if not text:
                continue
            size = max((s.get("size", 0.0) for s in spans), default=0.0)
            bold = any("bold" in s.get("font", "").lower() for s in spans)
            out.append((text, round(size, 1), bold))
    return out


def guess_meta(doc) -> dict:
    """Best-effort product/version guess off page 1; CLI args override."""
    first = " ".join(t for t, _, _ in page_lines(doc[0]))
    meta: dict = {}
    vm = VERSION_RE.search(first)
    if vm:
        meta["version"] = vm.group(1)
    if re.search(r"radview", first, re.I):
        meta.setdefault("product", "radview")
        meta.setdefault("product_kind", "nms")
    return meta


def _table_records(table, section: str) -> list[dict]:
    """One record per data row of a TRS-style table. Header row picks the ID
    and description columns; rows without a TRS still become records."""
    rows = table.extract()
    if not rows or len(rows) < 2:
        return []
    header = [(c or "").strip().lower() for c in rows[0]]
    trs_col = next((i for i, h in enumerate(header)
                    if re.search(r"\btrs\b|\bid\b|number", h)), None)
    desc_col = next((i for i, h in enumerate(header)
                     if re.search(r"desc|limitation|problem|feature|issue|detail", h)),
                    None)
    recs = []
    for row in rows[1:]:
        cells = [(c or "").strip() for c in row]
        if not any(cells):
            continue
        trs = None
        if trs_col is not None and cells[trs_col:trs_col + 1]:
            m = TRS_RE.search(cells[trs_col])
            trs = f"TRS-{m.group(1)}" if m else None
        body_cells = [f"{header[i] or f'col{i}'}: {c}"
                      for i, c in enumerate(cells) if c]
        body = "\n".join(body_cells)
        title_src = (cells[desc_col] if desc_col is not None and desc_col < len(cells)
                     and cells[desc_col] else body)
        title = re.sub(r"\s+", " ", title_src)[:160]
        recs.append({"section": section, "trs": trs, "title": title, "body": body})
    return recs


def parse_pdf(pdf: Path) -> tuple[dict, list[dict]]:
    doc = fitz.open(pdf)
    meta = guess_meta(doc)
    items: list[dict] = []
    section = "other"
    pending_text: dict[str, list[str]] = {}

    def flush(sec: str):
        text = "\n".join(pending_text.pop(sec, [])).strip()
        if text:
            items.append({"section": sec, "trs": None,
                          "title": f"{sec} notes", "body": text})

    for page in doc:
        # tables first: their bboxes let us drop table text from the prose flow
        table_bboxes = []
        try:
            for t in page.find_tables():
                table_bboxes.append(fitz.Rect(t.bbox))
                recs = _table_records(t, section)
                items.extend(recs)
        except Exception:
            pass  # table detection is best-effort; prose fallback still runs

        for block in page.get_text("dict").get("blocks", []):
            r = fitz.Rect(block.get("bbox", (0, 0, 0, 0)))
            if any(r.intersects(tb) for tb in table_bboxes):
                continue
            for line in block.get("lines", []):
                spans = line.get("spans", [])
                text = "".join(s.get("text", "") for s in spans).strip()
                if not text or NOISE_RE.match(text):
                    continue
                bold = any("bold" in s.get("font", "").lower() for s in spans)
                new_sec = classify_heading(text) if (bold or len(text) < 60) else None
                if new_sec and new_sec != section:
                    flush(section)
                    section = new_sec
                    continue
                pending_text.setdefault(section, []).append(text)
    flush(section)
    for sec in list(pending_text):
        flush(sec)
    doc.close()

    # prose in solved/known sections that escaped table detection: split per TRS
    refined: list[dict] = []
    for it in items:
        if it["trs"] is None and it["section"] in ("solved", "known", "known-new"):
            parts = _split_by_trs(it["body"])
            if len(parts) > 1:
                refined.extend({"section": it["section"], "trs": trs,
                                "title": re.sub(r"\s+", " ", body)[:160],
                                "body": body} for trs, body in parts)
                continue
        refined.append(it)
    return meta, refined


def _split_by_trs(text: str) -> list[tuple[str | None, str]]:
    marks = [(m.start(), f"TRS-{m.group(1)}") for m in TRS_RE.finditer(text)]
    if len(marks) < 2:
        return [(marks[0][1] if marks else None, text)]
    out = []
    for i, (pos, trs) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        out.append((trs, text[pos:end].strip()))
    return out


def write_outputs(meta: dict, items: list[dict], source_pdf: Path) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    slug = f"rn-{meta['product']}-{meta['version']}".replace(" ", "-").lower()
    out = OUT_DIR / f"{slug}.jsonl"
    with out.open("w", encoding="utf-8") as fh:
        fh.write(json.dumps({"kind": "meta", **meta,
                             "source_pdf": source_pdf.name}) + "\n")
        for it in items:
            fh.write(json.dumps(it, ensure_ascii=False) + "\n")
    _rebuild_index()
    return out


def _rebuild_index() -> None:
    lines = ["# Release-notes index",
             "",
             "Generated by scripts/ingest_release_notes.py — one jsonl per",
             "release-note document; first record is the doc meta, then one",
             "record per item (TRS-keyed for solved/known limitations).", ""]
    for jf in sorted(OUT_DIR.glob("rn-*.jsonl")):
        head = jf.read_text(encoding="utf-8").splitlines()
        meta = json.loads(head[0]) if head else {}
        n = max(0, len([l for l in head[1:] if l.strip()]))
        fam = f", family {meta['family']}" if meta.get("family") else ""
        lines.append(f"- `{jf.name}` — {meta.get('product', '?')} "
                     f"{meta.get('version', '?')} ({meta.get('product_kind', '?')}"
                     f"{fam}, doc rev {meta.get('doc_rev') or '-'}): {n} items")
    (OUT_DIR / "release-notes-index.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf", help="release-note PDF (path, or a name under "
                                f"{PDF_DIR})")
    ap.add_argument("--product", help="product slug, e.g. radview or etx2")
    ap.add_argument("--product-kind", choices=["nms", "device"], dest="product_kind")
    ap.add_argument("--family", default=None,
                    help="inventory family for device release notes")
    ap.add_argument("--version", help="release version, e.g. 7.2.3")
    ap.add_argument("--doc-rev", dest="doc_rev", default=None,
                    help="document revision, e.g. v6e")
    ap.add_argument("--released", default=None, help="release date if known")
    opts = ap.parse_args()

    pdf = Path(opts.pdf)
    if not pdf.exists():
        pdf = PDF_DIR / opts.pdf
    if not pdf.exists():
        print(f"PDF not found: {opts.pdf} (looked in {PDF_DIR} too)")
        return 1

    meta, items = parse_pdf(pdf)
    for key in ("product", "product_kind", "version"):
        if getattr(opts, key, None):
            meta[key] = getattr(opts, key)
        if not meta.get(key):
            print(f"cannot determine --{key.replace('_', '-')} from the PDF; "
                  "pass it explicitly")
            return 1
    meta["family"] = opts.family
    meta["doc_rev"] = opts.doc_rev
    meta["released"] = opts.released

    out = write_outputs(meta, items, pdf)
    by_sec: dict[str, int] = {}
    trs_count = 0
    for it in items:
        by_sec[it["section"]] = by_sec.get(it["section"], 0) + 1
        trs_count += 1 if it.get("trs") else 0
    print(f"wrote {out.relative_to(REPO)}: {len(items)} items "
          f"({trs_count} TRS-keyed) — " +
          ", ".join(f"{s}={n}" for s, n in sorted(by_sec.items())))
    print("REVIEW the jsonl (parser is document-vintage sensitive), then "
          "rebuild the catalog:\n  python scripts/build_knowledge_catalog.py "
          '--mib-root "MIBs2:priority=200" --mib-root "MIBS:priority=100"')
    return 0


if __name__ == "__main__":
    sys.exit(main())
