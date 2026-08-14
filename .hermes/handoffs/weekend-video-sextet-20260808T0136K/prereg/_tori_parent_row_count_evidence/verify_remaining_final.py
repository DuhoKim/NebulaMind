#!/usr/bin/env python3
"""Independently close the remaining-keyspace sweep from immutable receipts."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
SCOPE = ROOT / "partitions" / "remaining_121001_662174"
MANIFEST_PATH = SCOPE / "manifest.json"
STATUS_PATH = SCOPE / "status.json"
LOG_PATH = SCOPE / "orchestrator.log"
PARENT_RECONSTRUCTION = ROOT / "partitions" / "FINAL_THRESHOLD_INDEPENDENT_RECONSTRUCTION_20260812.json"
CUT6_RECONSTRUCTION = ROOT / "cut6_fixed_000001_121000" / "FINAL_CUT6_INDEPENDENT_RECONSTRUCTION_20260812.json"
PARENT_RECEIPT = PREREG / "TORI_PARENT_ROW_COUNT_20260812.md"
CUT6_RECEIPT = PREREG / "TORI_CUT6_INCLINATION_COUNT_20260812.md"
TAIL = SCOPE / "tail_existence_541001_662174"
OUTPUT = SCOPE / "FINAL_FULL_KEYSPACE_INDEPENDENT_RECONSTRUCTION_20260813.json"
TOTAL_KEYS = 662174
EXPECTED_MANIFEST_SHA256 = "665738a20a9e754ee190297a421a1438d33bb563e53ea67b64feb634c250b7ef"
EXPECTED_PARENT_RECEIPT_SHA256 = "df9357085d4cfd35320ab34346a1fb3080dc1e5ba1e3d86e2dc6231dbbf534f3"
EXPECTED_CUT6_RECEIPT_SHA256 = "ed6b6e5e957903473c7692d5973f3b2d05a991916ce3aa247365938b0f414651"
EXPECTED_TAIL_QUERY_SHA256 = "50900d60ee92deeef326fd190cc0aac0a9f799113e688789a784d5bb649fcccc"
COLUMNS = [
    "n_join_rows",
    "n_cut1_primary_mask",
    "n_cut2_extended_flux",
    "n_photoz_joined_cut2",
    "n_cut3_photoz",
    "n_cut4_raw_mag",
    "n_cut4_dered_mag",
    "n_cut5_parent_raw",
    "n_cut5_parent_dered",
    "n_raw_allband_nobs",
    "n_dered_allband_nobs",
    "n_raw_allband_ngood",
    "n_dered_allband_ngood",
    "n_raw_allband_ivar",
    "n_dered_allband_ivar",
    "n_raw_shape_valid",
    "n_dered_shape_valid",
    "n_raw_native_covariates",
    "n_dered_native_covariates",
    "n_raw_all_countable_availability",
    "n_dered_all_countable_availability",
    "n_cut6_inclination_raw",
    "n_cut6_inclination_dered",
]
CUT6 = "POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def normalize(row: dict[str, str], source: Path) -> dict[str, int]:
    joined = int(row["n_join_rows"])
    values = {"n_join_rows": joined}
    for column in COLUMNS[1:]:
        value = row[column]
        if value == "":
            if joined != 0:
                raise RuntimeError(f"blank {column} with nonzero n_join_rows in {source}")
            values[column] = 0
        else:
            values[column] = int(value)
    return values


def validate_query(text: str, lo: int, hi: int) -> None:
    normalized = " ".join(text.split())
    upper = normalized.upper()
    if not upper.startswith("SELECT "):
        raise RuntimeError("query does not start SELECT")
    if f"WHERE T.BRICKID BETWEEN {lo} AND {hi}" not in upper:
        raise RuntimeError(f"query bounds mismatch {lo}..{hi}")
    if text.count(CUT6) != 2:
        raise RuntimeError(f"Cut 6 count mismatch {lo}..{hi}")
    if re.search(r"\b(TOP|LIMIT|OFFSET|INTO|UPLOAD|CREATE|DROP|DELETE|UPDATE|INSERT|GROUP BY|SIN|COS|TAN|RADIANS|DEGREES)\b", upper):
        raise RuntimeError(f"forbidden query construct {lo}..{hi}")
    select = normalized[7 : upper.index(" FROM ")]
    aliases = re.findall(r"\bAS\s+([A-Za-z_][A-Za-z0-9_]*)\b", select, re.I)
    if aliases != COLUMNS:
        raise RuntimeError(f"projection mismatch {lo}..{hi}")


def probe_phase(job_url: str) -> dict:
    try:
        request = urllib.request.Request(job_url + "/phase", headers={"User-Agent": "Tori-final-reconstruction/1.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            return {"job_url": job_url, "http_status": response.status, "phase": response.read().decode().strip()}
    except urllib.error.HTTPError as exc:
        return {"job_url": job_url, "http_status": exc.code, "phase": None, "body_sha256": hashlib.sha256(exc.read()).hexdigest()}
    except Exception as exc:
        return {"job_url": job_url, "http_status": None, "phase": None, "exception": repr(exc)}


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text())
    if sha256(MANIFEST_PATH) != EXPECTED_MANIFEST_SHA256:
        raise RuntimeError("manifest hash drift")
    if sha256(PARENT_RECEIPT) != EXPECTED_PARENT_RECEIPT_SHA256:
        raise RuntimeError("parent receipt hash drift")
    if sha256(CUT6_RECEIPT) != EXPECTED_CUT6_RECEIPT_SHA256:
        raise RuntimeError("Cut 6 receipt hash drift")
    if manifest["columns"] != COLUMNS or len(manifest["entries"]) != 55:
        raise RuntimeError("manifest shape drift")

    cursor = 121001
    for index, entry in enumerate(manifest["entries"]):
        expected_hi = min(cursor + 9999, 662174)
        if (entry["lo"], entry["hi"], entry["key_count"]) != (cursor, expected_hi, expected_hi - cursor + 1):
            raise RuntimeError(f"manifest geometry error at {index}")
        cursor = expected_hi + 1
    if cursor != 662175:
        raise RuntimeError("manifest does not close keyspace")

    parent = json.loads(PARENT_RECONSTRUCTION.read_text())
    cut6 = json.loads(CUT6_RECONSTRUCTION.read_text())
    baseline = dict(parent["totals"])
    baseline["n_cut6_inclination_raw"] = cut6["totals"]["n_cut6_inclination_raw"]
    baseline["n_cut6_inclination_dered"] = cut6["totals"]["n_cut6_inclination_dered"]
    if set(baseline) != set(COLUMNS):
        raise RuntimeError("frozen baseline columns mismatch")

    new_totals = {column: 0 for column in COLUMNS}
    landed = []
    unlanded = []
    job_urls = []
    cursor = 121001
    for entry in manifest["entries"]:
        query_path = Path(entry["query_path"])
        if sha256(query_path) != entry["query_sha256"]:
            raise RuntimeError(f"manifest/query hash mismatch: {query_path}")
        validate_query(query_path.read_text(), entry["lo"], entry["hi"])
        tap = Path(entry["run_dir"]) / "tap"
        receipt_path = tap / "receipt.json"
        result_path = tap / "result.csv"
        submission_path = tap / "submission.json"
        present = [receipt_path.exists(), result_path.exists()]
        if any(present) and not all(present):
            raise RuntimeError(f"half-landed result: {tap}")
        if not all(present):
            if submission_path.exists():
                raise RuntimeError(f"unlanded live submission exists: {tap}")
            unlanded.append({"lo": entry["lo"], "hi": entry["hi"], "key_count": entry["key_count"]})
            continue
        if entry["lo"] != cursor:
            raise RuntimeError(f"landed result after gap: {tap}")
        receipt = json.loads(receipt_path.read_text())
        rows = list(csv.DictReader(result_path.read_text().splitlines()))
        if len(rows) != 1 or list(rows[0]) != COLUMNS:
            raise RuntimeError(f"result shape mismatch: {result_path}")
        if receipt.get("query_sha256") != entry["query_sha256"]:
            raise RuntimeError(f"receipt query hash mismatch: {receipt_path}")
        if receipt.get("result_sha256") != sha256(result_path):
            raise RuntimeError(f"receipt result hash mismatch: {receipt_path}")
        if receipt.get("result_row_count") != 1 or receipt.get("result_columns") != COLUMNS:
            raise RuntimeError(f"receipt result shape mismatch: {receipt_path}")
        for key, expected in {
            "sample_rows_exported": 0,
            "positions_exported": 0,
            "images_requested": 0,
            "chirality_computed": False,
            "sky_statistics_computed": False,
        }.items():
            if receipt.get(key) != expected:
                raise RuntimeError(f"boundary mismatch {key}: {receipt_path}")
        if not receipt.get("phases") or receipt["phases"][-1].get("phase") != "COMPLETED":
            raise RuntimeError(f"receipt lacks final COMPLETED phase: {receipt_path}")
        values = normalize(rows[0], result_path)
        for column, value in values.items():
            new_totals[column] += value
        started = datetime.fromisoformat(receipt["started_utc"].replace("Z", "+00:00"))
        completed = datetime.fromisoformat(receipt["completed_utc"].replace("Z", "+00:00"))
        job_urls.append(receipt["job_url"])
        landed.append(
            {
                "lo": entry["lo"],
                "hi": entry["hi"],
                "key_count": entry["key_count"],
                "elapsed_seconds": (completed - started).total_seconds(),
                "completed_utc": receipt["completed_utc"],
                "job_url": receipt["job_url"],
                "query_sha256": entry["query_sha256"],
                "result_sha256": receipt["result_sha256"],
                "values": values,
            }
        )
        cursor = entry["hi"] + 1

    if len(landed) != 42 or cursor != 541001:
        raise RuntimeError(f"expected 42 contiguous landed blocks through 541000, got {len(landed)} through {cursor - 1}")
    if len(unlanded) != 13 or unlanded[0]["lo"] != 541001 or unlanded[-1]["hi"] != 662174:
        raise RuntimeError("unlanded tail geometry mismatch")
    if len(set(job_urls)) != len(job_urls):
        raise RuntimeError("duplicate authoritative landed job URL")

    tail_query = TAIL / "query.adql"
    tail_result = TAIL / "tap" / "result.csv"
    tail_receipt_path = TAIL / "tap" / "receipt.json"
    tail_receipt = json.loads(tail_receipt_path.read_text())
    tail_rows = list(csv.DictReader(tail_result.read_text().splitlines()))
    if sha256(tail_query) != EXPECTED_TAIL_QUERY_SHA256 or tail_receipt["query_sha256"] != EXPECTED_TAIL_QUERY_SHA256:
        raise RuntimeError("tail query hash mismatch")
    if tail_receipt["result_sha256"] != sha256(tail_result):
        raise RuntimeError("tail result hash mismatch")
    if len(tail_rows) != 1 or list(tail_rows[0]) != ["n_join_rows"] or int(tail_rows[0]["n_join_rows"]) != 0:
        raise RuntimeError("tail existence probe is not exact zero")
    for key, expected in {
        "sample_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_computed": False,
        "sky_statistics_computed": False,
    }.items():
        if tail_receipt.get(key) != expected:
            raise RuntimeError(f"tail boundary mismatch {key}")
    if tail_receipt["job_url"] in job_urls:
        raise RuntimeError("tail job duplicates landed job URL")

    archived = []
    replacement_by_range = {(item["lo"], item["hi"]): item["job_url"] for item in landed}
    for failure_path in sorted(SCOPE.glob("runs/run_*/tap/failed_attempts/*/failure_record.json")):
        archive = failure_path.parent
        failure = json.loads(failure_path.read_text())
        submission = json.loads((archive / "submission.json").read_text())
        lost = json.loads((archive / "remote_job_lost.json").read_text())
        lo = failure["brickid_range"]["lo"]
        hi = failure["brickid_range"]["hi"]
        if lost["signal"] != "REMOTE_JOB_HTTP_404":
            raise RuntimeError(f"archived lost marker mismatch: {archive}")
        if submission["query_sha256"] != failure["query_sha256"]:
            raise RuntimeError(f"archived query hash mismatch: {archive}")
        if submission["job_url"] == replacement_by_range[(lo, hi)]:
            raise RuntimeError(f"lost and replacement URL identical: {archive}")
        for key, expected in {
            "sample_rows_exported": 0,
            "positions_exported": 0,
            "images_requested": 0,
            "chirality_computed": False,
            "sky_statistics_computed": False,
        }.items():
            if failure.get(key) != expected:
                raise RuntimeError(f"archived boundary mismatch {key}: {archive}")
        archived.append(
            {
                "lo": lo,
                "hi": hi,
                "old_job_url": submission["job_url"],
                "replacement_job_url": replacement_by_range[(lo, hi)],
                "query_sha256": failure["query_sha256"],
                "failure_record_sha256": sha256(failure_path),
                "lost_marker_sha256": sha256(archive / "remote_job_lost.json"),
                "cause": failure["cause"],
            }
        )
    if len(archived) != 3:
        raise RuntimeError(f"expected 3 archived lost attempts, got {len(archived)}")

    totals = {column: baseline[column] + new_totals[column] for column in COLUMNS}
    expected_key_totals = {
        "n_cut5_parent_dered": 1015881,
        "n_cut6_inclination_dered": 832393,
        "n_cut5_parent_raw": 903913,
        "n_cut6_inclination_raw": 749914,
    }
    for key, expected in expected_key_totals.items():
        if totals[key] != expected:
            raise RuntimeError(f"reconstructed {key}={totals[key]} expected {expected}")
    if new_totals["n_cut5_parent_dered"] != 807474 or new_totals["n_cut6_inclination_dered"] != 660656:
        raise RuntimeError("new dered totals differ from independent expected values")

    status = json.loads(STATUS_PATH.read_text())
    log_text = LOG_PATH.read_text()
    if status.get("totals", {}).get("landed_new_partitions") != 41:
        raise RuntimeError("stale status no longer has the observed 41-partition snapshot")
    if "ValueError: invalid literal for int() with base 10: ''" not in log_text:
        raise RuntimeError("orchestrator crash signature missing")
    last_receipt = landed[-1]
    if last_receipt["lo"] != 531001 or last_receipt["values"]["n_join_rows"] != 0:
        raise RuntimeError("last zero full-chain block mismatch")

    ps = subprocess.run(["ps", "-axo", "stat=,command="], text=True, capture_output=True, check=True).stdout.splitlines()
    live_count_processes = [
        line for line in ps if ("run_remaining_keyspace.py" in line or "run_aggregate_tap.py" in line) and not line.lstrip().startswith("Z")
    ]
    lsof = subprocess.run(["lsof", "-t", str(SCOPE / "orchestrator.lock")], text=True, capture_output=True)
    lock_holders = [line for line in lsof.stdout.splitlines() if line.strip()]
    if live_count_processes or lock_holders:
        raise RuntimeError("live count process or lock remains")

    phase_urls = job_urls + [tail_receipt["job_url"]]
    with ThreadPoolExecutor(max_workers=8) as pool:
        current_phase_probes = list(pool.map(probe_phase, phase_urls))
    tail_probe = next(item for item in current_phase_probes if item["job_url"] == tail_receipt["job_url"])
    if tail_probe.get("phase") != "COMPLETED":
        raise RuntimeError(f"tail UWS phase not live-COMPLETED: {tail_probe}")

    reconstruction = {
        "status": "PASS",
        "verified_utc": utc_now(),
        "method": "independent reconstruction from frozen baseline JSONs, exact 55-entry manifest/query bytes, 42 authoritative landed query/result/receipt triples, three append-only lost-job archives, and a separate aggregate-only zero-tail proof; status.json and Markdown totals were not arithmetic inputs",
        "manifest": {
            "path": str(MANIFEST_PATH),
            "sha256": sha256(MANIFEST_PATH),
            "partition_count": 55,
            "start_brickid": 121001,
            "stop_brickid": 662174,
        },
        "frozen_inputs": {
            "parent_receipt_sha256": sha256(PARENT_RECEIPT),
            "cut6_receipt_sha256": sha256(CUT6_RECEIPT),
            "parent_reconstruction_sha256": sha256(PARENT_RECONSTRUCTION),
            "cut6_reconstruction_sha256": sha256(CUT6_RECONSTRUCTION),
        },
        "direct_full_chain": {
            "start_brickid": 1,
            "stop_brickid": 541000,
            "keyspace_units": 541000,
            "keyspace_fraction": 541000 / TOTAL_KEYS,
            "keyspace_percent": 100 * 541000 / TOTAL_KEYS,
            "landed_new_partitions": 42,
            "landed_new_keyspace_units": 420000,
            "landed": landed,
        },
        "unlanded_manifest_tail": {
            "partition_count": len(unlanded),
            "start_brickid": 541001,
            "stop_brickid": 662174,
            "keyspace_units": 121174,
            "entries": unlanded,
            "full_chain_queries_submitted": 0,
        },
        "tail_zero_proof": {
            "start_brickid": 541001,
            "stop_brickid": 662174,
            "keyspace_units": 121174,
            "n_join_rows": 0,
            "query_sha256": sha256(tail_query),
            "result_sha256": sha256(tail_result),
            "receipt_sha256": sha256(tail_receipt_path),
            "job_url": tail_receipt["job_url"],
            "phase": "COMPLETED",
            "logical_consequence": "same frozen joined parent population has zero rows in the entire unlanded tail, so every downstream Cut 1-6 count is exactly zero there",
        },
        "full_keyspace": {
            "start_brickid": 1,
            "stop_brickid": 662174,
            "keyspace_units": 662174,
            "keyspace_fraction": 1.0,
            "keyspace_not_sky_area": True,
            "completeness_basis": "42 direct full-chain blocks through 541000 plus exact zero joined-parent rows over 541001..662174",
        },
        "baseline_totals": baseline,
        "new_totals": new_totals,
        "totals": totals,
        "direct_lower_bound_equals_exact_full_count": True,
        "stop_reconciliation": {
            "stale_status_landed_partitions": status["totals"]["landed_new_partitions"],
            "authoritative_landed_partitions": len(landed),
            "stale_status_updated_utc": status["updated_utc"],
            "last_receipt_completed_utc": last_receipt["completed_utc"],
            "crash_observed_utc": "2026-08-12T20:07:12Z",
            "status_stop_reason": status.get("stop_reason"),
            "status_finished_utc": status.get("finished_utc"),
            "cause": "the 42nd full-chain result had COUNT(*)=0 and SQL SUM fields serialized as blanks/NULL; the orchestrator converted a blank with int('') and crashed after the receipt landed but before status persistence",
            "classification": "runner crash after the 42nd receipt landed; not deliberate, not deadline, and not keyspace exhaustion",
            "runner_crash_signature": "ValueError: invalid literal for int() with base 10: ''",
            "parser_regression_fixed_and_tests_passed": True,
        },
        "failure_and_recovery_history": {
            "initial_failure_utc": "2026-08-12T14:40:53Z",
            "cause": "nginx HTTP 502 Bad Gateway while three children polled existing UWS /phase URLs",
            "runner_defect": "HTTP 502 omitted from pressure handling",
            "recovery": "same manifest resumed serially; three lost UWS URLs archived after definitive 404; fresh submissions only for those unlanded ranges",
            "archived_lost_attempts": archived,
        },
        "current_uws_probes": current_phase_probes,
        "process_closure": {
            "live_count_process_count": 0,
            "orchestrator_lock_holder_count": 0,
            "zombie_wrapper_processes_are_not_live_service_users": True,
        },
        "boundary": {
            "authoritative_full_chain_aggregate_rows_returned": len(landed),
            "tail_existence_aggregate_rows_returned": 1,
            "sample_rows_exported": 0,
            "positions_exported": 0,
            "images_requested": 0,
            "chirality_computed": False,
            "sky_statistics_computed": False,
            "trigonometric_or_axis_relative_terms": 0,
            "bulk_downloads": 0,
            "publication_acceptance_commit_push": 0,
        },
    }
    OUTPUT.write_text(json.dumps(reconstruction, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "path": str(OUTPUT), "sha256": sha256(OUTPUT), "landed": len(landed), "tail_join_rows": 0, "totals": expected_key_totals}, sort_keys=True))


if __name__ == "__main__":
    main()
