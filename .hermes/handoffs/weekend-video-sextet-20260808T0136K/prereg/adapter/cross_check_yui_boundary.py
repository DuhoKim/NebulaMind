#!/usr/bin/env python3
"""Adapter-side cross-check: Yui's boundary fixtures through the adapter.

Runs BOTH of Yui's independently-built boundary fixture rounds through
`nm_brick_cutout_adapter` planning and local cutting, and writes
`CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json` next to the adapter. This makes the
cross-check an adapter receipt (Kun's corner-repair condition 5), extended on
2026-08-16 to cover the round-2 boundary classes after the round-1-only
receipt was flagged as narrower than it looked.

Round 1 (`make_boundary_fixtures.py`, 29 objects): shared-tangent 3x3 grid at
(180, -30) — centre, edge, overlap-only, exact/beyond edge, exact/beyond
corner. The fixture tree is regenerated in a temp directory each run.

Round 2 (`make_boundary_fixtures_round2.py`, 4 objects): distinct per-brick
tangent points — RA-wrap seam crossing at dec -10, selected-footprint
declination extremes at +32.25 and -89.875, and a derived
overlap-without-unique-crossing case at dec -30. The pinned pre-generated
tree `boundary_fixtures/generated_round2/` is loaded read-only; its
objects/sidecar hashes are verified against its own manifest before use.

Round 3 (`make_boundary_fixtures_round3.py`, 10 objects): extreme-declination
sub-pixel knife edges — signed offset ladders (-10, -0.25, 0, +0.25, +1
candidate-source pixels, solved to 1e-8 px) at both selected-footprint
declination extremes. Round-3 fixtures also declare expected CONTRIBUTING and
ZERO-PIXEL-TOUCH sets, and the cross-check compares planned, opened, AND
contributing/zero-touch against them: at the +1 and +0.25 offsets the
knife-edge source is legitimately planned yet contributes no output pixel
centre, so planned and contributing differ by design. The pinned pre-generated
tree `boundary_fixtures/generated_round3/` is loaded read-only, hash-verified
against its own manifest.

Round-1, round-2, and round-3 results are reported SEPARATELY and never
merged into one total: a single number would hide exactly the scope ambiguity
this receipt exists to prevent.

Pixel values (2026-08-16 resampler gate): the adapter renderer is now a
bilinear resampler matching the oracle's interpolation rule, and this
cross-check stages Yui's exact brick pixel data (verified against her
recorded data_sha256) and compares adapter output arrays against her expected
arrays at HER pre-declared absolute tolerances: 5e-6 for round 1, 1e-5 for
rounds 2-3. Round-1 comparison covers only cases planned entirely within the
centre brick, where Yui's shared-tangent fixture model and the adapter's
per-brick-TAN source model coincide identically; neighbour-involving round-1
cases are skipped with the geometric reason recorded in the receipt.

Yui's artifacts are imported/loaded read-only and never modified. The round-1
geometry mapping mirrors Kun's scratch cross-runner
(`prereg/_tmp_kun_cross_adapter_fixtures_20260816.py`).

Synthetic only. No network, no real survey data.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREREG = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(PREREG / "boundary_fixtures"))
sys.path.insert(0, str(PREREG / "readstage"))

import numpy as np  # noqa: E402
from astropy.io import fits  # noqa: E402

import make_boundary_fixtures as yui  # noqa: E402  (Yui's round-1 oracle, read-only)
from make_boundary_fixtures_round2 import VALUE_TOLERANCE as ROUND23_PIXEL_TOLERANCE  # noqa: E402
import nm_brick_cutout_adapter as tori  # noqa: E402
import nm_brick_read_stage as readstage  # noqa: E402  (pinned .fits.fz decode stage)

# Yui's round-1 declared comparison bound: render_fixture_oracle emits
# "adapter_comparison_absolute_tolerance": 5e-6 in make_boundary_fixtures.py.
ROUND1_PIXEL_TOLERANCE = 5e-6
ROUND1_PIXEL_SKIP_REASON = (
    "round-1 bricks share ONE tangent plane (Yui's declared approximation); the adapter's "
    "production-shaped source model is per-brick TAN, which displaces neighbour-brick "
    "sampling by up to ~1.4 px at 0.25 deg from the shared tangent point. Pixel comparison "
    "on neighbour-involving cases would measure that mapping approximation, not the "
    "resampler; rounds 2-3 (distinct per-brick tangent points) exist to supersede it. "
    "Compared cases are exactly those whose planned set is the centre brick alone, where "
    "the two source models coincide identically."
)

RECEIPT_PATH = HERE / "CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json"
KUN_SCRATCH_RUNNER = PREREG / "_tmp_kun_cross_adapter_fixtures_20260816.py"
ROUND2_GENERATOR = PREREG / "boundary_fixtures" / "make_boundary_fixtures_round2.py"
ROUND2_GENERATED = PREREG / "boundary_fixtures" / "generated_round2"
ROUND3_GENERATOR = PREREG / "boundary_fixtures" / "make_boundary_fixtures_round3.py"
ROUND3_GENERATED = PREREG / "boundary_fixtures" / "generated_round3"
ROUND4_GENERATOR = PREREG / "boundary_fixtures" / "make_boundary_fixtures_round4.py"
ROUND4_GENERATED = PREREG / "boundary_fixtures" / "generated_round4"
READ_STAGE_PATH = PREREG / "readstage" / "nm_brick_read_stage.py"

SCOPE_STATEMENT = {
    "covered": [
        "round-1: shared-tangent 3x3 grid at (180, -30): centre control, edge cases "
        "(no-neighbour gap, overlap-only, within-63px, exact-edge, one-pixel-beyond) in all "
        "four directions, and exact-/beyond-corner in all four corners — planned source sets, "
        "end-to-end cut completion, PC-3 planned/opened set equality, coverage_min >= 1, "
        "zero uncovered pixels",
        "round-2: distinct per-brick TAN tangent points; RA-wrap seam crossing at dec -10; "
        "selected-footprint declination extremes at +32.25 and -89.875; derived "
        "overlap-without-unique-boundary-crossing at dec -30 — same comparisons as round 1",
        "round-3: extreme-declination sub-pixel knife edges at both selected-footprint "
        "declination extremes (+32.25 and -89.875): signed candidate-edge offset ladder "
        "(-10, -0.25, exact 0, +0.25, +1 source pixels, solved to 1e-8 px); exact zero-area "
        "tangency excluded from planning; and the planned/opened/contributing/zero-pixel-"
        "touch distinction compared against Yui's declared expectations — including the "
        "cases where a source is legitimately planned (positive intersection area) yet "
        "contributes no output pixel centre",
        "pixel-value agreement against Yui's expected arrays, on her exact hash-verified "
        "brick data, at her pre-declared absolute tolerances (round-1 5e-6 on centre-brick-"
        "only cases; rounds 2-3 1e-5 on all cases): the adapter renderer is a bilinear "
        "resampler with the oracle's interpolation rule (support window [1, N], float64 "
        "accumulation, mean over coverage)",
        "round-4: production-shaped .fits.fz read path through the separate pinned read "
        "stage (nm_brick_read_stage.py): empty-primary + RICE_1 image-HDU-1 files; raw "
        "compression cards (ZIMAGE/ZCMPTYPE/ZBITPIX/ZNAXIS1/2) gated terminally BEFORE "
        "decode; decompressed arrays hash-equal to the parent uncompressed data; WCS cards "
        "verified against the geometry sidecar; and the adapter output from read-stage "
        "staging byte-identical (exact, no tolerance) to the uncompressed staging path — "
        "the adapter itself stays stdlib-only and cannot tell the two provenances apart",
    ],
    "not_covered": [
        "exact float32 bit-equality of pixel values: unreachable in principle because Yui's "
        "expected arrays are analytic (float64 sky pattern evaluated at output-pixel world "
        "coordinates) while any real resampler interpolates the float32-quantized brick "
        "rasters — the irreducible residual is float32 quantization (~7e-6 at fixture "
        "values ~100-120, ~2e-6 at ~20) plus bilinear truncation, which is why the "
        "comparison bound is Yui's declared tolerance, not bit-equality",
        "round-1 pixel values on neighbour-involving cases: Yui's round-1 bricks share one "
        "tangent plane (her declared approximation), the adapter's source model is "
        "per-brick TAN; the mapping difference displaces neighbour-brick sampling by up to "
        "~1.4 px, so value comparison there would measure the fixture-model gap, not the "
        "resampler — rounds 2-3 supersede that model and ARE value-compared in full",
        "equivalence with the hash-pinned Imagine/astrometry.net production resampler "
        "kernel: bound to Yui's dependency lock (in progress, separate deliverable); this "
        "gate proves oracle-bilinear semantics, not production-kernel identity",
        "Yui's 'primary_brick' (west-side convention) is recorded but not compared: the "
        "adapter primary is grouping metadata under the nearest-planned-centre rule and "
        "never a selection rule",
        "real (non-synthetic) brick reads: the read stage terminally refuses any logical "
        "header without the SYNTHET marker — lifting that build-only guard for real DR10 "
        "bricks is a later explicit gate; the read stage's decoder environment lock "
        "(interpreter/astropy/numpy versions plus tile-compression module hashes) is a "
        "partial pin pending Yui's dependency lock",
        "real DR10 South geometry-sidecar bricks, multi-process scheduling determinism, "
        "full dependency/container lock — later gates",
    ],
}


def _sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _object_key(object_id: str) -> str:
    allowed = [char if char.isalnum() else "-" for char in object_id.upper()]
    return "SYNTH-" + "".join(allowed)[:57]


def _stage_brick_with_yui_data(source_root, geometry_row, tree_root: Path, brick_record) -> None:
    """Stage Yui's exact brick pixel data (hash-verified) in the adapter format."""
    with fits.open(tree_root / brick_record["relative_path"], memmap=False) as hdus:
        data = np.ascontiguousarray(hdus[1].data, dtype=np.float32)
    if data.shape != (tori.SRC_N, tori.SRC_N):
        raise AssertionError(f"unexpected fixture brick shape for {brick_record['brick_id']}")
    observed = hashlib.sha256(data.tobytes(order="C")).hexdigest()
    if observed != brick_record["data_sha256"]:
        raise AssertionError(
            f"fixture brick data custody mismatch for {brick_record['brick_id']}"
        )
    tori.write_synthetic_brick(
        source_root, geometry_row,
        data_big_endian=np.ascontiguousarray(data.astype(">f4")).tobytes(),
    )


