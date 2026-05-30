from pathlib import Path
import json

import pytest

from scripts.retrieval_filter_v2 import (
    BOUNDARY_REVIEW_KEEP,
    Decision,
    DROP,
    ELEMENT_UNSUPPORTED,
    KEEP,
    PROTECTED_MARKER,
    PROTECTED_ROW_KEY,
    ReasonCode,
    RetrievalCandidate,
    RoutingDecision,
    SEMANTIC_UNSUPPORTED,
    SUPPRESSION_DEMOTED,
    TAG_PROTECTION,
    apply_retrieval_filter,
    apply_retrieval_filter_v2,
    apply_v2_routing,
    retrieval_candidate_from_row,
    has_protected_marker,
    load_calibration,
    route_row_v2,
    section_rule,
    split_rows_by_entailment_gate,
    validate_v2_config,
)

import scripts.retrieval_filter_v2 as retrieval_filter_v2_mod


REAL_CONFIG = Path(__file__).resolve().parents[1] / "config" / "page_retrieval_calibration.galaxy-evolution.v2.yaml"
ARTIFACT_ROOT = Path("/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2")
LOCKED_REPLAY_CONFIG = ARTIFACT_ROOT / "retrieval_filter_v2_1_apply_validator_dryrun_20260527T001425Z" / "rollback_page_retrieval_calibration.galaxy-evolution.v2.yaml"
PROJECTED_ROWS = ARTIFACT_ROOT / "retrieval_filter_v2_design_and_dryrun_20260526T232738Z" / "retrieval_filter_v2_projected_rows.jsonl"
ACTUAL_ROWS = ARTIFACT_ROOT / "retrieval_filter_v2_apply_and_validator_dryrun_20260526T234016Z" / "v2_actual_routing_rows.jsonl"
V1_RECONSTRUCTED_ROWS = ARTIFACT_ROOT / "retrieval_filter_v1_partial_ship_and_v2_audit_20260526T232205Z" / "FILTERED_ROWS_RECONSTRUCTED_081400.jsonl"


def read_jsonl(path: Path):
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def rule(**extra):
    base = {
        "policy_id": "section_policy",
        "hard_drop_below": 0.1,
        "old_v1_floor": 0.2,
        "protected_markers": ["feedback", "cluster"],
        "tag_protection": {"neighbor_tag": "boundary_review"},
    }
    base.update(extra)
    return base


def test_keep_row_passes_without_boundary_state():
    decision = route_row_v2({"dropped": False, "final_score": 0.4}, rule())
    assert decision.decision == KEEP
    assert decision.boundary_review_reason is None
    assert decision.enters_validator is True


def test_frozen_api_contract_names_are_importable():
    row = {
        "page_slug": "page",
        "section": "section_a",
        "element_id": "e1",
        "paper_id": "p1",
        "final_score": 0.1,
        "combined_score": 0.1,
        "dropped": True,
        "drop_reasons": ["derived_score_gate"],
        "tags": ["neighbor_tag"],
        "element_text": "feedback",
    }
    candidate = retrieval_candidate_from_row(row)
    assert isinstance(candidate, RetrievalCandidate)
    assert candidate.section == "section_a"
    assert candidate.paper_id == "p1"
    assert apply_retrieval_filter_v2([], {"retrieval_filter_v2_boundary_review": {"scope": {"enabled_sections": []}}}) == []

    decision: RoutingDecision = route_row_v2(row, rule())
    assert decision.decision in {"keep", "drop", "downrank", "boundary_review_keep"}
    assert decision.reason_code in {"score_band", "protected_marker", "protected_row_key", "tag_protection", "suppression_demoted", "hard_drop", None}
    assert decision.promotion_authority is False
    assert Decision is not None
    assert ReasonCode is not None


def test_score_band_routes_to_boundary_review():
    decision = route_row_v2(
        {"dropped": True, "final_score": 0.15, "drop_reasons": ["derived_score_gate"]},
        rule(),
    )
    assert decision.decision == BOUNDARY_REVIEW_KEEP
    assert decision.boundary_review_reason == "score_band:0.1-0.2"
    assert decision.enters_validator is False
    assert decision.validator_enqueue_policy == "audit_only"
    assert decision.brk_usage == "retrieval_audit_only"


