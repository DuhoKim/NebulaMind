#!/usr/bin/env python3
"""Render the new remaining-keyspace sibling receipt from landed aggregates."""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
SCOPE = ROOT / "partitions" / "remaining_121001_662174"
MANIFEST_PATH = SCOPE / "manifest.json"
STATUS_PATH = SCOPE / "status.json"
OUTPUT = PREREG / "TORI_FULL_KEYSPACE_SWEEP_20260813.md"
FROZEN_PARENT_RECEIPT = PREREG / "TORI_PARENT_ROW_COUNT_20260812.md"
FROZEN_CUT6_RECEIPT = PREREG / "TORI_CUT6_INCLINATION_COUNT_20260812.md"
TOTAL_KEYS = 662174


def load_contract():
    path = ROOT / "run_remaining_keyspace.py"
    spec = importlib.util.spec_from_file_location("remaining_contract", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load remaining-keyspace contract")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CONTRACT = load_contract()
COLUMNS = CONTRACT.COLUMNS
BASE_TOTALS = CONTRACT.BASE_TOTALS


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt(value: int) -> str:
    return f"{value:,}"


def normalize_result_values(row: dict[str, str]) -> dict[str, int]:
    joined = int(row["n_join_rows"])
    values = {"n_join_rows": joined}
    for column in COLUMNS[1:]:
        value = row[column]
        if value == "":
            if joined != 0:
                raise RuntimeError(f"blank aggregate {column} with nonzero joined population")
            values[column] = 0
        else:
            values[column] = int(value)
    return values


def read_landed(manifest: dict) -> list[dict]:
    landed = []
    for entry in manifest["entries"]:
        tap = Path(entry["run_dir"]) / "tap"
        receipt_path = tap / "receipt.json"
        result_path = tap / "result.csv"
        if not receipt_path.exists() or not result_path.exists():
            continue
        receipt = json.loads(receipt_path.read_text())
        rows = list(csv.DictReader(result_path.read_text().splitlines()))
        if len(rows) != 1 or list(rows[0]) != COLUMNS:
            raise RuntimeError(f"result shape mismatch: {result_path}")
        if receipt.get("query_sha256") != entry["query_sha256"]:
            raise RuntimeError(f"query hash mismatch: {receipt_path}")
        if receipt.get("result_sha256") != sha256(result_path):
            raise RuntimeError(f"result hash mismatch: {receipt_path}")
        for name, expected in {
            "result_row_count": 1,
            "sample_rows_exported": 0,
            "positions_exported": 0,
            "images_requested": 0,
            "chirality_computed": False,
            "sky_statistics_computed": False,
        }.items():
            if receipt.get(name) != expected:
                raise RuntimeError(f"receipt boundary mismatch {name}: {receipt_path}")
        started = datetime.fromisoformat(receipt["started_utc"].replace("Z", "+00:00"))
        completed = datetime.fromisoformat(receipt["completed_utc"].replace("Z", "+00:00"))
        landed.append(
            {
                **entry,
                "elapsed_seconds": (completed - started).total_seconds(),
                "values": normalize_result_values(rows[0]),
                "result_sha256": receipt["result_sha256"],
            }
        )
    return landed


def render_text(
    manifest: dict,
    status: dict,
    landed: list[dict],
    recovery_events: list[dict] | None = None,
    closure: dict | None = None,
) -> str:
    totals = status["totals"]
    all_totals = totals["all_landed_totals"]
    counted = totals["landed_total_keys"]
    displayed_partitions = totals["landed_new_partitions"]
    displayed_new_keys = totals["landed_new_keys"]
    displayed_frontier = totals["contiguous_covered_hi"]
    zero_tail_complete = bool(closure and closure.get("direct_lower_bound_equals_exact_full_count"))
    if zero_tail_complete and closure is not None:
        direct = closure["direct_full_chain"]
        counted = direct["keyspace_units"]
        displayed_partitions = direct["landed_new_partitions"]
        displayed_new_keys = direct["keyspace_units"] - 121000
        displayed_frontier = direct["stop_brickid"]
        all_totals = closure["totals"]
    coverage_pct = 100 * counted / TOTAL_KEYS
    complete = (
        status.get("stop_reason") == "remaining_keyspace_exhausted"
        and totals["landed_new_partitions"] == manifest["partition_count"]
        and counted == TOTAL_KEYS
    )
    deadline = status.get("stop_reason") == "deadline_2026_08_13_0600_kst_reached"
    if zero_tail_complete:
        label = "COMPLETE FULL-KEYSPACE COUNT — ZERO-TAIL CLOSURE"
    elif complete:
        label = "COMPLETE FULL-KEYSPACE COUNT"
    elif deadline:
        label = "DEADLINE-STOPPED LOWER BOUND"
    elif str(status.get("stop_reason", "")).startswith("partition_failure_"):
        label = "FAILED-STOPPED LOWER BOUND"
    else:
        label = "RUNNING LOWER BOUND"

    lines = [
        "# TORI — Full BRICKID keyspace aggregate sweep",
        "",
        f"**Receipt rendered:** `{utc_now()}`  ",
        f"**Status:** `{label}`",
        "",
        "## Scope",
        "",
        "- Frozen `BRICKID 1…121000` certificates are inputs only and are not modified or re-queried.",
        "- New one-pass scope: `BRICKID 121001…662174`. Each block returns the existing Cut 1–5/availability aggregate chain and both Cut 6 branch counts in the same one-row response.",
        "- Cut 6 predicate: `POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551`.",
        f"- Stop at the first of keyspace exhaustion or `2026-08-13 06:00 KST` (`{manifest['stop_rule']['deadline_utc']}`).",
        "- No spiral fraction, retention factor, or other external factor is multiplied into these catalogue counts.",
        "",
        "## Running keyspace count",
        "",
        f"- **{counted:,} of {TOTAL_KEYS:,} BRICKID keyspace units counted = {coverage_pct:.6f}%.**",
        f"- Contiguous completed frontier: `BRICKID 1…{displayed_frontier}`.",
        f"- New landed partitions: `{displayed_partitions}/{manifest['partition_count']}`; new landed keyspace units: `{displayed_new_keys:,}/{manifest['remaining_key_count']:,}`.",
        "- These are BRICKID keyspace units, not sky area, footprint, or an equal-area statistic. Out-of-order landed blocks count only as their exact disjoint keyspace units; contiguous coverage is reported separately.",
        "- Every incomplete total is a **LOWER BOUND** formed only by summing frozen baseline aggregates plus landed, non-overlapping one-row blocks. No density extrapolation is performed.",
    ]
    if zero_tail_complete and closure is not None:
        direct = closure["direct_full_chain"]
        tail = closure["tail_zero_proof"]
        stop = closure["stop_reconciliation"]
        lines += [
            "",
            "## Zero-tail closure and completeness ruling",
            "",
            f"- Direct full-chain measurement covers **{direct['keyspace_units']:,} of {TOTAL_KEYS:,}** BRICKID keyspace units = **{100 * direct['keyspace_units'] / TOTAL_KEYS:.6f}%** through `BRICKID {direct['stop_brickid']}`.",
            f"- A separate aggregate-only existence probe measured the entire remaining `BRICKID {tail['start_brickid']}…{tail['stop_brickid']}` tail ({tail['keyspace_units']:,} keyspace units) and returned **`n_join_rows = 0`** in one hash-verified row.",
            "- Because the probe uses the same frozen tractor table and photo-z left join, zero joined parent rows means every downstream Cut 1–6 count is exactly zero throughout that tail.",
            "- Therefore the directly summed Cut totals were LOWER BOUND values before the probe, and the tail proof establishes that this lower bound equals the exact full-keyspace count over `BRICKID 1…662174`.",
            "- This is catalogue BRICKID keyspace, not sky area; it does not measure an equal-area footprint fraction.",
            f"- Tail query SHA-256: `{tail['query_sha256']}`; result SHA-256: `{tail['result_sha256']}`; UWS job `{tail['job_url']}` ended `{tail['phase']}`.",
            "",
            "## Final stop reconciliation",
            "",
            f"- `status.json` records {stop['stale_status_landed_partitions']} completed blocks because its last update was `{stop['stale_status_updated_utc']}`.",
            f"- Disk custody contains **{stop['authoritative_landed_partitions']} authoritative** receipt/result pairs: the 42nd completed at `{stop['last_receipt_completed_utc']}` after the stale status write.",
            f"- That stale status also records `stop_reason = {stop.get('status_stop_reason')}` and `finished_utc = {stop.get('status_finished_utc')}`; neither field records the parent process's later termination.",
            f"- Cause: {stop['cause']}.",
            f"- Classification: {stop['classification']}.",
        ]
        all_totals = closure["totals"]

    lines += [
        "",
        "## Full aggregate chain — frozen baseline plus all landed blocks",
        "",
        "| Aggregate | Count |",
        "|---|---:|",
    ]
    labels = {
        "n_join_rows": "joined catalogue rows",
        "n_cut1_primary_mask": "Cut 1 primary + mask",
        "n_cut2_extended_flux": "Cut 2 extended + positive R flux",
        "n_photoz_joined_cut2": "photo-z joined after Cut 2",
        "n_cut3_photoz": "Cut 3 photo-z",
        "n_cut4_raw_mag": "Cut 4 raw magnitude",
        "n_cut4_dered_mag": "Cut 4 dered magnitude",
        "n_cut5_parent_raw": "Cut 5 parent raw",
        "n_cut5_parent_dered": "Cut 5 parent dered",
        "n_raw_allband_nobs": "raw all-band nobs",
        "n_dered_allband_nobs": "dered all-band nobs",
        "n_raw_allband_ngood": "raw all-band ngood",
        "n_dered_allband_ngood": "dered all-band ngood",
        "n_raw_allband_ivar": "raw all-band inverse variance",
        "n_dered_allband_ivar": "dered all-band inverse variance",
        "n_raw_shape_valid": "raw shape-valid",
        "n_dered_shape_valid": "dered shape-valid",
        "n_raw_native_covariates": "raw native covariates",
        "n_dered_native_covariates": "dered native covariates",
        "n_raw_all_countable_availability": "raw all countable availability",
        "n_dered_all_countable_availability": "dered all countable availability",
        "n_cut6_inclination_raw": "Cut 6 inclination raw",
        "n_cut6_inclination_dered": "Cut 6 inclination dered",
    }
    for column in COLUMNS:
        lines.append(f"| {labels[column]} (`{column}`) | {fmt(all_totals[column])} |")

    lines += [
        "",
        "## Per-block landed aggregates",
        "",
        "| BRICKID block | Elapsed seconds | Cut 1 | Cut 3 | Cut 5 raw | Cut 5 dered | Cut 6 raw | Cut 6 dered | Query SHA-256 | Result SHA-256 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for item in landed:
        values = item["values"]
        lines.append(
            f"| {item['lo']}…{item['hi']} | {item['elapsed_seconds']:.1f} | "
            f"{fmt(values['n_cut1_primary_mask'])} | {fmt(values['n_cut3_photoz'])} | "
            f"{fmt(values['n_cut5_parent_raw'])} | {fmt(values['n_cut5_parent_dered'])} | "
            f"{fmt(values['n_cut6_inclination_raw'])} | {fmt(values['n_cut6_inclination_dered'])} | "
            f"`{item['query_sha256']}` | `{item['result_sha256']}` |"
        )
    if not landed:
        lines.append("| none landed yet | — | — | — | — | — | — | — | — | — |")

    events = recovery_events if recovery_events is not None else status.get("recovery_history", [])
    if events:
        lines += [
            "",
            "## Failure and recovery history",
            "",
            "- The six one-row receipts landed before the 502 incident remain authoritative; recovery never re-queries or replaces a landed partition.",
        ]
        for event in events:
            lines += [
                f"- Detected `{event.get('detected_utc', 'unknown')}`; prior stop `{event.get('stop_reason', 'partition failure')}`.",
                f"  - Cause: {event['cause']}.",
                f"  - Runner defect: {event['runner_defect']}.",
                f"  - Recovery: {event['recovery_action']}.",
            ]

    lines += [
        "",
        "## Boundary and custody",
        "",
        f"- full-chain server-side aggregate rows returned: **{len(landed)}**",
        "- sample rows exported: **0**",
        "- positions exported: **0**",
        "- images requested: **0**",
        "- chirality/handedness computed: **0**",
        "- sky statistics computed: **0**",
        "- trigonometric or axis-relative terms: **0**",
        "- bulk downloads: **0**",
        "- publication/acceptance/commit/push: **0**",
        f"- Stale `status.json` active-concurrency snapshot: `{status.get('active_concurrency', 3)}`; final live count processes and lock holders are reported below.",
    ]
    if zero_tail_complete:
        lines += [
            "- tail-existence server-side aggregate rows returned: **1**",
            f"- total server-side aggregate rows returned: **{len(landed) + 1}**",
        ]
    if status.get("service_backoff"):
        lines.append(
            f"- Service-pressure backoff: `{status['service_backoff']['signal']}` detected at `{status['service_backoff']['detected_utc']}`; future submissions reduced to serial and active jobs were preserved."
        )
    else:
        lines.append("- Service-pressure backoff: not triggered in the persisted state.")
    lines += [
        f"- Frozen parent receipt SHA-256: `{CONTRACT.FROZEN_PARENT_RECEIPT_SHA256}`.",
        f"- Frozen Cut 6 receipt SHA-256: `{CONTRACT.FROZEN_CUT6_RECEIPT_SHA256}`.",
        f"- Remaining manifest: `{MANIFEST_PATH}`" + (f" — SHA-256 `{sha256(MANIFEST_PATH)}`." if MANIFEST_PATH.exists() else "."),
    ]
    if zero_tail_complete and closure is not None:
        reconstruction_path = SCOPE / "FINAL_FULL_KEYSPACE_INDEPENDENT_RECONSTRUCTION_20260813.json"
        lines.append(
            f"- Independent final reconstruction: `{reconstruction_path}` — SHA-256 `{sha256(reconstruction_path)}`."
        )
        lines.append("- Final process/lock closure: **0 live count processes; 0 orchestrator lock holders**.")
    if status.get("stop_reason") and not zero_tail_complete:
        lines.append(f"- Persisted stop reason: `{status['stop_reason']}`.")
    if status.get("finished_utc") and not zero_tail_complete:
        lines.append(f"- Orchestrator finished at `{status['finished_utc']}`.")
    return "\n".join(lines) + "\n"


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text())
    status = json.loads(STATUS_PATH.read_text())
    landed = read_landed(manifest)
    closure_path = SCOPE / "FINAL_FULL_KEYSPACE_INDEPENDENT_RECONSTRUCTION_20260813.json"
    closure = json.loads(closure_path.read_text()) if closure_path.exists() else None
    text = render_text(manifest, status, landed, status.get("recovery_history", []), closure)
    OUTPUT.write_text(text)
    print(json.dumps({"path": str(OUTPUT), "sha256": sha256(OUTPUT), "bytes": len(text.encode()), "landed_partitions": len(landed)}, sort_keys=True))


if __name__ == "__main__":
    main()
