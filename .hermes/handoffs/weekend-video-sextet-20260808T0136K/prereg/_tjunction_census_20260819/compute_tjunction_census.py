#!/usr/bin/env python3
"""Offline DR10-South working-set T-junction census at brick-geometry level."""

from __future__ import annotations

import ast
import csv
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import numpy as np
from astropy.io import fits

HERE = Path(__file__).resolve().parent
PREREG = HERE.parent
CUSTODY = PREREG / "_tori_transfer_20260819/execution_package/SIDECAR_CUSTODY_20260819.md"
WORKING_SET = PREREG / "_tori_r1_workingset_evidence/workingset_bricks.csv"
ROUND5 = PREREG / "boundary_fixtures/make_boundary_fixtures_round5.py"
ROUND1 = PREREG / "boundary_fixtures/make_boundary_fixtures.py"
EXPECTED_GEOMETRY_SHA256 = "863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a"
EXPECTED_ROUND5_SHA256 = "498659bf1798c228aac8146fbfd53ea43c6723f319aae1d7ddec41f9d93ddf6c"
EXPECTED_WORKING_ROWS = 60_308
FLOAT_TOLERANCE_DEG = 1e-10
BOUNDARY_GRID_TOLERANCE = 1e-9
STRICT_INTERIOR_MARGIN_DEG = 1e-12


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def literal_assignment(path: Path, name: str) -> Any:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(isinstance(target, ast.Name) and target.id == name for target in targets):
                if node.value is None:
                    raise RuntimeError(f"literal assignment {name} has no value in {path}")
                return ast.literal_eval(node.value)
    raise RuntimeError(f"literal assignment {name} not found in {path}")


def custody_geometry_path() -> tuple[Path, str]:
    text = CUSTODY.read_text(encoding="utf-8")
    relative_match = re.search(r"- local object: `([^`]+survey-bricks-dr10-south\.fits\.gz)`", text)
    digest_match = re.search(r"- recomputed local SHA-256: `([0-9a-f]{64})`", text)
    if not relative_match or not digest_match:
        raise RuntimeError("could not parse sidecar path and digest from custody receipt")
    path = PREREG / relative_match.group(1)
    expected = digest_match.group(1)
    if expected != EXPECTED_GEOMETRY_SHA256:
        raise RuntimeError(f"custody digest changed: {expected}")
    observed = sha256(path)
    if observed != expected:
        raise RuntimeError(f"geometry SHA-256 mismatch: expected {expected}, observed {observed}")
    return path, observed


def load_fixture_band() -> tuple[dict[str, tuple[float, float]], float, float, float]:
    observed_round5 = sha256(ROUND5)
    if observed_round5 != EXPECTED_ROUND5_SHA256:
        raise RuntimeError(
            f"round-5 generator SHA-256 mismatch: expected {EXPECTED_ROUND5_SHA256}, "
            f"observed {observed_round5}"
        )
    requests = literal_assignment(ROUND5, "LADDER_REQUESTS_PIXELS")
    pixel_scale = float(literal_assignment(ROUND1, "PIXEL_SCALE_ARCSEC"))
    required = {
        "tjunction_exact": (0.0, 0.0),
        "vertical_inside": (-10.0, 0.0),
        "vertical_one_pixel_beyond": (1.0, 0.0),
        "vertical_subpixel_inside": (-0.25, 0.0),
        "vertical_subpixel_outside": (0.25, 0.0),
        "horizontal_inside": (0.0, -10.0),
        "horizontal_one_pixel_beyond": (0.0, 1.0),
        "horizontal_subpixel_inside": (0.0, -0.25),
        "horizontal_subpixel_outside": (0.0, 0.25),
    }
    if requests != required:
        raise RuntimeError(f"unexpected round-5 offset ladder: {requests!r}")
    # The tested band is the axis-aligned envelope of the requested east/north
    # object-centre offsets. It is [-10,+1] pixels on each axis.
    all_x = [value[0] for value in requests.values()]
    all_y = [value[1] for value in requests.values()]
    low_px = min(min(all_x), min(all_y))
    high_px = max(max(all_x), max(all_y))
    if (low_px, high_px) != (-10.0, 1.0):
        raise RuntimeError("round-5 tested band did not resolve to [-10,+1] pixels")
    return requests, pixel_scale, low_px, high_px


