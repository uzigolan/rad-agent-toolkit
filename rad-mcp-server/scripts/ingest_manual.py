"""Ingest a RAD user-manual PDF into the skill's manual reference layer.

Splits the PDF along its TOC bookmarks into per-chapter, grep-able markdown
under skills/rad-cli-operations/references/manual-<family>/, plus an index
file that lists every chapter/section and cross-links CLI topics to chapters.
The harvested CLI references are NEVER touched — the manual is a companion
layer (syntax lives in cli-reference-<family>.md; meaning lives here).

Re-runnable: drop a newer manual PDF, run again, the directory is rewritten.

Usage (server venv python):
  python scripts/ingest_manual.py <pdf-path> <family>
  python scripts/ingest_manual.py ETX-1p_6.4_Mn_05-26_GA.pdf etx1p
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

import fitz  # pymupdf

REPO = Path(__file__).resolve().parents[1]
REFERENCE_DIR = REPO / "skills" / "rad-cli-operations" / "references"

# Front/back matter chapters we skip entirely (no operational value).
SKIP_TITLES = re.compile(
    r"front cover|back cover|regulatory|declaration of conformity|"
    r"environmental compliance|^contents|drilling template|rack installation",
    re.IGNORECASE,
)

# Some manuals (e.g. ETX-2i) are organized as a few huge "parts" (1000+ pages)
# rather than per-topic chapters (~150-190 pages, per SecFlow/ETX-1p) — the
# real topics sit several TOC levels deeper. EXPAND_MIN_PAGES sits safely
# above SecFlow/ETX-1p's largest natural chapter (~184pp) so those manuals are
# untouched; anything bigger AND with enough children gets split on the next
# TOC level instead, recursively, until units are chapter-sized.
EXPAND_MIN_PAGES = 220
EXPAND_MIN_CHILDREN = 3
MAX_TOC_LEVEL = 6

# CLI topics -> keywords to find in section titles (for the cross-link index).
TOPIC_KEYWORDS = {
    "configure system mqtt": ["mqtt"],
    "configure crypto / pki / certificates": ["certificat", "pki", "public key", "crypto"],
    "configure crypto (IPsec/IKE)": ["ipsec", "ike"],
    "configure router (routing, static routes)": ["routing", "static route", "router"],
    "configure router bgp": ["bgp"],
    "configure router ospf": ["ospf"],
    "configure port ethernet / vlan": ["ethernet", "vlan"],
    "configure port cellular (LTE)": ["cellular", "lte", "sim"],
    "configure port wifi-client / wlan": ["wifi", "wlan"],
    "LoRa gateway": ["lora"],
    "configure system opcua-server": ["opc"],
    "configure system modbus-unit": ["modbus"],
    "configure management snmp": ["snmp"],
    "configure management (users, AAA, tacacs+)": ["user", "aaa", "tacacs", "radius", "authentication"],
    "NETCONF / YANG": ["netconf", "yang"],
    "configure reporting (alarms, syslog)": ["alarm", "syslog", "log"],
    "configure system date-and-time / ntp": ["ntp", "date and time", "clock"],
    "configure qos": ["qos", "quality of service", "shaper", "queue"],
    "configure protection erp": ["erp", "ring protection", "resiliency"],
    "configure oam": ["oam"],
    "access-control / firewall": ["firewall", "access control", "acl"],
    "dhcp": ["dhcp"],
    "admin software / file (upgrade, backup)": ["software upgrade", "file system", "backup", "installation"],
}


def slugify(title: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:60]


def clean_page_text(text: str, product: str, chapter_title: str) -> str:
    """Strip per-page running headers/footers and normalize bullets."""
    lines = text.splitlines()
    out = []
    for i, line in enumerate(lines):
        s = line.strip()
        if i < 4:  # running header zone: product name, chapter title, page no
            if not s or s == product or s.isdigit():
                continue
            if chapter_title and chapter_title.lower().startswith(s.lower().rstrip(". ")):
                continue
            if re.fullmatch(r"\d+\.?\s+" + re.escape(chapter_title[:20]) + r".*", s, re.IGNORECASE):
                continue
        out.append(line.replace("", "-").replace("�", "-"))
    return "\n".join(out)


def split_units(toc: list, page_count: int) -> list[tuple[str, int, int, int]]:
    """Adaptively split the TOC into chapter-sized (title, start, end, level)
    units. A unit expands into its next-level children when it's oversized
    AND has enough of them; otherwise it's a leaf — its own next-level
    children (if any) become '##' sections inside that single file."""
    lvl1 = [(t.strip(), p) for lvl, t, p in toc if lvl == 1]
    units: list[tuple[str, int, int, int]] = []

    def children_at(level: int, start: int, end: int) -> list[tuple[str, int]]:
        return [(t.strip(), p) for lvl, t, p in toc if lvl == level and start <= p <= end]

    def process(title: str, start: int, end: int, level: int) -> None:
        kids = children_at(level + 1, start, end) if level < MAX_TOC_LEVEL else []
        if (end - start + 1) > EXPAND_MIN_PAGES and len(kids) >= EXPAND_MIN_CHILDREN:
            for j, (ctitle, cpage) in enumerate(kids):
                cend = kids[j + 1][1] - 1 if j + 1 < len(kids) else end
                process(f"{title} – {ctitle}", cpage, cend, level + 1)
        else:
            units.append((title, start, end, level))

    for i, (title, page) in enumerate(lvl1):
        if SKIP_TITLES.search(title):
            continue
        end = lvl1[i + 1][1] - 1 if i + 1 < len(lvl1) else page_count
        process(title, page, end, 1)
    return units


def ingest(pdf_path: Path, family: str) -> None:
    doc = fitz.open(pdf_path)
    toc = doc.get_toc()
    product = doc.metadata.get("title") or pdf_path.stem.split("_")[0]
    product = product.strip() or "ETX-1p"

    out_dir = REFERENCE_DIR / f"manual-{family}"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    units = split_units(toc, doc.page_count)
    chapters = []  # (title, start_page, end_page, sections, sections_level)
    for title, start, end, level in units:
        sections = [(t.strip(), p) for lvl, t, p in toc
                    if lvl == level + 1 and start <= p <= end]
        chapters.append((title, start, end, sections, level + 1))

    index_lines = [
        f"# {product} user manual — chapter index (family: {family})",
        "",
        f"Extracted from `{pdf_path.name}` by scripts/ingest_manual.py.",
        "COMPANION to the harvested CLI reference: syntax questions -> "
        f"cli-reference-{family}.md; concepts, procedures, limits, alarm",
        "meanings -> the chapter files below. Grep a chapter file for the",
        "topic, or start from the cross-link table.",
        "",
        "| Chapter file | Pages | Sections |",
        "|---|---|---|",
    ]

    all_sections = []  # (title, chapter_slug) for topic mapping
    for n, (title, start, end, sections, sec_level) in enumerate(chapters, 1):
        slug = f"{n:02d}-{slugify(title)}"
        fname = f"{slug}.md"
        parts = [f"# {title}", "",
                 f"*Manual `{pdf_path.name}`, pages {start}–{end}.*", ""]
        # section boundaries at page granularity
        bounds = [(t, p) for t, p in sections] or [(title, start)]
        if bounds[0][1] > start:  # chapter intro before first section
            bounds.insert(0, ("(chapter introduction)", start))
        for j, (stitle, spage) in enumerate(bounds):
            send = bounds[j + 1][1] - 1 if j + 1 < len(bounds) else end
            parts.append(f"\n## {stitle}  *(p.{spage})*\n")
            for pno in range(spage - 1, min(send, doc.page_count)):
                parts.append(clean_page_text(doc[pno].get_text(), product, title))
            all_sections.append((stitle, slug))
        # Cross-link matching also needs titles BELOW this chapter's section
        # level — some manuals nest the real topics (MQTT, PKI, ...) deeper
        # than the level used for '##' headers, where they'd never match a
        # topic keyword on their own. Body rendering stays at sec_level;
        # this only enriches the cross-link source pool.
        deep = [(t.strip(), p) for lvl, t, p in toc if lvl > sec_level and start <= p <= end]
        all_sections.extend((t, slug) for t, p in deep)
        (out_dir / fname).write_text("\n".join(parts), encoding="utf-8")
        sec_names = "; ".join(t for t, _ in sections[:8]) + ("; ..." if len(sections) > 8 else "")
        index_lines.append(f"| `{fname}` | {start}–{end} | {sec_names} |")
        print(f"  {fname}  (pages {start}-{end}, {len(sections)} sections)")

    # CLI-topic cross-links
    index_lines += ["", "## CLI topic -> manual chapter cross-links", "",
                    "| CLI area | Manual sections (chapter file) |", "|---|---|"]
    for topic, keywords in TOPIC_KEYWORDS.items():
        hits = []
        for stitle, slug in all_sections:
            low = stitle.lower()
            if any(k in low for k in keywords):
                hits.append(f"{stitle} (`{slug}.md`)")
        if hits:
            shown = "; ".join(hits[:4]) + ("; ..." if len(hits) > 4 else "")
            index_lines.append(f"| {topic} | {shown} |")

    (out_dir / "manual-index.md").write_text("\n".join(index_lines), encoding="utf-8")
    total = sum(f.stat().st_size for f in out_dir.glob("*.md"))
    print(f"\nDone: {len(chapters)} chapters + manual-index.md -> {out_dir} "
          f"({total/1024:.0f} KB markdown)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    ingest(Path(sys.argv[1]).resolve(), sys.argv[2])
