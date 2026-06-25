import pytest

from app.services.sentence_trust import project_sentence_trust
from scripts.page58_slice2_calibrated_staking_dry_run import reroll


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
