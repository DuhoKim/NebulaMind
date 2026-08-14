#!/usr/bin/env python3
"""Independently reconstruct the fixed-range Cut 6 aggregate certificate."""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCOPE = ROOT / "cut6_fixed_000001_121000"
MANIFEST_PATH = SCOPE / "manifest.json"
OUTPUT = SCOPE / "FINAL_CUT6_INDEPENDENT_RECONSTRUCTION_20260812.json"
EXPECTED_MANIFEST_SHA256 = "b157e6c84ed91e77612caa6c0ada173324d9a42193f69777829a60354fd9fc89"
EXPECTED_COLUMNS = [
    "n_cut5_parent_raw",
    "n_cut5_parent_dered",
    "n_cut6_inclination_raw",
    "n_cut6_inclination_dered",
]
EXPECTED_RANGES = [
    (1, 1000),
    (1001, 11000),
    *[(lo, lo + 9999) for lo in range(11001, 111002, 10000)],
]
THRESHOLD = "POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def one_row(path: Path) -> dict[str, int]:
    rows = list(csv.DictReader(path.read_text().splitlines()))
    if len(rows) != 1:
        raise RuntimeError(f"expected one aggregate row: {path}")
    return {key: int(value) for key, value in rows[0].items()}


def load_guard():
    runner = ROOT / "run_aggregate_tap.py"
    spec = importlib.util.spec_from_file_location("aggregate_runner", runner)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load aggregate guard")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate_aggregate_only


def elapsed_seconds(receipt: dict) -> float:
    start = datetime.fromisoformat(receipt["started_utc"].replace("Z", "+00:00"))
    finish = datetime.fromisoformat(receipt["completed_utc"].replace("Z", "+00:00"))
    return (finish - start).total_seconds()


def uws_phase(job_url: str) -> str:
    with urllib.request.urlopen(job_url + "/phase", timeout=30) as response:
        return response.read().decode().strip()


