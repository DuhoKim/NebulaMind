import hashlib
from pathlib import Path
import sys

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.database import Base, get_db
from app.main import app
from app.models import (
    agent,
    arxiv,
    autowiki,
    benchmark,
    claim,
    claim_rewrite_lineage,
    comment,
    council,
    edit,
    evidence_element_link,
    external,
    facility,
    feedback,
    graph,
    jury,
    page,
    qa,
    reference,
    research_idea,
    social,
    spotlight,
    subscriber,
    survey,
    visitor,
    vote,
)
from app.models.agent import Agent
from app.models.comment import Comment
from app.models.edit import EditProposal
from app.models.page import WikiPage


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_pages_api_hardening.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
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


def _hash_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()


def _reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    db.add(WikiPage(id=57, slug="galaxy-evolution", title="Galaxy Evolution", content="old"))
    db.add(
        Agent(
            id=7,
            name="api-agent",
            model_name="test-model",
            role="editor",
            api_key_hash=_hash_key("valid-key"),
        )
    )
    db.commit()
    db.close()


def test_submit_proposal_requires_api_key_and_uses_authenticated_agent():
    _reset_db()

    missing = client.post(
        "/api/pages/galaxy-evolution/proposals",
        json={"agent_id": 999, "content": "new content", "summary": "test"},
    )
    assert missing.status_code == 422

    invalid = client.post(
        "/api/pages/galaxy-evolution/proposals",
        headers={"X-API-Key": "wrong"},
        json={"agent_id": 999, "content": "new content", "summary": "test"},
    )
    assert invalid.status_code == 401

    response = client.post(
        "/api/pages/galaxy-evolution/proposals",
        headers={"X-API-Key": "valid-key"},
        json={"agent_id": 999, "content": "new content", "summary": "test"},
    )
    assert response.status_code == 201
    payload = response.json()
    assert payload["agent_id"] == 7

    db = TestingSessionLocal()
    try:
        proposal = db.query(EditProposal).one()
        assert proposal.agent_id == 7
        assert proposal.content == "new content"
    finally:
        db.close()


def test_post_comment_requires_api_key_and_uses_authenticated_agent():
    _reset_db()

    missing = client.post(
        "/api/pages/galaxy-evolution/comments",
        json={"agent_id": 999, "body": "comment"},
    )
    assert missing.status_code == 422

    invalid = client.post(
        "/api/pages/galaxy-evolution/comments",
        headers={"X-API-Key": "wrong"},
        json={"agent_id": 999, "body": "comment"},
    )
    assert invalid.status_code == 401

    response = client.post(
        "/api/pages/galaxy-evolution/comments",
        headers={"X-API-Key": "valid-key"},
        json={"agent_id": 999, "body": "comment"},
    )
    assert response.status_code == 201
    payload = response.json()
    assert payload["agent_id"] == 7

    db = TestingSessionLocal()
    try:
        saved_comment = db.query(Comment).one()
        assert saved_comment.agent_id == 7
        assert saved_comment.body == "comment"
    finally:
        db.close()
