"""Astronomy news curator v2 — add general-news columns to facility_news_items

Revision ID: astro_news_curator_v2
Revises: news_social_drafts_v1
"""
from alembic import op
import sqlalchemy as sa

revision = "astro_news_curator_v2"
down_revision = "news_social_drafts_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("facility_news_items", sa.Column("source_publication", sa.String(80), nullable=True))
    op.add_column("facility_news_items", sa.Column("source_tier", sa.String(1), nullable=True))
    op.add_column("facility_news_items", sa.Column("paper_arxiv_id", sa.String(40), nullable=True))
    op.add_column("facility_news_items", sa.Column("paper_doi", sa.String(200), nullable=True))
    op.add_column("facility_news_items", sa.Column("paper_venue", sa.String(80), nullable=True))
    op.add_column("facility_news_items", sa.Column("is_press_release", sa.Boolean(), nullable=True))
    op.add_column("facility_news_items", sa.Column("advance_type", sa.String(40), nullable=True))
    op.add_column("facility_news_items", sa.Column("popsci_flags", sa.Text(), nullable=True))
    op.add_column("facility_news_items", sa.Column("topic_tags", sa.Text(), nullable=True))
    op.create_index(
        "idx_fni_paper_arxiv_id",
        "facility_news_items",
        ["paper_arxiv_id"],
        postgresql_where=sa.text("paper_arxiv_id IS NOT NULL"),
    )
    op.create_index(
        "idx_fni_source_publication",
        "facility_news_items",
        ["source_publication"],
        postgresql_where=sa.text("source_publication IS NOT NULL"),
    )


def downgrade():
    op.drop_index("idx_fni_source_publication", "facility_news_items")
    op.drop_index("idx_fni_paper_arxiv_id", "facility_news_items")
    op.drop_column("facility_news_items", "topic_tags")
    op.drop_column("facility_news_items", "popsci_flags")
    op.drop_column("facility_news_items", "advance_type")
    op.drop_column("facility_news_items", "is_press_release")
    op.drop_column("facility_news_items", "paper_venue")
    op.drop_column("facility_news_items", "paper_doi")
    op.drop_column("facility_news_items", "paper_arxiv_id")
    op.drop_column("facility_news_items", "source_tier")
    op.drop_column("facility_news_items", "source_publication")
