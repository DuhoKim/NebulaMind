#!/usr/bin/env python3
"""Reconstruct count-weighted Longo-axis brick-centre moments entirely locally."""
from __future__ import annotations

import csv
import hashlib
import json
import math
from decimal import Decimal
from pathlib import Path

from astropy.io import fits

ROOT = Path(__file__).resolve().parent
SCOPE = ROOT / "footprint_variance_brick_counts_20260814"
RUNS = SCOPE / "runs"
MANIFEST_PATH = SCOPE / "manifest.json"
FINAL_COUNTS_OUTCOME = SCOPE / "FINAL_COUNTS_OUTCOME.json"
STATIC_PRODUCT_PATH = SCOPE / "static" / "survey-bricks-dr10-south.fits.gz"
COMBINED_COUNTS_PATH = SCOPE / "combined_per_brick_counts.csv"
RESULT_PATH = SCOPE / "LOCAL_GEOMETRY_RESULT.json"
CUSTODY_PATH = SCOPE / "RECONSTRUCTION_CUSTODY.json"
STATIC_PRODUCT_SHA256 = "863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a"
EXPECTED_POPULATION = 832393
AXIS_RA_DEG = 216.984434295527
AXIS_DEC_DEG = 32.060611193471
THRESHOLD = Decimal("0.15")
ERROR_BRACKET = Decimal("0.0124")
TWICE_ERROR_BRACKET = Decimal("0.0248")


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def load_count_csvs(paths: list[Path]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for path in paths:
        with path.open(newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != ["brickid", "n_cut6_dered"]:
                raise RuntimeError(f"count result columns drift: {path}")
            for row in reader:
                try:
                    brickid = int(row["brickid"])
                    count = int(row["n_cut6_dered"])
                except (TypeError, ValueError) as exc:
                    raise RuntimeError(f"noninteger grouped count: {path}") from exc
                if brickid in counts:
                    raise RuntimeError(f"duplicate BRICKID across count results: {brickid}")
                if count <= 0:
                    raise RuntimeError(f"nonpositive grouped count: {brickid}")
                counts[brickid] = count
    return counts


def load_static_centers(path: Path, required_ids: set[int]) -> tuple[dict[int, tuple[float, float]], dict]:
    if sha256_path(path) != STATIC_PRODUCT_SHA256:
        raise RuntimeError("static brick-centre product hash drift")
    with fits.open(path, memmap=False) as hdul:
        table = getattr(hdul[1], "data", None)
        if table is None:
            raise RuntimeError("static brick product has no binary-table data extension")
        names = {name.lower(): name for name in table.names}
        if not {"brickid", "ra", "dec"}.issubset(names):
            raise RuntimeError(f"static brick product lacks required columns: {table.names}")
        brickids = table[names["brickid"]]
        ras = table[names["ra"]]
        decs = table[names["dec"]]
        centers: dict[int, tuple[float, float]] = {}
        seen_all: set[int] = set()
        for raw_id, raw_ra, raw_dec in zip(brickids, ras, decs):
            brickid = int(raw_id)
            if brickid in seen_all:
                raise RuntimeError(f"duplicate BRICKID in static product: {brickid}")
            seen_all.add(brickid)
            if brickid in required_ids:
                ra = float(raw_ra)
                dec = float(raw_dec)
                if not (math.isfinite(ra) and math.isfinite(dec) and 0.0 <= ra <= 360.0 and -90.0 <= dec <= 90.0):
                    raise RuntimeError(f"invalid brick centre for {brickid}")
                centers[brickid] = (ra, dec)
        missing = sorted(required_ids - centers.keys())
        if missing:
            raise RuntimeError(f"selected count BRICKIDs missing static centres: {missing[:20]}")
        metadata = {
            "static_table_rows": len(table),
            "static_unique_brickids": len(seen_all),
            "matched_nonempty_bricks": len(centers),
            "required_columns": [names["brickid"], names["ra"], names["dec"]],
        }
    return centers, metadata


def compute_weighted_geometry(
    counts: dict[int, int],
    centers: dict[int, tuple[float, float]],
    *,
    axis_ra_deg: float,
    axis_dec_deg: float,
) -> dict:
    if not counts:
        raise RuntimeError("no per-brick counts supplied")
    if set(counts) != set(centers):
        missing = sorted(set(counts) - set(centers))
        extra = sorted(set(centers) - set(counts))
        raise RuntimeError(f"count/centre key mismatch missing={missing[:10]} extra={extra[:10]}")
    axis_ra = math.radians(axis_ra_deg)
    axis_dec = math.radians(axis_dec_deg)
    axis = (
        math.cos(axis_dec) * math.cos(axis_ra),
        math.cos(axis_dec) * math.sin(axis_ra),
        math.sin(axis_dec),
    )
    weighted_first: list[float] = []
    weighted_second: list[float] = []
    population = 0
    minimum = 1.0
    maximum = -1.0
    for brickid in sorted(counts):
        count = counts[brickid]
        if count <= 0:
            raise RuntimeError(f"nonpositive count for BRICKID {brickid}")
        ra_deg, dec_deg = centers[brickid]
        ra = math.radians(ra_deg)
        dec = math.radians(dec_deg)
        center = (
            math.cos(dec) * math.cos(ra),
            math.cos(dec) * math.sin(ra),
            math.sin(dec),
        )
        value = math.fsum(axis_component * center_component for axis_component, center_component in zip(axis, center))
        value = max(-1.0, min(1.0, value))
        weighted_first.append(count * value)
        weighted_second.append(count * value * value)
        population += count
        minimum = min(minimum, value)
        maximum = max(maximum, value)
    mean = math.fsum(weighted_first) / population
    second = math.fsum(weighted_second) / population
    variance = second - mean * mean
    if variance < 0.0 and abs(variance) < 1e-15:
        variance = 0.0
    if not (0.0 <= variance <= 1.0):
        raise RuntimeError(f"computed variance outside mathematical bounds: {variance}")
    return {
        "population": population,
        "nonempty_bricks": len(counts),
        "axis_equatorial_degrees": {"ra": axis_ra_deg, "dec": axis_dec_deg},
        "axis_unit_vector": {"x": axis[0], "y": axis[1], "z": axis[2]},
        "mean_cos_theta_center": mean,
        "mean_cos2_theta_center": second,
        "variance_cos_theta_center": variance,
        "minimum_cos_theta_center": minimum,
        "maximum_cos_theta_center": maximum,
    }


def classify(variance: float) -> str:
    value = Decimal(str(variance))
    if value - THRESHOLD >= TWICE_ERROR_BRACKET:
        return "PASS"
    if value + ERROR_BRACKET < THRESHOLD:
        return "FAIL"
    return "INCONCLUSIVE"


def main() -> None:
    if not MANIFEST_PATH.exists() or not FINAL_COUNTS_OUTCOME.exists():
        raise RuntimeError("full grouped-count outcome not available")
    manifest = json.loads(MANIFEST_PATH.read_text())
    outcome = json.loads(FINAL_COUNTS_OUTCOME.read_text())
    if not outcome["coverage"]["full_coverage"]:
        raise RuntimeError("refuse local geometry from partial grouped-count coverage")
    if not outcome["population_matches_frozen_total"]:
        raise RuntimeError("refuse local geometry from population-mismatched grouped counts")
    result_paths: list[Path] = []
    for entry in manifest["entries"]:
        result_path = Path(entry["run_dir"]) / "tap" / "result.csv"
        if not result_path.exists():
            raise RuntimeError(f"missing grouped count result: {result_path}")
        result_paths.append(result_path)
    counts = load_count_csvs(result_paths)
    if sum(counts.values()) != EXPECTED_POPULATION:
        raise RuntimeError("combined grouped counts do not equal frozen Cut-6 population")
    centers, static_metadata = load_static_centers(STATIC_PRODUCT_PATH, set(counts))
    geometry = compute_weighted_geometry(counts, centers, axis_ra_deg=AXIS_RA_DEG, axis_dec_deg=AXIS_DEC_DEG)
    if geometry["population"] != EXPECTED_POPULATION:
        raise RuntimeError("geometry population drift")

    with COMBINED_COUNTS_PATH.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["brickid", "n_cut6_dered"])
        for brickid in sorted(counts):
            writer.writerow([brickid, counts[brickid]])
    variance = geometry["variance_cos_theta_center"]
    verdict = classify(variance)
    lower = max(0.0, variance - float(ERROR_BRACKET))
    upper = min(1.0, variance + float(ERROR_BRACKET))
    result = {
        "method": "Lana Tier 3 exact post-Cut-6 counts per brick; geometry local at frozen brick centres",
        **geometry,
        "brick_half_diagonal_degrees": 0.177,
        "brick_half_diagonal_radians_bound": 0.00309,
        "lipschitz_variance_error_bracket": float(ERROR_BRACKET),
        "conservative_object_variance_interval": {"lower": lower, "upper": upper},
        "threshold": float(THRESHOLD),
        "twice_error_bracket": float(TWICE_ERROR_BRACKET),
        "margin_above_threshold": variance - float(THRESHOLD),
        "binding_decision_rule": {
            "PASS": "V_center - 0.15 >= 0.0248",
            "FAIL": "V_center + 0.0124 < 0.15",
            "INCONCLUSIVE": "otherwise; report measured value and escalate",
        },
        "verdict": verdict,
        "static_product": static_metadata,
        "server_side_trigonometry": 0,
        "server_side_axis_terms": 0,
        "object_rows_exported": 0,
        "positions_exported_from_object_table": 0,
        "local_geometry_only": True,
    }
    atomic_json(RESULT_PATH, result)
    custody = {
        "manifest_sha256": sha256_path(MANIFEST_PATH),
        "counts_outcome_sha256": sha256_path(FINAL_COUNTS_OUTCOME),
        "static_product_sha256": sha256_path(STATIC_PRODUCT_PATH),
        "combined_counts_sha256": sha256_path(COMBINED_COUNTS_PATH),
        "local_geometry_result_sha256": sha256_path(RESULT_PATH),
        "reconstructor_sha256": sha256_path(Path(__file__)),
        "partition_result_sha256": {str(path): sha256_path(path) for path in result_paths},
        "population": EXPECTED_POPULATION,
        "nonempty_bricks": len(counts),
        "verdict": verdict,
    }
    atomic_json(CUSTODY_PATH, custody)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
