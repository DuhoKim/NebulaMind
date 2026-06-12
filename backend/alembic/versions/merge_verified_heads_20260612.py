"""merge verified Alembic heads

Revision ID: merge_verified_heads_20260612
Revises: ccm_seminal_claim_map_v1, 20260611_content_quarantine_v1, arxiv_wiki_feed_coverage_materialization_v1, research_idea_coverage_screen_v1
Create Date: 2026-06-12
"""

from __future__ import annotations


revision = "merge_verified_heads_20260612"
down_revision = (
    "ccm_seminal_claim_map_v1",
    "20260611_content_quarantine_v1",
    "arxiv_wiki_feed_coverage_materialization_v1",
    "research_idea_coverage_screen_v1",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
