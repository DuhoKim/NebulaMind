#!/usr/bin/env python3
"""Fail-closed linter for NebulaMind aggregate-only release packages.

The linter validates a complete hash-pinned package rooted at a directory containing
``release_manifest.json``. It is a conservative engineering gate, not legal advice.
"""
from __future__ import annotations

import argparse
import ast
import base64
import csv
import hashlib
import json
import math
import os
import re
import sys
import tempfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Iterable, Optional, Sequence

MANIFEST_NAME = "release_manifest.json"
SCHEMA_VERSION = 1
MAX_TABLE_CELLS = 5_000
MAX_CUMULATIVE_CELLS = 5_000
MIN_K = 50
TOP_LEVEL_MANIFEST_FIELDS = {
    "schema_version", "package_id", "schema_frozen_before_statistics",
    "cells_frozen_before_statistics", "dynamic_query_interface", "unlimited_slicing", "files",
}
BASE_FILE_FIELDS = {"path", "role", "sha256"}
TABLE_FILE_FIELDS = BASE_FILE_FIELDS | {
    "table_kind", "object_independent_cells", "cells_frozen_before_statistics",
    "columns", "cell_system", "whole_sample_n", "membership_partition",
}
IMAGE_FILE_FIELDS = BASE_FILE_FIELDS | {
    "contains_source_pixels", "image_origin", "image_layer", "licence_id",
    "licence_url", "credit_text", "credit_visible", "modification_status",
}
CELL_SYSTEM_FIELDS = {
    "id", "domain", "family", "resolution", "axes", "partition_kind",
    "overlap_group", "parent_system_id",
}
COLUMN_SCHEMA_FIELDS = {"name", "role", "quantity_class", "data_type"}

ALLOWED_ROLES = {
    "documentation",
    "code",
    "environment",
    "commitment",
    "table",
    "image",
}
ROLE_EXTENSIONS = {
    "documentation": {".md", ".txt"},
    "code": {".py", ".sh"},
    "environment": {".json", ".lock", ".toml", ".txt", ".yaml", ".yml"},
    "commitment": {".json", ".sha256", ".txt"},
    "table": {".csv", ".json"},
    "image": {".jpeg", ".jpg", ".png"},
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
SHA256_LINE_RE = re.compile(r"^[0-9a-f]{64}(?:[ \t]+[* ]?[A-Za-z0-9_.:/-]+)?$")
URL_RE = re.compile(r"(?:https?://|ftp://|s3://)", re.IGNORECASE)
IDENTIFIER_NAMES = {
    "objid", "objectid", "objectkey", "sourceid", "lsid", "brickid",
    "brickname", "release", "rowhash", "reversiblerowhash", "catalogid", "targetid",
    "source", "sourcefield", "surveyfield",
}
COORDINATE_NAMES = {
    "ra", "dec", "radeg", "decdeg", "rightascension", "declination",
    "galacticl", "galacticb", "longitude", "latitude",
}
PER_OBJECT_DERIVED_NAMES = {
    "label", "score", "confidence", "embedding", "chirality", "handedness",
    "prediction", "probability", "cutouturl", "sourceurl",
}
ALLOWED_TABLE_KINDS = {"ordinary_aggregate", "whole_sample_scan"}
ALLOWED_COLUMN_ROLES = {
    "cell_id", "axis", "support_k", "mask", "quantity", "uncertainty", "control",
}
ALLOWED_QUANTITY_CLASSES = {
    "cell_definition", "study_count", "mask", "study_estimand",
    "instrument_summary", "uncertainty", "control", "whole_sample_statistic",
}
ALLOWED_DATA_TYPES = {"string", "integer", "number", "boolean"}
APPROVED_QUANTITY_NAMES_BY_CLASS = {
    "study_estimand": {"mean_sign", "effect_size", "estimate"},
    "instrument_summary": {"abstention_fraction", "sensitivity"},
    "study_count": {"accepted_count", "count", "tp", "tn", "fp", "fn"},
    "whole_sample_statistic": {"whole_sample_statistic"},
    "uncertainty": {"standard_error", "ci_lower", "ci_upper"},
    "control": {"control_value", "null_statistic"},
}
ROLE_DATA_TYPE_COMPATIBILITY = {
    "cell_id": {"string", "integer"},
    "axis": {"string", "integer"},
    "support_k": {"integer"},
    "mask": {"boolean"},
    "quantity": {"integer", "number"},
    "uncertainty": {"number"},
    "control": {"integer", "number"},
}
ROLE_CLASS_COMPATIBILITY = {
    "cell_id": {"cell_definition"},
    "axis": {"cell_definition"},
    "support_k": {"study_count"},
    "mask": {"mask"},
    "quantity": {"study_estimand", "instrument_summary", "study_count", "whole_sample_statistic"},
    "uncertainty": {"uncertainty"},
    "control": {"control"},
}
SURVEY_ATTRIBUTE_RE = re.compile(
    r"(?:magnitude|meanmag|medianmag|mag[ugrizy]|redshift|zphot|zspec|"
    r"meansize|mediansize|rhalf|halflightradius|meanflux|medianflux|"
    r"flux[ugrizy]|meancolor|mediancolor|surveyattribute)"
)
SUSPICIOUS_QUANTITY_RE = re.compile(
    r"^(?:payload|blob|record|row|raw|data|object|source|field|value|encoded|serialized)(?:s|data|value)?$"
)
ALLOWED_SOURCE_IMAGE_LAYERS = {"legacy_surveys", "decals", "bass", "mzls"}
LEGACY_LICENCE_ID = "CC-BY-4.0"
LEGACY_LICENCE_URL = "https://creativecommons.org/licenses/by/4.0/"
LEGACY_CREDIT = "Legacy Surveys / D. Lang (Perimeter Institute)"


@dataclass(frozen=True)
class Finding:
    code: str
    rule: str
    message: str
    path: Optional[str] = None
    evidence: dict[str, Any] = field(default_factory=dict)


@dataclass
class LintResult:
    package: str
    accepted: bool
    findings: list[Finding]
    metrics: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "package": self.package,
            "verdict": "ACCEPT" if self.accepted else "REJECT",
            "findings": [asdict(item) for item in self.findings],
            "metrics": self.metrics,
        }


@dataclass
class ParsedTable:
    entry: dict[str, Any]
    path: str
    header: list[str]
    rows: list[dict[str, str]]


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _finding(
    findings: list[Finding],
    code: str,
    rule: str,
    message: str,
    path: Optional[str] = None,
    **evidence: Any,
) -> None:
    findings.append(Finding(code, rule, message, path, evidence))


def _load_manifest(package: Path, findings: list[Finding]) -> Optional[dict[str, Any]]:
    manifest_path = package / MANIFEST_NAME
    if manifest_path.is_symlink():
        _finding(
            findings,
            "E_MANIFEST_SYMLINK",
            "fail_closed",
            "Manifest must be an in-package regular file, not a symlink.",
            MANIFEST_NAME,
        )
        return None
    if not manifest_path.is_file():
        _finding(
            findings,
            "E_MANIFEST_MISSING",
            "fail_closed",
            f"Required {MANIFEST_NAME} is absent.",
            MANIFEST_NAME,
        )
        return None
    try:
        value = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        _finding(
            findings,
            "E_MANIFEST_UNPARSEABLE",
            "fail_closed",
            "Manifest cannot be parsed as UTF-8 JSON.",
            MANIFEST_NAME,
            error=str(exc),
        )
        return None
    if not isinstance(value, dict):
        _finding(
            findings,
            "E_MANIFEST_SCHEMA",
            "fail_closed",
            "Manifest root must be a JSON object.",
            MANIFEST_NAME,
        )
        return None
    return value


