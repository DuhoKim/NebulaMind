"""write_path_lockdown_v1: claim_proposal_votes table + unique(edit_id, agent_id) on votes

Revision ID: write_path_lockdown_v1
Revises: intro_augmentation_v1
Create Date: 2026-06-13
"""
from alembic import op
import sqlalchemy as sa


revision = "write_path_lockdown_v1"
down_revision = "intro_augmentation_v1"
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_tables = set(insp.get_table_names())

    if "claim_proposal_votes" not in existing_tables:
        op.create_table(
            "claim_proposal_votes",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("proposal_id", sa.Integer(), sa.ForeignKey("claim_edit_proposals.id"), nullable=False, index=True),
            sa.Column("agent_id", sa.Integer(), sa.ForeignKey("agents.id"), nullable=False, index=True),
            sa.Column("value", sa.Integer(), nullable=False),
            sa.Column("reason", sa.Text(), nullable=True),
            sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.func.now()),
            sa.UniqueConstraint("proposal_id", "agent_id", name="uq_claim_proposal_votes_proposal_agent"),
        )

    # Dedupe existing votes on (edit_id, agent_id), keeping the earliest row,
    # then enforce uniqueness so multi-vote inflation is impossible at the DB level.
    existing_constraints = {c["name"] for c in insp.get_unique_constraints("votes")}
    if "uq_votes_edit_agent" not in existing_constraints:
        conn.execute(sa.text("""
            DELETE FROM votes a
            USING votes b
            WHERE a.edit_id = b.edit_id
              AND a.agent_id = b.agent_id
              AND a.id > b.id
        """))
        op.create_unique_constraint("uq_votes_edit_agent", "votes", ["edit_id", "agent_id"])


def downgrade():
    op.drop_constraint("uq_votes_edit_agent", "votes", type_="unique")
    op.drop_table("claim_proposal_votes")
