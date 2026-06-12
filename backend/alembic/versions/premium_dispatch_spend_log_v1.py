"""Premium dispatch spend log

Revision ID: premium_dispatch_spend_log_v1
Revises: 9b26e14afeed
"""
from alembic import op
import sqlalchemy as sa

revision = "premium_dispatch_spend_log_v1"
down_revision = "9b26e14afeed"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "llm_spend_log",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("job_name", sa.String(120), nullable=False),
        sa.Column("model_name", sa.String(160), nullable=False),
        sa.Column("tier", sa.String(20), nullable=False),
        sa.Column("estimated_tokens", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("prompt_tokens", sa.Integer(), nullable=True),
        sa.Column("completion_tokens", sa.Integer(), nullable=True),
        sa.Column("input_cost_krw", sa.Float(), nullable=False, server_default="0"),
        sa.Column("output_cost_krw", sa.Float(), nullable=False, server_default="0"),
        sa.Column("total_cost_krw", sa.Float(), nullable=False, server_default="0"),
        sa.Column("status", sa.String(20), nullable=False, server_default="executed"),
        sa.Column("blocked_reason", sa.Text(), nullable=True),
        sa.Column("metadata_json", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("idx_llm_spend_window", "llm_spend_log", ["created_at", "tier", "status"])
    op.create_index("idx_llm_spend_job", "llm_spend_log", ["job_name", "created_at"])
    op.create_index("idx_llm_spend_model", "llm_spend_log", ["model_name", "created_at"])


def downgrade():
    op.drop_index("idx_llm_spend_model", "llm_spend_log")
    op.drop_index("idx_llm_spend_job", "llm_spend_log")
    op.drop_index("idx_llm_spend_window", "llm_spend_log")
    op.drop_table("llm_spend_log")
