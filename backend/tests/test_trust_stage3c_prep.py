import sys
import importlib.util
from pathlib import Path

import pytest
import sqlalchemy as sa
from alembic.migration import MigrationContext
from alembic.operations import Operations
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.auth import _hash_key
from app.database import Base
from app.models import (
    agent, arxiv, autowiki, benchmark, claim, claim_rewrite_lineage, comment,
    council, edit, evidence_element_link, external, facility, feedback, graph,
    jury, page, qa, reference, research_idea, social, spotlight, subscriber,
    survey, visitor, vote
)
from app.models.agent import Agent
from app.models.claim import Claim, Evidence, EvidenceVote, TrustAuditLog
from app.models.page import WikiPage
from app.services.trust_calculation import recalculate_trust_v2
from app.services.trust_mutation import TrustMutationError, TrustMutationService
from scripts.evidence_vote_dedupe_report import build_dedupe_report


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_trust_stage3c_prep.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


@pytest.fixture
def db_session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def seed_claim(db_session, *, claim_id: int = 1) -> Claim:
    test_page = WikiPage(id=claim_id, slug=f"stage3c-{claim_id}", title="Stage 3C")
    test_claim = Claim(id=claim_id, page_id=claim_id, text="Stage 3C Claim", trust_level="unverified")
    db_session.add_all([test_page, test_claim])
    db_session.flush()
    return test_claim


def test_evidence_status_defaults_active(db_session):
    seed_claim(db_session)
    evidence = Evidence(id=1, claim_id=1, title="Default Active Evidence")
    db_session.add(evidence)
    db_session.flush()

    assert evidence.status == "active"


def test_provisional_evidence_and_votes_are_excluded_from_trust(db_session):
    claim = seed_claim(db_session)
    provisional = Evidence(
        id=1,
        claim_id=claim.id,
        title="Provisional Evidence",
        stance="supports",
        quality=1.0,
        status="provisional",
    )
    db_session.add(provisional)
    db_session.flush()
    db_session.add(EvidenceVote(evidence_id=provisional.id, value=1, agent_id=77, weight=1.0))

    new_level, score = recalculate_trust_v2(claim.id, db_session, trigger="stage3c_test")

    assert new_level == "unverified"
    assert score == 0.0
    assert claim.trust_level == "unverified"
    assert claim.trust_score == 0.0


def test_trust_mutation_update_mode_keeps_single_vote_row(db_session):
    seed_claim(db_session)
    evidence = Evidence(id=1, claim_id=1, title="Active Evidence", status="active")
    agent_row = Agent(
        id=7,
        name="stage3c-agent",
        model_name="test-model",
        role="reviewer",
        reputation=0.75,
        api_key_hash=_hash_key("stage3c-key"),
    )
    db_session.add_all([evidence, agent_row])
    db_session.flush()

    first = TrustMutationService.create_or_update_evidence_vote(
        db_session,
        evidence_id=evidence.id,
        actor_agent=agent_row,
        value=1,
        reason="first",
        trigger="stage3c_test",
        duplicate_mode="reject",
        recalculate=False,
    )
    with pytest.raises(TrustMutationError) as exc:
        TrustMutationService.create_or_update_evidence_vote(
            db_session,
            evidence_id=evidence.id,
            actor_agent=agent_row,
            value=-1,
            reason="reject duplicate",
            trigger="stage3c_test",
            duplicate_mode="reject",
            recalculate=False,
        )
    updated = TrustMutationService.create_or_update_evidence_vote(
        db_session,
        evidence_id=evidence.id,
        actor_agent=agent_row,
        value=-1,
        reason="updated",
        trigger="stage3c_test",
        duplicate_mode="update",
        recalculate=False,
    )

    assert exc.value.status_code == 409
    assert first.vote.id == updated.vote.id
    assert updated.created is False
    assert db_session.query(EvidenceVote).filter_by(evidence_id=1, agent_id=7).count() == 1
    vote_row = db_session.query(EvidenceVote).filter_by(evidence_id=1, agent_id=7).one()
    assert vote_row.value == -1
    assert vote_row.reason == "updated"


