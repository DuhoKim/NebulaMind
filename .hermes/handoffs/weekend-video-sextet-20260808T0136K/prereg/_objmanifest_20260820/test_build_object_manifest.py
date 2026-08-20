from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
PREREG = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(PREREG / "boundary_fixtures"))
sys.path.insert(0, str(PREREG / "adapter"))

import build_object_manifest as builder
import make_boundary_fixtures as round1
import cross_check_yui_boundary as adapter_crosscheck


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_verified_sidecar(path: Path, rows: list[dict]) -> None:
    path.write_text(json.dumps({"rows": rows}, sort_keys=True) + "\n", encoding="utf-8")
    path.with_suffix(path.suffix + ".sha256").write_text(f"{sha256(path)}  {path.name}\n", encoding="ascii")


def write_positions(path: Path, records: list[tuple[float, float, str]]) -> None:
    path.write_text(
        "ra,dec,ls_id\n" + "".join(f"{ra},{dec},{ls_id}\n" for ra, dec, ls_id in records),
        encoding="utf-8",
    )


def write_receipts(
    path: Path,
    bricknames: list[str],
    destination_root: Path,
    *,
    active_directory: str = "staging",
    omit_files: set[str] | None = None,
) -> None:
    omit_files = omit_files or set()
    with path.open("w", encoding="utf-8") as handle:
        for index, brickname in enumerate(reversed(bricknames)):
            relative = Path("coadd") / brickname / "image-r.fits.fz"
            handle.write(json.dumps({
                "brickname": brickname,
                "outcome": "ACCEPTED",
                "digest_verified": True,
                "destination_relative_path": str(relative),
                "local_sha256": f"{index + 1:064x}",
            }, sort_keys=True) + "\n")
            if brickname not in omit_files:
                destination = destination_root / active_directory / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(brickname.encode("ascii"))
        handle.write(json.dumps({
            "brickname": "ignored-rejected",
            "outcome": "REJECTED",
            "digest_verified": True,
            "destination_relative_path": "ignored",
            "local_sha256": "f" * 64,
        }) + "\n")


