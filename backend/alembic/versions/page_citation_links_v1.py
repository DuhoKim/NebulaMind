"""Page-level dynamic citation links.

Revision ID: page_citation_links_v1
Revises: j2v1
"""
from alembic import op
import sqlalchemy as sa


revision = "page_citation_links_v1"
down_revision = "j2v1"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "page_citation_links",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id", ondelete="CASCADE"), nullable=False),
        sa.Column("evidence_id", sa.Integer(), sa.ForeignKey("evidence.id", ondelete="CASCADE"), nullable=False),
        sa.Column("author_year_key", sa.String(120), nullable=False),
        sa.Column("match_method", sa.String(32), nullable=False),
        sa.Column("match_confidence", sa.Float(), nullable=False, server_default="1.0"),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.UniqueConstraint("page_id", "author_year_key", name="uq_page_citation_links_page_key"),
    )
    op.create_index("ix_page_citation_links_page", "page_citation_links", ["page_id"])
    op.create_index("ix_page_citation_links_evidence", "page_citation_links", ["evidence_id"])


def downgrade():
    op.drop_index("ix_page_citation_links_evidence", table_name="page_citation_links")
    op.drop_index("ix_page_citation_links_page", table_name="page_citation_links")
    op.drop_table("page_citation_links")
