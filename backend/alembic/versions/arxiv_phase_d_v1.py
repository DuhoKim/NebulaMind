"""arXiv Phase D: verify_retry_at for ADS-lag retry path

Revision ID: arxiv_phase_d_v1
Revises: surveys_directory_v1
Create Date: 2026-05-20
"""
from alembic import op
import sqlalchemy as sa

revision = "arxiv_phase_d_v1"
down_revision = "drop_dyk_wiki_summary_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "arxiv_papers",
        sa.Column("verify_retry_at", sa.DateTime(), nullable=True),
    )
    op.create_index(
        "ix_arxiv_papers_verify_retry_at",
        "arxiv_papers",
        ["verify_retry_at"],
    )


def downgrade():
    op.drop_index("ix_arxiv_papers_verify_retry_at", table_name="arxiv_papers")
    op.drop_column("arxiv_papers", "verify_retry_at")
