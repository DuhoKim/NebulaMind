import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.agent_loop.citation_context import miner
from app.agent_loop.citation_context.miner import (
    CitationContext,
    PicoVerdict,
    build_contexts_for_mapping,
    keyphrase_hits,
    parse_pico_response,
    run_ccm_cycle,
)
from app.database import Base
from app.models.agent import Agent
from app.models.claim import Claim, Evidence, EvidenceVote, TrustAuditLog
from app.models.jury import JuryScorecard, PromptRevision
from app.models.page import WikiPage
from app.models.seminal import SeminalClaimMap
from app.services.paper_search import PaperRecord


def _session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(
        engine,
        tables=[
            Agent.__table__,
            WikiPage.__table__,
            Claim.__table__,
            Evidence.__table__,
            EvidenceVote.__table__,
            TrustAuditLog.__table__,
            PromptRevision.__table__,
            JuryScorecard.__table__,
            SeminalClaimMap.__table__,
        ],
    )
    return sessionmaker(bind=engine)()


def _seed_mapping(db):
    page = WikiPage(id=57, slug="galaxy-evolution", title="Galaxy Evolution")
    claim = Claim(
        id=1631,
        page_id=57,
        section="Overview & Historical Foundations",
        text="White and Rees established that gas cools radiatively inside dark matter halos.",
    )
    mapping = SeminalClaimMap(
        id=1,
        claim_id=1631,
        canonical_bibcode="1978MNRAS.183..341W",
        canonical_label="White & Rees 1978",
        canonical_doi="10.1093/mnras/183.3.341",
        topic_keyphrases='["radiative cooling", "dark matter halo"]',
    )
    db.add_all([page, claim, mapping])
    db.commit()
    return mapping


def test_parse_pico_response_and_quality():
    verdict = parse_pico_response("notes\n###LABEL: SUPPORTIVE\n###CONFIDENCE: HIGH")
    assert verdict.label == "SUPPORTIVE"
    assert verdict.confidence == "HIGH"
    assert verdict.quality == 0.80

    assert parse_pico_response("").label == "HOLD"
    assert parse_pico_response("###LABEL: SUPPORTIVE\n###CONFIDENCE: LOW").quality is None
    assert parse_pico_response("###LABEL: OFFTOPIC\n###CONFIDENCE: HIGH").quality is None


def test_keyphrase_hits():
    assert keyphrase_hits(["radiative cooling", "blue cloud"], "The radiative cooling model applies.") == 1
    assert keyphrase_hits(["red sequence"], "The context is unrelated.") == 0


def test_build_contexts_prefers_s2_then_abstract(monkeypatch):
    db = _session()
    try:
        mapping = _seed_mapping(db)
        records = [
            PaperRecord(
                title="Modern halo paper",
                abstract="Abstract mentions dark matter halo only.",
                authors=["A"],
                year=2025,
                arxiv_id="2501.00001",
                doi="10.1000/a",
                bibcode="2025ApJ...1....1A",
            ),
            PaperRecord(
                title="Modern fallback paper",
                abstract="This abstract uses radiative cooling in a dark matter halo.",
                authors=["B"],
                year=2025,
                arxiv_id="2501.00002",
                doi="10.1000/b",
                bibcode="2025ApJ...1....2B",
            ),
        ]

        monkeypatch.setattr(miner, "ads_citing_papers", lambda *args, **kwargs: records)
        monkeypatch.setattr(
            miner,
            "fetch_s2_context_index",
            lambda _mapping: {
                "10.1000/a": [
                    {
                        "contexts": ["Following White & Rees, radiative cooling in a dark matter halo is assumed."],
                        "intents": ["background"],
                    }
                ]
            },
        )

        contexts, ads_seen = build_contexts_for_mapping(
            db,
            mapping,
            min_year=2024,
            ads_rows=10,
            max_candidates=10,
            arxiv_intro_budget=[0],
        )

        assert ads_seen == 2
        assert [ctx.context_source for ctx in contexts] == ["s2_context", "abstract"]
        assert contexts[0].s2_intent == "background"
    finally:
        db.close()


def test_run_ccm_cycle_dry_run(monkeypatch):
    db = _session()
    try:
        _seed_mapping(db)
        record = PaperRecord(
            title="Modern halo paper",
            abstract="This abstract uses radiative cooling in a dark matter halo.",
            authors=["A"],
            year=2025,
            arxiv_id="2501.00001",
            doi="10.1000/a",
            bibcode="2025ApJ...1....1A",
        )
        monkeypatch.setattr(miner, "ads_citing_papers", lambda *args, **kwargs: [record])
        monkeypatch.setattr(miner, "fetch_s2_context_index", lambda _mapping: {})

        def fake_classify(ctx: CitationContext):
            return PicoVerdict(label="SUPPORTIVE", confidence="MEDIUM", raw="ok", latency_ms=5)

        report = run_ccm_cycle(
            db,
            dry_run=True,
            max_maps=1,
            ads_rows=1,
            classify_fn=fake_classify,
        )

        assert report.supportive == 1
        assert report.inserted == 0
        assert db.query(Evidence).count() == 0
        assert report.decisions[0].action == "would_insert"
    finally:
        db.close()
