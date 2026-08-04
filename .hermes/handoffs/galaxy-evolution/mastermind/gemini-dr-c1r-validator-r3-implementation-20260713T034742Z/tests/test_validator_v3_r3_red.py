from __future__ import annotations

import sys
from pathlib import Path

PACKET = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKET / "validator"))
from validator_v3 import validate_document  # noqa: E402

SECTIONS = [
    "1. Calibration ledger",
    "2. Out-of-sample validation ledger",
    "3. Double-counting warnings",
    "4. Feedback-relevant observables map",
    "5. Gaps",
    "Links ledger",
]
SPEC = {
    "marker": "",
    "expected_sections": SECTIONS,
    "bidirectional_c7": True,
    "section_columns": {
        "1. Calibration ledger": ["simulation", "calibration_target", "feedback_params", "emergent", "notes"],
        "2. Out-of-sample validation ledger": ["simulation", "observable", "result", "comparability", "overlap", "citation"],
        "4. Feedback-relevant observables map": ["simulation", "quenched_fractions", "gas_fractions", "outflow_demographics", "hot_halo_cavity", "radio_agn_incidence"],
    },
}

def cell(role: str, text: str, *, chips=None, resolved=None, links=None, claim_bearing=False, cited=None):
    resolved = resolved or []
    links = links or []
    if cited is None:
        cited = bool(resolved or links)
    return {
        "role": role,
        "text": text,
        "chips": chips or [],
        "resolved_citations": resolved,
        "unresolved_chips": [],
        "links": links,
        "claim_bearing": claim_bearing,
        "cited": cited,
    }

def block(block_id: str, block_type: str, text: str, *, section=None, cells=None, chips=None, resolved=None, links=None, gap_index=None, parent_path=None):
    value = {
        "id": block_id,
        "type": block_type,
        "text": text,
        "section": section,
        "source_lines": [],
        "links": links or [],
        "chips": chips or [],
        "resolved_citations": resolved or [],
        "unresolved_chips": [],
    }
    if cells is not None:
        value["cells"] = cells
    if gap_index is not None:
        value["gap_index"] = gap_index
    if parent_path is not None:
        value["parent_path"] = parent_path
    return value

def structure(blocks, *, ledger_entries=None):
    return {
        "schema": "NM_GEMINI_RENDERED_DOM_V3",
        "blocks": blocks,
        "chip_urls": {},
        "chip_index_occurrences": {},
        "chip_map_status": "OK",
        "chip_map_conflicts": [],
        "capture_flags": [],
        "ledger_entries": ledger_entries or [],
    }

def has_code(result, code):
    return [item for item in result["findings"] if item["code"] == code]

def heading_blocks(order=SECTIONS):
    return [block(f"h{index}", "heading", title, section=title) for index, title in enumerate(order)]

def test_d5_gap_multiple_per_paragraph() -> None:
    gap1 = block("gap1", "gap_line", "GAP: one", section="5. Gaps", gap_index=1, parent_path="p1")
    gap2 = block("gap2", "gap_line", "GAP: two", section="5. Gaps", gap_index=2, parent_path="p1")
    gap3 = block("gap3", "gap_line", "GAP: three", section="5. Gaps", gap_index=3, parent_path="p1")
    gap4 = block("gap4", "gap_line", "GAP: four", section="5. Gaps", gap_index=4, parent_path="p1")
    result = validate_document("", structure([*heading_blocks(), gap1, gap2, gap3, gap4]), SPEC)
    assert len(has_code(result, "GAP_MULTIPLE_PER_PARAGRAPH")) == 1

    gap1_p = block("gap1_p", "gap_line", "GAP: one", section="5. Gaps", gap_index=1, parent_path="p1")
    gap2_p = block("gap2_p", "gap_line", "GAP: two", section="5. Gaps", gap_index=2, parent_path="p2")
    gap3_p = block("gap3_p", "gap_line", "GAP: three", section="5. Gaps", gap_index=3, parent_path="p3")
    gap4_p = block("gap4_p", "gap_line", "GAP: four", section="5. Gaps", gap_index=4, parent_path="p4")
    result_p = validate_document("", structure([*heading_blocks(), gap1_p, gap2_p, gap3_p, gap4_p]), SPEC)
    assert not has_code(result_p, "GAP_MULTIPLE_PER_PARAGRAPH")