def main() -> int:
    geometry_path, geometry_hash = custody_geometry_path()
    requests, pixel_scale_arcsec, band_low_px, band_high_px = load_fixture_band()
    working_hash = sha256(WORKING_SET)

    with WORKING_SET.open(newline="", encoding="utf-8") as handle:
        working_rows = list(csv.DictReader(handle))
    required_working_columns = {"brickname", "brickid", "coverage_class_exact_indicator"}
    if not working_rows or not required_working_columns.issubset(working_rows[0]):
        raise RuntimeError("working-set CSV schema mismatch")
    if len(working_rows) != EXPECTED_WORKING_ROWS:
        raise RuntimeError(f"expected {EXPECTED_WORKING_ROWS} working rows, found {len(working_rows)}")
    working_names = {row["brickname"] for row in working_rows}
    working_ids = {int(row["brickid"]) for row in working_rows}
    if len(working_names) != EXPECTED_WORKING_ROWS or len(working_ids) != EXPECTED_WORKING_ROWS:
        raise RuntimeError("working-set brick names or IDs are not unique")

    with fits.open(geometry_path, memmap=False) as hdus:
        table = getattr(hdus[1], "data")
        names = np.char.strip(np.asarray(table["brickname"]).astype(str))
        brickids = np.asarray(table["brickid"], dtype=np.int64)
        dec = np.asarray(table["dec"], dtype=np.float64)
        ra1 = np.asarray(table["ra1"], dtype=np.float64)
        ra2 = np.asarray(table["ra2"], dtype=np.float64)
        dec1 = np.asarray(table["dec1"], dtype=np.float64)
        dec2 = np.asarray(table["dec2"], dtype=np.float64)
        area = np.asarray(table["area"], dtype=np.float64)

    name_to_index = {str(name): index for index, name in enumerate(names)}
    missing_names = sorted(working_names - set(name_to_index))
    if missing_names:
        raise RuntimeError(f"{len(missing_names)} working bricks absent from geometry sidecar")
    for row in working_rows:
        index = name_to_index[row["brickname"]]
        if int(brickids[index]) != int(row["brickid"]):
            raise RuntimeError(f"brick ID mismatch for {row['brickname']}")

    geometry_rows: list[tuple[float, np.ndarray, int]] = []
    for dec_value in np.unique(dec):
        indices = np.flatnonzero(dec == dec_value)
        indices = indices[np.argsort(ra1[indices])]
        width = float(np.median(ra2[indices] - ra1[indices]))
        full_row_ra_count = int(round(360.0 / width))
        geometry_rows.append((float(dec_value), indices, full_row_ra_count))

    count_by_brick: Counter[str] = Counter()
    band_area_by_brick: defaultdict[str, float] = defaultdict(float)
    event_rows: list[dict[str, Any]] = []
    skip_counts: Counter[str] = Counter()
    direction_counts: Counter[str] = Counter()
    round5_matched_junction_recovered = False
    band_low_arcsec = band_low_px * pixel_scale_arcsec
    band_high_arcsec = band_high_px * pixel_scale_arcsec

    for (lower_dec, lower_indices, lower_count), (
        upper_dec,
        upper_indices,
        upper_count,
    ) in zip(geometry_rows, geometry_rows[1:]):
        if abs(upper_dec - lower_dec - 0.25) > FLOAT_TOLERANCE_DEG:
            skip_counts["nonadjacent_declination_rows"] += 1
            continue
        interface_dec = 0.5 * (lower_dec + upper_dec)
        orientations = (
            ("lower-row-stem", lower_indices, upper_indices, upper_count),
            ("upper-row-stem", upper_indices, lower_indices, lower_count),
        )
        for orientation, stem, span, span_full_count in orientations:
            for k in range(len(stem) - 1):
                junction_ra = float(ra2[stem[k]])
                if abs(junction_ra - float(ra1[stem[k + 1]])) > FLOAT_TOLERANCE_DEG:
                    skip_counts["noncontiguous_available_stem_pair"] += 1
                    continue
                # Use the inferred complete-row count to detect coincident boundaries,
                # including boundaries whose neighbouring table rows are footprint-trimmed.
                other_grid_coordinate = junction_ra * span_full_count / 360.0
                if abs(other_grid_coordinate - round(other_grid_coordinate)) < BOUNDARY_GRID_TOLERANCE:
                    skip_counts["coincident_four_cell_boundary"] += 1
                    continue
                span_position = int(np.searchsorted(ra1[span], junction_ra, side="right") - 1)
                if span_position < 0 or span_position >= len(span):
                    skip_counts["spanning_brick_absent_from_sidecar"] += 1
                    continue
                span_index = int(span[span_position])
                if not (
                    float(ra1[span_index]) + STRICT_INTERIOR_MARGIN_DEG
                    < junction_ra
                    < float(ra2[span_index]) - STRICT_INTERIOR_MARGIN_DEG
                ):
                    skip_counts["spanning_brick_absent_from_sidecar"] += 1
                    continue

                incident_indices = (int(stem[k]), int(stem[k + 1]), span_index)
                incident_names = tuple(str(names[index]) for index in incident_indices)
                if (
                    abs(junction_ra - 175.40275049115917) < 1e-12
                    and abs(interface_dec - (-45.125)) < 1e-12
                    and set(incident_names) == {"1752m452", "1755m452", "1752m450"}
                ):
                    round5_matched_junction_recovered = True
                working_flags = tuple(name in working_names for name in incident_names)
                if not any(working_flags):
                    continue

                direction_counts[orientation] += 1
                event_id = len(event_rows) + 1
                contribution_total = 0.0
                contribution_by_name: dict[str, float] = {}
                tangent_ra_scale = math.cos(math.radians(interface_dec)) * 3600.0
                for index, name, is_working in zip(incident_indices, incident_names, working_flags):
                    if not is_working:
                        continue
                    count_by_brick[name] += 1
                    x1 = (float(ra1[index]) - junction_ra) * tangent_ra_scale
                    x2 = (float(ra2[index]) - junction_ra) * tangent_ra_scale
                    y1 = (float(dec1[index]) - interface_dec) * 3600.0
                    y2 = (float(dec2[index]) - interface_dec) * 3600.0
                    clipped_width = max(
                        0.0,
                        min(band_high_arcsec, x2) - max(band_low_arcsec, x1),
                    )
                    clipped_height = max(
                        0.0,
                        min(band_high_arcsec, y2) - max(band_low_arcsec, y1),
                    )
                    contribution = clipped_width * clipped_height / (3600.0**2)
                    if contribution <= 0.0:
                        raise RuntimeError(f"non-positive band contribution at event {event_id} for {name}")
                    band_area_by_brick[name] += contribution
                    contribution_by_name[name] = contribution
                    contribution_total += contribution

                event_rows.append(
                    {
                        "event_id": event_id,
                        "junction_ra_deg": junction_ra,
                        "junction_dec_deg": interface_dec,
                        "stem_orientation": orientation,
                        "incident_brick_1": incident_names[0],
                        "incident_brick_2": incident_names[1],
                        "incident_brick_3": incident_names[2],
                        "working_incident_count": sum(working_flags),
                        "working_incident_bricks": ";".join(
                            name for name, flag in zip(incident_names, working_flags) if flag
                        ),
                        "working_band_area_deg2": contribution_total,
                        "working_band_area_by_brick_json": json.dumps(
                            contribution_by_name, sort_keys=True, separators=(",", ":")
                        ),
                    }
                )

    # Round-5's exact real-geometry example must be represented by the same three rows.
    if not round5_matched_junction_recovered:
        raise RuntimeError("round-5 matched real T-junction was not recovered")

    denominator_area_deg2 = math.fsum(float(area[name_to_index[name]]) for name in working_names)
    band_area_deg2 = math.fsum(band_area_by_brick.values())
    area_fraction = band_area_deg2 / denominator_area_deg2
    total_junction_segments = sum(count_by_brick.values())
    bricks_with_junction = len(count_by_brick)
    unique_junction_events = len(event_rows)
    if bricks_with_junction != EXPECTED_WORKING_ROWS:
        raise RuntimeError(
            f"expected every working brick to have a junction; observed {bricks_with_junction}"
        )

    per_brick_path = HERE / "working_brick_tjunction_census.csv"
    with per_brick_path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = [
            "brickname",
            "brickid",
            "coverage_class_exact_indicator",
            "brick_area_deg2",
            "tjunction_boundary_segment_count",
            "tested_band_area_in_brick_deg2",
            "tested_band_fraction_of_brick_area",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in working_rows:
            name = row["brickname"]
            index = name_to_index[name]
            brick_area = float(area[index])
            brick_band_area = float(band_area_by_brick[name])
            writer.writerow(
                {
                    **row,
                    "brick_area_deg2": format(brick_area, ".17g"),
                    "tjunction_boundary_segment_count": count_by_brick[name],
                    "tested_band_area_in_brick_deg2": format(brick_band_area, ".17g"),
                    "tested_band_fraction_of_brick_area": format(brick_band_area / brick_area, ".17g"),
                }
            )

    event_path = HERE / "working_set_tjunction_events.csv"
    with event_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(event_rows[0]))
        writer.writeheader()
        for row in event_rows:
            writer.writerow(row)

    distribution = Counter(count_by_brick.values())
    summary = {
        "status": "GPT1_TJCENSUS_COMPLETE",
        "scope": "brick_geometry_only",
        "headline": {
            "total_junction_segments": total_junction_segments,
            "bricks_with_at_least_one_junction": bricks_with_junction,
            "fraction_of_working_brick_area_within_round5_tested_offset_band": area_fraction,
        },
        "definitions": {
            "junction_segment": (
                "one per-working-brick boundary incidence at a unique three-cell meet; "
                "the headline total is the sum of the per-brick counts"
            ),
            "unique_junction_events_with_any_working_brick": unique_junction_events,
            "tested_offset_band": (
                "axis-aligned east/north envelope of round-5 requested offsets, "
                "[-10,+1] pixels on each axis"
            ),
            "area_fraction": (
                "sum of each tested-band rectangle clipped to incident working-brick unique "
                "geometry, divided by sum of FITS AREA for all working bricks"
            ),
            "object_level_touching_counts": "NOT_DERIVABLE_POSITIONS_DELETED_BY_DESIGN",
        },
        "band": {
            "round5_requested_offsets_pixels": requests,
            "pixel_scale_arcsec": pixel_scale_arcsec,
            "low_pixels": band_low_px,
            "high_pixels": band_high_px,
            "low_arcsec": band_low_arcsec,
            "high_arcsec": band_high_arcsec,
            "width_arcsec": band_high_arcsec - band_low_arcsec,
            "working_band_area_deg2": band_area_deg2,
            "working_brick_area_denominator_deg2": denominator_area_deg2,
            "fraction": area_fraction,
        },
        "counts": {
            "working_rows": len(working_rows),
            "working_unique_bricknames": len(working_names),
            "working_unique_brickids": len(working_ids),
            "unique_junction_events_with_any_working_brick": unique_junction_events,
            "working_brick_junction_boundary_incidences": total_junction_segments,
            "bricks_with_at_least_one_junction": bricks_with_junction,
            "per_brick_segment_count_distribution": {
                str(key): value for key, value in sorted(distribution.items())
            },
            "selected_event_stem_orientation": dict(sorted(direction_counts.items())),
            "topology_skip_diagnostics": dict(sorted(skip_counts.items())),
        },
        "inputs": {
            "geometry_path_relative_to_prereg": geometry_path.relative_to(PREREG).as_posix(),
            "geometry_sha256": geometry_hash,
            "geometry_rows": len(names),
            "working_set_path_relative_to_prereg": WORKING_SET.relative_to(PREREG).as_posix(),
            "working_set_sha256": working_hash,
            "round5_generator_path_relative_to_prereg": ROUND5.relative_to(PREREG).as_posix(),
            "round5_generator_sha256": sha256(ROUND5),
            "round1_generator_sha256": sha256(ROUND1),
            "custody_receipt_sha256": sha256(CUSTODY),
        },
        "limits": {
            "network_used": False,
            "parent_object_positions_used": False,
            "object_count_interpretation_allowed": False,
            "ceiling": (
                "This brick-level census is the manifest-gate answer's ceiling, not an object count."
            ),
        },
    }
    summary_path = HERE / "tjunction_census_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    report = f"""GPT1_TJCENSUS_COMPLETE total_junction_segments={total_junction_segments} bricks_with_at_least_one_junction={bricks_with_junction} area_fraction={area_fraction:.17g}