def _load_expected_array(tree_root: Path, case) -> "np.ndarray":
    expected_path = tree_root / case["expected_array_path"]
    if _sha256_path(expected_path) != case["expected_array_sha256"]:
        raise AssertionError(f"expected-array custody mismatch for {case['object_id']}")
    expected = np.load(expected_path, allow_pickle=False)
    if expected.shape != (128, 128) or expected.dtype != np.dtype("float32"):
        raise AssertionError(f"unexpected expected-array shape/dtype for {case['object_id']}")
    return expected


def _read_cutout_array(out_dir: Path, receipt) -> "np.ndarray":
    payload = (out_dir / receipt["output_path"]).read_bytes()
    _, _, data_offset, _ = tori.parse_fits_header(payload)
    return np.frombuffer(
        payload, dtype=">f4", count=128 * 128, offset=data_offset
    ).reshape(128, 128)


def _run_case(case, item, geometry, source_root, out_dir, *,
              expected_array=None, pixel_tolerance=None, pixel_skip_reason=None):
    expected = sorted(str(name) for name in case["expected_bricks"])
    record = {"object_id": case["object_id"], "expected_bricks": expected}
    try:
        plan = tori.plan_object(item, geometry)
        record["planned_bricknames"] = plan["planned_bricknames"]
        record["adapter_primary_brickname"] = plan["primary_brickname"]
        record["unique_area_primary_bricknames"] = plan["unique_area_primary_bricknames"]
        record["reasons"] = plan["reasons"]
        if plan["planned_bricknames"] != expected:
            raise AssertionError("planned source set differs from Yui expected set")
        summary = tori.run_local_cut(
            [item], geometry, source_root, out_dir, invalid_fraction_cap=0.0
        )
        receipt = json.loads(
            (out_dir / "receipts" / f"{item.object_key}.json").read_text(encoding="utf-8")
        )
        pc3 = receipt.get("pc3", {})
        if summary.get("completed") != 1 or receipt.get("status") != "COMPLETED":
            raise AssertionError(f"cut did not complete: {receipt.get('status')}")
        if pc3.get("planned_sources") != expected or pc3.get("opened_sources") != expected:
            raise AssertionError("PC-3 receipt source sets differ from Yui expected set")
        if pc3.get("coverage_min", 0) < 1 or pc3.get("coverage_zero_count") != 0:
            raise AssertionError("coverage violated")
        record["coverage_min"] = pc3["coverage_min"]
        record["coverage_zero_count"] = pc3["coverage_zero_count"]
        record["contributing_sources"] = pc3["contributing_sources"]
        record["zero_pixel_touch_sources"] = pc3["zero_pixel_touch_sources"]
        record["output_file_sha256"] = receipt["output_file_sha256"]
        # Where the fixture declares contributing/zero-touch expectations
        # (round 3), compare all three set roles — planned, opened, AND
        # contributing — not just the planned set.
        if "expected_contributing_bricks" in case:
            expected_contributing = sorted(
                str(name) for name in case["expected_contributing_bricks"]
            )
            expected_zero_touch = sorted(
                str(name) for name in case["expected_zero_pixel_touch_bricks"]
            )
            record["expected_contributing_bricks"] = expected_contributing
            record["expected_zero_pixel_touch_bricks"] = expected_zero_touch
            if pc3["contributing_sources"] != expected_contributing:
                raise AssertionError(
                    "contributing sources differ from Yui expectation: "
                    f"adapter {pc3['contributing_sources']} vs {expected_contributing}"
                )
            if pc3["zero_pixel_touch_sources"] != expected_zero_touch:
                raise AssertionError(
                    "zero-pixel-touch sources differ from Yui expectation: "
                    f"adapter {pc3['zero_pixel_touch_sources']} vs {expected_zero_touch}"
                )
        # Pixel-value comparison (2026-08-16 resampler gate): adapter output
        # bytes against Yui's expected array, absolute per-pixel, at her
        # declared tolerance for the round.
        if expected_array is not None:
            adapter_array = _read_cutout_array(out_dir, receipt).astype(np.float64)
            max_abs_error = float(
                np.max(np.abs(adapter_array - expected_array.astype(np.float64)))
            )
            record["pixel_compared"] = True
            record["pixel_max_abs_error"] = max_abs_error
            record["pixel_tolerance"] = pixel_tolerance
            if max_abs_error > pixel_tolerance:
                raise AssertionError(
                    f"pixel values differ from Yui expected array: max abs error "
                    f"{max_abs_error} exceeds {pixel_tolerance}"
                )
        else:
            record["pixel_compared"] = False
            record["pixel_skip_reason"] = pixel_skip_reason
        record["status"] = "PASS"
    except Exception as exc:  # noqa: BLE001 - the receipt must record the exact failure
        record["status"] = "FAIL"
        record["error_type"] = type(exc).__name__
        record["error"] = str(exc)
    return record


