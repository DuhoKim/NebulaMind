#!/usr/bin/env python3
"""Independent output/topology reduction for the brick-level T-junction census."""

from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from astropy.io import fits

HERE = Path(__file__).resolve().parent
PREREG = HERE.parent
EXPECTED_GEOMETRY_SHA256 = "863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a"
EXPECTED_HEADLINE = (359_607, 60_308, 2.0614381359289613e-05)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def close(left: float, right: float, tolerance: float = 1e-15) -> bool:
    return math.isclose(left, right, rel_tol=tolerance, abs_tol=tolerance)


def main() -> int:
    summary_path = HERE / "tjunction_census_summary.json"
    brick_path = HERE / "working_brick_tjunction_census.csv"
    event_path = HERE / "working_set_tjunction_events.csv"
    report_path = HERE / "T_JUNCTION_CENSUS_REPORT.md"
    inventory_path = HERE / "OUTPUT_SHA256.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))

    for filename, record in inventory.items():
        path = HERE / filename
        if sha256(path) != record["sha256"] or path.stat().st_size != record["bytes"]:
            raise RuntimeError(f"inventory mismatch for {filename}")

    geometry_path = PREREG / summary["inputs"]["geometry_path_relative_to_prereg"]
    if sha256(geometry_path) != EXPECTED_GEOMETRY_SHA256:
        raise RuntimeError("independent geometry SHA-256 mismatch")
    with fits.open(geometry_path, memmap=False) as hdus:
        table = getattr(hdus[1], "data")
        names = np.char.strip(np.asarray(table["brickname"]).astype(str))
        ra1 = np.asarray(table["ra1"], dtype=np.float64)
        ra2 = np.asarray(table["ra2"], dtype=np.float64)
        dec1 = np.asarray(table["dec1"], dtype=np.float64)
        dec2 = np.asarray(table["dec2"], dtype=np.float64)
    geometry = {
        str(name): (float(ra1[index]), float(ra2[index]), float(dec1[index]), float(dec2[index]))
        for index, name in enumerate(names)
    }

    with brick_path.open(newline="", encoding="utf-8") as handle:
        bricks = list(csv.DictReader(handle))
    if len(bricks) != EXPECTED_HEADLINE[1]:
        raise RuntimeError("per-brick output row count mismatch")
    segment_sum = sum(int(row["tjunction_boundary_segment_count"]) for row in bricks)
    positive_bricks = sum(int(row["tjunction_boundary_segment_count"]) > 0 for row in bricks)
    brick_area_sum = math.fsum(float(row["brick_area_deg2"]) for row in bricks)
    band_area_sum = math.fsum(float(row["tested_band_area_in_brick_deg2"]) for row in bricks)
    fraction = band_area_sum / brick_area_sum

    with event_path.open(newline="", encoding="utf-8") as handle:
        events = list(csv.DictReader(handle))
    if len(events) != 132_108:
        raise RuntimeError("unique event row count mismatch")
    event_incidence_sum = sum(int(row["working_incident_count"]) for row in events)
    event_band_sum = math.fsum(float(row["working_band_area_deg2"]) for row in events)
    seen_keys: set[tuple[str, str, str]] = set()
    for row in events:
        junction_ra = float(row["junction_ra_deg"])
        junction_dec = float(row["junction_dec_deg"])
        orientation = row["stem_orientation"]
        first = row["incident_brick_1"]
        second = row["incident_brick_2"]
        third = row["incident_brick_3"]
        key = (format(junction_ra, ".15g"), format(junction_dec, ".15g"), orientation)
        if key in seen_keys:
            raise RuntimeError(f"duplicate event key {key}")
        seen_keys.add(key)
        first_bounds = geometry[first]
        second_bounds = geometry[second]
        third_bounds = geometry[third]
        if not (
            abs(first_bounds[1] - junction_ra) < 1e-10
            and abs(second_bounds[0] - junction_ra) < 1e-10
            and third_bounds[0] < junction_ra < third_bounds[1]
        ):
            raise RuntimeError(f"RA topology mismatch for event {row['event_id']}")
        if orientation == "lower-row-stem":
            valid_dec = (
                abs(first_bounds[3] - junction_dec) < 1e-10
                and abs(second_bounds[3] - junction_dec) < 1e-10
                and abs(third_bounds[2] - junction_dec) < 1e-10
            )
        elif orientation == "upper-row-stem":
            valid_dec = (
                abs(first_bounds[2] - junction_dec) < 1e-10
                and abs(second_bounds[2] - junction_dec) < 1e-10
                and abs(third_bounds[3] - junction_dec) < 1e-10
            )
        else:
            raise RuntimeError(f"unknown orientation {orientation}")
        if not valid_dec:
            raise RuntimeError(f"declination topology mismatch for event {row['event_id']}")

    headline = summary["headline"]
    checks = {
        "geometry_sha256_verified": True,
        "inventory_verified": True,
        "brick_rows": len(bricks),
        "unique_event_rows": len(events),
        "all_event_topologies_verified": len(seen_keys),
        "per_brick_segment_sum": segment_sum,
        "event_working_incidence_sum": event_incidence_sum,
        "positive_bricks": positive_bricks,
        "per_brick_area_sum_deg2": brick_area_sum,
        "per_brick_band_area_sum_deg2": band_area_sum,
        "event_band_area_sum_deg2": event_band_sum,
        "reduced_area_fraction": fraction,
        "status": "PASS",
    }
    if segment_sum != EXPECTED_HEADLINE[0] or event_incidence_sum != segment_sum:
        raise RuntimeError("junction segment reduction mismatch")
    if positive_bricks != EXPECTED_HEADLINE[1]:
        raise RuntimeError("positive-brick reduction mismatch")
    if not close(fraction, EXPECTED_HEADLINE[2]) or not close(event_band_sum, band_area_sum, 1e-12):
        raise RuntimeError("band-area reduction mismatch")
    if (
        headline["total_junction_segments"] != segment_sum
        or headline["bricks_with_at_least_one_junction"] != positive_bricks
        or not close(
            headline["fraction_of_working_brick_area_within_round5_tested_offset_band"],
            fraction,
        )
    ):
        raise RuntimeError("summary headline mismatch")
    first_line = report_path.read_text(encoding="utf-8").splitlines()[0]
    if not first_line.startswith("GPT1_TJCENSUS_COMPLETE "):
        raise RuntimeError("report completion marker missing")

    verification_path = HERE / "INDEPENDENT_VERIFICATION.json"
    verification_path.write_text(json.dumps(checks, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(checks, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
