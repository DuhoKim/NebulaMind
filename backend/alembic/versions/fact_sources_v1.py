"""Fact sources table

Revision ID: fact_sources_v1
Revises: oac_v2
Create Date: 2026-05-05
"""
from alembic import op
import sqlalchemy as sa

revision = "fact_sources_v1"
down_revision = "oac_v2"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "fact_sources",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id"), nullable=False),
        sa.Column("fact_kind", sa.String(20), nullable=False),      # 'hero' | 'did_you_know'
        sa.Column("fact_index", sa.Integer(), nullable=False),
        sa.Column("source_tier", sa.String(20), nullable=False),    # 'authoritative' | 'claim' | 'ai_estimate'
        sa.Column("authority", sa.String(40), nullable=True),
        sa.Column("reference_url", sa.Text(), nullable=True),
        sa.Column("reference_title", sa.Text(), nullable=True),
        sa.Column("retrieval_year", sa.Integer(), nullable=True),
        sa.Column("claim_id", sa.Integer(), sa.ForeignKey("claims.id"), nullable=True),
        sa.Column("trust_level_snapshot", sa.String(20), nullable=True),
        sa.Column("evidence_count_snapshot", sa.Integer(), nullable=True),
        sa.Column("representative_arxiv_id", sa.String(30), nullable=True),
        sa.Column("generator", sa.String(30), nullable=True),
        sa.Column("flagged", sa.Boolean(), nullable=False, server_default="false"),
        sa.Column("reason", sa.Text(), nullable=True),
        sa.Column("attribution", sa.Text(), nullable=False),
        sa.Column("cited_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("created_by_agent_id", sa.Integer(), nullable=True),
        sa.Column("superseded_at", sa.TIMESTAMP(), nullable=True),
    )
    op.create_index(
        "idx_fact_sources_page_kind_idx",
        "fact_sources",
        ["page_id", "fact_kind", "fact_index"],
    )
    op.create_index(
        "idx_fact_sources_claim",
        "fact_sources",
        ["claim_id"],
        postgresql_where=sa.text("claim_id IS NOT NULL"),
    )
    op.create_index("idx_fact_sources_tier", "fact_sources", ["source_tier"])


def downgrade():
    op.drop_index("idx_fact_sources_tier", table_name="fact_sources")
    op.drop_index("idx_fact_sources_claim", table_name="fact_sources")
    op.drop_index("idx_fact_sources_page_kind_idx", table_name="fact_sources")
    op.drop_table("fact_sources")