def test_score_band_lower_boundary_is_inclusive():
    decision = route_row_v2(
        {"dropped": True, "final_score": 0.1, "drop_reasons": ["derived_score_gate"]},
        rule(),
    )
    assert decision.decision == BOUNDARY_REVIEW_KEEP
    assert decision.boundary_review_reason == "score_band:0.1-0.2"


def test_score_below_hard_floor_drops_without_other_match():
    decision = route_row_v2(
        {"dropped": True, "final_score": 0.099999, "drop_reasons": ["derived_score_gate"]},
        rule(),
    )
    assert decision.decision == DROP
    assert decision.boundary_review_reason == "hard_drop"


def test_score_at_old_v1_floor_is_out_of_band_and_drops_without_marker():
    decision = route_row_v2(
        {"dropped": True, "final_score": 0.2, "drop_reasons": ["derived_score_gate"]},
        rule(),
    )
    assert decision.decision == DROP
    assert decision.boundary_review_reason == "hard_drop"


def test_score_above_old_v1_floor_drops_without_marker():
    decision = route_row_v2(
        {"dropped": True, "final_score": 0.21, "drop_reasons": ["derived_score_gate"]},
        rule(),
    )
    assert decision.decision == DROP
    assert decision.boundary_review_reason == "hard_drop"


def test_tag_protection_routes_neighbor_downweight_to_boundary_review():
    decision = route_row_v2(
        {
            "dropped": True,
            "final_score": 0.05,
            "tags": ["neighbor_tag"],
            "drop_reasons": ["neighboring_domain_tag_downweight", "derived_score_gate"],
        },
        rule(),
    )
    assert decision.decision == BOUNDARY_REVIEW_KEEP
    assert decision.boundary_review_reason == TAG_PROTECTION


def test_no_markers_configured_out_of_band_drop_stays_drop():
    decision = route_row_v2(
        {"dropped": True, "final_score": 0.0, "drop_reasons": ["derived_score_gate"]},
        rule(protected_markers=[]),
    )
    assert decision.decision == DROP
    assert decision.boundary_review_reason == "hard_drop"


def test_configured_marker_routes_to_protected_marker_review():
    row = {
        "dropped": True,
        "final_score": 0.0,
        "drop_reasons": ["derived_score_gate"],
        "paper_title_snapshot": "AGN feedback and circumgalactic outflows",
    }
    decision = route_row_v2(row, rule(protected_markers=["feedback", "cluster"]))
    assert decision.decision == BOUNDARY_REVIEW_KEEP
    assert decision.boundary_review_reason == PROTECTED_MARKER
    assert decision.features["matched_protected_markers"] == ["feedback"]
    assert has_protected_marker(row, rule(protected_markers=["feedback"])) is True


def test_configured_marker_can_match_target_section_title():
    row = {
        "dropped": True,
        "final_score": 0.0,
        "drop_reasons": ["derived_score_gate"],
        "target_section_title": "Feedback/outflows",
    }
    decision = route_row_v2(row, rule(protected_markers=["feedback", "outflow"]))
    assert decision.decision == BOUNDARY_REVIEW_KEEP
    assert decision.boundary_review_reason == PROTECTED_MARKER
    assert decision.features["matched_protected_markers"] == ["feedback", "outflow"]


def test_configured_marker_can_match_section_slug():
    row = {
        "section": "high_z_sf",
        "dropped": True,
        "final_score": 0.0,
        "drop_reasons": ["derived_score_gate"],
    }
    decision = route_row_v2(row, rule(protected_markers=["high_z", "feedback"]))
    assert decision.decision == BOUNDARY_REVIEW_KEEP
    assert decision.boundary_review_reason == PROTECTED_MARKER
    assert decision.features["matched_protected_markers"] == ["high_z"]


def test_legacy_protected_marker_fallback_is_explicit_and_temporary():
    row = {
        "dropped": True,
        "final_score": 0.0,
        "drop_reasons": ["derived_score_gate"],
        "tags": [],
        "target_section_title": "unrelated title",
    }
    decision_without_fallback = route_row_v2(
        row,
        rule(protected_markers=["feedback"], legacy_protected_marker_fallback=False),
    )
    decision_with_fallback = route_row_v2(
        row,
        rule(protected_markers=["feedback"], legacy_protected_marker_fallback=True),
    )
    assert decision_without_fallback.decision == DROP
    assert decision_with_fallback.decision == BOUNDARY_REVIEW_KEEP
    assert decision_with_fallback.boundary_review_reason == PROTECTED_MARKER
    assert decision_with_fallback.features["matched_protected_markers"] == ["__legacy_protected_marker_fallback__"]


