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

NOTE: the layout parser (y-ordered lines, bold headings, gap-based row
grouping) was tuned against the RADview SP 7.2.3 (v6e) document structure;
review the jsonl after the first run on each new document vintage (parse
fallbacks degrade to section-level records, never silently drop content).

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
from collections import Counter
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
                r"limitations?\s+introduced|^new\s+limitations?\b", re.I), "known-new"),
    (re.compile(r"solved|fixed|resolved|corrected", re.I), "solved"),
    (re.compile(r"known\s+(limitation|issue|problem)|open\s+issues", re.I), "known"),
    (re.compile(r"new\s+feature|enhancement|what'?s\s+new", re.I), "feature"),
    (re.compile(r"compatib|interoperab|supported\s+(version|platform|device|agent)|"
                r"requirement", re.I), "compatibility"),
    (re.compile(r"upgrade|install|migration", re.I), "upgrade"),
]

# Only an explicit TRS prefix keys a record — bare 4-7 digit numbers are
# phone numbers, ZIP codes and years in these documents.
TRS_RE = re.compile(r"\bTRS[-\s]?(\d{3,7})\b", re.I)
VERSION_RE = re.compile(r"\b(\d+\.\d+(?:\.\d+)?(?:\.\d+)?)\b")
NOISE_RE = re.compile(
    r"^(release notes?|page \d+( of \d+)?|www\.rad\.com.*|"
    r".*all rights reserved.*|the access company|\d{1,3})$", re.I)
# End-matter boilerplate (contact block, legal, RADcare portal how-to):
# from the first match onward, content is discarded until a real heading.
SKIP_RE = re.compile(
    r"headquarters|\u00a9\s*\d{4}|copyright|all rights reserved|"
    r"publication no|radcare online|www\.rad\.com", re.I)
RELEASED_RE = re.compile(
    r"(January|February|March|April|May|June|July|August|September|"
    r"October|November|December)\s+\d{1,2},\s+\d{4}")


def classify_heading(text: str) -> str | None:
    for rx, section in HEADING_MAP:
        if rx.search(text):
            return section
    return None


def page_lines(page) -> list[tuple]:
    """(text, size, bold, y, x, rect) per visual line."""
    out = []
    for block in page.get_text("dict").get("blocks", []):
        for line in block.get("lines", []):
            spans = line.get("spans", [])
            text = "".join(s.get("text", "") for s in spans).strip()
            if not text:
                continue
            size = max((s.get("size", 0.0) for s in spans), default=0.0)
            bold = any("bold" in s.get("font", "").lower() for s in spans)
            rect = fitz.Rect(line["bbox"])
            out.append((text, round(size, 1), bold, rect.y0, rect.x0, rect))
    return out


def guess_meta(doc) -> dict:
    """Best-effort product/version/date guess off page 1; CLI args override."""
    first = " ".join(l[0] for l in page_lines(doc[0]))
    meta: dict = {}
    vm = VERSION_RE.search(first)
    if vm:
        meta["version"] = vm.group(1)
    dm = RELEASED_RE.search(first)
    if dm:
        meta["released"] = dm.group(0)
    if re.search(r"radview", first, re.I):
        meta.setdefault("product", "radview")
        meta.setdefault("product_kind", "nms")
    return meta


# groups made only of table column-header words are layout junk, not items
HEADER_JUNK_RE = re.compile(
    r"^(category|limitation|comments?|description|trs|id|notes?|status|"
    r"severity|[\s|]+)+$", re.I)


def _row_groups(buf: list[tuple[int, float, str]]) -> list[list[tuple[int, float, str]]]:
    """Group section lines back into visual table rows by vertical gaps.
    pymupdf's find_tables is unreliable on these documents (it fragments
    wrapped rows or sees only the header row), but reading order sorted by
    (y, x) is row-major and row boundaries show up as larger y-gaps."""
    diffs = [b[1] - a[1] for a, b in zip(buf, buf[1:])
             if b[0] == a[0] and b[1] - a[1] > 1]
    med = sorted(diffs)[len(diffs) // 2] if diffs else 0.0
    thresh = max(med * 1.45, 8.0)
    groups: list[list] = [[buf[0]]]
    for prev, line in zip(buf, buf[1:]):
        if line[0] != prev[0] or (line[1] - prev[1]) > thresh:
            groups.append([])
        groups[-1].append(line)
    return groups


def parse_pdf(pdf: Path) -> tuple[dict, list[dict]]:
    doc = fitz.open(pdf)
    meta = guess_meta(doc)

    per_page = [page_lines(p) for p in doc]
    # running headers/footers: whole lines repeated on several pages
    counts: Counter = Counter()
    for lines in per_page:
        counts.update({l[0].casefold() for l in lines})
    boiler = {t for t, c in counts.items()
              if c >= min(3, len(per_page)) and len(t) < 80}

    items: list[dict] = []
    section = "other"
    pending: list[tuple[int, float, str]] = []  # (page, y, text)

    def flush():
        nonlocal pending
        buf, pending = pending, []
        if section == "_skip" or not buf:
            return
        if section in ("solved", "known", "known-new"):
            for group in _row_groups(buf):
                text = "\n".join(t for _, _, t in group).strip()
                if not text or HEADER_JUNK_RE.match(re.sub(r"\s+", " ", text)):
                    continue
                m = TRS_RE.search(text)
                items.append({"section": section,
                              "trs": f"TRS-{m.group(1)}" if m else None,
                              "title": re.sub(r"\s+", " ", text)[:160],
                              "body": text})
        else:
            text = "\n".join(t for _, _, t in buf).strip()
            if text:
                items.append({"section": section, "trs": None,
                              "title": f"{section} notes", "body": text})

    for pno in range(len(per_page)):
        for text, size, bold, y, x, rect in sorted(
                per_page[pno], key=lambda l: (l[3], l[4])):
            if text.casefold() in boiler or NOISE_RE.match(text):
                continue
            if SKIP_RE.search(text):
                flush()
                section = "_skip"
                continue
            if (bold or size >= 13) and len(text) < 60:
                new_sec = classify_heading(text)
                if new_sec and new_sec != section:
                    flush()
                    section = new_sec
                    continue
            if section != "_skip":
                pending.append((pno, y, text))
    flush()
    doc.close()
    return meta, items


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
    if opts.released:
        meta["released"] = opts.released
    meta.setdefault("released", None)

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
