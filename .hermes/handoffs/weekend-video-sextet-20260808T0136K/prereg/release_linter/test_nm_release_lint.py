#!/usr/bin/env python3
"""Unit tests for the NebulaMind aggregate-only release linter."""
from __future__ import annotations

import base64
import csv
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from nm_release_lint import lint_package, run_selftest

PNG_1X1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_manifest(package: Path, files: list[dict], **overrides: object) -> None:
    manifest = {
        "schema_version": 1,
        "package_id": "synthetic-test-package",
        "schema_frozen_before_statistics": True,
        "cells_frozen_before_statistics": True,
        "dynamic_query_interface": False,
        "unlimited_slicing": False,
        "files": files,
    }
    manifest.update(overrides)
    (package / "release_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def write_csv(path: Path, columns: list[str], rows: list[list[object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(columns)
        writer.writerows(rows)


def ordinary_table_entry(path: Path, columns: list[dict], **overrides: object) -> dict:
    typed_columns = []
    for original in columns:
        column = dict(original)
        if "data_type" not in column:
            role = column.get("role")
            quantity_class = column.get("quantity_class")
            if role == "support_k" or quantity_class == "study_count":
                column["data_type"] = "integer"
            elif role == "mask":
                column["data_type"] = "boolean"
            elif role in {"cell_id", "axis"}:
                column["data_type"] = "string" if role == "cell_id" else "integer"
            else:
                column["data_type"] = "number"
        typed_columns.append(column)
    entry = {
        "path": path.name,
        "role": "table",
        "sha256": sha256(path),
        "table_kind": "ordinary_aggregate",
        "object_independent_cells": True,
        "cells_frozen_before_statistics": True,
        "columns": typed_columns,
        "cell_system": {
            "id": "synthetic_partition_v1",
            "domain": "synthetic_sample",
            "family": "fixed_partition",
            "resolution": 1,
            "axes": ["synthetic_axis"],
            "partition_kind": "fixed_bins",
        },
    }
    entry.update(overrides)
    return entry


class ManifestCustodyTests(unittest.TestCase):
    def test_minimal_hash_pinned_document_package_passes(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            doc = package / "README.md"
            doc.write_text("Synthetic aggregate-only package.\n", encoding="utf-8")
            write_manifest(
                package,
                [{"path": "README.md", "role": "documentation", "sha256": sha256(doc)}],
            )

            result = lint_package(package)

            self.assertTrue(result.accepted, result.findings)
            self.assertEqual(result.findings, [])

    def test_unlisted_file_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            doc = package / "README.md"
            doc.write_text("Synthetic aggregate-only package.\n", encoding="utf-8")
            (package / "unlisted.bin").write_bytes(b"synthetic")
            write_manifest(
                package,
                [{"path": "README.md", "role": "documentation", "sha256": sha256(doc)}],
            )

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_MANIFEST_UNLISTED_FILE", {item.code for item in result.findings})

    def test_tabular_object_rows_disguised_as_documentation_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            disguised = package / "notes.txt"
            disguised.write_text(
                "objid,label,score\nSYNTH-1,L,0.9\nSYNTH-2,R,0.8\n",
                encoding="utf-8",
            )
            write_manifest(
                package,
                [{"path": disguised.name, "role": "documentation", "sha256": sha256(disguised)}],
            )

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R1_DISGUISED_TABLE", {item.code for item in result.findings})

    def test_unknown_manifest_or_file_entry_fields_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            doc = package / "README.md"
            doc.write_text("Synthetic package.\n", encoding="utf-8")
            entry = {
                "path": doc.name,
                "role": "documentation",
                "sha256": sha256(doc),
                "object_rows": [{"objid": "SYNTH-1"}],
            }
            write_manifest(package, [entry], extra_payload={"objid": "SYNTH-2"})

            result = lint_package(package)

            codes = {item.code for item in result.findings}
            self.assertFalse(result.accepted)
            self.assertIn("E_MANIFEST_UNKNOWN_FIELD", codes)
            self.assertIn("E_MANIFEST_FILE_UNKNOWN_FIELD", codes)

    def test_manifest_symlink_is_rejected_without_following_it(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            root = Path(tmp)
            package = root / "package"
            package.mkdir()
            external = root / "external_manifest.json"
            external.write_text(
                json.dumps({
                    "schema_version": 1,
                    "package_id": "external",
                    "schema_frozen_before_statistics": True,
                    "cells_frozen_before_statistics": True,
                    "dynamic_query_interface": False,
                    "unlimited_slicing": False,
                    "files": [],
                }),
                encoding="utf-8",
            )
            (package / "release_manifest.json").symlink_to(external)

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_MANIFEST_SYMLINK", {item.code for item in result.findings})

    def test_cached_object_records_in_environment_json_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            cache = package / "environment.json"
            cache.write_text(
                json.dumps({"cached_rows": [{"objid": "SYNTH-OBJECT-1", "ra": 12.3, "dec": -4.5}]}),
                encoding="utf-8",
            )
            write_manifest(
                package,
                [{"path": cache.name, "role": "environment", "sha256": sha256(cache)}],
            )

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R1_EMBEDDED_OBJECT_RECORD", {item.code for item in result.findings})

    def test_embedded_object_rows_after_code_preamble_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            code = package / "pipeline.py"
            code.write_text(
                "# Synthetic code preamble\n"
                "CACHED_ROWS = [\n"
                "    {'objid': 'FIXTURE-OBJECT-1', 'ra': 12.3, 'dec': -4.5},\n"
                "]\n",
                encoding="utf-8",
            )
            write_manifest(
                package,
                [{"path": code.name, "role": "code", "sha256": sha256(code)}],
            )

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R1_EMBEDDED_OBJECT_RECORD", {item.code for item in result.findings})

    def test_query_aliases_and_explicit_synthetic_code_fixtures_pass(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            code = package / "synthetic_harness.py"
            code.write_text(
                "QUERY_ALIASES = {'objid': 'objid', 'ra': 'ra', 'dec': 'dec'}\n"
                "SYNTHETIC_ROWS = [\n"
                "    {'objid': 'SYNTH-OBJECT-1', 'ra': 12.3, 'dec': -4.5},\n"
                "]\n",
                encoding="utf-8",
            )
            write_manifest(
                package,
                [{"path": code.name, "role": "code", "sha256": sha256(code)}],
            )

            result = lint_package(package)

            self.assertTrue(result.accepted, result.findings)


class RowlessRuleTests(unittest.TestCase):
    def test_ordinary_aggregate_without_object_fields_passes(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "aggregate.csv"
            write_csv(table, ["cell_id", "k", "masked", "mean_sign"], [["A", 60, False, 0.1]])
            columns = [
                {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
                {"name": "k", "role": "support_k", "quantity_class": "study_count"},
                {"name": "masked", "role": "mask", "quantity_class": "mask"},
                {"name": "mean_sign", "role": "quantity", "quantity_class": "study_estimand"},
            ]
            write_manifest(package, [ordinary_table_entry(table, columns)])

            result = lint_package(package)

            self.assertTrue(result.accepted, result.findings)

    def test_per_object_identifier_label_and_score_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "objects.csv"
            write_csv(table, ["objid", "label", "score"], [["SYNTH-1", "L", 0.9]])
            columns = [
                {"name": "objid", "role": "cell_id", "quantity_class": "cell_definition"},
                {"name": "label", "role": "quantity", "quantity_class": "study_estimand"},
                {"name": "score", "role": "quantity", "quantity_class": "instrument_summary"},
            ]
            write_manifest(package, [ordinary_table_entry(table, columns)])

            result = lint_package(package)

            codes = {item.code for item in result.findings}
            self.assertFalse(result.accepted)
            self.assertIn("E_R1_IDENTIFIER_COLUMN", codes)
            self.assertIn("E_R1_PER_OBJECT_DERIVED_COLUMN", codes)

    def test_ra_dec_columns_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "coordinates.csv"
            write_csv(table, ["cell_id", "ra", "dec", "k", "masked"], [["A", 123.1, -4.2, 60, False]])
            columns = [
                {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
                {"name": "ra", "role": "axis", "quantity_class": "cell_definition"},
                {"name": "dec", "role": "axis", "quantity_class": "cell_definition"},
                {"name": "k", "role": "support_k", "quantity_class": "study_count"},
                {"name": "masked", "role": "mask", "quantity_class": "mask"},
            ]
            write_manifest(package, [ordinary_table_entry(table, columns)])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R1_COORDINATE_COLUMN", {item.code for item in result.findings})

    def test_generic_object_precision_float_pair_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "hidden_coordinates.csv"
            rows = [
                ["A", "123.12345678", "-4.12345678", 60, False],
                ["B", "124.23456789", "-3.23456789", 60, False],
                ["C", "125.34567891", "-2.34567891", 60, False],
            ]
            write_csv(table, ["cell_id", "axis_x", "axis_y", "k", "masked"], rows)
            columns = [
                {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
                {"name": "axis_x", "role": "axis", "quantity_class": "cell_definition"},
                {"name": "axis_y", "role": "axis", "quantity_class": "cell_definition"},
                {"name": "k", "role": "support_k", "quantity_class": "study_count"},
                {"name": "masked", "role": "mask", "quantity_class": "mask"},
            ]
            write_manifest(package, [ordinary_table_entry(table, columns)])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R1_OBJECT_PRECISION_FLOAT_PAIR", {item.code for item in result.findings})

    def test_string_payload_cannot_be_declared_as_study_estimand(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "encoded_payload.csv"
            write_csv(
                table,
                ["cell_id", "k", "masked", "payload"],
                [["A", 60, False, '{"objid":"SYNTH-1","ra":12.3}']],
            )
            columns = [
                {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
                {"name": "k", "role": "support_k", "quantity_class": "study_count"},
                {"name": "masked", "role": "mask", "quantity_class": "mask"},
                {
                    "name": "payload", "role": "quantity",
                    "quantity_class": "study_estimand", "data_type": "string",
                },
            ]
            write_manifest(package, [ordinary_table_entry(table, columns)])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R3_ROLE_DATA_TYPE", {item.code for item in result.findings})

    def test_coordinate_pair_mislabeled_as_quantities_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "mislabeled_coordinates.csv"
            rows = [
                ["A", 60, False, "123.12345678", "-4.12345678"],
                ["B", 60, False, "124.23456789", "-3.23456789"],
                ["C", 60, False, "125.34567891", "-2.34567891"],
            ]
            write_csv(table, ["cell_id", "k", "masked", "metric_x", "metric_y"], rows)
            columns = [
                {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
                {"name": "k", "role": "support_k", "quantity_class": "study_count"},
                {"name": "masked", "role": "mask", "quantity_class": "mask"},
                {"name": "metric_x", "role": "quantity", "quantity_class": "study_estimand"},
                {"name": "metric_y", "role": "quantity", "quantity_class": "study_estimand"},
            ]
            write_manifest(package, [ordinary_table_entry(table, columns)])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R1_OBJECT_PRECISION_FLOAT_PAIR", {item.code for item in result.findings})


class FixedFiniteRuleTests(unittest.TestCase):
    def test_dynamic_query_interface_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            doc = package / "README.md"
            doc.write_text("Synthetic package.\n", encoding="utf-8")
            write_manifest(
                package,
                [{"path": doc.name, "role": "documentation", "sha256": sha256(doc)}],
                dynamic_query_interface=True,
            )

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R2_DYNAMIC_QUERY", {item.code for item in result.findings})

    def test_object_dependent_or_post_statistic_cells_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "adaptive.csv"
            write_csv(table, ["cell_id", "k", "masked", "mean_sign"], [["A", 60, False, 0.1]])
            columns = [
                {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
                {"name": "k", "role": "support_k", "quantity_class": "study_count"},
                {"name": "masked", "role": "mask", "quantity_class": "mask"},
                {"name": "mean_sign", "role": "quantity", "quantity_class": "study_estimand"},
            ]
            entry = ordinary_table_entry(
                table,
                columns,
                object_independent_cells=False,
                cells_frozen_before_statistics=False,
            )
            write_manifest(package, [entry])

            result = lint_package(package)

            codes = {item.code for item in result.findings}
            self.assertIn("E_R2_OBJECT_DEPENDENT_CELLS", codes)
            self.assertIn("E_R2_TABLE_NOT_FROZEN", codes)

    def test_nside16_whole_sample_scan_surface_passes(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "scan_nside16.csv"
            rows = [[i, f"{(i % 17) / 1000:.6f}"] for i in range(3072)]
            write_csv(table, ["scan_pixel", "whole_sample_statistic"], rows)
            columns = [
                {"name": "scan_pixel", "role": "axis", "quantity_class": "cell_definition"},
                {
                    "name": "whole_sample_statistic",
                    "role": "quantity",
                    "quantity_class": "whole_sample_statistic",
                },
            ]
            entry = ordinary_table_entry(
                table,
                columns,
                table_kind="whole_sample_scan",
                whole_sample_n=12000,
                membership_partition=False,
                cell_system={
                    "id": "nside16_direction_scan",
                    "domain": "whole_sample_direction",
                    "family": "healpix_scan",
                    "resolution": 16,
                    "axes": ["direction_index"],
                    "partition_kind": "whole_sample_directional_scan",
                },
            )
            write_manifest(package, [entry])

            result = lint_package(package)

            self.assertTrue(result.accepted, result.findings)

    def test_scan_claiming_membership_partition_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "bad_scan.csv"
            write_csv(table, ["scan_pixel", "whole_sample_statistic"], [[0, 0.1]])
            columns = [
                {"name": "scan_pixel", "role": "axis", "quantity_class": "cell_definition"},
                {
                    "name": "whole_sample_statistic",
                    "role": "quantity",
                    "quantity_class": "whole_sample_statistic",
                },
            ]
            entry = ordinary_table_entry(
                table,
                columns,
                table_kind="whole_sample_scan",
                whole_sample_n=12000,
                membership_partition=True,
            )
            write_manifest(package, [entry])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R2_SCAN_IS_MEMBERSHIP", {item.code for item in result.findings})


class StudyResultRuleTests(unittest.TestCase):
    def test_mean_survey_magnitude_is_rejected_even_if_misclassified(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "survey_attribute.csv"
            write_csv(table, ["cell_id", "k", "masked", "mean_magnitude"], [["A", 60, False, 20.1]])
            columns = [
                {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
                {"name": "k", "role": "support_k", "quantity_class": "study_count"},
                {"name": "masked", "role": "mask", "quantity_class": "mask"},
                {"name": "mean_magnitude", "role": "quantity", "quantity_class": "study_estimand"},
            ]
            write_manifest(package, [ordinary_table_entry(table, columns)])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R3_SURVEY_ATTRIBUTE", {item.code for item in result.findings})

    def test_unknown_quantity_class_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "unknown_quantity.csv"
            write_csv(table, ["cell_id", "k", "masked", "mystery"], [["A", 60, False, 1.0]])
            columns = [
                {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
                {"name": "k", "role": "support_k", "quantity_class": "study_count"},
                {"name": "masked", "role": "mask", "quantity_class": "mask"},
                {"name": "mystery", "role": "quantity", "quantity_class": "unknown"},
            ]
            write_manifest(package, [ordinary_table_entry(table, columns)])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R3_UNKNOWN_QUANTITY_CLASS", {item.code for item in result.findings})

    def test_allowed_class_with_unregistered_quantity_name_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "semantic_alias.csv"
            write_csv(table, ["cell_id", "k", "masked", "foo"], [["A", 60, False, 123.0]])
            columns = [
                {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
                {"name": "k", "role": "support_k", "quantity_class": "study_count"},
                {"name": "masked", "role": "mask", "quantity_class": "mask"},
                {"name": "foo", "role": "quantity", "quantity_class": "study_estimand"},
            ]
            write_manifest(package, [ordinary_table_entry(table, columns)])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R3_UNAPPROVED_QUANTITY", {item.code for item in result.findings})

    def test_column_role_and_quantity_class_must_agree(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "role_mismatch.csv"
            write_csv(table, ["cell_id", "k", "masked", "mean_sign"], [["A", 60, False, 0.1]])
            columns = [
                {"name": "cell_id", "role": "cell_id", "quantity_class": "study_estimand"},
                {"name": "k", "role": "support_k", "quantity_class": "study_count"},
                {"name": "masked", "role": "mask", "quantity_class": "mask"},
                {"name": "mean_sign", "role": "quantity", "quantity_class": "study_estimand"},
            ]
            write_manifest(package, [ordinary_table_entry(table, columns)])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R3_ROLE_CLASS_MISMATCH", {item.code for item in result.findings})


class NumericGuardrailTests(unittest.TestCase):
    @staticmethod
    def columns() -> list[dict]:
        return [
            {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
            {"name": "k", "role": "support_k", "quantity_class": "study_count"},
            {"name": "masked", "role": "mask", "quantity_class": "mask"},
            {"name": "mean_sign", "role": "quantity", "quantity_class": "study_estimand"},
        ]

    def test_unmasked_cell_below_k_floor_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "low_k.csv"
            write_csv(table, ["cell_id", "k", "masked", "mean_sign"], [["A", 49, False, 0.1]])
            write_manifest(package, [ordinary_table_entry(table, self.columns())])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_G_K_FLOOR", {item.code for item in result.findings})

    def test_subthreshold_cell_passes_only_when_masked_values_are_blank(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "masked.csv"
            write_csv(table, ["cell_id", "k", "masked", "mean_sign"], [["A", 49, True, ""]])
            write_manifest(package, [ordinary_table_entry(table, self.columns())])

            result = lint_package(package)

            self.assertTrue(result.accepted, result.findings)

    def test_mask_flag_cannot_hide_a_released_subthreshold_value(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "masked_leak.csv"
            write_csv(table, ["cell_id", "k", "masked", "mean_sign"], [["A", 49, True, 0.1]])
            write_manifest(package, [ordinary_table_entry(table, self.columns())])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_G_MASK_LEAK", {item.code for item in result.findings})

    def test_ordinary_table_above_5000_cells_is_rejected_by_controlling_budget(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            table = package / "too_many_cells.csv"
            rows = [[f"C{i:04d}", 60, False, 0.0] for i in range(5001)]
            write_csv(table, ["cell_id", "k", "masked", "mean_sign"], rows)
            write_manifest(package, [ordinary_table_entry(table, self.columns())])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R5_CUMULATIVE_CELL_BUDGET", {item.code for item in result.findings})


class CumulativePackageRuleTests(unittest.TestCase):
    @staticmethod
    def columns() -> list[dict]:
        return NumericGuardrailTests.columns()

    @staticmethod
    def system(system_id: str, family: str, resolution: int, axis: str) -> dict:
        return {
            "id": system_id,
            "domain": "synthetic_sky" if family == "healpix" else system_id,
            "family": family,
            "resolution": resolution,
            "axes": [axis],
            "partition_kind": family,
        }

    def test_related_nside32_and_nside64_same_quantity_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            coarse = package / "nside32.csv"
            fine = package / "nside64.csv"
            write_csv(coarse, ["cell_id", "k", "masked", "mean_sign"], [["C0", 120, False, 0.1]])
            write_csv(fine, ["cell_id", "k", "masked", "mean_sign"], [["F0", 60, False, 0.2]])
            entries = [
                ordinary_table_entry(
                    coarse,
                    self.columns(),
                    cell_system=self.system("nside32", "healpix", 32, "sky"),
                ),
                ordinary_table_entry(
                    fine,
                    self.columns(),
                    cell_system=self.system("nside64", "healpix", 64, "sky"),
                ),
            ]
            write_manifest(package, entries)

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R4_RELATED_CELL_SYSTEMS", {item.code for item in result.findings})

    def test_relabeling_domain_and_axis_cannot_hide_cross_file_hazard(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            coarse = package / "nside32.csv"
            fine = package / "nside64.csv"
            write_csv(coarse, ["cell_id", "k", "masked", "mean_sign"], [["C0", 120, False, 0.1]])
            write_csv(fine, ["cell_id", "k", "masked", "mean_sign"], [["F0", 60, False, 0.2]])
            coarse_system = self.system("nside32", "healpix", 32, "sky")
            fine_system = self.system("nside64", "healpix", 64, "invented_axis")
            fine_system["domain"] = "invented_domain"
            entries = [
                ordinary_table_entry(coarse, self.columns(), cell_system=coarse_system),
                ordinary_table_entry(fine, self.columns(), cell_system=fine_system),
            ]
            write_manifest(package, entries)

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R4_RELATED_CELL_SYSTEMS", {item.code for item in result.findings})

    def test_refined_finest_unmasked_cell_below_k_floor_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            coarse = package / "coarse.csv"
            fine = package / "fine.csv"
            write_csv(coarse, ["cell_id", "k", "masked", "mean_sign"], [["C0", 100, False, 0.1]])
            write_csv(fine, ["cell_id", "k", "masked", "mean_sign"], [["F0", 40, False, 0.2]])
            entries = [
                ordinary_table_entry(
                    coarse,
                    self.columns(),
                    cell_system=self.system("nside32", "healpix", 32, "sky"),
                ),
                ordinary_table_entry(
                    fine,
                    self.columns(),
                    cell_system=self.system("nside64", "healpix", 64, "sky"),
                ),
            ]
            write_manifest(package, entries)

            result = lint_package(package)

            self.assertIn("E_R4_REFINEMENT_K", {item.code for item in result.findings})

    def test_cumulative_unique_ordinary_cells_above_5000_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            first = package / "first.csv"
            second = package / "second.csv"
            write_csv(
                first,
                ["cell_id", "k", "masked", "mean_sign"],
                [[f"A{i:04d}", 60, False, 0.0] for i in range(2501)],
            )
            write_csv(
                second,
                ["cell_id", "k", "masked", "mean_sign"],
                [[f"B{i:04d}", 60, False, 0.0] for i in range(2500)],
            )
            entries = [
                ordinary_table_entry(
                    first,
                    self.columns(),
                    cell_system=self.system("independent_A", "fixed_partition", 1, "axis_A"),
                ),
                ordinary_table_entry(
                    second,
                    self.columns(),
                    cell_system=self.system("independent_B", "fixed_partition", 1, "axis_B"),
                ),
            ]
            write_manifest(package, entries)

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R5_CUMULATIVE_CELL_BUDGET", {item.code for item in result.findings})


class ImageComplianceRuleTests(unittest.TestCase):
    def test_original_result_image_with_source_pixels_absent_passes(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            image = package / "result.png"
            image.write_bytes(PNG_1X1)
            entry = {
                "path": image.name,
                "role": "image",
                "sha256": sha256(image),
                "contains_source_pixels": False,
                "image_origin": "original_study_visualization",
            }
            write_manifest(package, [entry])

            result = lint_package(package)

            self.assertTrue(result.accepted, result.findings)

    def test_source_pixel_image_without_layer_route_and_credit_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            image = package / "source.png"
            image.write_bytes(PNG_1X1)
            entry = {
                "path": image.name,
                "role": "image",
                "sha256": sha256(image),
                "contains_source_pixels": True,
            }
            write_manifest(package, [entry])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R6_IMAGE_COMPLIANCE", {item.code for item in result.findings})

    def test_arbitrary_asserted_source_image_route_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            image = package / "source.png"
            image.write_bytes(PNG_1X1)
            entry = {
                "path": image.name,
                "role": "image",
                "sha256": sha256(image),
                "contains_source_pixels": True,
                "image_layer": "x",
                "licence_id": "x",
                "licence_url": "x",
                "credit_text": "x",
                "credit_visible": True,
                "modification_status": "unmodified",
            }
            write_manifest(package, [entry])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R6_IMAGE_ROUTE", {item.code for item in result.findings})

    def test_exact_legacy_source_image_route_passes_metadata_gate(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            image = package / "source.png"
            image.write_bytes(PNG_1X1)
            entry = {
                "path": image.name,
                "role": "image",
                "sha256": sha256(image),
                "contains_source_pixels": True,
                "image_layer": "legacy_surveys",
                "licence_id": "CC-BY-4.0",
                "licence_url": "https://creativecommons.org/licenses/by/4.0/",
                "credit_text": "Legacy Surveys / D. Lang (Perimeter Institute)",
                "credit_visible": True,
                "modification_status": "unmodified",
            }
            write_manifest(package, [entry])

            result = lint_package(package)

            self.assertTrue(result.accepted, result.findings)

    def test_compliant_image_cannot_cure_a_catalogue_like_table(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_lint_unit_") as tmp:
            package = Path(tmp)
            image = package / "credited.png"
            image.write_bytes(PNG_1X1)
            table = package / "objects.csv"
            write_csv(table, ["objid", "label"], [["SYNTH-1", "L"]])
            image_entry = {
                "path": image.name,
                "role": "image",
                "sha256": sha256(image),
                "contains_source_pixels": True,
                "image_layer": "legacy_surveys",
                "licence_id": "CC-BY-4.0",
                "licence_url": "https://creativecommons.org/licenses/by/4.0/",
                "credit_text": "Legacy Surveys / D. Lang (Perimeter Institute)",
                "credit_visible": True,
                "modification_status": "unmodified",
            }
            columns = [
                {"name": "objid", "role": "cell_id", "quantity_class": "cell_definition"},
                {"name": "label", "role": "quantity", "quantity_class": "study_estimand"},
            ]
            write_manifest(package, [image_entry, ordinary_table_entry(table, columns)])

            result = lint_package(package)

            self.assertFalse(result.accepted)
            self.assertIn("E_R1_IDENTIFIER_COLUMN", {item.code for item in result.findings})


class SelfTestHarnessTests(unittest.TestCase):
    def test_required_synthetic_fixture_matrix_matches_expected_verdicts(self) -> None:
        summary = run_selftest()
        names = {item["fixture"] for item in summary["fixtures"]}
        required = {
            "bad_per_object_row_file",
            "bad_per_brick_270577",
            "bad_ra_dec",
            "bad_nside32_nside64_overlap",
            "bad_cumulative_cell_budget",
            "bad_mean_survey_magnitude",
            "bad_low_k_unmasked",
            "bad_rule2_dynamic_interface",
            "bad_rule6_image_missing_compliance",
            "bad_manifest_symlink",
            "bad_environment_cached_object_rows",
            "bad_string_payload_quantity",
            "bad_rule6_asserted_bogus_route",
            "good_s1_nside32_masked_maps",
            "good_67_partition_table",
            "good_9_hand_check_strata",
            "good_nside16_scan_surface",
        }
        self.assertTrue(required.issubset(names), required - names)
        self.assertTrue(summary["passed"], summary)
        self.assertTrue(all(item["match"] for item in summary["fixtures"]))
        self.assertTrue(
            all(set(item["expected_codes"]) == set(item["actual_codes"]) for item in summary["fixtures"])
        )
        by_name = {item["fixture"]: item for item in summary["fixtures"]}
        self.assertEqual(
            by_name["good_s1_nside32_masked_maps"]["metrics"]["ordinary_unique_cells_cumulative"],
            4096,
        )


if __name__ == "__main__":
    unittest.main()
