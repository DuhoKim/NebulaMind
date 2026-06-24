import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.auth import _hash_key
from app.database import Base, get_db
from app.main import app
from app.models import (
    agent, arxiv, autowiki, benchmark, claim, claim_rewrite_lineage, comment,
    council, edit, evidence_element_link, external, facility, feedback, graph,
    jury, page, qa, reference, research_idea, social, spotlight, subscriber,
    survey, visitor, vote
)
from app.models.agent import Agent
from app.models.claim import Claim, Evidence, EvidenceVote, TrustAuditLog
from app.models.jury import JuryAssignment, JuryTask
from app.models.page import WikiPage


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_jury_trust_mutation.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


client = TestClient(app)


@pytest.fixture(autouse=True)
def override_db_dependency():
    previous = app.dependency_overrides.get(get_db)
    app.dependency_overrides[get_db] = override_get_db
    try:
        yield
    finally:
        if previous is None:
            app.dependency_overrides.pop(get_db, None)
        else:
            app.dependency_overrides[get_db] = previous


def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def seed_open_jury_task(db_session, *, api_key: str = "jury-agent-key") -> Agent:
    test_page = WikiPage(id=1, slug="jury-page", title="Jury Page")
    test_claim = Claim(id=1, page_id=1, text="Jury Claim", trust_level="unverified")
    test_evidence = Evidence(
        id=1,
        claim_id=1,
        title="Jury Evidence",
        stance="supports",
        quality=1.0,
    )
    test_task = JuryTask(
        id=1,
        evidence_id=1,
        claim_id=1,
        status="open",
        votes_received=0,
        votes_target=2,
    )
    test_agent = Agent(
        id=7,
        name="jury-agent",
        model_name="test-model",
        role="reviewer",
        reputation=0.75,
        api_key_hash=_hash_key(api_key),
    )
    test_assignment = JuryAssignment(task_id=1, agent_id=7, delivery_method="poll")
    db_session.add_all([test_page, test_claim, test_evidence, test_task, test_agent, test_assignment])
    db_session.commit()
    return test_agent


def test_jury_vote_uses_trust_mutation_service_and_ignores_body_agent_id():
    reset_db()
    api_key = "jury-agent-key"
    db_session = TestingSessionLocal()
    try:
        seed_open_jury_task(db_session, api_key=api_key)

        response = client.post(
            "/api/jury/tasks/1/vote",
            headers={"X-API-Key": api_key},
            json={"value": 1, "agent_id": 999, "reason": "service path"},
        )

        assert response.status_code == 200
        vote_id = response.json()["vote_id"]
        vote = db_session.query(EvidenceVote).one()
        assert vote.id == vote_id
        assert vote.evidence_id == 1
        assert vote.agent_id == 7
        assert vote.value == 1
        assert vote.weight == 0.75
        assert vote.voter_type == "agent"
        assert vote.reason == "service path"

        task = db_session.get(JuryTask, 1)
        assert task.votes_received == 1
        assert task.status == "open"
        assignment = db_session.query(JuryAssignment).filter_by(task_id=1, agent_id=7).one()
        assert assignment.responded_at is not None
        assert assignment.vote_id == vote_id

        claim = db_session.get(Claim, 1)
        assert claim.trust_score_updated_at is not None
        audit = db_session.query(TrustAuditLog).filter_by(claim_id=1).one()
        assert audit.trigger == "external_jury"
        assert audit.triggered_by_agent_id == 7
    finally:
        db_session.close()


def test_jury_vote_rejects_duplicate_without_incrementing_task():
    reset_db()
    api_key = "jury-agent-key"
    db_session = TestingSessionLocal()
    try:
        seed_open_jury_task(db_session, api_key=api_key)
        first = client.post(
            "/api/jury/tasks/1/vote",
            headers={"X-API-Key": api_key},
            json={"value": 1},
        )
        second = client.post(
            "/api/jury/tasks/1/vote",
            headers={"X-API-Key": api_key},
            json={"value": -1},
        )

        assert first.status_code == 200
        assert second.status_code == 409
        assert second.json()["detail"] == "Already voted on this evidence"
        assert db_session.query(EvidenceVote).filter_by(evidence_id=1, agent_id=7).count() == 1
        task = db_session.get(JuryTask, 1)
        assert task.votes_received == 1
    finally:
        db_session.close()


def test_jury_vote_rejects_invalid_value_before_mutation():
    reset_db()
    api_key = "jury-agent-key"
    db_session = TestingSessionLocal()
    try:
        seed_open_jury_task(db_session, api_key=api_key)

        response = client.post(
            "/api/jury/tasks/1/vote",
            headers={"X-API-Key": api_key},
            json={"value": 2},
        )

        assert response.status_code == 422
        assert response.json()["detail"] == "value must be -1, 0, or 1"
        assert db_session.query(EvidenceVote).count() == 0
        task = db_session.get(JuryTask, 1)
        assert task.votes_received == 0
        claim = db_session.get(Claim, 1)
        assert claim.trust_score_updated_at is None
        assert db_session.query(TrustAuditLog).count() == 0
    finally:
        db_session.close()
