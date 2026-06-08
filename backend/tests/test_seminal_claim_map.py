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
from scripts.seed_seminal_claims import build_rows


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
        page = WikiPage(slug="galaxy-formation", title="Galaxy Formation")
        db.add(page)
        db.flush()
        claim = Claim(
            page_id=page.id,
            text="Gas can cool radiatively inside dark matter halos and condense into galaxies.",
        )
        db.add(claim)
        db.commit()

        entries = [
            {
                "label": "White & Rees 1978",
                "bibcode": "1978MNRAS.183..341W",
                "doi": "10.1093/mnras/183.3.341",
                "match_claims": [{"page_slug": "galaxy-formation", "text_contains": "cool radiatively"}],
                "keyphrases": ["radiative cooling", "dark matter halo"],
            }
        ]
        rows = build_rows(db, entries, added_by="kun_audit", allow_ambiguous=False, validate_ads=False)
        assert rows == [
            {
                "claim_id": claim.id,
                "canonical_bibcode": "1978MNRAS.183..341W",
                "canonical_label": "White & Rees 1978",
                "canonical_doi": "10.1093/mnras/183.3.341",
                "canonical_arxiv_id": None,
                "topic_keyphrases": '["radiative cooling", "dark matter halo"]',
                "enabled": True,
                "added_by": "kun_audit",
                "notes": None,
            }
        ]

        db.add(SeminalClaimMap(**rows[0]))
        db.commit()
        mapped = db.scalar(select(SeminalClaimMap))
        assert mapped.claim_id == claim.id
        assert mapped.canonical_label == "White & Rees 1978"
        assert mapped.enabled is True
    finally:
        db.close()
