import pytest
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models import agent, claim, jury  # noqa: F401 - registers FK target tables for metadata
from app.models.page import PageVersion, WikiPage
from app.models.sentence_trust import SentenceTrust, SentenceVote
from app.services.sentence_trust import recalculate_sentence_trust
from app.services.trust_mutation import TrustMutationService


@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def seed_page_version(db_session, *, page_version_id: int = 100) -> PageVersion:
    page = WikiPage(id=58, slug="galaxy-evolution-v2", title="Galaxy Evolution", content="Seed")
    version = PageVersion(
        id=page_version_id,
        page_id=page.id,
        version_num=3,
        content="Sentence zero. Sentence one.",
    )
    db_session.add_all([page, version])
    db_session.flush()
    return version


def add_sentence_vote(
    db_session,
    version: PageVersion,
    *,
    sentence_index: int,
    arxiv_id: str,
    value: int,
    sentence_hash: str = "hash-branch",
) -> None:
    db_session.add(SentenceVote(
        page_version_id=version.id,
        sentence_index=sentence_index,
        sentence_hash=sentence_hash,
        arxiv_id=arxiv_id,
        value=value,
        stance_confidence=0.9,
        tone_tier="accepted" if value > 0 else "debated",
        voter_type="atom-astronomy-7b",
    ))


def test_sentence_vote_model_declares_one_paper_per_sentence_guard():
    constraints = {
        constraint.name: tuple(column.name for column in constraint.columns)
        for constraint in SentenceVote.__table__.constraints
        if isinstance(constraint, sa.UniqueConstraint)
    }

    assert constraints["uq_sentence_votes_page_sentence_paper"] == (
        "page_version_id",
        "sentence_index",
        "sentence_hash",
        "arxiv_id",
    )


def test_sentence_models_match_committed_migration_types():
    assert isinstance(SentenceVote.__table__.c.value.type, sa.SmallInteger)
    assert isinstance(SentenceTrust.__table__.c.tone_tier.type, sa.Text)
    assert isinstance(SentenceTrust.__table__.c.trust_level.type, sa.Text)
    assert isinstance(SentenceTrust.__table__.c.trust_score.type, sa.Double)


def test_sentence_vote_unique_guard_rejects_duplicate_paper_stake(db_session):
    version = seed_page_version(db_session)
    vote_kwargs = {
        "page_version_id": version.id,
        "sentence_index": 0,
        "sentence_hash": "hash-0",
        "arxiv_id": "2401.00001",
        "value": 1,
        "stance_confidence": 0.91,
        "tone_tier": "accepted",
        "voter_type": "atom-astronomy-7b",
    }
    db_session.add(SentenceVote(**vote_kwargs))
    db_session.flush()

    db_session.add(SentenceVote(**vote_kwargs))
    with pytest.raises(IntegrityError):
        db_session.flush()


def test_recalculate_sentence_trust_with_no_votes_is_unverified_mixed(db_session):
    version = seed_page_version(db_session)

    row = recalculate_sentence_trust(
        db_session,
        page_version_id=version.id,
        sentence_index=7,
        sentence_hash="hash-7",
    )

    assert row.vote_count == 0
    assert row.settled_votes == 0
    assert row.contested_votes == 0
    assert row.settled_share == 0.0
    assert row.trust_score == 0.0
    assert row.trust_level == "unverified"
    assert row.tone_tier == "mixed"
    assert row.single_source is False
    assert row.contested_veto is False


def test_recalculate_sentence_trust_rolls_votes_into_sentence_trust(db_session):
    version = seed_page_version(db_session)
    db_session.add_all([
        SentenceVote(
            page_version_id=version.id,
            sentence_index=4,
            sentence_hash="hash-4",
            arxiv_id="2401.00001",
            value=1,
            stance_confidence=0.94,
            tone_tier="accepted",
            voter_type="atom-astronomy-7b",
        ),
        SentenceVote(
            page_version_id=version.id,
            sentence_index=4,
            sentence_hash="hash-4",
            arxiv_id="2401.00002",
            value=1,
            stance_confidence=0.88,
            tone_tier="accepted",
            voter_type="atom-astronomy-7b",
        ),
        SentenceVote(
            page_version_id=version.id,
            sentence_index=4,
            sentence_hash="hash-4",
            arxiv_id="2401.00003",
            value=-1,
            stance_confidence=0.82,
            tone_tier="debated",
            voter_type="atom-astronomy-7b",
        ),
    ])
    db_session.flush()

    row = recalculate_sentence_trust(
        db_session,
        page_version_id=version.id,
        sentence_index=4,
        sentence_hash="hash-4",
    )

    assert row.vote_count == 3
    assert row.settled_votes == 2
    assert row.contested_votes == 1
    assert row.settled_share == pytest.approx(2 / 3)
    assert row.trust_score == pytest.approx(0.45 * (1 / 3), abs=0.001)
    assert row.trust_level == "debated"
    assert row.tone_tier == "mixed"
    assert row.single_source is False
    assert row.contested_veto is False
    assert db_session.query(SentenceTrust).filter_by(
        page_version_id=version.id,
        sentence_index=4,
    ).one().id == row.id