# DR10 South working-set T-junction census — brick geometry only

## Headline

- Total T-junction boundary segments in the working set: **{total_junction_segments:,}**.
- Working-set bricks with at least one T-junction on their boundary: **{bricks_with_junction:,}** of {len(working_rows):,}.
- Fraction of summed working-brick `AREA` inside the round-5 tested offset band: **{area_fraction:.17g}** ({area_fraction * 1e6:.9f} ppm).

“Segment” is counted as one per-working-brick boundary incidence at a unique three-cell meet. The total above is therefore the sum of the per-brick `tjunction_boundary_segment_count` column. There are **{unique_junction_events:,} unique T-junction events** having at least one working-set brick among their three incident cells; this separate number is reported to prevent incidence/event ambiguity.

## Geometry and band definition

A T-junction is detected only where two available contiguous bricks in one declination row share an RA boundary, that boundary is not a boundary of the adjacent 0.25-degree row, and it lies strictly inside an available brick in that adjacent row. Thus exactly three sidecar cells meet. Coincident boundaries are excluded as four-cell crossings.

The band is taken directly from the SHA-pinned round-5 fixture ladder in `boundary_fixtures/make_boundary_fixtures_round5.py:176-186` and its contract at `boundary_fixtures/make_boundary_fixtures_round5.py:613-617`: requested east/north offsets include -10, -0.25, 0, +0.25, and +1 pixels. The area calculation uses their axis-aligned envelope, **[-10,+1] pixels on each axis**, at the fixture pixel scale **{pixel_scale_arcsec} arcsec/pixel** (`boundary_fixtures/make_boundary_fixtures.py:24`). Each local tangent-plane band rectangle is clipped to each incident working brick; clipped areas are summed and divided by the FITS `AREA` sum.

