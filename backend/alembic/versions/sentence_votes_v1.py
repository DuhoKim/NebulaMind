"""sentence_votes_v1: per-sentence paper vote ledger

Revision ID: sentence_votes_v1
Revises: intro_synthesis_v2_ab_fold
Create Date: 2026-06-22
"""
from alembic import op
import sqlalchemy as sa


revision = "sentence_votes_v1"
down_revision = "intro_synthesis_v2_ab_fold"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "sentence_votes",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("page_version_id", sa.Integer(), sa.ForeignKey("page_versions.id", ondelete="CASCADE"), nullable=False),
        sa.Column("sentence_index", sa.Integer(), nullable=False),
        sa.Column("sentence_hash", sa.Text(), nullable=False),
        sa.Column("arxiv_id", sa.String(length=30), nullable=False),
        sa.Column("value", sa.SmallInteger(), nullable=False),
        sa.Column("stance_confidence", sa.Float(), nullable=False),
        sa.Column("tone_tier", sa.String(length=20), nullable=False),
        sa.Column("voter_type", sa.String(length=80), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("value IN (-1, 1)", name="ck_sentence_votes_value"),
        sa.UniqueConstraint(
            "page_version_id",
            "sentence_index",
            "sentence_hash",
            "arxiv_id",
            name="uq_sentence_votes_page_sentence_paper",
        ),
    )
    op.create_index("ix_sentence_votes_page_sentence", "sentence_votes", ["page_version_id", "sentence_index"])
    op.create_index("ix_sentence_votes_sentence_hash", "sentence_votes", ["sentence_hash"])
    op.create_index("ix_sentence_votes_arxiv_id", "sentence_votes", ["arxiv_id"])


def downgrade() -> None:
    op.drop_index("ix_sentence_votes_arxiv_id", table_name="sentence_votes")
    op.drop_index("ix_sentence_votes_sentence_hash", table_name="sentence_votes")
    op.drop_index("ix_sentence_votes_page_sentence", table_name="sentence_votes")
    op.drop_table("sentence_votes")
