import pytest

from app.services.sentence_trust import project_sentence_trust
from scripts.page58_slice2_calibrated_staking_dry_run import reroll, write_report


def test_slice2_reroll_uses_shared_sentence_trust_projector_for_baseline_contests():
    base_rows = [
        {
            "sentence_index": 3,
            "sentence_text": "Seed sentence with existing provenance.",
            "baseline_settled_votes": 10,
            "baseline_contested_votes": 2,
            "baseline_trust_level": "consensus",
            "existing_arxiv_ids": [f"2401.{i:05d}" for i in range(12)],
        }
    ]
    expected = project_sentence_trust(
        settled_votes=10,
        contested_votes=2,
        distinct_sources=12,
    )

    row = reroll(base_rows, stance_rows=[], tau_rel=0.55, tau_vote=0.70)[0]

    assert row["slice2_trust_level"] == expected["trust_level"]
    assert row["slice2_settled_share"] == pytest.approx(expected["settled_share"])
    assert row["slice2_trust_score"] == pytest.approx(expected["trust_score"], abs=0.001)
    assert row["slice2_tone_tier"] == expected["tone_tier"]
    assert row["slice2_single_source"] is expected["single_source"]
    assert row["slice2_contested_veto"] is expected["contested_veto"]


def test_slice2_report_surfaces_top_level_seed_duplicate_skip_count(tmp_path):
    summary = {
        "ratios": {
            "intros_staked": "1/2",
            "base_sentence_coverage": "1/1",
            "settled_share": "3/4",
        },
        "counts": {
            "stance_gold_rows": 2,
            "relevance_gold_rows": 2,
            "tone_transfer_gold_rows": 2,
            "seed_duplicate_stakes_skipped": 5,
        },
        "calibration": {
            "relevance": {"tau_rel": 0.55, "validate_f1": 0.8},
            "tone_transfer_gate": {
                "macro_f1_qwen_vs_panel_draft": 0.7,
                "macro_f1_gpt_vs_panel_draft": 0.8,
                "gate_passed_provisionally": True,
            },
        },
        "sensitivity": {
            "drop_con_votes": "0/1",
            "tau_vote_minus_0_10": "0/1",
            "tau_vote_plus_0_10": "0/1",
        },
        "db_write_count": 0,
        "paid_lane_touched": False,
        "local_only": True,
        "claude_p_invocations": 0,
    }
    roll = [
        {
            "sentence_index": 4,
            "sentence_text": "Seed sentence.",
            "slice2_new_pro_votes": 1,
            "slice2_new_con_votes": 0,
            "seed_duplicate_stakes_skipped": 5,
            "slice2_trust_level": "accepted",
            "slice2_settled_share": 0.75,
            "slice2_tone_tier": "settled",
            "slice2_contested_veto": False,
        }
    ]
    path = tmp_path / "REPORT.md"

    write_report(path, summary, roll)

    report = path.read_text(encoding="utf-8")
    assert "- Seed duplicate stakes skipped: 5." in report
    assert "seed duplicate stakes skipped 5" in report
