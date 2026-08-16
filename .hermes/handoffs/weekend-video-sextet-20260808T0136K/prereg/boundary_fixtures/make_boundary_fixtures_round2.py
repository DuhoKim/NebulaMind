#!/usr/bin/env python3
"""Generate round-2 synthetic WCS-geometry boundary fixtures.

This module is an offline oracle built from the written route contract.  It does
not import or inspect the production adapter.  Every synthetic brick has its own
TAN tangent point, source selection is derived from nine-point WCS polygons,
and per-brick value fingerprints make omitted overlap contributors observable
without relying on output shape.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable

import numpy as np
from astropy.io import fits
from astropy.wcs import WCS

from make_boundary_fixtures import (
    BRICK_SIZE,
    CD_DEG_PER_PIXEL,
    CUTOUT_SIZE,
    FixtureSourceError,
    MissingNeighbourError,
    PIXEL_SCALE_ARCSEC,
    sha256_path,
)

FOOTPRINT_DEC_MIN_DEG = -90.0
FOOTPRINT_DEC_MAX_DEG = 32.375
UNIQUE_BRICK_HEIGHT_DEG = 0.25
VALUE_TOLERANCE = 1e-5

OUTPUT_EDGE_PIXELS = np.array(
    [
        [0.5, 0.5],
        [64.5, 0.5],
        [128.5, 0.5],
        [128.5, 64.5],
        [128.5, 128.5],
        [64.5, 128.5],
        [0.5, 128.5],
        [0.5, 64.5],
        [0.5, 0.5],
    ],
    dtype=np.float64,
)
SOURCE_EDGE_PIXELS = np.array(
    [
        [0.5, 0.5],
        [1800.5, 0.5],
        [3600.5, 0.5],
        [3600.5, 1800.5],
        [3600.5, 3600.5],
        [1800.5, 3600.5],
        [0.5, 3600.5],
        [0.5, 1800.5],
        [0.5, 0.5],
    ],
    dtype=np.float64,
)


def output_wcs_contract(ra_deg: float, dec_deg: float) -> dict[str, Any]:
    return {
        "NAXIS1": CUTOUT_SIZE,
        "NAXIS2": CUTOUT_SIZE,
        "CTYPE1": "RA---TAN",
        "CTYPE2": "DEC--TAN",
        "CRVAL1": float(ra_deg) % 360.0,
        "CRVAL2": float(dec_deg),
        "CRPIX1": 64.5,
        "CRPIX2": 64.5,
        "CD1_1": -CD_DEG_PER_PIXEL,
        "CD1_2": 0.0,
        "CD2_1": 0.0,
        "CD2_2": CD_DEG_PER_PIXEL,
    }


def source_wcs_contract(ra_deg: float, dec_deg: float) -> dict[str, Any]:
    return {
        "CTYPE1": "RA---TAN",
        "CTYPE2": "DEC--TAN",
        "CRVAL1": float(ra_deg) % 360.0,
        "CRVAL2": float(dec_deg),
        "CRPIX1": 1800.5,
        "CRPIX2": 1800.5,
        "CD1_1": -CD_DEG_PER_PIXEL,
        "CD1_2": 0.0,
        "CD2_1": 0.0,
        "CD2_2": CD_DEG_PER_PIXEL,
    }


def _clip_polygon_axis(
    polygon: np.ndarray,
    *,
    axis: int,
    bound: float,
    keep_greater: bool,
) -> np.ndarray:
    if len(polygon) == 0:
        return polygon
    output: list[np.ndarray] = []

    def inside(point: np.ndarray) -> bool:
        return bool(point[axis] >= bound) if keep_greater else bool(point[axis] <= bound)

    previous = polygon[-1]
    previous_inside = inside(previous)
    for current in polygon:
        current_inside = inside(current)
        if current_inside != previous_inside:
            denominator = current[axis] - previous[axis]
            if denominator != 0.0:
                fraction = (bound - previous[axis]) / denominator
                intersection = previous + fraction * (current - previous)
                intersection[axis] = bound
                output.append(intersection)
        if current_inside:
            output.append(current)
        previous = current
        previous_inside = current_inside
    if not output:
        return np.empty((0, 2), dtype=np.float64)
    return np.asarray(output, dtype=np.float64)


def _clipped_polygon_area_in_source_pixels(
    output_wcs: dict[str, Any], source_wcs: dict[str, Any]
) -> float:
    world = WCS(output_wcs).all_pix2world(OUTPUT_EDGE_PIXELS, 1)
    projected = np.asarray(WCS(source_wcs).all_world2pix(world, 1), dtype=np.float64)[:-1]
    if not np.all(np.isfinite(projected)):
        return 0.0
    clipped = projected
    for axis, bound, keep_greater in (
        (0, 0.5, True),
        (0, BRICK_SIZE + 0.5, False),
        (1, 0.5, True),
        (1, BRICK_SIZE + 0.5, False),
    ):
        clipped = _clip_polygon_axis(
            clipped,
            axis=axis,
            bound=bound,
            keep_greater=keep_greater,
        )
        if len(clipped) < 3:
            return 0.0
    x = clipped[:, 0]
    y = clipped[:, 1]
    return float(abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1))) / 2.0)


def plan_source_ids(
    geometry_rows: Iterable[dict[str, Any]], output_wcs: dict[str, Any]
) -> list[str]:
    planned = [
        row["brick_id"]
        for row in geometry_rows
        if _clipped_polygon_area_in_source_pixels(output_wcs, row["wcs"]) > 1e-8
    ]
    return sorted(planned)


def _wrapped_delta_deg(value: np.ndarray | float, reference: float) -> np.ndarray:
    return (np.asarray(value, dtype=np.float64) - reference + 180.0) % 360.0 - 180.0


def _great_circle_separation_deg(
    ra1_deg: float, dec1_deg: float, ra2_deg: float, dec2_deg: float
) -> float:
    ra1, dec1, ra2, dec2 = map(math.radians, (ra1_deg, dec1_deg, ra2_deg, dec2_deg))
    cosine = (
        math.sin(dec1) * math.sin(dec2)
        + math.cos(dec1) * math.cos(dec2) * math.cos(ra1 - ra2)
    )
    return math.degrees(math.acos(max(-1.0, min(1.0, cosine))))


def _grid_pair(
    group_id: str,
    dec_center_deg: float,
    *,
    boundary_target_ra_deg: float,
    seam: bool = False,
    value_offset_start: float,
) -> tuple[list[dict[str, Any]], float]:
    n_ra = max(1, int(round(360.0 * math.cos(math.radians(dec_center_deg)) / UNIQUE_BRICK_HEIGHT_DEG)))
    ra_step = 360.0 / n_ra
    if seam:
        west_index = n_ra - 1
        east_index = 0
        boundary_ra = 0.0
    else:
        boundary_index = int(round(boundary_target_ra_deg / ra_step)) % n_ra
        west_index = (boundary_index - 1) % n_ra
        east_index = boundary_index
        boundary_ra = (boundary_index * ra_step) % 360.0

    rows: list[dict[str, Any]] = []
    for ordinal, (side, index) in enumerate((("west", west_index), ("east", east_index))):
        center_ra = ((index + 0.5) * ra_step) % 360.0
        unique_ra_min = index * ra_step
        unique_ra_max = (index + 1) * ra_step
        wcs = source_wcs_contract(center_ra, dec_center_deg)
        edge_world = np.asarray(WCS(wcs).all_pix2world(SOURCE_EDGE_PIXELS, 1), dtype=np.float64)
        edge_world[:, 0] %= 360.0
        rows.append(
            {
                "brick_id": f"{group_id}-{side}",
                "group_id": group_id,
                "side": side,
                "synthetic_grid_ra_index": index,
                "synthetic_grid_ra_count": n_ra,
                "synthetic_grid_ra_step_deg": ra_step,
                "unique_ra_bounds_deg": [unique_ra_min, unique_ra_max],
                "unique_dec_bounds_deg": [
                    max(FOOTPRINT_DEC_MIN_DEG, dec_center_deg - UNIQUE_BRICK_HEIGHT_DEG / 2.0),
                    min(FOOTPRINT_DEC_MAX_DEG, dec_center_deg + UNIQUE_BRICK_HEIGHT_DEG / 2.0),
                ],
                "wcs": wcs,
                "pixel_edge_sky_polygon_deg": edge_world.tolist(),
                "value_offset": value_offset_start + ordinal * 0.25,
            }
        )
    return rows, boundary_ra


def _output_crosses_ra_boundary(output_wcs: dict[str, Any], boundary_ra_deg: float) -> bool:
    world = np.asarray(WCS(output_wcs).all_pix2world(OUTPUT_EDGE_PIXELS, 1), dtype=np.float64)
    deltas = _wrapped_delta_deg(world[:, 0], boundary_ra_deg)
    return bool(np.min(deltas) < -1e-10 and np.max(deltas) > 1e-10)


def _derive_overlap_only_case(
    group: list[dict[str, Any]], boundary_ra_deg: float, dec_deg: float
) -> tuple[float, int, dict[str, Any]]:
    candidates: list[tuple[int, float, list[str]]] = []
    cos_dec = math.cos(math.radians(dec_deg))
    for offset_pixels in range(CUTOUT_SIZE // 2 + 1, 301):
        ra_deg = (boundary_ra_deg - offset_pixels * CD_DEG_PER_PIXEL / cos_dec) % 360.0
        output_wcs = output_wcs_contract(ra_deg, dec_deg)
        planned = plan_source_ids(group, output_wcs)
        if (
            len(planned) == 2
            and not _output_crosses_ra_boundary(output_wcs, boundary_ra_deg)
        ):
            candidates.append((offset_pixels, ra_deg, planned))
    if not candidates:
        raise RuntimeError("synthetic geometry produced no overlap-only polygon case")
    offset_pixels, ra_deg, planned = candidates[len(candidates) // 2]
    evidence = {
        "output_crosses_unique_boundary": False,
        "output_intersects_neighbour_source_polygon": True,
        "derived_inward_offset_pixels": offset_pixels,
        "candidate_offset_range_pixels": [candidates[0][0], candidates[-1][0]],
        "planned_by_positive_area_nine_point_wcs_polygon": planned,
    }
    return ra_deg, offset_pixels, evidence


def build_geometry_and_cases() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = {}
    boundaries: dict[str, float] = {}
    specifications = (
        ("ra-wrap", -10.0, 0.0, True, 0.0),
        ("dec-max", FOOTPRINT_DEC_MAX_DEG - 0.125, 200.0, False, 1.0),
        ("dec-min", FOOTPRINT_DEC_MIN_DEG + 0.125, 120.0, False, 2.0),
        ("geometry-overlap", -30.0, 180.0, False, 3.0),
    )
    for group_id, dec_deg, target_ra, seam, value_offset in specifications:
        group, boundary = _grid_pair(
            group_id,
            dec_deg,
            boundary_target_ra_deg=target_ra,
            seam=seam,
            value_offset_start=value_offset,
        )
        groups[group_id] = group
        boundaries[group_id] = boundary

    overlap_ra, _, overlap_evidence = _derive_overlap_only_case(
        groups["geometry-overlap"], boundaries["geometry-overlap"], -30.0
    )
    case_specs: list[tuple[str, str, float, float, dict[str, Any]]] = [
        (
            "ra_wrap_crossing",
            "ra-wrap",
            0.0,
            -10.0,
            {
                "plain_numeric_tangent_point_delta_deg": abs(
                    groups["ra-wrap"][0]["wcs"]["CRVAL1"]
                    - groups["ra-wrap"][1]["wcs"]["CRVAL1"]
                ),
                "great_circle_tangent_point_separation_deg": _great_circle_separation_deg(
                    groups["ra-wrap"][0]["wcs"]["CRVAL1"],
                    -10.0,
                    groups["ra-wrap"][1]["wcs"]["CRVAL1"],
                    -10.0,
                ),
            },
        ),
        (
            "selected_dec_max_crossing",
            "dec-max",
            boundaries["dec-max"],
            FOOTPRINT_DEC_MAX_DEG - 0.125,
            {"selected_footprint_extreme": "maximum"},
        ),
        (
            "selected_dec_min_crossing",
            "dec-min",
            boundaries["dec-min"],
            FOOTPRINT_DEC_MIN_DEG + 0.125,
            {"selected_footprint_extreme": "minimum"},
        ),
        (
            "geometry_overlap_only",
            "geometry-overlap",
            overlap_ra,
            -30.0,
            overlap_evidence,
        ),
    ]

    all_rows = [row for group_id in groups for row in groups[group_id]]
    cases: list[dict[str, Any]] = []
    for object_id, group_id, ra_deg, dec_deg, evidence in case_specs:
        candidates = groups[group_id]
        output_wcs = output_wcs_contract(ra_deg, dec_deg)
        expected_bricks = plan_source_ids(candidates, output_wcs)
        if len(expected_bricks) != 2:
            raise RuntimeError(
                f"{object_id} expected two polygon-intersecting sources, found {expected_bricks}"
            )
        cases.append(
            {
                "object_id": object_id,
                "group_id": group_id,
                "ra_deg": float(ra_deg) % 360.0,
                "dec_deg": float(dec_deg),
                "candidate_bricks": sorted(row["brick_id"] for row in candidates),
                "expected_bricks": expected_bricks,
                "primary_brick": next(
                    row["brick_id"] for row in candidates if row["side"] == "west"
                ),
                "source_set_signature_sha256": hashlib.sha256(
                    json.dumps(expected_bricks, separators=(",", ":")).encode("utf-8")
                ).hexdigest(),
                "output_wcs": output_wcs,
                "geometry_evidence": evidence,
            }
        )
    return all_rows, cases


def _sky_value_pattern(
    ra_deg: np.ndarray, dec_deg: np.ndarray, value_offset: float
) -> np.ndarray:
    ra = np.deg2rad(np.asarray(ra_deg, dtype=np.float64))
    dec = np.deg2rad(np.asarray(dec_deg, dtype=np.float64))
    values = (
        100.0
        + 15.0 * np.cos(dec) * np.cos(ra)
        + 11.0 * np.cos(dec) * np.sin(ra)
        + 7.0 * np.sin(dec)
        + value_offset
    )
    return values.astype(np.float32)


def _source_pattern(wcs_contract: dict[str, Any], value_offset: float) -> np.ndarray:
    wcs = WCS(wcs_contract)
    data = np.empty((BRICK_SIZE, BRICK_SIZE), dtype=np.float32)
    x = np.arange(1, BRICK_SIZE + 1, dtype=np.float64)
    chunk_rows = 128
    for start in range(0, BRICK_SIZE, chunk_rows):
        stop = min(start + chunk_rows, BRICK_SIZE)
        y = np.arange(start + 1, stop + 1, dtype=np.float64)
        xx, yy = np.meshgrid(x, y)
        world = np.asarray(
            wcs.all_pix2world(np.column_stack((xx.ravel(), yy.ravel())), 1),
            dtype=np.float64,
        )
        data[start:stop] = _sky_value_pattern(
            world[:, 0], world[:, 1], value_offset
        ).reshape(stop - start, BRICK_SIZE)
    return data


def _source_header(row: dict[str, Any]) -> fits.Header:
    header = fits.Header()
    for key, value in row["wcs"].items():
        header[key] = value
    header["BUNIT"] = "nanomaggy"
    header["SYNTHET"] = True
    header["GROUPID"] = row["group_id"]
    header["BRICKID"] = row["brick_id"]
    header["VALOFF"] = row["value_offset"]
    return header


def _write_source_brick(root: Path, row: dict[str, Any]) -> None:
    path = root / "bricks" / f"synthetic-{row['brick_id']}-image-r.fits.fz"
    data = _source_pattern(row["wcs"], row["value_offset"])
    image = fits.CompImageHDU(
        data=data,
        header=_source_header(row),
        compression_type="GZIP_2",
        quantize_level=0,
        name="IMAGE",
    )
    fits.HDUList([fits.PrimaryHDU(), image]).writeto(
        path, overwrite=False, checksum=True
    )
    row["relative_path"] = path.relative_to(root).as_posix()
    row["file_sha256"] = sha256_path(path)
    row["data_sha256"] = hashlib.sha256(data.tobytes(order="C")).hexdigest()


def _pixel_world(output_wcs: dict[str, Any]) -> np.ndarray:
    yy, xx = np.indices((CUTOUT_SIZE, CUTOUT_SIZE), dtype=np.float64)
    return np.asarray(
        WCS(output_wcs).all_pix2world(
            np.column_stack(((xx + 1).ravel(), (yy + 1).ravel())), 1
        ),
        dtype=np.float64,
    )


def _valid_source_centres(source_wcs: dict[str, Any], world: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    pixels = np.asarray(WCS(source_wcs).all_world2pix(world, 1), dtype=np.float64)
    valid = (
        np.isfinite(pixels[:, 0])
        & np.isfinite(pixels[:, 1])
        & (pixels[:, 0] >= 1.0)
        & (pixels[:, 0] <= BRICK_SIZE)
        & (pixels[:, 1] >= 1.0)
        & (pixels[:, 1] <= BRICK_SIZE)
    )
    return pixels, valid


def _analytic_expected(
    object_row: dict[str, Any], brick_records: dict[str, dict[str, Any]]
) -> tuple[np.ndarray, np.ndarray]:
    world = _pixel_world(object_row["output_wcs"])
    total = np.zeros(CUTOUT_SIZE * CUTOUT_SIZE, dtype=np.float64)
    coverage = np.zeros(CUTOUT_SIZE * CUTOUT_SIZE, dtype=np.uint8)
    for brick_id in object_row["expected_bricks"]:
        record = brick_records[brick_id]
        _, valid = _valid_source_centres(record["wcs"], world)
        values = _sky_value_pattern(world[:, 0], world[:, 1], record["value_offset"])
        total[valid] += values[valid]
        coverage[valid] += 1
    if np.any(coverage == 0):
        raise RuntimeError(
            f"{object_row['object_id']} analytic fixture has uncovered output pixels"
        )
    expected = (total / coverage).astype(np.float32).reshape(CUTOUT_SIZE, CUTOUT_SIZE)
    return expected, coverage.reshape(CUTOUT_SIZE, CUTOUT_SIZE)


def generate_round2_fixture_tree(root: Path) -> dict[str, Any]:
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    (root / "bricks").mkdir(exist_ok=False)
    (root / "expected").mkdir(exist_ok=False)

    geometry_rows, objects = build_geometry_and_cases()
    for row in geometry_rows:
        _write_source_brick(root, row)
    brick_records = {row["brick_id"]: row for row in geometry_rows}

    for object_row in objects:
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
        "unique_grid_rule": (
            "0.25-degree declination rows; per-row RA count round(360*cos(dec)/0.25); "
            "source selection never uses this scalar rule and is always recomputed from WCS polygons"
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
        "schema_version": "yui-boundary-fixtures-round2-v1",
        "synthetic_only": True,
        "brick_size": [BRICK_SIZE, BRICK_SIZE],
        "cutout_size": [CUTOUT_SIZE, CUTOUT_SIZE],
        "pixel_scale_arcsec": PIXEL_SCALE_ARCSEC,
        "geometry_sidecar_path": "geometry_sidecar.json",
        "geometry_sidecar_sha256": sha256_path(geometry_sidecar_path),
        "objects_path": "objects.json",
        "objects_sha256": sha256_path(objects_path),
        "brick_count": len(geometry_rows),
        "object_count": len(objects),
        "planning_contract": (
            "positive-area intersection after projecting the exact output nine-point pixel-edge "
            "polygon into each distinct source TAN WCS"
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


def _load_round2(root: Path) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    sidecar = json.loads((root / "geometry_sidecar.json").read_text(encoding="utf-8"))
    return sidecar, {row["brick_id"]: row for row in sidecar["bricks"]}


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


def _sample_source(
    data: np.ndarray,
    source_wcs: dict[str, Any],
    world: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    pixels, valid = _valid_source_centres(source_wcs, world)
    sampled = np.zeros(len(world), dtype=np.float64)
    if not np.any(valid):
        return sampled, valid
    source_x = pixels[valid, 0] - 1.0
    source_y = pixels[valid, 1] - 1.0
    x0 = np.floor(source_x).astype(np.int64)
    y0 = np.floor(source_y).astype(np.int64)
    x1 = np.minimum(x0 + 1, BRICK_SIZE - 1)
    y1 = np.minimum(y0 + 1, BRICK_SIZE - 1)
    wx = source_x - x0
    wy = source_y - y0
    sampled[valid] = (
        data[y0, x0] * (1.0 - wx) * (1.0 - wy)
        + data[y0, x1] * wx * (1.0 - wy)
        + data[y1, x0] * (1.0 - wx) * wy
        + data[y1, x1] * wx * wy
    )
    return sampled, valid


def render_round2_oracle(
    root: Path,
    object_row: dict[str, Any],
    *,
    source_order: list[str] | None = None,
    output_path: Path | None = None,
) -> tuple[np.ndarray, dict[str, Any]]:
    root = Path(root)
    _, brick_records = _load_round2(root)
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
        if float(header["CRVAL1"]) != record["wcs"]["CRVAL1"] or float(header["CRVAL2"]) != record["wcs"]["CRVAL2"]:
            raise RuntimeError(f"synthetic tangent-point mismatch for {brick_id}")
        sampled, valid = _sample_source(data, record["wcs"], world)
        if np.any(valid):
            sampled_sum[valid] += sampled[valid]
            coverage[valid] += 1
            contributing.add(brick_id)

    zero_coverage = int(np.count_nonzero(coverage == 0))
    if zero_coverage:
        raise RuntimeError(f"round-2 fixture oracle found {zero_coverage} uncovered output pixels")
    if not np.array_equal(coverage, expected_coverage.ravel()):
        raise RuntimeError("round-2 analytic and sampled coverage planes disagree")
    sampled_output = (sampled_sum / coverage).astype(np.float32).reshape(
        CUTOUT_SIZE, CUTOUT_SIZE
    )
    max_abs_error = float(
        np.max(np.abs(sampled_output.astype(np.float64) - expected.astype(np.float64)))
    )
    if max_abs_error > VALUE_TOLERANCE:
        raise RuntimeError(
            f"round-2 bilinear replay exceeded {VALUE_TOLERANCE}: {max_abs_error}"
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


def render_primary_only_shape_correct(root: Path, object_row: dict[str, Any]) -> np.ndarray:
    root = Path(root)
    _, brick_records = _load_round2(root)
    primary_id = object_row["primary_brick"]
    record = brick_records[primary_id]
    with fits.open(root / record["relative_path"], memmap=False) as hdus:
        data = np.asarray(hdus[1].data)
    sampled, valid = _sample_source(data, record["wcs"], _pixel_world(object_row["output_wcs"]))
    broken = np.zeros(CUTOUT_SIZE * CUTOUT_SIZE, dtype=np.float32)
    broken[valid] = sampled[valid].astype(np.float32)
    return broken.reshape(CUTOUT_SIZE, CUTOUT_SIZE)


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main() -> int:
    arguments = build_argument_parser().parse_args()
    manifest = generate_round2_fixture_tree(arguments.output)
    print(
        json.dumps(
            {
                "status": "PASS_GENERATED_SYNTHETIC_BOUNDARY_FIXTURES_ROUND2",
                "bricks": manifest["brick_count"],
                "objects": manifest["object_count"],
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
