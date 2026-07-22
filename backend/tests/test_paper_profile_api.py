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

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_paper_profile.db"
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
        page_a = WikiPage(id=901, slug="early-galaxies", title="Early Galaxies", content="")
        page_b = WikiPage(id=902, slug="dust-obscured-galaxies", title="Dust-obscured Galaxies", content="")
        page_c = WikiPage(id=903, slug="source-gaps", title="Source Gaps", content="")
        db.add_all([page_a, page_b, page_c])
        claim_a = Claim(id=9101, page_id=901, section="Assembly", order_idx=1, text="Massive galaxies assembled early.", trust_level="debated")
        claim_b = Claim(id=9102, page_id=902, section="Dust", order_idx=1, text="Dust obscuration changes counts.", trust_level="challenged")
        claim_c = Claim(id=9103, page_id=903, section="Sources", order_idx=1, text="This paper still needs source reconciliation.", trust_level="unverified")
        db.add_all([claim_a, claim_b, claim_c])
        db.add_all([
            Evidence(id=9201, claim_id=9101, arxiv_id="2606.990101", title="Paper profile fixture", authors="A. Lens; B. Halo", year=2026, url="https://example.org/profile", summary="Shared profile paper linked to multiple wiki claims.", stance="supporting", status="active"),
            Evidence(id=9202, claim_id=9102, arxiv_id="2606.990101", title="Paper profile fixture", authors="A. Lens; B. Halo", year=2026, url="https://example.org/profile", summary="Shared profile paper linked to multiple wiki claims.", stance="contradicting", status="active"),
            Evidence(id=9203, claim_id=9103, arxiv_id=None, doi=None, url=None, title="Unstable source gap", authors="", year=None, summary="No stable identifier.", stance="neutral", status="draft"),
        ])
        db.add_all([
            EvidenceVote(id=9301, evidence_id=9202, agent_id=1, value=-1, reason="fixture counter pressure"),
            EvidenceVote(id=9302, evidence_id=9201, agent_id=1, value=1, reason="fixture support"),
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


def test_paper_profile_groups_full_footprint_without_writes():
    def run():
        before = TestingSessionLocal().query(Evidence).count()
        response = client.get("/api/pages/paper-profile", params={"paper_id": "arxiv:2606.990101"})
        after = TestingSessionLocal().query(Evidence).count()
        return before, response, after

    before, response, after = _with_test_db(run)
    assert response.status_code == 200, response.text
    assert before == after, "Paper profile must be read-only."
    payload = response.json()
    assert payload["schema_version"] == "paper_profile.v1"
    assert payload["paper_id"] == "arxiv:2606.990101"
    assert payload["paper"]["arxiv_id"] == "2606.990101"
    assert payload["paper"]["author_year_key"] == "Lens2026"
    assert payload["triage_status"] == "needs_adjudication"
    assert payload["profile_summary"] == "2 pages · 2 claims · 1 countering"
    assert payload["page_count"] == 2
    assert payload["claim_count"] == 2
    assert payload["evidence_count"] == 2
    assert payload["tone_counts"] == {"support": 1, "counter": 1, "neutral": 0}
    assert payload["vote_counts"] == {"agree": 1, "disagree": 1}
    assert payload["source_gap_count"] == 0
    assert "not a final verdict" in payload["scope"]["caveat"]
    assert [page["slug"] for page in payload["pages"]] == ["dust-obscured-galaxies", "early-galaxies"]
    assert payload["pages"][0]["claims"][0]["tone"] == "counter"
    assert payload["pages"][0]["claims"][0]["href"] == "/wiki/dust-obscured-galaxies#claim-9102"
    assert payload["pages_truncated"] is False


def test_paper_profile_supports_evidence_key_and_source_gap_status():
    def run():
        return client.get("/api/pages/paper-profile", params={"paper_id": "evidence:9203"})

    response = _with_test_db(run)
    assert response.status_code == 200, response.text
    payload = response.json()
    assert payload["paper_id"] == "evidence:9203"
    assert payload["triage_status"] == "needs_source"
    assert payload["source_gap_count"] == 1
    assert payload["pages"][0]["claims"][0]["trust_level"] == "unverified"


def test_paper_profile_requires_known_paper_id():
    def run():
        missing = client.get("/api/pages/paper-profile")
        unknown = client.get("/api/pages/paper-profile", params={"paper_id": "arxiv:missing"})
        return missing, unknown

    missing, unknown = _with_test_db(run)
    assert missing.status_code == 400
    assert unknown.status_code == 404
