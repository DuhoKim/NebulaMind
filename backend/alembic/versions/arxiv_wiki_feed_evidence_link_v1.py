"""Arxiv wiki feed v1 production evidence linkage columns.

Revision ID: arxiv_wiki_feed_evidence_link_v1
Revises: arxiv_wiki_feed_shadow_v1
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "arxiv_wiki_feed_evidence_link_v1"
down_revision = "arxiv_wiki_feed_shadow_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "evidence",
        sa.Column("arxiv_wiki_candidate_id", sa.Integer(), nullable=True),
    )
    op.add_column(
        "evidence",
        sa.Column("evidence_status", sa.Text(), nullable=False, server_default="production_active"),
    )
    op.add_column(
        "evidence",
        sa.Column("provenance", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    )
    op.create_foreign_key(
        "fk_evidence_arxiv_wiki_candidate",
        "evidence",
        "arxiv_wiki_evidence_candidates",
        ["arxiv_wiki_candidate_id"],
        ["id"],
    )
    op.create_index("idx_evidence_arxiv_wiki_candidate_id", "evidence", ["arxiv_wiki_candidate_id"])
    op.create_index("idx_evidence_evidence_status", "evidence", ["evidence_status"])


def downgrade():
    op.drop_index("idx_evidence_evidence_status", table_name="evidence")
    op.drop_index("idx_evidence_arxiv_wiki_candidate_id", table_name="evidence")
    op.drop_constraint("fk_evidence_arxiv_wiki_candidate", "evidence", type_="foreignkey")
    op.drop_column("evidence", "provenance")
    op.drop_column("evidence", "evidence_status")
    op.drop_column("evidence", "arxiv_wiki_candidate_id")
