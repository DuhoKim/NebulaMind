"""autowiki_runs: add idea_signals_json for §16 telemetry

Revision ID: autowiki_idea_signals_v1
Revises: research_ideas_phase3_v1
Create Date: 2026-05-14
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "autowiki_idea_signals_v1"
down_revision = "research_ideas_phase3_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("autowiki_runs", sa.Column("idea_signals_json", JSONB, nullable=True))


def downgrade():
    op.drop_column("autowiki_runs", "idea_signals_json")