def test_configured_row_key_routes_to_boundary_review_without_promotion_authority():
    row = {
        "section": "section_a",
        "claim_id": 42,
        "element_id": "claim-42-e01",
        "paper_id": "paper-1",
        "dropped": True,
        "final_score": 0.0,
        "drop_reasons": ["derived_score_gate"],
    }
    decision = route_row_v2(
        row,
        rule(protected_markers=[], protected_row_keys=["section_a::claim-42-e01::paper-1"]),
    )
    assert decision.decision == BOUNDARY_REVIEW_KEEP
    assert decision.boundary_review_reason == PROTECTED_ROW_KEY
    assert decision.enters_validator is False
    assert decision.features["matched_protected_row_keys"] == ["section_a::claim-42-e01::paper-1"]


def test_enriched_tag_gate_remains_hard_drop():
    decision = route_row_v2(
        {
            "dropped": True,
            "final_score": 0.05,
            "drop_reasons": ["off_domain_enriched_tag_gate", "derived_score_gate"],
        },
        rule(),
    )
    assert decision.decision == DROP
    assert decision.enters_validator is False


def test_page_local_suppression_drops_without_support():
    decision = route_row_v2(
        {
            "section": "section_a",
            "paper_id": "paper_a",
            "dropped": True,
            "final_score": 0.05,
            "drop_reasons": ["page_local_paper_suppression", "derived_score_gate"],
        },
        rule(),
    )
    assert decision.decision == DROP


def test_page_local_suppression_demotes_when_support_exists():
    decision = route_row_v2(
        {
            "section": "section_a",
            "paper_id": "paper_a",
            "dropped": True,
            "final_score": 0.05,
            "drop_reasons": ["page_local_paper_suppression", "derived_score_gate"],
        },
        rule(),
        support_by_section_paper={("section_a", "paper_a"): 1},
    )
    assert decision.decision == BOUNDARY_REVIEW_KEEP
    assert decision.boundary_review_reason == SUPPRESSION_DEMOTED


def test_apply_empty_input_returns_empty_list():
    assert apply_v2_routing([], {"retrieval_filter_v2_boundary_review": {"scope": {"enabled_sections": []}}}) == []


def test_all_kept_rows_preserve_keep_and_validator_routing():
    calibration = {
        "retrieval_filter_v2_boundary_review": {
            "scope": {"enabled_sections": ["section_a"], "excluded_sections": []},
            "section_rules": {"section_a": rule()},
        }
    }
    rows = [{"section": "section_a", "paper_id": "p1", "dropped": False, "final_score": 0.4}]
    routed = apply_v2_routing(rows, calibration)
    assert routed[0]["retrieval_filter_decision"] == KEEP
    assert routed[0]["retrieval_routes_to_validator"] is True
    assert routed[0]["would_enter_validator"] is True
    assert routed[0]["boundary_review_reason"] is None
    assert routed[0]["boundary_review_policy"] == "section_policy"


def test_element_support_gate_miss_routes_to_element_unsupported():
    calibration = {
        "retrieval_filter_v2_boundary_review": {
            "scope": {"enabled_sections": ["section_a"], "excluded_sections": []},
            "section_rules": {"section_a": rule()},
        }
    }
    rows = [
        {
            "section": "section_a",
            "paper_id": "p1",
            "dropped": False,
            "final_score": 0.4,
            "element_support_gate": False,
        }
    ]
    routed = apply_v2_routing(rows, calibration)
    assert routed[0]["retrieval_filter_decision"] == ELEMENT_UNSUPPORTED
    assert routed[0]["retrieval_routes_to_validator"] is False
    assert routed[0]["would_enter_validator"] is False
    assert routed[0]["boundary_review_reason"] is None


