"""doi_resolution_log: audit table for DOI backfill results

Revision ID: doi_resolution_log_v1
Revises: surveys_directory_v1
Create Date: 2026-05-18
"""
from alembic import op
import sqlalchemy as sa

revision = "doi_resolution_log_v1"
down_revision = "surveys_directory_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "doi_resolution_log",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("news_item_id", sa.Integer(), sa.ForeignKey("facility_news_items.id"), nullable=False, index=True),
        sa.Column("resolved_doi", sa.String(200), nullable=True),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("source_api", sa.String(20), nullable=False),
        sa.Column("title_similarity", sa.Float(), nullable=False),
        sa.Column("venue_match", sa.Boolean(), nullable=False),
        sa.Column("status", sa.String(20), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
    )


def downgrade():
    op.drop_table("doi_resolution_log")
