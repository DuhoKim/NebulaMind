from __future__ import annotations

import re
from collections import defaultdict
from typing import Any, Iterable


COMPARABILITY_TOKENS = {
    "MATCHED_SELECTIONS",
    "NON_COMMENSURABLE_UNMATCHED_SELECTIONS",
}
ABSENCE_TOKEN = "ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED"
UNCERTAINTY_TOKEN = "UNCERTAINTY_NOT_QUOTED_BY_SOURCE"
CHECKABLE_CITATION_RE = re.compile(
    r"(?:\barXiv:\d{4}\.\d{4,5}(?:v\d+)?\b|"
    r"arxiv\.org/(?:abs|html|pdf)/\d{4}\.\d{4,5}(?:v\d+)?|"
    r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+\b|"
    r"\b\d{4}[A-Za-z][A-Za-z0-9.&]{14,}\b|"
    r"https?://[^\s\]]+)",
    re.IGNORECASE,
)
SIMULATION_RE = re.compile(
    r"\b(?:IllustrisTNG|TNG|EAGLE|SIMBA|FIRE(?:-2)?|ROMULUS|ASTRID|FLAMINGO|BAHAMAS|"
    r"simulations?|suites?|models?)\b",
    re.IGNORECASE,
)
OBSERVATION_RE = re.compile(
    r"\b(?:observed|observations?|observational|surveys?|empirical|data)\b",
    re.IGNORECASE,
)
S1_EMERGENT_NAMED_OBSERVABLE_RE = re.compile(
    r"(?:cluster scaling relations|thermodynamic density and temperature profiles)",
    re.IGNORECASE,
)
RESULT_RE = re.compile(
    r"\b(?:agrees?|agreement|matches?|reproduces?|consistent|tension|discrepan\w+|offset|"
    r"over-?predicts?|under-?predicts?|fails?(?:\s+to)?)\b",
    re.IGNORECASE,
)
NUMERIC_FRACTION_PATTERNS = [
    re.compile(r"\b\d+(?:\.\d+)?\s?%"),
    re.compile(r"\b\d+(?:\.\d+)?\s?(?:per ?cent|percent)\b", re.IGNORECASE),
    re.compile(r"\b\d+\s?/\s?\d+\b"),
    re.compile(r"\b(?:fraction|incidence)\b[^.]{0,40}?\b\d+(?:\.\d+)?\b", re.IGNORECASE),
    re.compile(r"\b\d+(?:\.\d+)?\b[^.]{0,40}?\b(?:fraction|incidence)\b", re.IGNORECASE),
]
QUALIFIER_RE = re.compile(
    r"TRACER=[^;()]+;\s*SELECTION=[^;()]+;\s*DENOMINATOR=[^;()]+;\s*REDSHIFT=[^)]+",
    re.IGNORECASE,
)
QUANTITY_RE = re.compile(
    r"\b\d+(?:\.\d+)?\s*(?:%|dex|kpc|Mpc|km\s*s?-1|yr|Myr|Gyr|M(?:sun|☉))\b",
    re.IGNORECASE,
)


def _finding(
    clause: str,
    status: str,
    code: str,
    evidence: Any,
    source_refs: list[Any] | None = None,
) -> dict[str, Any]:
    return {
        "clause": clause,
        "status": status,
        "code": code,
        "evidence": evidence,
        "source_refs": source_refs or [],
    }


def _normalise_url(value: str) -> str:
    url = str(value or "").strip().rstrip(".,;:)'\"]")
    return re.sub(
        r"(arxiv\.org)/(?:abs|html|pdf)/(\d+\.\d+)(?:v\d+)?",
        r"\1/abs/\2",
        url,
        flags=re.IGNORECASE,
    )


def _is_cited(unit: dict[str, Any]) -> bool:
    text = str(unit.get("text", ""))
    if "UNCITED_NOT_USABLE" in text:
        return False
    return bool(
        unit.get("cited")
        or unit.get("resolved_citations")
        or unit.get("links")
        or CHECKABLE_CITATION_RE.search(text)
    )


def _has_numeric_fraction(text: str) -> bool:
    return any(pattern.search(text) for pattern in NUMERIC_FRACTION_PATTERNS)


def _iter_units(blocks: list[dict[str, Any]]) -> Iterable[tuple[str, list[Any], str, str | None]]:
    for block in blocks:
        if block.get("type") in {"heading", "table_header"}:
            continue
        section = block.get("section")
        if section == "Links ledger":
            continue
        if block.get("type") == "table_row":
            for index, cell in enumerate(block.get("cells", [])):
                yield str(cell.get("text", "")), [block.get("id"), index], str(cell.get("role", "")), section
            continue
        role = "bullet" if block.get("type") == "bullet" else "gap_line" if block.get("type") == "gap_line" else "paragraph"
        yield str(block.get("text", "")), [block.get("id")], role, section


