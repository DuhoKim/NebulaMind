import sys
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.auth import _hash_key
from app.database import Base
from app.models import (
    agent, arxiv, autowiki, benchmark, claim, claim_rewrite_lineage, comment,
    council, edit, evidence_element_link, external, facility, feedback, graph,
    jury, page, qa, reference, research_idea, social, spotlight, subscriber,
    survey, visitor, vote
)
from app.models.agent import Agent
from app.models.claim import Claim, Evidence, EvidenceVote, TrustAuditLog
from app.models.page import WikiPage
from scripts.promote_provisional_evidence import find_promotion_candidates, run_promotion, _print_text


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_promote_provisional_evidence.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def setup_function():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def seed_promotion_fixture(db):
    page_row = WikiPage(id=1, slug="promotion-runner", title="Promotion Runner")
    claim_row = Claim(id=1, page_id=1, text="Promotion Runner Claim", trust_level="unverified")
    promoter = Agent(
        id=7,
        name="promotion-runner-agent",
        model_name="test-model",
        role="reviewer",
        reputation=1.0,
        api_key_hash=_hash_key("promotion-runner-key"),
    )
    promotable = Evidence(
        id=1,
        claim_id=1,
        title="Promotable Evidence",
        stance="supports",
        quality=1.0,
        status="provisional",
        source_channel="targeted_ads_miner",
    )
    other_channel = Evidence(
        id=2,
        claim_id=1,
        title="Other Channel Evidence",
        stance="supports",
        quality=1.0,
        status="provisional",
        source_channel="dynamic_citation_context_mining",
    )
    active = Evidence(
        id=3,
        claim_id=1,
        title="Already Active Evidence",
        stance="supports",
        quality=1.0,
        status="active",
        source_channel="targeted_ads_miner",
    )
    db.add_all([page_row, claim_row, promoter, promotable, other_channel, active])
    db.flush()
    db.add(EvidenceVote(evidence_id=1, value=1, agent_id=7, weight=1.0))
    db.commit()
    return claim_row, promotable


def test_find_promotion_candidates_filters_to_provisional_source_channel():
    db = TestingSessionLocal()
    try:
        seed_promotion_fixture(db)

        candidates = find_promotion_candidates(db, source_channel="targeted_ads_miner", limit=10)

        assert [candidate.id for candidate in candidates] == [1]
    finally:
        db.close()


def test_promotion_runner_dry_run_reports_without_mutating():
    db = TestingSessionLocal()
    try:
        claim_row, promotable = seed_promotion_fixture(db)

        report = run_promotion(
            db,
            source_channel="targeted_ads_miner",
            limit=10,
            commit=False,
            actor_agent_id=7,
        )

        assert report["commit"] is False
        assert report["destructive_action"] is False
        assert report["candidate_count"] == 1
        assert report["promoted_count"] == 0
        assert report["sample"][0]["evidence_id"] == 1
        db.refresh(promotable)
        db.refresh(claim_row)
        assert promotable.status == "provisional"
        assert claim_row.trust_level == "unverified"
    finally:
        db.close()


def test_promotion_runner_commit_activates_and_recalculates():
    db = TestingSessionLocal()
    try:
        claim_row, promotable = seed_promotion_fixture(db)

        report = run_promotion(db, evidence_ids=[1], commit=True, actor_agent_id=7)

        assert report["commit"] is True
        assert report["destructive_action"] is False
        assert report["candidate_count"] == 1
        assert report["promoted_count"] == 1
        assert report["sample"][0]["old_trust_score"] == 0.0
        assert report["sample"][0]["new_trust_level"] == "accepted"
        assert report["sample"][0]["new_trust_score"] > 0.3
        assert report["sample"][0]["trust_score_delta"] == (
            report["sample"][0]["new_trust_score"] - report["sample"][0]["old_trust_score"]
        )
        db.refresh(promotable)
        db.refresh(claim_row)
        assert promotable.status == "active"
        assert claim_row.trust_level == "accepted"
        audit = db.query(TrustAuditLog).filter_by(trigger="provisional_evidence_promotion_runner").one()
        assert audit.claim_id == claim_row.id
        assert audit.triggered_by_agent_id == 7
    finally:
        db.close()


def test_promotion_runner_text_output_includes_trust_score_delta(capsys):
    _print_text({
        "commit": True,
        "destructive_action": False,
        "candidate_count": 1,
        "promoted_count": 1,
        "retention_policy": "not applicable; promotion activates rows and does not delete data",
        "sample": [{
            "evidence_id": 1,
            "claim_id": 1,
            "old_status": "provisional",
            "status": "active",
            "source_channel": "targeted_ads_miner",
            "title": "Promotable Evidence",
            "old_trust_score": 0.0,
            "new_trust_score": 0.8123,
            "trust_score_delta": 0.8123,
        }],
    })

    output = capsys.readouterr().out
    assert "trust_score=0.000->0.812" in output
    assert "trust_score_delta=+0.812" in output
