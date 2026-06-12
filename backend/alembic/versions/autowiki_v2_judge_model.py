"""Autowiki v2 — add judge_model column to autowiki_runs

Revision ID: autowiki_v2_judge_model
Revises: autowiki_v1
"""
from alembic import op
import sqlalchemy as sa

revision = "autowiki_v2_judge_model"
down_revision = "autowiki_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "autowiki_runs",
        sa.Column("judge_model", sa.String(40), nullable=True),
    )


def downgrade():
    op.drop_column("autowiki_runs", "judge_model")