def test_semantic_support_gate_miss_routes_to_semantic_unsupported():
    calibration = {
        "retrieval_filter_v2_boundary_review": {
            "scope": {"enabled_sections": ["section_a"], "excluded_sections": []},
            "section_rules": {"section_a": rule()},
        }
    }
    routed = apply_v2_routing(
        [{"section": "section_a", "paper_id": "p1", "dropped": False, "final_score": 0.4, "coverage_candidate": False}],
        calibration,
    )
    assert routed[0]["retrieval_filter_decision"] == SEMANTIC_UNSUPPORTED
    assert routed[0]["retrieval_routes_to_validator"] is False
    assert routed[0]["would_enter_validator"] is False


def test_all_boundary_band_rows_are_brk_without_promotion_authority():
    calibration = {
        "retrieval_filter_v2_boundary_review": {
            "scope": {"enabled_sections": ["section_a"], "excluded_sections": []},
            "section_rules": {"section_a": rule()},
        }
    }
    rows = [
        {"section": "section_a", "paper_id": "p1", "dropped": True, "final_score": 0.11, "drop_reasons": ["derived_score_gate"]},
        {"section": "section_a", "paper_id": "p2", "dropped": True, "final_score": 0.19, "drop_reasons": ["derived_score_gate"]},
    ]
    routed = apply_v2_routing(rows, calibration)
    assert all(row["retrieval_filter_decision"] == BOUNDARY_REVIEW_KEEP for row in routed)
    assert all(row["retrieval_routes_to_validator"] is False for row in routed)
    assert all(row["would_enter_validator"] is False for row in routed)
    assert all(row["validator_enqueue_policy"] == "audit_only" for row in routed)
    assert all(row["brk_usage"] == "retrieval_audit_only" for row in routed)
    assert all(row["would_be_promotion_authority"] is False for row in routed)


def test_brk_rows_are_not_manifest_eligible_without_validator_ready_status():
    def manifest_eligible(row, validator_aggregate):
        return validator_aggregate.get((row["section"], row["paper_id"])) == "validated_ready"

    calibration = {
        "retrieval_filter_v2_boundary_review": {
            "scope": {"enabled_sections": ["section_a"], "excluded_sections": []},
            "section_rules": {"section_a": rule()},
        }
    }
    row = apply_v2_routing(
        [{"section": "section_a", "paper_id": "p1", "dropped": True, "final_score": 0.11, "drop_reasons": ["derived_score_gate"]}],
        calibration,
    )[0]

    assert row["retrieval_filter_decision"] == BOUNDARY_REVIEW_KEEP
    assert row["would_enter_validator"] is False
    assert row["retrieval_routes_to_validator"] is False
    assert row["would_be_promotion_authority"] is False
    assert manifest_eligible(row, {}) is False
    assert manifest_eligible(row, {("section_a", "p1"): "validated_ready"}) is True


def test_brk_audit_only_writes_element_row_but_no_validator_queue_insert():
    calibration = {
        "retrieval_filter_v2_boundary_review": {
            "scope": {"enabled_sections": ["section_a"], "excluded_sections": []},
            "section_rules": {"section_a": rule()},
        }
    }
    routed = apply_v2_routing(
        [{"section": "section_a", "element_id": "claim-1-e01", "paper_id": "p1", "dropped": True, "final_score": 0.11, "drop_reasons": ["derived_score_gate"]}],
        calibration,
    )
    validator_queue = [row for row in routed if row.get("retrieval_routes_to_validator")]
    assert len(routed) == 1
    assert routed[0]["retrieval_filter_decision"] == BOUNDARY_REVIEW_KEEP
    assert routed[0]["validator_enqueue_policy"] == "audit_only"
    assert validator_queue == []

    from scripts.retrieval_filter_v2_production_apply import create_rows

    handoff_rows = create_rows(
        [
            {
                **routed[0],
                "v2_1_decision": routed[0]["retrieval_filter_decision"],
                "label": "citable",
            }
        ],
        {"p1": 1},
        99,
    )
    assert len(handoff_rows) == 1
    assert handoff_rows[0]["retrieval_routes_to_validator"] is False
    assert handoff_rows[0]["validator_status"] == "audit_only"


