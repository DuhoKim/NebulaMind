"""News social post drafts table

Revision ID: news_social_drafts_v1
Revises: security_p2_week2_ban_v1
"""
from alembic import op
import sqlalchemy as sa

revision = "news_social_drafts_v1"
down_revision = "security_p2_week2_ban_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "social_post_drafts",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("news_item_id", sa.Integer(), sa.ForeignKey("facility_news_items.id"), nullable=False),
        sa.Column("platform", sa.String(30), nullable=False),
        sa.Column("draft_text", sa.Text(), nullable=False),
        sa.Column("status", sa.String(20), nullable=False, server_default="draft"),
        sa.Column("created_at", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=False),
    )
    op.create_index("ix_social_post_drafts_news_item_id", "social_post_drafts", ["news_item_id"])
    op.create_index("ix_social_post_drafts_status", "social_post_drafts", ["status"])


def downgrade():
    op.drop_table("social_post_drafts")
