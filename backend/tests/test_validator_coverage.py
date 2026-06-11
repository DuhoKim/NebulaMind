import json
from pathlib import Path

from scripts import validator_coverage as mod
from scripts.retrieval_filter_v2 import apply_retrieval_filter


def row(**extra):
    base = {
        "retrieval_filter_run_id": 4,
        "claim_id": 1,
        "element_id": "claim-1-e01",
        "arxiv_id": "1234.5678",
        "candidate_key": "candidate-1",
        "section": "section_a",
        "dropped": False,
        "final_score": 0.5,
        "retrieval_filter_decision": "keep",
        "claim_text_snapshot": "Outflows suppress star formation.",
        "element_text": "Outflows suppress star formation",
        "required": True,
        "paper_title_snapshot": "Fast outflows",
        "paper_abstract_snapshot": "Fast outflows suppress star formation.",
        "candidate_atom_coverage_status": "ready",
        "candidate_atoms": [{"atom_text": "Fast outflows suppress star formation.", "support_relation": "direct"}],
        "entailment_gate_decision": "yes",
    }
    base.update(extra)
    return base


def calibration():
    return {
        "retrieval_filter_v2_boundary_review": {
            "scope": {"enabled_sections": ["section_a"], "excluded_sections": []},
            "section_rules": {
                "section_a": {
                    "policy_id": "fixture_policy",
                    "hard_drop_below": 0.1,
                    "old_v1_floor": 0.2,
                    "protected_markers": [],
                    "tag_protection": {},
                }
            },
        }
    }


def test_retrieval_filter_rows_start_coverage_pending():
    [routed] = apply_retrieval_filter([row()], calibration())
    assert routed["coverage_status"] == "coverage_pending"
    assert routed["coverage_required_stages"] == ["atom_decomposition", "precheck", "astrosage_verdict"]
    assert routed["coverage_missing_stages"] == ["atom_decomposition", "precheck", "astrosage_verdict"]
    assert routed["coverage_artifact_refs"] == {}


def test_retryable_model_failure_does_not_mutate_retrieval_decision():
    source = row(candidate_atom_coverage_status="error_retryable", candidate_atoms=[], entailment_gate_decision="yes")
    [coverage] = mod.materialize_coverage_rows([source])
    assert coverage["coverage_status"] == "blocked_retryable"
    assert coverage["retrieval_filter_decision"] == source.get("retrieval_filter_decision")
    assert coverage["coverage_stage_statuses"]["atom_decomposition"] == "blocked_retryable"


def test_missing_prerequisite_row_stays_coverage_pending():
    source = row(candidate_atom_coverage_status=None, candidate_atoms=[], entailment_gate_decision="yes")
    [coverage] = mod.materialize_coverage_rows([source])
    assert coverage["coverage_status"] == "coverage_pending"
    assert coverage["coverage_stage_statuses"]["atom_decomposition"] == "coverage_pending"


def test_later_run_reuses_cached_coverage_when_key_versions_match():
    [first] = mod.materialize_coverage_rows([row()])
    [second] = mod.materialize_coverage_rows([row(retrieval_filter_run_id=5)], cached_rows=[first])
    assert second["coverage_status"] == "coverage_ready"
    assert second["coverage_artifact_refs"]["atom_decomposition"]["reused"] is True
    assert second["coverage_artifact_refs"]["precheck"]["reused"] is True
    assert second["coverage_artifact_refs"]["astrosage_verdict"]["reused"] is True
    assert second["retrieval_filter_run_id"] == 5


def test_db_run_id_3_fixture_remains_unchanged_by_reference_only():
    original = row(retrieval_filter_run_id=3)
    snapshot = json.loads(json.dumps(original, sort_keys=True))
    [coverage] = mod.materialize_coverage_rows([original])
    assert original == snapshot
    assert coverage["retrieval_filter_run_id"] == 3
    assert coverage["coverage_status"] == "coverage_ready"
    assert coverage["hydration_db_reads_used"] is False
    assert coverage["hydration_policy"] == "artifact_only_fail_closed"
    assert coverage["source_hashes"]["element_text_hash"] == mod.sha_text(original["element_text"])


def test_cli_writes_ready_manifest_and_blocked_report(tmp_path):
    input_path = tmp_path / "rows.jsonl"
    out_dir = tmp_path / "out"
    input_path.write_text(
        "\n".join(
            [
                json.dumps(row()),
                json.dumps(row(claim_id=2, element_id="claim-2-e01", candidate_key="candidate-2", candidate_atom_coverage_status="error_retryable", candidate_atoms=[])),
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    summary = mod.run(type("Args", (), {"input": input_path, "out_dir": out_dir, "cache": None})())
    assert summary["row_count"] == 2
    assert summary["ready_rows"] == 1
    assert summary["blocked_rows"] == 1
    assert len(read_jsonl(out_dir / "coverage_ready_manifest.jsonl")) == 1
    assert len(read_jsonl(out_dir / "blocked_rows.jsonl")) == 1


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