def _safe_relative_path(value: object) -> Optional[Path]:
    if not isinstance(value, str) or not value or "\\" in value:
        return None
    path = Path(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        return None
    return path


def _normalize_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def _parse_table(
    package: Path, entry: dict[str, Any], findings: list[Finding]
) -> Optional[ParsedTable]:
    rel = _safe_relative_path(entry.get("path"))
    if rel is None:
        return None
    rel_text = rel.as_posix()
    path = package / rel
    if not path.is_file():
        return None
    if path.suffix.lower() != ".csv":
        _finding(
            findings, "E_TABLE_UNKNOWN_FORMAT", "fail_closed",
            "Only strict UTF-8 CSV tables are supported by schema version 1.", rel_text,
        )
        return None
    try:
        with path.open("r", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            header = list(reader.fieldnames or [])
            if not header or any(not name for name in header) or len(set(header)) != len(header):
                raise ValueError("header is empty, duplicated, or contains an empty name")
            rows: list[dict[str, str]] = []
            for row_number, row in enumerate(reader, start=2):
                if None in row or any(value is None for value in row.values()):
                    raise ValueError(f"row {row_number} has the wrong number of fields")
                rows.append({str(key): str(value) for key, value in row.items()})
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        _finding(
            findings, "E_TABLE_UNPARSEABLE", "fail_closed",
            "Table cannot be parsed completely as strict UTF-8 CSV.", rel_text, error=str(exc),
        )
        return None

    declared_columns = entry.get("columns")
    if not isinstance(declared_columns, list) or not all(
        isinstance(item, dict) and isinstance(item.get("name"), str)
        for item in declared_columns
    ):
        _finding(
            findings, "E_TABLE_SCHEMA_UNPARSEABLE", "fail_closed",
            "Table entry must declare every column as a schema object.", rel_text,
        )
    else:
        declared_names = [str(item["name"]) for item in declared_columns]
        if declared_names != header:
            _finding(
                findings, "E_TABLE_SCHEMA_MISMATCH", "fail_closed",
                "Declared columns do not exactly match CSV header order.", rel_text,
                declared=declared_names, actual=header,
            )
    return ParsedTable(entry, rel_text, header, rows)


def _lint_rowless(table: ParsedTable, findings: list[Finding]) -> None:
    normalized = {_normalize_name(name): name for name in table.header}
    for key in sorted(set(normalized) & IDENTIFIER_NAMES):
        _finding(
            findings, "E_R1_IDENTIFIER_COLUMN", "R1_rowless",
            "Object/catalogue identifier or reversible-row field is forbidden.",
            table.path, column=normalized[key],
        )
    for key in sorted(set(normalized) & COORDINATE_NAMES):
        _finding(
            findings, "E_R1_COORDINATE_COLUMN", "R1_rowless",
            "Coordinate-like column is forbidden.", table.path, column=normalized[key],
        )
    for key in sorted(set(normalized) & PER_OBJECT_DERIVED_NAMES):
        _finding(
            findings, "E_R1_PER_OBJECT_DERIVED_COLUMN", "R1_rowless",
            "Per-object label, score, confidence, embedding, or source field is forbidden.",
            table.path, column=normalized[key],
        )
    for row_index, row in enumerate(table.rows, start=2):
        for column, value in row.items():
            if URL_RE.search(value):
                _finding(
                    findings, "E_R1_URL_VALUE", "R1_rowless",
                    "URL-like table cell is forbidden.", table.path,
                    row=row_index, column=column,
                )
                return

    declared = table.entry.get("columns")
    numeric_candidate_names = [
        str(item.get("name"))
        for item in declared
        if isinstance(declared, list)
        and isinstance(item, dict)
        and item.get("role") in {"axis", "quantity", "uncertainty", "control"}
        and isinstance(item.get("name"), str)
    ] if isinstance(declared, list) else []
    numeric_candidates: dict[str, list[float]] = {}
    for name in numeric_candidate_names:
        values = [row.get(name, "").strip() for row in table.rows]
        if len(values) < 3 or any(not value for value in values):
            continue
        if any(
            "." not in value
            or len(value.rsplit(".", 1)[1].rstrip("0")) < 6
            for value in values
        ):
            continue
        try:
            numbers = [float(value) for value in values]
        except ValueError:
            continue
        if len(set(numbers)) / len(numbers) < 0.8:
            continue
        if max(numbers) - min(numbers) < 1.0:
            continue
        numeric_candidates[name] = numbers
    candidates = sorted(numeric_candidates)
    for first_index, first_name in enumerate(candidates):
        for second_name in candidates[first_index + 1 :]:
            first_values = numeric_candidates[first_name]
            second_values = numeric_candidates[second_name]
            first_ra_second_dec = (
                all(0.0 <= value < 360.0 for value in first_values)
                and all(-90.0 <= value <= 90.0 for value in second_values)
            )
            second_ra_first_dec = (
                all(0.0 <= value < 360.0 for value in second_values)
                and all(-90.0 <= value <= 90.0 for value in first_values)
            )
            if first_ra_second_dec or second_ra_first_dec:
                _finding(
                    findings, "E_R1_OBJECT_PRECISION_FLOAT_PAIR", "R1_rowless",
                    "Two high-precision numeric columns have object-coordinate-like ranges.",
                    table.path, columns=[first_name, second_name], rows=len(table.rows),
                )
                return


def _lint_fixed_finite_manifest(manifest: dict[str, Any], findings: list[Finding]) -> None:
    required_true = {
        "schema_frozen_before_statistics": "E_R2_SCHEMA_NOT_FROZEN",
        "cells_frozen_before_statistics": "E_R2_CELLS_NOT_FROZEN",
    }
    required_false = {
        "dynamic_query_interface": "E_R2_DYNAMIC_QUERY",
        "unlimited_slicing": "E_R2_UNLIMITED_SLICING",
    }
    for key, code in required_true.items():
        if manifest.get(key) is not True:
            _finding(
                findings, code, "R2_fixed_and_finite",
                f"Manifest field '{key}' must be exactly true.", MANIFEST_NAME,
                actual=manifest.get(key),
            )
    for key, code in required_false.items():
        if manifest.get(key) is not False:
            _finding(
                findings, code, "R2_fixed_and_finite",
                f"Manifest field '{key}' must be exactly false.", MANIFEST_NAME,
                actual=manifest.get(key),
            )


def _lint_closed_manifest_schema(manifest: dict[str, Any], findings: list[Finding]) -> None:
    unknown_top = sorted(set(manifest) - TOP_LEVEL_MANIFEST_FIELDS)
    if unknown_top:
        _finding(
            findings, "E_MANIFEST_UNKNOWN_FIELD", "fail_closed",
            "Manifest contains fields outside schema version 1.", MANIFEST_NAME,
            fields=unknown_top,
        )
    package_id = manifest.get("package_id")
    if not isinstance(package_id, str) or not package_id.strip():
        _finding(
            findings, "E_MANIFEST_PACKAGE_ID", "fail_closed",
            "Manifest package_id must be a nonempty string.", MANIFEST_NAME,
            actual=package_id,
        )
    raw_entries = manifest.get("files")
    if not isinstance(raw_entries, list):
        return
    for index, entry in enumerate(raw_entries):
        if not isinstance(entry, dict):
            continue
        role = entry.get("role")
        allowed = (
            TABLE_FILE_FIELDS if role == "table"
            else IMAGE_FILE_FIELDS if role == "image"
            else BASE_FILE_FIELDS
        )
        unknown = sorted(set(entry) - allowed)
        if unknown:
            _finding(
                findings, "E_MANIFEST_FILE_UNKNOWN_FIELD", "fail_closed",
                "File entry contains fields outside its role schema.", MANIFEST_NAME,
                entry_index=index, entry_path=entry.get("path"), fields=unknown,
            )
        if role != "table":
            continue
        cell_system = entry.get("cell_system")
        if isinstance(cell_system, dict):
            unknown_system = sorted(set(cell_system) - CELL_SYSTEM_FIELDS)
            if unknown_system:
                _finding(
                    findings, "E_MANIFEST_CELL_SYSTEM_UNKNOWN_FIELD", "fail_closed",
                    "Cell-system declaration contains fields outside schema version 1.",
                    str(entry.get("path")), fields=unknown_system,
                )
            resolution = cell_system.get("resolution")
            if (
                not isinstance(resolution, (int, float))
                or isinstance(resolution, bool)
                or resolution <= 0
            ):
                _finding(
                    findings, "E_R2_CELL_SYSTEM_RESOLUTION", "R2_fixed_and_finite",
                    "Cell-system resolution must be a positive number.",
                    str(entry.get("path")), actual=resolution,
                )
        columns = entry.get("columns")
        if isinstance(columns, list):
            for column_index, column in enumerate(columns):
                if not isinstance(column, dict):
                    continue
                unknown_column = sorted(set(column) - COLUMN_SCHEMA_FIELDS)
                if unknown_column:
                    _finding(
                        findings, "E_MANIFEST_COLUMN_UNKNOWN_FIELD", "fail_closed",
                        "Column declaration contains fields outside schema version 1.",
                        str(entry.get("path")), column_index=column_index,
                        fields=unknown_column,
                    )


def _lint_table_contract(table: ParsedTable, findings: list[Finding]) -> None:
    entry = table.entry
    kind = entry.get("table_kind")
    if kind not in ALLOWED_TABLE_KINDS:
        _finding(
            findings, "E_R2_UNKNOWN_TABLE_KIND", "R2_fixed_and_finite",
            "Table kind is missing or not classified.", table.path, actual=kind,
        )
    elif kind == "whole_sample_scan":
        if entry.get("membership_partition") is not False:
            _finding(
                findings, "E_R2_SCAN_IS_MEMBERSHIP", "R2_fixed_and_finite",
                "Whole-sample scan points must not be object-membership cells.", table.path,
                actual=entry.get("membership_partition"),
            )
        whole_sample_n = entry.get("whole_sample_n")
        if not isinstance(whole_sample_n, int) or isinstance(whole_sample_n, bool) or whole_sample_n < MIN_K:
            _finding(
                findings, "E_R2_SCAN_SAMPLE_SIZE", "R2_fixed_and_finite",
                "Whole-sample scan must pin an integer whole_sample_n of at least 50.",
                table.path, actual=whole_sample_n,
            )
        if len(table.rows) > MAX_TABLE_CELLS:
            _finding(
                findings, "E_R2_SCAN_POINT_LIMIT", "R2_fixed_and_finite",
                "Whole-sample scan exceeds the finite 5,000-point surface limit.",
                table.path, points=len(table.rows), limit=MAX_TABLE_CELLS,
            )
    if entry.get("object_independent_cells") is not True:
        _finding(
            findings, "E_R2_OBJECT_DEPENDENT_CELLS", "R2_fixed_and_finite",
            "Cell definitions must be object-independent.", table.path,
        )
    if entry.get("cells_frozen_before_statistics") is not True:
        _finding(
            findings, "E_R2_TABLE_NOT_FROZEN", "R2_fixed_and_finite",
            "Table cells must be frozen before real-sky statistics.", table.path,
        )
    cell_system = entry.get("cell_system")
    valid_cell_system = (
        isinstance(cell_system, dict)
        and isinstance(cell_system.get("id"), str)
        and bool(cell_system.get("id"))
        and isinstance(cell_system.get("domain"), str)
        and bool(cell_system.get("domain"))
        and isinstance(cell_system.get("family"), str)
        and bool(cell_system.get("family"))
        and isinstance(cell_system.get("axes"), list)
        and bool(cell_system.get("axes"))
        and all(isinstance(axis, str) and axis for axis in cell_system.get("axes", []))
        and isinstance(cell_system.get("partition_kind"), str)
        and bool(cell_system.get("partition_kind"))
    )
    if not valid_cell_system:
        _finding(
            findings, "E_R2_CELL_SYSTEM_UNCLASSIFIED", "R2_fixed_and_finite",
            "Cell system requires nonempty id, domain, family, axes, and partition_kind.",
            table.path,
        )

    declared_columns = entry.get("columns")
    if not isinstance(declared_columns, list):
        return
    for item in declared_columns:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str):
            continue
        name = str(item["name"])
        role = item.get("role")
        quantity_class = item.get("quantity_class")
        data_type = item.get("data_type")
        if role not in ALLOWED_COLUMN_ROLES:
            _finding(
                findings, "E_R3_UNKNOWN_COLUMN_ROLE", "R3_study_result_only",
                "Column role is missing or cannot be classified.", table.path,
                column=name, actual=role,
            )
        if quantity_class not in ALLOWED_QUANTITY_CLASSES:
            _finding(
                findings, "E_R3_UNKNOWN_QUANTITY_CLASS", "R3_study_result_only",
                "Quantity class is missing or cannot be classified.", table.path,
                column=name, actual=quantity_class,
            )
        elif role in ROLE_CLASS_COMPATIBILITY and quantity_class not in ROLE_CLASS_COMPATIBILITY[role]:
            _finding(
                findings, "E_R3_ROLE_CLASS_MISMATCH", "R3_study_result_only",
                "Column role and quantity class are inconsistent.", table.path,
                column=name, role=role, quantity_class=quantity_class,
            )
        if data_type not in ALLOWED_DATA_TYPES:
            _finding(
                findings, "E_R3_UNKNOWN_DATA_TYPE", "R3_study_result_only",
                "Column data type is missing or unsupported.", table.path,
                column=name, actual=data_type,
            )
        elif role in ROLE_DATA_TYPE_COMPATIBILITY and data_type not in ROLE_DATA_TYPE_COMPATIBILITY[role]:
            _finding(
                findings, "E_R3_ROLE_DATA_TYPE", "R3_study_result_only",
                "Column role cannot use the declared data type.", table.path,
                column=name, role=role, data_type=data_type,
            )
        if (
            kind == "whole_sample_scan"
            and role in {"quantity", "uncertainty", "control"}
            and quantity_class not in {"whole_sample_statistic", "uncertainty", "control"}
        ):
            _finding(
                findings, "E_R3_SCAN_NOT_WHOLE_SAMPLE", "R3_study_result_only",
                "Scan result columns must be classified as whole-sample statistics or their uncertainty/control.",
                table.path, column=name, actual=quantity_class,
            )
        normalized = _normalize_name(name)
        approved_names = APPROVED_QUANTITY_NAMES_BY_CLASS.get(str(quantity_class))
        if role in {"quantity", "uncertainty", "control"} and approved_names is not None:
            approved_normalized = {_normalize_name(item) for item in approved_names}
            if normalized not in approved_normalized:
                _finding(
                    findings, "E_R3_UNAPPROVED_QUANTITY", "R3_study_result_only",
                    "Quantity name is outside the schema-version-pinned study-result registry.",
                    table.path, column=name, quantity_class=quantity_class,
                    approved=sorted(approved_names),
                )
        if role in {"quantity", "uncertainty", "control"} and SURVEY_ATTRIBUTE_RE.search(normalized):
            _finding(
                findings, "E_R3_SURVEY_ATTRIBUTE", "R3_study_result_only",
                "Aggregated re-tabulation of a survey attribute is forbidden.", table.path,
                column=name,
            )
        if role in {"quantity", "uncertainty", "control"} and SUSPICIOUS_QUANTITY_RE.fullmatch(normalized):
            _finding(
                findings, "E_R3_SUSPICIOUS_QUANTITY_NAME", "R3_study_result_only",
                "Generic payload-like quantity name cannot be classified as a study result.",
                table.path, column=name,
            )


def _lint_table_value_shapes(table: ParsedTable, findings: list[Finding]) -> None:
    declared = table.entry.get("columns")
    if not isinstance(declared, list):
        return
    schemas = {
        str(item.get("name")): item
        for item in declared
        if isinstance(item, dict) and isinstance(item.get("name"), str)
    }
    mask_names = [name for name, schema in schemas.items() if schema.get("role") == "mask"]
    mask_name = mask_names[0] if len(mask_names) == 1 else None
    for row_number, row in enumerate(table.rows, start=2):
        row_masked = (
            mask_name is not None
            and row.get(mask_name, "").strip().lower() == "true"
        )
        for name, schema in schemas.items():
            value = row.get(name, "")
            role = schema.get("role")
            data_type = schema.get("data_type")
            if value == "" and role in {"quantity", "uncertainty", "control"} and row_masked:
                continue
            valid = True
            if data_type == "integer":
                valid = re.fullmatch(r"[+-]?[0-9]+", value) is not None
            elif data_type == "number":
                try:
                    valid = bool(value) and math.isfinite(float(value))
                except ValueError:
                    valid = False
            elif data_type == "boolean":
                valid = value.strip().lower() in {"true", "false"}
            elif data_type == "string":
                valid = (
                    bool(value)
                    and len(value) <= 128
                    and not any(ord(char) < 32 for char in value)
                    and not value.lstrip().startswith(("{", "["))
                )
            else:
                continue
            if not valid:
                _finding(
                    findings, "E_R3_VALUE_SHAPE", "R3_study_result_only",
                    "Released cell value does not match its closed scalar data type.",
                    table.path, row=row_number, column=name, data_type=data_type,
                    preview=value[:80],
                )


def _lint_numeric_guardrails(table: ParsedTable, findings: list[Finding]) -> None:
    if table.entry.get("table_kind") != "ordinary_aggregate":
        return
    row_count = len(table.rows)
    if row_count == 0:
        _finding(
            findings, "E_G_EMPTY_TABLE", "numeric_guardrail",
            "Ordinary aggregate table must contain at least one cell.", table.path,
        )
    if row_count > MAX_TABLE_CELLS:
        _finding(
            findings, "E_G_TABLE_CELL_LIMIT", "numeric_guardrail",
            "Ordinary table exceeds the 5,000-cell limit.", table.path,
            cells=row_count, limit=MAX_TABLE_CELLS,
        )

    declared = table.entry.get("columns")
    if not isinstance(declared, list):
        return
    role_names: dict[str, list[str]] = {}
    for item in declared:
        if isinstance(item, dict) and isinstance(item.get("name"), str):
            role_names.setdefault(str(item.get("role")), []).append(str(item["name"]))
    k_columns = role_names.get("support_k", [])
    mask_columns = role_names.get("mask", [])
    if len(k_columns) != 1:
        _finding(
            findings, "E_G_K_COLUMN", "numeric_guardrail",
            "Ordinary table requires exactly one support_k column.", table.path,
            columns=k_columns,
        )
        return
    if len(mask_columns) != 1:
        _finding(
            findings, "E_G_MASK_COLUMN", "numeric_guardrail",
            "Ordinary table requires exactly one mask column.", table.path,
            columns=mask_columns,
        )
        return
    k_name = k_columns[0]
    mask_name = mask_columns[0]
    releasable_names = set(
        role_names.get("quantity", [])
        + role_names.get("uncertainty", [])
        + role_names.get("control", [])
    )
    for row_number, row in enumerate(table.rows, start=2):
        try:
            raw_k = row[k_name]
            if not re.fullmatch(r"[0-9]+", raw_k):
                raise ValueError("k is not a nonnegative integer")
            support = int(raw_k)
        except (KeyError, ValueError) as exc:
            _finding(
                findings, "E_G_K_UNPARSEABLE", "numeric_guardrail",
                "support_k value must be a nonnegative base-10 integer.", table.path,
                row=row_number, error=str(exc),
            )
            continue
        raw_mask = row.get(mask_name, "").strip().lower()
        if raw_mask not in {"true", "false"}:
            _finding(
                findings, "E_G_MASK_UNPARSEABLE", "numeric_guardrail",
                "Mask value must be exactly true or false.", table.path,
                row=row_number, actual=row.get(mask_name),
            )
            continue
        masked = raw_mask == "true"
        if support < MIN_K and not masked:
            _finding(
                findings, "E_G_K_FLOOR", "numeric_guardrail",
                "Sub-threshold ordinary cell is not masked.", table.path,
                row=row_number, k=support, minimum=MIN_K,
            )
        if masked:
            leaked = {
                name: row.get(name, "")
                for name in sorted(releasable_names)
                if row.get(name, "").strip().upper() not in {"", "MASKED", "NA", "NULL"}
            }
            if leaked:
                _finding(
                    findings, "E_G_MASK_LEAK", "numeric_guardrail",
                    "Masked cell still releases a result, uncertainty, or control value.",
                    table.path, row=row_number, columns=sorted(leaked),
                )


def _column_names_by_role(table: ParsedTable) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    declared = table.entry.get("columns")
    if not isinstance(declared, list):
        return result
    for item in declared:
        if isinstance(item, dict) and isinstance(item.get("name"), str):
            result.setdefault(str(item.get("role")), []).append(str(item["name"]))
    return result


def _table_quantities(table: ParsedTable) -> set[str]:
    by_role = _column_names_by_role(table)
    quantities = {
        _normalize_name(name)
        for role in ("quantity", "uncertainty", "control")
        for name in by_role.get(role, [])
    }
    if by_role.get("support_k"):
        quantities.add("__support_k__")
    return quantities


def _cell_systems_related(first: dict[str, Any], second: dict[str, Any]) -> bool:
    # Public metadata cannot prove that two row-membership systems are disjoint.
    # Treat every pair as potentially related; otherwise a producer could defeat
    # the detector merely by changing self-declared domain/axis strings.
    return bool(first) and bool(second)


def _unmasked_subthreshold_rows(table: ParsedTable) -> list[int]:
    by_role = _column_names_by_role(table)
    if len(by_role.get("support_k", [])) != 1 or len(by_role.get("mask", [])) != 1:
        return [-1]
    k_name = by_role["support_k"][0]
    mask_name = by_role["mask"][0]
    failures: list[int] = []
    for row_number, row in enumerate(table.rows, start=2):
        raw_k = row.get(k_name, "")
        raw_mask = row.get(mask_name, "").strip().lower()
        if not re.fullmatch(r"[0-9]+", raw_k) or raw_mask not in {"true", "false"}:
            failures.append(row_number)
        elif int(raw_k) < MIN_K and raw_mask == "false":
            failures.append(row_number)
    return failures


def _lint_cumulative_rules(tables: list[ParsedTable], findings: list[Finding]) -> dict[str, Any]:
    ordinary = [table for table in tables if table.entry.get("table_kind") == "ordinary_aggregate"]
    for index, first in enumerate(ordinary):
        first_system = first.entry.get("cell_system")
        if not isinstance(first_system, dict):
            continue
        for second in ordinary[index + 1 :]:
            second_system = second.entry.get("cell_system")
            if not isinstance(second_system, dict) or not _cell_systems_related(first_system, second_system):
                continue
            shared = sorted(_table_quantities(first).intersection(_table_quantities(second)))
            if not shared:
                continue
            _finding(
                findings, "E_R4_RELATED_CELL_SYSTEMS", "R4_non_reconstructable",
                "Distinct cell-system tables release shared quantities without machine-verifiable disjointness.",
                first.path, other_path=second.path,
                first_system=first_system.get("id"), second_system=second_system.get("id"),
                shared_quantities=shared,
            )
            first_resolution = first_system.get("resolution")
            second_resolution = second_system.get("resolution")
            if (
                first_system.get("family") == second_system.get("family")
                and isinstance(first_resolution, (int, float))
                and isinstance(second_resolution, (int, float))
                and first_resolution != second_resolution
            ):
                finer = first if first_resolution > second_resolution else second
                bad_rows = _unmasked_subthreshold_rows(finer)
                if bad_rows:
                    _finding(
                        findings, "E_R4_REFINEMENT_K", "R4_non_reconstructable",
                        "The implied finest nested system has an unmasked or unverifiable cell below k=50.",
                        finer.path, rows=bad_rows[:20], total_bad_rows=len(bad_rows),
                    )

    system_cells: dict[str, set[str]] = {}
    for table in ordinary:
        by_role = _column_names_by_role(table)
        cell_columns = by_role.get("cell_id", [])
        if len(cell_columns) != 1:
            _finding(
                findings, "E_R5_CELL_ID_SCHEMA", "R5_non_substitutive",
                "Ordinary table requires exactly one aggregate cell_id column.",
                table.path, columns=cell_columns,
            )
            continue
        cell_name = cell_columns[0]
        system = table.entry.get("cell_system")
        system_id = system.get("id") if isinstance(system, dict) else None
        if not isinstance(system_id, str) or not system_id:
            continue
        seen_in_table: set[str] = set()
        for row_number, row in enumerate(table.rows, start=2):
            cell_id = row.get(cell_name, "").strip()
            if not cell_id:
                _finding(
                    findings, "E_R5_EMPTY_CELL_ID", "R5_non_substitutive",
                    "Aggregate cell identifier is empty.", table.path, row=row_number,
                )
            elif cell_id in seen_in_table:
                _finding(
                    findings, "E_R5_DUPLICATE_CELL_ID", "R5_non_substitutive",
                    "Aggregate cell identifier is duplicated within a table.",
                    table.path, row=row_number, cell_id=cell_id,
                )
            else:
                seen_in_table.add(cell_id)
                system_cells.setdefault(system_id, set()).add(cell_id)

        family = str(system.get("family", "")) if isinstance(system, dict) else ""
        normalized_header = {_normalize_name(name) for name in table.header}
        if (
            len(table.rows) >= 100_000
            or "brick" in family.lower()
            or bool(normalized_header.intersection({"brickid", "brickname"}))
        ):
            _finding(
                findings, "E_R5_CATALOGUE_SCALE", "R5_non_substitutive",
                "Table has catalogue-scale or per-brick lookup shape.", table.path,
                rows=len(table.rows), family=family,
            )

    cumulative_cells = sum(len(cells) for cells in system_cells.values())
    if cumulative_cells > MAX_CUMULATIVE_CELLS:
        _finding(
            findings, "E_R5_CUMULATIVE_CELL_BUDGET", "R5_non_substitutive",
            "Complete package exceeds the 5,000 unique ordinary-cell budget.",
            MANIFEST_NAME, cells=cumulative_cells, limit=MAX_CUMULATIVE_CELLS,
            systems={key: len(value) for key, value in sorted(system_cells.items())},
        )
    return {
        "ordinary_tables": len(ordinary),
        "ordinary_unique_cells_cumulative": cumulative_cells,
        "ordinary_cell_systems": {key: len(value) for key, value in sorted(system_cells.items())},
    }


def _lint_image_compliance(
    package: Path, entry: dict[str, Any], findings: list[Finding]
) -> None:
    rel = _safe_relative_path(entry.get("path"))
    if rel is None:
        return
    rel_text = rel.as_posix()
    path = package / rel
    if not path.is_file():
        return
    try:
        data = path.read_bytes()
    except OSError as exc:
        _finding(
            findings, "E_R6_IMAGE_UNREADABLE", "R6_separate_image_compliance",
            "Image bytes cannot be read for type verification.", rel_text, error=str(exc),
        )
        return
    suffix = path.suffix.lower()
    valid_magic = (
        suffix == ".png" and data.startswith(b"\x89PNG\r\n\x1a\n")
    ) or (
        suffix in {".jpg", ".jpeg"}
        and data.startswith(b"\xff\xd8\xff")
        and data.endswith(b"\xff\xd9")
    )
    if not valid_magic:
        _finding(
            findings, "E_R6_IMAGE_MAGIC", "R6_separate_image_compliance",
            "Image extension and file signature do not agree.", rel_text,
        )

    contains_source_pixels = entry.get("contains_source_pixels")
    if not isinstance(contains_source_pixels, bool):
        _finding(
            findings, "E_R6_IMAGE_UNCLASSIFIED", "R6_separate_image_compliance",
            "Image must declare contains_source_pixels as true or false.", rel_text,
        )
        return
    if contains_source_pixels:
        required_nonempty = ("image_layer", "licence_id", "licence_url", "credit_text")
        missing = [
            key for key in required_nonempty
            if not isinstance(entry.get(key), str) or not str(entry.get(key)).strip()
        ]
        valid_modification = entry.get("modification_status") in {
            "unmodified", "modified_and_indicated",
        }
        if missing or entry.get("credit_visible") is not True or not valid_modification:
            _finding(
                findings, "E_R6_IMAGE_COMPLIANCE", "R6_separate_image_compliance",
                "Source-pixel image lacks a complete layer-specific licence and visible-credit route.",
                rel_text, missing=missing,
                credit_visible=entry.get("credit_visible"),
                modification_status=entry.get("modification_status"),
            )
        route_matches = (
            entry.get("image_layer") in ALLOWED_SOURCE_IMAGE_LAYERS
            and entry.get("licence_id") == LEGACY_LICENCE_ID
            and entry.get("licence_url") == LEGACY_LICENCE_URL
            and entry.get("credit_text") == LEGACY_CREDIT
        )
        if not route_matches:
            _finding(
                findings, "E_R6_IMAGE_ROUTE", "R6_separate_image_compliance",
                "Source-pixel metadata does not match the closed Legacy Surveys licence/credit route.",
                rel_text, image_layer=entry.get("image_layer"),
                licence_id=entry.get("licence_id"),
                licence_url=entry.get("licence_url"),
                credit_text=entry.get("credit_text"),
            )
    elif entry.get("image_origin") not in {
        "original_study_visualization", "synthetic_instrument_visualization",
    }:
        _finding(
            findings, "E_R6_IMAGE_ORIGIN", "R6_separate_image_compliance",
            "Non-source-pixel image must declare an allowed original or synthetic origin.",
            rel_text, actual=entry.get("image_origin"),
        )


def _literal_contains_object_record(value: Any, *, allow_synthetic: bool = False) -> bool:
    if isinstance(value, dict):
        normalized = {
            _normalize_name(str(key)): item
            for key, item in value.items()
            if isinstance(key, (str, int, float))
        }
        matched = set(normalized).intersection(
            IDENTIFIER_NAMES | COORDINATE_NAMES | PER_OBJECT_DERIVED_NAMES
        )
        concrete = {
            key for key in matched
            if not (
                isinstance(normalized[key], str)
                and _normalize_name(normalized[key]) == key
            )
        }
        synthetic_identifier = any(
            key in IDENTIFIER_NAMES
            and isinstance(normalized[key], str)
            and _normalize_name(normalized[key]).startswith("synth")
            for key in concrete
        )
        if allow_synthetic and synthetic_identifier:
            return any(
                _literal_contains_object_record(item, allow_synthetic=allow_synthetic)
                for key, item in value.items()
                if _normalize_name(str(key)) not in matched
            )
        strong_identifiers = concrete.intersection(IDENTIFIER_NAMES - {"source", "release"})
        if len(concrete) >= 2 or strong_identifiers:
            return True
        return any(
            _literal_contains_object_record(item, allow_synthetic=allow_synthetic)
            for item in value.values()
        )
    if isinstance(value, (list, tuple)):
        return any(
            _literal_contains_object_record(item, allow_synthetic=allow_synthetic)
            for item in value
        )
    return False


def _lint_delimited_text_payload(
    lines: list[str], rel_text: str, findings: list[Finding]
) -> bool:
    forbidden = IDENTIFIER_NAMES | COORDINATE_NAMES | PER_OBJECT_DERIVED_NAMES
    for delimiter in (",", "\t", "|"):
        for header_index, raw_header in enumerate(lines):
            header = [part.strip() for part in raw_header.strip("|").split(delimiter)]
            if len(header) < 2:
                continue
            normalized_header = {_normalize_name(part) for part in header}
            matched = normalized_header.intersection(forbidden)
            if not matched:
                continue
            data_like = 0
            for line in lines[header_index + 1 : header_index + 102]:
                fields = [part.strip() for part in line.strip("|").split(delimiter)]
                if len(fields) != len(header):
                    continue
                if all(re.fullmatch(r":?-{3,}:?", field) for field in fields):
                    continue
                data_like += 1
            if data_like:
                _finding(
                    findings, "E_R1_DISGUISED_TABLE", "R1_rowless",
                    "Non-table file has a row shape with object-like header fields.",
                    rel_text, delimiter=repr(delimiter), header_line=header_index + 1,
                    data_rows_detected=data_like,
                    forbidden_header_fields=sorted(matched),
                )
                return True
    return False


def _lint_non_table_payload(
    package: Path, entry: dict[str, Any], findings: list[Finding]
) -> None:
    rel = _safe_relative_path(entry.get("path"))
    if rel is None:
        return
    rel_text = rel.as_posix()
    path = package / rel
    try:
        size = path.stat().st_size
        if size > 5_000_000:
            _finding(
                findings, "E_FILE_TEXT_SIZE", "fail_closed",
                "Text-role file exceeds the 5 MB closed-parser limit.",
                rel_text, bytes=size, limit=5_000_000,
            )
            return
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        _finding(
            findings, "E_FILE_UNPARSEABLE_TEXT", "fail_closed",
            "Non-table file is not readable strict UTF-8 text.", rel_text, error=str(exc),
        )
        return

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if entry.get("role") == "commitment" and rel.suffix.lower() == ".sha256":
        malformed = [index for index, line in enumerate(lines, start=1) if not SHA256_LINE_RE.fullmatch(line)]
        if malformed or len(lines) > 100:
            _finding(
                findings, "E_COMMITMENT_SHAPE", "fail_closed",
                "Commitment file must contain at most 100 canonical SHA-256 artifact commitments.",
                rel_text, malformed_lines=malformed[:20], lines=len(lines), limit=100,
            )
        return

    hash_literals = re.findall(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", text.lower())
    if len(hash_literals) > 100:
        _finding(
            findings, "E_R1_ROW_HASH_PAYLOAD", "R1_rowless",
            "Non-table file contains more hashes than the bounded artifact-commitment route permits.",
            rel_text, hashes=len(hash_literals), limit=100,
        )

    if rel.suffix.lower() != ".py":
        _lint_delimited_text_payload(lines, rel_text, findings)

    parsed_literal: Any = None
    if rel.suffix.lower() == ".json":
        try:
            parsed_literal = json.loads(text)
        except json.JSONDecodeError as exc:
            _finding(
                findings, "E_FILE_UNPARSEABLE_JSON", "fail_closed",
                "JSON-role file is not valid JSON.", rel_text, error=str(exc),
            )
            return
    elif rel.suffix.lower() == ".py":
        try:
            tree = ast.parse(text, filename=rel_text)
        except SyntaxError as exc:
            _finding(
                findings, "E_FILE_UNPARSEABLE_CODE", "fail_closed",
                "Python code file is not parseable.", rel_text, error=str(exc),
            )
            return
        literals: list[Any] = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.Dict, ast.List, ast.Tuple, ast.Set)):
                try:
                    literals.append(ast.literal_eval(node))
                except (ValueError, TypeError, SyntaxError):
                    continue
        parsed_literal = literals

    allow_synthetic = entry.get("role") == "code"
    if parsed_literal is not None and _literal_contains_object_record(
        parsed_literal, allow_synthetic=allow_synthetic
    ):
        _finding(
            findings, "E_R1_EMBEDDED_OBJECT_RECORD", "R1_rowless",
            "Non-table structured payload contains embedded object-like records.", rel_text,
        )
        return

    assignment_re = re.compile(
        r"(?:^|[,{\s])[\"']?"
        r"(objid|objectid|sourceid|targetid|catalogid|ra|dec|label|score|chirality|handedness)"
        r"[\"']?\s*[:=]\s*[\"']?([^,}\]\s\"']+)",
        re.IGNORECASE | re.MULTILINE,
    )
    assignment_matches = [] if rel.suffix.lower() == ".py" else assignment_re.findall(text)
    for key, value in assignment_matches:
        normalized_value = _normalize_name(value)
        synthetic_code_value = allow_synthetic and normalized_value.startswith("synth")
        if _normalize_name(key) != normalized_value and not synthetic_code_value:
            _finding(
                findings, "E_R1_EMBEDDED_OBJECT_RECORD", "R1_rowless",
                "Non-table text contains an object-field assignment to a concrete value.",
                rel_text, field=key,
            )
            return


