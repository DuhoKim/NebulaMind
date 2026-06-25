import argparse
import json
from pathlib import Path

import pytest

import scripts.candidate_grounded_atom_backfill as mod


def row(**extra):
    base = {
        "retrieval_filter_run_id": 6,
        "claim_id": 1,
        "element_id": "claim-1-e01",
        "element_index": 1,
        "arxiv_id": "1234.56789",
        "section": "section_a",
        "retrieval_filter_decision": "keep",
        "label": "citable",
        "candidate_key": "candidate-1",
        "candidate_source": "fixture",
        "claim_text_snapshot": "Outflows suppress star formation.",
        "element_text": "Outflows suppress star formation",
        "element_type": "mechanism",
        "required": True,
        "normalized_subject": None,
        "normalized_mechanism": "outflows suppress star formation",
        "quantity_or_range": None,
        "redshift_or_environment": None,
        "paper_title_snapshot": "Fast outflows in compact systems",
        "paper_abstract_snapshot": "We show that fast outflows suppress star formation in compact systems.",
        "matched_terms": ["outflows", "suppress"],
        "element_matched_terms": ["outflows", "suppress"],
        "source_candidate_artifact": "fixture/element_candidate_pairs.jsonl",
    }
    base.update(extra)
    return base


def write_source(source_dir: Path, rows: list[dict]) -> None:
    pair_dir = source_dir / "validator_firm_keep_run"
    pair_dir.mkdir(parents=True)
    with (pair_dir / "element_candidate_pairs.jsonl").open("w", encoding="utf-8") as handle:
        for item in rows:
            handle.write(json.dumps(item) + "\n")
    (source_dir / "validator_brk_run").mkdir()
    (source_dir / "retrieval_filter_v2_ship_routed_rows.jsonl").write_text("", encoding="utf-8")


def write_split_source(source_dir: Path, firm_rows: list[dict], brk_rows: list[dict], routed_rows: list[dict]) -> None:
    for subdir, rows in [("validator_firm_keep_run", firm_rows), ("validator_brk_run", brk_rows)]:
        pair_dir = source_dir / subdir
        pair_dir.mkdir(parents=True)
        with (pair_dir / "element_candidate_pairs.jsonl").open("w", encoding="utf-8") as handle:
            for item in rows:
                handle.write(json.dumps(item) + "\n")
    with (source_dir / "retrieval_filter_v2_ship_routed_rows.jsonl").open("w", encoding="utf-8") as handle:
        for item in routed_rows:
            handle.write(json.dumps(item) + "\n")


def ready_model_response(_model, _prompt, _timeout):
    return (
        json.dumps(
            {
                "candidate_atom_coverage_status": "ready",
                "candidate_atoms": [
                    {
                        "atom_text": "Fast outflows suppress star formation in compact systems.",
                        "atom_type": "mechanism",
                        "evidence_anchor_terms": ["outflows", "suppress"],
                        "evidence_anchor_numbers": [],
                        "quoted_span_or_null": "fast outflows suppress star formation",
                        "support_relation": "direct",
                        "confidence": 0.91,
                    }
                ],
                "rationale": "Grounded in the abstract.",
                "failure_mode": None,
            }
        ),
        0.01,
    )


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def semantic_supported(row, *_args, **_kwargs):
    return {
        "coverage_candidate": True,
        "semantic_similarity": 0.9,
        "semantic_similarity_threshold": 0.5,
        "semantic_support_status": "semantic_supported",
        "semantic_support_error": None,
    }


def test_a_producer_emits_inline_snapshots(monkeypatch):
    monkeypatch.setattr(mod, "ollama_chat", ready_model_response)
    out = mod.coverage_row(row(), "coverage_run")
    assert out["candidate_atom_coverage_status"] == "ready"
    assert out["claim_text_snapshot"] == "Outflows suppress star formation."
    assert out["element_text"] == "Outflows suppress star formation"
    assert out["paper_title_snapshot"] == "Fast outflows in compact systems"
    assert out["paper_abstract_snapshot"] == "We show that fast outflows suppress star formation in compact systems."
    assert out["required"] is True
    assert out["hydration_db_reads_used"] is False
    assert out["hydration_sources"] == {
        "claim_text": "artifact",
        "element_text": "artifact",
        "paper_title": "artifact",
        "paper_abstract": "artifact",
    }


