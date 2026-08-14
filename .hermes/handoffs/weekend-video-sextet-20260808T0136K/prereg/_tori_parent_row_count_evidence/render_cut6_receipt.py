#!/usr/bin/env python3
"""Render the fixed-range Cut 6 sibling receipt from landed aggregate rows."""
from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCOPE = ROOT / "cut6_fixed_000001_121000"
MANIFEST_PATH = SCOPE / "manifest.json"
STATUS_PATH = SCOPE / "status.json"
OUTPUT = ROOT.parent / "TORI_CUT6_INCLINATION_COUNT_20260812.md"
ORIGINAL_RECEIPT = ROOT.parent / "TORI_PARENT_ROW_COUNT_20260812.md"
INDEPENDENT_RECONSTRUCTION = (
    SCOPE / "FINAL_CUT6_INDEPENDENT_RECONSTRUCTION_20260812.json"
)
COLUMNS = [
    "n_cut5_parent_raw",
    "n_cut5_parent_dered",
    "n_cut6_inclination_raw",
    "n_cut6_inclination_dered",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def load_rows(manifest: dict) -> list[dict]:
    rows: list[dict] = []
    for entry in manifest["entries"]:
        tap = Path(entry["run_dir"]) / "tap"
        receipt_path = tap / "receipt.json"
        result_path = tap / "result.csv"
        if not receipt_path.exists() or not result_path.exists():
            break
        receipt = json.loads(receipt_path.read_text())
        if receipt.get("query_sha256") != entry["query_sha256"]:
            raise RuntimeError(f"Cut 6 receipt/query mismatch: {tap}")
        if receipt.get("result_sha256") != sha256(result_path):
            raise RuntimeError(f"Cut 6 receipt/result mismatch: {tap}")
        parsed = list(csv.DictReader(result_path.read_text().splitlines()))
        if len(parsed) != 1 or list(parsed[0]) != COLUMNS:
            raise RuntimeError(f"Cut 6 result shape mismatch: {tap}")
        values = {key: int(value) for key, value in parsed[0].items()}
        rows.append(
            {
                "lo": entry["lo"],
                "hi": entry["hi"],
                "elapsed_seconds": (
                    parse_time(receipt["completed_utc"])
                    - parse_time(receipt["started_utc"])
                ).total_seconds(),
                "job_url": receipt["job_url"],
                "query_sha256": receipt["query_sha256"],
                "result_sha256": receipt["result_sha256"],
                **values,
            }
        )
    return rows


def ratio(numerator: int, denominator: int) -> str:
    return f"{(numerator / denominator * 100):.6f}%" if denominator else "undefined"


def render_document(manifest: dict, status: dict, rows: list[dict]) -> str:
    complete = (
        len(rows) == manifest["partition_count"]
        and status.get("stop_reason") == "fixed_range_1_121000_complete"
    )
    label = "COMPLETE FIXED-RANGE LOWER BOUND" if complete else "PARTIAL LOWER BOUND"
    totals = {column: sum(row[column] for row in rows) for column in COLUMNS}
    covered_hi = rows[-1]["hi"] if rows else 0
    coverage = manifest["coverage"]
    lines = [
        "# Cut 6 inclination count — fixed-range aggregate receipt",
        "",
        f"**Status: {label}.**",
        "",
        "## Scope and interpretation",
        "",
        "- This sibling receipt appends one catalogue-native inclination cut after Cut 5 and does not modify the accepted Cut-5 receipt.",
        "- Frozen predicate: `POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551`.",
        "- This is `e^2 < 9/49`, specified by Lana as equivalent to `b/a > 0.4` under `b/a = (1 - |e|)/(1 + |e|)`.",
        "- Objects with `e >= 1` fail this threshold directly; no separate assumed inclination fraction is applied.",
        "- Frozen range: `BRICKID 1…121000`, the same frozen coverage as the Cut 5 certificate. This does not reopen or extend the stopped sweep.",
        f"- Coverage: `121000/662174 = {coverage['keyspace_fraction'] * 100:.6f}%` of the documented BRICKID keyspace, not sky area.",
        f"- Landed contiguous range in this receipt: `BRICKID 1…{covered_hi}` across `{len(rows)}/{manifest['partition_count']}` blocks.",
        "- Every total is a **LOWER BOUND** over only the named keyspace. No density, keyspace, or sky-area extrapolation is performed.",
        "- Cut 6 / Cut 5 percentages below are measured same-block catalogue survival ratios, not external spiral, inclination, or Yui-retention assumptions.",
        "",
        "## Running totals",
        "",
        "| Branch | Cut 5 parent LOWER BOUND | Cut 6 inclination LOWER BOUND | Measured Cut 6/Cut 5 |",
        "|---|---:|---:|---:|",
        f"| raw `mag_r` | {totals['n_cut5_parent_raw']:,} | {totals['n_cut6_inclination_raw']:,} | {ratio(totals['n_cut6_inclination_raw'], totals['n_cut5_parent_raw'])} |",
        f"| dered `dered_mag_r` | {totals['n_cut5_parent_dered']:,} | {totals['n_cut6_inclination_dered']:,} | {ratio(totals['n_cut6_inclination_dered'], totals['n_cut5_parent_dered'])} |",
        "",
        "## Per-block aggregates",
        "",
        "| BRICKID block | Elapsed seconds | Cut 5 raw | Cut 6 raw | Raw survival | Cut 5 dered | Cut 6 dered | Dered survival |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['lo']}…{row['hi']} | {row['elapsed_seconds']:.1f} | "
            f"{row['n_cut5_parent_raw']:,} | {row['n_cut6_inclination_raw']:,} | "
            f"{ratio(row['n_cut6_inclination_raw'], row['n_cut5_parent_raw'])} | "
            f"{row['n_cut5_parent_dered']:,} | {row['n_cut6_inclination_dered']:,} | "
            f"{ratio(row['n_cut6_inclination_dered'], row['n_cut5_parent_dered'])} |"
        )
    lines += [
        "",
        "## Boundary and custody",
        "",
        "- server-side aggregate rows returned: one per landed block",
        "- sample rows exported: **0**",
        "- positions exported: **0**",
        "- images requested: **0**",
        "- chirality/handedness computed: **0**",
        "- sky statistics computed: **0**",
        "- trigonometric or axis-relative terms: **0**",
        "- bulk downloads: **0**",
        "- publication/acceptance/commit/push: **0**",
        "",
        "This count does not decide accepted yield. It applies only the specified catalogue inclination cut. Spiral classification, image/WCS availability, Yui retention, and user acceptance remain separate gates.",
        "",
        "## Hash custody",
        "",
        f"- Original Cut-5 receipt: `{ORIGINAL_RECEIPT}` — SHA-256 `{sha256(ORIGINAL_RECEIPT) if ORIGINAL_RECEIPT.exists() else 'missing'}`.",
        f"- Cut 6 manifest: `{MANIFEST_PATH}` — SHA-256 `{sha256(MANIFEST_PATH) if MANIFEST_PATH.exists() else 'not-yet-written'}`.",
        f"- Independent reconstruction: `{INDEPENDENT_RECONSTRUCTION}` — SHA-256 `{sha256(INDEPENDENT_RECONSTRUCTION) if INDEPENDENT_RECONSTRUCTION.exists() else 'pending'}`. This reconstruction sums the 13 hash-matched one-row results and checks each Cut 5 block against its original result without trusting status or Markdown totals.",
    ]
    if status.get("finished_utc"):
        lines.append(
            f"- Fixed-range pass finished at `{status['finished_utc']}` with reason `{status.get('stop_reason')}`."
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text())
    status = json.loads(STATUS_PATH.read_text()) if STATUS_PATH.exists() else {}
    rows = load_rows(manifest)
    content = render_document(manifest, status, rows)
    OUTPUT.write_text(content)
    print(
        json.dumps(
            {
                "path": str(OUTPUT),
                "bytes": OUTPUT.stat().st_size,
                "sha256": sha256(OUTPUT),
                "landed_partitions": len(rows),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
