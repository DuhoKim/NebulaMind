import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.agent_loop.citation_context import dynamic_miner
from app.agent_loop.citation_context.dynamic_miner import (
    DCCM_SOURCE_CHANNEL,
    DynamicSeed,
    build_seed_index,
    dynamic_quality,
    has_primary_support,
    load_dynamic_seeds,
    normalize_identifier,
    parse_dynamic_pico_response,
    process_dynamic_paper,
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


def _add_claim(db, claim_id=1, claim_type="established", locked=False):
    page = WikiPage(id=claim_id, slug=f"page-{claim_id}", title=f"Page {claim_id}")
    claim = Claim(
        id=claim_id,
        page_id=claim_id,
        text="Radiative cooling in dark matter halos allows gas condensation.",
        claim_type=claim_type,
        human_override_locked=locked,
    )
    db.add_all([page, claim])
    db.flush()
    return claim


def _add_seed(db, claim_id=1, source_channel="manual", quality=0.7, peer_reviewed=True):
    ev = Evidence(
        claim_id=claim_id,
        title="Seed cooling paper",
        year=2020,
        stance="supports",
        quality=quality,
        peer_reviewed=peer_reviewed,
        source_channel=source_channel,
        ads_bibcode="2020ApJ...1....1S",
        doi="10.1000/seed",
        abstract="Seed abstract.",
    )
    db.add(ev)
    db.flush()
    return ev


def test_dynamic_seed_eligibility_and_index():
    db = _session()
    try:
        _add_claim(db, claim_id=1)
        _add_seed(db, claim_id=1)
        _add_claim(db, claim_id=2, claim_type="debate")
        _add_seed(db, claim_id=2)
        _add_claim(db, claim_id=3, locked=True)
        _add_seed(db, claim_id=3)
        _add_claim(db, claim_id=4)
        _add_seed(db, claim_id=4, quality=0.49)
        db.commit()

        seeds = load_dynamic_seeds(db)
        assert [seed.claim_id for seed in seeds] == [1]
        index = build_seed_index(seeds)
        assert index["bibcode:2020ApJ...1....1S"][0].claim_id == 1
        assert index["doi:10.1000/seed"][0].evidence_id == seeds[0].evidence_id
    finally:
        db.close()


def test_identifier_normalization_and_classifier_quality():
    assert normalize_identifier("doi", "DOI:10.1000/ABC") == "doi:10.1000/abc"
    assert normalize_identifier("arxiv", "arXiv:2501.00001") == "arxiv:2501.00001"

    assert parse_dynamic_pico_response("###LABEL: SUPPORTIVE\n###CONFIDENCE: HIGH") == ("SUPPORTIVE", "HIGH")
    assert parse_dynamic_pico_response("") == ("HOLD", None)
    assert dynamic_quality("SUPPORTIVE", "HIGH") == 0.72
    assert dynamic_quality("SUPPORTIVE", "MEDIUM") == 0.60
    assert dynamic_quality("SUPPORTIVE", "LOW") is None


def test_primary_floor_blocks_transitive_only_seed(monkeypatch):
    db = _session()
    try:
        _add_claim(db, claim_id=1)
        _add_seed(db, claim_id=1, source_channel="citation_context_mining")
        db.commit()

        assert has_primary_support(db, 1) is False

        new_record = PaperRecord(
            title="New halo paper",
            abstract="Radiative cooling in dark matter halos is used.",
            year=2026,
            bibcode="2026ApJ...1....1N",
        )
        ref = PaperRecord(title="Seed cooling paper", year=2020, bibcode="2020ApJ...1....1S", doi="10.1000/seed")
        monkeypatch.setattr(dynamic_miner, "fetch_s2_reference_index", lambda _record: ({}, []))

        report = process_dynamic_paper(
            db,
            new_record,
            references=[ref],
            dry_run=True,
            classify_fn=lambda _ctx: ("SUPPORTIVE", "HIGH", "raw", 1),
        )

        assert report.primary_floor_blocked == 1
        assert report.inserted == 0
        assert report.decisions[0].action == "primary_floor_blocked"
    finally:
        db.close()


def test_lifetime_cap_blocks_dynamic_insert(monkeypatch):
    db = _session()
    try:
        _add_claim(db, claim_id=1)
        _add_seed(db, claim_id=1, source_channel="manual")
        for idx in range(6):
            db.add(
                Evidence(
                    claim_id=1,
                    title=f"DCCM {idx}",
                    stance="supports",
                    quality=0.6,
                    peer_reviewed=True,
                    source_channel=DCCM_SOURCE_CHANNEL,
                    ads_bibcode=f"2026ApJ...1...{idx:02d}D",
                )
            )
        db.commit()

        new_record = PaperRecord(
            title="New halo paper",
            abstract="Radiative cooling in dark matter halos is used.",
            year=2026,
            bibcode="2026ApJ...1....1N",
        )
        ref = PaperRecord(title="Seed cooling paper", year=2020, bibcode="2020ApJ...1....1S", doi="10.1000/seed")
        monkeypatch.setattr(dynamic_miner, "fetch_s2_reference_index", lambda _record: ({}, []))

        report = process_dynamic_paper(
            db,
            new_record,
            references=[ref],
            dry_run=True,
            classify_fn=lambda _ctx: ("SUPPORTIVE", "HIGH", "raw", 1),
        )

        assert report.capped == 1
        assert report.inserted == 0
        assert report.decisions[0].action == "lifetime_cap_blocked"
    finally:
        db.close()


def test_dynamic_dry_run_would_insert(monkeypatch):
    db = _session()
    try:
        _add_claim(db, claim_id=1)
        _add_seed(db, claim_id=1, source_channel="manual")
        db.commit()

        new_record = PaperRecord(
            title="New halo paper",
            abstract="Radiative cooling in dark matter halos is used.",
            year=2026,
            bibcode="2026ApJ...1....1N",
        )
        ref = PaperRecord(title="Seed cooling paper", year=2020, bibcode="2020ApJ...1....1S", doi="10.1000/seed")
        monkeypatch.setattr(
            dynamic_miner,
            "fetch_s2_reference_index",
            lambda _record: (
                {
                    "bibcode:2020ApJ...1....1S": [
                        {
                            "contexts": ["We build on radiative cooling in dark matter halos from the seed paper."],
                            "intents": ["background"],
                        }
                    ]
                },
                [],
            ),
        )

        report = process_dynamic_paper(
            db,
            new_record,
            references=[ref],
            dry_run=True,
            classify_fn=lambda _ctx: ("SUPPORTIVE", "MEDIUM", "raw", 1),
        )

        assert report.supportive == 1
        assert report.inserted == 0
        assert report.decisions[0].quality == 0.60
        assert report.decisions[0].action == "would_insert"
    finally:
        db.close()