def test_d4_ledger_integrity() -> None:
    body = block("body", "paragraph", "Claim", chips=[1], resolved=[{"index": 1, "url": "https://example.test/a"}])
    entries_fail = [
        {"row": 1, "index": 1, "url": "https://example.test/a", "short_name": ""},
        {"row": 2, "index": 1, "url": "https://example.test/a", "short_name": ""},
        {"row": 3, "index": 2, "url": "https://arxiv.org/html/1234.56789v2", "short_name": ""},
    ]
    result = validate_document("", structure([body], ledger_entries=entries_fail), SPEC)
    assert len(has_code(result, "C7_INTEGRITY_FAILURE")) == 1
    
    # arXiv variants auto-merge: should NOT produce near-duplicate, but WILL produce duplicate rows under C7_INTEGRITY_FAILURE
    entries_arxiv = [
        {"row": 1, "index": 1, "url": "https://arxiv.org/abs/1234.56789v1", "short_name": "A1"},
        {"row": 2, "index": 2, "url": "https://arxiv.org/html/1234.56789", "short_name": "A2"},
        {"row": 3, "index": 3, "url": "https://arxiv.org/pdf/1234.56789v2.pdf", "short_name": "A3"},
    ]
    body1 = block("body1", "paragraph", "C", chips=[1], resolved=[{"index": 1, "url": entries_arxiv[0]["url"]}])
    body2 = block("body2", "paragraph", "C", chips=[2], resolved=[{"index": 2, "url": entries_arxiv[1]["url"]}])
    body3 = block("body3", "paragraph", "C", chips=[3], resolved=[{"index": 3, "url": entries_arxiv[2]["url"]}])
    result_arxiv = validate_document("", structure([body1, body2, body3], ledger_entries=entries_arxiv), SPEC)
    assert not has_code(result_arxiv, "C7_NEAR_DUPLICATE")
    
    # We expect C7_INTEGRITY_FAILURE because there are 3 indices that represent the same paper, thus they are duplicate rows
    c7_arxiv = has_code(result_arxiv, "C7_INTEGRITY_FAILURE")
    assert len(c7_arxiv) == 1
    assert len(c7_arxiv[0]["evidence"]["duplicate_rows"]) == 2
    
    # 14/29 near duplicate
    entries_near = [
        {"row": 1, "index": 1, "url": "https://academic.oup.com/mnras/article/470/1/1121/3828081", "short_name": "Art1"},
        {"row": 2, "index": 2, "url": "https://academic.oup.com/mnras/article-abstract/470/1/1121/3828081", "short_name": "Art2"},
    ]
    body1_n = block("body1_n", "paragraph", "Claim1", chips=[1], resolved=[{"index": 1, "url": entries_near[0]["url"]}])
    body2_n = block("body2_n", "paragraph", "Claim2", chips=[2], resolved=[{"index": 2, "url": entries_near[1]["url"]}])
    result_near = validate_document("", structure([body1_n, body2_n], ledger_entries=entries_near), SPEC)
    assert len(has_code(result_near, "C7_NEAR_DUPLICATE")) == 1

