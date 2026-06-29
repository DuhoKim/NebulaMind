import json
from pathlib import Path
import sys

from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
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
from app.models.page import FactSource, PageCitationLink, WikiPage


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_page_source_surface_fallbacks.db"
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
        page_row = WikiPage(
            id=58,
            slug="galaxy-evolution-v2",
            title="Galaxy Evolution (Intro-Synthesis V2 Pilot)",
            content=(
                "<!--claim:5801-->Morphology correlates with black-hole mass.<!--/claim:5801-->\n"
                "<!--claim:5802-->Satellite quenching tracks environment.<!--/claim:5802-->"
            ),
            hero_facts="",
        )
        db.add(page_row)
        db.add_all([
            Claim(
                id=5801,
                page_id=58,
                section="Morphology",
                order_idx=1,
                text="Morphology correlates with black-hole mass.",
                trust_level="debated",
            ),
            Claim(
                id=5802,
                page_id=58,
                section="Environment",
                order_idx=2,
                text="Satellite quenching tracks environment.",
                trust_level="accepted",
            ),
        ])
        db.add_all([
            Evidence(
                id=8801,
                claim_id=5801,
                arxiv_id="2604.03503",
                doi=None,
                url="",
                title="The morphologies of present-day galaxies in the COLIBRE simulations",
                authors='["Nushkia Chamba", "Ivan K. Baldry"]',
                year=2026,
                summary="COLIBRE exact-span source.",
                stance="neutral",
                quality=0.91,
                status="active",
            ),
            Evidence(
                id=8802,
                claim_id=5802,
                arxiv_id="2605.03008v1",
                doi=None,
                url=None,
                title="Environmental Quenching of High-Redshift Galaxies",
                authors="Aleyna Döven; Mohammadreza Ayromlou; Cristiano Porciani",
                year=2026,
                summary="Environmental quenching source.",
                stance="supporting",
                quality=0.83,
                status="active",
            ),
        ])
        db.commit()
    finally:
        db.close()


def _with_override(fn):
    previous = app.dependency_overrides.get(get_db)
    app.dependency_overrides[get_db] = override_get_db
    try:
        return fn()
    finally:
        if previous is None:
            app.dependency_overrides.pop(get_db, None)
        else:
            app.dependency_overrides[get_db] = previous


def test_citations_fall_back_to_page_claim_evidence_without_writing_links():
    def run():
        _reset_db()
        response = client.get("/api/pages/galaxy-evolution-v2/citations")
        assert response.status_code == 200, response.text
        payload = response.json()

        db = TestingSessionLocal()
        try:
            link_count = db.execute(text("SELECT count(*) FROM page_citation_links")).scalar()
        finally:
            db.close()
        assert link_count == 0
        return payload

    payload = _with_override(run)
    citations = payload["citations"]
    assert [row["evidence_id"] for row in citations] == [8801, 8802]
    assert citations[0]["seq"] == 1
    assert citations[0]["author_year_key"] == "Chamba2026"
    assert citations[0]["url"] == "https://arxiv.org/abs/2604.03503"
    assert citations[0]["authors"] == ["Nushkia Chamba", "Ivan K. Baldry"]
    assert citations[1]["author_year_key"] == "Döven2026"


def test_source_surfaces_normalize_prefixed_arxiv_abs_urls_without_writing():
    def run():
        _reset_db()
        db = TestingSessionLocal()
        try:
            db.add(Claim(
                id=5803,
                page_id=58,
                section="Legacy URL",
                order_idx=3,
                text="Legacy arXiv URLs should render cleanly.",
                trust_level="accepted",
            ))
            db.add(Evidence(
                id=8803,
                claim_id=5803,
                arxiv_id="1712.04452",
                doi=None,
                url="https://arxiv.org/abs/arXiv:1712.04452",
                title="Legacy prefixed arXiv URL",
                authors='["Jane Doe"]',
                year=2017,
                summary="Legacy URL exact-span source.",
                stance="supporting",
                quality=0.77,
                status="active",
            ))
            db.commit()
        finally:
            db.close()

        citations_response = client.get("/api/pages/galaxy-evolution-v2/citations")
        fact_sources_response = client.get("/api/pages/galaxy-evolution-v2/fact-sources")
        assert citations_response.status_code == 200, citations_response.text
        assert fact_sources_response.status_code == 200, fact_sources_response.text

        db = TestingSessionLocal()
        try:
            link_count = db.execute(text("SELECT count(*) FROM page_citation_links")).scalar()
            fact_source_count = db.execute(text("SELECT count(*) FROM fact_sources")).scalar()
        finally:
            db.close()
        assert link_count == 0
        assert fact_source_count == 0
        return citations_response.json(), fact_sources_response.json()

    citations_payload, fact_sources_payload = _with_override(run)
    citation = next(row for row in citations_payload["citations"] if row["evidence_id"] == 8803)
    assert citation["url"] == "https://arxiv.org/abs/1712.04452"
    fact_source = next(row for row in fact_sources_payload if row["claim_id"] == 5803)
    assert fact_source["reference_url"] == "https://arxiv.org/abs/1712.04452"
    assert fact_source["representative_arxiv_id"] == "1712.04452"


