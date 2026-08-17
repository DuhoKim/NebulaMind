#!/usr/bin/env python3
"""Generate round-5 synthetic fixtures for a real-pattern three-source T-junction.

The geometry oracle is independent of the production adapter.  It freezes five
DR10 South brick-geometry records from the locally cached survey-bricks table:
two adjacent lower-row bricks, the offset upper-row brick spanning their shared
RA boundary, and the two nearest upper-row guard bricks.  Only synthetic pixel
rasters are written.  The real table supplies geometry and provenance, never
survey image or catalogue values.
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
    SOURCE_EDGE_PIXELS,
    VALUE_TOLERANCE,
    _analytic_expected,
    _pixel_world,
    _sample_source,
    _source_header,
    _source_pattern,
    _valid_source_centres,
    output_wcs_contract,
    plan_source_ids,
    source_wcs_contract,
)


PINNED_GENERATOR_SHA256 = {
    "make_boundary_fixtures.py": (
        "24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d"
    ),
    "make_boundary_fixtures_round2.py": (
        "60e3d662d72fbc87e0c82889b4f9174c033882b8f9a2019011c5104bb4aa15bc"
    ),
    "make_boundary_fixtures_round3.py": (
        "6b410fb40def2869d4f3431f029654d8fa7cacd20741dca5a84b12409d5e5e62"
    ),
    "make_boundary_fixtures_round4.py": (
        "d6c193841ff8ff52f1188ae1d48bbe5ea8c89bf553c542ad176f70189b7b7533"
    ),
}
ROUND5_BRIEF_SHA256 = (
    "34e4c0e4d8fa569bda1d31cf976dab9ec0314ffc9c39c88541769230f37524a6"
)
REAL_GEOMETRY_SHA256 = (
    "863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a"
)
REAL_GEOMETRY_RELATIVE_PATH = (
    "_tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/"
    "static/survey-bricks-dr10-south.fits.gz"
)

MEETING_BRICK_IDS = (
    "tj-lower-east",
    "tj-lower-west",
    "tj-upper-span",
)
GUARD_BRICK_IDS = (
    "tj-upper-east-guard",
    "tj-upper-west-guard",
)

# These values are frozen from HDU 1 of the hash-pinned local
# survey-bricks-dr10-south.fits.gz table.  They are geometry metadata only.
REAL_GEOMETRY_ROWS: tuple[dict[str, Any], ...] = (
    {
        "role": "upper-west-guard",
        "brickname": "1748m450",
        "brickid": 97326,
        "ra": 174.89236790606654,
        "dec": -45.0,
        "ra1": 174.71624266144818,
        "ra2": 175.06849315068496,
        "dec1": -45.125,
        "dec2": -44.875,
        "area": 0.06226967740390164,
        "survey_primary": True,
    },
    {
        "role": "lower-west",
        "brickname": "1752m452",
        "brickid": 96307,
        "ra": 175.22593320235757,
        "dec": -45.25,
        "ra1": 175.04911591355597,
        "ra2": 175.40275049115917,
        "dec1": -45.375,
        "dec2": -45.125,
        "area": 0.06224098742735528,
        "survey_primary": True,
    },
    {
        "role": "upper-span",
        "brickname": "1752m450",
        "brickid": 97327,
        "ra": 175.24461839530332,
        "dec": -45.0,
        "ra1": 175.06849315068496,
        "ra2": 175.42074363992174,
        "dec1": -45.125,
        "dec2": -44.875,
        "area": 0.06226967740390164,
        "survey_primary": True,
    },
    {
        "role": "lower-east",
        "brickname": "1755m452",
        "brickid": 96308,
        "ra": 175.5795677799607,
        "dec": -45.25,
        "ra1": 175.40275049115917,
        "ra2": 175.75638506876226,
        "dec1": -45.375,
        "dec2": -45.125,
        "area": 0.062240987427335276,
        "survey_primary": True,
    },
    {
        "role": "upper-east-guard",
        "brickname": "1755m450",
        "brickid": 97328,
        "ra": 175.59686888454013,
        "dec": -45.0,
        "ra1": 175.42074363992174,
        "ra2": 175.77299412915852,
        "dec1": -45.125,
        "dec2": -44.875,
        "area": 0.06226967740390164,
        "survey_primary": True,
    },
)
MATCHED_REAL_ROWS = tuple(
    row
    for row in REAL_GEOMETRY_ROWS
    if row["role"] in {"lower-west", "lower-east", "upper-span"}
)

ROLE_TO_BRICK_ID = {
    "upper-west-guard": "tj-upper-west-guard",
    "lower-west": "tj-lower-west",
    "upper-span": "tj-upper-span",
    "lower-east": "tj-lower-east",
    "upper-east-guard": "tj-upper-east-guard",
}
ROLE_TO_VALUE_OFFSET = {
    "upper-west-guard": 0.0,
    "lower-west": 0.25,
    "upper-span": 0.5,
    "lower-east": 0.75,
    "upper-east-guard": 1.0,
}

# Signed object offsets use east and north as positive.  For the vertical
# branch, negative is west/in the lower-west unique cell and positive is east.
# For the horizontal branch, negative is south/in the lower row and positive
# is north/in the upper row.  The exact case is shared by both ladders.
LADDER_REQUESTS_PIXELS: dict[str, tuple[float, float]] = {
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
OFFSET_SOLVE_TOLERANCE_PIXELS = 1e-8
GROUP_ID = "tjunction-dr10-row-offset"
JUNCTION_RA_DEG = 175.40275049115917
JUNCTION_DEC_DEG = -45.125


def _verify_parent_custody() -> dict[str, str]:
    fixture_root = Path(__file__).resolve().parent
    observed = {
        filename: sha256_path(fixture_root / filename)
        for filename in PINNED_GENERATOR_SHA256
    }
    if observed != PINNED_GENERATOR_SHA256:
        mismatches = {
            filename: {
                "expected": PINNED_GENERATOR_SHA256[filename],
                "observed": observed[filename],
            }
            for filename in PINNED_GENERATOR_SHA256
            if observed[filename] != PINNED_GENERATOR_SHA256[filename]
        }
        raise RuntimeError(
            "round-1 through round-4 generator custody mismatch; round 5 refuses "
            f"to generate: {json.dumps(mismatches, sort_keys=True)}"
        )
    return observed


def _geometry_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for source in REAL_GEOMETRY_ROWS:
        role = str(source["role"])
        wcs = source_wcs_contract(float(source["ra"]), float(source["dec"]))
        edge_world = np.asarray(
            WCS(wcs).all_pix2world(SOURCE_EDGE_PIXELS, 1), dtype=np.float64
        )
        edge_world[:, 0] %= 360.0
        row_ra_count = int(
            round(360.0 / (float(source["ra2"]) - float(source["ra1"])))
        )
        rows.append(
            {
                "brick_id": ROLE_TO_BRICK_ID[role],
                "group_id": GROUP_ID,
                "side": role,
                "synthetic_grid_ra_count": row_ra_count,
                "synthetic_grid_ra_step_deg": 360.0 / row_ra_count,
                "unique_ra_bounds_deg": [
                    float(source["ra1"]),
                    float(source["ra2"]),
                ],
                "unique_dec_bounds_deg": [
                    float(source["dec1"]),
                    float(source["dec2"]),
                ],
                "wcs": wcs,
                "pixel_edge_sky_polygon_deg": edge_world.tolist(),
                "value_offset": ROLE_TO_VALUE_OFFSET[role],
                "real_geometry_provenance": dict(source),
            }
        )
    return rows


def _signed_object_offset(
    object_ra_deg: float, object_dec_deg: float
) -> tuple[np.ndarray, np.ndarray, dict[str, Any]]:
    output_wcs = output_wcs_contract(object_ra_deg, object_dec_deg)
    junction_pixel = np.asarray(
        WCS(output_wcs).all_world2pix(
            [[JUNCTION_RA_DEG, JUNCTION_DEC_DEG]], 1
        ),
        dtype=np.float64,
    )[0]
    pixel_offset = junction_pixel - np.array([64.5, 64.5], dtype=np.float64)
    # East-positive object displacement is +x for the junction because the
    # output has CD1_1 < 0.  North-positive object displacement is -y for the
    # junction because CD2_2 > 0.
    signed_object_offset = np.array(
        [pixel_offset[0], -pixel_offset[1]], dtype=np.float64
    )
    return signed_object_offset, junction_pixel, output_wcs


def _solve_object_centre(
    requested_signed_offset_pixels: tuple[float, float]
) -> tuple[dict[str, Any], dict[str, Any]]:
    target = np.asarray(requested_signed_offset_pixels, dtype=np.float64)
    reference = WCS(output_wcs_contract(JUNCTION_RA_DEG, JUNCTION_DEC_DEG))
    # This is only a first-order seed.  The Newton solve below measures the
    # achieved offset through the final object-centred TAN projection.
    seed_pixel = np.array(
        [[64.5 - target[0], 64.5 + target[1]]], dtype=np.float64
    )
    centre = np.asarray(reference.all_pix2world(seed_pixel, 1), dtype=np.float64)[0]

    for _ in range(16):
        achieved, _, _ = _signed_object_offset(float(centre[0]), float(centre[1]))
        residual = achieved - target
        if float(np.max(np.abs(residual))) <= OFFSET_SOLVE_TOLERANCE_PIXELS:
            break
        jacobian = np.zeros((2, 2), dtype=np.float64)
        for axis in (0, 1):
            shifted = centre.copy()
            shifted[axis] += 1e-7
            shifted_achieved, _, _ = _signed_object_offset(
                float(shifted[0]), float(shifted[1])
            )
            jacobian[:, axis] = (shifted_achieved - achieved) / 1e-7
        centre -= np.linalg.solve(jacobian, residual)

    achieved, junction_pixel, output_wcs = _signed_object_offset(
        float(centre[0]), float(centre[1])
    )
    error = achieved - target
    max_error = float(np.max(np.abs(error)))
    if max_error > OFFSET_SOLVE_TOLERANCE_PIXELS:
        raise RuntimeError(
            "T-junction object-centre solve missed requested offset: "
            f"requested={target.tolist()}, achieved={achieved.tolist()}, "
            f"max_error={max_error}"
        )
    evidence = {
        "placement_method": (
            "two-dimensional Newton solve of the frozen real-geometry junction "
            "through the final object-centred TAN WCS"
        ),
        "junction_world_deg": [JUNCTION_RA_DEG, JUNCTION_DEC_DEG],
        "junction_output_pixel": junction_pixel.tolist(),
        "junction_pixel_offset_from_crpix": (
            junction_pixel - np.array([64.5, 64.5], dtype=np.float64)
        ).tolist(),
        "signed_offset_axes": ["east", "north"],
        "requested_signed_object_offset_pixels": target.tolist(),
        "achieved_signed_object_offset_pixels": achieved.tolist(),
        "solve_error_pixels": error.tolist(),
        "solve_max_abs_error_pixels": max_error,
        "solve_tolerance_pixels": OFFSET_SOLVE_TOLERANCE_PIXELS,
        "negative_vertical_meaning": "object centre is west in the lower-west unique cell",
        "positive_vertical_meaning": "object centre is east in the lower-east unique cell",
        "negative_horizontal_meaning": "object centre is south in the lower declination row",
        "positive_horizontal_meaning": "object centre is north in the upper declination row",
    }
    return output_wcs, evidence


def build_geometry_and_cases() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    geometry_rows = _geometry_rows()
    cases: list[dict[str, Any]] = []
    meeting = sorted(MEETING_BRICK_IDS)
    all_candidates = sorted(row["brick_id"] for row in geometry_rows)
    for object_id, requested in LADDER_REQUESTS_PIXELS.items():
        output_wcs, evidence = _solve_object_centre(requested)
        expected_bricks = plan_source_ids(geometry_rows, output_wcs)
        if expected_bricks != meeting:
            raise RuntimeError(
                f"{object_id} did not plan the legitimate three-source set: "
                f"expected {meeting}, observed {expected_bricks}"
            )
        cases.append(
            {
                "object_id": object_id,
                "group_id": GROUP_ID,
                "ra_deg": float(output_wcs["CRVAL1"]),
                "dec_deg": float(output_wcs["CRVAL2"]),
                "candidate_bricks": all_candidates,
                "expected_bricks": expected_bricks,
                "primary_brick": "tj-lower-west",
                "tjunction_meeting_bricks": meeting,
                "tjunction_guard_bricks": sorted(GUARD_BRICK_IDS),
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


def _real_geometry_verification() -> dict[str, Any]:
    lower_west = next(
        row for row in REAL_GEOMETRY_ROWS if row["role"] == "lower-west"
    )
    lower_east = next(
        row for row in REAL_GEOMETRY_ROWS if row["role"] == "lower-east"
    )
    upper_span = next(
        row for row in REAL_GEOMETRY_ROWS if row["role"] == "upper-span"
    )
    return {
        "claim_verified": True,
        "claim": (
            "DR10 South uses fixed 0.25-degree declination rows whose inferred full-row "
            "RA counts vary with declination; adjacent unequal-count rows offset RA "
            "boundaries and therefore contain legitimate three-cell T-junctions"
        ),
        "published_documentation": [
            {
                "url": "https://www.legacysurvey.org/dr9/description/",
                "supports": (
                    "Legacy Surveys bricks are approximately 0.25 degree by 0.25 degree "
                    "boxes on the sky; the brick name encodes the centre RA and declination"
                ),
            },
            {
                "url": "https://www.legacysurvey.org/dr10/files/",
                "supports": (
                    "survey-bricks-dr10-south.fits.gz is the DR10 South survey-brick "
                    "summary and exposes BRICKNAME/BRICKID/RA/DEC/RA1/RA2/DEC1/DEC2/AREA"
                ),
            },
        ],
        "local_geometry_source": {
            "relative_to_prereg": REAL_GEOMETRY_RELATIVE_PATH,
            "sha256": REAL_GEOMETRY_SHA256,
            "hdu": 1,
            "rows": 366912,
            "columns_read": [
                "brickname",
                "brickid",
                "ra",
                "dec",
                "ra1",
                "ra2",
                "dec1",
                "dec2",
                "area",
                "survey_primary",
            ],
            "use_limit": (
                "geometry/provenance metadata only; no survey image or catalogue values "
                "enter the synthetic fixtures"
            ),
        },
        "systematic_row_evidence": {
            "unique_declination_rows": 503,
            "declination_centre_range_deg": [-89.75, 35.75],
            "adjacent_row_pairs": 502,
            "adjacent_row_count_changes": 426,
            "row_count_derivation": (
                "round(360 / median(RA2-RA1)) for each distinct DEC row"
            ),
        },
        "matched_junction": {
            "junction_ra_deg": JUNCTION_RA_DEG,
            "junction_dec_deg": JUNCTION_DEC_DEG,
            "lower_row_ra_count": 1018,
            "upper_row_ra_count": 1022,
            "lower_boundary_equality": (
                float(lower_west["ra2"]) == float(lower_east["ra1"])
            ),
            "shared_declination_boundary_equality": (
                float(lower_west["dec2"]) == float(upper_span["dec1"])
            ),
            "lower_boundary_strictly_inside_upper_span": (
                float(upper_span["ra1"])
                < float(lower_west["ra2"])
                < float(upper_span["ra2"])
            ),
            "meeting_real_rows": [dict(row) for row in MATCHED_REAL_ROWS],
            "guard_real_rows": [
                dict(row)
                for row in REAL_GEOMETRY_ROWS
                if row["role"].endswith("guard")
            ],
        },
    }


def _write_round5_source_brick(root: Path, row: dict[str, Any]) -> None:
    """Write deterministic synthetic bytes with no timestamped checksum cards."""
    path = root / "bricks" / f"synthetic-{row['brick_id']}-image-r.fits.fz"
    data = _source_pattern(row["wcs"], row["value_offset"])
    image = fits.CompImageHDU(
        data=data,
        header=_source_header(row),
        compression_type="GZIP_2",
        quantize_level=0,
        name="IMAGE",
    )
    # astropy's checksum=True comments include the current UTC timestamp and
    # therefore change otherwise identical files.  Round 5 uses whole-file and
    # decoded-data SHA-256 custody instead, so checksum cards are deliberately
    # omitted to make two builds byte-identical.
    fits.HDUList([fits.PrimaryHDU(), image]).writeto(
        path, overwrite=False, checksum=False
    )
    blob = bytearray(path.read_bytes())
    gzip_stream_count = 0
    cursor = 0
    while True:
        header_offset = blob.find(b"\x1f\x8b\x08\x00", cursor)
        if header_offset < 0:
            break
        cursor = header_offset + 10
        if blob[header_offset + 8 : header_offset + 10] != b"\x02\xff":
            continue
        # GZIP_2 stores one gzip member per compressed row tile.  Its four-byte
        # MTIME field is wall-clock dependent but has no bearing on decoding.
        blob[header_offset + 4 : header_offset + 8] = b"\x00\x00\x00\x00"
        gzip_stream_count += 1
    if gzip_stream_count != BRICK_SIZE:
        raise RuntimeError(
            f"expected {BRICK_SIZE} GZIP_2 row-tile streams, found "
            f"{gzip_stream_count} in {path.name}"
        )
    path.write_bytes(blob)
    row["canonicalized_gzip_tile_mtime_count"] = gzip_stream_count
    row["relative_path"] = path.relative_to(root).as_posix()
    row["file_sha256"] = sha256_path(path)
    row["data_sha256"] = hashlib.sha256(data.tobytes(order="C")).hexdigest()


def generate_round5_fixture_tree(root: Path) -> dict[str, Any]:
    root = Path(root)
    observed_parent_hashes = _verify_parent_custody()
    root.mkdir(parents=True, exist_ok=True)
    (root / "bricks").mkdir()
    (root / "expected").mkdir()

    geometry_rows, objects = build_geometry_and_cases()
    for row in geometry_rows:
        _write_round5_source_brick(root, row)
    brick_records = {row["brick_id"]: row for row in geometry_rows}

    coverage_ranges: dict[str, list[int]] = {}
    for object_row in objects:
        contributing, zero_touch = _classify_pixel_contributors(
            object_row, brick_records
        )
        object_row["expected_contributing_bricks"] = contributing
        object_row["expected_zero_pixel_touch_bricks"] = zero_touch
        expected, coverage = _analytic_expected(object_row, brick_records)
        if int(coverage.min()) != 3 or int(coverage.max()) != 3:
            raise RuntimeError(
                f"{object_row['object_id']} did not retain three-source pixel coverage"
            )
        expected_path = root / "expected" / f"{object_row['object_id']}.npy"
        np.save(expected_path, expected, allow_pickle=False)
        object_row["expected_array_path"] = expected_path.relative_to(root).as_posix()
        object_row["expected_array_sha256"] = sha256_path(expected_path)
        object_row["expected_coverage_sha256"] = hashlib.sha256(
            coverage.tobytes(order="C")
        ).hexdigest()
        coverage_ranges[object_row["object_id"]] = [
            int(coverage.min()),
            int(coverage.max()),
        ]
        bits = expected.view(np.uint32)
        object_row["value_probes"] = [
            {"y": y, "x": x, "float32_bits": int(bits[y, x])}
            for y, x in ((0, 0), (0, 127), (64, 64), (127, 0), (127, 127))
        ]

    sidecar = {
        "schema_version": "yui-synthetic-geometry-sidecar-v1",
        "synthetic_only": True,
        "geometry_pattern": "dr10-south-adjacent-unequal-ra-count-row-tjunction",
        "junction_world_deg": [JUNCTION_RA_DEG, JUNCTION_DEC_DEG],
        "meeting_brick_ids": sorted(MEETING_BRICK_IDS),
        "guard_brick_ids": sorted(GUARD_BRICK_IDS),
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
        "schema_version": "yui-boundary-fixtures-round5-v1",
        "object_schema_compatible_with": "yui-boundary-fixtures-round2-v1",
        "cross_runner_loading_contract": (
            "load through the existing round-2/round-3 pinned-tree schema as a "
            "separately counted fifth fixture block"
        ),
        "synthetic_only": True,
        "brief_sha256": ROUND5_BRIEF_SHA256,
        "parent_generator_sha256": observed_parent_hashes,
        "brick_size": [BRICK_SIZE, BRICK_SIZE],
        "cutout_size": [CUTOUT_SIZE, CUTOUT_SIZE],
        "pixel_scale_arcsec": PIXEL_SCALE_ARCSEC,
        "geometry_sidecar_path": "geometry_sidecar.json",
        "geometry_sidecar_sha256": sha256_path(geometry_sidecar_path),
        "objects_path": "objects.json",
        "objects_sha256": sha256_path(objects_path),
        "brick_count": len(geometry_rows),
        "meeting_source_count": len(MEETING_BRICK_IDS),
        "guard_source_count": len(GUARD_BRICK_IDS),
        "object_count": len(objects),
        "requested_signed_object_offsets_pixels": {
            object_id: list(offset)
            for object_id, offset in LADDER_REQUESTS_PIXELS.items()
        },
        "achieved_signed_object_offsets_pixels": {
            row["object_id"]: row["geometry_evidence"][
                "achieved_signed_object_offset_pixels"
            ]
            for row in objects
        },
        "coverage_min_max_by_object": coverage_ranges,
        "real_geometry_verification": _real_geometry_verification(),
        "planning_contract": (
            "positive-area intersection after projecting the exact output nine-point "
            "pixel-edge polygon into each distinct source TAN WCS; five local candidates "
            "prove exactly three planned sources while two nearest upper-row guards stay out"
        ),
        "junction_ladder_contract": (
            "east/north-positive object-centre offsets of -10, -0.25, exact 0, +0.25, "
            "and +1 pixels are solved independently across the vertical and horizontal "
            "unique-area branches, with the exact junction shared"
        ),
        "pattern_contract": (
            "float32 smooth spherical sky function plus a declared per-brick value_offset; "
            "expected pixels average all three valid planned contributors"
        ),
        "storage_determinism_contract": (
            "GZIP_2 row-tile MTIME fields are canonicalized to zero and timestamped FITS "
            "checksum cards are omitted; whole-file and decoded-data SHA-256 values provide "
            "custody, and two consecutive builds must be byte-identical"
        ),
        "failure_contract": (
            "all planned source paths and SHA-256 digests are verified before output write"
        ),
        "scope_limit": (
            "synthetic reproduction of one verified real row-offset geometry pattern; not "
            "real survey image validation, adapter validation, or production acceptance"
        ),
    }
    (root / "fixture_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return manifest


def _load_round5(root: Path) -> dict[str, dict[str, Any]]:
    sidecar = json.loads(
        (root / "geometry_sidecar.json").read_text(encoding="utf-8")
    )
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
                f"{brick_id} digest mismatch: expected {record['file_sha256']}, "
                f"observed {observed}"
            )


def render_round5_oracle(
    root: Path,
    object_row: dict[str, Any],
    *,
    source_order: list[str] | None = None,
    output_path: Path | None = None,
) -> tuple[np.ndarray, dict[str, Any]]:
    root = Path(root)
    brick_records = _load_round5(root)
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
        data_hash = hashlib.sha256(data.tobytes(order="C")).hexdigest()
        if data_hash != record["data_sha256"]:
            raise FixtureSourceError(
                f"{brick_id} decoded data digest mismatch: expected "
                f"{record['data_sha256']}, observed {data_hash}"
            )
        sampled, valid = _sample_source(data, record["wcs"], world)
        if np.any(valid):
            sampled_sum[valid] += sampled[valid]
            coverage[valid] += 1
            contributing.add(brick_id)

    zero_coverage = int(np.count_nonzero(coverage == 0))
    if zero_coverage:
        raise RuntimeError(
            f"round-5 fixture oracle found {zero_coverage} uncovered output pixels"
        )
    if not np.array_equal(coverage, expected_coverage.ravel()):
        raise RuntimeError("round-5 analytic and sampled coverage planes disagree")
    sampled_output = (sampled_sum / coverage).astype(np.float32).reshape(
        CUTOUT_SIZE, CUTOUT_SIZE
    )
    max_abs_error = float(
        np.max(
            np.abs(
                sampled_output.astype(np.float64) - expected.astype(np.float64)
            )
        )
    )
    if max_abs_error > VALUE_TOLERANCE:
        raise RuntimeError(
            f"round-5 bilinear replay exceeded {VALUE_TOLERANCE}: {max_abs_error}"
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
        "output_array_sha256": hashlib.sha256(
            expected.tobytes(order="C")
        ).hexdigest(),
    }
    if output_path is not None:
        output_path = Path(output_path)
        temporary_path = output_path.with_name(output_path.name + ".tmp")
        with temporary_path.open("wb") as handle:
            np.save(handle, expected, allow_pickle=False)
        temporary_path.replace(output_path)
    return expected, receipt


def verify_round5_fixture_tree(root: Path) -> dict[str, Any]:
    root = Path(root)
    manifest_path = root / "fixture_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    objects_path = root / manifest["objects_path"]
    sidecar_path = root / manifest["geometry_sidecar_path"]
    if sha256_path(objects_path) != manifest["objects_sha256"]:
        raise RuntimeError("round-5 objects.json custody mismatch")
    if sha256_path(sidecar_path) != manifest["geometry_sidecar_sha256"]:
        raise RuntimeError("round-5 geometry sidecar custody mismatch")
    objects = json.loads(objects_path.read_text(encoding="utf-8"))
    sidecar = json.loads(sidecar_path.read_text(encoding="utf-8"))
    brick_records = {row["brick_id"]: row for row in sidecar["bricks"]}

    source_hashes: dict[str, str] = {}
    for brick_id, record in sorted(brick_records.items()):
        source_path = root / record["relative_path"]
        observed_file_hash = sha256_path(source_path)
        if observed_file_hash != record["file_sha256"]:
            raise FixtureSourceError(f"{brick_id} file custody mismatch")
        with fits.open(source_path, memmap=False) as hdus:
            data = np.asarray(hdus[1].data)
        observed_data_hash = hashlib.sha256(data.tobytes(order="C")).hexdigest()
        if observed_data_hash != record["data_sha256"]:
            raise FixtureSourceError(f"{brick_id} decoded data custody mismatch")
        source_hashes[brick_id] = observed_file_hash

    output_hashes: dict[str, str] = {}
    coverage_hashes: dict[str, str] = {}
    max_replay_error = 0.0
    for object_row in objects:
        expected_path = root / object_row["expected_array_path"]
        if sha256_path(expected_path) != object_row["expected_array_sha256"]:
            raise RuntimeError(
                f"{object_row['object_id']} expected-array custody mismatch"
            )
        expected = np.load(expected_path, allow_pickle=False)
        forward, forward_receipt = render_round5_oracle(root, object_row)
        reverse, reverse_receipt = render_round5_oracle(
            root,
            object_row,
            source_order=list(reversed(object_row["expected_bricks"])),
        )
        if not np.array_equal(forward, expected) or not np.array_equal(reverse, expected):
            raise RuntimeError(
                f"{object_row['object_id']} exact expected-array replay mismatch"
            )
        if forward_receipt["output_array_sha256"] != reverse_receipt[
            "output_array_sha256"
        ]:
            raise RuntimeError(
                f"{object_row['object_id']} source-order output hash mismatch"
            )
        if forward_receipt["coverage_array_sha256"] != object_row[
            "expected_coverage_sha256"
        ]:
            raise RuntimeError(
                f"{object_row['object_id']} coverage hash mismatch"
            )
        output_hashes[object_row["object_id"]] = forward_receipt[
            "output_array_sha256"
        ]
        coverage_hashes[object_row["object_id"]] = forward_receipt[
            "coverage_array_sha256"
        ]
        max_replay_error = max(
            max_replay_error,
            float(forward_receipt["bilinear_sample_max_abs_error"]),
            float(reverse_receipt["bilinear_sample_max_abs_error"]),
        )

    return {
        "status": "PASS",
        "manifest_sha256": sha256_path(manifest_path),
        "objects_sha256": sha256_path(objects_path),
        "geometry_sidecar_sha256": sha256_path(sidecar_path),
        "cases_verified": len(objects),
        "source_files_verified": len(brick_records),
        "meeting_source_count": len(MEETING_BRICK_IDS),
        "guard_source_count": len(GUARD_BRICK_IDS),
        "source_order_replays": len(objects) * 2,
        "coverage_min": 3,
        "coverage_max": 3,
        "max_bilinear_replay_abs_error": max_replay_error,
        "source_file_sha256": source_hashes,
        "output_array_sha256": output_hashes,
        "coverage_array_sha256": coverage_hashes,
    }


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--verify-existing", action="store_true")
    return parser


def main() -> int:
    arguments = build_argument_parser().parse_args()
    if arguments.verify_existing:
        result = verify_round5_fixture_tree(arguments.output)
    else:
        manifest = generate_round5_fixture_tree(arguments.output)
        result = {
            "status": "PASS_GENERATED_SYNTHETIC_TJUNCTION_FIXTURES_ROUND5",
            "bricks": manifest["brick_count"],
            "objects": manifest["object_count"],
        }
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
