from validator import validate_document

REQ = "REQ_JOINT_C1R_20260712T045317Z"
MODEL = "Gemini Pro (selected UI mode; backend version not exposed)"
MARKER = "GEMINI_WEB_JOINT_C1R_OUTPUT_DONE_20260712T045317Z"
SECTIONS = [
    "1. Calibration ledger",
    "2. Out-of-sample validation ledger",
    "3. Double-counting warnings",
    "4. Feedback-relevant observables map",
    "5. Gaps",
    "Links ledger",
]
SPEC = {
    "req_id": REQ,
    "model": MODEL,
    "marker": MARKER,
    "bidirectional_c7": True,
    "expected_sections": SECTIONS,
}


def block(block_id, block_type, text, *, cells=None, links=None):
    value = {
        "id": block_id,
        "type": block_type,
        "text": text,
        "source_lines": [],
        "links": links or [],
    }
    if cells is not None:
        value["cells"] = cells
    return value


def header_text(title=None, model=None):
    return "\n".join(
        [
            title or f"Joint C1R answer — {REQ}",
            "Run date (UTC): 2026-07-12T05:30:00Z",
            f"Model: {model or MODEL}",
            "Simulations covered: 8",
        ]
    )


def finding(result, clause, code=None):
    return [
        item
        for item in result["findings"]
        if item["clause"] == clause and (code is None or item["code"] == code)
    ]


def test_c1r_header_requires_exact_first_four_nonblank_lines():
    text = header_text()
    structured = {"blocks": [block("h", "heading", text)]}
    result = validate_document(text, structured, SPEC)
    assert not [item for item in finding(result, "C1") if item["status"] == "FAIL"]

    prefixed = "Unexpected preface\n" + text
    result = validate_document(prefixed, structured, SPEC)
    assert finding(result, "C1", "BAD_HEADER")


def test_c1r_structure_requires_numbered_section_headings_in_order():
    text = header_text() + "\n" + "\n".join(SECTIONS) + "\n" + MARKER
    structured = {
        "blocks": [block(str(index), "heading", name) for index, name in enumerate(SECTIONS)]
    }
    result = validate_document(text, structured, SPEC)
    assert not [item for item in finding(result, "C2") if item["status"] == "FAIL"]

    old = [name.split(". ", 1)[-1] for name in SECTIONS]
    structured = {
        "blocks": [block(str(index), "heading", name) for index, name in enumerate(old)]
    }
    result = validate_document(text, structured, SPEC)
    assert finding(result, "C2", "BAD_STRUCTURE")


def test_c4_section_one_claim_cell_requires_its_own_citation():
    row = block(
        "cal-row",
        "table_row",
        "Sim | stellar mass function at z=0 | NONE_FOUND | NONE_FOUND | NONE_FOUND",
        cells=[
            {"text": "Sim [https://example.org/method]", "links": [{"url": "https://example.org/method"}]},
            {"text": "stellar mass function at z=0", "links": []},
            {"text": "NONE_FOUND", "links": []},
            {"text": "NONE_FOUND", "links": []},
            {"text": "NONE_FOUND", "links": []},
        ],
    )
    row["section"] = "1. Calibration ledger"
    result = validate_document("", {"blocks": [row]}, SPEC)
    uncited = finding(result, "C4", "UNCITED_CELL_CLAIM")
    assert uncited
    assert ["cal-row", 1] in [item["source_refs"] for item in uncited]


def test_c6_uses_dedicated_comparability_column_not_result_column():
    valid = block(
        "val-row",
        "table_row",
        "Sim | Obs | Agreement | MATCHED_SELECTIONS | NONE_FOUND | citation",
        cells=[
            {"text": "Sim"},
            {"text": "Obs"},
            {"text": "Agreement"},
            {"text": "MATCHED_SELECTIONS"},
            {"text": "NONE_FOUND"},
            {"text": "https://example.org/validation", "links": [{"url": "https://example.org/validation"}]},
        ],
    )
    valid["section"] = "2. Out-of-sample validation ledger"
    result = validate_document("", {"blocks": [valid]}, SPEC)
    assert not finding(result, "C6", "MISSING_COMPARABILITY")

    misplaced = block(
        "val-row-bad",
        "table_row",
        "Sim | Obs | Agreement MATCHED_SELECTIONS | NONE_FOUND | NONE_FOUND | citation",
        cells=[
            {"text": "Sim"},
            {"text": "Obs"},
            {"text": "Agreement MATCHED_SELECTIONS"},
            {"text": "NONE_FOUND"},
            {"text": "NONE_FOUND"},
            {"text": "https://example.org/validation", "links": [{"url": "https://example.org/validation"}]},
        ],
    )
    misplaced["section"] = "2. Out-of-sample validation ledger"
    result = validate_document("", {"blocks": [misplaced]}, SPEC)
    assert finding(result, "C6", "MISSING_COMPARABILITY")


def test_c6_qualifier_values_must_be_nonempty():
    row = block(
        "fraction-row",
        "table_row",
        "Quenched fraction TRACER=; SELECTION=sample; DENOMINATOR=galaxies; REDSHIFT=z0",
        cells=[
            {"text": "Quenched fraction TRACER=; SELECTION=sample; DENOMINATOR=galaxies; REDSHIFT=z0"}
        ],
    )
    row["section"] = "4. Feedback-relevant observables map"
    result = validate_document("", {"blocks": [row]}, SPEC)
    assert finding(result, "C6", "MISSING_QUALIFIER")


def test_c2_section_four_not_reported_requires_none_found():
    row = block(
        "map-row",
        "table_row",
        "ASTRID | NOT_REPORTED | NOT_REPORTED — NONE_FOUND",
        cells=[
            {"text": "ASTRID"},
            {"text": "NOT_REPORTED"},
            {"text": "NOT_REPORTED — NONE_FOUND"},
        ],
    )
    row["section"] = "4. Feedback-relevant observables map"
    result = validate_document("", {"blocks": [row]}, SPEC)
    missing = finding(result, "C2", "MISSING_NONE_FOUND")
    assert missing
    assert ["map-row", 1] in [item["source_refs"] for item in missing]


def test_c6_unlabeled_comparison_outside_section_two_is_rejected():
    text = "ASTRID agrees with observations for the UV luminosity function."
    paragraph = block("comparison", "paragraph", text)
    paragraph["section"] = "3. Double-counting warnings"
    result = validate_document(text, {"blocks": [paragraph]}, SPEC)
    assert finding(result, "C6", "UNLABELED_COMPARISON")

    labeled_text = text + " MATCHED_SELECTIONS"
    paragraph = block("comparison-labeled", "paragraph", labeled_text)
    paragraph["section"] = "3. Double-counting warnings"
    result = validate_document(labeled_text, {"blocks": [paragraph]}, SPEC)
    assert not finding(result, "C6", "UNLABELED_COMPARISON")
