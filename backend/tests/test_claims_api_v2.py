import sys
import json
import logging
import datetime as dt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import get_db, Base
# Import all models to ensure they are registered with Base
from app.models import (
    agent, arxiv, autowiki, benchmark, claim, claim_rewrite_lineage, comment,
    council, edit, evidence_element_link, external, facility, feedback, graph,
    jury, page, qa, reference, research_idea, social, spotlight, subscriber,
    survey, visitor, vote
)
from app.models.claim import Claim, Evidence, EvidenceVote, TrustAuditLog
from app.models.evidence_element_link import EvidenceElementLink
from app.models.page import WikiPage
from app.models.agent import Agent
from app.auth import _hash_key


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
REPO_ROOT = Path(__file__).resolve().parents[1]
DEBATE_EVIDENCE_SCHEMA = json.loads((REPO_ROOT / "app/contracts/debate_evidence_v1.schema.json").read_text())
STATIC_PREVIEW_SAMPLE = json.loads((REPO_ROOT / "tests/fixtures/debate_evidence_static_preview_sample.json").read_text())


def assert_debate_evidence_contract(payload: dict):
    required = set(DEBATE_EVIDENCE_SCHEMA["required"])
    assert required <= payload.keys()
    assert payload["schema_version"] == "debate_evidence.v1"
    assert isinstance(payload["claim_id"], int)
    assert isinstance(payload["claim_text"], str)
    assert payload["trust_level"] in DEBATE_EVIDENCE_SCHEMA["properties"]["trust_level"]["enum"]
    assert payload["vote_scope"] == {
        "display_counts_unit": "evidence_id",
        "dedupe": "latest_vote_per_agent_id_per_evidence_id",
        "same_proposition_scoped": False,
        "limitation": (
            "votes_agree/votes_disagree are deduped display counts per evidence row; "
            "they are not independently scoped by proposition or claim element."
        ),
    }
    assert isinstance(payload["total_elements"], int)
    assert payload["total_elements"] >= 0
    assert isinstance(payload["evidence"], list)

    item_schema = DEBATE_EVIDENCE_SCHEMA["properties"]["evidence"]["items"]
    item_required = set(item_schema["required"])
    for item in payload["evidence"]:
        assert item_required <= item.keys()
        assert isinstance(item["id"], (int, str))
        assert isinstance(item["title"], str)
        assert item["arxiv_id"] is None or isinstance(item["arxiv_id"], str)
        assert item["url"] is None or isinstance(item["url"], str)
        assert item["authors"] is None or isinstance(item["authors"], str)
        assert item["year"] is None or isinstance(item["year"], int)
        assert item["summary"] is None or isinstance(item["summary"], str)
        assert item["stance"] is None or isinstance(item["stance"], str)
        assert item["status"] in {"active", "provisional"}
        assert isinstance(item["votes_agree"], int) and item["votes_agree"] >= 0
        assert isinstance(item["votes_disagree"], int) and item["votes_disagree"] >= 0
        assert isinstance(item["comments_count"], int) and item["comments_count"] >= 0
        assert isinstance(item["element_links"], list)
        assert isinstance(item["link_count"], int) and item["link_count"] >= 0
        for score_key in ("relevance", "entailment", "rigor", "confidence", "quality_v2"):
            assert item[score_key] is None or isinstance(item[score_key], (int, float))
        for link in item["element_links"]:
            assert {"element_id", "element_text_snapshot"} <= link.keys()
            assert isinstance(link["element_id"], (str, int))
            assert link["element_text_snapshot"] is None or isinstance(link["element_text_snapshot"], str)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_get_evidence_with_element_links(db_session):
    # Create a test page, claim and evidence
    test_page = WikiPage(id=1, slug="test-page", title="Test Page")
    test_claim = Claim(id=1, page_id=1, text="Test Claim")
    test_evidence = Evidence(id=1, claim_id=1, title="Test Evidence", arxiv_id="1234.5678")
    db_session.add(test_page)
    db_session.add(test_claim)
    db_session.add(test_evidence)
    db_session.commit()

    # Create an element link
    link = EvidenceElementLink(
        evidence_id=1,
        source_claim_id=1,
        target_claim_id=1,
        page_id=1,
        page_slug="test-page",
        element_id="test-element-1",
        element_text_snapshot="This is a test element.",
        arxiv_id="1234.5678"
    )
    db_session.add(link)
    db_session.commit()

    # Make the API request
    response = client.get("/api/claims/1/evidence")
    assert response.status_code == 200
    data = response.json()

    # Check the response
    assert "evidence" in data
    assert_debate_evidence_contract(data)
    assert data["schema_version"] == "debate_evidence.v1"
    assert data["trust_level"] == "unverified"
    assert len(data["evidence"]) == 1
    evidence_data = data["evidence"][0]
    assert "element_links" in evidence_data
    assert len(evidence_data["element_links"]) == 1
    link_data = evidence_data["element_links"][0]
    assert link_data["element_id"] == "test-element-1"
    assert link_data["element_text_snapshot"] == "This is a test element."
    assert "total_elements" in data
    assert data["total_elements"] == 1


