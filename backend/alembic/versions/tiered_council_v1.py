"""Tiered Council MVP — schema

Revision ID: tiered_council_v1
Revises: fact_sources_v1
Create Date: 2026-05-05
"""
from alembic import op
import sqlalchemy as sa

revision = "tiered_council_v1"
down_revision = "fact_sources_v1"
branch_labels = None
depends_on = None


def upgrade():
    # Extend agents
    op.add_column("agents", sa.Column("is_verified", sa.Boolean(), nullable=False, server_default="false"))
    op.add_column("agents", sa.Column("verified_at", sa.TIMESTAMP(), nullable=True))
    op.add_column("agents", sa.Column("verified_via", sa.String(40), nullable=True))

    # Stage 3 roll
    op.create_table(
        "stage3_roll",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("agent_id", sa.Integer(), sa.ForeignKey("agents.id"), unique=True, nullable=False),
        sa.Column("seated_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("seated_by", sa.Integer(), nullable=True),
        sa.Column("seat_reason", sa.String(40), nullable=False),
        sa.Column("removed_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("removal_reason", sa.Text(), nullable=True),
    )
    op.create_index(
        "idx_stage3_roll_active", "stage3_roll", ["agent_id"],
        postgresql_where=sa.text("removed_at IS NULL"),
    )

    # Escalations
    op.create_table(
        "escalations",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("source_kind", sa.String(40), nullable=False),
        sa.Column("source_id", sa.Integer(), nullable=False),
        sa.Column("current_stage", sa.Integer(), nullable=False),
        sa.Column("trigger_code", sa.String(20), nullable=False),
        sa.Column("trigger_detail", sa.Text(), nullable=True),
        sa.Column("status", sa.String(20), nullable=False, server_default="open"),
        sa.Column("resolution", sa.String(40), nullable=True),
        sa.Column("votes_received", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("votes_target", sa.Integer(), nullable=False),
        sa.Column("veto_count", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("opened_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("expires_at", sa.TIMESTAMP(), nullable=False),
        sa.Column("resolved_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("opened_by_agent_id", sa.Integer(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
    )
    op.create_index("idx_escalations_status", "escalations", ["status", "current_stage"])
    op.create_index("idx_escalations_source", "escalations", ["source_kind", "source_id"])

    # Escalation votes
    op.create_table(
        "escalation_votes",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("escalation_id", sa.Integer(), sa.ForeignKey("escalations.id"), nullable=False),
        sa.Column("agent_id", sa.Integer(), sa.ForeignKey("agents.id"), nullable=False),
        sa.Column("action", sa.String(20), nullable=False),
        sa.Column("weight", sa.Float(), nullable=False),
        sa.Column("voter_tier", sa.Integer(), nullable=False),
        sa.Column("reason", sa.Text(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("uniq_escal_voter", "escalation_votes", ["escalation_id", "agent_id"], unique=True)

    # Extend evidence_votes
    op.add_column(
        "evidence_votes",
        sa.Column("tier_eligibility", sa.String(20), nullable=False, server_default="stage1"),
    )

    # Extend trust_audit_log
    op.add_column("trust_audit_log", sa.Column("escalation_id", sa.Integer(), nullable=True))
    op.add_column("trust_audit_log", sa.Column("tier_decided", sa.Integer(), nullable=True))


def downgrade():
    op.drop_table("escalation_votes")
    op.drop_table("escalations")
    op.drop_table("stage3_roll")
    op.drop_column("trust_audit_log", "tier_decided")
    op.drop_column("trust_audit_log", "escalation_id")
    op.drop_column("evidence_votes", "tier_eligibility")
    op.drop_column("agents", "verified_via")
    op.drop_column("agents", "verified_at")
    op.drop_column("agents", "is_verified")