def test_b_producer_fails_closed_on_missing_text(tmp_path, monkeypatch):
    monkeypatch.setattr(mod, "semantic_support_features", semantic_supported)
    source_dir = tmp_path / "source"
    out_dir = tmp_path / "out"
    write_source(source_dir, [row(paper_abstract_snapshot="")])
    args = argparse.Namespace(
        source_dir=source_dir,
        out_dir=out_dir,
        retrieval_run_id=6,
        section=None,
        limit=0,
        model="fixture-model",
        timeout=1,
        no_model=True,
        progress_every=0,
    )
    with pytest.raises(ValueError, match="HYDRATION_ARTIFACT_MISSING_TEXT"):
        mod.run_backfill(args)
    assert not (out_dir / "validator_ready_rows.jsonl").exists()


def test_c_no_db_imports_in_producer_hydration_path():
    content = Path("scripts/candidate_grounded_atom_backfill.py").read_text(encoding="utf-8")
    forbidden = ["SessionLocal", "ArxivPaper", "app.database", "app.models.arxiv"]
    assert all(token not in content for token in forbidden)


def test_d_hydration_manifest_is_artifact_only(tmp_path, monkeypatch):
    monkeypatch.setattr(mod, "ollama_chat", ready_model_response)
    monkeypatch.setattr(mod, "semantic_support_features", semantic_supported)
    source_dir = tmp_path / "source"
    out_dir = tmp_path / "out"
    write_source(source_dir, [row()])
    args = argparse.Namespace(
        source_dir=source_dir,
        out_dir=out_dir,
        retrieval_run_id=6,
        section=None,
        limit=0,
        model="fixture-model",
        timeout=1,
        no_model=False,
        progress_every=0,
    )
    mod.run_backfill(args)
    manifest = json.loads((out_dir / "hydration_manifest.json").read_text(encoding="utf-8"))
    assert manifest["hydration_policy"] == "artifact_only_fail_closed"
    assert manifest["hydration_db_reads_used"] is False
    assert manifest["db_writes_used"] is False
    assert manifest["coverage_rows"] == 1
    assert manifest["validator_ready_rows"] == 1


def test_e_required_must_be_boolean():
    with pytest.raises(ValueError, match="HYDRATION_ARTIFACT_MISSING_TEXT"):
        mod.coverage_row(row(required=None), "coverage_run", use_model=False)


def test_f_source_hashes_match_inline_text(monkeypatch):
    monkeypatch.setattr(mod, "ollama_chat", ready_model_response)
    out = mod.coverage_row(row(), "coverage_run")
    assert out["source_hashes"] == {
        "claim_text_hash": mod.sha_text(out["claim_text_snapshot"]),
        "element_text_hash": mod.sha_text(out["element_text"]),
        "paper_title_hash": mod.sha_text(out["paper_title_snapshot"]),
        "paper_abstract_hash": mod.sha_text(out["paper_abstract_snapshot"]),
    }


def test_g_extract_json_repairs_latex_backslashes():
    payload = mod.extract_json_object(
        r'''{
  "candidate_atom_coverage_status": "missing",
  "candidate_atoms": [],
  "rationale": "The paper reports $\langle z \rangle=0.036$, not z > 1.",
  "failure_mode": null
}'''
    )
    assert payload["candidate_atom_coverage_status"] == "missing"
    assert r"\langle" in payload["rationale"]


def test_h_extract_json_repairs_unquoted_anchor_numbers():
    payload = mod.extract_json_object(
        '''{
  "candidate_atom_coverage_status": "ready",
  "candidate_atoms": [
    {
      "atom_text": "AGN feedback is the primary quenching mechanism",
      "atom_type": "relationship",
      "evidence_anchor_terms": ["AGN feedback"],
      "evidence_anchor_numbers": [2512.16208v1, 1865],
      "quoted_span_or_null": null,
      "support_relation": "direct",
      "confidence": 0.95
    }
  ],
  "rationale": "Grounded.",
  "failure_mode": null
}'''
    )
    assert payload["candidate_atoms"][0]["evidence_anchor_numbers"] == ["2512.16208v1", "1865"]


def test_i_extract_json_ignores_trailing_prose():
    payload = mod.extract_json_object(
        '''{
  "candidate_atom_coverage_status": "missing",
  "candidate_atoms": [],
  "rationale": "No support.",
  "failure_mode": null
}

The paper is outside the target scope.'''
    )
    assert payload["candidate_atom_coverage_status"] == "missing"


