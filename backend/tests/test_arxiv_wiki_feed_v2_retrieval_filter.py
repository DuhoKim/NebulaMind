import json
import inspect
from pathlib import Path

import scripts.arxiv_wiki_feed_v2_retrieval_filter as mod
from scripts.arxiv_wiki_feed_v2_retrieval_filter import (
    build_candidate_rows,
    element_support_features,
    semantic_support_features,
    semantic_threshold_from_calibration,
)


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")


def test_element_support_gate_hits_content_token():
    features = element_support_features(
        "Ram pressure stripping removes gas",
        "The abstract describes ram pressure stripping in cluster satellites.",
    )
    assert features["element_support_gate"] is True
    assert "ram" in features["element_support_terms"]
    assert features["element_support_numbers"] == []


def test_element_support_gate_hits_numeric_literal():
    features = element_support_features(
        "Quenching occurs below 10.5 solar masses",
        "The paper reports a threshold of 10.5 for the sample.",
    )
    assert features["element_support_gate"] is True
    assert "10.5" in features["element_support_numbers"]


def test_element_support_gate_miss_is_page_agnostic(monkeypatch, tmp_path):
    candidates = tmp_path / "candidates.jsonl"
    labels = tmp_path / "labels.jsonl"
    write_jsonl(
        candidates,
        [
            {
                "candidate_key": "c1",
                "claim_id": 1,
                "element_id": "e1",
                "arxiv_id": "1234.5678",
                "claim_text_snapshot": "Cluster environment quenches satellites.",
                "element_text": "ram pressure stripping removes gas",
                "paper_title_snapshot": "Blazar variability",
                "paper_abstract_snapshot": "We study optical variability in a compact source.",
            }
        ],
    )
    write_jsonl(
        labels,
        [
            {
                "claim_id": 1,
                "element_id": "e1",
                "arxiv_id": "1234.5678",
                "target_section": "env_quenching",
                "label": "citable",
            }
        ],
    )
    monkeypatch.setattr(mod.requests, "post", lambda *_args, **_kwargs: DummyResponse([1.0, 0.0]))
    rows = build_candidate_rows(candidates, labels, ollama_host="http://fixture")
    assert len(rows) == 1
    assert rows[0]["element_support_gate"] is False
    assert rows[0]["element_support_terms"] == []
    assert rows[0]["element_support_threshold"] == ">=1_content_token_or_>=1_numeric_literal"


class DummyResponse:
    def __init__(self, embedding):
        self.embedding = embedding

    def raise_for_status(self):
        return None

    def json(self):
        return {"embedding": self.embedding}


def test_mocked_embedding_semantic_gate_hit_and_miss(monkeypatch, tmp_path):
    candidates = tmp_path / "candidates.jsonl"
    labels = tmp_path / "labels.jsonl"
    write_jsonl(
        candidates,
        [
            {
                "candidate_key": "low",
                "claim_id": 1,
                "element_id": "e-low",
                "arxiv_id": "1111.1111",
                "element_text": "alpha",
                "paper_abstract_snapshot": "beta",
            },
            {
                "candidate_key": "high",
                "claim_id": 2,
                "element_id": "e-high",
                "arxiv_id": "2222.2222",
                "element_text": "gamma",
                "paper_abstract_snapshot": "gamma aligned",
            },
        ],
    )
    write_jsonl(
        labels,
        [
            {"claim_id": 1, "element_id": "e-low", "arxiv_id": "1111.1111", "target_section": "env_quenching", "label": "citable"},
            {"claim_id": 2, "element_id": "e-high", "arxiv_id": "2222.2222", "target_section": "env_quenching", "label": "citable"},
        ],
    )

    def fake_post(_url, json, timeout):
        prompt = json["prompt"]
        if prompt == "alpha":
            return DummyResponse([1.0, 0.0])
        if prompt == "beta":
            return DummyResponse([0.0, 1.0])
        return DummyResponse([1.0, 0.0])

    monkeypatch.setattr(mod.requests, "post", fake_post)
    rows = build_candidate_rows(candidates, labels, min_semantic_similarity=0.50, ollama_host="http://fixture")
    by_key = {row["candidate_key"]: row for row in rows}
    assert by_key["low"]["coverage_candidate"] is False
    assert by_key["low"]["semantic_support_status"] == "semantic_unsupported"
    assert by_key["high"]["coverage_candidate"] is True
    assert by_key["high"]["semantic_support_status"] == "semantic_supported"


def test_semantic_threshold_loads_from_page_calibration(tmp_path):
    calibration = tmp_path / "page.yaml"
    calibration.write_text("semantic_band:\n  min_semantic_similarity: 0.73\n", encoding="utf-8")
    assert semantic_threshold_from_calibration(calibration, 0.50) == 0.73


def test_semantic_band_embedding_failure_is_fail_closed(monkeypatch):
    def fail_post(*_args, **_kwargs):
        raise RuntimeError("embedding unavailable")

    monkeypatch.setattr(mod.requests, "post", fail_post)
    result = semantic_support_features("element text", "paper abstract", 0.50, "http://fixture")
    assert result["coverage_candidate"] is False
    assert result["semantic_support_status"] == "embedding_failed"


def test_semantic_filter_logic_is_page_agnostic():
    source = "\n".join(
        inspect.getsource(obj)
        for obj in [mod.get_embedding, mod.cosine_similarity, mod.semantic_support_features]
    ).lower()
    for forbidden in ["galaxy", "quenching", "astronomy", "environment"]:
        assert forbidden not in source


def test_semantic_filter_has_no_db_reads():
    source = "\n".join(
        inspect.getsource(obj)
        for obj in [mod.get_embedding, mod.cosine_similarity, mod.semantic_support_features, mod.build_candidate_rows]
    )
    for forbidden in ["SessionLocal", "sessionmaker", ".query(", "app.database"]:
        assert forbidden not in source