def _validate_file_inventory(
    package: Path, manifest: dict[str, Any], findings: list[Finding]
) -> list[dict[str, Any]]:
    raw_entries = manifest.get("files")
    if not isinstance(raw_entries, list):
        _finding(
            findings,
            "E_MANIFEST_SCHEMA",
            "fail_closed",
            "Manifest field 'files' must be an array.",
            MANIFEST_NAME,
        )
        return []

    entries: list[dict[str, Any]] = []
    listed: set[str] = set()
    for index, raw in enumerate(raw_entries):
        if not isinstance(raw, dict):
            _finding(
                findings,
                "E_MANIFEST_SCHEMA",
                "fail_closed",
                "Each file entry must be an object.",
                MANIFEST_NAME,
                entry_index=index,
            )
            continue
        rel = _safe_relative_path(raw.get("path"))
        if rel is None:
            _finding(
                findings,
                "E_MANIFEST_PATH",
                "fail_closed",
                "File path is empty, absolute, backslash-based, or traverses directories.",
                MANIFEST_NAME,
                entry_index=index,
            )
            continue
        rel_text = rel.as_posix()
        if rel_text == MANIFEST_NAME or rel_text in listed:
            _finding(
                findings,
                "E_MANIFEST_DUPLICATE_PATH",
                "fail_closed",
                "Manifest file paths must be unique and must not list the manifest itself.",
                rel_text,
            )
            continue
        listed.add(rel_text)

        role = raw.get("role")
        if role not in ALLOWED_ROLES:
            _finding(
                findings,
                "E_FILE_UNKNOWN_ROLE",
                "fail_closed",
                "Unknown file role.",
                rel_text,
                role=role,
            )
        elif rel.suffix.lower() not in ROLE_EXTENSIONS[role]:
            _finding(
                findings,
                "E_FILE_UNKNOWN_TYPE",
                "fail_closed",
                "File extension is not allowed for its declared role.",
                rel_text,
                role=role,
                extension=rel.suffix.lower(),
            )

        target = package / rel
        if target.is_symlink():
            _finding(
                findings,
                "E_FILE_SYMLINK",
                "fail_closed",
                "Symlinks are not permitted in a release package.",
                rel_text,
            )
        elif not target.is_file():
            _finding(
                findings,
                "E_MANIFEST_FILE_MISSING",
                "fail_closed",
                "Manifest-listed file is absent or not a regular file.",
                rel_text,
            )
        else:
            expected_hash = raw.get("sha256")
            if not isinstance(expected_hash, str) or not SHA256_RE.fullmatch(expected_hash):
                _finding(
                    findings,
                    "E_MANIFEST_HASH_INVALID",
                    "fail_closed",
                    "Each file must have a full lowercase SHA-256 pin.",
                    rel_text,
                )
            else:
                actual_hash = file_sha256(target)
                if actual_hash != expected_hash:
                    _finding(
                        findings,
                        "E_MANIFEST_HASH_MISMATCH",
                        "fail_closed",
                        "File bytes do not match the manifest pin.",
                        rel_text,
                        expected=expected_hash,
                        actual=actual_hash,
                    )
        entries.append(raw)

    actual_files: set[str] = set()
    try:
        for path in package.rglob("*"):
            if path.is_file() or path.is_symlink():
                rel_text = path.relative_to(package).as_posix()
                if rel_text != MANIFEST_NAME:
                    actual_files.add(rel_text)
    except OSError as exc:
        _finding(
            findings,
            "E_PACKAGE_UNREADABLE",
            "fail_closed",
            "Package tree could not be enumerated completely.",
            evidence_error=str(exc),
        )
        return entries

    for rel_text in sorted(actual_files - listed):
        _finding(
            findings,
            "E_MANIFEST_UNLISTED_FILE",
            "fail_closed",
            "File exists in package but is absent from the manifest.",
            rel_text,
        )
    for rel_text in sorted(listed - actual_files):
        if not any(item.path == rel_text for item in findings):
            _finding(
                findings,
                "E_MANIFEST_FILE_MISSING",
                "fail_closed",
                "Manifest-listed file does not exist in the enumerated package.",
                rel_text,
            )
    return entries


