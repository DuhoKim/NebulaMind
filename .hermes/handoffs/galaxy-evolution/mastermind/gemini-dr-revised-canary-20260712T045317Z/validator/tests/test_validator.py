import pytest
import json
from pathlib import Path
from validator import validate_document

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"

def create_block(id_str, type_str, text, links=None, source_lines=None, cells=None):
    if links is None: links = []
    if source_lines is None: source_lines = []
    if cells is None: cells = []
    b = {"id": id_str, "type": type_str, "text": text, "links": links, "source_lines": source_lines}
    if type_str == "table_row":
        b["cells"] = cells
    return b

def get_findings(res, clause, status=None):
    return [f for f in res["findings"] if f["clause"] == clause and (status is None or f["status"] == status)]

def test_c1_header_pass():
    spec = {"req_id": "REQ_C1R_123", "model": "Gemini Pro"}
    txt = "Joint C1R answer — REQ_C1R_123\nRun date (UTC): 2026-07-12T05:30:00Z\nModel: Gemini Pro\nSimulations covered: 1"
    res = validate_document(txt, {"blocks": [create_block("1", "heading", txt)]}, spec=spec)
    assert not get_findings(res, "C1", "FAIL")

def test_c1_header_wrong_req():
    spec = {"req_id": "REQ_C1r_123", "model": "Gemini 1.5 Pro"}
    txt = "Joint C1 answer — REQ_WRONG\nRun date (UTC): 2026\nModel: Gemini 1.5 Pro\nSimulations covered: 1"
    res = validate_document(txt, {"blocks": [create_block("1", "heading", txt)]}, spec=spec)
    assert get_findings(res, "C1", "FAIL")

def test_c1_header_wrong_model():
    spec = {"req_id": "REQ_C1r_123", "model": "Gemini 1.5 Pro"}
    txt = "Joint C1 answer — REQ_C1r_123\nRun date (UTC): 2026\nModel: ChatGPT\nSimulations covered: 1"
    res = validate_document(txt, {"blocks": [create_block("1", "heading", txt)]}, spec=spec)
    assert get_findings(res, "C1", "FAIL")

def test_c1_header_missing_sims():
    spec = {"req_id": "REQ_C1r_123", "model": "Gemini 1.5 Pro"}
    txt = "Joint C1 answer — REQ_C1r_123\nRun date (UTC): 2026\nModel: Gemini 1.5 Pro"
    res = validate_document(txt, {"blocks": [create_block("1", "heading", txt)]}, spec=spec)
    assert get_findings(res, "C1", "FAIL")

def test_c2_order_and_empty():
    txt = "Calibration ledger\nNONE_FOUND\nOut-of-sample validation ledger\nDouble-counting warnings\nFeedback-relevant observables map\nGaps\nLinks ledger"
    struct = {"blocks": [create_block(str(i), "heading", t) for i, t in enumerate(txt.split("\n"))]}
    res = validate_document(txt, struct)
    assert not get_findings(res, "C2", "FAIL")

def test_c2_empty_table_cell():
    txt = ""
    struct = {"blocks": [create_block("1", "table_row", txt, cells=[{"text": "A"}, {"text": "   "}])]} # empty cell 2
    res = validate_document(txt, struct)
    assert get_findings(res, "C2", "FAIL")

def test_c2_gap_missing_token_or_url():
    txt = "GAP: We found no data."
    struct = {"blocks": [create_block("1", "paragraph", txt)]}
    res = validate_document(txt, struct)
    assert get_findings(res, "C2", "FAIL")

def test_c2_gap_has_token():
    txt = "GAP: We found no data. ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED"
    struct = {"blocks": [
        create_block("0", "heading", "Calibration ledger"),
        create_block("1", "heading", "Out-of-sample validation ledger"),
        create_block("2", "heading", "Double-counting warnings"),
        create_block("3", "heading", "Feedback-relevant observables map"),
        create_block("4", "heading", "Gaps"),
        create_block("g", "paragraph", txt),
        create_block("5", "heading", "Links ledger")
    ]}
    res = validate_document(txt, struct)
    assert not get_findings(res, "C2", "FAIL")

def test_c3_scientific_bare_quantity():
    txt = "The distance is 2 km."
    res = validate_document(txt, {"blocks": [create_block("1", "paragraph", txt)]})
    assert get_findings(res, "C3", "FAIL")