def _round1_geometry_rows() -> list:
    rows = []
    brickid = 1
    for grid_row in (-1, 0, 1):
        for grid_col in (-1, 0, 1):
            origin_x = grid_col * yui.STRIDE
            origin_y = grid_row * yui.STRIDE
            ra, dec = yui._world_for_global(origin_x, origin_y)
            west_ra, _ = yui._world_for_global(origin_x - yui.UNIQUE_HALF_SIZE, origin_y)
            east_ra, _ = yui._world_for_global(origin_x + yui.UNIQUE_HALF_SIZE, origin_y)
            _, south_dec = yui._world_for_global(origin_x, origin_y - yui.UNIQUE_HALF_SIZE)
            _, north_dec = yui._world_for_global(origin_x, origin_y + yui.UNIQUE_HALF_SIZE)
            rows.append(
                {
                    "brickname": f"r{grid_row:+d}c{grid_col:+d}",
                    "brickid": brickid,
                    "ra": ra,
                    "dec": dec,
                    "ra1": min(west_ra, east_ra),
                    "ra2": max(west_ra, east_ra),
                    "dec1": min(south_dec, north_dec),
                    "dec2": max(south_dec, north_dec),
                }
            )
            brickid += 1
    return rows


def _build_round1_geometry() -> "tori.SyntheticBrickGeometry":
    return tori.SyntheticBrickGeometry(_round1_geometry_rows(), scope=tori.SCOPE)


