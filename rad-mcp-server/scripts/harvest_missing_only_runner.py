from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BASE = REPO / "skills" / "rad-cli-operations" / "references"
PY = "c:/Users/uzi_g/Downloads/ai-projects/fusion-cli/.venv/Scripts/python.exe"
JOBS = [
    ("etx1p", "ehud1p"),
    ("mp1", "mp-one"),
    ("mp4100", "marks-mp4"),
    ("etx2v", "etx2v-1"),
]
BRANCH_TIMEOUT_SEC = 180


def read_rows(family: str) -> list[dict]:
    p = BASE / f"cli-help-{family}.jsonl"
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def args_noenter_count_and_contexts(family: str) -> tuple[int, list[str]]:
    rows = read_rows(family)
    miss = [r for r in rows if r.get("kind") == "args-noenter"]
    return len(miss), sorted({r["context"] for r in miss})


def run_branch(device: str, branch: str, cache: Path) -> tuple[bool, str]:
    cmd = [PY, "scripts/harvest_cli.py", "harvest", device, "--branch", branch, "--tree-cache", str(cache)]
    try:
        r = subprocess.run(cmd, text=True, capture_output=True, cwd=REPO, timeout=BRANCH_TIMEOUT_SEC)
    except subprocess.TimeoutExpired as e:
        return False, f"timeout after {BRANCH_TIMEOUT_SEC}s: {e}"
    out = (r.stdout + "\n" + r.stderr).strip()
    return (r.returncode == 0), out


def main() -> int:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    log_path = BASE / f"harvest-missing-only-{ts}.log"

    lines: list[str] = []
    summary: list[tuple[str, int, int, int, int, int]] = []

    for family, device in JOBS:
        before, ctxs = args_noenter_count_and_contexts(family)
        lines.append(f"=== {family} on {device}: before={before}, contexts={len(ctxs)}")
        print(lines[-1], flush=True)

        cache = BASE / f"{device}-tree-cache.txt"
        ok = 0
        fail = 0
        retried = 0

        for i, ctx in enumerate(ctxs, 1):
            tried = [ctx]
            success, out = run_branch(device, ctx, cache)

            if (not success) and ("not found in the live tree" in out) and (" NAME" in ctx):
                alt = " ".join("name" if t == "NAME" else t for t in ctx.split())
                if alt != ctx:
                    retried += 1
                    tried.append(alt)
                    success, out = run_branch(device, alt, cache)

            if success:
                ok += 1
            else:
                fail += 1
                tail = "\n".join(out.splitlines()[-8:])
                lines.append(f"FAIL [{family} {i}/{len(ctxs)}] tried={tried}\n{tail}")
                print(lines[-1], flush=True)

        after, _ = args_noenter_count_and_contexts(family)
        delta = after - before
        lines.append(
            f"=== {family} done: ok={ok} fail={fail} retried={retried} after={after} delta={delta}"
        )
        print(lines[-1], flush=True)
        summary.append((family, before, after, delta, ok, fail))

    lines.append("")
    lines.append("=== SUMMARY ===")
    for family, before, after, delta, ok, fail in summary:
        lines.append(
            f"{family}: before={before} after={after} delta={delta} branch_ok={ok} branch_fail={fail}"
        )

    text = "\n".join(lines) + "\n"
    log_path.write_text(text, encoding="utf-8")
    print(text)
    print(f"log_file={log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
