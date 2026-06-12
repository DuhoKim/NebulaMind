"""drop did_you_know, wiki_summary, wiki_summary_url from wiki_pages

Revision ID: drop_dyk_wiki_summary_v1
Revises: karpathy_v2_schema_v1
Create Date: 2026-05-20
"""
from alembic import op
import sqlalchemy as sa

revision = "drop_dyk_wiki_summary_v1"
down_revision = "karpathy_v2_schema_v1"
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_cols = {c["name"] for c in insp.get_columns("wiki_pages")}

    if "did_you_know" in existing_cols:
        op.drop_column("wiki_pages", "did_you_know")
    if "wiki_summary" in existing_cols:
        op.drop_column("wiki_pages", "wiki_summary")
    if "wiki_summary_url" in existing_cols:
        op.drop_column("wiki_pages", "wiki_summary_url")


def downgrade():
    op.add_column("wiki_pages", sa.Column("did_you_know", sa.Text(), nullable=True))
    op.add_column("wiki_pages", sa.Column("wiki_summary", sa.Text(), nullable=True))
    op.add_column("wiki_pages", sa.Column("wiki_summary_url", sa.Text(), nullable=True))
