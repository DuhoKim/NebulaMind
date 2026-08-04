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


def block(block_id: str, block_type: str, text: str, *, section=None, cells=None, chips=None, resolved=None, links=None, gap_index=None):
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
    return value


def structure(blocks, *, ledger_entries=None):
    return {
        "schema": "NM_GEMINI_RENDERED_DOM_V2",
        "blocks": blocks,
        "chip_urls": {},
        "chip_index_occurrences": {},
        "chip_map_status": "OK",
        "chip_map_conflicts": [],
        "capture_flags": [],
        "ledger_entries": ledger_entries or [],
    }


def codes(result, clause=None, status=None):
    return [
        item
        for item in result["findings"]
        if (clause is None or item["clause"] == clause) and (status is None or item["status"] == status)
    ]


def has_code(result, code):
    return [item for item in result["findings"] if item["code"] == code]


def heading_blocks(order=SECTIONS):
    return [block(f"h{index}", "heading", title, section=title) for index, title in enumerate(order)]


def test_t7_structure_order_is_decoupled_from_empty_cells() -> None:
    empty_row = block("r", "table_row", "A\t", cells=[cell("simulation", "A"), cell("notes", "")])
    result = validate_document("", structure([*heading_blocks(), empty_row]), SPEC)
    assert has_code(result, "EMPTY_TABLE_CELL")
    assert not has_code(result, "BAD_STRUCTURE")
    assert has_code(result, "STRUCTURE_OK")

    scrambled = [SECTIONS[1], SECTIONS[0], *SECTIONS[2:]]
    result = validate_document("", structure(heading_blocks(scrambled)), SPEC)
    bad = has_code(result, "BAD_STRUCTURE")
    assert len(bad) == 1
    assert "set()" not in str(bad[0]["evidence"])
    assert SECTIONS[0] in str(bad[0]["evidence"])


def test_t8_fraction_qualifiers_require_a_numeric_fraction_or_incidence() -> None:
    no_value = block("plain", "paragraph", "The study examines cluster gas fractions without quoting a value.")
    result = validate_document(no_value["text"], structure([no_value]), SPEC)
    assert not has_code(result, "MISSING_QUALIFIER")

    numeric = block("numeric", "paragraph", "The quenched fraction is 23% in the selected sample.")
    result = validate_document(numeric["text"], structure([numeric]), SPEC)
    assert has_code(result, "MISSING_QUALIFIER")

    qualified = block(
        "qualified",
        "paragraph",
        "The quenched fraction is 23% (TRACER=colour; SELECTION=mass-limited; DENOMINATOR=all galaxies; REDSHIFT=z=0).",
    )
    result = validate_document(qualified["text"], structure([qualified]), SPEC)
    assert not has_code(result, "MISSING_QUALIFIER")
    assert has_code(result, "SEMANTIC_QUALIFIER")


def test_t9_c4_uses_typed_same_cell_claim_units() -> None:
    citation = cell("citation", "", chips=[27], resolved=[{"index": 27, "url": "https://example.test/source"}], cited=True)
    uncited_result = cell("result", "Agreement", claim_bearing=True, cited=False)
    row = block(
        "s2-row",
        "table_row",
        "Sim\tObs\tAgreement\tMATCHED_SELECTIONS\tNo\t",
        section="2. Out-of-sample validation ledger",
        cells=[
            cell("simulation", "Sim"),
            cell("observable", "Obs"),
            uncited_result,
            cell("comparability", "MATCHED_SELECTIONS"),
            cell("overlap", "No"),
            citation,
        ],
    )
    result = validate_document("", structure([row]), SPEC)
    assert not has_code(result, "UNCITED_CELL_CLAIM")
    assert ["s2-row", 2] in [
        item["source_refs"] for item in has_code(result, "CITED_CELL_CLAIM_REVIEW")
    ]

    row["cells"][2] = cell(
        "result",
        "Agreement",
        chips=[27],
        resolved=[{"index": 27, "url": "https://example.test/source"}],
        claim_bearing=True,
        cited=True,
    )
    result = validate_document("", structure([row]), SPEC)
    assert not has_code(result, "UNCITED_CELL_CLAIM")
    assert has_code(result, "CITED_CELL_CLAIM_REVIEW")

    s4 = block(
        "s4-row",
        "table_row",
        "Sim\tEMERGENT",
        section="4. Feedback-relevant observables map",
        cells=[cell("simulation", "Sim"), cell("quenched_fractions", "EMERGENT", claim_bearing=True, cited=False)],
    )
    result = validate_document("", structure([s4]), SPEC)
    assert ["s4-row", 1] in [item["source_refs"] for item in has_code(result, "UNCITED_CELL_CLAIM")]

    bullet = block(
        "bullet",
        "bullet",
        "Calibrated values are not predictions.",
        section="3. Double-counting warnings",
        chips=[3],
        resolved=[{"index": 3, "url": "https://example.test/bullet"}],
    )
    gap = block(
        "gap",
        "gap_line",
        "GAP: no systematic sample. ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED",
        section="5. Gaps",
        gap_index=2,
    )
    result = validate_document("", structure([bullet, gap]), SPEC)
    assert not has_code(result, "UNCITED_CLAIM")
    assert not has_code(result, "GAP_MISSING_VERIFICATION")