def test_d2_missing_qualifier() -> None:
    # Negative: SIMBA ~10%
    numeric = block("numeric", "table_row", "sim\ttarget\t~10%\temergent\tnotes", section="1. Calibration ledger", cells=[
        cell("simulation", "SIMBA"), cell("calibration_target", "NONE_FOUND."), cell("feedback_params", "couples ~10%"), cell("emergent", "NONE_FOUND."), cell("notes", "")
    ])
    result = validate_document("", structure([*heading_blocks(), numeric]), SPEC)
    assert has_code(result, "MISSING_QUALIFIER")

    # Positive: MODEL_PARAMETER
    qualified = block("qualified", "table_row", "sim\ttarget\t~10%\temergent\tnotes", section="1. Calibration ledger", cells=[
        cell("simulation", "SIMBA"), cell("calibration_target", "NONE_FOUND."), 
        cell("feedback_params", "couples ~10% TRACER=MODEL_PARAMETER; SELECTION=NOT_APPLICABLE; DENOMINATOR=SN; REDSHIFT=NOT_APPLICABLE"), 
        cell("emergent", "NONE_FOUND."), cell("notes", "")
    ])
    result_q = validate_document("", structure([*heading_blocks(), qualified]), SPEC)
    assert not has_code(result_q, "MISSING_QUALIFIER")
    assert has_code(result_q, "SEMANTIC_QUALIFIER")

    # Positive: non-numeric word "fraction"/"incidence"
    non_numeric = block("non_numeric", "table_row", "sim\ttarget\tfraction\temergent\tnotes", section="1. Calibration ledger", cells=[
        cell("simulation", "SIMBA"), cell("calibration_target", "NONE_FOUND."), cell("feedback_params", "cluster gas fraction incidence"), cell("emergent", "NONE_FOUND."), cell("notes", "")
    ])
    result_nn = validate_document("", structure([*heading_blocks(), non_numeric]), SPEC)
    assert not has_code(result_nn, "MISSING_QUALIFIER")
    assert not has_code(result_nn, "SEMANTIC_QUALIFIER")

    # Positive: observational numeric fraction with real 4-field tuple
    obs_numeric = block("obs_numeric", "table_row", "sim\ttarget\t20%\temergent\tnotes", section="1. Calibration ledger", cells=[
        cell("simulation", "SIMBA"), cell("calibration_target", "NONE_FOUND."), cell("feedback_params", "20% TRACER=mass; SELECTION=halo; DENOMINATOR=total; REDSHIFT=z=0"), cell("emergent", "NONE_FOUND."), cell("notes", "")
    ])
    result_on = validate_document("", structure([*heading_blocks(), obs_numeric]), SPEC)
    assert not has_code(result_on, "MISSING_QUALIFIER")
    assert has_code(result_on, "SEMANTIC_QUALIFIER")