def _capture_guard(structured: dict[str, Any], findings: list[dict[str, Any]]) -> None:
    if structured.get("schema") != "NM_GEMINI_RENDERED_DOM_V2":
        findings.append(
            _finding(
                "CAPTURE",
                "FAIL",
                "CAPTURE_SCHEMA_MISMATCH",
                {"actual": structured.get("schema"), "expected": "NM_GEMINI_RENDERED_DOM_V2"},
            )
        )
    if structured.get("chip_map_status") == "FAIL_CLOSED":
        findings.append(
            _finding(
                "CAPTURE",
                "FAIL",
                "CHIP_MAP_FAIL_CLOSED",
                structured.get("chip_map_conflicts", []),
            )
        )
    if structured.get("capture_flags"):
        findings.append(
            _finding(
                "CAPTURE",
                "FAIL",
                "CAPTURE_FLAGS",
                list(structured.get("capture_flags", [])),
            )
        )


def _check_c1(body: str, spec: dict[str, Any], findings: list[dict[str, Any]]) -> None:
    req_id = str(spec.get("req_id") or "")
    model = str(spec.get("model") or "")
    if not req_id or not model:
        findings.append(_finding("C1", "PASS", "NO_SPEC_PROVIDED", ""))
        return
    header = [line.strip() for line in body.splitlines() if line.strip()][:4]
    expected_title = str(spec.get("title") or f"Joint C1R answer — {req_id}")
    valid = (
        len(header) == 4
        and header[0].lstrip("# ") == expected_title
        and bool(re.fullmatch(r"Run date \(UTC\): \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", header[1]))
        and header[2] == f"Model: {model}"
        and bool(re.fullmatch(r"Simulations covered: \d+", header[3]))
    )
    if valid:
        findings.append(_finding("C1", "PASS", "C1_OK", header))
    else:
        findings.append(_finding("C1", "FAIL", "BAD_HEADER", {"expected_title": expected_title, "observed": header}))


def _check_c2(
    blocks: list[dict[str, Any]],
    spec: dict[str, Any],
    findings: list[dict[str, Any]],
) -> None:
    expected = list(spec.get("expected_sections") or [])
    headings = [
        str(block.get("text", ""))
        for block in blocks
        if block.get("type") == "heading" and str(block.get("text", "")) in expected
    ]
    missing = [section for section in expected if section not in headings]
    positions = [headings.index(section) for section in expected if section in headings]
    order_bad = positions != sorted(positions)
    if missing or order_bad:
        findings.append(
            _finding(
                "C2",
                "FAIL",
                "BAD_STRUCTURE",
                {"expected": expected, "observed": headings, "missing": missing, "order_bad": order_bad},
            )
        )
    else:
        findings.append(_finding("C2", "PASS", "STRUCTURE_OK", {"observed": headings}))

    for block in blocks:
        if block.get("type") == "table_row":
            for index, cell in enumerate(block.get("cells", [])):
                text = str(cell.get("text", "")).strip()
                refs = [block.get("id"), index]
                if not text and not cell.get("chips") and not cell.get("links"):
                    findings.append(_finding("C2", "FAIL", "EMPTY_TABLE_CELL", "", refs))
                if text.startswith("NONE_FOUND") and text != "NONE_FOUND":
                    findings.append(_finding("C2", "FAIL", "SENTINEL_FORMAT_DEFECT", text, refs))
                if block.get("section") == "4. Feedback-relevant observables map" and text.startswith("NOT_REPORTED") and "NONE_FOUND" not in text:
                    findings.append(_finding("C2", "FAIL", "MISSING_NONE_FOUND", text, refs))
        if block.get("type") == "gap_line":
            text = str(block.get("text", ""))
            if not _is_cited(block) and ABSENCE_TOKEN not in text:
                code = "UNRESOLVED_CITATION" if block.get("unresolved_chips") else "GAP_MISSING_VERIFICATION"
                findings.append(_finding("C2", "FAIL", code, text[:160], [block.get("id")]))


def _check_c3(blocks: list[dict[str, Any]], findings: list[dict[str, Any]]) -> None:
    for text, refs, _role, _section in _iter_units(blocks):
        if not text:
            continue
        if "±" in text or UNCERTAINTY_TOKEN in text:
            findings.append(_finding("C3", "MANUAL_REVIEW_REQUIRED", "UNCERTAINTY_CHECK", text[:180], refs))
        elif QUANTITY_RE.search(text):
            findings.append(_finding("C3", "FAIL", "BARE_QUANTITY", text[:180], refs))


