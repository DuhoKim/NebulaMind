#!/usr/bin/env python3
"""Generate offline synthetic DR10-like bricks for boundary-contract testing.

This is a fixture oracle, not Tori's production adapter.  It uses one shared TAN
projection so overlapping source pixels carry the same non-zero global-coordinate
pattern.  A crop, zero pad, shifted strip, or wrong-neighbour read therefore
changes values even when the returned array still has shape 128 x 128.
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

BRICK_SIZE = 3600
CUTOUT_SIZE = 128
PIXEL_SCALE_ARCSEC = 0.262
CD_DEG_PER_PIXEL = PIXEL_SCALE_ARCSEC / 3600.0
STRIDE = 3472
SOURCE_OVERLAP_PIXELS = BRICK_SIZE - STRIDE
UNIQUE_HALF_SIZE = STRIDE // 2
SOURCE_HALF_SIZE = BRICK_SIZE // 2
REFERENCE_RA_DEG = 180.0
REFERENCE_DEC_DEG = -30.0


class MissingNeighbourError(RuntimeError):
    """A polygon-intersecting synthetic source brick is unavailable."""


class FixtureSourceError(RuntimeError):
    """A required synthetic source no longer matches its fixture manifest."""


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _pattern_from_doubled_global(x2: np.ndarray, y2: np.ndarray) -> np.ndarray:
    """Return a positive linear sky-plane pattern with independent x/y slopes."""
    y_term = y2.astype(np.float64)[:, np.newaxis] * 0.001
    x_term = x2.astype(np.float64)[np.newaxis, :] * 0.00005
    return (20.0 + y_term + x_term).astype(np.float32)


def brick_pattern(origin_x: int, origin_y: int) -> np.ndarray:
    indices = np.arange(BRICK_SIZE, dtype=np.int64)
    x2 = 2 * origin_x + 2 * indices - (BRICK_SIZE - 1)
    y2 = 2 * origin_y + 2 * indices - (BRICK_SIZE - 1)
    return _pattern_from_doubled_global(x2, y2)


def output_wcs_contract(center_x: int, center_y: int) -> dict[str, Any]:
    ra, dec = _world_for_global(center_x, center_y)
    return {
        "NAXIS1": CUTOUT_SIZE,
        "NAXIS2": CUTOUT_SIZE,
        "CTYPE1": "RA---TAN",
        "CTYPE2": "DEC--TAN",
        "CRVAL1": ra,
        "CRVAL2": dec,
        "CRPIX1": 64.5,
        "CRPIX2": 64.5,
        "CD1_1": -CD_DEG_PER_PIXEL,
        "CD1_2": 0.0,
        "CD2_1": 0.0,
        "CD2_2": CD_DEG_PER_PIXEL,
    }


def expected_cutout(center_x: int, center_y: int) -> np.ndarray:
    output_wcs = WCS(output_wcs_contract(center_x, center_y))
    yy, xx = np.indices((CUTOUT_SIZE, CUTOUT_SIZE), dtype=np.float64)
    world = output_wcs.all_pix2world(
        np.column_stack(((xx + 1).ravel(), (yy + 1).ravel())),
        1,
    )
    common_pixels = WCS(brick_header(0, 0, 0, 0)).all_world2pix(world, 1)
    global_x = np.asarray(common_pixels)[:, 0] - 1800.5
    global_y = np.asarray(common_pixels)[:, 1] - 1800.5
    return (20.0 + global_y * 0.002 + global_x * 0.0001).astype(np.float32).reshape(
        CUTOUT_SIZE, CUTOUT_SIZE
    )


def nine_point_pixel_edge_polygon(center_x: int, center_y: int, size: int) -> list[list[int]]:
    half = size // 2
    left, right = center_x - half, center_x + half
    bottom, top = center_y - half, center_y + half
    return [
        [left, bottom],
        [center_x, bottom],
        [right, bottom],
        [right, center_y],
        [right, top],
        [center_x, top],
        [left, top],
        [left, center_y],
        [left, bottom],
    ]


def output_pixel_edge_polygon_global(center_x: int, center_y: int) -> list[list[float]]:
    edge_pixels = np.array(
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
    world = WCS(output_wcs_contract(center_x, center_y)).all_pix2world(edge_pixels, 1)
    common = np.asarray(WCS(brick_header(0, 0, 0, 0)).all_world2pix(world, 1))
    common -= np.array([1800.5, 1800.5])
    return common.tolist()


def _polygons_intersect_with_positive_area(
    first: list[list[float]], second: list[list[float]]
) -> bool:
    polygons = (np.asarray(first[:-1], dtype=np.float64), np.asarray(second[:-1], dtype=np.float64))
    for polygon in polygons:
        for index in range(len(polygon)):
            edge = polygon[(index + 1) % len(polygon)] - polygon[index]
            axis = np.array([-edge[1], edge[0]], dtype=np.float64)
            if not np.any(axis):
                continue
            first_projection = polygons[0] @ axis
            second_projection = polygons[1] @ axis
            if (
                first_projection.max() <= second_projection.min()
                or second_projection.max() <= first_projection.min()
            ):
                return False
    return True


def planned_bricks(center_x: int, center_y: int) -> list[str]:
    """Return every source with positive-area nine-point polygon overlap."""
    output_polygon = output_pixel_edge_polygon_global(center_x, center_y)
    planned: list[str] = []
    for row in (-1, 0, 1):
        for column in (-1, 0, 1):
            origin_x = column * STRIDE
            origin_y = row * STRIDE
            source_polygon = nine_point_pixel_edge_polygon(origin_x, origin_y, BRICK_SIZE)
            if _polygons_intersect_with_positive_area(output_polygon, source_polygon):
                planned.append(f"r{row:+d}c{column:+d}")
    return sorted(planned)


def _world_for_global(center_x: int, center_y: int) -> tuple[float, float]:
    wcs = WCS(brick_header(0, 0, 0, 0))
    world = wcs.all_pix2world([[center_x + 1800.5, center_y + 1800.5]], 1)[0]
    return float(world[0] % 360.0), float(world[1])


def _case(object_id: str, center_x: int, center_y: int, case: str) -> dict[str, Any]:
    ra, dec = _world_for_global(center_x, center_y)
    expected_bricks = planned_bricks(center_x, center_y)
    return {
        "object_id": object_id,
        "center_x": center_x,
        "center_y": center_y,
        "ra_deg": ra,
        "dec_deg": dec,
        "case": case,
        "expected_bricks": expected_bricks,
        "source_set_signature_sha256": hashlib.sha256(
            json.dumps(expected_bricks, separators=(",", ":")).encode("utf-8")
        ).hexdigest(),
        "output_pixel_edge_polygon_global": output_pixel_edge_polygon_global(center_x, center_y),
        "output_wcs": output_wcs_contract(center_x, center_y),
    }


def fixture_cases() -> list[dict[str, Any]]:
    cases = [_case("centre", 0, 0, "centre-control")]
    directions = {
        "north": (0, 1),
        "south": (0, -1),
        "east": (-1, 0),
        "west": (1, 0),
    }
    distances = (
        ("no_neighbour", 1607, "output ends before adjacent source footprint"),
        ("overlap_only", 1609, "adjacent source overlaps without unique-boundary crossing"),
        ("within_63px", 1673, "centre within output half-width of unique edge"),
        ("exact", UNIQUE_HALF_SIZE, "centre exactly on unique edge"),
        ("beyond", UNIQUE_HALF_SIZE + 1, "centre one pixel beyond unique edge"),
    )
    for direction, (dx, dy) in directions.items():
        for suffix, distance, description in distances:
            cases.append(
                _case(
                    f"edge_{direction}_{suffix}",
                    dx * distance,
                    dy * distance,
                    description,
                )
            )

    corners = {
        "north_east": (-UNIQUE_HALF_SIZE, UNIQUE_HALF_SIZE),
        "north_west": (UNIQUE_HALF_SIZE, UNIQUE_HALF_SIZE),
        "south_east": (-UNIQUE_HALF_SIZE, -UNIQUE_HALF_SIZE),
        "south_west": (UNIQUE_HALF_SIZE, -UNIQUE_HALF_SIZE),
    }
    for corner, (center_x, center_y) in corners.items():
        cases.append(
            _case(
                f"corner_{corner}_exact",
                center_x,
                center_y,
                "centre exactly on both unique edges; side and diagonal neighbours required",
            )
        )
        cases.append(
            _case(
                f"corner_{corner}_beyond",
                center_x + (-1 if center_x < 0 else 1),
                center_y + (-1 if center_y < 0 else 1),
                "centre one pixel beyond both unique edges; truncated-primary stress case",
            )
        )
    return cases


def brick_header(origin_x: int, origin_y: int, row: int, column: int) -> fits.Header:
    header = fits.Header()
    header["CTYPE1"] = "RA---TAN"
    header["CTYPE2"] = "DEC--TAN"
    header["CRVAL1"] = REFERENCE_RA_DEG
    header["CRVAL2"] = REFERENCE_DEC_DEG
    header["CRPIX1"] = 1800.5 - origin_x
    header["CRPIX2"] = 1800.5 - origin_y
    header["CD1_1"] = -CD_DEG_PER_PIXEL
    header["CD1_2"] = 0.0
    header["CD2_1"] = 0.0
    header["CD2_2"] = CD_DEG_PER_PIXEL
    header["BUNIT"] = "nanomaggy"
    header["SYNTHET"] = True
    header["GRIDROW"] = row
    header["GRIDCOL"] = column
    header["ORIGINX"] = origin_x
    header["ORIGINY"] = origin_y
    return header


def _write_brick(path: Path, origin_x: int, origin_y: int, row: int, column: int) -> dict[str, Any]:
    data = brick_pattern(origin_x, origin_y)
    image = fits.CompImageHDU(
        data=data,
        header=brick_header(origin_x, origin_y, row, column),
        compression_type="GZIP_2",
        quantize_level=0,
        name="IMAGE",
    )
    fits.HDUList([fits.PrimaryHDU(), image]).writeto(path, overwrite=False, checksum=True)
    return {
        "brick_id": f"r{row:+d}c{column:+d}",
        "grid_row": row,
        "grid_column": column,
        "origin_x": origin_x,
        "origin_y": origin_y,
        "pixel_edge_polygon_global": nine_point_pixel_edge_polygon(
            origin_x, origin_y, BRICK_SIZE
        ),
        "relative_path": path.relative_to(path.parents[1]).as_posix(),
        "file_sha256": sha256_path(path),
        "data_sha256": hashlib.sha256(data.tobytes(order="C")).hexdigest(),
    }


def generate_fixture_tree(root: Path) -> dict[str, Any]:
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    bricks_root = root / "bricks"
    bricks_root.mkdir(exist_ok=False)
    expected_root = root / "expected"
    expected_root.mkdir(exist_ok=False)

    bricks: list[dict[str, Any]] = []
    for row in (-1, 0, 1):
        for column in (-1, 0, 1):
            path = bricks_root / f"synthetic-r{row:+d}c{column:+d}-image-r.fits.fz"
            bricks.append(_write_brick(path, column * STRIDE, row * STRIDE, row, column))

    objects = fixture_cases()
    for object_row in objects:
        expected_path = expected_root / f"{object_row['object_id']}.npy"
        expected = expected_cutout(object_row["center_x"], object_row["center_y"])
        np.save(expected_path, expected, allow_pickle=False)
        object_row["expected_array_path"] = expected_path.relative_to(root).as_posix()
        object_row["expected_array_sha256"] = sha256_path(expected_path)
        expected_bits = expected.view(np.uint32)
        object_row["value_probes"] = [
            {"y": y, "x": x, "float32_bits": int(expected_bits[y, x])}
            for y, x in ((0, 0), (0, 127), (64, 64), (127, 0), (127, 127))
        ]
    (root / "objects.json").write_text(
        json.dumps(objects, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    manifest: dict[str, Any] = {
        "schema_version": "yui-boundary-fixtures-v1",
        "synthetic_only": True,
        "brick_size": [BRICK_SIZE, BRICK_SIZE],
        "cutout_size": [CUTOUT_SIZE, CUTOUT_SIZE],
        "pixel_scale_arcsec": PIXEL_SCALE_ARCSEC,
        "cd_deg_per_pixel": CD_DEG_PER_PIXEL,
        "stride_pixels": STRIDE,
        "source_overlap_pixels": SOURCE_OVERLAP_PIXELS,
        "pattern_contract": "float32(20 + global_y*0.002 + global_x*0.0001)",
        "bricks": bricks,
        "objects_path": "objects.json",
    }
    (root / "fixture_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def render_fixture_oracle(
    root: Path,
    object_row: dict[str, Any],
    *,
    source_order: list[str] | None = None,
    output_path: Path | None = None,
) -> tuple[np.ndarray, dict[str, Any]]:
    """Replay fixture sources into the exact output TAN WCS; not the production adapter."""
    root = Path(root)
    manifest = json.loads((root / "fixture_manifest.json").read_text(encoding="utf-8"))
    brick_records = {row["brick_id"]: row for row in manifest["bricks"]}
    expected_bricks = sorted(object_row["expected_bricks"])
    order = list(source_order) if source_order is not None else list(expected_bricks)
    if len(order) != len(set(order)) or set(order) != set(expected_bricks):
        raise ValueError("source_order must contain every expected brick exactly once")
    missing = [
        brick_id
        for brick_id in expected_bricks
        if brick_id not in brick_records
        or not (root / brick_records[brick_id]["relative_path"]).is_file()
    ]
    if missing:
        raise MissingNeighbourError(f"missing required neighbour brick(s): {', '.join(missing)}")
    for brick_id in expected_bricks:
        record = brick_records[brick_id]
        observed_sha256 = sha256_path(root / record["relative_path"])
        if observed_sha256 != record["file_sha256"]:
            raise FixtureSourceError(
                f"{brick_id} digest mismatch: expected {record['file_sha256']}, observed {observed_sha256}"
            )

    output_wcs = WCS(object_row["output_wcs"])
    yy, xx = np.indices((CUTOUT_SIZE, CUTOUT_SIZE), dtype=np.float64)
    world = output_wcs.all_pix2world(
        np.column_stack(((xx + 1).ravel(), (yy + 1).ravel())),
        1,
    )
    sampled_sum = np.zeros(CUTOUT_SIZE * CUTOUT_SIZE, dtype=np.float64)
    coverage = np.zeros((CUTOUT_SIZE, CUTOUT_SIZE), dtype=np.uint8)
    contributing: set[str] = set()
    for brick_id in order:
        record = brick_records[brick_id]
        path = root / record["relative_path"]
        with fits.open(path, memmap=False) as hdus:
            data = np.asarray(hdus[1].data)
            source_wcs = WCS(hdus[1].header)
        if data.shape != (BRICK_SIZE, BRICK_SIZE) or data.dtype != np.dtype("float32"):
            raise RuntimeError(f"invalid synthetic brick {brick_id}")

        source_pixels = np.asarray(source_wcs.all_world2pix(world, 1), dtype=np.float64)
        source_x = source_pixels[:, 0] - 1.0
        source_y = source_pixels[:, 1] - 1.0
        valid = (
            (source_x >= 0.0)
            & (source_x <= BRICK_SIZE - 1)
            & (source_y >= 0.0)
            & (source_y <= BRICK_SIZE - 1)
        )
        if not np.any(valid):
            continue

        valid_indices = np.flatnonzero(valid)
        valid_x = source_x[valid]
        valid_y = source_y[valid]
        x0 = np.floor(valid_x).astype(np.int64)
        y0 = np.floor(valid_y).astype(np.int64)
        x1 = np.minimum(x0 + 1, BRICK_SIZE - 1)
        y1 = np.minimum(y0 + 1, BRICK_SIZE - 1)
        wx = valid_x - x0
        wy = valid_y - y0
        sampled = (
            data[y0, x0] * (1.0 - wx) * (1.0 - wy)
            + data[y0, x1] * wx * (1.0 - wy)
            + data[y1, x0] * (1.0 - wx) * wy
            + data[y1, x1] * wx * wy
        )
        sampled_sum[valid_indices] += sampled
        coverage.ravel()[valid_indices] += 1
        contributing.add(brick_id)

    zero_coverage = int(np.count_nonzero(coverage == 0))
    if zero_coverage:
        raise RuntimeError(f"fixture oracle found {zero_coverage} uncovered output pixels")
    sampled_output = (sampled_sum / coverage.ravel()).astype(np.float32).reshape(
        CUTOUT_SIZE, CUTOUT_SIZE
    )
    output = expected_cutout(object_row["center_x"], object_row["center_y"])
    max_abs_error = float(np.max(np.abs(sampled_output.astype(np.float64) - output)))
    if max_abs_error > 5e-6:
        raise RuntimeError(
            f"fixture resampling oracle exceeded 5e-6 absolute tolerance: {max_abs_error}"
        )
    receipt = {
        "object_id": object_row["object_id"],
        "planned_bricks": expected_bricks,
        "opened_bricks": sorted(order),
        "contributing_bricks": sorted(contributing),
        "zero_pixel_touch_bricks": sorted(set(expected_bricks) - contributing),
        "coverage_min": int(coverage.min()),
        "coverage_max": int(coverage.max()),
        "zero_coverage_pixels": zero_coverage,
        "bilinear_sample_max_abs_error": max_abs_error,
        "adapter_comparison_absolute_tolerance": 5e-6,
        "coverage_array_sha256": hashlib.sha256(coverage.tobytes(order="C")).hexdigest(),
        "output_array_sha256": hashlib.sha256(output.tobytes(order="C")).hexdigest(),
    }
    if output_path is not None:
        output_path = Path(output_path)
        temporary_path = output_path.with_name(output_path.name + ".tmp")
        with temporary_path.open("wb") as handle:
            np.save(handle, output, allow_pickle=False)
        temporary_path.replace(output_path)
    return output, receipt


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main() -> int:
    arguments = build_argument_parser().parse_args()
    manifest = generate_fixture_tree(arguments.output)
    print(json.dumps({"status": "PASS_GENERATED_SYNTHETIC_BOUNDARY_FIXTURES", "bricks": len(manifest["bricks"])}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
