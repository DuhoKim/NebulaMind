#!/usr/bin/env python3
"""Generate round-3 extreme-declination sub-pixel knife-edge fixtures.

The inclusion oracle is independent of the product adapter.  Object centres are
solved at fixed declination so that an exact output pixel edge reaches a
requested signed offset in a candidate source brick's own TAN pixel plane.
Positive offsets cross into the candidate; negative offsets remain outside.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np
from astropy.io import fits
from astropy.wcs import WCS

from make_boundary_fixtures import (
    BRICK_SIZE,
    CUTOUT_SIZE,
    FixtureSourceError,
    MissingNeighbourError,
    PIXEL_SCALE_ARCSEC,
    sha256_path,
)
from make_boundary_fixtures_round2 import (
    FOOTPRINT_DEC_MAX_DEG,
    FOOTPRINT_DEC_MIN_DEG,
    OUTPUT_EDGE_PIXELS,
    VALUE_TOLERANCE,
    _analytic_expected,
    _grid_pair,
    _pixel_world,
    _sample_source,
    _valid_source_centres,
    _write_source_brick,
    output_wcs_contract,
    plan_source_ids,
)

PINNED_ROUND1_SHA256 = "24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d"
PINNED_ROUND2_SHA256 = "60e3d662d72fbc87e0c82889b4f9174c033882b8f9a2019011c5104bb4aa15bc"
ROUND3_BRIEF_SHA256 = "4127deec7fb1b81f52040e31d733fa749ac2d5b9173732a8d75d6e01357b7fc8"

LADDER_OFFSETS_PIXELS = (
    ("inside", -10.0),
    ("exact_boundary", 0.0),
    ("one_pixel_beyond", 1.0),
    ("subpixel_just_inside", -0.25),
    ("subpixel_just_outside", 0.25),
)
OFFSET_SOLVE_TOLERANCE_PIXELS = 1e-8


def _wrapped_delta_deg(value_deg: float, reference_deg: float) -> float:
    return (float(value_deg) - float(reference_deg) + 180.0) % 360.0 - 180.0


def _candidate_boundary_from_primary(
    primary: dict[str, Any], candidate: dict[str, Any]
) -> dict[str, Any]:
    """Find the candidate image edge approached from the primary source."""
    primary_world = [[primary["wcs"]["CRVAL1"], primary["wcs"]["CRVAL2"]]]
    projected = np.asarray(
        WCS(candidate["wcs"]).all_world2pix(primary_world, 1), dtype=np.float64
    )[0]
    possible: list[tuple[float, int, float, float, str]] = []
    for axis, axis_name in ((0, "x"), (1, "y")):
        if projected[axis] < 0.5:
            possible.append((0.5 - projected[axis], axis, 0.5, 1.0, axis_name))
        if projected[axis] > BRICK_SIZE + 0.5:
            possible.append(
                (
                    projected[axis] - (BRICK_SIZE + 0.5),
                    axis,
                    BRICK_SIZE + 0.5,
                    -1.0,
                    axis_name,
                )
            )
    if not possible:
        raise RuntimeError(
            f"primary {primary['brick_id']} centre lies inside candidate {candidate['brick_id']}"
        )
    _, axis, boundary, inward_sign, axis_name = max(possible, key=lambda row: row[0])
    return {
        "boundary_axis_index": axis,
        "boundary_axis": axis_name,
        "boundary_source_pixel": float(boundary),
        "candidate_inward_sign": float(inward_sign),
        "primary_centre_in_candidate_pixels": projected.tolist(),
    }


def _output_polygon_edge_pixels() -> np.ndarray:
    return OUTPUT_EDGE_PIXELS.copy()


def _edge_offsets_in_candidate_pixels(
    output_wcs: dict[str, Any],
    candidate_wcs: dict[str, Any],
    boundary_spec: dict[str, Any],
) -> tuple[np.ndarray, np.ndarray]:
    output_edge = _output_polygon_edge_pixels()
    world = np.asarray(WCS(output_wcs).all_pix2world(output_edge, 1), dtype=np.float64)
    candidate_pixels = np.asarray(
        WCS(candidate_wcs).all_world2pix(world, 1), dtype=np.float64
    )
    axis = int(boundary_spec["boundary_axis_index"])
    boundary = float(boundary_spec["boundary_source_pixel"])
    inward_sign = float(boundary_spec["candidate_inward_sign"])
    offsets = inward_sign * (candidate_pixels[:, axis] - boundary)
    return candidate_pixels, offsets


def _solve_case_at_fixed_declination(
    group: list[dict[str, Any]],
    requested_offset_pixels: float,
    dec_deg: float,
) -> tuple[float, dict[str, Any]]:
    primary = next(row for row in group if row["side"] == "west")
    candidate = next(row for row in group if row["side"] == "east")
    boundary_spec = _candidate_boundary_from_primary(primary, candidate)
    target_ra = float(candidate["wcs"]["CRVAL1"])
    primary_ra = float(primary["wcs"]["CRVAL1"])
    path_delta_ra = _wrapped_delta_deg(primary_ra, target_ra)

    def evaluate(path_fraction: float) -> tuple[float, float, np.ndarray, np.ndarray]:
        ra_deg = (target_ra + path_fraction * path_delta_ra) % 360.0
        output_wcs = output_wcs_contract(ra_deg, dec_deg)
        candidate_pixels, offsets = _edge_offsets_in_candidate_pixels(
            output_wcs, candidate["wcs"], boundary_spec
        )
        return float(np.max(offsets)), ra_deg, candidate_pixels, offsets

    inside_value, _, _, _ = evaluate(0.0)
    outside_value, _, _, _ = evaluate(1.0)
    if not (inside_value > requested_offset_pixels and outside_value < requested_offset_pixels):
        raise RuntimeError(
            "pixel-space knife-edge solve is not bracketed: "
            f"inside={inside_value}, outside={outside_value}, requested={requested_offset_pixels}"
        )

    lower = 0.0
    upper = 1.0
    for _ in range(100):
        middle = (lower + upper) / 2.0
        achieved, _, _, _ = evaluate(middle)
        if achieved > requested_offset_pixels:
            lower = middle
        else:
            upper = middle
    path_fraction = (lower + upper) / 2.0
    achieved, ra_deg, candidate_pixels, offsets = evaluate(path_fraction)
    if abs(achieved - requested_offset_pixels) > OFFSET_SOLVE_TOLERANCE_PIXELS:
        raise RuntimeError(
            f"pixel-space knife-edge solve missed target: requested {requested_offset_pixels}, "
            f"achieved {achieved}"
        )

    evidence = {
        **boundary_spec,
        "placement_method": (
            "bisection at fixed object declination along the primary-to-candidate RA arc; "
            "objective evaluated in the candidate source TAN pixel plane"
        ),
        "requested_edge_offset_pixels": float(requested_offset_pixels),
        "achieved_edge_offset_pixels": achieved,
        "achieved_subpixel_fraction": abs(achieved - round(achieved)),
        "solve_absolute_error_pixels": abs(achieved - requested_offset_pixels),
        "solve_tolerance_pixels": OFFSET_SOLVE_TOLERANCE_PIXELS,
        "path_fraction_candidate_to_primary": path_fraction,
        "output_edge_pixels": _output_polygon_edge_pixels().tolist(),
        "sampled_edge_candidate_source_pixels": candidate_pixels.tolist(),
        "sampled_edge_inward_offsets_pixels": offsets.tolist(),
        "positive_offset_meaning": "output polygon crosses into knife_edge_source_brick",
    }
    return ra_deg, evidence


def build_geometry_and_cases() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    specifications = (
        ("dec_max", "knife-dec-max", FOOTPRINT_DEC_MAX_DEG - 0.125, 200.0, 10.0),
        ("dec_min", "knife-dec-min", FOOTPRINT_DEC_MIN_DEG + 0.125, 120.0, 20.0),
    )
    geometry_rows: list[dict[str, Any]] = []
    cases: list[dict[str, Any]] = []
    for prefix, group_id, dec_deg, target_ra, value_offset in specifications:
        group, _ = _grid_pair(
            group_id,
            dec_deg,
            boundary_target_ra_deg=target_ra,
            seam=False,
            value_offset_start=value_offset,
        )
        geometry_rows.extend(group)
        primary = next(row for row in group if row["side"] == "west")
        candidate = next(row for row in group if row["side"] == "east")
        for suffix, requested_offset in LADDER_OFFSETS_PIXELS:
            ra_deg, evidence = _solve_case_at_fixed_declination(
                group, requested_offset, dec_deg
            )
            output_wcs = output_wcs_contract(ra_deg, dec_deg)
            expected_bricks = plan_source_ids(group, output_wcs)
            cases.append(
                {
                    "object_id": f"{prefix}_{suffix}",
                    "group_id": group_id,
                    "ra_deg": float(ra_deg) % 360.0,
                    "dec_deg": float(dec_deg),
                    "candidate_bricks": sorted(row["brick_id"] for row in group),
                    "expected_bricks": expected_bricks,
                    "primary_brick": primary["brick_id"],
                    "knife_edge_source_brick": candidate["brick_id"],
                    "source_set_signature_sha256": hashlib.sha256(
                        json.dumps(expected_bricks, separators=(",", ":")).encode("utf-8")
                    ).hexdigest(),
                    "output_wcs": output_wcs,
                    "geometry_evidence": evidence,
                }
            )
    return geometry_rows, cases


def _classify_pixel_contributors(
    object_row: dict[str, Any], brick_records: dict[str, dict[str, Any]]
) -> tuple[list[str], list[str]]:
    world = _pixel_world(object_row["output_wcs"])
    contributing: list[str] = []
    zero_touch: list[str] = []
    for brick_id in object_row["expected_bricks"]:
        _, valid = _valid_source_centres(brick_records[brick_id]["wcs"], world)
        if np.any(valid):
            contributing.append(brick_id)
        else:
            zero_touch.append(brick_id)
    return sorted(contributing), sorted(zero_touch)


def generate_round3_fixture_tree(root: Path) -> dict[str, Any]:
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    (root / "bricks").mkdir(exist_ok=False)
    (root / "expected").mkdir(exist_ok=False)

    fixture_root = Path(__file__).resolve().parent
    observed_round1 = sha256_path(fixture_root / "make_boundary_fixtures.py")
    observed_round2 = sha256_path(fixture_root / "make_boundary_fixtures_round2.py")
    if observed_round1 != PINNED_ROUND1_SHA256 or observed_round2 != PINNED_ROUND2_SHA256:
        raise RuntimeError(
            "round-1/round-2 generator custody mismatch; round 3 refuses to generate"
        )

    geometry_rows, objects = build_geometry_and_cases()
    for row in geometry_rows:
        _write_source_brick(root, row)
    brick_records = {row["brick_id"]: row for row in geometry_rows}

    for object_row in objects:
        contributing, zero_touch = _classify_pixel_contributors(object_row, brick_records)
        object_row["expected_contributing_bricks"] = contributing
        object_row["expected_zero_pixel_touch_bricks"] = zero_touch
        expected, coverage = _analytic_expected(object_row, brick_records)
        expected_path = root / "expected" / f"{object_row['object_id']}.npy"
        np.save(expected_path, expected, allow_pickle=False)
        object_row["expected_array_path"] = expected_path.relative_to(root).as_posix()
        object_row["expected_array_sha256"] = sha256_path(expected_path)
        object_row["expected_coverage_sha256"] = hashlib.sha256(
            coverage.tobytes(order="C")
        ).hexdigest()
        bits = expected.view(np.uint32)
        object_row["value_probes"] = [
            {"y": y, "x": x, "float32_bits": int(bits[y, x])}
            for y, x in ((0, 0), (0, 127), (64, 64), (127, 0), (127, 127))
        ]

    sidecar = {
        "schema_version": "yui-synthetic-geometry-sidecar-v1",
        "synthetic_only": True,
        "selected_footprint_declination_domain_deg": [
            FOOTPRINT_DEC_MIN_DEG,
            FOOTPRINT_DEC_MAX_DEG,
        ],
        "selected_footprint_extreme_fixture_centres_deg": [
            FOOTPRINT_DEC_MIN_DEG + 0.125,
            FOOTPRINT_DEC_MAX_DEG - 0.125,
        ],
        "knife_edge_placement_contract": (
            "solve the extremal sampled output polygon edge in each candidate source TAN pixel "
            "plane while holding object declination fixed"
        ),
        "bricks": geometry_rows,
    }
    geometry_sidecar_path = root / "geometry_sidecar.json"
    geometry_sidecar_path.write_text(
        json.dumps(sidecar, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    objects_path = root / "objects.json"
    objects_path.write_text(
        json.dumps(objects, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    manifest = {
        "schema_version": "yui-boundary-fixtures-round3-v1",
        "object_schema_compatible_with": "yui-boundary-fixtures-round2-v1",
        "synthetic_only": True,
        "brief_sha256": ROUND3_BRIEF_SHA256,
        "parent_generator_sha256": {
            "round1": observed_round1,
            "round2": observed_round2,
        },
        "brick_size": [BRICK_SIZE, BRICK_SIZE],
        "cutout_size": [CUTOUT_SIZE, CUTOUT_SIZE],
        "pixel_scale_arcsec": PIXEL_SCALE_ARCSEC,
        "geometry_sidecar_path": "geometry_sidecar.json",
        "geometry_sidecar_sha256": sha256_path(geometry_sidecar_path),
        "objects_path": "objects.json",
        "objects_sha256": sha256_path(objects_path),
        "brick_count": len(geometry_rows),
        "object_count": len(objects),
        "requested_ladder_offsets_pixels": {
            suffix: offset for suffix, offset in LADDER_OFFSETS_PIXELS
        },
        "achieved_edge_offsets_pixels": {
            row["object_id"]: row["geometry_evidence"]["achieved_edge_offset_pixels"]
            for row in objects
        },
        "achieved_subpixel_fractions": {
            row["object_id"]: row["geometry_evidence"]["achieved_subpixel_fraction"]
            for row in objects
        },
        "planning_contract": (
            "positive-area intersection after projecting the exact output nine-point pixel-edge "
            "polygon into each distinct source TAN WCS"
        ),
        "knife_edge_contract": (
            "signed edge offsets are solved and reported in candidate source pixels; positive is "
            "inside the candidate, negative is outside"
        ),
        "pattern_contract": (
            "float32 smooth spherical sky function plus a declared per-brick value_offset; "
            "expected pixels average every valid planned contributor"
        ),
    }
    (root / "fixture_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return manifest


def _load_round3(root: Path) -> dict[str, dict[str, Any]]:
    sidecar = json.loads((root / "geometry_sidecar.json").read_text(encoding="utf-8"))
    return {row["brick_id"]: row for row in sidecar["bricks"]}


def _verify_sources(
    root: Path,
    object_row: dict[str, Any],
    brick_records: dict[str, dict[str, Any]],
) -> None:
    missing = [
        brick_id
        for brick_id in object_row["expected_bricks"]
        if brick_id not in brick_records
        or not (root / brick_records[brick_id]["relative_path"]).is_file()
    ]
    if missing:
        raise MissingNeighbourError(
            f"missing required neighbour brick(s): {', '.join(missing)}"
        )
    for brick_id in object_row["expected_bricks"]:
        record = brick_records[brick_id]
        observed = sha256_path(root / record["relative_path"])
        if observed != record["file_sha256"]:
            raise FixtureSourceError(
                f"{brick_id} digest mismatch: expected {record['file_sha256']}, observed {observed}"
            )


def render_round3_oracle(
    root: Path,
    object_row: dict[str, Any],
    *,
    source_order: list[str] | None = None,
    output_path: Path | None = None,
) -> tuple[np.ndarray, dict[str, Any]]:
    root = Path(root)
    brick_records = _load_round3(root)
    _verify_sources(root, object_row, brick_records)
    expected_ids = sorted(object_row["expected_bricks"])
    order = list(source_order) if source_order is not None else expected_ids
    if len(order) != len(set(order)) or set(order) != set(expected_ids):
        raise ValueError("source_order must contain every expected brick exactly once")

    expected, expected_coverage = _analytic_expected(object_row, brick_records)
    world = _pixel_world(object_row["output_wcs"])
    sampled_sum = np.zeros(CUTOUT_SIZE * CUTOUT_SIZE, dtype=np.float64)
    coverage = np.zeros(CUTOUT_SIZE * CUTOUT_SIZE, dtype=np.uint8)
    contributing: set[str] = set()
    for brick_id in order:
        record = brick_records[brick_id]
        with fits.open(root / record["relative_path"], memmap=False) as hdus:
            data = np.asarray(hdus[1].data)
            header = hdus[1].header
        if data.shape != (BRICK_SIZE, BRICK_SIZE) or data.dtype != np.dtype("float32"):
            raise RuntimeError(f"invalid synthetic brick {brick_id}")
        if (
            float(header["CRVAL1"]) != record["wcs"]["CRVAL1"]
            or float(header["CRVAL2"]) != record["wcs"]["CRVAL2"]
        ):
            raise RuntimeError(f"synthetic tangent-point mismatch for {brick_id}")
        sampled, valid = _sample_source(data, record["wcs"], world)
        if np.any(valid):
            sampled_sum[valid] += sampled[valid]
            coverage[valid] += 1
            contributing.add(brick_id)

    zero_coverage = int(np.count_nonzero(coverage == 0))
    if zero_coverage:
        raise RuntimeError(f"round-3 fixture oracle found {zero_coverage} uncovered output pixels")
    if not np.array_equal(coverage, expected_coverage.ravel()):
        raise RuntimeError("round-3 analytic and sampled coverage planes disagree")
    sampled_output = (sampled_sum / coverage).astype(np.float32).reshape(
        CUTOUT_SIZE, CUTOUT_SIZE
    )
    max_abs_error = float(
        np.max(np.abs(sampled_output.astype(np.float64) - expected.astype(np.float64)))
    )
    if max_abs_error > VALUE_TOLERANCE:
        raise RuntimeError(
            f"round-3 bilinear replay exceeded {VALUE_TOLERANCE}: {max_abs_error}"
        )

    receipt = {
        "object_id": object_row["object_id"],
        "planned_bricks": expected_ids,
        "opened_bricks": sorted(order),
        "contributing_bricks": sorted(contributing),
        "zero_pixel_touch_bricks": sorted(set(expected_ids) - contributing),
        "coverage_min": int(coverage.min()),
        "coverage_max": int(coverage.max()),
        "zero_coverage_pixels": zero_coverage,
        "bilinear_sample_max_abs_error": max_abs_error,
        "adapter_comparison_absolute_tolerance": VALUE_TOLERANCE,
        "coverage_array_sha256": hashlib.sha256(
            coverage.reshape(CUTOUT_SIZE, CUTOUT_SIZE).tobytes(order="C")
        ).hexdigest(),
        "output_array_sha256": hashlib.sha256(expected.tobytes(order="C")).hexdigest(),
    }
    if output_path is not None:
        output_path = Path(output_path)
        temporary_path = output_path.with_name(output_path.name + ".tmp")
        with temporary_path.open("wb") as handle:
            np.save(handle, expected, allow_pickle=False)
        temporary_path.replace(output_path)
    return expected, receipt


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main() -> int:
    arguments = build_argument_parser().parse_args()
    manifest = generate_round3_fixture_tree(arguments.output)
    print(
        json.dumps(
            {
                "status": "PASS_GENERATED_SYNTHETIC_BOUNDARY_FIXTURES_ROUND3",
                "bricks": manifest["brick_count"],
                "objects": manifest["object_count"],
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
