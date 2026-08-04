"""Ingest FPGA MEA HTML memory maps into a repeatable knowledge artifact set.

Input: prefixed HTML files (for example files generated under MEA/html_from_zips):
  etx-2i-400g-v9.1-mem-map__entu_registers.html
  etx-2i-400g-v9.1-mem-map__entu_tables.html

Output (rewritten on each run):
  skills/rad-cli-operations/references/fpga-mea/
    raw/<input-file>.json           # normalized per-file payload
    fpga-mea-index.json             # merged index across all inputs
    fpga-mea-index.md               # human-readable summary

Usage:
  python scripts/ingest_mea.py
  python scripts/ingest_mea.py --input-dir MEA/html_from_zips
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_DIR = REPO.parent / "MEA" / "html_from_zips"
OUT_DIR = REPO / "skills" / "rad-cli-operations" / "references" / "fpga-mea"
DEFAULT_COMMANDS_FILE = REPO.parent / "MEA" / "mea_commands_only_with_relation 1.txt"

REGISTER_ANCHOR_RE = re.compile(
    r"Register\s+(0x[0-9a-fA-F]+)\s+-\s+([^<\n\r]+)",
    re.IGNORECASE,
)
ADDRESS_BLOCK_RE = re.compile(
    r"Address Block\s*-\s*([^<\n\r]+)",
    re.IGNORECASE,
)
TITLE_RE = re.compile(r"<title>([^<]+)</title>", re.IGNORECASE)

TR_RE = re.compile(r"<tr[^>]*>(.*?)</tr>", re.IGNORECASE | re.DOTALL)
TD_RE = re.compile(r"<td[^>]*>(.*?)</td>", re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")

HEX_RE = re.compile(r"^0x[0-9a-fA-F]+$")


def _clean_text(raw: str) -> str:
    text = TAG_RE.sub(" ", raw)
    text = html.unescape(text)
    text = WS_RE.sub(" ", text).strip()
    return text


def parse_source_metadata(stem: str) -> dict[str, str]:
    """Parse metadata from filename stem before '__'.

    Example stem:
      etx-2i-400g-v9.1-mem-map__entu_registers
    """
    if "__" not in stem:
        return {
            "device": "unknown",
            "version": "unknown",
            "map_type": "unknown",
            "source_stem": stem,
        }

    left, map_type = stem.split("__", 1)
    if left.endswith("-mem-map"):
        core = left[: -len("-mem-map")]
    else:
        core = left

    idx = core.rfind("-v")
    if idx >= 0:
        device = core[:idx]
        version = core[idx + 2 :]
    else:
        device = core
        version = "unknown"

    return {
        "device": device,
        "version": version,
        "map_type": map_type,
        "source_stem": stem,
    }


def parse_rows(html_text: str) -> list[dict[str, str]]:
    """Parse HTML table rows and keep common MEA summary row patterns.

    We keep:
    - 3-column rows where column-2 is an address (block, address, name)
    - 2-column rows where column-1 is an address (address, name)
    """
    rows: list[dict[str, str]] = []
    for tr in TR_RE.findall(html_text):
        cols = [_clean_text(td) for td in TD_RE.findall(tr)]
        cols = [c for c in cols if c]
        if len(cols) == 3 and HEX_RE.match(cols[1]):
            rows.append(
                {
                    "block": cols[0],
                    "address": cols[1].lower(),
                    "name": cols[2],
                }
            )
        elif len(cols) == 2 and HEX_RE.match(cols[0]):
            rows.append(
                {
                    "block": "",
                    "address": cols[0].lower(),
                    "name": cols[1],
                }
            )
    return rows


def parse_html_file(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    meta = parse_source_metadata(path.stem)

    title_match = TITLE_RE.search(text)
    title = _clean_text(title_match.group(1)) if title_match else ""

    anchors: list[dict[str, str]] = []
    seen = set()
    for addr, name in REGISTER_ANCHOR_RE.findall(text):
        key = (addr.lower(), _clean_text(name).lower())
        if key in seen:
            continue
        seen.add(key)
        anchors.append({"address": addr.lower(), "name": _clean_text(name)})

    blocks: list[str] = []
    seen_blocks = set()
    for block in ADDRESS_BLOCK_RE.findall(text):
        b = _clean_text(block)
        if b and b.lower() not in seen_blocks:
            seen_blocks.add(b.lower())
            blocks.append(b)

    rows = parse_rows(text)

    return {
        "source_file": path.name,
        "source_path": str(path),
        "metadata": meta,
        "title": title,
        "address_blocks": blocks,
        "toc_register_entries": anchors,
        "table_rows": rows,
        "counts": {
            "address_blocks": len(blocks),
            "toc_register_entries": len(anchors),
            "table_rows": len(rows),
        },
    }


def write_outputs(records: list[dict[str, Any]], out_dir: Path) -> None:
    if out_dir.exists():
        shutil.rmtree(out_dir)
    (out_dir / "raw").mkdir(parents=True, exist_ok=True)

    for rec in records:
        out_file = out_dir / "raw" / f"{Path(rec['source_file']).stem}.json"
        out_file.write_text(json.dumps(rec, indent=2, ensure_ascii=True), encoding="utf-8")

    index = {
        "schema": "fpga-mea.v1",
        "source": "scripts/ingest_mea.py",
        "files": [
            {
                "source_file": rec["source_file"],
                "device": rec["metadata"]["device"],
                "version": rec["metadata"]["version"],
                "map_type": rec["metadata"]["map_type"],
                "counts": rec["counts"],
            }
            for rec in records
        ],
    }
    (out_dir / "fpga-mea-index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=True), encoding="utf-8"
    )

    md_lines = [
        "# FPGA MEA ingest index",
        "",
        "Generated by `scripts/ingest_mea.py`.",
        "",
        "| File | Device | Version | Type | TOC registers | Table rows | Blocks |",
        "|---|---|---|---|---:|---:|---:|",
    ]
    for item in index["files"]:
        c = item["counts"]
        md_lines.append(
            f"| {item['source_file']} | {item['device']} | {item['version']} | {item['map_type']} | "
            f"{c['toc_register_entries']} | {c['table_rows']} | {c['address_blocks']} |"
        )
    (out_dir / "fpga-mea-index.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")


def copy_commands_catalog(commands_file: Path, out_dir: Path) -> None:
    """Copy MEA command catalog into tracked fpga-mea references location.

    This makes command-catalog lookups portable across clones and installs,
    rather than depending on a local ../MEA folder existing on that machine.
    """
    if not commands_file.exists():
        print(f"WARNING: MEA command catalog not found: {commands_file}")
        return
    dst = out_dir / "mea-commands-only-with-relation.txt"
    dst.write_text(commands_file.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
    print(f"Command catalog copied: {dst}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=DEFAULT_INPUT_DIR,
        help="Directory containing prefixed MEA HTML files",
    )
    parser.add_argument(
        "--pattern",
        default="*.html",
        help="Glob pattern for MEA files (default: *.html)",
    )
    parser.add_argument(
        "--commands-file",
        type=Path,
        default=DEFAULT_COMMANDS_FILE,
        help="MEA command catalog text file to copy into references",
    )
    args = parser.parse_args()

    input_dir = args.input_dir.resolve()
    if not input_dir.exists():
        raise SystemExit(f"Input directory not found: {input_dir}")

    files = sorted(input_dir.glob(args.pattern))
    if not files:
        raise SystemExit(f"No files matched in {input_dir} with pattern '{args.pattern}'")

    records = [parse_html_file(p) for p in files]
    write_outputs(records, OUT_DIR)
    copy_commands_catalog(args.commands_file.resolve(), OUT_DIR)

    total_toc = sum(r["counts"]["toc_register_entries"] for r in records)
    total_rows = sum(r["counts"]["table_rows"] for r in records)
    print(f"Input dir: {input_dir}")
    print(f"Files parsed: {len(records)}")
    print(f"TOC register entries: {total_toc}")
    print(f"Table rows: {total_rows}")
    print(f"Output dir: {OUT_DIR}")


if __name__ == "__main__":
    main()