def test_keep_writes_element_row_and_validator_queue_insert():
    calibration = {
        "retrieval_filter_v2_boundary_review": {
            "scope": {"enabled_sections": ["section_a"], "excluded_sections": []},
            "section_rules": {"section_a": rule()},
        }
    }
    routed = apply_v2_routing(
        [{"section": "section_a", "element_id": "claim-1-e01", "paper_id": "p1", "dropped": False, "final_score": 0.4}],
        calibration,
    )
    validator_queue = [row for row in routed if row.get("retrieval_routes_to_validator")]
    assert len(routed) == 1
    assert routed[0]["retrieval_filter_decision"] == KEEP
    assert routed[0]["validator_enqueue_policy"] == "enqueue"
    assert len(validator_queue) == 1

    from scripts.retrieval_filter_v2_production_apply import create_rows

    handoff_rows = create_rows(
        [
            {
                **routed[0],
                "v2_1_decision": routed[0]["retrieval_filter_decision"],
                "label": "citable",
            }
        ],
        {"p1": 1},
        99,
    )
    assert len(handoff_rows) == 1
    assert handoff_rows[0]["retrieval_routes_to_validator"] is True
    assert handoff_rows[0]["validator_status"] == "pending"
    payload = json.loads(handoff_rows[0]["row_payload"])
    assert "paper_title_snapshot" not in payload


def test_production_apply_persists_paper_metadata_snapshot_in_row_payload():
    from scripts.retrieval_filter_v2_production_apply import create_rows

    handoff_rows = create_rows(
        [
            {
                "section": "section_a",
                "element_id": "claim-1-e01",
                "paper_id": "p1",
                "v2_1_decision": KEEP,
                "retrieval_routes_to_validator": True,
                "label": "citable",
            }
        ],
        {"p1": {"id": 1, "title": "Paper title", "abstract": "Paper abstract"}},
        99,
    )
    payload = json.loads(handoff_rows[0]["row_payload"])
    assert handoff_rows[0]["arxiv_paper_id"] == 1
    assert payload["paper_title_snapshot"] == "Paper title"
    assert payload["paper_abstract_snapshot"] == "Paper abstract"


def test_boundary_policy_is_top_level_for_brk_and_unset_for_non_v2():
    calibration = {
        "retrieval_filter_v2_boundary_review": {
            "scope": {"enabled_sections": ["section_a"], "excluded_sections": []},
            "section_rules": {"section_a": rule(policy_id="policy_a")},
        }
    }
    routed = apply_v2_routing(
        [
            {"section": "section_a", "paper_id": "p1", "dropped": True, "final_score": 0.11, "drop_reasons": ["derived_score_gate"]},
            {"section": "section_b", "paper_id": "p2", "dropped": False, "final_score": 0.4},
        ],
        calibration,
    )
    assert routed[0]["retrieval_filter_decision"] == BOUNDARY_REVIEW_KEEP
    assert routed[0]["boundary_review_policy"] == "policy_a"
    assert "retrieval_filter_decision" not in routed[1]
    assert routed[1].get("boundary_review_policy") is None


def test_real_config_excludes_shipped_v1_sections():
    calibration = load_calibration(REAL_CONFIG)
    assert section_rule(calibration, "size_evolution") is None
    assert section_rule(calibration, "shmr_halo_quenching") is None


def test_excluded_section_wins_over_enabled_section():
    calibration = {
        "retrieval_filter_v2_boundary_review": {
            "scope": {"enabled_sections": ["section_a"], "excluded_sections": ["section_a"]},
            "section_rules": {"section_a": rule()},
        }
    }
    assert section_rule(calibration, "section_a") is None


def test_validate_v2_config_rejects_overlapping_enabled_and_excluded_sections():
    calibration = {
        "retrieval_filter_v2_boundary_review": {
            "scope": {"enabled_sections": ["section_a"], "excluded_sections": ["section_a"]},
            "section_rules": {"section_a": rule()},
        }
    }
    with pytest.raises(ValueError, match="disjoint"):
        validate_v2_config(calibration)


def valid_calibration(**override):
    base = {
        "retrieval_filter_v2_boundary_review": {
            "scope": {"enabled_sections": ["section_a"], "excluded_sections": []},
            "section_rules": {"section_a": rule()},
        }
    }
    base.update(override)
    return base