def test_d1_missing_calibration_target_prefix() -> None:
    # Negative: No prefix but references observation
    unprefixed = block("unprefixed", "table_row", "sim\tmatch observation\tNONE\tNONE\tNONE", section="1. Calibration ledger", cells=[
        cell("simulation", "SIMBA"), cell("calibration_target", "calibrated to reproduce the observed mass"), cell("feedback_params", "NONE_FOUND"), cell("emergent", "NONE_FOUND"), cell("notes", "NONE_FOUND")
    ])
    result = validate_document("", structure([*heading_blocks(), unprefixed]), SPEC)
    assert len(has_code(result, "MISSING_CALIBRATION_TARGET_PREFIX")) == 1

    # Positive: Prefixed
    prefixed = block("prefixed", "table_row", "sim\tmatch observation\tNONE\tNONE\tNONE", section="1. Calibration ledger", cells=[
        cell("simulation", "SIMBA"), cell("calibration_target", "CALIBRATION_TARGET_DESCRIPTION: calibrated to reproduce the observed mass"), cell("feedback_params", "NONE_FOUND"), cell("emergent", "NONE_FOUND"), cell("notes", "NONE_FOUND")
    ])
    result_p = validate_document("", structure([*heading_blocks(), prefixed]), SPEC)
    assert not has_code(result_p, "MISSING_CALIBRATION_TARGET_PREFIX")

    # Positive: no-observation reference
    no_obs = block("no_obs", "table_row", "sim\tmatch observation\tNONE\tNONE\tNONE", section="1. Calibration ledger", cells=[
        cell("simulation", "SIMBA"), cell("calibration_target", "adjusted parameters governing galactic winds"), cell("feedback_params", "NONE_FOUND"), cell("emergent", "NONE_FOUND"), cell("notes", "NONE_FOUND")
    ])
    result_no_obs = validate_document("", structure([*heading_blocks(), no_obs]), SPEC)
    assert not has_code(result_no_obs, "MISSING_CALIBRATION_TARGET_PREFIX")

    # Positive: NONE_FOUND exemption
    none_found = block("none_found", "table_row", "sim\tmatch observation\tNONE\tNONE\tNONE", section="1. Calibration ledger", cells=[
        cell("simulation", "SIMBA"), cell("calibration_target", "NONE_FOUND."), cell("feedback_params", "NONE_FOUND"), cell("emergent", "NONE_FOUND"), cell("notes", "NONE_FOUND")
    ])
    result_nf = validate_document("", structure([*heading_blocks(), none_found]), SPEC)
    assert not has_code(result_nf, "MISSING_CALIBRATION_TARGET_PREFIX")

    # Positive: retained emergent-token MANUAL behavior with correct comparison-bearing text
    emergent_man = block("emergent_man", "table_row", "sim\tmatch observation\tNONE\tSIMBA matches observed data MATCHED_SELECTIONS\tNONE", section="1. Calibration ledger", cells=[
        cell("simulation", "SIMBA"), cell("calibration_target", "NONE_FOUND"), cell("feedback_params", "NONE_FOUND"), cell("emergent", "SIMBA matches observed data MATCHED_SELECTIONS", claim_bearing=True, cited=True, resolved=[{"index": 1, "url": "https://e"}]), cell("notes", "NONE_FOUND")
    ])
    result_em = validate_document("", structure([*heading_blocks(), emergent_man]), SPEC)
    assert has_code(result_em, "COMPARISON_LABEL_REVIEW")
    assert not has_code(result_em, "UNLABELED_COMPARISON")

def test_d3_cited_cell_claim_review() -> None:
    # Negative: empty citation cell
    empty_cit = block("empty_cit", "table_row", "sim\tobs\tres\tMATCHED_SELECTIONS\tNo\t", section="2. Out-of-sample validation ledger", cells=[
        cell("simulation", "sim"), cell("observable", "obs"), cell("result", "Agreement"), cell("comparability", "MATCHED_SELECTIONS"), cell("overlap", "No"), cell("citation", "")
    ])
    result = validate_document("", structure([*heading_blocks(), empty_cit]), SPEC)
    assert len(has_code(result, "EMPTY_CITATION_CELL")) == 1

    # Negative: missing citation cell entirely
    missing_cit = block("missing_cit", "table_row", "sim\tobs\tres\tMATCHED_SELECTIONS\tNo\t", section="2. Out-of-sample validation ledger", cells=[
        cell("simulation", "sim"), cell("observable", "obs"), cell("result", "Agreement"), cell("comparability", "MATCHED_SELECTIONS"), cell("overlap", "No")
    ])
    result_missing = validate_document("", structure([*heading_blocks(), missing_cit]), SPEC)
    assert len(has_code(result_missing, "EMPTY_CITATION_CELL")) == 1

    # Positive: populated citation cell -> CITED_CELL_CLAIM_REVIEW
    pop_cit = block("pop_cit", "table_row", "sim\tobs\tres\tMATCHED_SELECTIONS\tNo\t", section="2. Out-of-sample validation ledger", cells=[
        cell("simulation", "sim"), cell("observable", "obs"), cell("result", "Agreement"), cell("comparability", "MATCHED_SELECTIONS"), cell("overlap", "No"), cell("citation", "", chips=[1], resolved=[{"index": 1, "url": "https://example.test"}])
    ])
    result_p = validate_document("", structure([*heading_blocks(), pop_cit]), SPEC)
    assert not has_code(result_p, "UNCITED_CELL_CLAIM")
    rev = has_code(result_p, "CITED_CELL_CLAIM_REVIEW")
    assert len(rev) == 1
    assert rev[0]["source_refs"] == ["pop_cit", 2]