def test_promote_provisional_evidence_activates_and_recalculates_trust(db_session):
    claim = seed_claim(db_session)
    evidence = Evidence(
        id=1,
        claim_id=claim.id,
        title="Promotable Evidence",
        stance="supports",
        quality=1.0,
        status="provisional",
    )
    agent_row = Agent(
        id=7,
        name="promotion-agent",
        model_name="test-model",
        role="reviewer",
        reputation=1.0,
        api_key_hash=_hash_key("promotion-key"),
    )
    db_session.add_all([evidence, agent_row])
    db_session.flush()
    db_session.add(EvidenceVote(evidence_id=evidence.id, value=1, agent_id=agent_row.id, weight=1.0))

    before_level, before_score = recalculate_trust_v2(claim.id, db_session, trigger="stage3c_test")
    result = TrustMutationService.promote_evidence(
        db_session,
        evidence_id=evidence.id,
        actor_agent=agent_row,
        trigger="evidence_promoted",
    )

    assert before_level == "unverified"
    assert before_score == 0.0
    assert result.promoted is True
    assert result.evidence.id == evidence.id
    assert result.old_level == "unverified"
    assert result.old_score == before_score
    assert result.new_level == "accepted"
    assert result.new_score > 0.3
    assert result.score_delta == result.new_score - result.old_score
    assert evidence.status == "active"
    assert claim.trust_level == "accepted"
    audit = db_session.query(TrustAuditLog).filter_by(trigger="evidence_promoted").one()
    assert audit.claim_id == claim.id
    assert audit.triggered_by_agent_id == agent_row.id


def test_stage3c_migration_defers_evidence_vote_unique_constraint():
    source = (Path(__file__).resolve().parents[1] / "alembic/versions/trust_stage3c_evidence_status.py").read_text()

    assert "sa.Column(\"status\"" in source
    assert "ck_evidence_status" in source
    assert "idx_evidence_status" in source
    assert "deferred" in source
    assert "create_unique_constraint" not in source


def test_stage3c_migration_upgrade_downgrade_idempotent_on_sqlite(monkeypatch):
    migration_path = Path(__file__).resolve().parents[1] / "alembic/versions/trust_stage3c_evidence_status.py"
    spec = importlib.util.spec_from_file_location("trust_stage3c_evidence_status_test", migration_path)
    migration = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(migration)

    local_engine = create_engine("sqlite:///:memory:")
    with local_engine.begin() as conn:
        conn.execute(sa.text("CREATE TABLE evidence (id INTEGER PRIMARY KEY)"))
        conn.execute(sa.text("INSERT INTO evidence (id) VALUES (1)"))
        context = MigrationContext.configure(conn)
        monkeypatch.setattr(migration, "op", Operations(context))

        migration.upgrade()
        migration.upgrade()

        columns = {column["name"] for column in sa.inspect(conn).get_columns("evidence")}
        indexes = {index["name"] for index in sa.inspect(conn).get_indexes("evidence")}
        status = conn.execute(sa.text("SELECT status FROM evidence WHERE id = 1")).scalar_one()
        assert "status" in columns
        assert "idx_evidence_status" in indexes
        assert status == "active"

        migration.downgrade()
        migration.downgrade()

        columns = {column["name"] for column in sa.inspect(conn).get_columns("evidence")}
        indexes = {index["name"] for index in sa.inspect(conn).get_indexes("evidence")}
        assert "status" not in columns
        assert "idx_evidence_status" not in indexes


def test_evidence_vote_model_declares_unique_evidence_agent_constraint():
    constraints = {
        constraint.name: tuple(column.name for column in constraint.columns)
        for constraint in getattr(EvidenceVote.__table__, "constraints")
        if isinstance(constraint, sa.UniqueConstraint)
    }

    assert constraints["uq_evidence_votes_evidence_agent"] == ("evidence_id", "agent_id")