- Tested-band area in working bricks: `{band_area_deg2:.17g}` deg^2.
- Summed working-brick FITS `AREA`: `{denominator_area_deg2:.17g}` deg^2.
- Ratio: `{area_fraction:.17g}`.

## Custody and scope ceiling

The geometry sidecar was located through `_tori_transfer_20260819/execution_package/SIDECAR_CUSTODY_20260819.md:7-13` and rehashed before FITS open. Observed SHA-256: `{geometry_hash}`. It matches the custody record and the survey-published digest quoted there. The working-set CSV has {len(working_rows):,} rows, {len(working_names):,} unique brick names, {len(working_ids):,} unique brick IDs, and every name/ID pair matches the FITS geometry table.

**Object-level touching counts are NOT derivable: parent-object positions were deleted by design.** No attempt was made to re-derive or re-fetch them. This brick-level census is the manifest-gate answer's ceiling, not an object count. The round-5 gate itself left the real-parent touching question to the manifest stage (`KUN_ROUND5_TJUNCTION_GATE_20260817.md:194-204`); this result answers only the geometry-level portion now possible under the deletion rule.

No network operation, real image read, object-position read, object reconstruction, or object count was performed.

## Receipts

- `compute_tjunction_census.py` — executable census and validation logic.
- `working_brick_tjunction_census.csv` — one row per working-set brick.
- `working_set_tjunction_events.csv` — one row per unique selected three-cell meet.
- `tjunction_census_summary.json` — machine-readable definitions, counts, areas, input hashes, and limits.
- `OUTPUT_SHA256.json` — output inventory hashes.
"""
    report_path = HERE / "T_JUNCTION_CENSUS_REPORT.md"
    report_path.write_text(report, encoding="utf-8")

    output_paths = [Path(__file__), per_brick_path, event_path, summary_path, report_path]
    inventory = {
        path.name: {"sha256": sha256(path), "bytes": path.stat().st_size}
        for path in output_paths
    }
    inventory_path = HERE / "OUTPUT_SHA256.json"
    inventory_path.write_text(json.dumps(inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps(summary["headline"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
