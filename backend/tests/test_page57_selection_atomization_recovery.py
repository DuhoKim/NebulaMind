import scripts.page57_selection_atomization_recovery as mod


def pair(**extra):
    base = {
        "candidate_db_id": 1,
        "candidate_key": "candidate-1",
        "retrieval_filter_run_id": 16,
        "claim_id": 1,
        "element_id": "claim-1-e01",
        "element_index": 1,
        "element_type": "mechanism",
        "element_text": "fast outflows suppress star formation",
        "required": True,
        "normalized_subject": None,
        "normalized_mechanism": "outflows suppress star formation",
        "quantity_or_range": None,
        "redshift_or_environment": None,
        "section": "Physical Mechanisms",
        "arxiv_id": "1234.56789",
        "claim_text_snapshot": "Fast outflows suppress star formation.",
        "paper_title_snapshot": "Fast outflows in compact galaxies",
        "paper_abstract_snapshot": "We show that fast outflows suppress star formation in compact galaxies.",
        "candidate_source": "related_pages_bm25",
        "candidate_status": "shadow_proposed",
        "matched_terms": ["outflows", "suppress"],
        "claim_key_overlap": 0.5,
        "hydration_db_reads_used": False,
        "hydration_policy": "artifact_only_fail_closed",
    }
    base.update(extra)
    return base


def test_splitter_filters_anchor_missing_before_selection():
    selected, excluded = mod.split_selection_queue(
        [
            pair(),
            pair(
                candidate_db_id=2,
                candidate_key="candidate-2",
                element_id="claim-1-e02",
                element_text="halo mass threshold",
                paper_title_snapshot="Optical variability",
                paper_abstract_snapshot="We study optical variability.",
            ),
        ],
        semantic_threshold=0.5,
        ollama_host="http://localhost:11434",
        compute_semantic=False,
        ordering="score",
        claim_seed_count=0,
    )
    assert [row["selection_status"] for row in selected] == ["selected_for_atom_coverage"]
    assert [row["selection_status"] for row in excluded] == ["excluded_anchor_overlap_missing"]


def test_splitter_keeps_brk_and_off_domain_out_of_main_queue():
    selected, excluded = mod.split_selection_queue(
        [
            pair(candidate_db_id=1, candidate_key="candidate-1"),
            pair(candidate_db_id=2, candidate_key="candidate-2", retrieval_filter_decision="boundary_review_keep"),
            pair(candidate_db_id=3, candidate_key="candidate-3", candidate_status="off_domain"),
        ],
        semantic_threshold=0.5,
        ollama_host="http://localhost:11434",
        compute_semantic=False,
        ordering="score",
        claim_seed_count=0,
    )
    assert len(selected) == 1
    assert {row["selection_status"] for row in excluded} == {
        "audit_only_boundary_review_keep",
        "excluded_off_domain",
    }


def test_deterministic_fallback_elements_are_fail_closed_atoms():
    elements = mod.deterministic_fallback_elements(
        {
            "id": 42,
            "text": "AGN feedback suppresses star formation at z ~ 2.",
            "section": "Physical Mechanisms",
            "order_idx": 1,
        },
        "fixture_failure",
    )
    assert elements
    assert all(element["claim_id"] == 42 for element in elements)
    assert all(element["required"] is True for element in elements)
    assert {element["atomization_source"] for element in elements} == {"deterministic_fallback"}


def test_claim_round_robin_ordering_diversifies_before_siblings():
    rows = [
        {**pair(claim_id=1, element_id="claim-1-e01"), "selection_rank_score": 1.0},
        {**pair(claim_id=1, element_id="claim-1-e02"), "selection_rank_score": 0.9},
        {**pair(claim_id=2, element_id="claim-2-e01", candidate_db_id=2), "selection_rank_score": 0.8},
    ]
    ordered = mod.order_selected_rows(rows, "claim_round_robin")
    assert [(row["claim_id"], row["element_id"]) for row in ordered] == [
        (1, "claim-1-e01"),
        (2, "claim-2-e01"),
        (1, "claim-1-e02"),
    ]


def test_claim_seed_then_score_seeds_claims_then_preserves_score_order():
    rows = [
        {**pair(claim_id=1, element_id="claim-1-e01"), "selection_rank_score": 1.0},
        {**pair(claim_id=1, element_id="claim-1-e02"), "selection_rank_score": 0.9},
        {**pair(claim_id=2, element_id="claim-2-e01", candidate_db_id=2), "selection_rank_score": 0.8},
        {**pair(claim_id=3, element_id="claim-3-e01", candidate_db_id=3), "selection_rank_score": 0.7},
    ]
    ordered = mod.order_selected_rows(rows, "claim_seed_then_score", claim_seed_count=2)
    assert [(row["claim_id"], row["element_id"]) for row in ordered] == [
        (1, "claim-1-e01"),
        (2, "claim-2-e01"),
        (1, "claim-1-e02"),
        (3, "claim-3-e01"),
    ]


def test_coverage_summary_counts_ready_and_safety_flags():
    coverage = {
        **pair(),
        "candidate_atom_coverage_status": "ready",
        "candidate_atoms": [
            {
                "atom_text": "Fast outflows suppress star formation.",
                "support_relation": "direct",
                "evidence_anchor_terms": ["outflows"],
            }
        ],
        "coverage_key": "coverage-key",
        "source_hashes": {
            "claim_text_hash": "a",
            "element_text_hash": "b",
            "paper_title_hash": "c",
            "paper_abstract_hash": "d",
        },
    }
    summary = mod.summarize_coverage(
        [coverage],
        [pair(selection_status="excluded_anchor_overlap_missing")],
        [pair(selection_status="selected_for_atom_coverage")],
        db_writes=0,
    )
    assert summary["ready_rows"] == 1
    assert summary["unique_ready_tuples"] == 1
    assert summary["evidence_rows_written"] == 0
    assert summary["promoter_run"] is False
    assert summary["db_reads_used_for_validator_hydration"] is False
