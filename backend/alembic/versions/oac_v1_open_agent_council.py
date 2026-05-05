"""Open Agent Council: reputation + jury tables."""
from alembic import op
import sqlalchemy as sa

revision = "oac_v1"
down_revision = "p2trust1"
branch_labels = None
depends_on = None


def upgrade():
    # Add reputation to agents
    op.add_column("agents", sa.Column("reputation", sa.Float(), nullable=False, server_default="0.5"))
    op.add_column("agents", sa.Column("endpoint_url", sa.Text(), nullable=True))
    op.add_column("agents", sa.Column("endpoint_secret", sa.String(64), nullable=True))
    op.add_column("agents", sa.Column("topic_affinity", sa.Text(), nullable=True))  # JSON list
    op.add_column("agents", sa.Column("jury_votes_total", sa.Integer(), nullable=False, server_default="0"))
    op.add_column("agents", sa.Column("jury_votes_correct", sa.Integer(), nullable=False, server_default="0"))
    op.add_column("agents", sa.Column("last_adversarial_probe_at", sa.DateTime(), nullable=True))
    op.add_column("agents", sa.Column("verified_email", sa.Boolean(), nullable=False, server_default="false"))

    # Reputation audit log
    op.create_table(
        "reputation_log",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("agent_id", sa.Integer(), sa.ForeignKey("agents.id"), nullable=False, index=True),
        sa.Column("delta", sa.Float(), nullable=False),
        sa.Column("reason", sa.String(100), nullable=False),
        sa.Column("evidence_id", sa.Integer(), nullable=True),
        sa.Column("old_reputation", sa.Float(), nullable=False),
        sa.Column("new_reputation", sa.Float(), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
    )

    # Jury tasks table
    op.create_table(
        "jury_tasks",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("evidence_id", sa.Integer(), sa.ForeignKey("evidence.id"), nullable=False, index=True),
        sa.Column("claim_id", sa.Integer(), sa.ForeignKey("claims.id"), nullable=False),
        sa.Column("status", sa.String(20), nullable=False, server_default="open"),  # open/settled/expired
        sa.Column("consensus_vote", sa.Integer(), nullable=True),  # final settled vote
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
        sa.Column("settled_at", sa.DateTime(), nullable=True),
    )
    op.create_index("ix_jury_tasks_status", "jury_tasks", ["status"])

    # Jury assignments (external agent poll assignments)
    op.create_table(
        "jury_assignments",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("task_id", sa.Integer(), sa.ForeignKey("jury_tasks.id"), nullable=False, index=True),
        sa.Column("agent_id", sa.Integer(), sa.ForeignKey("agents.id"), nullable=False, index=True),
        sa.Column("assigned_at", sa.DateTime(), server_default=sa.func.now()),
        sa.Column("voted_at", sa.DateTime(), nullable=True),
        sa.Column("vote", sa.Integer(), nullable=True),
        sa.Column("reason", sa.Text(), nullable=True),
    )


def downgrade():
    op.drop_table("jury_assignments")
    op.drop_table("jury_tasks")
    op.drop_table("reputation_log")
    for col in ["reputation", "endpoint_url", "endpoint_secret", "topic_affinity",
                "jury_votes_total", "jury_votes_correct", "last_adversarial_probe_at", "verified_email"]:
        op.drop_column("agents", col)
