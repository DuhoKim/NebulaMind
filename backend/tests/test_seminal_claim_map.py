import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models.agent import Agent
from app.models.claim import Claim
from app.models.page import WikiPage
from app.models.seminal import SeminalClaimMap
from scripts.ccm_seed_seminal_map import resolve_mappings, strip_claim_markers


def test_seminal_claim_map_model_and_seed_resolution():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(
        engine,
        tables=[
            Agent.__table__,
            WikiPage.__table__,
            Claim.__table__,
            SeminalClaimMap.__table__,
        ],
    )
    Session = sessionmaker(bind=engine)
    db = Session()
    try:
        page = WikiPage(id=57, slug="galaxy-evolution", title="Galaxy Evolution")
        db.add(page)
        db.flush()
        claim = Claim(
            id=1632,
            page_id=page.id,
            section="Overview & Historical Foundations",
            text=(
                "The <!--claim:1579-->Planck Collaboration measured the primordial "
                "power spectrum with high precision."
            ),
        )
        db.add(claim)
        db.commit()

        meta = {"page_id": 57, "section": "Overview & Historical Foundations"}
        mappings = [
            {
                "claim_id": 1632,
                "text_guard": "measured the primordial power spectrum",
                "label": "Planck Collaboration 2020",
                "bibcode": "2020A&A...641A..10P",
                "doi": "10.1051/0004-6361/201833887",
                "arxiv_id": "1807.06211",
                "keyphrases": ["primordial power spectrum", "Planck"],
            }
        ]
        resolved, failures = resolve_mappings(db, meta, mappings, added_by="kun_audit")
        assert failures == []
        rows = [item.row for item in resolved]
        assert strip_claim_markers(claim.text) == (
            "The Planck Collaboration measured the primordial power spectrum with high precision."
        )
        assert rows == [
            {
                "claim_id": claim.id,
                "canonical_bibcode": "2020A&A...641A..10P",
                "canonical_label": "Planck Collaboration 2020",
                "canonical_doi": "10.1051/0004-6361/201833887",
                "canonical_arxiv_id": "1807.06211",
                "topic_keyphrases": '["primordial power spectrum", "Planck"]',
                "enabled": True,
                "added_by": "kun_audit",
                "notes": None,
            }
        ]

        db.add(SeminalClaimMap(**rows[0]))
        db.commit()
        mapped = db.scalar(select(SeminalClaimMap))
        assert mapped.claim_id == claim.id
        assert mapped.canonical_label == "Planck Collaboration 2020"
        assert mapped.enabled is True
    finally:
        db.close()