def test_c3_project_suffix_passes():
    txt = "We used FIRE-2 and TNG50 and IllustrisTNG100."
    res = validate_document(txt, {"blocks": [create_block("1", "paragraph", txt)]})
    assert not get_findings(res, "C3", "FAIL")

def test_c3_url_digits_pass():
    txt = "See [http://arxiv.org/abs/2501.16602v1]"
    res = validate_document(txt, {"blocks": [create_block("1", "paragraph", txt)]})
    assert not get_findings(res, "C3", "FAIL")

def test_c3_uncertainty_token_manual():
    txt = "The distance is 2 km UNCERTAINTY_NOT_QUOTED_BY_SOURCE."
    res = validate_document(txt, {"blocks": [create_block("1", "paragraph", txt)]})
    assert get_findings(res, "C3", "MANUAL_REVIEW_REQUIRED")
    assert not get_findings(res, "C3", "FAIL")

def test_c4_prose_claim_uncited():
    txt = "This simulation was calibrated on the z=0 stellar mass function to match observations perfectly." # has calibration keywords
    res = validate_document(txt, {"blocks": [create_block("1", "paragraph", txt)]})
    assert get_findings(res, "C4", "FAIL")

def test_c4_generic_prose_passes():
    txt = "Galaxies are very large systems composed of stars, gas, and dark matter that interact over time." # no keywords
    res = validate_document(txt, {"blocks": [create_block("1", "paragraph", txt)]})
    assert not get_findings(res, "C4", "FAIL")

def test_c4_same_cell_citation_pass():
    txt = ""
    struct = {"blocks": [create_block("1", "table_row", txt, cells=[
        {"text": "Sim1"}, {"text": "calibrated on mass [http://a.com]", "links": [{"url": "http://a.com"}]}
    ])]}
    res = validate_document(txt, struct)
    assert not get_findings(res, "C4", "FAIL")

def test_c4_same_cell_citation_fail():
    txt = ""
    struct = {"blocks": [create_block("1", "table_row", txt, cells=[
        {"text": "this is calibrated on mass"}, {"text": "[http://a.com]", "links": [{"url": "http://a.com"}]}
    ])]}
    res = validate_document(txt, struct)
    assert get_findings(res, "C4", "FAIL")

def test_c5_own_voice_banned():
    txt = "This proves that the mechanism is correct."
    res = validate_document(txt, {"blocks": [create_block("1", "paragraph", txt)]})
    assert get_findings(res, "C5", "FAIL")

def test_c5_attributed_quote():
    txt = 'The author states "it proves the theory".'
    res = validate_document(txt, {"blocks": [create_block("1", "paragraph", txt)]})
    assert get_findings(res, "C5", "MANUAL_REVIEW_REQUIRED")

def test_c6_comparability_cell_matched():
    txt = "Out-of-sample validation ledger"
    struct = {"blocks": [
        create_block("h", "heading", txt),
        create_block("r", "table_row", "", cells=[
            {"text": "Sim1"}, {"text": "Obs"}, {"text": "MATCHED_SELECTIONS Agreement"}
        ])
    ]}
    res = validate_document(txt, struct)
    assert not get_findings(res, "C6", "FAIL")

def test_c6_comparability_cell_unmatched():
    txt = "Out-of-sample validation ledger"
    struct = {"blocks": [
        create_block("h", "heading", txt),
        create_block("r", "table_row", "Sim1 Obs Tension NON_COMMENSURABLE_UNMATCHED_SELECTIONS", cells=[
            {"text": "Sim1"}, {"text": "Obs"}, {"text": "NON_COMMENSURABLE_UNMATCHED_SELECTIONS"}
        ])
    ]}
    res = validate_document(txt, struct)
    assert get_findings(res, "C6", "MANUAL_REVIEW_REQUIRED")
    assert not get_findings(res, "C6", "FAIL")

def test_c6_comparability_cell_missing():
    txt = "Out-of-sample validation ledger"
    struct = {"blocks": [
        create_block("h", "heading", txt),
        create_block("r", "table_row", "Sim1 Obs Agreement without comparability", cells=[
            {"text": "Sim1"}, {"text": "Obs"}, {"text": "Agreement without comparability"}
        ])
    ]}
    res = validate_document(txt, struct)
    assert get_findings(res, "C6", "FAIL")

