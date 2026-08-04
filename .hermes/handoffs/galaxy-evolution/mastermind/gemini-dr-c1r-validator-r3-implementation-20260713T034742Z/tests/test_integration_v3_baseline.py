from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


PACKET = Path(__file__).resolve().parents[1]
FIXTURES = PACKET / "fixtures"
CAPTURE_RUNNER = PACKET / "capture" / "run_capture_v3.mjs"
sys.path.insert(0, str(PACKET / "validator"))
from validator_v3 import validate_document  # noqa: E402


def run_capture(output: Path) -> dict:
    subprocess.run(
        [
            "node",
            str(CAPTURE_RUNNER),
            str(FIXTURES / "rendered_body.html"),
            str(FIXTURES / "body.md"),
            str(output),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(output.read_text())


def test_t14_exact_mechanical_residue_and_t15_determinism(tmp_path: Path) -> None:
    first_path = tmp_path / "capture-a.json"
    second_path = tmp_path / "capture-b.json"
    capture = run_capture(first_path)
    second_capture = run_capture(second_path)

    assert capture["schema"] == "NM_GEMINI_RENDERED_DOM_V3"
    assert capture["chip_map_status"] == "OK"
    assert capture["capture_flags"] == []
    assert first_path.read_bytes() == second_path.read_bytes()
    assert capture == second_capture

    spec = json.loads((PACKET / "validator" / "contract_spec_v3.json").read_text())
    body = (FIXTURES / "body.md").read_text()
    result = validate_document(body, capture, spec)
    repeated = validate_document(body, second_capture, spec)
    assert json.dumps(result, sort_keys=True, separators=(",", ":")) == json.dumps(
        repeated, sort_keys=True, separators=(",", ":")
    )

    failures = [finding for finding in result["findings"] if finding["status"] == "FAIL"]
    by_clause_code: dict[tuple[str, str], list[dict]] = {}
    for finding in failures:
        by_clause_code.setdefault((finding["clause"], finding["code"]), []).append(finding)

    assert {key: len(value) for key, value in by_clause_code.items()} == {
        ("C2", "SENTINEL_FORMAT_DEFECT"): 1,
        ("C2", "GAP_MULTIPLE_PER_PARAGRAPH"): 1,
        ("C6", "UNLABELED_COMPARISON"): 6,
        ("C6", "MISSING_QUALIFIER"): 1,
        ("C6", "MISSING_CALIBRATION_TARGET_PREFIX"): 9,
        ("C7", "C7_INTEGRITY_FAILURE"): 1,
    }
    assert len(failures) == 19
    assert result["overall"] == "FAIL"

    c4 = [
        finding
        for finding in result["findings"]
        if finding["code"] == "CITED_CELL_CLAIM_REVIEW"
        and finding["status"] == "MANUAL_REVIEW_REQUIRED"
        and finding["source_refs"][0] in {f"table_row_{row}" for row in range(14, 22)}
    ]
    assert [finding["source_refs"][1] for finding in c4] == [2] * 8
    for finding in c4:
        block_id = finding["source_refs"][0]
        row = next(block for block in capture["blocks"] if block["id"] == block_id)
        assert row["section"] == "2. Out-of-sample validation ledger"
        assert row["cells"][2]["role"] == "result"
        assert row["cells"][2]["chips"] == []

    c6 = by_clause_code[("C6", "UNLABELED_COMPARISON")]
    table_refs = [finding["source_refs"] for finding in c6 if len(finding["source_refs"]) == 2]
    gap_refs = [finding["source_refs"] for finding in c6 if len(finding["source_refs"]) == 1]
    assert len(table_refs) == 5
    assert all(ref[1] == 3 for ref in table_refs)
    assert len(gap_refs) == 1
    gap = next(block for block in capture["blocks"] if block["id"] == gap_refs[0][0])
    assert gap["type"] == "gap_line"
    assert gap["gap_index"] == 1

    qualifier = by_clause_code[("C6", "MISSING_QUALIFIER")][0]
    qualifier_row = next(block for block in capture["blocks"] if block["id"] == qualifier["source_refs"][0])
    assert qualifier["source_refs"][1] == 2
    assert qualifier_row["cells"][2]["role"] == "feedback_params"
    assert "∼10%" in qualifier_row["cells"][2]["text"]

    c7 = by_clause_code[("C7", "C7_INTEGRITY_FAILURE")][0]["evidence"]
    assert c7["orphan_indices"] == [2, 5, 8, 9, 13, 16, 18, 23, 24, 29, 31, 33]
    assert len(c7["duplicate_rows"]) == 9
    assert len(c7["blank_short_name_rows"]) == 46
    assert "near_duplicate_indices" not in c7
    assert c7["inline_only_indices"] == []
    c7_near = [
        finding
        for finding in result["findings"]
        if finding["code"] == "C7_NEAR_DUPLICATE"
        and finding["status"] == "MANUAL_REVIEW_REQUIRED"
    ]
    assert len(c7_near) == 1
    assert c7_near[0]["evidence"]["near_duplicate_indices"] == [[14, 29]]

    sentinel = by_clause_code[("C2", "SENTINEL_FORMAT_DEFECT")][0]
    sentinel_row = next(block for block in capture["blocks"] if block["id"] == sentinel["source_refs"][0])
    assert sentinel["source_refs"][1] == 2
    assert sentinel_row["cells"][2]["role"] == "feedback_params"
    assert sentinel_row["cells"][2]["text"] == "NONE_FOUND."

    pass_codes = {finding["code"] for finding in result["findings"] if finding["status"] == "PASS"}
    assert {"C1_OK", "STRUCTURE_OK", "C5_OK", "C8_OK"} <= pass_codes

    forbidden = {
        "BAD_STRUCTURE",
        "EMPTY_TABLE_CELL",
        "GAP_MISSING_VERIFICATION",
    }
    assert not forbidden.intersection(finding["code"] for finding in result["findings"])
    assert not any(
        finding["code"] in {"UNCITED_CELL_CLAIM", "UNCITED_CLAIM"}
        and finding["source_refs"][0]
        in {
            block["id"]
            for block in capture["blocks"]
            if block["section"] in {"1. Calibration ledger", "3. Double-counting warnings", "4. Feedback-relevant observables map"}
        }
        for finding in failures
    )

    manual_codes = {
        finding["code"]
        for finding in result["findings"]
        if finding["status"] == "MANUAL_REVIEW_REQUIRED"
    }
    assert {
        "COMPARISON_LABEL_REVIEW",
        "UNCERTAINTY_CHECK",
        "CITED_CELL_CLAIM_REVIEW",
        "CITED_CLAIM_REVIEW",
        "CITATION_QUALITY_REVIEW",
        "SOURCE_FIDELITY_REVIEW",
        "C7_NEAR_DUPLICATE",
    } <= manual_codes