def _check_claim(
    unit: dict[str, Any],
    refs: list[Any],
    cell: bool,
    findings: list[dict[str, Any]],
) -> None:
    text = str(unit.get("text", ""))
    if text.startswith("NONE_FOUND") or (unit.get("role") and not unit.get("claim_bearing")):
        return
    if "UNCITED_NOT_USABLE" in text:
        findings.append(
            _finding("C4", "MANUAL_REVIEW_REQUIRED", "UNCITED_DECLARED_NOT_USABLE", text[:180], refs)
        )
        return
    if unit.get("unresolved_chips"):
        findings.append(_finding("C4", "FAIL", "UNRESOLVED_CITATION", unit.get("unresolved_chips"), refs))
        return
    if _is_cited(unit):
        findings.append(
            _finding(
                "C4",
                "MANUAL_REVIEW_REQUIRED",
                "CITED_CELL_CLAIM_REVIEW" if cell else "CITED_CLAIM_REVIEW",
                text[:180],
                refs,
            )
        )
        return
    findings.append(
        _finding("C4", "FAIL", "UNCITED_CELL_CLAIM" if cell else "UNCITED_CLAIM", text[:180], refs)
    )


def _check_c4(blocks: list[dict[str, Any]], findings: list[dict[str, Any]]) -> None:
    resolved_count = 0
    for block in blocks:
        if block.get("section") == "Links ledger" or block.get("type") in {"heading", "table_header"}:
            continue
        if block.get("type") == "table_row":
            for index, cell in enumerate(block.get("cells", [])):
                resolved_count += len(cell.get("resolved_citations", []))
                if cell.get("claim_bearing"):
                    _check_claim(cell, [block.get("id"), index], True, findings)
            continue
        resolved_count += len(block.get("resolved_citations", []))
        if block.get("type") == "gap_line" and ABSENCE_TOKEN in str(block.get("text", "")):
            continue
        if block.get("type") in {"bullet", "gap_line"} or block.get("resolved_citations"):
            _check_claim(block, [block.get("id")], False, findings)

    if resolved_count:
        findings.append(
            _finding(
                "C4",
                "MANUAL_REVIEW_REQUIRED",
                "CITATION_QUALITY_REVIEW",
                {"resolved_citation_occurrences": resolved_count},
            )
        )
        findings.append(
            _finding(
                "C4",
                "MANUAL_REVIEW_REQUIRED",
                "SOURCE_FIDELITY_REVIEW",
                {"resolved_citation_occurrences": resolved_count},
            )
        )


def _check_c5(body: str, spec: dict[str, Any], findings: list[dict[str, Any]]) -> None:
    banned = [str(value) for value in spec.get("banned_tokens", ["hero_facts"])]
    present = [token for token in banned if token and token.lower() in body.lower()]
    if present:
        findings.append(_finding("C5", "FAIL", "BANNED_WORD", present))
    else:
        findings.append(_finding("C5", "PASS", "C5_OK", ""))


def _check_c6(blocks: list[dict[str, Any]], findings: list[dict[str, Any]]) -> None:
    for block in blocks:
        if block.get("type") != "table_row" or block.get("section") != "2. Out-of-sample validation ledger":
            continue
        comparability = [
            (index, cell)
            for index, cell in enumerate(block.get("cells", []))
            if cell.get("role") == "comparability"
        ]
        if not comparability or str(comparability[0][1].get("text", "")).strip() not in COMPARABILITY_TOKENS:
            refs = [block.get("id"), comparability[0][0] if comparability else 3]
            findings.append(_finding("C6", "FAIL", "MISSING_COMPARABILITY", block.get("text", "")[:180], refs))
        else:
            index, cell = comparability[0]
            findings.append(
                _finding(
                    "C6",
                    "MANUAL_REVIEW_REQUIRED",
                    "COMPARISON_LABEL_REVIEW",
                    cell.get("text", ""),
                    [block.get("id"), index],
                )
            )

    for text, refs, role, section in _iter_units(blocks):
        if _has_numeric_fraction(text):
            if QUALIFIER_RE.search(text):
                findings.append(_finding("C6", "MANUAL_REVIEW_REQUIRED", "SEMANTIC_QUALIFIER", text[:180], refs))
            else:
                findings.append(_finding("C6", "FAIL", "MISSING_QUALIFIER", text[:180], refs))

        comparison_role = role == "emergent" or role == "gap_line"
        if section == "2. Out-of-sample validation ledger" or not comparison_role:
            continue
        observation_reference = bool(OBSERVATION_RE.search(text)) or bool(
            role == "emergent"
            and section == "1. Calibration ledger"
            and S1_EMERGENT_NAMED_OBSERVABLE_RE.search(text)
        )
        is_comparison = bool(SIMULATION_RE.search(text) and observation_reference and RESULT_RE.search(text))
        if not is_comparison:
            continue
        if any(token in text for token in COMPARABILITY_TOKENS):
            findings.append(_finding("C6", "MANUAL_REVIEW_REQUIRED", "COMPARISON_LABEL_REVIEW", text[:180], refs))
        else:
            findings.append(_finding("C6", "FAIL", "UNLABELED_COMPARISON", text[:180], refs))


