"""Ingest Altera PDF documentation into a repeatable reference layer.

Input (default):
  <workspace>/Altera/*.pdf

Output (rewritten on each run):
  skills/rad-cli-operations/references/altera-docs/
    <doc-slug>.md
        figures/<doc-slug>/*
    altera-index.md

Usage:
  python scripts/ingest_altera.py
  python scripts/ingest_altera.py --input-dir Altera
    python scripts/ingest_altera.py --no-figures
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
from pathlib import Path

import fitz  # pymupdf

REPO = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_DIR = REPO.parent / "Altera"
OUT_DIR = REPO / "skills" / "rad-cli-operations" / "references" / "altera-docs"


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:80]


def clean_page_text(text: str) -> str:
    lines = [ln.rstrip() for ln in text.splitlines()]
    # Drop repeated empty lines to keep markdown compact and grep-friendly.
    out: list[str] = []
    empty = False
    for ln in lines:
        if not ln.strip():
            if not empty:
                out.append("")
            empty = True
            continue
        empty = False
        out.append(ln.replace("\u2022", "- "))
    return "\n".join(out).strip()


def section_bounds(doc: fitz.Document) -> list[tuple[str, int, int]]:
    """Return (title, start_page_1based, end_page_1based) sections.

    Prefer level-1 TOC split. If TOC is missing, chunk pages in 20-page blocks.
    """
    toc = doc.get_toc()
    lvl1 = [(t.strip(), int(p)) for lvl, t, p in toc if lvl == 1 and int(p) >= 1]
    if lvl1:
        out: list[tuple[str, int, int]] = []
        for i, (title, start) in enumerate(lvl1):
            end = lvl1[i + 1][1] - 1 if i + 1 < len(lvl1) else doc.page_count
            if end < start:
                end = start
            out.append((title or f"Section {i + 1}", start, end))
        return out

    out = []
    step = 20
    page = 1
    idx = 1
    while page <= doc.page_count:
        end = min(page + step - 1, doc.page_count)
        out.append((f"Pages {page}-{end}", page, end))
        page = end + 1
        idx += 1
    return out


def extract_page_figures(
    doc: fitz.Document,
    page_idx: int,
    doc_slug: str,
    out_dir: Path,
    seen_hashes: dict[str, str],
) -> tuple[list[str], int]:
    """Extract page images and return markdown links plus new-file count."""
    links: list[str] = []
    created = 0
    assets_dir = out_dir / "figures" / doc_slug
    assets_dir.mkdir(parents=True, exist_ok=True)

    page = doc[page_idx]
    page_images = page.get_images(full=True)
    for i, img in enumerate(page_images, start=1):
        xref = img[0]
        try:
            data = doc.extract_image(xref)
        except Exception:
            continue

        blob = data.get("image")
        if not blob:
            continue
        ext = (data.get("ext") or "png").lower()
        digest = hashlib.sha256(blob).hexdigest()[:16]

        if digest in seen_hashes:
            file_name = seen_hashes[digest]
        else:
            file_name = f"p{page_idx + 1:04d}-img{i:02d}-{digest}.{ext}"
            (assets_dir / file_name).write_bytes(blob)
            seen_hashes[digest] = file_name
            created += 1

        links.append(f"![Figure p{page_idx + 1}-{i}](figures/{doc_slug}/{file_name})")

    return links, created


def ingest_pdf(
    pdf_path: Path,
    out_dir: Path,
    with_figures: bool,
) -> tuple[str, int, int, str, int, int]:
    doc = fitz.open(pdf_path)
    slug = slugify(pdf_path.stem)
    out_file = out_dir / f"{slug}.md"
    seen_hashes: dict[str, str] = {}
    figure_refs = 0
    figure_files = 0

    try:
        title = (doc.metadata.get("title") or "").strip() or pdf_path.name
        sections = section_bounds(doc)

        lines = [
            f"# Altera document: {title}",
            "",
            f"Source PDF: `{pdf_path.name}`",
            f"Pages: {doc.page_count}",
            f"Figures extracted: {'yes' if with_figures else 'no'}",
            "",
        ]

        for sec_title, start, end in sections:
            lines.append(f"## {sec_title}  *(p.{start}-{end})*")
            lines.append("")
            for p in range(start - 1, end):
                txt = clean_page_text(doc[p].get_text())
                if txt:
                    lines.append(txt)
                    lines.append("")

                if with_figures:
                    figs, new_files = extract_page_figures(doc, p, slug, out_dir, seen_hashes)
                    figure_refs += len(figs)
                    figure_files += new_files
                    if figs:
                        lines.append(f"### Figures from page {p + 1}")
                        lines.append("")
                        lines.extend(figs)
                        lines.append("")

        out_file.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        return (pdf_path.name, doc.page_count, len(sections), out_file.name, figure_refs, figure_files)
    finally:
        doc.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT_DIR)
    parser.add_argument("--pattern", default="*.pdf")
    parser.add_argument(
        "--no-figures",
        action="store_true",
        help="Disable figure extraction (text-only markdown output).",
    )
    args = parser.parse_args()

    input_dir = args.input_dir.resolve()
    if not input_dir.exists():
        raise SystemExit(f"Input directory not found: {input_dir}")

    pdfs = sorted(input_dir.glob(args.pattern))
    if not pdfs:
        raise SystemExit(f"No files matched '{args.pattern}' in {input_dir}")

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    rows: list[tuple[str, int, int, str, int, int]] = []
    for pdf in pdfs:
        rows.append(ingest_pdf(pdf, OUT_DIR, with_figures=not args.no_figures))

    index_lines = [
        "# Altera docs index",
        "",
        "Generated by `scripts/ingest_altera.py`.",
        "",
        "| Source PDF | Pages | Sections | Figure refs | Figure files | Output file |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for name, pages, sections, out_name, fig_refs, fig_files in rows:
        index_lines.append(
            f"| {name} | {pages} | {sections} | {fig_refs} | {fig_files} | `{out_name}` |"
        )
    (OUT_DIR / "altera-index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    print(f"Input dir: {input_dir}")
    print(f"PDF files parsed: {len(rows)}")
    print(f"Figure extraction: {'enabled' if not args.no_figures else 'disabled'}")
    print(f"Output dir: {OUT_DIR}")


if __name__ == "__main__":
    main()
