from scripts import page57_candidate_universe_expand as expand


def test_prepare_source_paper_pool_dedupes_and_flags_old_ids():
    papers = [
        {"id": 1, "arxiv_id": "arXiv:1234.1", "title": "Galaxy evolution", "abstract": "galaxy growth", "category": "astro-ph.GA"},
        {"id": 2, "arxiv_id": "1234.1", "title": "Duplicate", "abstract": "duplicate", "category": "astro-ph.GA"},
        {"id": 3, "arxiv_id": "5678.1", "title": "AGN feedback", "abstract": "black hole galaxy", "category": "astro-ph.HE"},
    ]

    pool, summary = expand.prepare_source_paper_pool(papers, {"1234.1"})

    assert [row["arxiv_id"] for row in pool] == ["1234.1", "5678.1"]
    assert pool[0]["old_db_candidate_arxiv"] is True
    assert summary["source_paper_pool"] == 2
    assert summary["new_arxiv_ids_vs_db"] == 1


def test_candidate_universe_dedupes_claim_element_arxiv_tuple():
    claims = [{"id": 10, "text": "Galaxies quench at high redshift.", "section": "A"}]
    elements = [
        {"claim_id": 10, "element_id": "c10-e1", "element_index": 1, "text": "galaxies quench", "required": True},
        {"claim_id": 10, "element_id": "c10-e1", "element_index": 1, "text": "galaxies quench", "required": True},
    ]
    papers = [
        {
            "arxiv_paper_id": 1,
            "arxiv_id": "1111.1",
            "paper_title_snapshot": "Quenching galaxies",
            "paper_abstract_snapshot": "Galaxies quench at high redshift.",
            "source_paper_tier": "astro_ph_ga",
            "old_db_candidate_arxiv": False,
        }
    ]

    rows = expand.build_candidate_universe(claims, elements, papers, top_k_per_element=2, min_rows_per_claim=0)

    assert len(rows) == 1
    assert rows[0]["claim_id"] == 10
    assert rows[0]["element_id"] == "c10-e1"
    assert rows[0]["arxiv_id"] == "1111.1"


def test_preflight_excludes_anchor_missing_before_selection():
    rows = [
        {
            "claim_id": 1,
            "element_id": "e1",
            "element_text": "rareword",
            "required": True,
            "claim_text_snapshot": "rareword",
            "paper_title_snapshot": "No overlap",
            "paper_abstract_snapshot": "Nothing matches.",
            "arxiv_id": "1",
            "candidate_status": "artifact_only_expanded",
        },
        {
            "claim_id": 2,
            "element_id": "e2",
            "element_text": "galaxy quenching",
            "required": True,
            "claim_text_snapshot": "galaxy quenching",
            "paper_title_snapshot": "Galaxy quenching",
            "paper_abstract_snapshot": "This paper studies galaxy quenching.",
            "arxiv_id": "2",
            "candidate_status": "artifact_only_expanded",
        },
    ]

    selected, excluded = expand.preflight_split(
        rows,
        semantic_threshold=0.5,
        ollama_host="http://localhost:11434",
        compute_semantic=False,
        previous_ready_claims=set(),
    )

    assert [row["claim_id"] for row in selected] == [2]
    assert excluded[0]["selection_status"] == "excluded_anchor_overlap_missing"


def test_choose_probe_rows_prioritizes_no_ready_and_new_arxiv_ids():
    selected = []
    for claim_id in range(1, 7):
        selected.append(
            {
                "claim_id": claim_id,
                "element_id": f"e{claim_id}",
                "arxiv_id": f"new-{claim_id}",
                "selection_rank_score": 1.0,
                "semantic_similarity": 0.7,
            }
        )
        selected.append(
            {
                "claim_id": claim_id,
                "element_id": f"e{claim_id}b",
                "arxiv_id": "old-1",
                "selection_rank_score": 0.9,
                "semantic_similarity": 0.6,
            }
        )

    probe, plan = expand.choose_probe_rows(
        selected,
        old_arxiv_ids={"old-1"},
        previous_ready={1, 2},
        limit=5,
    )

    assert len(probe) == 5
    assert any(row["probe_bucket"] == "no_previous_ready_claim_seed" for row in probe)
    assert plan["probe_new_arxiv_id_rows"] >= 4
    assert not {1, 2}.issuperset({row["claim_id"] for row in probe})


def test_phase_gates_report_expected_failures():
    assert "candidate_rows_lt_12000" in expand.phase_a_gate(
        {
            "source_paper_pool": 600,
            "candidate_rows": 10,
            "distinct_claims_with_candidates": 500,
            "claims_with_ge5_candidate_rows": 350,
            "distinct_candidate_arxiv_ids": 500,
            "new_candidate_arxiv_ids_vs_db": 300,
        }
    )
    assert "selected_queue_rows_lt_2500" in expand.phase_b_gate(
        {
            "selected_queue_rows": 10,
            "selected_claims": 300,
            "selected_arxiv_ids": 350,
            "anchor_overlap_missing_model_rows": 0,
            "brk_or_off_domain_rows_in_main_queue": 0,
        }
    )
    assert "unique_ready_tuples_lt_40" in expand.phase_c_gate(
        {
            "valid_ready_rate": 0.08,
            "unique_ready_tuples": 39,
            "distinct_ready_claims": 35,
            "ready_tuples_from_new_arxiv_ids": 25,
            "retryable_error_rate": 0.0,
            "hydration_db_reads_used": False,
            "db_reads_used_for_validator_hydration": False,
            "db_writes_used": False,
            "promoter_run": False,
            "evidence_rows_written": 0,
            "db_write_count": 0,
        }
    )


def test_phase_d_gate_requires_full_run_thresholds_and_safety():
    failures = expand.phase_d_gate(
        {
            "valid_ready_rows": 499,
            "unique_ready_tuples": 249,
            "distinct_ready_claims": 99,
            "ready_tuples_from_new_arxiv_ids": 99,
            "retryable_error_rate": 0.021,
            "hydration_db_reads_used": False,
            "db_reads_used_for_validator_hydration": False,
            "db_writes_used": False,
            "promoter_run": False,
            "broad_validator_run": False,
            "db_candidate_insertion": False,
            "evidence_rows_written": 0,
            "db_write_count": 0,
        }
    )

    assert "valid_ready_rows_lt_500" in failures
    assert "unique_ready_tuples_lt_250" in failures
    assert "distinct_ready_claims_lt_100" in failures
    assert "ready_tuples_from_new_arxiv_ids_lt_100" in failures
    assert "retryable_error_rate_gt_2pct" in failures


def test_validator_build_pairs_gate_requires_artifact_only_targeted_match():
    assert expand.validator_build_pairs_gate(
        {
            "coverage_ready_input_rows": 250,
            "targeted_pair_rows": 250,
            "hydration_missing_rows": 0,
            "db_reads_used": False,
            "promotion_eligible": False,
        }
    ) == []

    failures = expand.validator_build_pairs_gate(
        {
            "coverage_ready_input_rows": 250,
            "targeted_pair_rows": 249,
            "hydration_missing_rows": 1,
            "db_reads_used": True,
            "promotion_eligible": True,
        }
    )

    assert "coverage_ready_input_rows_ne_targeted_pair_rows" in failures
    assert "hydration_missing_rows_not_zero" in failures
    assert "db_reads_used_not_false" in failures
    assert "promotion_eligible_not_false" in failures