def _pixel_agreement_summary(cases, tolerance: float, tolerance_source: str) -> dict:
    compared = [case for case in cases if case.get("pixel_compared")]
    skipped = [case for case in cases if case.get("pixel_compared") is False]
    return {
        "cases_compared": len(compared),
        "cases_skipped": len(skipped),
        "max_abs_error_over_compared": (
            max(case["pixel_max_abs_error"] for case in compared) if compared else None
        ),
        "tolerance_absolute": tolerance,
        "tolerance_source": tolerance_source,
        "skip_reasons": sorted({case["pixel_skip_reason"] for case in skipped}),
    }


def _run_round1(tmp: Path) -> dict:
    yui_root = tmp / "yui_round1"
    manifest = yui.generate_fixture_tree(yui_root)
    yui_rows = json.loads((yui_root / "objects.json").read_text(encoding="utf-8"))
    objects_json_sha256 = _sha256_path(yui_root / "objects.json")
    geometry = _build_round1_geometry()
    brick_records = {row["brick_id"]: row for row in manifest["bricks"]}
    source_root = tmp / "round1_staged"
    for row in geometry.rows:
        _stage_brick_with_yui_data(source_root, row, yui_root, brick_records[row["brickname"]])
    cases = []
    for yui_row in yui_rows:
        item = tori.SyntheticCutTarget(
            _object_key(str(yui_row["object_id"])),
            float(yui_row["ra_deg"]),
            float(yui_row["dec_deg"]),
        )
        primary_only = sorted(yui_row["expected_bricks"]) == ["r+0c+0"]
        record = _run_case(
            yui_row, item, geometry, source_root, tmp / "round1_out" / str(yui_row["object_id"]),
            expected_array=_load_expected_array(yui_root, yui_row) if primary_only else None,
            pixel_tolerance=ROUND1_PIXEL_TOLERANCE if primary_only else None,
            pixel_skip_reason=None if primary_only else ROUND1_PIXEL_SKIP_REASON,
        )
        record["case"] = yui_row["case"]
        cases.append(record)
    failed = sum(1 for record in cases if record["status"] != "PASS")
    return {
        "fixture_round": 1,
        "fixture_generator": "make_boundary_fixtures.py",
        "fixture_source": "regenerated in temp directory this run",
        "generated_objects_json_sha256": objects_json_sha256,
        "status": "PASS" if failed == 0 else "FAIL",
        "cases_total": len(cases),
        "cases_passed": len(cases) - failed,
        "cases_failed": failed,
        "pixel_agreement": _pixel_agreement_summary(
            cases, ROUND1_PIXEL_TOLERANCE,
            "Yui round-1 render_fixture_oracle adapter_comparison_absolute_tolerance (5e-6)",
        ),
        "cases": cases,
    }