def test_n_full_artifact_smoke(tmp_path, monkeypatch):
    monkeypatch.setattr(mod, "ollama_chat", ready_model_response)
    monkeypatch.setattr(mod, "semantic_support_features", semantic_supported)
    source_dir = tmp_path / "source"
    out_dir = tmp_path / "out"
    write_source(source_dir, [row()])
    args = argparse.Namespace(
        source_dir=source_dir,
        out_dir=out_dir,
        retrieval_run_id=6,
        section=None,
        limit=25,
        model="fixture-model",
        timeout=1,
        no_model=False,
        progress_every=0,
    )
    mod.run_backfill(args)
    ready = read_jsonl(out_dir / "validator_ready_rows.jsonl")
    assert len(ready) == 1
    assert ready[0]["candidate_atom_coverage_status"] == "ready"
    assert (out_dir / "coverage_summary.json").exists()
    assert (out_dir / "REPORT.md").exists()


def test_o_brk_row_goes_to_audit_file_not_main_queue(tmp_path, monkeypatch):
    monkeypatch.setattr(mod, "ollama_chat", ready_model_response)
    monkeypatch.setattr(mod, "semantic_support_features", semantic_supported)
    source_dir = tmp_path / "source"
    out_dir = tmp_path / "out"
    brk = row(claim_id=2, element_id="claim-2-e01", candidate_key="candidate-2")
    write_split_source(
        source_dir,
        firm_rows=[row()],
        brk_rows=[brk],
        routed_rows=[
            {"claim_id": 1, "element_id": "claim-1-e01", "paper_id": "1234.56789", "label": "citable", "retrieval_filter_decision": "keep"},
            {"claim_id": 2, "element_id": "claim-2-e01", "paper_id": "1234.56789", "label": "citable", "retrieval_filter_decision": "boundary_review_keep"},
        ],
    )
    args = argparse.Namespace(source_dir=source_dir, out_dir=out_dir, retrieval_run_id=6, section=None, limit=0, model="fixture-model", timeout=1, no_model=False, progress_every=0)
    mod.run_backfill(args)
    main = read_jsonl(out_dir / "coverage_rows.jsonl")
    audit = read_jsonl(out_dir / "audit_only_coverage_rows.jsonl")
    assert [r["claim_id"] for r in main] == [1]
    assert [r["claim_id"] for r in audit] == [2]
    manifest = json.loads((out_dir / "hydration_manifest.json").read_text(encoding="utf-8"))
    assert manifest["audit_only_coverage_rows"] == 1


def test_p_off_domain_excluded_from_main_and_audit(tmp_path, monkeypatch):
    monkeypatch.setattr(mod, "ollama_chat", ready_model_response)
    monkeypatch.setattr(mod, "semantic_support_features", semantic_supported)
    source_dir = tmp_path / "source"
    out_dir = tmp_path / "out"
    off = row(claim_id=3, element_id="claim-3-e01", candidate_key="candidate-3", label="off_domain")
    write_split_source(
        source_dir,
        firm_rows=[row(), off],
        brk_rows=[],
        routed_rows=[
            {"claim_id": 1, "element_id": "claim-1-e01", "paper_id": "1234.56789", "label": "citable", "retrieval_filter_decision": "keep"},
            {"claim_id": 3, "element_id": "claim-3-e01", "paper_id": "1234.56789", "label": "off_domain", "retrieval_filter_decision": "keep"},
        ],
    )
    args = argparse.Namespace(source_dir=source_dir, out_dir=out_dir, retrieval_run_id=6, section=None, limit=0, model="fixture-model", timeout=1, no_model=False, progress_every=0)
    mod.run_backfill(args)
    assert [r["claim_id"] for r in read_jsonl(out_dir / "coverage_rows.jsonl")] == [1]
    assert read_jsonl(out_dir / "audit_only_coverage_rows.jsonl") == []
    excluded = read_jsonl(out_dir / "excluded_coverage_rows.jsonl")
    assert excluded[0]["coverage_queue_exclusion_reason"] == "off_domain"


