from pathlib import Path

from scripts.arxiv_wiki_feed_v2_retrieval_filter import semantic_threshold_from_calibration
from scripts.retrieval_filter_v2 import apply_retrieval_filter
from scripts.validator_coverage import materialize_coverage_rows


def test_second_page_config_runs_without_code_literals(tmp_path):
    calibration_path = tmp_path / "page_retrieval_calibration.second-page.v2.yaml"
    calibration_path.write_text(
        """
page_slug: second-page
semantic_band:
  min_semantic_similarity: 0.62
retrieval_filter_v2_boundary_review:
  scope:
    enabled_sections: [alpha_section]
    excluded_sections: []
  section_rules:
    alpha_section:
      policy_id: second_page_alpha_policy
      hard_drop_below: 0.1
      old_v1_floor: 0.2
      protected_markers: [alpha_marker]
      tag_protection: {}
""",
        encoding="utf-8",
    )
    assert semantic_threshold_from_calibration(calibration_path, 0.50) == 0.62

    routed = apply_retrieval_filter(
        [
            {
                "page_slug": "second-page",
                "section": "alpha_section",
                "element_id": "claim-1-e01",
                "paper_id": "2501.00001v1",
                "claim_id": 1,
                "dropped": False,
                "final_score": 0.4,
                "coverage_candidate": True,
                "element_support_gate": True,
            }
        ],
        {
            "retrieval_filter_v2_boundary_review": {
                "scope": {"enabled_sections": ["alpha_section"], "excluded_sections": []},
                "section_rules": {
                    "alpha_section": {
                        "policy_id": "second_page_alpha_policy",
                        "hard_drop_below": 0.1,
                        "old_v1_floor": 0.2,
                        "protected_markers": ["alpha_marker"],
                        "tag_protection": {},
                    }
                },
            }
        },
    )
    assert routed[0]["retrieval_filter_decision"] == "keep"
    assert routed[0]["coverage_status"] == "coverage_pending"


def test_second_page_coverage_materializes_arbitrary_section():
    [row] = materialize_coverage_rows(
        [
            {
                "retrieval_filter_run_id": 99,
                "page_slug": "second-page",
                "section": "alpha_section",
                "claim_id": 1,
                "element_id": "claim-1-e01",
                "arxiv_id": "2501.00001v1",
                "candidate_key": "candidate-1",
                "retrieval_filter_decision": "keep",
                "claim_text_snapshot": "A second page claim.",
                "element_text": "second page claim",
                "required": True,
                "paper_title_snapshot": "Second page paper",
                "paper_abstract_snapshot": "This paper directly addresses the second page claim.",
                "candidate_atom_coverage_status": "ready",
                "candidate_atoms": [{"atom_text": "second page claim", "support_relation": "direct"}],
                "entailment_gate_decision": "yes",
            }
        ]
    )
    assert row["coverage_status"] == "coverage_ready"
    assert row["page_slug"] == "second-page"
    assert row["section"] == "alpha_section"