def _near_duplicate_indices(entries: list[dict[str, Any]]) -> list[list[int]]:
    groups: dict[str, set[int]] = defaultdict(set)
    exact: dict[str, set[str]] = defaultdict(set)
    for entry in entries:
        url = _normalise_url(str(entry.get("url", "")))
        key = url.replace("/article-abstract/", "/article/")
        groups[key].add(int(entry.get("index") or 0))
        exact[key].add(url)
    pairs: list[list[int]] = []
    for key in sorted(groups):
        if len(exact[key]) > 1 and len(groups[key]) > 1:
            pairs.append(sorted(groups[key]))
    return pairs


def _body_indices(blocks: list[dict[str, Any]]) -> set[int]:
    result: set[int] = set()
    for block in blocks:
        if block.get("section") == "Links ledger":
            continue
        result.update(int(value) for value in block.get("chips", []))
        for cell in block.get("cells", []):
            result.update(int(value) for value in cell.get("chips", []))
    return result


def _check_c7(structured: dict[str, Any], findings: list[dict[str, Any]]) -> None:
    entries = list(structured.get("ledger_entries") or [])
    if not entries:
        findings.append(_finding("C7", "PASS", "C7_OK", {"ledger_rows": 0}))
        return
    ledger_indices = {int(entry.get("index")) for entry in entries}
    body_indices = _body_indices(list(structured.get("blocks") or []))
    orphan = sorted(ledger_indices - body_indices)
    inline_only = sorted(body_indices - ledger_indices)

    seen_urls: set[str] = set()
    duplicates: list[dict[str, Any]] = []
    for entry in entries:
        url = _normalise_url(str(entry.get("url", "")))
        if url in seen_urls:
            duplicates.append({"row": int(entry.get("row")), "index": int(entry.get("index")), "url": url})
        seen_urls.add(url)
    blanks = [int(entry.get("row")) for entry in entries if not str(entry.get("short_name", "")).strip()]
    near = _near_duplicate_indices(entries)
    evidence = {
        "orphan_indices": orphan,
        "inline_only_indices": inline_only,
        "duplicate_rows": duplicates,
        "blank_short_name_rows": blanks,
        "near_duplicate_indices": near,
    }
    if orphan or inline_only or duplicates or blanks or near:
        findings.append(_finding("C7", "FAIL", "C7_INTEGRITY_FAILURE", evidence))
    else:
        findings.append(_finding("C7", "PASS", "C7_OK", {"ledger_rows": len(entries)}))


def _check_c8(body: str, spec: dict[str, Any], findings: list[dict[str, Any]]) -> None:
    marker = str(spec.get("final_marker") or "")
    if not marker:
        findings.append(_finding("C8", "PASS", "NO_FINAL_MARKER_SPECIFIED", ""))
        return
    nonempty = [line.strip() for line in body.splitlines() if line.strip()]
    count = body.count(marker)
    if count == 1 and nonempty and nonempty[-1] == marker:
        findings.append(_finding("C8", "PASS", "C8_OK", marker))
    else:
        findings.append(
            _finding(
                "C8",
                "FAIL",
                "FINAL_MARKER_BAD",
                {"marker": marker, "count": count, "last_nonempty": nonempty[-1] if nonempty else ""},
            )
        )


def validate_document(body: str, structured: dict[str, Any], spec: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    blocks = list(structured.get("blocks") or [])
    _capture_guard(structured, findings)
    _check_c1(body, spec, findings)
    _check_c2(blocks, spec, findings)
    _check_c3(blocks, findings)
    _check_c4(blocks, findings)
    _check_c5(body, spec, findings)
    _check_c6(blocks, findings)
    _check_c7(structured, findings)
    _check_c8(body, spec, findings)
    overall = "FAIL" if any(item["status"] == "FAIL" for item in findings) else "PASS"
    return {"overall": overall, "findings": findings}


__all__ = ["validate_document"]