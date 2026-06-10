"""Content quarantine for wiki stored-content contract violations.

Revision ID: 20260611_content_quarantine_v1
Revises: page_citation_links_v1
"""
from alembic import op
import sqlalchemy as sa


revision = "20260611_content_quarantine_v1"
down_revision = "page_citation_links_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "content_quarantine",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id"), nullable=True),
        sa.Column("source_tag", sa.String(120), nullable=False, server_default="wiki_page_content_set"),
        sa.Column("violations", sa.Text(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("resolved_at", sa.TIMESTAMP(), nullable=True),
    )
    op.create_index("ix_content_quarantine_page_id", "content_quarantine", ["page_id"])


def downgrade():
    op.drop_index("ix_content_quarantine_page_id", table_name="content_quarantine")
    op.drop_table("content_quarantine")
