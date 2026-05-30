import json
from argparse import Namespace
from pathlib import Path

import pytest

import scripts.arxiv_wiki_feed_v2_validate_elements as mod


def ready_row(**extra):
    base = {
        "coverage_run_id": "coverage_run",
        "coverage_key": "coverage-key-1",
        "retrieval_filter_run_id": 6,
        "section": "s1",
        "claim_id": 1,
        "element_id": "claim-1-e01",
        "arxiv_id": "1234.5678",
        "candidate_key": "candidate-1",
        "retrieval_filter_decision": "keep",
        "source_label": "citable",
        "candidate_atom_coverage_status": "ready",
        "candidate_atoms": [{"atom_text": "supported", "support_relation": "direct"}],
        "claim_text_snapshot": "Outflows suppress star formation.",
        "element_text": "Outflows suppress star formation",
        "element_type": "mechanism",
        "required": True,
        "paper_title_snapshot": "Fast outflows",
        "paper_abstract_snapshot": "Fast outflows suppress star formation.",
        "matched_terms": ["outflows"],
        "element_matched_terms": ["outflows"],
        "hydration_sources": {
            "claim_text": "artifact",
            "element_text": "artifact",
            "paper_title": "artifact",
            "paper_abstract": "artifact",
        },
        "hydration_db_reads_used": False,
        "hydration_policy": "artifact_only_fail_closed",
    }
    base["source_hashes"] = {
        "claim_text_hash": mod.sha_text(base["claim_text_snapshot"]),
        "element_text_hash": mod.sha_text(base["element_text"]),
        "paper_title_hash": mod.sha_text(base["paper_title_snapshot"]),
        "paper_abstract_hash": mod.sha_text(base["paper_abstract_snapshot"]),
    }
    base.update(extra)
    if not extra.get("source_hashes"):
        base["source_hashes"] = {
            "claim_text_hash": mod.sha_text(base.get("claim_text_snapshot")),
            "element_text_hash": mod.sha_text(base.get("element_text")),
            "paper_title_hash": mod.sha_text(base.get("paper_title_snapshot")),
            "paper_abstract_hash": mod.sha_text(base.get("paper_abstract_snapshot")),
        }
    return base


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def test_g_validator_does_not_hydrate_from_db(tmp_path):
    path = tmp_path / "validator_ready_rows.jsonl"
    write_jsonl(path, [ready_row(paper_title_snapshot="", paper_abstract_snapshot="")])
    with pytest.raises(ValueError, match="HYDRATION_ARTIFACT_MISSING_TEXT"):
        mod.build_targeted_pairs_from_coverage_ready(path, tmp_path / "source", tmp_path / "out", require_hydrated=True)
    content = Path("scripts/arxiv_wiki_feed_v2_validate_elements.py").read_text(encoding="utf-8")
    assert "SessionLocal" not in content
    assert "ArxivPaper" not in content


def test_h_validator_does_not_expand_sibling_elements(tmp_path):
    path = tmp_path / "validator_ready_rows.jsonl"
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    write_jsonl(path, [ready_row()])
    pairs = mod.build_targeted_pairs_from_coverage_ready(path, source_dir, tmp_path / "out", require_hydrated=True)
    assert len(pairs) == 1
    assert pairs[0]["element_id"] == "claim-1-e01"
    assert pairs[0]["claim_text_snapshot"] == "Outflows suppress star formation."


def test_i_targeted_metrics_show_no_db_reads(tmp_path):
    path = tmp_path / "validator_ready_rows.jsonl"
    out_dir = tmp_path / "out"
    write_jsonl(path, [ready_row()])
    mod.build_targeted_pairs_from_coverage_ready(path, None, out_dir, require_hydrated=True)
    metrics = json.loads((out_dir / "targeted_metrics.json").read_text(encoding="utf-8"))
    assert metrics["coverage_ready_input_rows"] == 1
    assert metrics["targeted_pair_rows"] == 1
    assert metrics["hydration_missing_rows"] == 0
    assert metrics["db_reads_used"] is False
    assert metrics["hydration_policy"] == "artifact_only_fail_closed"
    assert metrics["precheck_empty_text_failures"] == 0


def test_j_existing_default_validator_path_still_exists():
    assert hasattr(mod, "merge_elements")
    assert hasattr(mod, "build_pairs")


def test_duplicate_target_tuple_rejected(tmp_path):
    path = tmp_path / "validator_ready_rows.jsonl"
    write_jsonl(path, [ready_row(), ready_row()])
    with pytest.raises(ValueError, match="DUPLICATE_TARGET_TUPLE"):
        mod.build_targeted_pairs_from_coverage_ready(path, None, tmp_path / "out", require_hydrated=True)


def test_hash_mismatch_blocks_before_voting(tmp_path):
    path = tmp_path / "validator_ready_rows.jsonl"
    write_jsonl(path, [ready_row(source_hashes={"claim_text_hash": "bad"})])
    with pytest.raises(ValueError, match="HYDRATION_ARTIFACT_HASH_MISMATCH"):
        mod.build_targeted_pairs_from_coverage_ready(path, None, tmp_path / "out", require_hydrated=True)


def test_m_promotion_safety_flags_remain_false(tmp_path):
    path = tmp_path / "validator_ready_rows.jsonl"
    out_dir = tmp_path / "out"
    write_jsonl(path, [ready_row()])
    pairs = mod.build_targeted_pairs_from_coverage_ready(path, None, out_dir, require_hydrated=True)
    write_jsonl(
        out_dir / "element_votes_atom.jsonl",
        [
            {
                "candidate_key": pairs[0]["candidate_key"],
                "element_id": "claim-1-e01",
                "label": "supported",
                "score": 0.9,
            }
        ],
    )
    aggregates = mod.aggregate(out_dir)
    assert aggregates[0]["targeted_coverage_mode"] is True
    assert aggregates[0]["coverage_ready_targeted_run"] is True
    assert aggregates[0]["promotion_eligible"] is False
    shadow = json.loads((out_dir / "promotion_manifest_phase2_shadow.json").read_text(encoding="utf-8"))
    assert shadow["promotion_eligible"] is False
    assert shadow["validated_ready"] == []


def test_n_count_gate_fallback_is_expand_first(tmp_path):
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    (out_dir / "targeted_metrics.json").write_text(
        json.dumps(
            {
                "coverage_ready_input_rows": 1,
                "targeted_pair_rows": 1,
                "hydration_missing_rows": 0,
                "db_reads_used": False,
                "hydration_policy": "artifact_only_fail_closed",
            }
        ),
        encoding="utf-8",
    )
    write_jsonl(out_dir / "claim_candidate_aggregate.jsonl", [])
    args = Namespace(
        no_db_write=True,
        phase1_elements="p1",
        phase15_elements="p15",
        candidates="candidates",
    )
    metrics = mod.build_metrics(out_dir, args)
    assert metrics["promotion_eligible"] is False
    assert metrics["next_step"] == "expand_coverage_first"
