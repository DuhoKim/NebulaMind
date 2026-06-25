"""widen pipeline_runs.schedule_name to VARCHAR(255)

Revision ID: pipeline_runs_schedule_name_widen_v1
Revises: facility_registry_links_v1
"""
from alembic import op
import sqlalchemy as sa

revision = "pipeline_runs_schedule_name_widen_v1"
down_revision = "facility_registry_links_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        "pipeline_runs",
        "schedule_name",
        existing_type=sa.String(120),
        type_=sa.String(255),
        existing_nullable=True,
    )


def downgrade():
    op.alter_column(
        "pipeline_runs",
        "schedule_name",
        existing_type=sa.String(255),
        type_=sa.String(120),
        existing_nullable=True,
    )