def test_q_ready_rate_denominator_excludes_brk_off_domain_and_element_unsupported(tmp_path, monkeypatch):
    monkeypatch.setattr(mod, "ollama_chat", ready_model_response)
    def semantic_by_claim(row, *_args, **_kwargs):
        if row.get("claim_id") == 4:
            return {
                "coverage_candidate": False,
                "semantic_similarity": 0.1,
                "semantic_similarity_threshold": 0.5,
                "semantic_support_status": "semantic_unsupported",
                "semantic_support_error": None,
            }
        return semantic_supported(row)
    monkeypatch.setattr(mod, "semantic_support_features", semantic_by_claim)
    source_dir = tmp_path / "source"
    out_dir = tmp_path / "out"
    unsupported = row(
        claim_id=4,
        element_id="claim-4-e01",
        candidate_key="candidate-4",
        element_text="halo mass threshold",
        normalized_mechanism="halo mass threshold",
        paper_title_snapshot="Optical variability",
        paper_abstract_snapshot="We study optical light curves of a compact source.",
    )
    brk = row(claim_id=5, element_id="claim-5-e01", candidate_key="candidate-5")
    off = row(claim_id=6, element_id="claim-6-e01", candidate_key="candidate-6", label="off_domain")
    write_split_source(
        source_dir,
        firm_rows=[row(), unsupported, off],
        brk_rows=[brk],
        routed_rows=[
            {"claim_id": 1, "element_id": "claim-1-e01", "paper_id": "1234.56789", "label": "citable", "retrieval_filter_decision": "keep"},
            {"claim_id": 4, "element_id": "claim-4-e01", "paper_id": "1234.56789", "label": "citable", "retrieval_filter_decision": "keep"},
            {"claim_id": 5, "element_id": "claim-5-e01", "paper_id": "1234.56789", "label": "citable", "retrieval_filter_decision": "boundary_review_keep"},
            {"claim_id": 6, "element_id": "claim-6-e01", "paper_id": "1234.56789", "label": "off_domain", "retrieval_filter_decision": "keep"},
        ],
    )
    args = argparse.Namespace(source_dir=source_dir, out_dir=out_dir, retrieval_run_id=6, section=None, limit=0, model="fixture-model", timeout=1, no_model=False, progress_every=0)
    report = mod.run_backfill(args)
    assert report["summary"]["non_off_domain_rows"] == 1
    assert report["summary"]["non_off_domain_ready_rate"] == 1.0
    excluded = read_jsonl(out_dir / "excluded_coverage_rows.jsonl")
    assert {r["coverage_queue_exclusion_reason"] for r in excluded} == {"semantic_unsupported", "off_domain"}


def test_r_gemini_entailment_provider_uses_existing_key_path(tmp_path, monkeypatch):
    monkeypatch.setenv("TEST_GEMINI_API_KEY", "fixture-key")
    monkeypatch.setattr(mod, "ollama_chat", ready_model_response)
    monkeypatch.setattr(mod, "semantic_support_features", semantic_supported)

    calls = []

    def fake_gemini(row, *, model, base_url, api_key, timeout):
        from scripts.retrieval_filter_v2 import EntailmentGateResult

        calls.append({"model": model, "base_url": base_url, "api_key": api_key, "timeout": timeout})
        return EntailmentGateResult(
            entailment="yes",
            reason="supported",
            latency_seconds=0.01,
            prompt_tokens=11,
            completion_tokens=5,
            total_tokens=16,
        )

    monkeypatch.setattr(mod, "evaluate_entailment_gate_gemini", fake_gemini)
    source_dir = tmp_path / "source"
    out_dir = tmp_path / "out"
    write_source(source_dir, [row()])
    args = argparse.Namespace(
        source_dir=source_dir,
        out_dir=out_dir,
        retrieval_run_id=6,
        section=None,
        limit=25,
        model="fixture-model",
        timeout=1,
        no_model=False,
        progress_every=0,
        min_semantic_similarity=0.5,
        ollama_host="http://localhost:11434",
        no_entailment_gate=False,
        entailment_provider="gemini",
        entailment_model="google/gemini-2.5-flash",
        entailment_timeout=30,
        entailment_ollama_host=None,
        entailment_base_url=None,
        entailment_api_key_env="TEST_GEMINI_API_KEY",
    )
    mod.run_backfill(args)

    assert calls == [
        {
            "model": "google/gemini-2.5-flash",
            "base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
            "api_key": "fixture-key",
            "timeout": 30,
        }
    ]
    coverage = read_jsonl(out_dir / "coverage_rows.jsonl")
    assert coverage[0]["entailment_gate_decision"] == "yes"
    assert coverage[0]["entailment_gate_total_tokens"] == 16
    manifest = json.loads((out_dir / "hydration_manifest.json").read_text(encoding="utf-8"))
    assert manifest["entailment_gate_provider"] == "gemini"