def lint_package(package: Path | str) -> LintResult:
    package_path = Path(package).resolve()
    findings: list[Finding] = []
    if not package_path.is_dir():
        _finding(
            findings,
            "E_PACKAGE_NOT_DIRECTORY",
            "fail_closed",
            "Package path is not a readable directory.",
            str(package),
        )
        return LintResult(str(package_path), False, findings)

    manifest = _load_manifest(package_path, findings)
    entries: list[dict[str, Any]] = []
    tables: list[ParsedTable] = []
    if manifest is not None:
        if manifest.get("schema_version") != SCHEMA_VERSION:
            _finding(
                findings,
                "E_MANIFEST_VERSION",
                "fail_closed",
                "Unsupported or missing manifest schema version.",
                MANIFEST_NAME,
                supported=SCHEMA_VERSION,
                actual=manifest.get("schema_version"),
            )
        _lint_closed_manifest_schema(manifest, findings)
        _lint_fixed_finite_manifest(manifest, findings)
        entries = _validate_file_inventory(package_path, manifest, findings)
        for entry in entries:
            if entry.get("role") == "table":
                table = _parse_table(package_path, entry, findings)
                if table is not None:
                    tables.append(table)
                    _lint_rowless(table, findings)
                    _lint_table_contract(table, findings)
                    _lint_table_value_shapes(table, findings)
            elif entry.get("role") == "image":
                _lint_image_compliance(package_path, entry, findings)
            elif entry.get("role") in {"documentation", "code", "environment", "commitment"}:
                _lint_non_table_payload(package_path, entry, findings)

        cumulative_metrics = _lint_cumulative_rules(tables, findings)
        controlling_or_custody_failure = bool(findings)
        if not controlling_or_custody_failure:
            for table in tables:
                _lint_numeric_guardrails(table, findings)
    else:
        cumulative_metrics = {}

    return LintResult(
        package=str(package_path),
        accepted=not findings,
        findings=findings,
        metrics={"manifest_entries": len(entries), "parsed_tables": len(tables), **cumulative_metrics},
    )