def _build_round2_geometry(sidecar: dict) -> "tori.SyntheticBrickGeometry":
    rows = []
    for index, brick in enumerate(sidecar["bricks"]):
        rows.append(
            {
                "brickname": brick["brick_id"],
                "brickid": index + 1,
                "ra": brick["wcs"]["CRVAL1"],
                "dec": brick["wcs"]["CRVAL2"],
                "ra1": brick["unique_ra_bounds_deg"][0] % 360.0,
                "ra2": brick["unique_ra_bounds_deg"][1] % 360.0,
                "dec1": brick["unique_dec_bounds_deg"][0],
                "dec2": brick["unique_dec_bounds_deg"][1],
            }
        )
    return tori.SyntheticBrickGeometry(rows, scope=tori.SCOPE)


def _run_pinned_tree(tmp: Path, *, round_number: int, generated_root: Path, generator_name: str) -> dict:
    manifest = json.loads((generated_root / "fixture_manifest.json").read_text(encoding="utf-8"))
    objects_path = generated_root / manifest["objects_path"]
    sidecar_path = generated_root / manifest["geometry_sidecar_path"]
    integrity = {
        "objects_sha256_verified": _sha256_path(objects_path) == manifest["objects_sha256"],
        "geometry_sidecar_sha256_verified": _sha256_path(sidecar_path)
        == manifest["geometry_sidecar_sha256"],
    }
    if not all(integrity.values()):
        return {
            "fixture_round": round_number,
            "fixture_generator": generator_name,
            "status": "FAIL",
            "error": f"pinned round-{round_number} tree failed its own manifest hash check",
            "integrity": integrity,
            "cases_total": 0,
            "cases_passed": 0,
            "cases_failed": 0,
            "cases": [],
        }
    yui_rows = json.loads(objects_path.read_text(encoding="utf-8"))
    sidecar = json.loads(sidecar_path.read_text(encoding="utf-8"))
    geometry = _build_round2_geometry(sidecar)
    brick_records = {row["brick_id"]: row for row in sidecar["bricks"]}
    source_root = tmp / f"round{round_number}_staged"
    for row in geometry.rows:
        _stage_brick_with_yui_data(
            source_root, row, generated_root, brick_records[row["brickname"]]
        )
    cases = []
    for yui_row in yui_rows:
        item = tori.SyntheticCutTarget(
            _object_key(str(yui_row["object_id"])),
            float(yui_row["ra_deg"]),
            float(yui_row["dec_deg"]),
        )
        record = _run_case(
            yui_row, item, geometry, source_root,
            tmp / f"round{round_number}_out" / str(yui_row["object_id"]),
            expected_array=_load_expected_array(generated_root, yui_row),
            pixel_tolerance=ROUND23_PIXEL_TOLERANCE,
        )
        record["group_id"] = yui_row["group_id"]
        record["yui_primary_brick_not_compared"] = yui_row["primary_brick"]
        record["geometry_evidence"] = yui_row.get("geometry_evidence")
        cases.append(record)
    failed = sum(1 for record in cases if record["status"] != "PASS")
    return {
        "pixel_agreement": _pixel_agreement_summary(
            cases, ROUND23_PIXEL_TOLERANCE,
            "Yui rounds-2/3 VALUE_TOLERANCE / adapter_comparison_absolute_tolerance (1e-5), "
            "declared in make_boundary_fixtures_round2.py before this gate",
        ),
        "fixture_round": round_number,
        "fixture_generator": generator_name,
        "fixture_source": (
            f"pinned pre-generated tree {generated_root.relative_to(PREREG).as_posix()} (read-only)"
        ),
        "fixture_manifest_schema": manifest["schema_version"],
        "objects_sha256": manifest["objects_sha256"],
        "geometry_sidecar_sha256": manifest["geometry_sidecar_sha256"],
        "integrity": integrity,
        "status": "PASS" if failed == 0 else "FAIL",
        "cases_total": len(cases),
        "cases_passed": len(cases) - failed,
        "cases_failed": failed,
        "cases": cases,
    }


