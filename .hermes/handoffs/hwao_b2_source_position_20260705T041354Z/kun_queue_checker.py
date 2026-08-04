#!/usr/bin/env python3
"""Read-only B2 queue edit checker."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


MARKER = "KUN_B2_QUEUE_CHECKER_READY_20260705T041354Z"
DEFAULT_QUEUE_DIR = Path("docs/galaxy_2929_source_position_queue_20260705T013911Z/queue")
DEFAULT_SNAPSHOT_DIR = Path(
    ".hermes/handoffs/hwao_b2_source_position_20260705T041354Z/"
    "pre_edit_queue_snapshot_b2_20260705T041354Z"
)
DEFAULT_OUTPUT = Path(
    ".hermes/handoffs/hwao_b2_source_position_20260705T041354Z/"
    "kun_queue_checker_results.json"
)
DEFAULT_EDITED_IDS = "28087,28108,28133,28074"
EXPECTED_ROW_COUNT = 36
QUEUE_BASENAME = "source_position_human_adjudication_queue"
PRODUCT_GATE = "NO_GO_DB_OR_PRODUCT_PUBLICATION_UNDER_THIS_APPROVAL"
WRITE_LOCK = "NO_APPLY_SQL_NO_DB_WRITE_FROM_THIS_QUEUE"

VALID_DECISIONS = {
    "relink",
    "copy_source_fill",
    "retire_reject",
    "leave_archival",
    "route_kinetic_radio",
}
VALID_DECISIONS_WITH_PENDING = VALID_DECISIONS | {"pending"}
VALID_REVIEW_STATUS = {"reviewed", "needs_second_review", "pending"}
VALID_SOURCE_STATUS = {
    "accepted",
    "accepted_limited",
    "rejected",
    "pending",
}
VALID_VERIFICATION_STATUS = {
    "abstract_only_verified",
    "pdf_verified",
    "source_record_verified",
    "docs_verified",
    "pending",
    "not_applicable",
}
VALID_STANCE = {"supports", "contradicts", "none", "needs_new_stance", "not_applicable"}
VALID_ROLE = {
    "support",
    "challenge",
    "limitation_or_caution",
    "background_only",
    "not_applicable",
}
SQL_KEYWORD_RE = re.compile(
    r"\b(SELECT|INSERT|UPDATE|DELETE|BEGIN|COMMIT|ROLLBACK)\b|"
    r"\bCREATE\s+TABLE\b|\bALTER\s+TABLE\b",
    re.IGNORECASE,
)


def fail(results: dict[str, Any], check: str, detail: str) -> None:
    results["failed_checks"].append({"check": check, "detail": detail})


def is_filled(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, dict, set)):
        return bool(value)
    return True


def is_filled_or_na(value: Any) -> bool:
    if not is_filled(value):
        return False
    if isinstance(value, str):
        return value.strip().lower() in {"n/a", "na", "not_applicable"} or bool(value.strip())
    return True


def canonical_hash(row: dict[str, Any]) -> str:
    payload = json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_json(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"{path} did not contain a JSON list")
    return data


def load_jsonl(path: Path) -> tuple[list[dict[str, Any]], dict[int, bytes]]:
    rows: list[dict[str, Any]] = []
    lines: dict[int, bytes] = {}
    with path.open("rb") as f:
        for line in f:
            if not line.strip():
                continue
            row = json.loads(line.decode("utf-8"))
            evidence_id = int(row["evidence_id"])
            rows.append(row)
            lines[evidence_id] = line
    return rows, lines


def load_csv(path: Path) -> tuple[list[dict[str, str]], dict[int, bytes]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    line_map: dict[int, bytes] = {}
    with path.open("rb") as f:
        lines = f.readlines()
    for row, line in zip(rows, lines[1:]):
        line_map[int(row["evidence_id"])] = line
    return rows, line_map


def split_md_table_line(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [part.strip() for part in stripped.split("|")]


def load_markdown(path: Path) -> tuple[list[dict[str, str]], dict[int, bytes]]:
    rows: list[dict[str, str]] = []
    line_map: dict[int, bytes] = {}
    header: list[str] | None = None
    with path.open("rb") as f:
        for raw_line in f:
            line = raw_line.decode("utf-8")
            if not line.startswith("|"):
                continue
            cells = split_md_table_line(line)
            if not cells:
                continue
            if header is None:
                header = cells
                continue
            if all(set(cell) <= {"-", ":"} for cell in cells):
                continue
            if len(cells) != len(header):
                continue
            row = dict(zip(header, cells))
            try:
                evidence_id = int(row["evidence"])
            except (KeyError, ValueError):
                continue
            rows.append(row)
            line_map[evidence_id] = raw_line
    return rows, line_map


def index_json(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    return {int(row["evidence_id"]): row for row in rows}


def index_csv(rows: list[dict[str, str]]) -> dict[int, dict[str, str]]:
    return {int(row["evidence_id"]): row for row in rows}


def index_md(rows: list[dict[str, str]]) -> dict[int, dict[str, str]]:
    return {int(row["evidence"]): row for row in rows}


def nested(row: dict[str, Any], *keys: str) -> Any:
    value: Any = row
    for key in keys:
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


def source_field(row: dict[str, Any], key: str) -> Any:
    rsp = row.get("required_source_position_fields")
    if isinstance(rsp, dict) and key in rsp:
        return rsp.get(key)
    return nested(row, "human_adjudication", key)


def row_decision(row: dict[str, Any]) -> str | None:
    return nested(row, "human_adjudication", "decision_enum") or source_field(row, "human_decision_enum")


def row_review(row: dict[str, Any]) -> str | None:
    return nested(row, "human_adjudication", "review_status") or source_field(row, "review_status")


def row_source_status(row: dict[str, Any]) -> str | None:
    return nested(row, "human_adjudication", "source_position_verification_status") or source_field(
        row, "source_position_verification_status"
    )


def row_source_acceptance(row: dict[str, Any]) -> str | None:
    return nested(row, "human_adjudication", "accepted_for_docs_source_position") or source_field(
        row, "accepted_for_docs_source_position"
    )


def normalize_optional(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def check_row_counts(
    results: dict[str, Any],
    live: dict[str, Any],
    snapshot: dict[str, Any],
) -> None:
    for name in ("json", "jsonl", "csv", "markdown"):
        live_count = len(live[name]["rows"])
        snapshot_count = len(snapshot[name]["rows"])
        results["row_counts"][name] = {"live": live_count, "snapshot": snapshot_count}
        if live_count != EXPECTED_ROW_COUNT:
            fail(results, "row_counts", f"{name} live count {live_count}, expected {EXPECTED_ROW_COUNT}")
        if snapshot_count != EXPECTED_ROW_COUNT:
            fail(results, "row_counts", f"{name} snapshot count {snapshot_count}, expected {EXPECTED_ROW_COUNT}")


def check_presence(results: dict[str, Any], ids: set[int], live: dict[str, Any]) -> None:
    for name in ("json", "jsonl", "csv", "markdown"):
        present = set(live[name]["index"])
        missing = sorted(ids - present)
        if missing:
            fail(results, "edited_ids_present", f"{name} missing edited IDs {missing}")


def check_untouched_rows(results: dict[str, Any], edited_ids: set[int], live: dict[str, Any], snapshot: dict[str, Any]) -> None:
    unchanged = {"json": True, "jsonl": True, "csv": True, "markdown": True}
    live_json = live["json"]["index"]
    snap_json = snapshot["json"]["index"]
    for evidence_id, row in live_json.items():
        if evidence_id in edited_ids:
            continue
        if evidence_id not in snap_json:
            unchanged["json"] = False
            fail(results, "json_untouched_rows", f"{evidence_id} missing from snapshot")
            continue
        if canonical_hash(row) != canonical_hash(snap_json[evidence_id]):
            unchanged["json"] = False
            fail(results, "json_untouched_rows", f"{evidence_id} canonical row hash changed")

    for name in ("jsonl", "csv", "markdown"):
        live_lines = live[name]["lines"]
        snap_lines = snapshot[name]["lines"]
        for evidence_id, line in live_lines.items():
            if evidence_id in edited_ids:
                continue
            if snap_lines.get(evidence_id) != line:
                unchanged[name] = False
                fail(results, f"{name}_untouched_rows", f"{evidence_id} line bytes changed")

    results["other_rows_unchanged"] = unchanged


def check_locks(results: dict[str, Any], live_json: dict[int, dict[str, Any]], snapshot_json: dict[int, dict[str, Any]]) -> None:
    lock_checks = {"product_gate_preserved": True, "write_lock_preserved": True}
    for evidence_id, row in live_json.items():
        snap = snapshot_json.get(evidence_id, {})
        for label, expected, keys in (
            ("product_gate", PRODUCT_GATE, ("product_gate",)),
            ("write_lock", WRITE_LOCK, ("write_lock",)),
        ):
            value = row.get(keys[0])
            if value != expected or snap.get(keys[0]) != value:
                lock_checks[f"{label}_preserved"] = False
                fail(results, "lock_checks", f"{evidence_id} {label} not preserved")
        ha_gate = nested(row, "human_adjudication", "product_publication_gate")
        rsp_gate = source_field(row, "product_publication_gate")
        if ha_gate != PRODUCT_GATE or rsp_gate != PRODUCT_GATE:
            lock_checks["product_gate_preserved"] = False
            fail(results, "lock_checks", f"{evidence_id} nested product gate not preserved")
    results["lock_checks"] = lock_checks


def check_edited_rows(
    results: dict[str, Any],
    edited_ids: set[int],
    live: dict[str, Any],
    snapshot: dict[str, Any],
) -> None:
    edited: dict[str, Any] = {}
    live_json = live["json"]["index"]
    snap_json = snapshot["json"]["index"]
    for evidence_id in sorted(edited_ids):
        row = live_json.get(evidence_id)
        snap = snap_json.get(evidence_id)
        detail: dict[str, Any] = {"present": row is not None, "checks": {}}
        edited[str(evidence_id)] = detail
        if row is None or snap is None:
            fail(results, "edited_rows", f"{evidence_id} missing in JSON live or snapshot")
            continue

        decision = normalize_optional(row_decision(row))
        review = normalize_optional(row_review(row))
        verification = normalize_optional(row_source_status(row))
        acceptance = normalize_optional(row_source_acceptance(row))
        json_changed = canonical_hash(row) != canonical_hash(snap)
        payload_hash_changed = row.get("source_payload_hash") != snap.get("source_payload_hash")
        detail.update(
            {
                "decision_enum": decision,
                "review_status": review,
                "source_position_verification_status": verification,
                "accepted_for_docs_source_position": acceptance,
                "json_changed": json_changed,
                "source_payload_hash_changed": payload_hash_changed,
            }
        )

        row_failures: list[str] = []
        if decision not in VALID_DECISIONS:
            row_failures.append(f"decision_enum is {decision!r}, expected non-pending valid decision")
        if review not in VALID_REVIEW_STATUS or review == "pending":
            row_failures.append(f"review_status is {review!r}, expected non-pending valid review status")
        if verification not in VALID_VERIFICATION_STATUS or verification == "pending":
            row_failures.append(f"source_position_verification_status is {verification!r}, expected non-pending valid status")
        if acceptance not in VALID_SOURCE_STATUS or acceptance == "pending":
            row_failures.append(f"accepted_for_docs_source_position is {acceptance!r}, expected non-pending valid status")

        enum_fields = {
            "accepted_support_role": (source_field(row, "accepted_support_role"), VALID_ROLE),
            "accepted_target_stance": (source_field(row, "accepted_target_stance"), VALID_STANCE),
            "selected_role": (source_field(row, "selected_role"), VALID_ROLE),
            "selected_stance_if_visible_successor": (source_field(row, "selected_stance_if_visible_successor"), VALID_STANCE),
            "human_decision_enum": (source_field(row, "human_decision_enum"), VALID_DECISIONS_WITH_PENDING),
        }
        for field, (value, valid_values) in enum_fields.items():
            text = normalize_optional(value)
            if text and text not in valid_values:
                row_failures.append(f"{field} has invalid enum value {text!r}")

        required_fields = [
            "decision_owner",
            "decision_reason",
            "decision_reason_plain_english",
            "dependency_handling_action",
            "human_decision",
            "human_decision_enum",
            "human_reviewed_at_utc",
            "human_reviewer",
            "source_accessed_url_or_path",
            "source_position_note",
            "source_type",
        ]
        for field in required_fields:
            if not is_filled_or_na(source_field(row, field)):
                row_failures.append(f"{field} empty")

        quote = source_field(row, "exact_quote_or_paraphrase_source_span")
        if not is_filled_or_na(quote):
            row_failures.append("exact_quote_or_paraphrase_source_span empty")
        locator_fields = [
            source_field(row, "section"),
            source_field(row, "paragraph_or_sentence_locator"),
            source_field(row, "pdf_page"),
            source_field(row, "figure_or_table"),
        ]
        if not any(is_filled_or_na(value) for value in locator_fields):
            row_failures.append("section/paragraph/page/table locator empty")

        if row.get("product_gate") != PRODUCT_GATE or source_field(row, "product_publication_gate") != PRODUCT_GATE:
            row_failures.append("product gate changed or missing")
        if row.get("write_lock") != WRITE_LOCK:
            row_failures.append("write lock changed or missing")
        if json_changed and not payload_hash_changed:
            row_failures.append("JSON changed but source_payload_hash did not change")

        detail["checks"]["pass"] = not row_failures
        detail["checks"]["failures"] = row_failures
        for row_failure in row_failures:
            fail(results, "edited_rows", f"{evidence_id}: {row_failure}")
    results["edited_rows"] = edited


def check_format_consistency(results: dict[str, Any], edited_ids: set[int], live: dict[str, Any]) -> None:
    consistency: dict[str, Any] = {"pass": True, "rows": {}}
    json_idx = live["json"]["index"]
    csv_idx = live["csv"]["index"]
    md_idx = live["markdown"]["index"]
    for evidence_id in sorted(edited_ids):
        row = json_idx.get(evidence_id)
        csv_row = csv_idx.get(evidence_id)
        md_row = md_idx.get(evidence_id)
        if not row or not csv_row or not md_row:
            consistency["pass"] = False
            fail(results, "format_consistency", f"{evidence_id} missing in at least one format")
            continue
        expected = {
            "decision": normalize_optional(row_decision(row)),
            "review": normalize_optional(row_review(row)),
            "source_position": normalize_optional(row_source_status(row)),
        }
        actual = {
            "csv_decision": normalize_optional(csv_row.get("decision_enum")),
            "csv_review": normalize_optional(csv_row.get("review_status")),
            "csv_source_position": normalize_optional(csv_row.get("source_position_verification_status")),
            "md_decision": normalize_optional(md_row.get("decision")),
            "md_review": normalize_optional(md_row.get("review")),
            "md_source_position": normalize_optional(md_row.get("source-position")),
        }
        row_pass = (
            expected["decision"] == actual["csv_decision"] == actual["md_decision"]
            and expected["review"] == actual["csv_review"] == actual["md_review"]
            and expected["source_position"] == actual["csv_source_position"] == actual["md_source_position"]
        )
        consistency["rows"][str(evidence_id)] = {"pass": row_pass, "json": expected, "formats": actual}
        if not row_pass:
            consistency["pass"] = False
            fail(results, "format_consistency", f"{evidence_id} decision/review/source-position mismatch")
    results["format_consistency"] = consistency


def check_queue_artifact_locks(results: dict[str, Any], queue_dir: Path) -> None:
    artifact_checks = {"no_sql_files": True, "no_apply_or_rollback_files": True, "no_dml_keywords": True}
    for path in queue_dir.iterdir():
        if not path.is_file():
            continue
        lower_name = path.name.lower()
        if lower_name.endswith(".sql"):
            artifact_checks["no_sql_files"] = False
            fail(results, "queue_artifacts", f"{path} has .sql extension")
        if "apply" in lower_name or "rollback" in lower_name:
            artifact_checks["no_apply_or_rollback_files"] = False
            fail(results, "queue_artifacts", f"{path} name contains apply or rollback")
        if path.suffix.lower() in {".json", ".jsonl", ".csv", ".md"}:
            text = path.read_text(encoding="utf-8")
            for match in SQL_KEYWORD_RE.finditer(text):
                artifact_checks["no_dml_keywords"] = False
                fail(results, "queue_artifacts", f"{path} contains locked keyword {match.group(0)!r}")
                break
    results["queue_artifacts"] = artifact_checks


def load_all(queue_dir: Path, snapshot_dir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    def paths(base: Path) -> dict[str, Path]:
        return {
            "json": base / f"{QUEUE_BASENAME}.json",
            "jsonl": base / f"{QUEUE_BASENAME}.jsonl",
            "csv": base / f"{QUEUE_BASENAME}.csv",
            "markdown": base / f"{QUEUE_BASENAME}.md",
        }

    def load(base_paths: dict[str, Path]) -> dict[str, Any]:
        json_rows = load_json(base_paths["json"])
        jsonl_rows, jsonl_lines = load_jsonl(base_paths["jsonl"])
        csv_rows, csv_lines = load_csv(base_paths["csv"])
        md_rows, md_lines = load_markdown(base_paths["markdown"])
        return {
            "json": {"rows": json_rows, "index": index_json(json_rows)},
            "jsonl": {"rows": jsonl_rows, "index": index_json(jsonl_rows), "lines": jsonl_lines},
            "csv": {"rows": csv_rows, "index": index_csv(csv_rows), "lines": csv_lines},
            "markdown": {"rows": md_rows, "index": index_md(md_rows), "lines": md_lines},
        }

    return load(paths(queue_dir)), load(paths(snapshot_dir))


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read-only checker for B2 queue edits.")
    parser.add_argument("--queue-dir", type=Path, default=DEFAULT_QUEUE_DIR)
    parser.add_argument("--snapshot-dir", type=Path, default=DEFAULT_SNAPSHOT_DIR)
    parser.add_argument("--edited-ids", default=DEFAULT_EDITED_IDS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    edited_ids = {int(part.strip()) for part in args.edited_ids.split(",") if part.strip()}
    results: dict[str, Any] = {
        "marker": MARKER,
        "pass": False,
        "row_counts": {},
        "other_rows_unchanged": {},
        "edited_rows": {},
        "format_consistency": {},
        "lock_checks": {},
        "failed_checks": [],
        "checked_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }

    try:
        live, snapshot = load_all(args.queue_dir, args.snapshot_dir)
        check_row_counts(results, live, snapshot)
        check_presence(results, edited_ids, live)
        check_untouched_rows(results, edited_ids, live, snapshot)
        check_edited_rows(results, edited_ids, live, snapshot)
        check_format_consistency(results, edited_ids, live)
        check_locks(results, live["json"]["index"], snapshot["json"]["index"])
        check_queue_artifact_locks(results, args.queue_dir)
    except Exception as exc:
        fail(results, "checker_exception", f"{type(exc).__name__}: {exc}")

    results["pass"] = not results["failed_checks"]
    output_text = json.dumps(results, indent=2, sort_keys=True, ensure_ascii=False)
    print(output_text)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output_text + "\n", encoding="utf-8")
    return 0 if results["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
