#!/usr/bin/env python3
"""Independently verify BS-2 product coverage and the 8-of-10 gate."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCOPE = ROOT / "bs2_covariate_coverage_20260814"
DIRECT_PATH = SCOPE / "FINAL_COVERAGE.json"
BRICK_PATH = SCOPE / "BRICK_PRODUCT_COVERAGE.json"
ARM_PATH = SCOPE / "ARM_CONTRAST_PRODUCT_AUDIT.json"
OUTPUT_PATH = SCOPE / "FINAL_BS2_VERIFICATION.json"
EXPECTED_POPULATION = 832393
MINIMUM_ACCEPTED = 100000
COVERAGE_THRESHOLD = 0.95
DIRECT_RESULT_COLUMNS = [
    "n_total",
    "n_extinction",
    "n_angular_size",
    "n_axis_ratio",
    "n_colour",
    "n_magnitude",
    "n_flag_fields",
    "n_photoz",
]
CORE_ORDER = [
    "imaging_depth",
    "seeing_psf",
    "galactic_extinction",
    "stellar_density",
    "crowding",
    "angular_size",
    "axis_ratio",
    "colour_g_minus_r",
    "magnitude_r",
    "arm_contrast",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def worst_case_accepted_coverage(parent: int, available: int, accepted_minimum: int) -> float:
    if parent <= 0 or accepted_minimum <= 0 or accepted_minimum > parent:
        raise ValueError("invalid parent/accepted population")
    if available < 0 or available > parent:
        raise ValueError("invalid available count")
    missing = parent - available
    missing_in_accepted = min(missing, accepted_minimum)
    return (accepted_minimum - missing_in_accepted) / accepted_minimum


def build_core_matrix(
    parent: int,
    accepted_minimum: int,
    available: dict[str, int],
    products_defined: dict[str, bool],
) -> list[dict]:
    if set(available) != set(CORE_ORDER) or set(products_defined) != set(CORE_ORDER):
        raise ValueError("core covariate key set drift")
    rows = []
    for name in CORE_ORDER:
        lower = worst_case_accepted_coverage(parent, available[name], accepted_minimum)
        product_defined = bool(products_defined[name])
        survives = product_defined and lower >= COVERAGE_THRESHOLD
        if not product_defined:
            reason = "product_not_defined"
        elif lower < COVERAGE_THRESHOLD:
            reason = "worst_case_accepted_coverage_below_0.95"
        else:
            reason = None
        rows.append(
            {
                "covariate": name,
                "product_defined": product_defined,
                "eligible_parent_available": available[name],
                "eligible_parent_missing": parent - available[name],
                "worst_case_accepted_coverage": lower,
                "threshold": COVERAGE_THRESHOLD,
                "survives": survives,
                "drop_reason": reason,
            }
        )
    return rows


def independent_direct_census(scope: Path) -> dict:
    manifest_path = scope / "manifest.json"
    if not manifest_path.exists():
        raise RuntimeError("independent census manifest is missing")
    manifest = json.loads(manifest_path.read_text())
    entries = manifest.get("entries", [])
    if manifest.get("partition_count") != len(entries) or not entries:
        raise RuntimeError("independent census manifest shape mismatch")
    totals = {name: 0 for name in DIRECT_RESULT_COLUMNS}
    for entry in entries:
        query_path = Path(entry["query_path"])
        query_bytes = query_path.read_bytes()
        query_hash = hashlib.sha256(query_bytes).hexdigest()
        if query_hash != entry["query_sha256"]:
            raise RuntimeError(f"independent query hash mismatch: {query_path}")
        query = " ".join(query_bytes.decode().upper().split())
        for alias in DIRECT_RESULT_COLUMNS:
            if query.count(f" AS {alias.upper()}") != 1:
                raise RuntimeError(f"independent query column drift: {query_path} {alias}")
        if " GROUP BY " in f" {query} " or "T.RA" in query or "T.DEC" in query:
            raise RuntimeError(f"independent query boundary violation: {query_path}")
        if re.search(r"\b(SIN|COS|TAN|RADIANS|DEGREES|COSTHETA|CHIRALITY|ARM_CONTRAST)\b", query):
            raise RuntimeError(f"independent query signal term: {query_path}")
        tap = Path(entry["run_dir"]) / "tap"
        receipt_path = tap / "receipt.json"
        result_path = tap / "result.csv"
        if not receipt_path.exists() or not result_path.exists():
            raise RuntimeError(f"independent census partition incomplete: {tap}")
        receipt = json.loads(receipt_path.read_text())
        result_hash = sha256_path(result_path)
        if receipt.get("query_sha256") != query_hash or receipt.get("result_sha256") != result_hash:
            raise RuntimeError(f"independent receipt hash mismatch: {tap}")
        if receipt.get("result_columns") != DIRECT_RESULT_COLUMNS or receipt.get("result_row_count") != 1:
            raise RuntimeError(f"independent receipt shape mismatch: {tap}")
        for name, expected in {
            "sample_rows_exported": 0,
            "positions_exported": 0,
            "images_requested": 0,
            "chirality_computed": False,
            "sky_statistics_computed": False,
        }.items():
            if receipt.get(name) != expected:
                raise RuntimeError(f"independent receipt boundary mismatch {name}: {tap}")
        rows = list(csv.DictReader(result_path.read_text().splitlines()))
        if len(rows) != 1 or list(rows[0]) != DIRECT_RESULT_COLUMNS:
            raise RuntimeError(f"independent result shape mismatch: {tap}")
        for name in DIRECT_RESULT_COLUMNS:
            totals[name] += int(rows[0][name] or 0)
    population = totals["n_total"]
    if population <= 0:
        raise RuntimeError("independent census population is not positive")
    coverage = {
        name.removeprefix("n_"): {
            "count": totals[name],
            "fraction": totals[name] / population,
        }
        for name in DIRECT_RESULT_COLUMNS[1:]
    }
    return {
        "manifest_sha256": sha256_path(manifest_path),
        "partition_count": len(entries),
        "aggregate_rows_returned": len(entries),
        "population": population,
        "coverage": coverage,
    }


def verify_actual(direct_path: Path, brick_path: Path, arm_path: Path) -> dict:
    for path in (direct_path, brick_path, arm_path):
        if not path.exists():
            raise RuntimeError(f"refuse incomplete BS-2 verification; missing {path}")
    direct = json.loads(direct_path.read_text())
    independent = independent_direct_census(direct_path.parent)
    brick = json.loads(brick_path.read_text())
    arm = json.loads(arm_path.read_text())
    if direct.get("partition_count") != 67 or direct.get("aggregate_rows_returned") != 67:
        raise RuntimeError("direct census is not complete at 67/67")
    if direct.get("population") != EXPECTED_POPULATION or direct.get("population_matches_frozen_cut6") is not True:
        raise RuntimeError("direct census population mismatch")
    for name in ("partition_count", "aggregate_rows_returned", "population", "coverage"):
        if direct.get(name) != independent.get(name):
            raise RuntimeError(f"orchestrator/independent direct-census mismatch: {name}")
    for name, expected in {
        "sample_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_or_morphology_computed": False,
        "sky_statistic_computed": False,
    }.items():
        if direct.get(name) != expected:
            raise RuntimeError(f"direct census boundary mismatch: {name}")
    if brick.get("population") != EXPECTED_POPULATION or brick.get("nonempty_bricks") != 270577:
        raise RuntimeError("brick-product population mismatch")
    if brick.get("missing_brick_centres_or_summary_rows") != 0:
        raise RuntimeError("brick-summary join is incomplete")
    if brick.get("object_rows_read_or_exported") != 0 or brick.get("positions_read_or_exported") != 0:
        raise RuntimeError("brick-product boundary mismatch")
    if arm.get("arm_contrast_product_defined") is not False:
        raise RuntimeError("arm-contrast audit unexpectedly found a frozen product")

    coverage = direct["coverage"]
    available = {
        "imaging_depth": int(brick["coverage"]["imaging_depth_psfdepth_r"]["count"]),
        "seeing_psf": int(brick["coverage"]["seeing_psfsize_r"]["count"]),
        "galactic_extinction": int(coverage["extinction"]["count"]),
        "stellar_density": EXPECTED_POPULATION,
        "crowding": EXPECTED_POPULATION,
        "angular_size": int(coverage["angular_size"]["count"]),
        "axis_ratio": int(coverage["axis_ratio"]["count"]),
        "colour_g_minus_r": int(coverage["colour"]["count"]),
        "magnitude_r": int(coverage["magnitude"]["count"]),
        "arm_contrast": 0,
    }
    products_defined = {name: True for name in CORE_ORDER}
    products_defined["arm_contrast"] = False
    matrix = build_core_matrix(EXPECTED_POPULATION, MINIMUM_ACCEPTED, available, products_defined)
    basis = {
        "imaging_depth": "pinned survey-bricks-dr10-south PSFDEPTH_R weighted by exact Cut-6 per-brick aggregate counts",
        "seeing_psf": "pinned survey-bricks-dr10-south PSFSIZE_R weighted by exact Cut-6 per-brick aggregate counts",
        "galactic_extinction": "DR10.1 South sweep EBV aggregate validity census",
        "stellar_density": "Gaia DR3 gaia_source PHOT_G_MEAN_MAG<19 counts on complete Nside=128 RING ICRS grid; zero is a defined count",
        "crowding": "DR10.1 South sweep neighbour count within 30 arcsec; every accepted object necessarily has the bound catalogue coordinate used for its cutout",
        "angular_size": "DR10.1 South sweep SHAPE_R aggregate validity census",
        "axis_ratio": "DR10.1 South sweep SHAPE_E1/SHAPE_E2 aggregate validity census and frozen b/a transform",
        "colour_g_minus_r": "DR10.1 South sweep positive FLUX_G/FLUX_R and MW_TRANSMISSION_G/R aggregate validity census",
        "magnitude_r": "DR10.1 South sweep positive FLUX_R and MW_TRANSMISSION_R aggregate validity census",
        "arm_contrast": "no s(x)/u(x)/arm-contrast product in the frozen BS-3 appendix; dropped",
    }
    for row in matrix:
        row["coverage_basis"] = basis[row["covariate"]]
    survivors = sum(bool(row["survives"]) for row in matrix)

    photoz_available = int(coverage["photoz"]["count"])
    photoz_lower = worst_case_accepted_coverage(EXPECTED_POPULATION, photoz_available, MINIMUM_ACCEPTED)
    flag_fields_available = int(coverage["flag_fields"]["count"])
    result = {
        "recorded_utc": utc_now(),
        "status": "PASS" if survivors >= 8 else "FAIL",
        "validity_rule": "at least 8 of 10 core covariates have a defined product and worst-case coverage >=0.95 for any accepted sample with N>=100000",
        "eligible_parent_population": EXPECTED_POPULATION,
        "minimum_accepted_population": MINIMUM_ACCEPTED,
        "maximum_missing_for_95_percent_gate": 5000,
        "core_covariates": matrix,
        "surviving_core_covariates": survivors,
        "required_surviving_core_covariates": 8,
        "photoz_decision": {
            "decision": "INCLUDE_AS_CONDITIONAL_ELEVENTH_COVARIATE",
            "product": "DESI Legacy DR10.1 South 10.1-photo-z sweeps / ls_dr10.photo_z Z_PHOT_MEDIAN",
            "eligible_parent_available": photoz_available,
            "worst_case_accepted_coverage": photoz_lower,
            "survives_coverage_gate": photoz_lower >= COVERAGE_THRESHOLD,
            "not_counted_in_core_ten": True,
        },
        "deblend_flag_decision": {
            "selection_mask": "MASKBITS=0 (therefore BAILOUT bit 10 and SUB_BLOB bit 16, plus every other MASKBITS bit, are excluded)",
            "fitbits_field_available": flag_fields_available,
            "additional_fitbits_exclusion": "NONE",
            "deblend_quality_covariate": "DROPPED",
            "reason": "DR10 documents FITBITS as fit peculiarities, not a single deblend-quality scalar; adding a post-count subset would change the frozen parent without a preregistered interpretation",
        },
        "source_receipts": {
            "direct_coverage_sha256": sha256_path(direct_path),
            "independent_manifest_sha256": independent["manifest_sha256"],
            "brick_product_coverage_sha256": sha256_path(brick_path),
            "arm_contrast_audit_sha256": sha256_path(arm_path),
        },
        "object_rows": 0,
        "positions": 0,
        "images": 0,
        "chirality_or_morphology_labels": 0,
        "sky_statistics": 0,
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--direct", type=Path, default=DIRECT_PATH)
    parser.add_argument("--brick", type=Path, default=BRICK_PATH)
    parser.add_argument("--arm", type=Path, default=ARM_PATH)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()
    result = verify_actual(args.direct, args.brick, args.arm)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
