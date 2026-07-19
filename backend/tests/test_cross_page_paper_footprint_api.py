from pathlib import Path
import sys

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
from app.models.claim import Claim, Evidence, EvidenceVote
from app.models.page import WikiPage

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_cross_page_paper_footprint.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


client = TestClient(app, raise_server_exceptions=False)


def _reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        page_a = WikiPage(id=701, slug="early-galaxies", title="Early Galaxies", content="")
        page_b = WikiPage(id=702, slug="dust-obscured-galaxies", title="Dust-obscured Galaxies", content="")
        db.add_all([page_a, page_b])
        claim_a = Claim(id=7101, page_id=701, section="Assembly", order_idx=1, text="Massive galaxies assembled early.", trust_level="debated")
        claim_b = Claim(id=7102, page_id=701, section="Assembly", order_idx=2, text="Minor mergers add stellar halos.", trust_level="accepted")
        claim_c = Claim(id=7201, page_id=702, section="Dust", order_idx=1, text="Dust obscuration changes inferred high-redshift counts.", trust_level="challenged")
        db.add_all([claim_a, claim_b, claim_c])
        db.add_all([
            Evidence(id=8101, claim_id=7101, arxiv_id="2606.990101", title="Cross-page footprint fixture", authors="A. Lens; B. Halo", year=2026, url="https://example.org/footprint", summary="Shared paper linked to multiple wiki claims.", stance="supporting", status="active"),
            Evidence(id=8102, claim_id=7102, arxiv_id="2606.990101", title="Cross-page footprint fixture", authors="A. Lens; B. Halo", year=2026, url="https://example.org/footprint", summary="Shared paper linked to multiple wiki claims.", stance="supporting", status="active"),
            Evidence(id=8103, claim_id=7201, arxiv_id="2606.990101", title="Cross-page footprint fixture", authors="A. Lens; B. Halo", year=2026, url="https://example.org/footprint", summary="Shared paper linked to multiple wiki claims.", stance="contradicting", status="active"),
            Evidence(id=8104, claim_id=7201, arxiv_id="2606.999999", title="Different paper", stance="supporting", status="active"),
        ])
        db.add_all([
            EvidenceVote(id=9001, evidence_id=8101, value=1, agent_id=1),
            EvidenceVote(id=9002, evidence_id=8103, value=-1, agent_id=2),
            EvidenceVote(id=9003, evidence_id=8103, value=-1, agent_id=None),
        ])
        db.commit()
    finally:
        db.close()


def test_cross_page_paper_footprint_groups_claims_pages_and_votes_by_arxiv():
    previous = app.dependency_overrides.get(get_db)
    app.dependency_overrides[get_db] = override_get_db
    try:
        _reset_db()
        response = client.get("/api/pages/paper-footprint", params={"arxiv_id": "2606.990101"})
        assert response.status_code == 200, response.text
        payload = response.json()
    finally:
        if previous is None:
            app.dependency_overrides.pop(get_db, None)
        else:
            app.dependency_overrides[get_db] = previous

    assert payload["schema_version"] == "cross_page_paper_footprint.v1"
    assert payload["paper"]["arxiv_id"] == "2606.990101"
    assert payload["paper"]["title"] == "Cross-page footprint fixture"
    assert payload["page_count"] == 2
    assert payload["claim_count"] == 3
    assert payload["evidence_count"] == 3
    assert payload["tone_counts"] == {"support": 2, "counter": 1, "neutral": 0}
    assert payload["trust_counts"] == {"accepted": 1, "challenged": 1, "debated": 1}
    assert payload["scope"]["label"] == "wiki-wide paper footprint"
    assert "not a final verdict" in payload["scope"]["caveat"]

    assert [page["slug"] for page in payload["pages"]] == ["dust-obscured-galaxies", "early-galaxies"]
    first_page = payload["pages"][0]
    assert first_page["counter_count"] == 1
    assert first_page["claim_count"] == 1
    assert first_page["claims"][0]["claim_id"] == 7201
    assert first_page["claims"][0]["tone"] == "counter"
    assert first_page["claims"][0]["href"] == "/wiki/dust-obscured-galaxies#claim-7201"
    assert first_page["claims"][0]["votes_disagree"] == 2


def test_cross_page_paper_footprint_reports_404_for_unknown_paper_without_writes():
    previous = app.dependency_overrides.get(get_db)
    app.dependency_overrides[get_db] = override_get_db
    try:
        _reset_db()
        response = client.get("/api/pages/paper-footprint", params={"arxiv_id": "2606.missing"})
    finally:
        if previous is None:
            app.dependency_overrides.pop(get_db, None)
        else:
            app.dependency_overrides[get_db] = previous

    assert response.status_code == 404
    assert response.json()["detail"] == "Paper footprint not found"