class ObjectManifestTests(unittest.TestCase):
    def test_reuses_certified_planner_for_edge_corner_and_tjunction(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            round1.generate_fixture_tree(root / "round1")
            cases = {
                row["object_id"]: row
                for row in json.loads((root / "round1" / "objects.json").read_text())
            }
            sidecar = root / "round1-sidecar.json"
            write_verified_sidecar(sidecar, adapter_crosscheck._round1_geometry_rows())
            geometry = builder.load_geometry_sidecar(sidecar)
            for object_id in ("edge_north_exact", "corner_north_east_exact"):
                case = cases[object_id]
                self.assertEqual(
                    builder.plan_candidate_bricks(
                        geometry, object_id, float(case["ra_deg"]), float(case["dec_deg"])
                    ),
                    sorted(case["expected_bricks"]),
                )

            round5_root = PREREG / "boundary_fixtures" / "generated_round5"
            round5_geometry = builder.load_geometry_sidecar(round5_root / "geometry_sidecar.json")
            round5_case = json.loads((round5_root / "objects.json").read_text())[0]
            self.assertEqual(round5_case["object_id"], "tjunction_exact")
            self.assertEqual(
                builder.plan_candidate_bricks(
                    round5_geometry,
                    "tjunction_exact",
                    float(round5_case["ra_deg"]),
                    float(round5_case["dec_deg"]),
                ),
                sorted(round5_case["expected_bricks"]),
            )
            self.assertEqual(builder.planner_module_sha256(), builder.PINNED_ADAPTER_SHA256)

    def test_every_candidate_must_be_accepted_and_manifest_matches_runner_schema(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            rows = adapter_crosscheck._round1_geometry_rows()
            sidecar = root / "sidecar.json"
            write_verified_sidecar(sidecar, rows)
            with tempfile.TemporaryDirectory() as generated:
                round1.generate_fixture_tree(Path(generated))
                cases = {r["object_id"]: r for r in json.loads((Path(generated) / "objects.json").read_text())}
            edge = cases["edge_north_exact"]
            corner = cases["corner_north_east_exact"]
            positions = root / "positions.csv"
            write_positions(positions, [
                (edge["ra_deg"], edge["dec_deg"], "edge"),
                (corner["ra_deg"], corner["dec_deg"], "corner"),
            ])
            accepted = sorted(set(edge["expected_bricks"]) | (set(corner["expected_bricks"]) - {"r+1c-1"}))
            receipts = root / "receipts.jsonl"
            destination_root = root / "destination"
            write_receipts(receipts, accepted, destination_root)
            document, summary = builder.build_object_manifest(
                positions, receipts, destination_root, sidecar
            )
            self.assertEqual(summary["objects_ready"], 1)
            self.assertEqual(summary["objects_waiting"], 1)
            self.assertEqual(summary["missing_bricks_top10"], [{"brickname": "r+1c-1", "objects_waiting": 1}])
            self.assertEqual(list(document), ["objects", "schema_version"])
            self.assertEqual(list(document["objects"]), ["edge"])
            self.assertEqual(
                [entry["brickname"] for entry in document["objects"]["edge"]],
                sorted(edge["expected_bricks"]),
            )
            for entry in document["objects"]["edge"]:
                self.assertEqual(set(entry), {"brickname", "path", "row", "sha256"})
                self.assertEqual(set(entry["row"]), {"dec", "ra"})

            runner_path = PREREG / "_cutout_runner_20260820" / "cutout_runner.py"
            spec = importlib.util.spec_from_file_location("fixture_runner", runner_path)
            runner = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = runner
            spec.loader.exec_module(runner)
            output = root / "manifest.json"
            builder.write_manifest(output, document)
            loaded = runner.load_brick_manifest(output)
            self.assertEqual(list(loaded), ["edge"])

    def test_only_bricks_requires_candidate_set_to_be_within_subset(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            sidecar = root / "sidecar.json"
            rows = adapter_crosscheck._round1_geometry_rows()
            write_verified_sidecar(sidecar, rows)
            with tempfile.TemporaryDirectory() as generated:
                round1.generate_fixture_tree(Path(generated))
                cases = {r["object_id"]: r for r in json.loads((Path(generated) / "objects.json").read_text())}
            centre, edge = cases["centre"], cases["edge_north_exact"]
            positions = root / "positions.csv"
            write_positions(positions, [
                (centre["ra_deg"], centre["dec_deg"], "centre"),
                (edge["ra_deg"], edge["dec_deg"], "edge"),
            ])
            receipts = root / "receipts.jsonl"
            destination_root = root / "destination"
            write_receipts(receipts, sorted(set(edge["expected_bricks"])), destination_root)
            only = root / "only.txt"
            only.write_text("r+0c+0\n", encoding="utf-8")
            document, summary = builder.build_object_manifest(
                positions, receipts, destination_root, sidecar, only_bricks_path=only
            )
            self.assertEqual(list(document["objects"]), ["centre"])
            self.assertEqual(summary["objects_considered"], 1)
            self.assertEqual(summary["objects_excluded_by_only_bricks"], 1)

    def test_same_inputs_produce_byte_identical_output(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            rows = adapter_crosscheck._round1_geometry_rows()
            sidecar = root / "sidecar.json"
            write_verified_sidecar(sidecar, rows)
            centre = rows[4]
            positions = root / "positions.csv"
            write_positions(positions, [(centre["ra"], centre["dec"], "z-id"), (centre["ra"], centre["dec"], "a-id")])
            receipts = root / "receipts.jsonl"
            destination_root = root / "destination"
            write_receipts(receipts, [centre["brickname"]], destination_root)
            first, first_summary = builder.build_object_manifest(positions, receipts, destination_root, sidecar)
            second, second_summary = builder.build_object_manifest(positions, receipts, destination_root, sidecar)
            one, two = root / "one.json", root / "two.json"
            builder.write_manifest(one, first)
            builder.write_manifest(two, second)
            self.assertEqual(one.read_bytes(), two.read_bytes())
            self.assertEqual(first_summary, second_summary)
            self.assertEqual(list(first["objects"]), ["a-id", "z-id"])

    def test_receipts_are_hashed_from_the_same_snapshot_used_for_the_join(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            rows = adapter_crosscheck._round1_geometry_rows()
            sidecar = root / "sidecar.json"
            write_verified_sidecar(sidecar, rows)
            centre = rows[4]
            positions = root / "positions.csv"
            write_positions(positions, [(centre["ra"], centre["dec"], "object")])
            receipts = root / "receipts.jsonl"
            receipts.write_text("", encoding="utf-8")
            original_payload = receipts.read_bytes()
            real_plan = builder.plan_candidate_bricks

            def mutate_after_receipt_load(*args, **kwargs):
                write_receipts(receipts, [centre["brickname"]], root / "destination")
                return real_plan(*args, **kwargs)

            with mock.patch.object(builder, "plan_candidate_bricks", side_effect=mutate_after_receipt_load):
                document, summary = builder.build_object_manifest(
                    positions, receipts, root / "destination", sidecar
                )
            self.assertEqual(document["objects"], {})
            self.assertEqual(summary["objects_waiting"], 1)
            self.assertEqual(summary["receipts_sha256"], hashlib.sha256(original_payload).hexdigest())

    def test_active_root_prefers_accepted_and_missing_receipted_file_waits(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            rows = adapter_crosscheck._round1_geometry_rows()
            sidecar = root / "sidecar.json"
            write_verified_sidecar(sidecar, rows)
            with tempfile.TemporaryDirectory() as generated:
                round1.generate_fixture_tree(Path(generated))
                cases = {
                    row["object_id"]: row
                    for row in json.loads((Path(generated) / "objects.json").read_text())
                }
            edge = cases["edge_north_exact"]
            bricknames = sorted(edge["expected_bricks"])
            positions = root / "positions.csv"
            write_positions(positions, [(edge["ra_deg"], edge["dec_deg"], "object")])
            receipts = root / "receipts.jsonl"
            destination_root = root / "destination"
            write_receipts(receipts, bricknames, destination_root)

            staging_document, staging_summary = builder.build_object_manifest(
                positions, receipts, destination_root, sidecar
            )
            self.assertEqual(len(staging_document["objects"]["object"]), len(bricknames))
            self.assertTrue(all(
                entry["path"].startswith(str(destination_root / "staging") + "/")
                for entry in staging_document["objects"]["object"]
            ))
            self.assertEqual(staging_summary["receipts_without_file"], 0)

            write_receipts(
                receipts,
                bricknames,
                destination_root,
                active_directory="accepted",
                omit_files={bricknames[-1]},
            )
            accepted_document, accepted_summary = builder.build_object_manifest(
                positions, receipts, destination_root, sidecar
            )
            self.assertEqual(accepted_document["objects"], {})
            self.assertEqual(accepted_summary["objects_ready"], 0)
            self.assertEqual(accepted_summary["objects_waiting"], 1)
            self.assertEqual(accepted_summary["receipts_without_file"], 1)
            self.assertEqual(
                accepted_summary["waiting_reason_histogram"],
                {"RECEIPTED_FILE_MISSING": 1},
            )

    def test_zero_intersecting_bricks_waits_without_aborting_build(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            rows = adapter_crosscheck._round1_geometry_rows()
            sidecar = root / "sidecar.json"
            write_verified_sidecar(sidecar, rows)
            centre = rows[4]
            positions = root / "positions.csv"
            write_positions(positions, [
                (10.0, 0.0, "no-intersection"),
                (centre["ra"], centre["dec"], "ready"),
            ])
            receipts = root / "receipts.jsonl"
            destination_root = root / "destination"
            write_receipts(receipts, [centre["brickname"]], destination_root)

            document, summary = builder.build_object_manifest(
                positions, receipts, destination_root, sidecar
            )

            self.assertEqual(list(document["objects"]), ["ready"])
            self.assertEqual(summary["objects_ready"], 1)
            self.assertEqual(summary["objects_waiting"], 1)
            self.assertEqual(
                summary["waiting_reason_histogram"],
                {"ZERO_INTERSECTING_BRICKS": 1},
            )


if __name__ == "__main__":
    unittest.main()