def test_get_evidence_counts_unique_agent_and_anonymous_votes(db_session):
    test_page = WikiPage(id=11, slug="vote-page", title="Vote Page")
    test_claim = Claim(id=11, page_id=11, text="Vote Claim", trust_level="debated")
    test_evidence = Evidence(id=11, claim_id=11, title="Vote Evidence", arxiv_id="2601.11111")
    db_session.add_all([test_page, test_claim, test_evidence])
    db_session.flush()
    db_session.add_all([
        EvidenceVote(id=101, evidence_id=11, value=1, agent_id=7),
        EvidenceVote(id=102, evidence_id=11, value=-1, agent_id=9),
        EvidenceVote(id=103, evidence_id=11, value=1, agent_id=8),
        EvidenceVote(id=104, evidence_id=11, value=1, agent_id=None),
        EvidenceVote(id=105, evidence_id=11, value=-1, agent_id=None),
    ])
    db_session.commit()

    response = client.get("/api/claims/11/evidence")
    assert response.status_code == 200
    data = response.json()
    evidence_data = data["evidence"][0]

    assert data["schema_version"] == "debate_evidence.v1"
    assert data["trust_level"] == "debated"
    assert evidence_data["votes_agree"] == 3
    assert evidence_data["votes_disagree"] == 2
    assert_debate_evidence_contract(data)


def test_get_evidence_exposes_provisional_status(db_session):
    test_page = WikiPage(id=12, slug="provisional-page", title="Provisional Page")
    test_claim = Claim(id=12, page_id=12, text="Provisional Claim", trust_level="unverified")
    test_evidence = Evidence(
        id=12,
        claim_id=12,
        title="Provisional Evidence",
        arxiv_id="2601.12121",
        status="provisional",
    )
    db_session.add_all([test_page, test_claim, test_evidence])
    db_session.commit()

    response = client.get("/api/claims/12/evidence")
    assert response.status_code == 200
    data = response.json()
    assert_debate_evidence_contract(data)
    assert data["evidence"][0]["status"] == "provisional"


def test_evidence_vote_requires_api_key(db_session):
    test_page = WikiPage(id=21, slug="locked-vote-page", title="Locked Vote Page")
    test_claim = Claim(id=21, page_id=21, text="Locked Vote Claim")
    test_evidence = Evidence(id=21, claim_id=21, title="Locked Vote Evidence")
    db_session.add_all([test_page, test_claim, test_evidence])
    db_session.commit()

    response = client.post("/api/evidence/21/vote", json={"value": 1, "agent_id": 999})

    assert response.status_code == 422
    assert db_session.query(EvidenceVote).filter(EvidenceVote.evidence_id == 21).count() == 0


def test_evidence_vote_rejects_invalid_api_key(db_session):
    test_page = WikiPage(id=23, slug="invalid-key-vote-page", title="Invalid Key Vote Page")
    test_claim = Claim(id=23, page_id=23, text="Invalid Key Vote Claim")
    test_evidence = Evidence(id=23, claim_id=23, title="Invalid Key Vote Evidence")
    db_session.add_all([test_page, test_claim, test_evidence])
    db_session.commit()

    response = client.post(
        "/api/evidence/23/vote",
        headers={"X-API-Key": "not-a-real-key"},
        json={"value": 1, "agent_id": 999},
    )

    assert response.status_code == 401
    assert db_session.query(EvidenceVote).filter(EvidenceVote.evidence_id == 23).count() == 0


def test_evidence_vote_deprecated_no_write_with_valid_auth(db_session, caplog):
    api_key = "test-agent-key"
    test_page = WikiPage(id=22, slug="authed-vote-page", title="Authed Vote Page")
    test_claim = Claim(id=22, page_id=22, text="Authed Vote Claim", trust_level="challenged")
    test_evidence = Evidence(id=22, claim_id=22, title="Authed Vote Evidence")
    test_agent = Agent(
        id=42,
        name="vote-lock-agent",
        model_name="test-model",
        role="reviewer",
        api_key_hash=_hash_key(api_key),
    )
    db_session.add_all([test_page, test_claim, test_evidence, test_agent])
    db_session.commit()

    with caplog.at_level(logging.WARNING, logger="app.routers.claims"):
        response = client.post(
            "/api/evidence/22/vote",
            headers={"X-API-Key": api_key},
            json={"value": 1, "agent_id": 999, "reason": "authenticated"},
        )

    assert response.status_code == 200
    assert response.headers["X-API-Deprecated"] == "true"
    assert response.headers["X-API-No-Write"] == "true"
    assert response.headers["X-API-Replacement"] == "/api/jury/tasks/{task_id}/vote"
    data = response.json()
    assert data["deprecated"] is True
    assert data["no_write"] is True
    assert data["replacement"] == "/api/jury/tasks/{task_id}/vote"
    assert data["authenticated_agent_id"] == 42
    assert "no vote was committed" in data["detail"]
    assert db_session.query(EvidenceVote).filter(EvidenceVote.evidence_id == 22).count() == 0
    db_session.refresh(test_claim)
    assert test_claim.trust_level == "challenged"
    assert "deprecated_legacy_evidence_vote_no_write" in caplog.text
    assert "'route_name': 'vote_evidence'" in caplog.text
    assert "'evidence_id': 22" in caplog.text
    assert "'authenticated_agent_id': 42" in caplog.text
    assert "'no_write': True" in caplog.text


