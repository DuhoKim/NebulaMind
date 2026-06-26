from app.services.sentence_trust import project_sentence_trust
from scripts import page58_sentence_vote_staking_dry_run as slice1
from scripts.page58_sentence_vote_staking_dry_run import rollup, write_report


def test_slice1_rollup_skips_seed_duplicate_paper_stakes():
    base_rows = [
        {
            "page_version_id": 6197,
            "sentence_index": 4,
            "sentence_hash": "hash-4",
            "sentence_text": "Seed sentence with existing paper provenance.",
            "trust_level": "accepted",
            "settled_votes": 2,
            "contested_votes": 0,
            "existing_arxiv_ids": ["2401.00001", "2401.00002"],
        }
    ]
    votes = [
        {
            "sentence_index": 4,
            "arxiv_id": "2401.00001",
            "tone_tier": "accepted",
            "tone_confidence": 0.95,
        },
        {
            "sentence_index": 4,
            "arxiv_id": "2401.00003",
            "tone_tier": "accepted",
            "tone_confidence": 0.93,
        },
    ]

    row = rollup(base_rows, votes, tau_vote=0.70)[0]
    expected = project_sentence_trust(
        settled_votes=3,
        contested_votes=0,
        distinct_sources=3,
    )

    assert row["new_pro_votes"] == 1
    assert row["new_con_votes"] == 0
    assert row["seed_duplicate_stakes_skipped"] == 1
    assert row["would_be_settled_votes"] == expected["settled_votes"]
    assert row["would_be_contested_votes"] == expected["contested_votes"]
    assert row["would_be_vote_count"] == expected["vote_count"]
    assert row["would_be_trust_level"] == expected["trust_level"]
    assert row["single_source"] is expected["single_source"]
    assert row["contested_veto"] is expected["contested_veto"]


def test_slice1_rollup_preserves_seed_duplicate_skip_when_dropping_con_votes():
    base_rows = [
        {
            "page_version_id": 6197,
            "sentence_index": 5,
            "sentence_hash": "hash-5",
            "sentence_text": "Seed sentence with a debated baseline.",
            "trust_level": "debated",
            "settled_votes": 2,
            "contested_votes": 1,
            "existing_arxiv_ids": ["2401.01001", "2401.01002", "2401.01003"],
        }
    ]
    votes = [
        {
            "sentence_index": 5,
            "arxiv_id": "2401.01003",
            "tone_tier": "challenged",
            "tone_confidence": 0.96,
        },
        {
            "sentence_index": 5,
            "arxiv_id": "2401.01004",
            "tone_tier": "challenged",
            "tone_confidence": 0.96,
        },
    ]

    row = rollup(base_rows, votes, tau_vote=0.70, drop_con=True)[0]
    expected = project_sentence_trust(
        settled_votes=2,
        contested_votes=1,
        distinct_sources=3,
    )

    assert row["new_pro_votes"] == 0
    assert row["new_con_votes"] == 0
    assert row["seed_duplicate_stakes_skipped"] == 1
    assert row["would_be_contested_votes"] == expected["contested_votes"]
    assert row["would_be_vote_count"] == expected["vote_count"]
    assert row["would_be_trust_level"] == expected["trust_level"]


def test_slice1_summary_counts_include_seed_duplicate_skip_total():
    counts = slice1.summarize_rollup_counts([
        {"new_pro_votes": 1, "new_con_votes": 0, "refine_tally": 2, "seed_duplicate_stakes_skipped": 3},
        {"new_pro_votes": 0, "new_con_votes": 1, "refine_tally": 0, "seed_duplicate_stakes_skipped": 4},
    ])

    assert counts == {
        "new_votes": 2,
        "new_pro_votes": 1,
        "new_con_votes": 1,
        "refine_tally": 2,
        "seed_duplicate_stakes_skipped": 7,
    }


def test_slice1_report_surfaces_seed_duplicate_skip_count(tmp_path):
    summary = {
        "ratios": {
            "intros_staked": "1/2",
            "intros_no_op": "1/2",
            "intros_no_match_emergent_pool": "0/2",
            "finding_sentences_kept": "2/3",
            "finding_sentences_filtered": "1/3",
            "provenance_coverage": "1/1",
            "settled_share": "3/3",
        },
        "sensitivity": {
            "trust_tier_changes_if_con_votes_dropped": "0/1",
            "trust_tier_changes_if_tau_vote_minus_0_10": "0/1",
            "trust_tier_changes_if_tau_vote_plus_0_10": "0/1",
        },
        "timings": {"total_seconds": 0.01},
        "counts": {"seed_duplicate_stakes_skipped": 2},
        "db_write_count": 0,
        "no_apply": True,
        "local_only": True,
        "paid_lane_touched": False,
        "claude_p_used": False,
    }
    trust_rows = [
        {
            "sentence_index": 4,
            "sentence_text": "Seed sentence.",
            "new_pro_votes": 1,
            "new_con_votes": 0,
            "seed_duplicate_stakes_skipped": 2,
            "refine_tally": 0,
            "no_op_tally": 0,
            "would_be_trust_level": "consensus",
            "would_be_tone_tier": "settled",
            "baseline_trust_level": "accepted",
            "settled_share": 1.0,
            "single_source": False,
            "contested_veto": False,
        }
    ]
    path = tmp_path / "REPORT.md"

    write_report(path, summary, trust_rows)

    report = path.read_text(encoding="utf-8")
    assert "- Seed duplicate stakes skipped: 2." in report
    assert "seed duplicate stakes skipped 2" in report