def main() -> None:
    if sha256(MANIFEST_PATH) != EXPECTED_MANIFEST_SHA256:
        raise RuntimeError("manifest hash does not match frozen pre-submission hash")
    manifest = json.loads(MANIFEST_PATH.read_text())
    if manifest["coverage"] != {
        "start_brickid": 1,
        "stop_brickid": 121000,
        "keyspace_total": 662174,
        "keyspace_fraction": 121000 / 662174,
        "keyspace_not_sky_area": True,
    }:
        raise RuntimeError("coverage contract drift")
    if manifest.get("no_coverage_extension") is not True:
        raise RuntimeError("coverage-extension guard missing")
    if [(entry["lo"], entry["hi"]) for entry in manifest["entries"]] != EXPECTED_RANGES:
        raise RuntimeError("range sequence drift")

    validate = load_guard()
    totals = {column: 0 for column in EXPECTED_COLUMNS}
    blocks = []
    jobs = set()
    cursor = 1
    for entry in manifest["entries"]:
        lo, hi = entry["lo"], entry["hi"]
        if lo != cursor:
            raise RuntimeError(f"non-contiguous range: expected {cursor}, got {lo}")
        cursor = hi + 1
        query_path = Path(entry["query_path"])
        source_path = Path(entry["source_cut5_result_path"])
        tap = Path(entry["run_dir"]) / "tap"
        submission_path = tap / "submission.json"
        receipt_path = tap / "receipt.json"
        result_path = tap / "result.csv"
        for path in (query_path, source_path, submission_path, receipt_path, result_path):
            if not path.exists():
                raise RuntimeError(f"missing custody artifact: {path}")

        query = query_path.read_text()
        validate(query)
        if sha256(query_path) != entry["query_sha256"]:
            raise RuntimeError(f"query hash mismatch: {query_path}")
        if f"WHERE t.brickid BETWEEN {lo} AND {hi}" not in " ".join(query.split()):
            raise RuntimeError(f"query range mismatch: {query_path}")
        if query.count(THRESHOLD) != 2:
            raise RuntimeError(f"Cut 6 predicate count mismatch: {query_path}")
        if re.search(r"\b(SIN|COS|TAN|ASIN|ACOS|ATAN|RADIANS|DEGREES|COSTHETA)\b", query.upper()):
            raise RuntimeError(f"forbidden trigonometric token: {query_path}")
        normalized_query = " ".join(query.split())
        select_clause = normalized_query[7 : normalized_query.upper().index(" FROM ")]
        aliases = re.findall(
            r"\bAS\s+([A-Za-z_][A-Za-z0-9_]*)\b",
            select_clause,
            re.IGNORECASE,
        )
        if aliases != EXPECTED_COLUMNS:
            raise RuntimeError(f"projection mismatch: {query_path}")

        if sha256(source_path) != entry["source_cut5_result_sha256"]:
            raise RuntimeError(f"source Cut 5 hash mismatch: {source_path}")
        source = one_row(source_path)
        submission = json.loads(submission_path.read_text())
        receipt = json.loads(receipt_path.read_text())
        result = one_row(result_path)
        if list(result) != EXPECTED_COLUMNS:
            raise RuntimeError(f"result columns mismatch: {result_path}")
        if submission["query_sha256"] != entry["query_sha256"]:
            raise RuntimeError(f"submission/query mismatch: {submission_path}")
        if receipt["query_sha256"] != entry["query_sha256"]:
            raise RuntimeError(f"receipt/query mismatch: {receipt_path}")
        if receipt["result_sha256"] != sha256(result_path):
            raise RuntimeError(f"receipt/result mismatch: {receipt_path}")
        if receipt["result_row_count"] != 1 or receipt["result_columns"] != EXPECTED_COLUMNS:
            raise RuntimeError(f"non-single aggregate result: {receipt_path}")
        expected_zeroes = {
            "sample_rows_exported": 0,
            "positions_exported": 0,
            "images_requested": 0,
            "chirality_computed": False,
            "sky_statistics_computed": False,
        }
        for name, expected in expected_zeroes.items():
            if receipt.get(name) != expected:
                raise RuntimeError(f"boundary violation {name}: {receipt_path}")
        if receipt["job_url"] != submission["job_url"]:
            raise RuntimeError(f"job URL mismatch: {tap}")
        if receipt["job_url"] in jobs:
            raise RuntimeError(f"duplicate TAP job URL: {receipt['job_url']}")
        jobs.add(receipt["job_url"])
        phase = uws_phase(receipt["job_url"])
        if phase != "COMPLETED":
            raise RuntimeError(f"TAP job not completed: {receipt['job_url']} {phase}")

        if result["n_cut5_parent_raw"] != source["n_cut5_parent_raw"]:
            raise RuntimeError(f"raw Cut 5 cross-pass mismatch: {tap}")
        if result["n_cut5_parent_dered"] != source["n_cut5_parent_dered"]:
            raise RuntimeError(f"dered Cut 5 cross-pass mismatch: {tap}")
        if not 0 <= result["n_cut6_inclination_raw"] <= result["n_cut5_parent_raw"]:
            raise RuntimeError(f"raw monotonicity failure: {tap}")
        if not 0 <= result["n_cut6_inclination_dered"] <= result["n_cut5_parent_dered"]:
            raise RuntimeError(f"dered monotonicity failure: {tap}")

        for column in EXPECTED_COLUMNS:
            totals[column] += result[column]
        blocks.append(
            {
                "lo": lo,
                "hi": hi,
                "job_url": receipt["job_url"],
                "uws_phase_verified": phase,
                "query_sha256": entry["query_sha256"],
                "source_cut5_result_sha256": entry["source_cut5_result_sha256"],
                "cut6_result_sha256": receipt["result_sha256"],
                "elapsed_seconds": elapsed_seconds(receipt),
                **result,
            }
        )

    if cursor - 1 != 121000 or len(blocks) != 13:
        raise RuntimeError("fixed-range reconstruction incomplete")
    if totals["n_cut5_parent_raw"] != 185345 or totals["n_cut5_parent_dered"] != 208407:
        raise RuntimeError("reconstructed Cut 5 totals do not match accepted certificate")

    status = json.loads((SCOPE / "status.json").read_text())
    status_match = status.get("totals") == {
        "completed_partitions": 13,
        "covered_hi": 121000,
        **totals,
    }
    output = {
        "verified_utc": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "status": "PASS",
        "method": "independent reconstruction from frozen manifest, exact queries, original Cut-5 block results, Cut-6 one-row results, receipts, and live UWS final phases; status.json and Markdown totals were not trusted inputs",
        "coverage": manifest["coverage"],
        "partition_count": len(blocks),
        "unique_tap_job_count": len(jobs),
        "all_uws_phases": "COMPLETED",
        "totals": totals,
        "losses": {
            "raw_cut5_minus_cut6": totals["n_cut5_parent_raw"] - totals["n_cut6_inclination_raw"],
            "dered_cut5_minus_cut6": totals["n_cut5_parent_dered"] - totals["n_cut6_inclination_dered"],
        },
        "measured_survival": {
            "raw": totals["n_cut6_inclination_raw"] / totals["n_cut5_parent_raw"],
            "dered": totals["n_cut6_inclination_dered"] / totals["n_cut5_parent_dered"],
        },
        "status_totals_match_after_independent_reconstruction": status_match,
        "boundary": {
            "aggregate_rows_returned": 13,
            "sample_rows_exported": 0,
            "positions_exported": 0,
            "images_requested": 0,
            "chirality_computed": False,
            "sky_statistics_computed": False,
            "trigonometric_or_axis_relative_terms": 0,
            "bulk_downloads": 0,
            "publication_commit_push": 0,
        },
        "blocks": blocks,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "PASS",
        "path": str(OUTPUT),
        "sha256": sha256(OUTPUT),
        "totals": totals,
        "losses": output["losses"],
        "measured_survival": output["measured_survival"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
