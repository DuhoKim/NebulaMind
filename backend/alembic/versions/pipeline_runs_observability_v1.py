"""pipeline runs observability ledger

Revision ID: pipeline_runs_observability_v1
Revises: merge_phase3_heads
"""
from alembic import op
import sqlalchemy as sa

revision = "pipeline_runs_observability_v1"
down_revision = "merge_phase3_heads"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "pipeline_runs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("task_name", sa.String(200), nullable=False),
        sa.Column("task_id", sa.String(80), nullable=True),
        sa.Column("schedule_name", sa.String(120), nullable=True),
        sa.Column("status", sa.String(20), nullable=False, server_default="running"),
        sa.Column("started_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("finished_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("duration_ms", sa.Integer(), nullable=True),
        sa.Column("args_json", sa.Text(), nullable=True),
        sa.Column("kwargs_json", sa.Text(), nullable=True),
        sa.Column("result_json", sa.Text(), nullable=True),
        sa.Column("error_text", sa.Text(), nullable=True),
    )
    op.create_index("idx_pipeline_runs_task_started", "pipeline_runs", ["task_name", "started_at"])
    op.create_index(
        "idx_pipeline_runs_task_id",
        "pipeline_runs",
        ["task_id"],
        unique=True,
        postgresql_where=sa.text("task_id IS NOT NULL"),
    )


def downgrade():
    op.drop_index("idx_pipeline_runs_task_id", table_name="pipeline_runs")
    op.drop_index("idx_pipeline_runs_task_started", table_name="pipeline_runs")
    op.drop_table("pipeline_runs")
