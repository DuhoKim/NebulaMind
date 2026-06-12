"""LLM Routing telemetry table

Revision ID: llm_routing_telemetry_v1
Revises: wiki_renovation_v1
"""
from alembic import op
import sqlalchemy as sa

revision = "llm_routing_telemetry_v1"
down_revision = ("wiki_renovation_v1", "news_calendar_v1")
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "llm_calls",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("task_role", sa.String(50), nullable=False),
        sa.Column("model_label", sa.String(80), nullable=False),
        sa.Column("model_name", sa.String(120), nullable=True),
        sa.Column("success", sa.Boolean(), nullable=False, server_default="true"),
        sa.Column("latency_ms", sa.Integer(), nullable=True),
        sa.Column("prompt_tokens", sa.Integer(), nullable=True),
        sa.Column("completion_tokens", sa.Integer(), nullable=True),
        sa.Column("error", sa.Text(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("idx_llm_calls_role", "llm_calls", ["task_role", "created_at"])
    op.create_index("idx_llm_calls_model", "llm_calls", ["model_label", "created_at"])


def downgrade():
    op.drop_index("idx_llm_calls_model", "llm_calls")
    op.drop_index("idx_llm_calls_role", "llm_calls")
    op.drop_table("llm_calls")
