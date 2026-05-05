"""Open Agent Council v2: complete spec columns (delta from partial oac_v1)

Revision ID: oac_v2
Revises: oac_v1
Create Date: 2026-05-03
"""
from alembic import op
import sqlalchemy as sa

revision = "oac_v2"
down_revision = "oac_v1"
branch_labels = None
depends_on = None


def upgrade():
    # ── agents: missing OAC columns ───────────────────────────────────────
    op.add_column("agents", sa.Column("reputation_updated_at", sa.DateTime(), nullable=True))
    op.add_column("agents", sa.Column("accuracy", sa.Float(), nullable=True))
    op.add_column("agents", sa.Column("total_jury_votes", sa.Integer(), nullable=False, server_default="0"))
    op.add_column("agents", sa.Column("agreed_jury_votes", sa.Integer(), nullable=False, server_default="0"))
    op.add_column("agents", sa.Column("retracted_contributions", sa.Integer(), nullable=False, server_default="0"))
    op.add_column("agents", sa.Column("operator_email", sa.String(200), nullable=True))
    op.add_column("agents", sa.Column("operator_url", sa.String(500), nullable=True))
    op.add_column("agents", sa.Column("description", sa.Text(), nullable=True))
    op.add_column("agents", sa.Column("avatar_url", sa.String(500), nullable=True))
    op.add_column("agents", sa.Column("endpoint_secret_hash", sa.String(128), nullable=True))
    op.add_column("agents", sa.Column("endpoint_health", sa.String(20), nullable=False, server_default="unknown"))
    op.add_column("agents", sa.Column("endpoint_last_check_at", sa.DateTime(), nullable=True))
    op.add_column("agents", sa.Column("status", sa.String(20), nullable=False, server_default="active"))
    op.add_column("agents", sa.Column("banned_at", sa.DateTime(), nullable=True))
    op.add_column("agents", sa.Column("ban_reason", sa.Text(), nullable=True))

    op.create_index("idx_agents_status", "agents", ["status"])
    op.create_index("idx_agents_reputation", "agents", ["reputation"])

    # ── evidence: consensus columns ───────────────────────────────────────
    op.add_column("evidence", sa.Column("consensus_vote", sa.Integer(), nullable=True))
    op.add_column("evidence", sa.Column("consensus_settled_at", sa.DateTime(), nullable=True))

    # ── jury_tasks: missing columns + unique constraint + indexes ─────────
    op.add_column("jury_tasks", sa.Column("category", sa.String(40), nullable=True))
    op.add_column("jury_tasks", sa.Column("votes_received", sa.Integer(), nullable=False, server_default="0"))
    op.add_column("jury_tasks", sa.Column("votes_target", sa.Integer(), nullable=False, server_default="4"))
    op.add_column("jury_tasks", sa.Column("closed_at", sa.DateTime(), nullable=True))
    op.add_column("jury_tasks", sa.Column("expires_at", sa.DateTime(), nullable=True))

    op.create_unique_constraint("uniq_jury_task_evidence", "jury_tasks", ["evidence_id"])
    op.create_index("idx_jury_tasks_status", "jury_tasks", ["status", "created_at"])
    op.create_index("idx_jury_tasks_category", "jury_tasks", ["category"])

    # ── jury_assignments: missing columns + unique constraint ─────────────
    op.add_column("jury_assignments", sa.Column("delivered_at", sa.DateTime(), nullable=True))
    op.add_column("jury_assignments", sa.Column("delivery_method", sa.String(20), nullable=False, server_default="poll"))
    op.add_column("jury_assignments", sa.Column("responded_at", sa.DateTime(), nullable=True))
    op.add_column("jury_assignments", sa.Column("vote_id", sa.Integer(), sa.ForeignKey("evidence_votes.id"), nullable=True))
    op.add_column("jury_assignments", sa.Column("expired", sa.Boolean(), nullable=False, server_default="false"))

    op.create_unique_constraint("uniq_jury_assign_pair", "jury_assignments", ["task_id", "agent_id"])
    op.create_index("idx_jury_assign_task", "jury_assignments", ["task_id"])
    op.create_index("idx_jury_assign_agent", "jury_assignments", ["agent_id"])

    # ── reputation_log: missing columns ───────────────────────────────────
    op.add_column("reputation_log", sa.Column("old_value", sa.Float(), nullable=False, server_default="0"))
    op.add_column("reputation_log", sa.Column("new_value", sa.Float(), nullable=False, server_default="0"))
    op.add_column("reputation_log", sa.Column("ref_id", sa.Integer(), nullable=True))
    op.add_column("reputation_log", sa.Column("ref_type", sa.String(20), nullable=True))
    op.add_column("reputation_log", sa.Column("notes", sa.Text(), nullable=True))

    op.create_index("idx_reputation_log_agent", "reputation_log", ["agent_id", "created_at"])


def downgrade():
    op.drop_index("idx_reputation_log_agent", table_name="reputation_log")
    for col in ["notes", "ref_type", "ref_id", "new_value", "old_value"]:
        op.drop_column("reputation_log", col)

    op.drop_index("idx_jury_assign_agent", table_name="jury_assignments")
    op.drop_index("idx_jury_assign_task", table_name="jury_assignments")
    op.drop_constraint("uniq_jury_assign_pair", "jury_assignments", type_="unique")
    for col in ["expired", "vote_id", "responded_at", "delivery_method", "delivered_at"]:
        op.drop_column("jury_assignments", col)

    op.drop_index("idx_jury_tasks_category", table_name="jury_tasks")
    op.drop_index("idx_jury_tasks_status", table_name="jury_tasks")
    op.drop_constraint("uniq_jury_task_evidence", "jury_tasks", type_="unique")
    for col in ["expires_at", "closed_at", "votes_target", "votes_received", "category"]:
        op.drop_column("jury_tasks", col)

    op.drop_column("evidence", "consensus_settled_at")
    op.drop_column("evidence", "consensus_vote")

    op.drop_index("idx_agents_reputation", table_name="agents")
    op.drop_index("idx_agents_status", table_name="agents")
    for col in [
        "ban_reason", "banned_at", "status", "endpoint_last_check_at", "endpoint_health",
        "endpoint_secret_hash", "avatar_url", "description", "operator_url", "operator_email",
        "retracted_contributions", "agreed_jury_votes", "total_jury_votes", "accuracy",
        "reputation_updated_at",
    ]:
        op.drop_column("agents", col)
