from __future__ import annotations

import json
import subprocess
import sys
import hashlib
from pathlib import Path
from collections import Counter

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


def test_t14_exact_mechanical_residue_r3_and_t15_determinism(tmp_path: Path) -> None:
    # T-CUST: Immutable input hashes
    def get_hash(path_str):
        with open(path_str, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    assert get_hash(FIXTURES / "prompt_submitted.md") == "fffac44fbf6e9abe3afb1f8f34f3a9e3e7688991f319c4927459fb29ac00e1ef"
    assert get_hash(FIXTURES / "body.md") == "8a130c5a6fc1b1f5d534888d3fb20806230b8b4c7737cb00f9bfb18ad0d6bc00"
    assert get_hash(FIXTURES / "rendered_body.html") == "78ed129c47daf9300d9ed319aa1ffe95bbb0d1810a223733afaf48c4372f2bbc"
    assert get_hash(FIXTURES / "contract_spec_v2_reference.json") == "1b10b4538162e1f786e3e36b639448cbe0d4252282d236c88495272398062338"
    assert get_hash(FIXTURES / "structured_capture_v2_reference.json") == "e26819dbc90a040ecc228639fbee3e2a68f8942fa9d26b9458aee71bbc65e3e9"
    assert get_hash(FIXTURES / "validator_result_v2_reference.json") == "ad4d035b291f6d64ad47f510811cc05826d822f449cf3d181974be2ce2473d52"

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

    # Deterministic FAILs expected = 19
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

    # C4:UNCITED_CELL_CLAIM should be absent
    assert ("C4", "UNCITED_CELL_CLAIM") not in by_clause_code

    # D1 exact refs for MISSING_CALIBRATION_TARGET_PREFIX
    d1_refs = sorted([finding["source_refs"] for finding in by_clause_code[("C6", "MISSING_CALIBRATION_TARGET_PREFIX")]])
    expected_d1_refs = sorted([
        ["table_row_4", 1], ["table_row_5", 1], ["table_row_6", 1], ["table_row_7", 1],
        ["table_row_8", 1], ["table_row_9", 1], ["table_row_10", 1], ["table_row_11", 1],
        ["table_row_11", 2]
    ])
    assert d1_refs == expected_d1_refs

    # D5 gap schema directly asserted
    gap_blocks = [b for b in capture["blocks"] if b["type"] == "gap_line"]
    assert len(gap_blocks) == 4
    for b in gap_blocks:
        assert "parent_path" in b
        assert b["parent_path"] != ""
        assert b["parent_path"] == gap_blocks[0]["parent_path"]

    # Manual multiset check
    manual = [finding for finding in result["findings"] if finding["status"] == "MANUAL_REVIEW_REQUIRED"]
    actual_manual_counter = Counter((f["clause"], f["code"], f["status"], tuple(f["source_refs"])) for f in manual)
    
    with open(FIXTURES / "validator_result_v2_reference.json") as f:
        v2_res = json.load(f)
    v2_manual = [f for f in v2_res["findings"] if f["status"] == "MANUAL_REVIEW_REQUIRED"]
    
    expected_manual_counter = Counter((f["clause"], f["code"], f["status"], tuple(f["source_refs"])) for f in v2_manual)
    
    # Add 8 D3 row reviews
    for row_idx in range(14, 22):
        expected_manual_counter[("C4", "CITED_CELL_CLAIM_REVIEW", "MANUAL_REVIEW_REQUIRED", (f"table_row_{row_idx}", 2))] += 1
    
    # Add 1 C7 near duplicate
    expected_manual_counter[("C7", "C7_NEAR_DUPLICATE", "MANUAL_REVIEW_REQUIRED", ())] += 1
    
    assert actual_manual_counter == expected_manual_counter
    assert sum(actual_manual_counter.values()) == 82
    
    # Extract the eight D3-specific rows without also selecting retained
    # Section-1 reviews such as table_row_10/table_row_11 at column 2.
    d3_expected_refs = {(f"table_row_{row}", 2) for row in range(14, 22)}
    d3_added = [
        finding
        for finding in manual
        if finding["code"] == "CITED_CELL_CLAIM_REVIEW"
        and tuple(finding["source_refs"]) in d3_expected_refs
    ]
    d3_refs = sorted([m["source_refs"][0] for m in d3_added])
    assert d3_refs == [f"table_row_{r}" for r in range(14, 22)]

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
    
    assert "near_duplicate_indices" not in c7 or c7["near_duplicate_indices"] == []
    assert c7.get("inline_only_indices", []) == []

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
