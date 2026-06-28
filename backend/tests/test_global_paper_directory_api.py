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
from app.models.claim import Claim, Evidence
from app.models.page import WikiPage

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_global_paper_directory.db"
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
        page_a = WikiPage(id=801, slug="early-galaxies", title="Early Galaxies", content="")
        page_b = WikiPage(id=802, slug="dust-obscured-galaxies", title="Dust-obscured Galaxies", content="")
        page_c = WikiPage(id=803, slug="stellar-halos", title="Stellar Halos", content="")
        db.add_all([page_a, page_b, page_c])
        claim_a = Claim(id=8101, page_id=801, section="Assembly", order_idx=1, text="Massive galaxies assembled early.", trust_level="debated")
        claim_b = Claim(id=8102, page_id=802, section="Dust", order_idx=1, text="Dust obscuration changes counts.", trust_level="challenged")
        claim_c = Claim(id=8103, page_id=803, section="Halos", order_idx=1, text="Minor mergers build halos.", trust_level="accepted")
        db.add_all([claim_a, claim_b, claim_c])
        db.add_all([
            Evidence(id=9101, claim_id=8101, arxiv_id="2606.990101", title="Cross-page directory fixture", authors="A. Lens; B. Halo", year=2026, url="https://example.org/directory", summary="Shared paper linked to multiple wiki claims.", stance="supporting", status="active"),
            Evidence(id=9102, claim_id=8102, arxiv_id="2606.990101", title="Cross-page directory fixture", authors="A. Lens; B. Halo", year=2026, url="https://example.org/directory", summary="Shared paper linked to multiple wiki claims.", stance="contradicting", status="active"),
            Evidence(id=9103, claim_id=8103, arxiv_id="2606.123456", title="Synthesis-ready halo catalog", authors="C. Stream", year=2025, url="https://example.org/halo", summary="A supporting catalog paper.", stance="supporting", status="active"),
        ])
        db.commit()
    finally:
        db.close()


def _with_test_db(fn):
    previous = app.dependency_overrides.get(get_db)
    app.dependency_overrides[get_db] = override_get_db
    try:
        _reset_db()
        return fn()
    finally:
        if previous is None:
            app.dependency_overrides.pop(get_db, None)
        else:
            app.dependency_overrides[get_db] = previous


def test_global_paper_directory_groups_papers_and_prioritizes_counter_pressure():
    def run():
        before = TestingSessionLocal().query(Evidence).count()
        response = client.get("/api/pages/paper-directory")
        after = TestingSessionLocal().query(Evidence).count()
        return before, response, after

    before, response, after = _with_test_db(run)
    assert response.status_code == 200, response.text
    assert before == after, "Directory search must be read-only."
    payload = response.json()
    assert payload["schema_version"] == "global_paper_directory.v1"
    assert payload["query"] == ""
    assert payload["total_papers"] == 2
    assert payload["result_count"] == 2
    assert "not a final verdict" in payload["scope"]["caveat"]

    first = payload["items"][0]
    assert first["paper"]["arxiv_id"] == "2606.990101"
    assert first["paper"]["author_year_key"] == "Lens2026"
    assert first["page_count"] == 2
    assert first["claim_count"] == 2
    assert first["evidence_count"] == 2
    assert first["tone_counts"] == {"support": 1, "counter": 1, "neutral": 0}
    assert first["triage_status"] == "needs_adjudication"
    assert [page["slug"] for page in first["pages"]] == ["dust-obscured-galaxies", "early-galaxies"]
    assert first["pages"][0]["counter_count"] == 1


def test_global_paper_directory_search_and_limit_are_disclosed():
    def run():
        return client.get("/api/pages/paper-directory", params={"q": "halo", "limit": 1})

    response = _with_test_db(run)
    assert response.status_code == 200, response.text
    payload = response.json()
    assert payload["query"] == "halo"
    assert payload["limit"] == 1
    assert payload["total_papers"] == 2
    assert payload["result_count"] == 1
    assert payload["items"][0]["paper"]["arxiv_id"] == "2606.990101"
    assert payload["items"][0]["pages"][0]["href"] == "/wiki/dust-obscured-galaxies"


def test_global_paper_directory_empty_search_returns_empty_deck_not_404():
    def run():
        return client.get("/api/pages/paper-directory", params={"q": "missing-paper"})

    response = _with_test_db(run)
    assert response.status_code == 200, response.text
    payload = response.json()
    assert payload["schema_version"] == "global_paper_directory.v1"
    assert payload["query"] == "missing-paper"
    assert payload["total_papers"] == 0
    assert payload["items"] == []