def test_t10_comparisons_are_scanned_per_typed_logical_unit() -> None:
    comparison = "EAGLE agrees with observed galaxy quenched fractions."
    emergent = block(
        "s1-row",
        "table_row",
        comparison,
        section="1. Calibration ledger",
        cells=[
            cell("simulation", "EAGLE"),
            cell("calibration_target", "The model was tuned to reproduce observed sizes."),
            cell("feedback_params", "NONE_FOUND"),
            cell("emergent", comparison, claim_bearing=True, cited=True, resolved=[{"index": 4, "url": "https://example.test/eagle"}]),
            cell("notes", "NONE_FOUND"),
        ],
    )
    result = validate_document("", structure([emergent]), SPEC)
    found = has_code(result, "UNLABELED_COMPARISON")
    assert ["s1-row", 3] in [item["source_refs"] for item in found]
    assert ["s1-row", 1] not in [item["source_refs"] for item in found]

    gap1 = block(
        "gap1",
        "gap_line",
        "GAP: simulations calibrated to clusters fail to predict observed lensing surveys.",
        section="5. Gaps",
        chips=[30],
        resolved=[{"index": 30, "url": "https://example.test/gap"}],
        gap_index=1,
    )
    gap2 = block(
        "gap2",
        "gap_line",
        "GAP: data remain unavailable. ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED",
        section="5. Gaps",
        gap_index=2,
    )
    result = validate_document("", structure([gap1, gap2]), SPEC)
    refs = [item["source_refs"] for item in has_code(result, "UNLABELED_COMPARISON")]
    assert ["gap1"] in refs
    assert ["gap2"] not in refs


def test_t11_exact_sentinels_are_enforced_once() -> None:
    malformed = block(
        "fire",
        "table_row",
        "FIRE\tNONE_FOUND.",
        section="1. Calibration ledger",
        cells=[cell("simulation", "FIRE"), cell("feedback_params", "NONE_FOUND.")],
    )
    result = validate_document("", structure([malformed]), SPEC)
    assert len(has_code(result, "SENTINEL_FORMAT_DEFECT")) == 1
    assert not has_code(result, "UNCITED_CELL_CLAIM")

    malformed["cells"][1] = cell("feedback_params", "NONE_FOUND")
    result = validate_document("", structure([malformed]), SPEC)
    assert not has_code(result, "SENTINEL_FORMAT_DEFECT")

    missing = block(
        "s4",
        "table_row",
        "Sim\tNOT_REPORTED",
        section="4. Feedback-relevant observables map",
        cells=[cell("simulation", "Sim"), cell("quenched_fractions", "NOT_REPORTED")],
    )
    result = validate_document("", structure([missing]), SPEC)
    assert has_code(result, "MISSING_NONE_FOUND")


def test_t12_c7_reports_one_integrity_failure_with_complete_evidence() -> None:
    body = block("body", "paragraph", "Claim", chips=[1], resolved=[{"index": 1, "url": "https://example.test/a"}])
    entries = [
        {"row": 1, "index": 1, "url": "https://example.test/a", "short_name": ""},
        {"row": 2, "index": 1, "url": "https://example.test/a", "short_name": ""},
        {"row": 3, "index": 2, "url": "https://arxiv.org/html/1234.56789v2", "short_name": ""},
    ]
    result = validate_document("", structure([body], ledger_entries=entries), SPEC)
    finding = has_code(result, "C7_INTEGRITY_FAILURE")
    assert len(finding) == 1
    evidence = finding[0]["evidence"]
    assert evidence["orphan_indices"] == [2]
    assert len(evidence["duplicate_rows"]) == 1
    assert evidence["blank_short_name_rows"] == [1, 2, 3]


def test_t13_semantic_families_remain_manual() -> None:
    cited = block(
        "cited",
        "paragraph",
        "This simulation was calibrated against observations.",
        chips=[1],
        resolved=[{"index": 1, "url": "https://example.test/source"}],
    )
    uncertainty = block("uncertain", "paragraph", "The value is 23 ± 4.")
    comparison = block(
        "s2",
        "table_row",
        "Sim\tObs\tAgreement\tMATCHED_SELECTIONS\tNo\t",
        section="2. Out-of-sample validation ledger",
        cells=[
            cell("simulation", "Sim"),
            cell("observable", "Obs"),
            cell("result", "Agreement", claim_bearing=True, cited=True, resolved=[{"index": 1, "url": "https://example.test/source"}]),
            cell("comparability", "MATCHED_SELECTIONS"),
            cell("overlap", "No"),
            cell("citation", "", chips=[1], resolved=[{"index": 1, "url": "https://example.test/source"}]),
        ],
    )
    result = validate_document("", structure([cited, uncertainty, comparison]), SPEC)
    manual_codes = {item["code"] for item in codes(result, status="MANUAL_REVIEW_REQUIRED")}
    assert "CITED_CLAIM_REVIEW" in manual_codes
    assert "UNCERTAINTY_CHECK" in manual_codes
    assert "COMPARISON_LABEL_REVIEW" in manual_codes