SELFTEST_PNG_1X1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
)
SELFTEST_EXPECTATIONS: list[tuple[str, bool, set[str]]] = [
    ("bad_per_object_row_file", False, {
        "E_R1_IDENTIFIER_COLUMN", "E_R1_PER_OBJECT_DERIVED_COLUMN",
        "E_R3_UNAPPROVED_QUANTITY", "E_R3_VALUE_SHAPE",
    }),
    ("bad_per_brick_270577", False, {
        "E_R1_IDENTIFIER_COLUMN", "E_R5_CATALOGUE_SCALE", "E_R5_CUMULATIVE_CELL_BUDGET",
    }),
    ("bad_ra_dec", False, {"E_R1_COORDINATE_COLUMN", "E_R3_VALUE_SHAPE"}),
    ("bad_nside32_nside64_overlap", False, {"E_R4_RELATED_CELL_SYSTEMS"}),
    ("bad_refinement_finest_k", False, {"E_R4_REFINEMENT_K", "E_R4_RELATED_CELL_SYSTEMS"}),
    ("bad_cumulative_cell_budget", False, {
        "E_R4_RELATED_CELL_SYSTEMS", "E_R5_CUMULATIVE_CELL_BUDGET",
    }),
    ("bad_mean_survey_magnitude", False, {
        "E_R3_SURVEY_ATTRIBUTE", "E_R3_UNAPPROVED_QUANTITY",
    }),
    ("bad_low_k_unmasked", False, {"E_G_K_FLOOR"}),
    ("bad_rule2_dynamic_interface", False, {"E_R2_DYNAMIC_QUERY"}),
    ("bad_rule6_image_missing_compliance", False, {"E_R6_IMAGE_COMPLIANCE", "E_R6_IMAGE_ROUTE"}),
    ("bad_manifest_symlink", False, {"E_MANIFEST_SYMLINK"}),
    ("bad_environment_cached_object_rows", False, {"E_R1_EMBEDDED_OBJECT_RECORD"}),
    ("bad_string_payload_quantity", False, {
        "E_R3_ROLE_DATA_TYPE", "E_R3_SUSPICIOUS_QUANTITY_NAME",
        "E_R3_UNAPPROVED_QUANTITY", "E_R3_VALUE_SHAPE",
    }),
    ("bad_rule6_asserted_bogus_route", False, {"E_R6_IMAGE_ROUTE"}),
    ("bad_unknown_file_type", False, {"E_FILE_UNKNOWN_TYPE"}),
    ("bad_unknown_quantity_class", False, {"E_R3_UNKNOWN_QUANTITY_CLASS"}),
    ("bad_object_precision_float_pair", False, {
        "E_R1_OBJECT_PRECISION_FLOAT_PAIR", "E_R3_VALUE_SHAPE",
    }),
    ("bad_unlisted_auxiliary_file", False, {"E_MANIFEST_UNLISTED_FILE"}),
    ("good_s1_nside32_masked_maps", True, set()),
    ("good_67_partition_table", True, set()),
    ("good_9_hand_check_strata", True, set()),
    ("good_nside16_scan_surface", True, set()),
]