def test_citations_keep_materialized_links_when_available():
    def run():
        _reset_db()
        db = TestingSessionLocal()
        try:
            db.add(PageCitationLink(
                page_id=58,
                evidence_id=8802,
                author_year_key="Materialized 2026",
                match_method="exact_key",
                match_confidence=1.0,
            ))
            db.commit()
        finally:
            db.close()
        response = client.get("/api/pages/galaxy-evolution-v2/citations")
        assert response.status_code == 200, response.text
        return response.json()

    payload = _with_override(run)
    assert [row["evidence_id"] for row in payload["citations"]] == [8802]
    assert payload["citations"][0]["author_year_key"] == "Materialized 2026"


def test_fact_sources_fall_back_to_claim_evidence_when_fact_source_table_is_empty():
    def run():
        _reset_db()
        response = client.get("/api/pages/galaxy-evolution-v2/fact-sources")
        assert response.status_code == 200, response.text
        payload = response.json()

        db = TestingSessionLocal()
        try:
            fact_source_count = db.execute(text("SELECT count(*) FROM fact_sources")).scalar()
        finally:
            db.close()
        assert fact_source_count == 0
        return payload

    payload = _with_override(run)
    assert [row["fact_kind"] for row in payload] == ["claim", "claim"]
    assert [row["claim_id"] for row in payload] == [5801, 5802]
    assert payload[0]["source_tier"] == "claim"
    assert payload[0]["trust_level_snapshot"] == "debated"
    assert payload[0]["evidence_count_snapshot"] == 1
    assert payload[0]["representative_arxiv_id"] == "2604.03503"
    assert payload[0]["reference_url"] == "https://arxiv.org/abs/2604.03503"
    assert payload[0]["source_surface"] == "claim_evidence_fallback"
    assert "no fact_sources row written" in payload[0]["attribution"]


def test_fact_sources_keep_inline_hero_sources_before_claim_evidence_fallback():
    def run():
        _reset_db()
        db = TestingSessionLocal()
        try:
            page_row = db.query(WikiPage).filter(WikiPage.id == 58).one()
            page_row.hero_facts = json.dumps([
                {
                    "label": "Sample size",
                    "value": "34 papers",
                    "source": {
                        "tier": "indexed_page_claims",
                        "authority": "NebulaMind claim index",
                        "reference_url": "https://nebulamind.net/wiki/galaxy-evolution-v2",
                        "reference_title": "Galaxy Evolution V2 page claims",
                        "retrieval_year": 2026,
                        "claim_id": 5801,
                        "trust_level": "debated",
                        "evidence_count": 2,
                        "representative_arxiv_id": "2604.03503",
                        "attribution": "Inline page fact source",
                        "reason": "Hero fact source should take precedence over claim fallback.",
                    },
                }
            ])
            db.commit()
        finally:
            db.close()

        response = client.get("/api/pages/galaxy-evolution-v2/fact-sources")
        assert response.status_code == 200, response.text
        payload = response.json()

        db = TestingSessionLocal()
        try:
            fact_source_count = db.execute(text("SELECT count(*) FROM fact_sources")).scalar()
        finally:
            db.close()
        assert fact_source_count == 0
        return payload

    payload = _with_override(run)
    assert len(payload) == 1
    assert payload[0]["fact_kind"] == "hero"
    assert payload[0]["source_tier"] == "indexed_page_claims"
    assert payload[0]["authority"] == "NebulaMind claim index"
    assert payload[0]["claim_id"] == 5801
    assert payload[0]["trust_level_snapshot"] == "debated"
    assert payload[0]["evidence_count_snapshot"] == 2
    assert payload[0]["representative_arxiv_id"] == "2604.03503"
    assert payload[0]["source_surface"] == "inline_hero_fact_source"


def test_fact_sources_keep_materialized_rows_when_available():
    def run():
        _reset_db()
        db = TestingSessionLocal()
        try:
            db.add(FactSource(
                page_id=58,
                fact_kind="hero",
                fact_index=0,
                source_tier="authoritative",
                authority="Fixture Authority",
                reference_url="https://example.org/source",
                reference_title="Fixture source",
                retrieval_year=2026,
                claim_id=None,
                trust_level_snapshot=None,
                evidence_count_snapshot=None,
                representative_arxiv_id=None,
                attribution="Fixture authority",
                flagged=False,
                reason=None,
            ))
            db.commit()
        finally:
            db.close()
        response = client.get("/api/pages/galaxy-evolution-v2/fact-sources")
        assert response.status_code == 200, response.text
        return response.json()

    payload = _with_override(run)
    assert len(payload) == 1
    assert payload[0]["fact_kind"] == "hero"
    assert payload[0]["source_tier"] == "authoritative"
    assert payload[0]["source_surface"] == "fact_sources_table"
