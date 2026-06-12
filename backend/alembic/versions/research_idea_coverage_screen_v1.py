"""research idea coverage screen fields

Revision ID: research_idea_coverage_screen_v1
Revises: research_ideas_factual_verification_v1
Create Date: 2026-06-12
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "research_idea_coverage_screen_v1"
down_revision = "research_ideas_factual_verification_v1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE research_ideas ADD COLUMN IF NOT EXISTS coverage_status VARCHAR(20)")
    op.execute("ALTER TABLE research_ideas ADD COLUMN IF NOT EXISTS closest_prior_work JSONB")
    op.execute("ALTER TABLE research_ideas ADD COLUMN IF NOT EXISTS coverage_checked_at TIMESTAMPTZ")
    op.execute("CREATE INDEX IF NOT EXISTS ix_research_ideas_coverage_status ON research_ideas (coverage_status)")
    op.execute(
        """
        UPDATE research_ideas
        SET factual_verified = (coverage_status IN ('screened_pass', 'partial'))
        WHERE coverage_status IS NOT NULL
        """
    )


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS ix_research_ideas_coverage_status")
    op.execute("ALTER TABLE research_ideas DROP COLUMN IF EXISTS coverage_checked_at")
    op.execute("ALTER TABLE research_ideas DROP COLUMN IF EXISTS closest_prior_work")
    op.execute("ALTER TABLE research_ideas DROP COLUMN IF EXISTS coverage_status")