def test_validate_v2_config_accepts_real_config():
    validate_v2_config(load_calibration(REAL_CONFIG))


@pytest.mark.parametrize(
    "calibration",
    [
        {},
        {"retrieval_filter_v2_boundary_review": {"scope": {"enabled_sections": ["section_a"], "excluded_sections": []}, "section_rules": {}}},
        {"retrieval_filter_v2_boundary_review": {"scope": {"enabled_sections": ["section_a"], "excluded_sections": []}, "section_rules": {"section_a": {"hard_drop_below": "nope", "old_v1_floor": 0.2}}}},
        {"retrieval_filter_v2_boundary_review": {"scope": {"enabled_sections": ["section_a"], "excluded_sections": []}, "section_rules": {"section_a": rule(tag_protection=["bad"])}}},
        {"retrieval_filter_v2_boundary_review": {"scope": {"enabled_sections": ["section_a"], "excluded_sections": []}, "validator_enqueue_policy": {"keep_decisions": ["boundary_review_keep"]}, "section_rules": {"section_a": rule()}}},
    ],
)
def test_validate_v2_config_rejects_malformed_configs(calibration):
    with pytest.raises((KeyError, ValueError)):
        validate_v2_config(calibration)


@pytest.mark.parametrize("path", [PROJECTED_ROWS, ACTUAL_ROWS])
def test_locked_replay_rows_match_full_v2_projection(path):
    calibration = load_calibration(LOCKED_REPLAY_CONFIG)
    rows = read_jsonl(path)
    routed = apply_retrieval_filter(rows, calibration)
    divergences = []
    counts = {}
    brk = {}
    for expected, actual in zip(rows, routed):
        expected_decision = expected.get("retrieval_filter_decision") or expected.get("v2_decision")
        expected_reason = expected.get("boundary_review_reason") or expected.get("v2_boundary_reason")
        key = (expected.get("section"), expected.get("element_id"), expected.get("paper_id") or expected.get("arxiv_id"))
        if actual.get("retrieval_filter_decision") != expected_decision:
            divergences.append((key, "decision", expected_decision, actual.get("retrieval_filter_decision")))
        if actual.get("boundary_review_reason") != expected_reason:
            divergences.append((key, "reason", expected_reason, actual.get("boundary_review_reason")))
        if expected.get("config_policy_id") and actual.get("boundary_review_policy") != expected.get("config_policy_id"):
            divergences.append((key, "policy", expected.get("config_policy_id"), actual.get("boundary_review_policy")))
        expected_validator_route = expected_decision == KEEP
        if actual.get("retrieval_routes_to_validator") != expected_validator_route:
            divergences.append((key, "validator_route", expected_validator_route, actual.get("retrieval_routes_to_validator")))
        section = actual["section"]
        if actual.get("retrieval_filter_decision") != DROP:
            counts[section] = counts.get(section, 0) + 1
        if actual.get("retrieval_filter_decision") == BOUNDARY_REVIEW_KEEP:
            brk[section] = brk.get(section, 0) + 1

    assert divergences == []
    assert counts == {"feedback_outflows": 180, "high_z_sf": 198, "env_quenching": 99}
    assert brk == {"feedback_outflows": 70, "high_z_sf": 47, "env_quenching": 40}
    assert sum(1 for row in routed if row.get("retrieval_filter_decision") != DROP) == 477
    assert sum(1 for row in routed if row.get("retrieval_routes_to_validator")) == 320
    assert sum(1 for row in routed if row.get("retrieval_filter_decision") == BOUNDARY_REVIEW_KEEP and row.get("retrieval_routes_to_validator")) == 0


@pytest.mark.parametrize("path", [PROJECTED_ROWS, ACTUAL_ROWS])
def test_no_brk_rows_are_validator_queued_in_replay(path):
    calibration = load_calibration(LOCKED_REPLAY_CONFIG)
    routed = apply_retrieval_filter(read_jsonl(path), calibration)
    assert [
        row
        for row in routed
        if row.get("retrieval_filter_decision") == BOUNDARY_REVIEW_KEEP
        and row.get("retrieval_routes_to_validator")
    ] == []


