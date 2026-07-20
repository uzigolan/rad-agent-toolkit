"""Ingest RAD product-datasheet PDFs into the skill's datasheet reference layer.

The datasheet layer is the THIRD knowledge domain beside the harvested CLI
reference (syntax) and the user manuals (concepts/procedures): hardware specs,
interfaces, ordering options and product variants live here. Each datasheet
becomes ONE markdown file split into '##' subject sections (features,
interfaces, timing, ordering, ...) under
skills/rad-cli-operations/references/datasheets/, plus datasheet-index.md.

Unlike manuals, datasheets carry no TOC bookmarks — section headings are
detected from font spans (lines rendered notably larger than body text).
Sheets whose fonts defeat detection fall back to per-page sections.

Which PDF maps to which family/product/kind is driven by the single-source
references/datasheet-map.yaml (classification read off each PDF's own
first-page banner, not filenames). Re-runnable: the output dir is rewritten.

Usage (server venv python):
  python scripts/ingest_datasheet.py --all            # everything in the map
  python scripts/ingest_datasheet.py asmi-54c         # one product (or pdf name)
"""
from __future__ import annotations

import re
import shutil
import sys
from collections import Counter
from pathlib import Path

import fitz  # pymupdf
import yaml

REPO = Path(__file__).resolve().parents[1]
PDF_DIR = REPO / "datasheets"
REFERENCE_DIR = REPO / "skills" / "rad-cli-operations" / "references"
MAP_PATH = REFERENCE_DIR / "datasheet-map.yaml"
OUT_DIR = REFERENCE_DIR / "datasheets"

# Heading candidates: bigger-than-body lines that read like section titles.
MIN_HEADING_DELTA = 1.3          # points above body size
MAX_HEADING_LEN = 70
MIN_SECTIONS_FOR_HEADINGS = 3    # fewer detected -> fall back to per-page split
MIN_SECTION_BODY = 120           # merge tiny sections into their predecessor

# Boilerplate lines that appear on every page (footer/banner noise).
NOISE_RE = re.compile(
    r"^(data ?sheet|product page ?>?|general availability|controlled availability|"
    r"the access company|www\.rad\.com.*|.*all rights reserved.*|"
    r"international headquarters.*|north america headquarters.*|\d{1,3})$",
    re.IGNORECASE,
)


def clean_line(line: str) -> str:
    return (line.replace("", "-").replace("", "-")
            .replace("•", "-").replace("�", "-").rstrip())


def page_lines(page) -> list[tuple[str, float, bool]]:
    """Flatten a page into (text, max_font_size, bold) per line, top-down."""
    out = []
    d = page.get_text("dict")
    for block in d.get("blocks", []):
        for line in block.get("lines", []):
            spans = line.get("spans", [])
            text = "".join(s.get("text", "") for s in spans).strip()
            if not text:
                continue
            size = max((s.get("size", 0.0) for s in spans), default=0.0)
            bold = any("bold" in (s.get("font", "").lower()) for s in spans)
            out.append((clean_line(text), round(size, 1), bold))
    return out


def body_font_size(pages_lines) -> float:
    sizes = Counter()
    for lines in pages_lines:
        for text, size, _ in lines:
            sizes[size] += len(text)
    return sizes.most_common(1)[0][0] if sizes else 10.0


def looks_like_heading(text: str, size: float, body: float) -> bool:
    if size - body < MIN_HEADING_DELTA:
        return False
    if not (2 < len(text) <= MAX_HEADING_LEN):
        return False
    if text.startswith(("-", "•")) or text.endswith((".", ",", ";", ":")):
        return False
    if NOISE_RE.match(text):
        return False
    if not re.search(r"[A-Za-z]{3}", text):
        return False
    return True


def extract_sections(doc) -> list[tuple[str, int, str]]:
    """Return [(section_title, start_page_1based, body_text)]. Heading-driven
    when the sheet's fonts allow it, else one section per page."""
    pages_lines = [page_lines(p) for p in doc]
    body = body_font_size(pages_lines)

    # a heading-sized line repeating on 2+ pages is a running banner (the
    # product headline re-rendered atop every page), not a section heading
    seen_on = Counter()
    for lines in pages_lines:
        page_heads = {t for t, s, _ in lines if looks_like_heading(t, s, body)}
        seen_on.update(page_heads)
    banners = {t for t, n in seen_on.items() if n >= 2 and len(t) > 15}

    sections: list[tuple[str, int, list[str]]] = []
    current = ("(overview)", 1, [])
    for pno, lines in enumerate(pages_lines, start=1):
        for text, size, bold in lines:
            if NOISE_RE.match(text) or (pno > 1 and text in banners):
                continue
            if looks_like_heading(text, size, body):
                # consecutive heading lines extend the title (wrapped headings)
                if not current[2] and current[0] != "(overview)":
                    current = (current[0] + " " + text, current[1], current[2])
                    continue
                sections.append(current)
                current = (text, pno, [])
            else:
                current[2].append(text)
    sections.append(current)
    sections = [(t, p, b) for t, p, b in sections if b]

    if len(sections) < MIN_SECTIONS_FOR_HEADINGS:
        # font detection failed (older Word-exported sheets) -> per-page
        sections = []
        for pno, lines in enumerate(pages_lines, start=1):
            keep = [t for t, _, _ in lines if not NOISE_RE.match(t)]
            if keep:
                sections.append((f"Page {pno}", pno, keep))

    # the page-1 headline repeats as a large-font running banner on later
    # pages and glues onto that page's first real heading — strip it
    if sections:
        banner = sections[0][0]
        if len(banner) > 15:
            fixed = [sections[0]]
            for title, pno, lines in sections[1:]:
                if title.startswith(banner):
                    rest = title[len(banner):].strip(" -–—")
                    title = rest or "(continued)"
                fixed.append((title, pno, lines))
            sections = fixed

    # merge tiny fragments into their predecessor
    merged: list[tuple[str, int, list[str]]] = []
    for title, pno, lines in sections:
        if merged and len(" ".join(lines)) < MIN_SECTION_BODY:
            merged[-1][2].extend([f"**{title}**"] + lines)
        else:
            merged.append((title, pno, list(lines)))
    return [(t, p, "\n".join(b)) for t, p, b in merged]


