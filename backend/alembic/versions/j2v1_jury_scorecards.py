"""j2v1 jury scorecards

Revision ID: j2v1
Revises: premium_dispatch_spend_log_v1
Create Date: 2026-06-06
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "j2v1"
down_revision = "premium_dispatch_spend_log_v1"
branch_labels = None
depends_on = None


def upgrade():
    # 1. Create prompt_revisions table
    op.create_table(
        "prompt_revisions",
        sa.Column("id", sa.BigInteger(), primary_key=True),
        sa.Column("prompt_id", sa.String(length=80), nullable=False),
        sa.Column("policy_id", sa.String(length=80), nullable=False),
        sa.Column("prompt_sha256", sa.String(length=64), nullable=False, unique=True),
        sa.Column("system_text", sa.Text(), nullable=False),
        sa.Column("user_template", sa.Text(), nullable=False),
        sa.Column("aggregation", JSONB(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("idx_prompt_rev_prompt_policy", "prompt_revisions", ["prompt_id", "policy_id"])

    # 2. Create jury_scorecards table
    op.create_table(
        "jury_scorecards",
        sa.Column("id", sa.BigInteger(), primary_key=True),
        sa.Column("evidence_id", sa.BigInteger(), sa.ForeignKey("evidence.id", ondelete="CASCADE"), nullable=False),
        sa.Column("prompt_revision_id", sa.BigInteger(), sa.ForeignKey("prompt_revisions.id"), nullable=False),
        sa.Column("relevance", sa.Float(), nullable=False),
        sa.Column("entailment", sa.Float(), nullable=False),
        sa.Column("rigor", sa.Float(), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("var_entailment", sa.Float(), nullable=False),
        sa.Column("quality_v2", sa.Float(), nullable=False),
        sa.Column("stance", sa.String(length=20), nullable=False),
        sa.Column("jurors_used", JSONB(), nullable=False),
        sa.Column("policy_id", sa.String(length=80), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("idx_jury_scorecards_evidence", "jury_scorecards", ["evidence_id", "created_at"])

    # 3. Create jury_agent_profiles table
    op.create_table(
        "jury_agent_profiles",
        sa.Column("agent_id", sa.Integer(), sa.ForeignKey("agents.id", ondelete="CASCADE"), primary_key=True),
        sa.Column("tier_weight", sa.Float(), nullable=False, server_default="0.7"),
        sa.Column("domain_weight", sa.Float(), nullable=False, server_default="0.85"),
        sa.Column("reliability_weight", sa.Float(), nullable=False, server_default="0.6"),
        sa.Column("calibration_temperature", sa.Float(), nullable=False, server_default="1.0"),
        sa.Column("fallback_chain", JSONB(), nullable=False, server_default=sa.text("'[]'")),
        sa.Column("last_calibrated_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
    )

    # 4. Add columns to evidence
    op.add_column("evidence", sa.Column("consensus_scorecard_id", sa.BigInteger(), sa.ForeignKey("jury_scorecards.id"), nullable=True))
    op.add_column("evidence", sa.Column("relevance", sa.Float(), nullable=True))
    op.add_column("evidence", sa.Column("entailment", sa.Float(), nullable=True))
    op.add_column("evidence", sa.Column("rigor", sa.Float(), nullable=True))
    op.add_column("evidence", sa.Column("confidence", sa.Float(), nullable=True))

    # 5. Add columns to evidence_votes
    op.add_column("evidence_votes", sa.Column("prompt_revision_id", sa.BigInteger(), sa.ForeignKey("prompt_revisions.id"), nullable=True))
    op.add_column("evidence_votes", sa.Column("relevance", sa.Float(), nullable=True))
    op.add_column("evidence_votes", sa.Column("entailment", sa.Float(), nullable=True))
    op.add_column("evidence_votes", sa.Column("rigor", sa.Float(), nullable=True))
    op.add_column("evidence_votes", sa.Column("confidence", sa.Float(), nullable=True))
    op.add_column("evidence_votes", sa.Column("scheduled_via", sa.String(length=40), nullable=True))
    op.add_column("evidence_votes", sa.Column("latency_ms", sa.Integer(), nullable=True))
    op.create_index("idx_evidence_votes_prompt_rev", "evidence_votes", ["prompt_revision_id"])

    # 6. Seed jury_agent_profiles for all existing registered agents
    op.execute(
        "INSERT INTO jury_agent_profiles (agent_id, tier_weight, domain_weight, reliability_weight, calibration_temperature, fallback_chain) "
        "SELECT id, 0.7, 0.85, 0.6, 1.0, '[]'::jsonb FROM agents "
        "ON CONFLICT (agent_id) DO NOTHING"
    )


def downgrade():
    op.drop_index("idx_evidence_votes_prompt_rev", "evidence_votes")
    op.drop_column("evidence_votes", "latency_ms")
    op.drop_column("evidence_votes", "scheduled_via")
    op.drop_column("evidence_votes", "confidence")
    op.drop_column("evidence_votes", "rigor")
    op.drop_column("evidence_votes", "entailment")
    op.drop_column("evidence_votes", "relevance")
    op.drop_column("evidence_votes", "prompt_revision_id")

    op.drop_column("evidence", "confidence")
    op.drop_column("evidence", "rigor")
    op.drop_column("evidence", "entailment")
    op.drop_column("evidence", "relevance")
    op.drop_column("evidence", "consensus_scorecard_id")

    op.drop_table("jury_agent_profiles")
    op.drop_table("jury_scorecards")
    op.drop_table("prompt_revisions")