def _run_round2(tmp: Path) -> dict:
    return _run_pinned_tree(
        tmp, round_number=2, generated_root=ROUND2_GENERATED,
        generator_name="make_boundary_fixtures_round2.py",
    )


def _run_round3(tmp: Path) -> dict:
    return _run_pinned_tree(
        tmp, round_number=3, generated_root=ROUND3_GENERATED,
        generator_name="make_boundary_fixtures_round3.py",
    )


def _run_round4(tmp: Path) -> dict:
    """Round 4: production-shaped .fits.fz through the pinned read stage.

    Each case runs TWICE — once from sources staged by nm_brick_read_stage
    (decompressed from Yui's RICE_1 fixtures) and once from direct
    uncompressed staging of the same arrays — and the two adapter outputs
    must be byte-identical: tile compression is lossless here, so a value
    difference anywhere in the read path is a defect, not a tolerance
    question. Expected-array pixel comparison uses the parent round's
    tolerance semantics (round-1 parents: 5e-6, centre-brick-only; round-3
    parent: 1e-5).
    """
    manifest = json.loads((ROUND4_GENERATED / "fixture_manifest.json").read_text(encoding="utf-8"))
    objects_path = ROUND4_GENERATED / manifest["objects_path"]
    integrity = {
        "objects_sha256_verified": _sha256_path(objects_path) == manifest["objects_sha256"],
    }
    if not all(integrity.values()):
        return {
            "fixture_round": 4, "fixture_generator": "make_boundary_fixtures_round4.py",
            "status": "FAIL", "error": "pinned round-4 tree failed its own manifest hash check",
            "integrity": integrity, "cases_total": 0, "cases_passed": 0, "cases_failed": 0,
            "cases": [],
        }
    yui_rows = json.loads(objects_path.read_text(encoding="utf-8"))
    brick_records = {row["brick_id"]: row for row in manifest["bricks"]}

    geometry_rows = _round1_geometry_rows()
    west = brick_records["knife-dec-max-west"]
    geometry_rows.append(
        {
            "brickname": west["brick_id"],
            "brickid": len(geometry_rows) + 1,
            "ra": west["wcs"]["CRVAL1"],
            "dec": west["wcs"]["CRVAL2"],
            "ra1": west["unique_ra_bounds_deg"][0] % 360.0,
            "ra2": west["unique_ra_bounds_deg"][1] % 360.0,
            "dec1": west["unique_dec_bounds_deg"][0],
            "dec2": west["unique_dec_bounds_deg"][1],
        }
    )
    geometry = tori.SyntheticBrickGeometry(geometry_rows, scope=tori.SCOPE)
    rows_by_name = {row["brickname"]: row for row in geometry.rows}

    root_read = tmp / "round4_staged_readstage"
    root_direct = tmp / "round4_staged_direct"
    read_receipts = []
    decompressed_hashes_match = True
    for brick_id, record in sorted(brick_records.items()):
        row = rows_by_name[brick_id]
        if record["source_round"] == "round1":
            # Yui's round-1 bricks declare her shared-tangent WCS; verify the
            # header against those declared cards. The staging row remains the
            # adapter's per-brick model (same documented approximation as the
            # round-1 cross-check block).
            expected_wcs = {
                "CTYPE1": "RA---TAN", "CTYPE2": "DEC--TAN",
                "CRVAL1": 180.0, "CRVAL2": -30.0,
                "CRPIX1": 1800.5 - record["origin_x"],
                "CRPIX2": 1800.5 - record["origin_y"],
                "CD1_1": tori.OUT_CD[0][0], "CD1_2": tori.OUT_CD[0][1],
                "CD2_1": tori.OUT_CD[1][0], "CD2_2": tori.OUT_CD[1][1],
            }
        else:
            expected_wcs = None
        receipt = readstage.read_production_brick(
            ROUND4_GENERATED / record["relative_path"], row, root_read,
            expected_file_sha256=record["file_sha256"],
            expected_wcs_cards=expected_wcs,
        )
        if receipt["decompressed_array_sha256"] != record["data_sha256"]:
            decompressed_hashes_match = False
        # Embed without the read receipt's own run timestamp: its identity is
        # its content_sha256 (which already excludes recorded_utc), and the
        # cross-check receipt must stay byte-stable modulo its own timestamp.
        read_receipts.append(
            {key: value for key, value in receipt.items() if key != "recorded_utc"}
        )
        _stage_brick_with_yui_data(root_direct, row, ROUND4_GENERATED, record)

    cases = []
    for yui_row in yui_rows:
        item = tori.SyntheticCutTarget(
            _object_key(str(yui_row["object_id"])),
            float(yui_row["ra_deg"]),
            float(yui_row["dec_deg"]),
        )
        if yui_row["source_round"] == "round3":
            expected_array = _load_expected_array(ROUND4_GENERATED, yui_row)
            tolerance = ROUND23_PIXEL_TOLERANCE
            skip_reason = None
        elif sorted(yui_row["expected_bricks"]) == ["r+0c+0"]:
            expected_array = _load_expected_array(ROUND4_GENERATED, yui_row)
            tolerance = ROUND1_PIXEL_TOLERANCE
            skip_reason = None
        else:
            expected_array = None
            tolerance = None
            skip_reason = ROUND1_PIXEL_SKIP_REASON
        record = _run_case(
            yui_row, item, geometry, root_read,
            tmp / "round4_out_readstage" / str(yui_row["object_id"]),
            expected_array=expected_array, pixel_tolerance=tolerance,
            pixel_skip_reason=skip_reason,
        )
        record["source_round"] = yui_row["source_round"]
        direct = _run_case(
            yui_row, item, geometry, root_direct,
            tmp / "round4_out_direct" / str(yui_row["object_id"]),
            expected_array=expected_array, pixel_tolerance=tolerance,
            pixel_skip_reason=skip_reason,
        )
        record["read_path_output_sha256"] = record.get("output_file_sha256")
        record["uncompressed_path_output_sha256"] = direct.get("output_file_sha256")
        if direct["status"] != "PASS" and record["status"] == "PASS":
            record["status"] = "FAIL"
            record["error"] = f"uncompressed reference path failed: {direct.get('error')}"
        elif record["status"] == "PASS":
            byte_identical = (
                record["read_path_output_sha256"] is not None
                and record["read_path_output_sha256"] == record["uncompressed_path_output_sha256"]
            )
            record["byte_identical_to_uncompressed_path"] = byte_identical
            if not byte_identical:
                record["status"] = "FAIL"
                record["error"] = (
                    "adapter output from the read stage is not byte-identical to the "
                    "uncompressed staging path — a read-path value defect, not a tolerance question"
                )
        cases.append(record)

    failed = sum(1 for record in cases if record["status"] != "PASS")
    if not decompressed_hashes_match:
        failed = max(failed, 1)
    compared = [case for case in cases if case.get("pixel_compared")]
    skipped = [case for case in cases if case.get("pixel_compared") is False]
    return {
        "fixture_round": 4,
        "fixture_generator": "make_boundary_fixtures_round4.py",
        "fixture_source": "pinned pre-generated tree boundary_fixtures/generated_round4 (read-only)",
        "fixture_manifest_schema": manifest["schema_version"],
        "objects_sha256": manifest["objects_sha256"],
        "integrity": integrity,
        "status": "PASS" if failed == 0 and decompressed_hashes_match else "FAIL",
        "cases_total": len(cases),
        "cases_passed": len(cases) - sum(1 for c in cases if c["status"] != "PASS"),
        "cases_failed": sum(1 for c in cases if c["status"] != "PASS"),
        "read_stage": {
            "module_sha256": _sha256_path(READ_STAGE_PATH),
            "all_decompressed_hashes_match_parent_data": decompressed_hashes_match,
            "receipts": read_receipts,
        },
        "byte_identity": {
            "all_cases_byte_identical": all(
                case.get("byte_identical_to_uncompressed_path") for case in cases
            ),
            "comparison": "adapter output bytes, read-stage path vs uncompressed staging path, exact",
        },
        "pixel_agreement": {
            "cases_compared": len(compared),
            "cases_skipped": len(skipped),
            "max_abs_error_over_compared": (
                max(case["pixel_max_abs_error"] for case in compared) if compared else None
            ),
            "tolerance_absolute": None,
            "tolerance_source": (
                "parent-round tolerances per case: round-1 parents 5e-6 (centre-brick-only), "
                "round-3 parent 1e-5; byte-identity between compressed and uncompressed paths "
                "is asserted EXACTLY for every case"
            ),
            "skip_reasons": sorted({case["pixel_skip_reason"] for case in skipped}),
        },
        "cases": cases,
    }