def test_evidence_vote_uniqueness_migration_dedupes_and_enforces_sqlite(monkeypatch):
    migration_path = Path(__file__).resolve().parents[1] / "alembic/versions/evidence_vote_uniqueness_v1.py"
    spec = importlib.util.spec_from_file_location("evidence_vote_uniqueness_v1_test", migration_path)
    assert spec is not None
    migration = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(migration)

    local_engine = create_engine("sqlite:///:memory:")
    with local_engine.begin() as conn:
        conn.execute(sa.text("""
            CREATE TABLE evidence_votes (
                id INTEGER PRIMARY KEY,
                evidence_id INTEGER NOT NULL,
                agent_id INTEGER NULL,
                value INTEGER NOT NULL,
                created_at TIMESTAMP NULL
            )
        """))
        conn.execute(sa.text("""
            INSERT INTO evidence_votes (id, evidence_id, agent_id, value, created_at) VALUES
            (1, 10, 7, 1, '2026-01-01 12:00:00'),
            (2, 10, 7, -1, '2026-01-02 12:00:00'),
            (3, 10, 7, 1, '2026-01-02 12:00:00'),
            (10, 10, NULL, 1, '2026-01-03 12:00:00'),
            (11, 10, NULL, -1, '2026-01-04 12:00:00')
        """))
        context = MigrationContext.configure(conn)
        monkeypatch.setattr(migration, "op", Operations(context))

        migration.upgrade()
        migration.upgrade()

        rows = conn.execute(sa.text("""
            SELECT id, evidence_id, agent_id
            FROM evidence_votes
            ORDER BY id
        """)).mappings().all()
        assert [dict(row) for row in rows] == [
            {"id": 3, "evidence_id": 10, "agent_id": 7},
            {"id": 10, "evidence_id": 10, "agent_id": None},
            {"id": 11, "evidence_id": 10, "agent_id": None},
        ]
        indexes = {index["name"] for index in sa.inspect(conn).get_indexes("evidence_votes")}
        assert "uq_evidence_votes_evidence_agent" in indexes
        with pytest.raises(IntegrityError):
            conn.execute(sa.text("""
                INSERT INTO evidence_votes (id, evidence_id, agent_id, value, created_at)
                VALUES (12, 10, 7, 1, '2026-01-05 12:00:00')
            """))
        conn.execute(sa.text("""
            INSERT INTO evidence_votes (id, evidence_id, agent_id, value, created_at)
            VALUES (13, 10, NULL, 1, '2026-01-05 12:00:00')
        """))

        migration.downgrade()
        migration.downgrade()
        indexes = {index["name"] for index in sa.inspect(conn).get_indexes("evidence_votes")}
        assert "uq_evidence_votes_evidence_agent" not in indexes
        conn.execute(sa.text("""
            INSERT INTO evidence_votes (id, evidence_id, agent_id, value, created_at)
            VALUES (14, 10, 7, 1, '2026-01-06 12:00:00')
        """))


def test_dedupe_report_keeps_newest_vote_and_ignores_null_agents():
    local_engine = create_engine("sqlite:///:memory:")
    with local_engine.begin() as conn:
        conn.execute(sa.text("""
            CREATE TABLE evidence_votes (
                id INTEGER PRIMARY KEY,
                evidence_id INTEGER NOT NULL,
                agent_id INTEGER NULL,
                value INTEGER NOT NULL,
                created_at TIMESTAMP NULL
            )
        """))
        conn.execute(sa.text("""
            INSERT INTO evidence_votes (id, evidence_id, agent_id, value, created_at) VALUES
            (1, 1, 7, 1, '2026-01-01 12:00:00'),
            (2, 1, 7, -1, '2026-01-02 12:00:00'),
            (3, 1, 7, 1, '2026-01-02 12:00:00'),
            (10, 1, NULL, 1, '2026-01-03 12:00:00'),
            (11, 1, NULL, -1, '2026-01-04 12:00:00')
        """))

        report = build_dedupe_report(conn, limit=10)

    assert report["destructive_action"] is False
    assert report["duplicate_pairs"] == 1
    assert report["extra_rows"] == 2
    assert report["sample"] == [{
        "evidence_id": 1,
        "agent_id": 7,
        "keep_id": 3,
        "row_count": 3,
        "extra_rows": 2,
        "vote_ids": [3, 2, 1],
    }]
