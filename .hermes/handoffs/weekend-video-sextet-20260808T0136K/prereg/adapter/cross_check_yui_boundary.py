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

Yui's artifacts are imported/loaded read-only and never modified. The round-1
geometry mapping mirrors Kun's scratch cross-runner
(`prereg/_tmp_kun_cross_adapter_fixtures_20260816.py`). Pixel-value equality
is intentionally NOT required in either round: Yui's oracles use Astropy WCS
with bilinear sampling while the adapter declares a nearest-neighbour renderer
stand-in; a value mismatch would not isolate the boundary rule.

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

import make_boundary_fixtures as yui  # noqa: E402  (Yui's round-1 oracle, read-only)
import nm_brick_cutout_adapter as tori  # noqa: E402

RECEIPT_PATH = HERE / "CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json"
KUN_SCRATCH_RUNNER = PREREG / "_tmp_kun_cross_adapter_fixtures_20260816.py"
ROUND2_GENERATOR = PREREG / "boundary_fixtures" / "make_boundary_fixtures_round2.py"
ROUND2_GENERATED = PREREG / "boundary_fixtures" / "generated_round2"
ROUND3_GENERATOR = PREREG / "boundary_fixtures" / "make_boundary_fixtures_round3.py"
ROUND3_GENERATED = PREREG / "boundary_fixtures" / "generated_round3"

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
    ],
    "not_covered": [
        "pixel-value equality against Yui's bilinear Astropy oracles — the adapter renderer "
        "is a declared nearest-neighbour stand-in pending the hash-pinned Imagine/"
        "astrometry.net resampler and environment lock",
        "production contribution semantics: the adapter's contribution window (output pixel "
        "centre within the source's interior pixel-centre window [1, N], matching the "
        "fixture oracle's bilinear-support rule) stands in for whatever support window the "
        "hash-pinned resampler actually has — re-proven at the resampler gate",
        "Yui's 'primary_brick' (west-side convention) is recorded but not compared: the "
        "adapter primary is grouping metadata under the nearest-planned-centre rule and "
        "never a selection rule",
        "real DR10 South geometry-sidecar bricks, production .fits.fz HDU-1 reads, "
        "multi-process scheduling determinism, dependency/container lock — later gates",
    ],
}


def _sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _object_key(object_id: str) -> str:
    allowed = [char if char.isalnum() else "-" for char in object_id.upper()]
    return "SYNTH-" + "".join(allowed)[:57]


def _run_case(case, item, geometry, source_root, out_dir):
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
        record["status"] = "PASS"
    except Exception as exc:  # noqa: BLE001 - the receipt must record the exact failure
        record["status"] = "FAIL"
        record["error_type"] = type(exc).__name__
        record["error"] = str(exc)
    return record


def _build_round1_geometry() -> "tori.SyntheticBrickGeometry":
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
    return tori.SyntheticBrickGeometry(rows, scope=tori.SCOPE)


def _run_round1(tmp: Path) -> dict:
    yui_root = tmp / "yui_round1"
    yui.generate_fixture_tree(yui_root)
    yui_rows = json.loads((yui_root / "objects.json").read_text(encoding="utf-8"))
    objects_json_sha256 = _sha256_path(yui_root / "objects.json")
    geometry = _build_round1_geometry()
    source_root = tmp / "round1_staged"
    for row in geometry.rows:
        tori.write_synthetic_brick(source_root, row, value=1.0 + row["brickid"] / 10.0)
    cases = []
    for yui_row in yui_rows:
        item = tori.SyntheticCutTarget(
            _object_key(str(yui_row["object_id"])),
            float(yui_row["ra_deg"]),
            float(yui_row["dec_deg"]),
        )
        record = _run_case(
            yui_row, item, geometry, source_root, tmp / "round1_out" / str(yui_row["object_id"])
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
    source_root = tmp / f"round{round_number}_staged"
    for row in geometry.rows:
        tori.write_synthetic_brick(source_root, row, value=1.0 + row["brickid"] / 10.0)
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
        )
        record["group_id"] = yui_row["group_id"]
        record["yui_primary_brick_not_compared"] = yui_row["primary_brick"]
        record["geometry_evidence"] = yui_row.get("geometry_evidence")
        cases.append(record)
    failed = sum(1 for record in cases if record["status"] != "PASS")
    return {
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


def run_cross_check() -> dict:
    tmp = Path(tempfile.mkdtemp(prefix="_tmp_cross_check_yui_", dir=HERE))
    try:
        round1 = _run_round1(tmp)
        round2 = _run_round2(tmp)
        round3 = _run_round3(tmp)
        receipt = {
            "recorded_utc": datetime.now(timezone.utc)
            .isoformat(timespec="seconds")
            .replace("+00:00", "Z"),
            "scope": SCOPE_STATEMENT,
            "status": (
                "PASS"
                if all(block["status"] == "PASS" for block in (round1, round2, round3))
                else "FAIL"
            ),
            "round1": round1,
            "round2": round2,
            "round3": round3,
            "artifacts": {
                "nm_brick_cutout_adapter.py_sha256": _sha256_path(HERE / "nm_brick_cutout_adapter.py"),
                "yui_make_boundary_fixtures.py_sha256": _sha256_path(
                    PREREG / "boundary_fixtures" / "make_boundary_fixtures.py"
                ),
                "yui_make_boundary_fixtures_round2.py_sha256": _sha256_path(ROUND2_GENERATOR),
                "yui_make_boundary_fixtures_round3.py_sha256": _sha256_path(ROUND3_GENERATOR),
                "kun_scratch_runner_sha256": (
                    _sha256_path(KUN_SCRATCH_RUNNER) if KUN_SCRATCH_RUNNER.is_file() else None
                ),
            },
            "comparison_contract": {
                "source_sets": "adapter plan and PC-3 planned/opened sets must equal Yui expected_bricks",
                "coverage": "coverage_min >= 1 and coverage_zero_count == 0 on completed cuts",
                "pixel_values": (
                    "excluded: Yui oracles are Astropy bilinear, adapter renderer is a declared "
                    "nearest-neighbour stand-in pending the pinned resampler"
                ),
                "counts": "round-1, round-2, and round-3 are reported separately and never merged",
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
            },
            sort_keys=True,
        )
    )
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