def run_cross_check() -> dict:
    tmp = Path(tempfile.mkdtemp(prefix="_tmp_cross_check_yui_", dir=HERE))
    try:
        round1 = _run_round1(tmp)
        round2 = _run_round2(tmp)
        round3 = _run_round3(tmp)
        round4 = _run_round4(tmp)
        receipt = {
            "recorded_utc": datetime.now(timezone.utc)
            .isoformat(timespec="seconds")
            .replace("+00:00", "Z"),
            "scope": SCOPE_STATEMENT,
            "status": (
                "PASS"
                if all(block["status"] == "PASS" for block in (round1, round2, round3, round4))
                else "FAIL"
            ),
            "round1": round1,
            "round2": round2,
            "round3": round3,
            "round4": round4,
            "artifacts": {
                "nm_brick_cutout_adapter.py_sha256": _sha256_path(HERE / "nm_brick_cutout_adapter.py"),
                "nm_brick_read_stage.py_sha256": _sha256_path(READ_STAGE_PATH),
                "yui_make_boundary_fixtures.py_sha256": _sha256_path(
                    PREREG / "boundary_fixtures" / "make_boundary_fixtures.py"
                ),
                "yui_make_boundary_fixtures_round2.py_sha256": _sha256_path(ROUND2_GENERATOR),
                "yui_make_boundary_fixtures_round3.py_sha256": _sha256_path(ROUND3_GENERATOR),
                "yui_make_boundary_fixtures_round4.py_sha256": _sha256_path(ROUND4_GENERATOR),
                "kun_scratch_runner_sha256": (
                    _sha256_path(KUN_SCRATCH_RUNNER) if KUN_SCRATCH_RUNNER.is_file() else None
                ),
            },
            "comparison_contract": {
                "source_sets": "adapter plan and PC-3 planned/opened sets must equal Yui expected_bricks",
                "coverage": "coverage_min >= 1 and coverage_zero_count == 0 on completed cuts",
                "pixel_values": (
                    "compared per round against Yui's expected arrays on her hash-verified brick "
                    "data at her pre-declared absolute tolerances (round-1 5e-6 centre-brick-only; "
                    "rounds 2-3 1e-5 all cases); see scope for what remains excluded and why"
                ),
                "counts": "round-1, round-2, round-3, and round-4 are reported separately and never merged",
                "contributing_sets": (
                    "where the fixture declares expected_contributing_bricks / "
                    "expected_zero_pixel_touch_bricks (round 3), adapter PC-3 contributing and "
                    "zero-pixel-touch sets must equal them; planned-but-not-contributing is a "
                    "legitimate state, never an error"
                ),
            },
        }
        # Stable content identity a gate can pin: hash the receipt's own content
        # canonically with ONLY the run timestamp and the hash field itself
        # excluded. The exclusion list is declared inside the artifact (and is
        # itself part of the hashed content). Two runs with no code or fixture
        # change must produce an identical content_sha256.
        receipt["content_hash_excludes"] = ["content_sha256", "recorded_utc"]
        hash_body = {
            key: value
            for key, value in receipt.items()
            if key not in ("content_sha256", "recorded_utc")
        }
        receipt["content_sha256"] = hashlib.sha256(
            json.dumps(hash_body, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        RECEIPT_PATH.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return receipt
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> int:
    receipt = run_cross_check()
    print(
        json.dumps(
            {
                "status": receipt["status"],
                "content_sha256": receipt["content_sha256"],
                "recorded_utc": receipt["recorded_utc"],
                "round1": {
                    key: receipt["round1"][key]
                    for key in ("status", "cases_total", "cases_passed", "cases_failed")
                },
                "round2": {
                    key: receipt["round2"][key]
                    for key in ("status", "cases_total", "cases_passed", "cases_failed")
                },
                "round3": {
                    key: receipt["round3"][key]
                    for key in ("status", "cases_total", "cases_passed", "cases_failed")
                },
                "round4": {
                    key: receipt["round4"][key]
                    for key in ("status", "cases_total", "cases_passed", "cases_failed")
                },
                "round4_byte_identity": receipt["round4"]["byte_identity"],
                "pixel_agreement": {
                    name: receipt[name]["pixel_agreement"]
                    for name in ("round1", "round2", "round3", "round4")
                    if "pixel_agreement" in receipt[name]
                },
            },
            sort_keys=True,
        )
    )
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