def test_v1_shipped_sections_are_unchanged_by_live_v2_config():
    calibration = load_calibration(REAL_CONFIG)
    rows = [
        row
        for row in read_jsonl(V1_RECONSTRUCTED_ROWS)
        if row.get("section") in {"size_evolution", "shmr_halo_quenching"}
    ]
    routed = apply_retrieval_filter(rows, calibration)
    assert len(routed) == len(rows)
    assert routed == rows
    assert section_rule(calibration, "size_evolution") is None
    assert section_rule(calibration, "shmr_halo_quenching") is None
    assert all("retrieval_filter_version" not in row for row in routed)
    assert all("retrieval_filter_decision" not in row for row in routed)
    assert all("boundary_review_reason" not in row for row in routed)


class _EntailmentResponse:
    def __init__(self, content=None, json_exc=None):
        self.content = content
        self.json_exc = json_exc

    def raise_for_status(self):
        return None

    def json(self):
        if self.json_exc:
            raise self.json_exc
        return {"message": {"content": self.content}}


def _coverage_row():
    return {
        "claim_text_snapshot": "A claim context.",
        "element_text": "Specific element.",
        "paper_abstract_snapshot": "A source abstract.",
    }


@pytest.mark.parametrize("entailment", ["yes", "no", "abstain"])
def test_entailment_gate_routes_yes_only(monkeypatch, entailment):
    def fake_post(*_args, **_kwargs):
        return _EntailmentResponse(json.dumps({"entailment": entailment, "reason": "checked"}))

    monkeypatch.setattr(retrieval_filter_v2_mod.requests, "post", fake_post)

    coverage, excluded = split_rows_by_entailment_gate([_coverage_row()])

    if entailment == "yes":
        assert len(coverage) == 1
        assert excluded == []
        assert coverage[0]["entailment_gate_decision"] == "yes"
    else:
        assert coverage == []
        assert len(excluded) == 1
        assert excluded[0]["entailment_gate_decision"] == entailment
        assert excluded[0]["coverage_queue_exclusion_reason"] == "entailment_rejected"


def test_entailment_gate_connection_error_routes_excluded(monkeypatch):
    def fake_post(*_args, **_kwargs):
        raise retrieval_filter_v2_mod.requests.exceptions.ConnectionError("down")

    monkeypatch.setattr(retrieval_filter_v2_mod.requests, "post", fake_post)

    coverage, excluded = split_rows_by_entailment_gate([_coverage_row()])

    assert coverage == []
    assert len(excluded) == 1
    assert excluded[0]["entailment_gate_decision"] == "error"
    assert excluded[0]["coverage_queue_exclusion_reason"] == "entailment_error"


def test_entailment_gate_json_decode_error_routes_excluded(monkeypatch):
    def fake_post(*_args, **_kwargs):
        return _EntailmentResponse(json_exc=json.JSONDecodeError("bad", "", 0))

    monkeypatch.setattr(retrieval_filter_v2_mod.requests, "post", fake_post)

    coverage, excluded = split_rows_by_entailment_gate([_coverage_row()])

    assert coverage == []
    assert len(excluded) == 1
    assert excluded[0]["entailment_gate_decision"] == "error"
    assert excluded[0]["coverage_queue_exclusion_reason"] == "entailment_error"


def test_openai_compatible_entailment_records_usage(monkeypatch):
    class Response:
        def raise_for_status(self):
            return None

        def json(self):
            return {
                "choices": [
                    {
                        "message": {
                            "content": '```json\n{"entailment":"yes","reason":"supported"}\n```',
                        }
                    }
                ],
                "usage": {"prompt_tokens": 10, "completion_tokens": 4, "total_tokens": 14},
            }

    seen = {}

    def fake_post(url, **kwargs):
        seen["url"] = url
        seen["json"] = kwargs["json"]
        return Response()

    monkeypatch.setattr(retrieval_filter_v2_mod.requests, "post", fake_post)

    result = retrieval_filter_v2_mod.evaluate_entailment_gate_gemini(
        _coverage_row(),
        model="google/gemini-3.1-pro-preview",
        api_key="test-key",
        timeout=1,
    )

    assert result.entailment == "yes"
    assert result.prompt_tokens == 10
    assert result.completion_tokens == 4
    assert result.total_tokens == 14
    assert seen["url"] == "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
    assert seen["json"]["model"] == "gemini-3.1-pro-preview"
