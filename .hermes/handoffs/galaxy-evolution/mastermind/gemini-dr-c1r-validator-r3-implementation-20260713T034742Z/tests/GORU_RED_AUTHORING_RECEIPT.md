# GORU RED AUTHORING RECEIPT

The r3 RED tests were written matching the frozen LANA_R3_RED_PIN.md and updated per TORI_A_P2_TEST_SPEC_REVIEW and TORI_A_P2_TEST_SPEC_REVIEW_2.
Execution confirms genuine RED status (tests fail as expected before A-P3 implementation).

## Test Output

/Users/duhokim/Library/Python/3.9/lib/python/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-dr-c1r-validator-r3-implementation-20260713T034742Z
plugins: anyio-4.12.1, langsmith-0.4.37, cov-7.0.0
collected 6 items

tests/test_validator_v3_r3_red.py FF.FF                                  [ 83%]
tests/test_integration_v3_r3_red.py F                                    [100%]

=================================== FAILURES ===================================
______________________ test_d5_gap_multiple_per_paragraph ______________________

    def test_d5_gap_multiple_per_paragraph() -> None:
        gap1 = block("gap1", "gap_line", "GAP: one", section="5. Gaps", gap_index=1, parent_path="p1")
        gap2 = block("gap2", "gap_line", "GAP: two", section="5. Gaps", gap_index=2, parent_path="p1")
        gap3 = block("gap3", "gap_line", "GAP: three", section="5. Gaps", gap_index=3, parent_path="p1")
        gap4 = block("gap4", "gap_line", "GAP: four", section="5. Gaps", gap_index=4, parent_path="p1")
        result = validate_document("", structure([*heading_blocks(), gap1, gap2, gap3, gap4]), SPEC)
>       assert len(has_code(result, "GAP_MULTIPLE_PER_PARAGRAPH")) == 1
E       AssertionError: assert 0 == 1
E        +  where 0 = len([])
E        +    where [] = has_code({'findings': [{'clause': 'C1', 'code': 'NO_SPEC_PROVIDED', 'evidence': '', 'source_refs': [], ...}, {'clause': 'C2', '...', 'code': 'GAP_MISSING_VERIFICATION', 'evidence': 'GAP: four', 'source_refs': ['gap4'], ...}, ...], 'overall': 'FAIL'}, 'GAP_MULTIPLE_PER_PARAGRAPH')

tests/test_validator_v3_r3_red.py:89: AssertionError
___________________________ test_d4_ledger_integrity ___________________________

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
>       assert len(c7_arxiv[0]["evidence"]["duplicate_rows"]) == 2
E       AssertionError: assert 1 == 2
E        +  where 1 = len([{'index': 2, 'row': 2, 'url': 'https://arxiv.org/abs/1234.56789'}])

tests/test_validator_v3_r3_red.py:123: AssertionError
__________________ test_d1_missing_calibration_target_prefix ___________________

    def test_d1_missing_calibration_target_prefix() -> None:
        # Negative: No prefix but references observation
        unprefixed = block("unprefixed", "table_row", "sim\tmatch observation\tNONE\tNONE\tNONE", section="1. Calibration ledger", cells=[
            cell("simulation", "SIMBA"), cell("calibration_target", "calibrated to reproduce the observed mass"), cell("feedback_params", "NONE_FOUND"), cell("emergent", "NONE_FOUND"), cell("notes", "NONE_FOUND")
        ])
        result = validate_document("", structure([*heading_blocks(), unprefixed]), SPEC)
>       assert len(has_code(result, "MISSING_CALIBRATION_TARGET_PREFIX")) == 1
E       AssertionError: assert 0 == 1
E        +  where 0 = len([])
E        +    where [] = has_code({'findings': [{'clause': 'C1', 'code': 'NO_SPEC_PROVIDED', 'evidence': '', 'source_refs': [], ...}, {'clause': 'C2', '.....}, {'clause': 'C8', 'code': 'NO_FINAL_MARKER_SPECIFIED', 'evidence': '', 'source_refs': [], ...}], 'overall': 'PASS'}, 'MISSING_CALIBRATION_TARGET_PREFIX')

tests/test_validator_v3_r3_red.py:175: AssertionError
_______________________ test_d3_cited_cell_claim_review ________________________

    def test_d3_cited_cell_claim_review() -> None:
        # Negative: empty citation cell
        empty_cit = block("empty_cit", "table_row", "sim\tobs\tres\tMATCHED_SELECTIONS\tNo\t", section="2. Out-of-sample validation ledger", cells=[
            cell("simulation", "sim"), cell("observable", "obs"), cell("result", "Agreement"), cell("comparability", "MATCHED_SELECTIONS"), cell("overlap", "No"), cell("citation", "")
        ])
        result = validate_document("", structure([*heading_blocks(), empty_cit]), SPEC)
>       assert len(has_code(result, "EMPTY_CITATION_CELL")) == 1
E       AssertionError: assert 0 == 1
E        +  where 0 = len([])
E        +    where [] = has_code({'findings': [{'clause': 'C1', 'code': 'NO_SPEC_PROVIDED', 'evidence': '', 'source_refs': [], ...}, {'clause': 'C2', '....}, {'clause': 'C7', 'code': 'C7_OK', 'evidence': {'ledger_rows': 0}, 'source_refs': [], ...}, ...], 'overall': 'FAIL'}, 'EMPTY_CITATION_CELL')

tests/test_validator_v3_r3_red.py:212: AssertionError
___________ test_t14_exact_mechanical_residue_r3_and_t15_determinism ___________

tmp_path = PosixPath('/private/var/folders/64/71dstw0j1gd_n58lsxnhl3p80000gn/T/pytest-of-duhokim/pytest-90/test_t14_exact_mechanical_resi0')

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
>       assert {key: len(value) for key, value in by_clause_code.items()} == {
            ("C2", "SENTINEL_FORMAT_DEFECT"): 1,
            ("C2", "GAP_MULTIPLE_PER_PARAGRAPH"): 1,
            ("C6", "UNLABELED_COMPARISON"): 6,
            ("C6", "MISSING_QUALIFIER"): 1,
            ("C6", "MISSING_CALIBRATION_TARGET_PREFIX"): 9,
            ("C7", "C7_INTEGRITY_FAILURE"): 1,
        }
E       AssertionError: assert {('C2', 'SENT...SON'): 6, ...} == {('C2', 'GAP_...IER'): 1, ...}
E         
E         Omitting 4 identical items, use -vv to show
E         Left contains 1 more item:
E         {('C4', 'UNCITED_CELL_CLAIM'): 8}
E         Right contains 2 more items:
E         {('C2', 'GAP_MULTIPLE_PER_PARAGRAPH'): 1,
E          ('C6', 'MISSING_CALIBRATION_TARGET_PREFIX'): 9}
E         Use -v to get more diff

tests/test_integration_v3_r3_red.py:71: AssertionError
=========================== short test summary info ============================
FAILED tests/test_validator_v3_r3_red.py::test_d5_gap_multiple_per_paragraph
FAILED tests/test_validator_v3_r3_red.py::test_d4_ledger_integrity - Assertio...
FAILED tests/test_validator_v3_r3_red.py::test_d1_missing_calibration_target_prefix
FAILED tests/test_validator_v3_r3_red.py::test_d3_cited_cell_claim_review - A...
FAILED tests/test_integration_v3_r3_red.py::test_t14_exact_mechanical_residue_r3_and_t15_determinism
========================= 5 failed, 1 passed in 0.25s ==========================

GORU_GATE_A_RED_TESTS_WRITTEN_20260713T034742Z

