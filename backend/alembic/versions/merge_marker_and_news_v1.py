"""merge claim_marker_runs_v1 and astro_news_curator_v2 heads

Revision ID: merge_marker_and_news_v1
Revises: claim_marker_runs_v1, astro_news_curator_v2
Create Date: 2026-05-20
"""

revision = "merge_marker_and_news_v1"
down_revision = ("claim_marker_runs_v1", "astro_news_curator_v2")
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
