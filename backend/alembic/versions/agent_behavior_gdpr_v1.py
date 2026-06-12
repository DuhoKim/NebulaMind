"""Agent behavior scores + GDPR subscriber retention

Revision ID: agent_behavior_gdpr_v1
Revises: agent_key_hash_v1
"""
from alembic import op
import sqlalchemy as sa

revision = "agent_behavior_gdpr_v1"
down_revision = "agent_key_hash_v1"
branch_labels = None
depends_on = None


def upgrade():
    # Agent behavior scoring table
    op.create_table(
        "agent_behavior_scores",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("agent_id", sa.Integer(), sa.ForeignKey("agents.id"), nullable=False, unique=True),
        sa.Column("behavior_score", sa.Numeric(4, 3), nullable=False, server_default="0.500"),
        sa.Column("components", sa.JSON(), nullable=True),
        sa.Column("flags", sa.JSON(), nullable=True),  # list of flag strings
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("idx_behavior_agent", "agent_behavior_scores", ["agent_id"])
    op.create_index("idx_behavior_score", "agent_behavior_scores", ["behavior_score"])

    # GDPR: subscriber lifecycle columns
    op.add_column("subscribers", sa.Column("unsubscribed_at", sa.TIMESTAMP(), nullable=True))
    op.add_column("subscribers", sa.Column("deleted_at", sa.TIMESTAMP(), nullable=True))
    op.add_column("subscribers", sa.Column("anonymized_at", sa.TIMESTAMP(), nullable=True))


def downgrade():
    op.drop_column("subscribers", "anonymized_at")
    op.drop_column("subscribers", "deleted_at")
    op.drop_column("subscribers", "unsubscribed_at")
    op.drop_index("idx_behavior_score", "agent_behavior_scores")
    op.drop_index("idx_behavior_agent", "agent_behavior_scores")
    op.drop_table("agent_behavior_scores")