def test_c6_fractions_tags_missing():
    txt = "Feedback-relevant observables map"
    struct = {"blocks": [
        create_block("h", "heading", txt),
        create_block("r", "table_row", "Sim1 Quenched fractions: CALIBRATED", cells=[
            {"text": "Sim1"}, {"text": "Quenched fractions: CALIBRATED"}
        ])
    ]}
    res = validate_document(txt, struct)
    assert get_findings(res, "C6", "FAIL")

def test_c6_fractions_tags_pass():
    txt = "Feedback-relevant observables map"
    struct = {"blocks": [
        create_block("h", "heading", txt),
        create_block("r", "table_row", "Sim1 Quenched fractions: CALIBRATED (TRACER=NOT_APPLICABLE; SELECTION=NOT_APPLICABLE; DENOMINATOR=NOT_APPLICABLE; REDSHIFT=NOT_APPLICABLE)", cells=[
            {"text": "Sim1"}, {"text": "Quenched fractions: CALIBRATED (TRACER=NOT_APPLICABLE; SELECTION=NOT_APPLICABLE; DENOMINATOR=NOT_APPLICABLE; REDSHIFT=NOT_APPLICABLE)"}
        ])
    ]}
    res = validate_document(txt, struct)
    assert not get_findings(res, "C6", "FAIL")
    assert get_findings(res, "C6", "MANUAL_REVIEW_REQUIRED")

def test_c7_arxiv_normalization():
    txt = "See [https://arxiv.org/abs/1234.56789v2]"
    struct = {"blocks": [
        create_block("1", "paragraph", txt, links=[{"url": "https://arxiv.org/abs/1234.56789v2"}]),
        create_block("2", "heading", "Links ledger"),
        create_block("3", "paragraph", "123 | https://arxiv.org/html/1234.56789v3 | QUARANTINED", links=[{"url": "https://arxiv.org/html/1234.56789v3"}])
    ]}
    res = validate_document(txt, struct)
    assert not get_findings(res, "C7", "FAIL")

def test_c7_generic_url_normalization():
    txt = "See [http://a.com/path/v1.txt]"
    struct = {"blocks": [
        create_block("1", "paragraph", txt, links=[{"url": "http://a.com/path/v1.txt"}]),
        create_block("2", "heading", "Links ledger"),
        create_block("3", "paragraph", "[http://a.com/path/v1.txt]", links=[{"url": "http://a.com/path/v1.txt"}])
    ]}
    res = validate_document(txt, struct)
    assert not get_findings(res, "C7", "FAIL")
    
def test_c8_marker_duplicate():
    marker = "DONE"
    txt = "DONE\nDONE"
    res = validate_document(txt, {"blocks": []}, spec={"marker": marker})
    assert get_findings(res, "C8", "FAIL")

def test_c8_marker_not_final():
    marker = "DONE"
    txt = "DONE\nTrailing"
    res = validate_document(txt, {"blocks": []}, spec={"marker": marker})
    assert get_findings(res, "C8", "FAIL")

def test_failed_fixture():
    txt = (FIXTURES_DIR / "failed_c1.md").read_text()
    if not (FIXTURES_DIR / "failed_c1_structured.json").exists(): pytest.skip()
    struct = json.loads((FIXTURES_DIR / "failed_c1_structured.json").read_text())
    res = validate_document(txt, struct)
    assert res["overall"] == "FAIL"

def test_clean_fixture():
    if not (FIXTURES_DIR / "clean_c1_structured.json").exists(): pytest.skip()
    txt = (FIXTURES_DIR / "clean_c1.md").read_text()
    struct = json.loads((FIXTURES_DIR / "clean_c1_structured.json").read_text())
    spec = {
        "marker": "GEMINI_WEB_JOINT_C1R_OUTPUT_DONE_20260712T045317Z",
        "bidirectional_c7": True,
        "req_id": "REQ_JOINT_C1R_20260712T045317Z",
        "model": "Gemini Pro (selected UI mode; backend version not exposed)",
        "expected_sections": [
            "1. Calibration ledger", "2. Out-of-sample validation ledger",
            "3. Double-counting warnings", "4. Feedback-relevant observables map",
            "5. Gaps", "Links ledger",
        ],
    }
    res = validate_document(txt, struct, spec)
    assert res["overall"] == "MANUAL_REVIEW_REQUIRED"
    assert not any(f["status"] == "FAIL" for f in res["findings"])
