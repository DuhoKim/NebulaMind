import inspect
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_gemini_routing_uses_batch_safe_flash(monkeypatch):
    from app.config import BATCH_SAFE_DEFAULT_MODEL
    from app.services.llm_routing import routing

    monkeypatch.setattr(routing.settings, "GEMINI_API_KEY", "test-key")
    spec = routing._gemini()

    assert spec is not None
    assert spec["model"] == BATCH_SAFE_DEFAULT_MODEL
    assert spec["label"] == BATCH_SAFE_DEFAULT_MODEL
    assert spec["model"] == "gemini-2.5-flash"


def test_council_sweep_uses_evidence_consensus_settlement():
    from app.agent_loop import tasks

    source = inspect.getsource(tasks.sweep_council_tiers)

    assert "Evidence.consensus_settled_at" in source
    assert "evidence_votes.settled" not in source
    assert "EvidenceVote.settled" not in source