def load_map() -> list[dict]:
    doc = yaml.safe_load(MAP_PATH.read_text(encoding="utf-8"))
    entries = [e for e in doc.get("datasheets", []) if not e.get("skip")]
    if not entries:
        raise SystemExit(f"no active entries in {MAP_PATH}")
    return entries


def ingest_one(entry: dict) -> dict:
    pdf = PDF_DIR / entry["pdf"]
    doc = fitz.open(pdf)
    product, family = entry["product"], entry.get("family") or "-"
    kind, title = entry.get("kind", "system"), entry.get("title", product)

    parts = [
        f"# {title}",
        "",
        f"<!-- datasheet product={product} family={family} kind={kind} "
        f"source={entry['pdf']} -->",
        "",
        f"*Datasheet `{entry['pdf']}`, {doc.page_count} pages. "
        f"Product `{product}`, "
        + (f"family `{family}` ({kind})." if family != "-" else f"no inventory family ({kind})."),
    ]
    if entry.get("note"):
        parts.append(f"*Note: {entry['note']}*")
    sections = extract_sections(doc)
    for stitle, spage, body in sections:
        parts += [f"\n## {stitle}  *(p.{spage})*\n", body]
    out = OUT_DIR / f"{product}.md"
    out.write_text("\n".join(parts), encoding="utf-8")
    doc.close()
    return {"product": product, "family": family, "kind": kind,
            "file": out.name, "pages": doc.page_count if not doc.is_closed else "?",
            "sections": len(sections), "title": title, "pdf": entry["pdf"]}


def write_index(rows: list[dict]) -> None:
    lines = [
        "# RAD product datasheets — index",
        "",
        "Extracted from PDFs under `rad-mcp-server/datasheets/` (gitignored) by",
        "`scripts/ingest_datasheet.py`, driven by `datasheet-map.yaml`.",
        "THIRD knowledge domain: exact command syntax -> cli-reference;",
        "concepts/procedures -> manual-<family>/; hardware specs, interfaces,",
        "variants and ordering -> the files below. `kind=card` means a plug-in",
        "module for its family's chassis, not a standalone device.",
        "",
    ]
    by_fam: dict[str, list[dict]] = {}
    for r in rows:
        by_fam.setdefault(r["family"], []).append(r)
    order = sorted(by_fam, key=lambda f: (f == "-", f))
    for fam in order:
        label = f"Family `{fam}`" if fam != "-" else "No inventory family"
        lines += [f"## {label}", "", "| Product | Kind | File | Sections | Title |", "|---|---|---|---|---|"]
        for r in sorted(by_fam[fam], key=lambda r: (r["kind"] != "system", r["product"])):
            lines.append(f"| {r['product']} | {r['kind']} | `{r['file']}` "
                         f"| {r['sections']} | {r['title']} |")
        lines.append("")
    (OUT_DIR / "datasheet-index.md").write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str]) -> None:
    if len(argv) != 1:
        raise SystemExit(__doc__)
    entries = load_map()
    if argv[0] != "--all":
        key = argv[0].lower()
        picked = [e for e in entries
                  if e["product"].lower() == key or e["pdf"].lower() == key]
        if not picked:
            raise SystemExit(f"'{argv[0]}' matches no product/pdf in {MAP_PATH.name}")
        # single-product mode rewrites just that file; index rebuilt from all
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        for e in picked:
            r = ingest_one(e)
            print(f"  {r['file']}  ({r['sections']} sections, kind={r['kind']}, family={r['family']})")
        rows = [ingest_one(e) for e in entries]   # keep index consistent
        write_index(rows)
        return
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)
    rows, missing = [], []
    for e in entries:
        if not (PDF_DIR / e["pdf"]).exists():
            missing.append(e["pdf"])
            continue
        r = ingest_one(e)
        rows.append(r)
        print(f"  {r['file']:28s} {r['sections']:3d} sections  kind={r['kind']:9s} family={r['family']}")
    write_index(rows)
    total = sum(f.stat().st_size for f in OUT_DIR.glob("*.md"))
    print(f"\nDone: {len(rows)} datasheets + datasheet-index.md -> {OUT_DIR} "
          f"({total/1024:.0f} KB markdown)")
    if missing:
        print(f"WARNING: PDFs in the map but not on disk: {missing}")


if __name__ == "__main__":
    main(sys.argv[1:])
