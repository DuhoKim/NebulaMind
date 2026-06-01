import sys
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
from app.models.claim import Claim, Evidence
from app.models.evidence_element_link import EvidenceElementLink
from app.models.page import WikiPage


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
    assert len(data["evidence"]) == 1
    evidence_data = data["evidence"][0]
    assert "element_links" in evidence_data
    assert len(evidence_data["element_links"]) == 1
    link_data = evidence_data["element_links"][0]
    assert link_data["element_id"] == "test-element-1"
    assert link_data["element_text_snapshot"] == "This is a test element."
    assert "total_elements" in data
    assert data["total_elements"] == 1
