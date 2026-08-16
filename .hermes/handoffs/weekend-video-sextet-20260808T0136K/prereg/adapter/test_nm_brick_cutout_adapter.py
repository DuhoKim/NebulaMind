#!/usr/bin/env python3
"""Offline tests for nm_brick_cutout_adapter.py; synthetic fixtures only.

Every FITS byte, brick geometry row, and object position in this file is
synthetic. No network access, no Globus, no real survey product.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE / "nm_brick_cutout_adapter.py"
PREREG = HERE.parent

ALLOWED_IMPORTS = {
    "__future__", "argparse", "hashlib", "importlib", "importlib.util", "json",
    "math", "re", "struct", "sys", "datetime", "pathlib", "typing",
}
FORBIDDEN_IMPORT_FRAGMENTS = (
    "socket", "ssl", "http", "urllib", "requests", "httpx", "aiohttp",
    "ftplib", "telnetlib", "smtplib", "poplib", "imaplib", "globus",
    "subprocess", "asyncio", "ctypes", "os",
)


def load_module():
    if not MODULE_PATH.is_file():
        raise AssertionError("RED: nm_brick_cutout_adapter.py is missing")
    spec = importlib.util.spec_from_file_location("nm_brick_cutout_adapter", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise AssertionError("RED: cannot load nm_brick_cutout_adapter.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MOD = load_module()

CORNER_CENTRES = [(0.0, 0.0), (0.25, 0.0), (0.0, 0.25), (0.25, 0.25)]
BRICK_VALUES = {"0000p000": 1.0, "0002p000": 2.0, "0000p002": 3.0, "0002p002": 4.0}


class AdapterTestBase(unittest.TestCase):
    tmp_root: Path

    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp_root = Path(tempfile.mkdtemp(prefix="_tmp_selftest_", dir=HERE))
        cls.geometry = MOD.make_grid_geometry(CORNER_CENTRES)
        cls.source_root = cls.tmp_root / "staged"
        for row in cls.geometry.rows:
            MOD.write_synthetic_brick(
                cls.source_root, row, value=BRICK_VALUES[row["brickname"]]
            )

    @classmethod
    def tearDownClass(cls) -> None:
        shutil.rmtree(cls.tmp_root, ignore_errors=True)

    def out_dir(self, name: str) -> Path:
        path = self.tmp_root / name
        path.mkdir(parents=True, exist_ok=True)
        return path


class TestStaticGuarantees(AdapterTestBase):
    def test_authority_hashes_match_disk(self) -> None:
        route = PREREG / "TORI_ROUTE_BINDING_20260815.md"
        frozen = PREREG / "PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md"
        self.assertEqual(
            hashlib.sha256(route.read_bytes()).hexdigest(), MOD.ROUTE_BINDING_SHA256
        )
        self.assertEqual(
            hashlib.sha256(frozen.read_bytes()).hexdigest(), MOD.FROZEN_PREREG_SHA256
        )
        self.assertEqual(frozen.stat().st_mode & 0o777, 0o444)

    def test_static_source_has_no_transport(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        imported: set = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                self.assertEqual(node.level, 0, "no relative imports")
                imported.add(node.module or "")
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(
                    node.func.id, {"eval", "exec", "__import__", "compile"},
                    "dynamic execution primitives are forbidden",
                )
        self.assertTrue(imported <= ALLOWED_IMPORTS, f"unexpected imports: {imported - ALLOWED_IMPORTS}")
        for name in imported:
            for fragment in FORBIDDEN_IMPORT_FRAGMENTS:
                self.assertNotIn(fragment, name)

    def test_module_has_no_fetch_or_submit_capability(self) -> None:
        self.assertIs(MOD.BUILD_ONLY, True)
        self.assertEqual(MOD.SCOPE, "SYNTHETIC_ONLY_BUILD")
        for name in dir(MOD):
            lowered = name.lower()
            for banned in ("fetch", "download", "upload", "activate_endpoint"):
                self.assertNotIn(banned, lowered)
            self.assertNotRegex(lowered, r"^submit")
            attribute = getattr(MOD, name)
            if isinstance(attribute, type):
                for method in dir(attribute):
                    self.assertNotIn("fetch", method.lower())
                    self.assertNotIn("submit", method.lower())

    def test_pinned_validator_hashes(self) -> None:
        for path, expected in (
            (MOD.PARITY_VALIDATOR_PATH, MOD.PARITY_VALIDATOR_SHA256),
            (MOD.DISTORTION_VALIDATOR_PATH, MOD.DISTORTION_VALIDATOR_SHA256),
        ):
            self.assertEqual(hashlib.sha256(Path(path).read_bytes()).hexdigest(), expected)
        tampered = self.tmp_root / "_tmp_tampered_validator.py"
        tampered.write_bytes(Path(MOD.PARITY_VALIDATOR_PATH).read_bytes() + b"\n# tampered\n")
        with self.assertRaisesRegex(RuntimeError, "hash-pinned dependency changed"):
            MOD._load_hash_pinned_module(tampered, MOD.PARITY_VALIDATOR_SHA256, "nm_test_tamper")

    def test_output_wcs_exact_constants(self) -> None:
        self.assertEqual(repr(MOD.OUT_CD[0][0]), "-7.277777777777778e-05")
        self.assertEqual(repr(MOD.OUT_CD[1][1]), "7.277777777777778e-05")
        self.assertEqual(MOD.OUT_CD[0][1], 0.0)
        self.assertEqual(MOD.OUT_CD[1][0], 0.0)
        # Bound to the product of the frozen CD terms; the route binding's
        # human-readable determinant literal differs in the 16th digit.
        self.assertEqual(repr(MOD.OUT_CD_DET), "-5.2966049382716055e-09")
        self.assertLess(MOD.OUT_CD_DET, 0.0)
        self.assertEqual((128 / 2) * 0.262, 16.768)


class TestPc4Gate(AdapterTestBase):
    def clean_cards(self) -> dict:
        return {
            "SIMPLE": True, "BITPIX": -32, "NAXIS": 2, "NAXIS1": MOD.SRC_N, "NAXIS2": MOD.SRC_N,
            "CTYPE1": "RA---TAN", "CTYPE2": "DEC--TAN",
            "CRVAL1": 0.0, "CRVAL2": 0.0, "CRPIX1": MOD.SRC_CRPIX, "CRPIX2": MOD.SRC_CRPIX,
            "CD1_1": MOD.OUT_CD[0][0], "CD1_2": 0.0, "CD2_1": 0.0, "CD2_2": MOD.OUT_CD[1][1],
        }

    def gate(self, cards: dict, ordered=None):
        return MOD.fail_closed_header_gate(cards, ordered or list(cards), context="test")

    def expect_code(self, cards: dict, code: str, ordered=None) -> None:
        with self.assertRaises(MOD.WcsRejectedError) as ctx:
            self.gate(cards, ordered)
        self.assertEqual(ctx.exception.code, code)

    def test_clean_canonical_tan_passes(self) -> None:
        receipt = self.gate(self.clean_cards())
        self.assertTrue(receipt["east_left"] and receipt["north_up"])
        self.assertLess(receipt["combined_pixel_to_sky_determinant"], 0.0)
        self.assertEqual(receipt["pinned_distortion_audit"]["status"], "PASS")

    def test_rejection_matrix(self) -> None:
        base = self.clean_cards()
        cases = [
            ({**base, "A_ORDER": 2, "A_1_1": 1e-9}, "REJECTED_DISTORTION"),
            ({**base, "CTYPE1": "RA---TAN-SIP", "CTYPE2": "DEC--TAN-SIP"}, "REJECTED_NON_TAN"),
            ({**base, "PV1_1": 0.0}, "REJECTED_DISTORTION"),
            ({**base, "CTYPE1": "RA---TPV", "CTYPE2": "DEC--TPV"}, "REJECTED_NON_TAN"),
            ({**base, "CPDIS1": "LOOKUP"}, "REJECTED_DISTORTION"),
            ({**base, "D2IMDIS1": "LOOKUP"}, "REJECTED_DISTORTION"),
            ({**base, "DP1": "AXIS.1"}, "REJECTED_LOOKUP_DISTORTION"),
            ({key: value for key, value in base.items() if key != "CD2_2"}, "REJECTED_LINEAR_WCS"),
            ({**{key: value for key, value in base.items() if not key.startswith("CD")},
              "PC1_1": -1.0, "PC1_2": 0.0, "PC2_1": 0.0, "CDELT1": MOD.PIX_SCALE_DEG,
              "CDELT2": MOD.PIX_SCALE_DEG}, "REJECTED_LINEAR_WCS"),
            ({**base, "PC1_1": -1.0, "PC1_2": 0.0, "PC2_1": 0.0, "PC2_2": 1.0,
              "CDELT1": MOD.PIX_SCALE_DEG, "CDELT2": MOD.PIX_SCALE_DEG}, "REJECTED_AMBIGUOUS_WCS"),
            ({**base, "CD1_1": 0.0, "CD2_2": 0.0}, "REJECTED_SINGULAR_WCS"),
            ({**base, "CD1_1": float("nan")}, "REJECTED_SINGULAR_WCS"),
            ({**base, "CD1_1": float("inf")}, "REJECTED_SINGULAR_WCS"),
            ({key: value for key, value in base.items() if key != "CRPIX1"}, "REJECTED_INCOMPLETE_WCS"),
            ({key: value for key, value in base.items() if key != "CRVAL2"}, "REJECTED_INCOMPLETE_WCS"),
            ({key: value for key, value in base.items() if key != "CTYPE1"}, "REJECTED_NON_CELESTIAL"),
            ({**base, "CTYPE1": "GLON-TAN", "CTYPE2": "GLAT-TAN"}, "REJECTED_NON_CELESTIAL"),
            ({**base, "CTYPE1": "DEC--TAN", "CTYPE2": "RA---TAN"}, "REJECTED_SWAPPED_AXES"),
            ({**base, "CTYPE1A": "RA---TAN"}, "REJECTED_ALTERNATE_WCS"),
            ({**base, "CD1_1": -MOD.OUT_CD[1][1] * -1.0}, "REJECTED_PARITY"),
        ]
        for cards, code in cases:
            with self.subTest(code=code, keys=sorted(set(cards) - set(base))):
                self.expect_code(cards, code)

    def test_duplicate_keyword_rejected(self) -> None:
        cards = self.clean_cards()
        self.expect_code(cards, "REJECTED_DUPLICATE_KEY", ordered=list(cards) + ["CRVAL1"])


class TestPlanning(AdapterTestBase):
    def test_corner_object_requests_three_extra_bricks(self) -> None:
        item = MOD.SyntheticCutTarget("SYNTH-CORNER", 0.1249, 0.1249)
        plan = MOD.plan_object(item, self.geometry)
        self.assertEqual(plan["primary_brickname"], "0000p000")
        self.assertEqual(
            plan["planned_bricknames"], ["0000p000", "0000p002", "0002p000", "0002p002"]
        )
        self.assertEqual(plan["reasons"]["0000p000"], "primary")
        self.assertEqual(plan["reasons"]["0000p002"], "edge_neighbour")
        self.assertEqual(plan["reasons"]["0002p000"], "edge_neighbour")
        self.assertEqual(plan["reasons"]["0002p002"], "corner_neighbour")
        self.assertTrue(plan["output_crosses_unique_boundary"]["0000p002"])
        self.assertTrue(plan["output_crosses_unique_boundary"]["0002p000"])

    def test_centre_object_uses_single_brick(self) -> None:
        plan = MOD.plan_object(MOD.SyntheticCutTarget("SYNTH-CENTRE", 0.0, 0.0), self.geometry)
        self.assertEqual(plan["planned_bricknames"], ["0000p000"])

    def test_edge_object_uses_two_bricks(self) -> None:
        plan = MOD.plan_object(MOD.SyntheticCutTarget("SYNTH-EDGE", 0.0, 0.1249), self.geometry)
        self.assertEqual(plan["planned_bricknames"], ["0000p000", "0000p002"])
        self.assertEqual(plan["reasons"]["0000p002"], "edge_neighbour")
        self.assertTrue(plan["output_crosses_unique_boundary"]["0000p002"])

    def test_margin_scalar_is_not_the_selection_rule(self) -> None:
        # Exactly at 16.768" from the unique edge: polygon rule still includes
        # the neighbour, because survey images overlap the unique boundary.
        at_margin = MOD.plan_object(
            MOD.SyntheticCutTarget("SYNTH-ATMARGIN", 0.0, 0.125 - 16.768 / 3600.0), self.geometry
        )
        self.assertIn("0000p002", at_margin["planned_bricknames"])
        # 30" from the unique edge: the output does NOT cross the unique
        # boundary, yet the neighbouring image still intersects and contributes.
        overlap = MOD.plan_object(
            MOD.SyntheticCutTarget("SYNTH-OVERLAP", 0.0, 0.125 - 30.0 / 3600.0), self.geometry
        )
        self.assertIn("0000p002", overlap["planned_bricknames"])
        self.assertFalse(overlap["output_crosses_unique_boundary"]["0000p002"])

    def test_exact_and_beyond_corner_objects_plan_without_failure(self) -> None:
        # 2026-08-16 repair: a rectangular unique-area primary is metadata, not
        # a precondition; corner objects must reach the polygon rule.
        one_pixel = 0.262 / 3600.0
        for suffix, ra, dec in (
            ("EXACT", 0.125, 0.125),
            ("BEYOND", 0.125 + one_pixel, 0.125 + one_pixel),
        ):
            with self.subTest(suffix=suffix):
                plan = MOD.plan_object(
                    MOD.SyntheticCutTarget(f"SYNTH-CORNER-{suffix}", ra, dec), self.geometry
                )
                self.assertEqual(
                    plan["planned_bricknames"],
                    ["0000p000", "0000p002", "0002p000", "0002p002"],
                )
                self.assertIn(plan["primary_brickname"], plan["planned_bricknames"])
                self.assertEqual(plan["reasons"][plan["primary_brickname"]], "primary")
        exact = MOD.plan_object(
            MOD.SyntheticCutTarget("SYNTH-CORNER-META", 0.125, 0.125), self.geometry
        )
        # Rectangular containment survives as recorded metadata only.
        self.assertEqual(exact["unique_area_primary_bricknames"], ["0002p002"])
        self.assertIn("never a source-selection precondition", exact["primary_rule"])

    def test_empty_intersection_is_terminal_plan_failure(self) -> None:
        with self.assertRaises(MOD.ObjectTerminalError) as ctx:
            MOD.plan_object(
                MOD.SyntheticCutTarget("SYNTH-NOWHERE", 10.0, 0.0), self.geometry
            )
        self.assertEqual(ctx.exception.code, "FAILED_PLAN_NO_SOURCES")
        out = self.out_dir("nowhere_cut")
        summary = MOD.run_local_cut(
            [MOD.SyntheticCutTarget("SYNTH-NOWHERE", 10.0, 0.0)],
            self.geometry, self.source_root, out, invalid_fraction_cap=0.0,
        )
        self.assertEqual(summary["failed"], 1)
        receipt = json.loads((out / "receipts" / "SYNTH-NOWHERE.json").read_text())
        self.assertEqual(receipt["status"], "FAILED_PLAN_NO_SOURCES")
        self.assertIsNone(receipt["output_path"])

    def test_ra_wrap_plan(self) -> None:
        geometry = MOD.make_grid_geometry([(359.875, 0.0), (0.125, 0.0)])
        plan = MOD.plan_object(MOD.SyntheticCutTarget("SYNTH-WRAP", 0.0002, 0.0), geometry)
        self.assertEqual(plan["primary_brickname"], "0001p000")
        self.assertEqual(plan["planned_bricknames"], ["0001p000", "3599p000"])
        self.assertEqual(plan["reasons"]["3599p000"], "edge_neighbour")


class TestManifest(AdapterTestBase):
    def test_dry_run_manifest_sealed_not_submitted(self) -> None:
        out = self.out_dir("manifest_only")
        summary = MOD.run_local_cut(
            [MOD.SyntheticCutTarget("SYNTH-CORNER", 0.1249, 0.1249)],
            self.geometry, self.source_root, out,
            invalid_fraction_cap=0.0, manifest_only=True,
        )
        self.assertEqual(summary["mode"], "DRY_RUN_MANIFEST_ONLY")
        self.assertEqual(summary["zero_issuance"]["globus_tasks_submitted"], 0)
        manifest = json.loads((out / "transfer_manifest.json").read_text())
        image_records = [r for r in manifest["records"] if r["product"] == "image-r"]
        self.assertEqual(len(image_records), 4)
        self.assertEqual(
            [r["source_path"] for r in image_records],
            sorted(r["source_path"] for r in image_records),
        )
        for record in image_records:
            self.assertEqual(record["release"], "dr10.1-latest-byte-bound")
            self.assertEqual(record["source_collection_uuid"], MOD.SOURCE_COLLECTION_UUID)
            self.assertTrue(record["source_path"].endswith(".fits.fz"))
            self.assertTrue(record["source_path"].startswith("/global/cfs/cdirs/cosmo/"))
            self.assertEqual(len(record["source_sha256"]), 64)
            self.assertIn(record["reason"], {"primary", "edge_neighbour", "corner_neighbour"})
            self.assertEqual(record["required_by_object_keys"], ["SYNTH-CORNER"])
            self.assertTrue(record["synthetic_stand_in"])
        sidecar = [r for r in manifest["records"] if r["product"] == "geometry_sidecar"]
        self.assertEqual(len(sidecar), 1)
        self.assertEqual(sidecar[0]["source_sha256"], self.geometry.sidecar_sha256)
        template = manifest["globus_task_template"]
        self.assertFalse(template["submitted"])
        self.assertFalse(template["submission_capability_exists"])
        self.assertTrue(template["verify_checksum"])
        self.assertEqual(template["sync_level"], "checksum")
        self.assertFalse(template["skip_source_errors"])
        self.assertIn(manifest["manifest_sha256"][:12], template["label"])
        # Any record added after sealing changes the recomputed hash.
        recomputed = hashlib.sha256(
            json.dumps(
                {key: manifest[key] for key in (
                    "scope", "manifest_format_version", "records", "file_count", "total_source_bytes"
                )},
                sort_keys=True, separators=(",", ":"),
            ).encode()
        ).hexdigest()
        self.assertEqual(recomputed, manifest["manifest_sha256"])
        manifest["records"].append(dict(manifest["records"][0], brickname="9999p999"))
        tampered = hashlib.sha256(
            json.dumps(
                {key: manifest[key] for key in (
                    "scope", "manifest_format_version", "records", "file_count", "total_source_bytes"
                )},
                sort_keys=True, separators=(",", ":"),
            ).encode()
        ).hexdigest()
        self.assertNotEqual(tampered, manifest["manifest_sha256"])

    def test_missing_required_file_is_terminal_not_skippable(self) -> None:
        empty_root = self.tmp_root / "empty_staged"
        empty_root.mkdir(exist_ok=True)
        with self.assertRaisesRegex(MOD.ManifestError, "terminal, not skippable"):
            MOD.run_local_cut(
                [MOD.SyntheticCutTarget("SYNTH-CORNER", 0.1249, 0.1249)],
                self.geometry, empty_root, self.out_dir("manifest_missing"),
                invalid_fraction_cap=0.0, manifest_only=True,
            )


class TestLocalCut(AdapterTestBase):
    def test_corner_cut_completes_with_pc3_pc4_receipts(self) -> None:
        out = self.out_dir("corner_cut")
        summary = MOD.run_local_cut(
            [MOD.SyntheticCutTarget("SYNTH-CORNER", 0.1249, 0.1249)],
            self.geometry, self.source_root, out, invalid_fraction_cap=0.0,
        )
        self.assertEqual(summary["completed"], 1)
        self.assertEqual(summary["failed"], 0)
        receipt = json.loads((out / "receipts" / "SYNTH-CORNER.json").read_text())
        self.assertEqual(receipt["status"], "COMPLETED")
        pc3 = receipt["pc3"]
        self.assertTrue(pc3["wcs_constants_exact"])
        self.assertEqual(pc3["cd_determinant_sign"], -1)
        self.assertLessEqual(pc3["round_trip_max_residual_pixels"], 1e-6)
        self.assertLessEqual(pc3["centre_residual_pixels"], 1e-6)
        self.assertLess(pc3["ra_plus_1arcsec_dx"], 0.0)
        self.assertGreater(pc3["dec_plus_1arcsec_dy"], 0.0)
        self.assertGreaterEqual(pc3["coverage_min"], 1)
        self.assertEqual(pc3["coverage_zero_count"], 0)
        self.assertEqual(pc3["planned_sources"], pc3["opened_sources"])
        self.assertEqual(pc3["contributing_sources"], pc3["planned_sources"])
        self.assertEqual(len(receipt["sources"]), 4)
        for source in receipt["sources"].values():
            self.assertEqual(source["gate"]["pinned_distortion_audit"]["status"], "PASS")
        cutout = out / receipt["output_path"]
        self.assertTrue(cutout.is_file())
        self.assertEqual(
            hashlib.sha256(cutout.read_bytes()).hexdigest(), receipt["output_file_sha256"]
        )
        payload = cutout.read_bytes()
        self.assertEqual(len(payload) % 2880, 0)
        self.assertIn(b"'RA---TAN'", payload[:2880])
        self.assertIn(b"'DEC--TAN'", payload[:2880])

    def test_sip_source_rejected_and_skip_is_counted(self) -> None:
        root = self.tmp_root / "sip_staged"
        geometry = MOD.make_grid_geometry([(0.0, 0.0)])
        MOD.write_synthetic_brick(
            root, geometry.rows[0], header_only=True,
            extra_cards=[("A_ORDER", 2), ("A_1_1", 1e-9)],
        )
        out = self.out_dir("sip_cut")
        objects = [MOD.SyntheticCutTarget("SYNTH-SIP", 0.0, 0.0)]
        summary = MOD.run_local_cut(
            objects, geometry, root, out, invalid_fraction_cap=0.0
        )
        self.assertEqual(summary["failed"], 1)
        self.assertEqual(summary["completed"], 0)
        receipt = json.loads((out / "receipts" / "SYNTH-SIP.json").read_text())
        self.assertEqual(receipt["status"], "REJECTED_DISTORTION")
        self.assertIsNone(receipt["output_path"])
        self.assertEqual(list((out / "cutouts").glob("*")), [])
        # Resume over the terminal failure: a skipped object is a logged,
        # counted event, never a silent gap.
        resumed = MOD.run_local_cut(objects, geometry, root, out, invalid_fraction_cap=0.0)
        self.assertEqual(resumed["skipped"], 1)
        log_lines = [json.loads(line) for line in (out / "cut_log.jsonl").read_text().splitlines()]
        self.assertIn("RESUME_TERMINAL_NOT_RECUT", [line["status"] for line in log_lines])

    def test_parity_flipped_source_rejected(self) -> None:
        root = self.tmp_root / "parity_staged"
        geometry = MOD.make_grid_geometry([(0.0, 0.0)])
        MOD.write_synthetic_brick(
            root, geometry.rows[0], header_only=True,
            override_cards={"CD1_1": MOD.OUT_CD[1][1]},
        )
        out = self.out_dir("parity_cut")
        summary = MOD.run_local_cut(
            [MOD.SyntheticCutTarget("SYNTH-PARITYFLIP", 0.0, 0.0)],
            geometry, root, out, invalid_fraction_cap=0.0,
        )
        self.assertEqual(summary["failed"], 1)
        receipt = json.loads((out / "receipts" / "SYNTH-PARITYFLIP.json").read_text())
        self.assertEqual(receipt["status"], "REJECTED_PARITY")

    def test_truncated_source_rejected(self) -> None:
        root = self.tmp_root / "truncated_staged"
        geometry = MOD.make_grid_geometry([(0.0, 0.0)])
        MOD.write_synthetic_brick(root, geometry.rows[0], truncate_data=True)
        out = self.out_dir("truncated_cut")
        summary = MOD.run_local_cut(
            [MOD.SyntheticCutTarget("SYNTH-TRUNC", 0.0, 0.0)],
            geometry, root, out, invalid_fraction_cap=0.0,
        )
        self.assertEqual(summary["failed"], 1)
        receipt = json.loads((out / "receipts" / "SYNTH-TRUNC.json").read_text())
        self.assertEqual(receipt["status"], "FAILED_FITS_INTEGRITY")

    def test_source_digest_mismatch_rejected(self) -> None:
        row = self.geometry.row("0000p000")
        with self.assertRaises(MOD.ObjectTerminalError) as ctx:
            MOD.SyntheticBrickSource(
                self.source_root / MOD.staged_relpath_for("0000p000"), row, "0" * 64
            )
        self.assertEqual(ctx.exception.code, "FAILED_SOURCE_DIGEST")
        with self.assertRaises(MOD.ObjectTerminalError) as ctx:
            MOD.SyntheticBrickSource(self.source_root / "nonexistent.fits", row, "0" * 64)
        self.assertEqual(ctx.exception.code, "FAILED_SOURCE_MISSING")

    def test_truncated_cutout_rejected_not_padded(self) -> None:
        # Unique area deliberately wider than the image: the planner can only
        # plan the primary, and the cutout footprint leaves the image. The
        # result must be rejection, never zero-padding.
        geometry = MOD.SyntheticBrickGeometry(
            [{
                "brickname": "0000p000", "brickid": 1, "ra": 0.0, "dec": 0.0,
                "ra1": 359.5, "ra2": 0.5, "dec1": -0.5, "dec2": 0.5,
            }],
            scope="SYNTHETIC_ONLY_BUILD",
        )
        root = self.tmp_root / "zerocov_staged"
        MOD.write_synthetic_brick(root, geometry.rows[0])
        out = self.out_dir("zerocov_cut")
        summary = MOD.run_local_cut(
            [MOD.SyntheticCutTarget("SYNTH-ZEROCOV", 0.0, 0.135)],
            geometry, root, out, invalid_fraction_cap=1.0 - 1e-9,
        )
        self.assertEqual(summary["failed"], 1)
        receipt = json.loads((out / "receipts" / "SYNTH-ZEROCOV.json").read_text())
        self.assertEqual(receipt["status"], "FAILED_ZERO_COVERAGE")
        self.assertEqual(list((out / "cutouts").glob("*")), [])

    def test_invalid_pixel_cap_enforced(self) -> None:
        root = self.tmp_root / "nan_staged"
        geometry = MOD.make_grid_geometry([(0.0, 0.0)])
        MOD.write_synthetic_brick(root, geometry.rows[0], value=float("nan"))
        out = self.out_dir("nan_cut")
        summary = MOD.run_local_cut(
            [MOD.SyntheticCutTarget("SYNTH-NAN", 0.0, 0.0)],
            geometry, root, out, invalid_fraction_cap=0.0,
        )
        self.assertEqual(summary["failed"], 1)
        receipt = json.loads((out / "receipts" / "SYNTH-NAN.json").read_text())
        self.assertEqual(receipt["status"], "FAILED_INVALID_PIXEL_CAP")

    def test_output_header_tamper_rejected_and_quarantined(self) -> None:
        out = self.out_dir("tamper_cut")

        def tamper(object_key: str, header: bytes) -> bytes:
            return header.replace(b"-7.277777777777778e-05", b" 7.277777777777778e-05", 1)

        summary = MOD.run_local_cut(
            [MOD.SyntheticCutTarget("SYNTH-TAMPER", 0.0, 0.0)],
            self.geometry, self.source_root, out,
            invalid_fraction_cap=0.0, tamper_hook=tamper,
        )
        self.assertEqual(summary["failed"], 1)
        receipt = json.loads((out / "receipts" / "SYNTH-TAMPER.json").read_text())
        self.assertEqual(receipt["status"], "REJECTED_PARITY")
        self.assertEqual(list((out / "cutouts").glob("*")), [])
        self.assertEqual(len(list((out / "quarantine").glob("*"))), 1)

    def test_resume_after_interrupt_loses_nothing(self) -> None:
        objects = [
            MOD.SyntheticCutTarget("SYNTH-RES-A", 0.0, 0.0),
            MOD.SyntheticCutTarget("SYNTH-RES-B", 0.25, 0.0),
            MOD.SyntheticCutTarget("SYNTH-RES-C", 0.0, 0.25),
        ]
        out = self.out_dir("resume_cut")

        def interrupt(object_key: str, phase: str) -> None:
            if phase == "after_accept" and object_key == "SYNTH-RES-A":
                raise KeyboardInterrupt("synthetic interrupt after first acceptance")

        with self.assertRaises(KeyboardInterrupt):
            MOD.run_local_cut(
                objects, self.geometry, self.source_root, out,
                invalid_fraction_cap=0.0, interrupt_hook=interrupt,
            )
        state = json.loads((out / "state.json").read_text())
        self.assertEqual(state["objects"]["SYNTH-RES-A"]["status"], "COMPLETED")
        self.assertNotIn("SYNTH-RES-B", state["objects"])

        resumed = MOD.run_local_cut(
            objects, self.geometry, self.source_root, out, invalid_fraction_cap=0.0
        )
        self.assertEqual(resumed["resumed_complete"], 1)
        self.assertEqual(resumed["completed"], 2)
        self.assertEqual(resumed["failed"], 0)

        clean_out = self.out_dir("resume_clean")
        MOD.run_local_cut(
            objects, self.geometry, self.source_root, clean_out, invalid_fraction_cap=0.0
        )
        for item in objects:
            interrupted = (out / "cutouts" / f"{item.object_key}.fits").read_bytes()
            clean = (clean_out / "cutouts" / f"{item.object_key}.fits").read_bytes()
            self.assertEqual(
                hashlib.sha256(interrupted).hexdigest(), hashlib.sha256(clean).hexdigest()
            )
        log_lines = (out / "cut_log.jsonl").read_text().splitlines()
        self.assertTrue(log_lines)
        self.assertIsNotNone(MOD._validate_existing_log(out / "cut_log.jsonl"))

    def test_reversed_input_order_is_deterministic(self) -> None:
        objects = [
            MOD.SyntheticCutTarget("SYNTH-DET-A", 0.0, 0.0),
            MOD.SyntheticCutTarget("SYNTH-DET-B", 0.25, 0.0),
        ]
        out_forward = self.out_dir("det_forward")
        out_reverse = self.out_dir("det_reverse")
        forward = MOD.run_local_cut(
            objects, self.geometry, self.source_root, out_forward, invalid_fraction_cap=0.0
        )
        reverse = MOD.run_local_cut(
            list(reversed(objects)), self.geometry, self.source_root, out_reverse,
            invalid_fraction_cap=0.0,
        )
        self.assertEqual(forward["manifest_sha256"], reverse["manifest_sha256"])
        for item in objects:
            first = json.loads((out_forward / "receipts" / f"{item.object_key}.json").read_text())
            second = json.loads((out_reverse / "receipts" / f"{item.object_key}.json").read_text())
            self.assertEqual(first["output_file_sha256"], second["output_file_sha256"])


class TestYuiBoundaryCrossCheck(AdapterTestBase):
    def test_cross_check_receipt_passes_all_rounds_separately(self) -> None:
        # Kun repair condition 5 plus the round-2 and round-3 extensions: the
        # cross-check against ALL of Yui's fixture rounds is part of what the
        # adapter must demonstrate, recorded as one receipt with per-round
        # counts that are never merged.
        result = subprocess.run(
            [sys.executable, str(HERE / "cross_check_yui_boundary.py")],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr[-2000:])
        receipt = json.loads((HERE / "CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json").read_text())
        self.assertEqual(receipt["status"], "PASS")
        self.assertNotIn("cases_total", receipt, "per-round counts must never be merged")

        round1 = receipt["round1"]
        self.assertEqual(round1["status"], "PASS")
        self.assertEqual(round1["cases_total"], 29)
        self.assertEqual(round1["cases_passed"], 29)
        by_id = {case["object_id"]: case for case in round1["cases"]}
        for corner in ("north_east", "north_west", "south_east", "south_west"):
            for suffix in ("exact", "beyond"):
                case = by_id[f"corner_{corner}_{suffix}"]
                self.assertEqual(case["status"], "PASS")
                self.assertEqual(len(case["expected_bricks"]), 4)
                self.assertEqual(case["planned_bricknames"], case["expected_bricks"])
                self.assertGreaterEqual(case["coverage_min"], 1)
                self.assertEqual(case["coverage_zero_count"], 0)

        round2 = receipt["round2"]
        self.assertEqual(round2["status"], "PASS")
        self.assertEqual(round2["cases_total"], 4)
        self.assertEqual(round2["cases_passed"], 4)
        self.assertTrue(all(round2["integrity"].values()))
        round2_ids = {case["object_id"] for case in round2["cases"]}
        self.assertEqual(
            round2_ids,
            {
                "ra_wrap_crossing",
                "selected_dec_max_crossing",
                "selected_dec_min_crossing",
                "geometry_overlap_only",
            },
        )
        for case in round2["cases"]:
            self.assertEqual(case["status"], "PASS")
            self.assertEqual(len(case["expected_bricks"]), 2)
            self.assertEqual(case["planned_bricknames"], case["expected_bricks"])
            self.assertGreaterEqual(case["coverage_min"], 1)
            self.assertEqual(case["coverage_zero_count"], 0)

        round3 = receipt["round3"]
        self.assertEqual(round3["status"], "PASS")
        self.assertEqual(round3["cases_total"], 10)
        self.assertEqual(round3["cases_passed"], 10)
        self.assertTrue(all(round3["integrity"].values()))
        round3_by_id = {case["object_id"]: case for case in round3["cases"]}
        self.assertEqual(len(round3_by_id), 10)
        for prefix in ("dec_max", "dec_min"):
            # Planned-but-not-contributing knife edges: at +1 and +0.25 offsets
            # the candidate is planned yet holds no output pixel centre. The
            # planned and contributing sets must legitimately DIFFER, with the
            # candidate in zero-pixel-touch — not dropped, not credited, not an
            # error.
            for suffix in ("one_pixel_beyond", "subpixel_just_outside"):
                case = round3_by_id[f"{prefix}_{suffix}"]
                self.assertEqual(case["status"], "PASS")
                self.assertEqual(len(case["expected_bricks"]), 2)
                self.assertEqual(case["planned_bricknames"], case["expected_bricks"])
                self.assertEqual(len(case["contributing_sources"]), 1)
                self.assertEqual(len(case["zero_pixel_touch_sources"]), 1)
                self.assertNotEqual(case["planned_bricknames"], case["contributing_sources"])
                self.assertEqual(
                    case["contributing_sources"], case["expected_contributing_bricks"]
                )
                self.assertEqual(
                    case["zero_pixel_touch_sources"], case["expected_zero_pixel_touch_bricks"]
                )
                self.assertGreaterEqual(case["coverage_min"], 1)
                self.assertEqual(case["coverage_zero_count"], 0)
            # Exact tangency and sub-pixel-inside cases exclude the candidate.
            for suffix in ("inside", "exact_boundary", "subpixel_just_inside"):
                case = round3_by_id[f"{prefix}_{suffix}"]
                self.assertEqual(case["status"], "PASS")
                self.assertEqual(len(case["planned_bricknames"]), 1)
                self.assertEqual(case["planned_bricknames"], case["contributing_sources"])
                self.assertEqual(case["zero_pixel_touch_sources"], [])

        # Resampler gate: pixel values compared per round against Yui's
        # expected arrays on her hash-verified brick data, at her pre-declared
        # tolerances. Counts stay per-round; the tolerances are Yui's, not
        # ours, so a residual regression cannot be hidden by widening them.
        pixel1 = round1["pixel_agreement"]
        self.assertEqual(pixel1["cases_compared"], 5)
        self.assertEqual(pixel1["cases_skipped"], 24)
        self.assertEqual(pixel1["tolerance_absolute"], 5e-6)
        self.assertLessEqual(pixel1["max_abs_error_over_compared"], 5e-6)
        self.assertEqual(len(pixel1["skip_reasons"]), 1)
        self.assertIn("share ONE tangent plane", pixel1["skip_reasons"][0])
        for block, expected_compared in ((round2, 4), (round3, 10)):
            pixel = block["pixel_agreement"]
            self.assertEqual(pixel["cases_compared"], expected_compared)
            self.assertEqual(pixel["cases_skipped"], 0)
            self.assertEqual(pixel["tolerance_absolute"], 1e-5)
            self.assertLessEqual(pixel["max_abs_error_over_compared"], 1e-5)
        for case in round3["cases"]:
            self.assertTrue(case["pixel_compared"])

        # Round-4: production-shaped .fits.fz through the separate read stage.
        round4 = receipt["round4"]
        self.assertEqual(round4["status"], "PASS")
        self.assertEqual(round4["cases_total"], 3)
        self.assertEqual(round4["cases_passed"], 3)
        self.assertTrue(all(round4["integrity"].values()))
        self.assertTrue(round4["read_stage"]["all_decompressed_hashes_match_parent_data"])
        self.assertEqual(len(round4["read_stage"]["receipts"]), 5)
        for read_receipt in round4["read_stage"]["receipts"]:
            self.assertEqual(read_receipt["raw_compression_cards"]["ZCMPTYPE"], "RICE_1")
            self.assertEqual(read_receipt["raw_compression_cards"]["ZBITPIX"], -32)
            self.assertEqual(
                read_receipt["content_hash_excludes"], ["content_sha256", "recorded_utc"]
            )
        self.assertTrue(round4["byte_identity"]["all_cases_byte_identical"])
        round4_ids = {case["object_id"] for case in round4["cases"]}
        self.assertEqual(
            round4_ids, {"centre", "dec_max_exact_boundary", "corner_north_west_exact"}
        )
        for case in round4["cases"]:
            self.assertEqual(case["status"], "PASS")
            self.assertTrue(case["byte_identical_to_uncompressed_path"])
            self.assertEqual(
                case["read_path_output_sha256"], case["uncompressed_path_output_sha256"]
            )
        pixel4 = round4["pixel_agreement"]
        self.assertEqual(pixel4["cases_compared"], 2)
        self.assertEqual(pixel4["cases_skipped"], 1)
        self.assertLessEqual(pixel4["max_abs_error_over_compared"], 1e-5)

        scope = receipt["scope"]
        self.assertTrue(any(".fits.fz read path" in line for line in scope["covered"]))
        self.assertTrue(any("SYNTHET" in line for line in scope["not_covered"]))
        self.assertTrue(any("RA-wrap" in line for line in scope["covered"]))
        self.assertTrue(any("-89.875" in line for line in scope["covered"]))
        self.assertTrue(any("knife edge" in line for line in scope["covered"]))
        self.assertTrue(any("pixel-value agreement" in line for line in scope["covered"]))
        self.assertTrue(any("bit-equality" in line for line in scope["not_covered"]))
        self.assertTrue(any("dependency lock" in line for line in scope["not_covered"]))
        self.assertEqual(
            receipt["artifacts"]["nm_brick_cutout_adapter.py_sha256"],
            hashlib.sha256(MODULE_PATH.read_bytes()).hexdigest(),
        )

        # Pinnable identity: content_sha256 covers everything except itself and
        # the run timestamp, with the exclusion list declared in the artifact.
        self.assertEqual(
            receipt["content_hash_excludes"], ["content_sha256", "recorded_utc"]
        )
        recomputed = hashlib.sha256(
            json.dumps(
                {
                    key: value
                    for key, value in receipt.items()
                    if key not in ("content_sha256", "recorded_utc")
                },
                sort_keys=True, separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        self.assertEqual(receipt["content_sha256"], recomputed)
        # A second run with no code or fixture change must reproduce it.
        rerun = subprocess.run(
            [sys.executable, str(HERE / "cross_check_yui_boundary.py")],
            capture_output=True, text=True,
        )
        self.assertEqual(rerun.returncode, 0, rerun.stderr[-2000:])
        second = json.loads((HERE / "CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json").read_text())
        self.assertEqual(second["content_sha256"], receipt["content_sha256"])


class TestCli(AdapterTestBase):
    def test_cli_refuses_everything_but_dry_run(self) -> None:
        result = subprocess.run(
            [sys.executable, str(MODULE_PATH), "--output-dir", str(self.tmp_root / "cli_refuse")],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("BUILD_ONLY_STOP", result.stderr)

    def test_cli_dry_run_manifest_only(self) -> None:
        out = self.tmp_root / "cli_dry"
        result = subprocess.run(
            [sys.executable, str(MODULE_PATH), "--dry-run", "--output-dir", str(out)],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        summary = json.loads(result.stdout)
        self.assertEqual(summary["mode"], "DRY_RUN_MANIFEST_ONLY")
        self.assertEqual(summary["zero_issuance"]["globus_tasks_submitted"], 0)
        self.assertTrue((out / "transfer_manifest.json").is_file())


if __name__ == "__main__":
    unittest.main()