def test_promote_evidence_endpoint_activates_and_recalculates(db_session):
    api_key = "promote-agent-key"
    test_page = WikiPage(id=24, slug="promote-page", title="Promote Page")
    test_claim = Claim(id=24, page_id=24, text="Promote Claim", trust_level="unverified")
    test_evidence = Evidence(
        id=24,
        claim_id=24,
        title="Promotable Evidence",
        stance="supports",
        quality=1.0,
        status="provisional",
    )
    test_agent = Agent(
        id=44,
        name="evidence-promoter",
        model_name="test-model",
        role="reviewer",
        reputation=1.0,
        api_key_hash=_hash_key(api_key),
    )
    db_session.add_all([test_page, test_claim, test_evidence, test_agent])
    db_session.flush()
    db_session.add(EvidenceVote(evidence_id=24, value=1, agent_id=44, weight=1.0))
    db_session.commit()

    response = client.post("/api/evidence/24/promote", headers={"X-API-Key": api_key})

    assert response.status_code == 200
    data = response.json()
    assert data["evidence_id"] == 24
    assert data["promoted"] is True
    assert data["status"] == "active"
    assert data["old_trust_level"] == "unverified"
    assert data["old_trust_score"] == 0.0
    assert data["trust_level"] == "accepted"
    assert data["trust_score"] > 0.3
    assert data["trust_score_delta"] == data["trust_score"] - data["old_trust_score"]
    db_session.refresh(test_evidence)
    db_session.refresh(test_claim)
    assert test_evidence.status == "active"
    assert test_claim.trust_level == "accepted"


def test_trust_history_surfaces_evidence_promotion_without_level_change(db_session):
    test_page = WikiPage(id=25, slug="promotion-history-page", title="Promotion History Page")
    test_claim = Claim(
        id=25,
        page_id=25,
        text="Promotion History Claim",
        trust_level="unverified",
        trust_score=0.12,
    )
    db_session.add_all([test_page, test_claim])
    db_session.flush()
    db_session.add(
        TrustAuditLog(
            claim_id=25,
            old_level="unverified",
            new_level="unverified",
            old_score=0.12,
            new_score=0.12,
            trigger="evidence_promoted",
            triggered_by_agent_id=44,
            created_at=dt.datetime(2026, 6, 25, 12, 0, 0),
        )
    )
    db_session.commit()

    history_client = TestClient(app, raise_server_exceptions=False)
    response = history_client.get("/api/claims/25/trust-history")

    assert response.status_code == 200
    data = response.json()
    assert data["events"]
    event = data["events"][0]
    assert event["kind"] == "evidence_promoted"
    assert event["color"] == "gold"
    assert event["summary"] == "Evidence promoted into trust"
    assert event["level_before"] == "unverified"
    assert event["level_after"] == "unverified"
    assert data["stats"]["events_returned"] == 1
    assert data["stats"]["noise_filtered"] == 0


def test_trust_history_events_include_structured_score_delta(db_session):
    test_page = WikiPage(id=26, slug="promotion-score-history-page", title="Promotion Score History Page")
    test_claim = Claim(
        id=26,
        page_id=26,
        text="Promotion Score History Claim",
        trust_level="accepted",
        trust_score=0.42,
    )
    db_session.add_all([test_page, test_claim])
    db_session.flush()
    db_session.add(
        TrustAuditLog(
            claim_id=26,
            old_level="unverified",
            new_level="accepted",
            old_score=0.10,
            new_score=0.42,
            trigger="evidence_promoted",
            triggered_by_agent_id=44,
            created_at=dt.datetime(2026, 6, 25, 12, 30, 0),
        )
    )
    db_session.commit()

    history_client = TestClient(app, raise_server_exceptions=False)
    response = history_client.get("/api/claims/26/trust-history")

    assert response.status_code == 200
    event = response.json()["events"][0]
    assert event["kind"] == "evidence_promoted"
    assert event["score_before"] == pytest.approx(0.10)
    assert event["score_after"] == pytest.approx(0.42)
    assert event["score_delta"] == pytest.approx(0.32)
    assert event["detail"] == "Score 0.100 → 0.420 (+0.320)"


def test_static_preview_sample_matches_debate_evidence_contract():
    assert set(STATIC_PREVIEW_SAMPLE.keys()) == {"580016"}
    assert_debate_evidence_contract(STATIC_PREVIEW_SAMPLE["580016"])