def _selftest_write_csv(path: Path, header: list[str], rows: Iterable[Sequence[object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def _selftest_system(
    system_id: str,
    *,
    domain: Optional[str] = None,
    family: str = "fixed_partition",
    resolution: int = 1,
    axis: str = "synthetic_axis",
) -> dict[str, Any]:
    return {
        "id": system_id,
        "domain": domain or system_id,
        "family": family,
        "resolution": resolution,
        "axes": [axis],
        "partition_kind": family,
    }


def _selftest_standard_columns(quantity_name: str = "mean_sign") -> list[dict[str, str]]:
    return [
        {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
        {"name": "k", "role": "support_k", "quantity_class": "study_count"},
        {"name": "masked", "role": "mask", "quantity_class": "mask"},
        {"name": quantity_name, "role": "quantity", "quantity_class": "study_estimand"},
    ]


def _selftest_table_entry(
    path: Path,
    columns: list[dict[str, str]],
    *,
    cell_system: Optional[dict[str, Any]] = None,
    table_kind: str = "ordinary_aggregate",
    **metadata: Any,
) -> dict[str, Any]:
    typed_columns: list[dict[str, str]] = []
    for original in columns:
        column = dict(original)
        if "data_type" not in column:
            role = column.get("role")
            quantity_class = column.get("quantity_class")
            if role == "support_k" or quantity_class == "study_count":
                column["data_type"] = "integer"
            elif role == "mask":
                column["data_type"] = "boolean"
            elif role == "cell_id":
                column["data_type"] = "string"
            elif role == "axis":
                column["data_type"] = "integer"
            else:
                column["data_type"] = "number"
        typed_columns.append(column)
    entry: dict[str, Any] = {
        "path": path.name,
        "role": "table",
        "sha256": file_sha256(path),
        "table_kind": table_kind,
        "object_independent_cells": True,
        "cells_frozen_before_statistics": True,
        "columns": typed_columns,
        "cell_system": cell_system or _selftest_system("synthetic_partition_v1"),
    }
    entry.update(metadata)
    return entry


def _selftest_write_manifest(
    package: Path, entries: list[dict[str, Any]], **overrides: Any
) -> None:
    manifest: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "package_id": package.name,
        "schema_frozen_before_statistics": True,
        "cells_frozen_before_statistics": True,
        "dynamic_query_interface": False,
        "unlimited_slicing": False,
        "files": entries,
    }
    manifest.update(overrides)
    (package / MANIFEST_NAME).write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def _build_selftest_fixture(package: Path, fixture: str) -> None:
    package.mkdir(parents=True)
    standard_header = ["cell_id", "k", "masked", "mean_sign"]
    standard_columns = _selftest_standard_columns()

    if fixture == "bad_per_object_row_file":
        table = package / "objects.csv"
        _selftest_write_csv(table, ["objid", "label", "score"], [["SYNTH-1", "L", 0.9]])
        columns = [
            {"name": "objid", "role": "cell_id", "quantity_class": "cell_definition"},
            {"name": "label", "role": "quantity", "quantity_class": "study_estimand"},
            {"name": "score", "role": "quantity", "quantity_class": "instrument_summary"},
        ]
        _selftest_write_manifest(package, [_selftest_table_entry(table, columns)])
    elif fixture == "bad_per_brick_270577":
        table = package / "per_brick.csv"
        rows = ((f"BRICK-{index:06d}", 60, False, 0.0) for index in range(270_577))
        _selftest_write_csv(table, ["brickid", "k", "masked", "mean_sign"], rows)
        columns = [
            {"name": "brickid", "role": "cell_id", "quantity_class": "cell_definition"},
            *standard_columns[1:],
        ]
        system = _selftest_system(
            "per_brick_lookup", domain="synthetic_bricks", family="per_brick_lookup", axis="brick"
        )
        _selftest_write_manifest(package, [_selftest_table_entry(table, columns, cell_system=system)])
    elif fixture == "bad_ra_dec":
        table = package / "coordinates.csv"
        _selftest_write_csv(
            table, ["cell_id", "ra", "dec", "k", "masked"],
            [["A", 123.1, -4.2, 60, False]],
        )
        columns = [
            {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
            {"name": "ra", "role": "axis", "quantity_class": "cell_definition"},
            {"name": "dec", "role": "axis", "quantity_class": "cell_definition"},
            {"name": "k", "role": "support_k", "quantity_class": "study_count"},
            {"name": "masked", "role": "mask", "quantity_class": "mask"},
        ]
        _selftest_write_manifest(package, [_selftest_table_entry(table, columns)])
    elif fixture in {"bad_nside32_nside64_overlap", "bad_refinement_finest_k"}:
        coarse = package / "nside32.csv"
        fine = package / "nside64.csv"
        fine_k = 40 if fixture == "bad_refinement_finest_k" else 60
        _selftest_write_csv(coarse, standard_header, [["C0", 120, False, 0.1]])
        _selftest_write_csv(fine, standard_header, [["F0", fine_k, False, 0.2]])
        coarse_system = _selftest_system(
            "nside32", domain="synthetic_sky", family="healpix", resolution=32, axis="sky"
        )
        fine_system = _selftest_system(
            "nside64", domain="invented_domain", family="healpix", resolution=64,
            axis="invented_axis",
        )
        _selftest_write_manifest(
            package,
            [
                _selftest_table_entry(coarse, standard_columns, cell_system=coarse_system),
                _selftest_table_entry(fine, standard_columns, cell_system=fine_system),
            ],
        )
    elif fixture == "bad_cumulative_cell_budget":
        first = package / "first.csv"
        second = package / "second.csv"
        _selftest_write_csv(
            first, standard_header,
            ((f"A{index:04d}", 60, False, 0.0) for index in range(2501)),
        )
        _selftest_write_csv(
            second, standard_header,
            ((f"B{index:04d}", 60, False, 0.0) for index in range(2500)),
        )
        _selftest_write_manifest(
            package,
            [
                _selftest_table_entry(
                    first, standard_columns,
                    cell_system=_selftest_system("independent_A", axis="axis_A"),
                ),
                _selftest_table_entry(
                    second, standard_columns,
                    cell_system=_selftest_system("independent_B", axis="axis_B"),
                ),
            ],
        )
    elif fixture == "bad_mean_survey_magnitude":
        table = package / "survey_attribute.csv"
        _selftest_write_csv(
            table, ["cell_id", "k", "masked", "mean_magnitude"],
            [["A", 60, False, 20.1]],
        )
        _selftest_write_manifest(
            package, [_selftest_table_entry(table, _selftest_standard_columns("mean_magnitude"))]
        )
    elif fixture == "bad_low_k_unmasked":
        table = package / "low_k.csv"
        _selftest_write_csv(table, standard_header, [["A", 49, False, 0.1]])
        _selftest_write_manifest(package, [_selftest_table_entry(table, standard_columns)])
    elif fixture == "bad_rule2_dynamic_interface":
        document = package / "README.md"
        document.write_text("Synthetic dynamic-interface fixture.\n", encoding="utf-8")
        entry = {"path": document.name, "role": "documentation", "sha256": file_sha256(document)}
        _selftest_write_manifest(package, [entry], dynamic_query_interface=True)
    elif fixture == "bad_rule6_image_missing_compliance":
        image = package / "source.png"
        image.write_bytes(SELFTEST_PNG_1X1)
        entry = {
            "path": image.name,
            "role": "image",
            "sha256": file_sha256(image),
            "contains_source_pixels": True,
        }
        _selftest_write_manifest(package, [entry])
    elif fixture == "bad_manifest_symlink":
        external = package.parent / "synthetic_external_manifest.json"
        external.write_text(
            json.dumps({
                "schema_version": SCHEMA_VERSION,
                "package_id": "synthetic-external",
                "schema_frozen_before_statistics": True,
                "cells_frozen_before_statistics": True,
                "dynamic_query_interface": False,
                "unlimited_slicing": False,
                "files": [],
            }),
            encoding="utf-8",
        )
        (package / MANIFEST_NAME).symlink_to(external)
    elif fixture == "bad_environment_cached_object_rows":
        environment = package / "environment.json"
        environment.write_text(
            json.dumps({"cached_rows": [{"objid": "SYNTH-1", "ra": 12.3, "dec": -4.5}]}),
            encoding="utf-8",
        )
        entry = {"path": environment.name, "role": "environment", "sha256": file_sha256(environment)}
        _selftest_write_manifest(package, [entry])
    elif fixture == "bad_string_payload_quantity":
        table = package / "payload.csv"
        _selftest_write_csv(
            table, ["cell_id", "k", "masked", "payload"],
            [["A", 60, False, '{"objid":"SYNTH-1","ra":12.3}']],
        )
        columns = _selftest_standard_columns("payload")
        columns[-1]["data_type"] = "string"
        _selftest_write_manifest(package, [_selftest_table_entry(table, columns)])
    elif fixture == "bad_rule6_asserted_bogus_route":
        image = package / "source.png"
        image.write_bytes(SELFTEST_PNG_1X1)
        entry = {
            "path": image.name,
            "role": "image",
            "sha256": file_sha256(image),
            "contains_source_pixels": True,
            "image_layer": "x",
            "licence_id": "x",
            "licence_url": "x",
            "credit_text": "x",
            "credit_visible": True,
            "modification_status": "unmodified",
        }
        _selftest_write_manifest(package, [entry])
    elif fixture == "bad_unknown_file_type":
        payload = package / "payload.bin"
        payload.write_bytes(b"synthetic unknown type\n")
        entry = {"path": payload.name, "role": "documentation", "sha256": file_sha256(payload)}
        _selftest_write_manifest(package, [entry])
    elif fixture == "bad_unknown_quantity_class":
        table = package / "unknown.csv"
        _selftest_write_csv(table, ["cell_id", "k", "masked", "mystery"], [["A", 60, False, 1.0]])
        columns = _selftest_standard_columns("mystery")
        columns[-1]["quantity_class"] = "unknown"
        _selftest_write_manifest(package, [_selftest_table_entry(table, columns)])
    elif fixture == "bad_object_precision_float_pair":
        table = package / "hidden_coordinates.csv"
        rows = [
            ["A", "123.12345678", "-4.12345678", 60, False],
            ["B", "124.23456789", "-3.23456789", 60, False],
            ["C", "125.34567891", "-2.34567891", 60, False],
        ]
        _selftest_write_csv(table, ["cell_id", "axis_x", "axis_y", "k", "masked"], rows)
        columns = [
            {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
            {"name": "axis_x", "role": "axis", "quantity_class": "cell_definition"},
            {"name": "axis_y", "role": "axis", "quantity_class": "cell_definition"},
            {"name": "k", "role": "support_k", "quantity_class": "study_count"},
            {"name": "masked", "role": "mask", "quantity_class": "mask"},
        ]
        _selftest_write_manifest(package, [_selftest_table_entry(table, columns)])
    elif fixture == "bad_unlisted_auxiliary_file":
        document = package / "README.md"
        document.write_text("Synthetic listed file.\n", encoding="utf-8")
        (package / "unlisted.bin").write_bytes(b"synthetic unlisted file\n")
        entry = {"path": document.name, "role": "documentation", "sha256": file_sha256(document)}
        _selftest_write_manifest(package, [entry])
    elif fixture == "good_s1_nside32_masked_maps":
        table = package / "s1_nside32.csv"
        header = [
            "cell_id", "k", "masked", "accepted_count", "abstention_fraction",
            "mean_sign", "sensitivity",
        ]
        rows = []
        for index in range(4096):
            if index % 10 == 0:
                rows.append([f"P{index:04d}", 40, True, "", "", "", ""])
            else:
                rows.append([f"P{index:04d}", 80, False, 68, 0.15, 0.025, 0.8])
        _selftest_write_csv(table, header, rows)
        columns = [
            {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
            {"name": "k", "role": "support_k", "quantity_class": "study_count"},
            {"name": "masked", "role": "mask", "quantity_class": "mask"},
            {"name": "accepted_count", "role": "quantity", "quantity_class": "study_count"},
            {"name": "abstention_fraction", "role": "quantity", "quantity_class": "instrument_summary"},
            {"name": "mean_sign", "role": "quantity", "quantity_class": "study_estimand"},
            {"name": "sensitivity", "role": "quantity", "quantity_class": "instrument_summary"},
        ]
        system = _selftest_system(
            "s1_nside32", domain="synthetic_sky", family="healpix", resolution=32, axis="sky"
        )
        _selftest_write_manifest(package, [_selftest_table_entry(table, columns, cell_system=system)])
    elif fixture == "good_67_partition_table":
        table = package / "partition67.csv"
        _selftest_write_csv(
            table, standard_header,
            ((f"PART-{index:02d}", 60, False, 0.0) for index in range(67)),
        )
        system = _selftest_system("partition67", family="fixed_partition", axis="partition")
        _selftest_write_manifest(
            package, [_selftest_table_entry(table, standard_columns, cell_system=system)]
        )
    elif fixture == "good_9_hand_check_strata":
        table = package / "hand_strata9.csv"
        header = ["cell_id", "k", "masked", "tp", "tn", "fp", "fn"]
        rows = [[f"STRATUM-{index}", 100, False, 40, 45, 8, 7] for index in range(9)]
        _selftest_write_csv(table, header, rows)
        columns = [
            {"name": "cell_id", "role": "cell_id", "quantity_class": "cell_definition"},
            {"name": "k", "role": "support_k", "quantity_class": "study_count"},
            {"name": "masked", "role": "mask", "quantity_class": "mask"},
            *[
                {"name": name, "role": "quantity", "quantity_class": "study_count"}
                for name in ("tp", "tn", "fp", "fn")
            ],
        ]
        system = _selftest_system("hand_strata9", family="fixed_strata", axis="hand_check_stratum")
        _selftest_write_manifest(
            package, [_selftest_table_entry(table, columns, cell_system=system)]
        )
    elif fixture == "good_nside16_scan_surface":
        table = package / "scan_nside16.csv"
        _selftest_write_csv(
            table, ["scan_pixel", "whole_sample_statistic"],
            ((index, f"{(index % 17) / 1000:.6f}") for index in range(3072)),
        )
        columns = [
            {"name": "scan_pixel", "role": "axis", "quantity_class": "cell_definition"},
            {
                "name": "whole_sample_statistic", "role": "quantity",
                "quantity_class": "whole_sample_statistic",
            },
        ]
        system = _selftest_system(
            "nside16_direction_scan", domain="whole_sample_direction",
            family="healpix_scan", resolution=16, axis="direction_index",
        )
        entry = _selftest_table_entry(
            table, columns, cell_system=system, table_kind="whole_sample_scan",
            whole_sample_n=12000, membership_partition=False,
        )
        _selftest_write_manifest(package, [entry])
    else:
        raise ValueError(f"unknown self-test fixture: {fixture}")


def run_selftest() -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="_tmp_nm_release_linter_") as tmp:
        root = Path(tmp)
        for fixture, expected_accept, expected_codes in SELFTEST_EXPECTATIONS:
            package = root / fixture
            try:
                _build_selftest_fixture(package, fixture)
                result = lint_package(package)
                actual_codes = sorted({item.code for item in result.findings})
                match = result.accepted == expected_accept and expected_codes == set(actual_codes)
                results.append(
                    {
                        "fixture": fixture,
                        "expected": "ACCEPT" if expected_accept else "REJECT",
                        "actual": "ACCEPT" if result.accepted else "REJECT",
                        "expected_codes": sorted(expected_codes),
                        "actual_codes": actual_codes,
                        "match": match,
                        "metrics": result.metrics,
                    }
                )
            except Exception as exc:  # fail closed inside the self-test report
                results.append(
                    {
                        "fixture": fixture,
                        "expected": "ACCEPT" if expected_accept else "REJECT",
                        "actual": "ERROR",
                        "expected_codes": sorted(expected_codes),
                        "actual_codes": ["SELFTEST_EXCEPTION"],
                        "match": False,
                        "metrics": {"error": f"{type(exc).__name__}: {exc}"},
                    }
                )

    all_codes = {code for item in results for code in item["actual_codes"]}
    coverage = {
        "R1_rowless": any(code.startswith("E_R1_") for code in all_codes),
        "R2_fixed_and_finite": any(code.startswith("E_R2_") for code in all_codes),
        "R3_study_result_only": any(code.startswith("E_R3_") for code in all_codes),
        "R4_non_reconstructable": any(code.startswith("E_R4_") for code in all_codes),
        "R5_non_substitutive": any(code.startswith("E_R5_") for code in all_codes),
        "R6_image_compliance": any(code.startswith("E_R6_") for code in all_codes),
        "numeric_k_and_mask_guardrail": any(code.startswith("E_G_") for code in all_codes),
        "fail_closed_unknown_or_unlisted": bool(
            all_codes.intersection({"E_FILE_UNKNOWN_TYPE", "E_MANIFEST_UNLISTED_FILE"})
        ),
    }
    passed = all(item["match"] for item in results) and all(coverage.values())
    return {
        "status": "PASS_SYNTHETIC_SELFTEST" if passed else "FAIL_SYNTHETIC_SELFTEST",
        "passed": passed,
        "fixture_count": len(results),
        "matched_count": sum(bool(item["match"]) for item in results),
        "coverage": coverage,
        "fixtures": results,
        "linter_sha256": file_sha256(Path(__file__)),
        "synthetic_only": True,
        "network_used": False,
    }


def render_selftest_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# NebulaMind release-linter synthetic self-test",
        "",
        f"**Verdict:** **{summary['status']}**",
        "",
        "Generated by running `python3 nm_release_lint.py --self-test --write-selftest SELFTEST.md`.",
        "The fixture tree was temporary (`_tmp_nm_release_linter_*`) and contained synthetic values only.",
        "No network access or real-sky input was used.",
        "",
        f"- fixtures matched: **{summary['matched_count']}/{summary['fixture_count']}**",
        f"- linter SHA-256 at run: `{summary['linter_sha256']}`",
        "- expected rejects that unexpectedly passed: **"
        + str(sum(item['expected'] == 'REJECT' and item['actual'] == 'ACCEPT' for item in summary['fixtures']))
        + "**",
        "- expected accepts that were falsely rejected: **"
        + str(sum(item['expected'] == 'ACCEPT' and item['actual'] != 'ACCEPT' for item in summary['fixtures']))
        + "**",
        "",
        "## Per-fixture expected versus actual",
        "",
        "| Fixture | Expected | Actual | Required trigger(s) | Actual finding codes | Match |",
        "|---|---:|---:|---|---|---:|",
    ]
    for item in summary["fixtures"]:
        expected_codes = ", ".join(item["expected_codes"]) or "none"
        actual_codes = ", ".join(item["actual_codes"]) or "none"
        lines.append(
            f"| `{item['fixture']}` | {item['expected']} | {item['actual']} | "
            f"`{expected_codes}` | `{actual_codes}` | {'PASS' if item['match'] else 'FAIL'} |"
        )
    lines.extend(
        [
            "",
            "## Rule coverage",
            "",
            "| Rule family | A fixture proved it fires |",
            "|---|---:|",
        ]
    )
    for rule, fired in summary["coverage"].items():
        lines.append(f"| `{rule}` | {'YES' if fired else 'NO'} |")
    lines.extend(
        [
            "",
            "## Fixture facts",
            "",
            "- `bad_per_brick_270577` contains exactly **270,577 synthetic rows**; no survey brick was used.",
            "- `bad_cumulative_cell_budget` uses two individually sub-5,000 tables whose package total is 5,001 unique cells.",
            "- `good_67_partition_table` contains exactly **67 synthetic aggregate rows**.",
            "- `good_9_hand_check_strata` contains exactly **nine synthetic aggregate strata**.",
            "- `good_nside16_scan_surface` contains exactly **3,072 whole-sample scan points**, not object-membership cells.",
            "- `good_s1_nside32_masked_maps` contains **4,096 released synthetic footprint cells** (not a full-sky HEALPix census) and includes sub-k cells with every released result value blank and the mask set.",
            "- Expected finding-code sets are matched exactly; any missing or unexpected trigger fails the self-test.",
            "",
            "A mismatch remains a self-test failure; the harness does not weaken a fixture to obtain PASS.",
            "",
        ]
    )
    return "\n".join(lines)


def _render_human(result: LintResult) -> str:
    lines = [f"VERDICT: {'ACCEPT' if result.accepted else 'REJECT'}", f"PACKAGE: {result.package}"]
    if result.findings:
        for item in result.findings:
            location = f" [{item.path}]" if item.path else ""
            lines.append(f"{item.code} ({item.rule}){location}: {item.message}")
    else:
        lines.append("FINDINGS: 0")
    return "\n".join(lines)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", nargs="?", help="release package directory")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--self-test", action="store_true", help="run deterministic synthetic fixtures")
    parser.add_argument(
        "--write-selftest", metavar="PATH",
        help="write the self-test Markdown receipt (requires --self-test)",
    )
    args = parser.parse_args(argv)
    if args.self_test:
        if args.package:
            parser.error("do not provide a package directory with --self-test")
        summary = run_selftest()
        if args.write_selftest:
            Path(args.write_selftest).write_text(
                render_selftest_markdown(summary), encoding="utf-8"
            )
        if args.json:
            print(json.dumps(summary, indent=2, sort_keys=True))
        else:
            print(summary["status"])
            print(f"fixtures={summary['matched_count']}/{summary['fixture_count']}")
            if args.write_selftest:
                print(f"receipt={args.write_selftest}")
        return 0 if summary["passed"] else 1
    if args.write_selftest:
        parser.error("--write-selftest requires --self-test")
    if not args.package:
        parser.error("a package directory is required")
    result = lint_package(args.package)
    if args.json:
        print(json.dumps(result.to_dict(), indent=2, sort_keys=True))
    else:
        print(_render_human(result))
    return 0 if result.accepted else 2


if __name__ == "__main__":
    raise SystemExit(main())
