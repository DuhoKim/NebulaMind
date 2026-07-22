import sys
from pathlib import Path

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.database import Base
from app.models import (
    agent, arxiv, autowiki, benchmark, claim, claim_rewrite_lineage, comment,
    council, edit, evidence_element_link, external, facility, feedback, graph,
    jury, page, qa, reference, research_idea, social, spotlight, subscriber,
    survey, visitor, vote
)
from app.models.claim import Claim, Evidence, TrustAuditLog
from app.models.page import WikiPage
from app.services.trust_calculation import recalculate_trust_v2


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_trust_debate_stance_caps.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def db_session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def seed_claim_with_supports(
    db_session,
    *,
    claim_id: int,
    debate_stance: str,
    trust_level: str = "reported",
    human_override: str | None = None,
    human_locked: bool = False,
) -> Claim:
    page_row = WikiPage(id=claim_id, slug=f"trust-cap-{claim_id}", title="Trust Cap")
    claim_row = Claim(
        id=claim_id,
        page_id=claim_id,
        text=f"Trust cap claim {claim_id}",
        claim_type="established",
        debate_stance=debate_stance,
        trust_level=trust_level,
        trust_score=0.2 if trust_level == "reported" else 0.45,
        human_trust_override=human_override,
        human_override_locked=human_locked,
    )
    db_session.add_all([page_row, claim_row])
    for idx in range(1, 7):
        db_session.add(Evidence(
            id=claim_id * 100 + idx,
            claim_id=claim_id,
            title=f"Support evidence {idx}",
            stance="supports",
            quality=1.0,
            year=2026,
            status="active",
        ))
    db_session.flush()
    return claim_row


def test_mixed_debated_support_only_claim_is_capped_at_debated(db_session):
    claim = seed_claim_with_supports(
        db_session,
        claim_id=1,
        debate_stance="mixed_debated",
        trust_level="debated",
    )

    new_level, score = recalculate_trust_v2(claim.id, db_session, trigger="status_cap_test")
    db_session.flush()

    assert score >= 0.3
    assert new_level == "debated"
    assert claim.trust_level == "debated"
    audit = db_session.query(TrustAuditLog).filter_by(trigger="status_cap_test").one()
    assert audit.new_level == "debated"
    assert audit.notes == "debate_stance:mixed_debated capped accepted->debated"


def test_model_bounded_support_only_claim_is_capped_at_reported(db_session):
    claim = seed_claim_with_supports(
        db_session,
        claim_id=2,
        debate_stance="model_bounded",
        trust_level="reported",
    )

    new_level, score = recalculate_trust_v2(claim.id, db_session, trigger="status_cap_test")
    db_session.flush()

    assert score >= 0.3
    assert new_level == "reported"
    assert claim.trust_level == "reported"
    audit = db_session.query(TrustAuditLog).filter_by(trigger="status_cap_test").one()
    assert audit.new_level == "reported"
    assert audit.notes == "debate_stance:model_bounded capped accepted->reported"


def test_reported_scoped_claim_can_still_be_accepted(db_session):
    claim = seed_claim_with_supports(
        db_session,
        claim_id=3,
        debate_stance="reported_scoped",
        trust_level="reported",
    )

    new_level, score = recalculate_trust_v2(claim.id, db_session, trigger="status_cap_test")
    db_session.flush()

    assert score >= 0.3
    assert new_level == "accepted"
    assert claim.trust_level == "accepted"
    audit = db_session.query(TrustAuditLog).filter_by(trigger="status_cap_test").one()
    assert audit.new_level == "accepted"
    assert audit.notes is None


def test_locked_human_override_wins_over_debate_stance_cap(db_session):
    claim = seed_claim_with_supports(
        db_session,
        claim_id=4,
        debate_stance="mixed_debated",
        trust_level="debated",
        human_override="accepted",
        human_locked=True,
    )

    new_level, score = recalculate_trust_v2(claim.id, db_session, trigger="status_cap_test")
    db_session.flush()

    assert score >= 0.3
    assert new_level == "accepted"
    assert claim.trust_level == "accepted"
    audit = db_session.query(TrustAuditLog).filter_by(trigger="status_cap_test").one()
    assert audit.new_level == "accepted"
    assert audit.notes is None
