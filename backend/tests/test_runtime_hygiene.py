import inspect
import sys
import types
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


def test_marker_reembed_gate_defaults_off(monkeypatch):
    from app.agent_loop.marker_embed import tasks

    class FakeRedisClient:
        def get(self, key):
            assert key == "marker_embed:enabled"
            return None

    fake_redis = types.SimpleNamespace(
        from_url=lambda *args, **kwargs: FakeRedisClient()
    )

    monkeypatch.delenv("MARKER_REEMBED_ENABLED", raising=False)
    monkeypatch.setitem(sys.modules, "redis", fake_redis)

    assert tasks.marker_reembed_enabled() is False


def test_marker_reembed_gate_allows_explicit_env(monkeypatch):
    from app.agent_loop.marker_embed import tasks

    monkeypatch.setenv("MARKER_REEMBED_ENABLED", "1")

    assert tasks.marker_reembed_enabled() is True


def test_stance_jury_hold_helpers(monkeypatch):
    from app.agent_loop import tasks

    monkeypatch.setattr(tasks.settings, "STANCE_JURY_HELD_PAGE_IDS", "57, bad-token")
    monkeypatch.setattr(tasks.settings, "STANCE_JURY_HELD_CLAIM_IDS", "2905")
    monkeypatch.setattr(tasks.settings, "STANCE_JURY_HELD_EVIDENCE_IDS", "27096")

    ev = types.SimpleNamespace(id=27095, claim_id=2905)
    claim = types.SimpleNamespace(id=2905, page_id=12)

    assert tasks._stance_jury_is_held(ev=ev, claim=claim)
    assert tasks._stance_jury_is_held(evidence_id=27096)
    assert tasks._stance_jury_is_held(page_id=57)
    assert not tasks._stance_jury_is_held(evidence_id=1, claim_id=2, page_id=3)
