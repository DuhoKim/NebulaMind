"""research ideas factual verification fields

Revision ID: research_ideas_factual_verification_v1
Revises: page_orchestration_registry_v1
Create Date: 2026-06-12
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "research_ideas_factual_verification_v1"
down_revision = "page_orchestration_registry_v1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("research_ideas", sa.Column("factual_verified", sa.Boolean(), nullable=False, server_default=sa.text("false")))
    op.add_column("research_ideas", sa.Column("factual_verified_at", sa.DateTime(), nullable=True))
    op.add_column(
        "research_ideas",
        sa.Column("factual_verification_notes", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default=sa.text("'{}'::jsonb")),
    )


def downgrade() -> None:
    op.drop_column("research_ideas", "factual_verification_notes")
    op.drop_column("research_ideas", "factual_verified_at")
    op.drop_column("research_ideas", "factual_verified")
