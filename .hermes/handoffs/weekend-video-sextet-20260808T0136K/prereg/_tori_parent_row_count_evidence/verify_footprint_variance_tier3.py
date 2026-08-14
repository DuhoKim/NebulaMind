#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import math
import re
from decimal import Decimal
from pathlib import Path

import numpy as np
from astropy.io import fits

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
SCOPE = ROOT / "footprint_variance_brick_counts_20260814"
RECEIPT = PREREG / "TORI_FOOTPRINT_VARIANCE_RECEIPT.md"
GLOBAL_ATTEMPT = PREREG / "TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md"
PARTITION_ATTEMPT = PREREG / "TORI_FOOTPRINT_VARIANCE_PARTITIONED_ATTEMPT_20260814.md"
ORDINARY_GUARD = ROOT / "run_aggregate_tap.py"
EXPECTED_GUARD_SHA = "228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51"
EXPECTED_STATIC_SHA = "863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a"
EXPECTED_GLOBAL_ATTEMPT_SHA = "ef995652531d35cf3dc68df542661f9c503b571be9d34e4423de0347c63bf20e"
EXPECTED_PARTITION_ATTEMPT_SHA = "f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289"
EXPECTED_POPULATION = 832393
AXIS_RA_DEG = 216.984434295527
AXIS_DEC_DEG = 32.060611193471
BANNED_QUERY = re.compile(
    r"\b(SIN|COS|TAN|ASIN|ACOS|ATAN|RADIANS|DEGREES|COSTHETA|AXIS|THETA|DIPOLE|"
    r"CHIRALITY|HANDEDNESS|CLOCKWISE|COUNTERCLOCKWISE|CW|CCW|SPIN)\b",
    re.IGNORECASE,
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_partition(path: Path, lo: int, hi: int) -> list[tuple[int, int]]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["brickid", "n_cut6_dered"]:
            raise RuntimeError(f"columns drift: {path}")
        rows: list[tuple[int, int]] = []
        previous = lo - 1
        for row in reader:
            brickid = int(row["brickid"])
            count = int(row["n_cut6_dered"])
            if not lo <= brickid <= hi or brickid <= previous or count <= 0:
                raise RuntimeError(f"invalid grouped row: {path} {row}")
            rows.append((brickid, count))
            previous = brickid
    return rows


def independent_geometry(counts: dict[int, int], static_path: Path) -> dict:
    count_ids = np.array(sorted(counts), dtype=np.int64)
    weights = np.array([counts[int(brickid)] for brickid in count_ids], dtype=np.int64)
    with fits.open(static_path, memmap=False) as hdul:
        table = getattr(hdul[1], "data", None)
        if table is None:
            raise RuntimeError("static product lacks table")
        static_ids = np.asarray(table["brickid"], dtype=np.int64)
        order = np.argsort(static_ids)
        sorted_ids = static_ids[order]
        indices = np.searchsorted(sorted_ids, count_ids)
        if np.any(indices >= len(sorted_ids)) or not np.array_equal(sorted_ids[indices], count_ids):
            raise RuntimeError("independent join found missing count BRICKIDs")
        source_indices = order[indices]
        ra = np.deg2rad(np.asarray(table["ra"][source_indices], dtype=np.float64))
        dec = np.deg2rad(np.asarray(table["dec"][source_indices], dtype=np.float64))
    axis_ra = math.radians(AXIS_RA_DEG)
    axis_dec = math.radians(AXIS_DEC_DEG)
    axis = np.array(
        [math.cos(axis_dec) * math.cos(axis_ra), math.cos(axis_dec) * math.sin(axis_ra), math.sin(axis_dec)],
        dtype=np.float64,
    )
    centers = np.column_stack((np.cos(dec) * np.cos(ra), np.cos(dec) * np.sin(ra), np.sin(dec)))
    values = np.clip(centers @ axis, -1.0, 1.0)
    population = int(weights.sum(dtype=np.int64))
    first = np.sum(weights.astype(np.longdouble) * values.astype(np.longdouble), dtype=np.longdouble)
    second_sum = np.sum(weights.astype(np.longdouble) * values.astype(np.longdouble) ** 2, dtype=np.longdouble)
    mean = float(first / population)
    second = float(second_sum / population)
    variance = second - mean * mean
    return {
        "population": population,
        "nonempty_bricks": len(counts),
        "mean_cos_theta_center": mean,
        "mean_cos2_theta_center": second,
        "variance_cos_theta_center": variance,
    }


def classify(value: float) -> str:
    variance = Decimal(str(value))
    if variance - Decimal("0.15") >= Decimal("0.0248"):
        return "PASS"
    if variance + Decimal("0.0124") < Decimal("0.15"):
        return "FAIL"
    return "INCONCLUSIVE"


def main() -> None:
    required = [
        SCOPE / "manifest.json",
        SCOPE / "FINAL_COUNTS_OUTCOME.json",
        SCOPE / "combined_per_brick_counts.csv",
        SCOPE / "LOCAL_GEOMETRY_RESULT.json",
        SCOPE / "RECONSTRUCTION_CUSTODY.json",
        RECEIPT,
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise RuntimeError(f"final Tier-3 artifacts incomplete: {missing}")
    if sha(ORDINARY_GUARD) != EXPECTED_GUARD_SHA:
        raise RuntimeError("ordinary guard drift")
    if sha(SCOPE / "static/survey-bricks-dr10-south.fits.gz") != EXPECTED_STATIC_SHA:
        raise RuntimeError("static product drift")
    if sha(GLOBAL_ATTEMPT) != EXPECTED_GLOBAL_ATTEMPT_SHA or sha(PARTITION_ATTEMPT) != EXPECTED_PARTITION_ATTEMPT_SHA:
        raise RuntimeError("preserved attempt receipt drift")

    manifest = json.loads((SCOPE / "manifest.json").read_text())
    outcome = json.loads((SCOPE / "FINAL_COUNTS_OUTCOME.json").read_text())
    result = json.loads((SCOPE / "LOCAL_GEOMETRY_RESULT.json").read_text())
    if len(manifest["entries"]) != 67 or not outcome["coverage"]["full_coverage"]:
        raise RuntimeError("full 67-partition coverage absent")
    counts: dict[int, int] = {}
    total_group_rows = 0
    total_population = 0
    for entry in manifest["entries"]:
        query_path = Path(entry["query_path"])
        query = query_path.read_text()
        if sha(query_path) != entry["query_sha256"]:
            raise RuntimeError(f"query hash drift: {query_path}")
        if BANNED_QUERY.search(query) or "t.ra" in query.lower() or "t.dec" in query.lower():
            raise RuntimeError(f"forbidden server query term: {query_path}")
        if query.count("COUNT(*) AS n_cut6_dered") != 1 or query.count("GROUP BY t.brickid") != 1:
            raise RuntimeError(f"query shape drift: {query_path}")
        tap = Path(entry["run_dir"]) / "tap"
        receipt_path = tap / "receipt.json"
        result_path = tap / "result.csv"
        partition_receipt = json.loads(receipt_path.read_text())
        if partition_receipt["query_sha256"] != entry["query_sha256"] or partition_receipt["result_sha256"] != sha(result_path):
            raise RuntimeError(f"partition receipt hash mismatch: {tap}")
        for name, expected in {
            "trigonometric_terms_in_query": 0,
            "axis_terms_in_query": 0,
            "object_rows_exported": 0,
            "positions_exported": 0,
            "images_requested": 0,
            "chirality_computed": False,
            "handedness_spin_cw_ccw_computed": False,
            "sky_statistics_computed_server_side": False,
        }.items():
            if partition_receipt[name] != expected:
                raise RuntimeError(f"boundary violation {name}: {tap}")
        rows = parse_partition(result_path, entry["lo"], entry["hi"])
        if len(rows) != partition_receipt["aggregate_group_rows_returned"]:
            raise RuntimeError(f"aggregate row count mismatch: {tap}")
        for brickid, count in rows:
            if brickid in counts:
                raise RuntimeError(f"duplicate BRICKID across partitions: {brickid}")
            counts[brickid] = count
        total_group_rows += len(rows)
        total_population += sum(count for _, count in rows)
    if total_group_rows != outcome["coverage"]["aggregate_group_rows"]:
        raise RuntimeError("full aggregate-group row total mismatch")
    if total_population != EXPECTED_POPULATION or outcome["coverage"]["population"] != EXPECTED_POPULATION:
        raise RuntimeError("frozen population mismatch")

    with (SCOPE / "combined_per_brick_counts.csv").open(newline="") as handle:
        combined_rows = list(csv.DictReader(handle))
    combined = {int(row["brickid"]): int(row["n_cut6_dered"]) for row in combined_rows}
    if combined != counts:
        raise RuntimeError("combined per-brick table differs from 67 partition results")
    independent = independent_geometry(counts, SCOPE / "static/survey-bricks-dr10-south.fits.gz")
    for key in ("mean_cos_theta_center", "mean_cos2_theta_center", "variance_cos_theta_center"):
        if not math.isclose(independent[key], result[key], rel_tol=0.0, abs_tol=2e-14):
            raise RuntimeError(f"independent geometry mismatch {key}: {independent[key]} != {result[key]}")
    if independent["population"] != EXPECTED_POPULATION or independent["nonempty_bricks"] != result["nonempty_bricks"]:
        raise RuntimeError("independent population/brick count mismatch")
    verdict = classify(independent["variance_cos_theta_center"])
    if verdict != result["verdict"]:
        raise RuntimeError(f"independent verdict mismatch: {verdict} != {result['verdict']}")

    receipt = RECEIPT.read_text()
    literals = (
        f"**Verdict:** **{verdict}**",
        f"`{result['population']:,}` dered Cut-6 objects",
        f"`{result['nonempty_bricks']:,}`",
        f"`{result['variance_cos_theta_center']:.15f}`",
        "`|V_object - V_center| <= 0.0124`",
        "server-side trigonometric terms: **0**",
        "server-side axis/angular terms: **0**",
        "object rows exported: **0**",
        "object positions exported: **0**",
        "publication/acceptance/commit/push: **0**",
        sha(SCOPE / "manifest.json"),
        sha(SCOPE / "FINAL_COUNTS_OUTCOME.json"),
        sha(SCOPE / "combined_per_brick_counts.csv"),
        sha(SCOPE / "LOCAL_GEOMETRY_RESULT.json"),
        EXPECTED_GLOBAL_ATTEMPT_SHA,
        EXPECTED_PARTITION_ATTEMPT_SHA,
    )
    for literal in literals:
        if literal not in receipt:
            raise RuntimeError(f"receipt missing required literal: {literal}")
    verification = {
        "status": "PASS",
        "manifest_sha256": sha(SCOPE / "manifest.json"),
        "receipt_sha256": sha(RECEIPT),
        "partition_count": 67,
        "aggregate_group_rows": total_group_rows,
        "population": total_population,
        "nonempty_bricks": len(counts),
        "independent_geometry": independent,
        "verdict": verdict,
        "ordinary_guard_sha256": sha(ORDINARY_GUARD),
        "trigonometric_terms_in_queries": 0,
        "axis_terms_in_queries": 0,
        "object_rows": 0,
        "positions": 0,
    }
    output = SCOPE / "FINAL_INDEPENDENT_VERIFICATION.json"
    output.write_text(json.dumps(verification, indent=2, sort_keys=True) + "\n")
    print(
        f"tier3_independent_verification=PASS partitions=67 population={total_population} "
        f"nonempty_bricks={len(counts)} variance={independent['variance_cos_theta_center']:.15f} verdict={verdict}"
    )


if __name__ == "__main__":
    main()