def test_recalculate_sentence_trust_caps_single_source_as_unverified(db_session):
    version = seed_page_version(db_session)
    db_session.add(SentenceVote(
        page_version_id=version.id,
        sentence_index=2,
        sentence_hash="hash-2",
        arxiv_id="2401.00001",
        value=1,
        stance_confidence=0.94,
        tone_tier="accepted",
        voter_type="atom-astronomy-7b",
    ))
    db_session.flush()

    row = recalculate_sentence_trust(
        db_session,
        page_version_id=version.id,
        sentence_index=2,
        sentence_hash="hash-2",
    )

    assert row.vote_count == 1
    assert row.settled_votes == 1
    assert row.contested_votes == 0
    assert row.settled_share == 1.0
    assert row.trust_score == pytest.approx(0.45, abs=0.001)
    assert row.trust_level == "unverified"
    assert row.single_source is True


def test_sentence_trust_level_branches_cover_consensus_debated_and_challenged(db_session):
    version = seed_page_version(db_session)
    for i in range(3):
        add_sentence_vote(
            db_session,
            version,
            sentence_index=10,
            sentence_hash="hash-consensus",
            arxiv_id=f"2401.1000{i}",
            value=1,
        )
    for i, value in enumerate([1, 1, 1, -1, -1]):
        add_sentence_vote(
            db_session,
            version,
            sentence_index=11,
            sentence_hash="hash-veto",
            arxiv_id=f"2401.1100{i}",
            value=value,
        )
    for i, value in enumerate([1, -1, -1]):
        add_sentence_vote(
            db_session,
            version,
            sentence_index=12,
            sentence_hash="hash-challenged",
            arxiv_id=f"2401.1200{i}",
            value=value,
        )
    db_session.flush()

    consensus = recalculate_sentence_trust(
        db_session,
        page_version_id=version.id,
        sentence_index=10,
        sentence_hash="hash-consensus",
    )
    debated = recalculate_sentence_trust(
        db_session,
        page_version_id=version.id,
        sentence_index=11,
        sentence_hash="hash-veto",
    )
    challenged = recalculate_sentence_trust(
        db_session,
        page_version_id=version.id,
        sentence_index=12,
        sentence_hash="hash-challenged",
    )

    assert consensus.trust_level == "consensus"
    assert consensus.contested_veto is False
    assert debated.trust_level == "debated"
    assert debated.contested_veto is True
    assert challenged.trust_level == "challenged"
    assert challenged.contested_veto is True


def test_recalculate_sentence_trust_updates_existing_row_in_place(db_session):
    version = seed_page_version(db_session)
    add_sentence_vote(db_session, version, sentence_index=13, arxiv_id="2401.13001", value=1)
    add_sentence_vote(db_session, version, sentence_index=13, arxiv_id="2401.13002", value=1)
    db_session.flush()

    first = recalculate_sentence_trust(
        db_session,
        page_version_id=version.id,
        sentence_index=13,
        sentence_hash="hash-branch",
    )
    first_id = first.id
    add_sentence_vote(db_session, version, sentence_index=13, arxiv_id="2401.13003", value=-1)
    db_session.flush()

    second = recalculate_sentence_trust(
        db_session,
        page_version_id=version.id,
        sentence_index=13,
        sentence_hash="hash-branch",
    )

    assert second.id == first_id
    assert second.vote_count == 3
    assert second.settled_votes == 2
    assert second.contested_votes == 1
    assert second.tone_distribution == {"settled": 2, "contested": 1}
    assert db_session.query(SentenceTrust).filter_by(
        page_version_id=version.id,
        sentence_index=13,
    ).count() == 1


def test_trust_mutation_service_exposes_sentence_recalculation_seam(db_session):
    version = seed_page_version(db_session)
    db_session.add_all([
        SentenceVote(
            page_version_id=version.id,
            sentence_index=5,
            sentence_hash="hash-5",
            arxiv_id="2401.00001",
            value=1,
            stance_confidence=0.93,
            tone_tier="accepted",
            voter_type="atom-astronomy-7b",
        ),
        SentenceVote(
            page_version_id=version.id,
            sentence_index=5,
            sentence_hash="hash-5",
            arxiv_id="2401.00002",
            value=1,
            stance_confidence=0.87,
            tone_tier="accepted",
            voter_type="atom-astronomy-7b",
        ),
    ])
    db_session.flush()

    row = TrustMutationService.recalculate_sentence_trust(
        db_session,
        page_version_id=version.id,
        sentence_index=5,
        sentence_hash="hash-5",
    )

    assert row.trust_level == "accepted"
    assert row.settled_votes == 2
    assert row.contested_votes == 0
