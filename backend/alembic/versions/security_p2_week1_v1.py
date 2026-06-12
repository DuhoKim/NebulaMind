"""P2 Week 1: API key expiry + audit events table

Revision ID: security_p2_week1_v1
Revises: agent_behavior_gdpr_v1
"""
from alembic import op
import sqlalchemy as sa

revision = "security_p2_week1_v1"
down_revision = "agent_behavior_gdpr_v1"
branch_labels = None
depends_on = None


def upgrade():
    # API key expiry
    op.add_column("agents", sa.Column(
        "api_key_expires_at", sa.TIMESTAMP(), nullable=True
    ))
    # Set expiry = created_at + 365 days for all existing agents
    op.execute("""
        UPDATE agents
        SET api_key_expires_at = created_at + INTERVAL '365 days'
        WHERE api_key_expires_at IS NULL
    """)

    # Audit events table
    op.create_table(
        "audit_events",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("event_type", sa.String(50), nullable=False),
        sa.Column("actor_id", sa.Integer(), nullable=True),
        sa.Column("actor_ip_hash", sa.String(64), nullable=True),  # sha256, GDPR-clean
        sa.Column("target_kind", sa.String(50), nullable=True),
        sa.Column("target_id", sa.Integer(), nullable=True),
        sa.Column("payload", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("idx_audit_type", "audit_events", ["event_type", "created_at"])
    op.create_index("idx_audit_actor", "audit_events", ["actor_id", "created_at"])


def downgrade():
    op.drop_index("idx_audit_actor", "audit_events")
    op.drop_index("idx_audit_type", "audit_events")
    op.drop_table("audit_events")
    op.drop_column("agents", "api_key_expires_at")
