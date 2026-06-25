"""evidence_vote_uniqueness_v1: dedupe and enforce one vote per agent/evidence

Revision ID: evidence_vote_uniqueness_v1
Revises: trust_stage3c_evidence_status
Create Date: 2026-06-25

Before adding the unique guard, existing duplicate non-null
(evidence_id, agent_id) rows are collapsed by keeping the newest row per pair:
created_at DESC NULLS LAST, then id DESC. Rows with agent_id NULL are ignored
by the dedupe policy and remain allowed by SQL unique semantics.

This migration is destructive for duplicate non-null vote rows. Run
backend/scripts/evidence_vote_dedupe_report.py before applying to production.
"""
from alembic import op
import sqlalchemy as sa


revision = "evidence_vote_uniqueness_v1"
down_revision = "trust_stage3c_evidence_status"
branch_labels = None
depends_on = None

INDEX_NAME = "uq_evidence_votes_evidence_agent"
TABLE_NAME = "evidence_votes"


def _index_exists(conn, name: str) -> bool:
    return name in {idx["name"] for idx in sa.inspect(conn).get_indexes(TABLE_NAME)}


def upgrade() -> None:
    conn = op.get_bind()

    # Keep the newest row for each non-null (evidence_id, agent_id) pair.
    # The CASE expression is portable across SQLite/PostgreSQL and gives
    # created_at DESC NULLS LAST semantics without relying on dialect syntax.
    op.execute(sa.text("""
        WITH ranked AS (
            SELECT
                id,
                ROW_NUMBER() OVER (
                    PARTITION BY evidence_id, agent_id
                    ORDER BY
                        CASE WHEN created_at IS NULL THEN 0 ELSE 1 END DESC,
                        created_at DESC,
                        id DESC
                ) AS rn
            FROM evidence_votes
            WHERE agent_id IS NOT NULL
        )
        DELETE FROM evidence_votes
        WHERE id IN (SELECT id FROM ranked WHERE rn > 1)
    """))

    if not _index_exists(conn, INDEX_NAME):
        op.create_index(
            INDEX_NAME,
            TABLE_NAME,
            ["evidence_id", "agent_id"],
            unique=True,
        )


def downgrade() -> None:
    conn = op.get_bind()
    if _index_exists(conn, INDEX_NAME):
        op.drop_index(INDEX_NAME, table_name=TABLE_NAME)
