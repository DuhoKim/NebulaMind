"""add api_key to agents

Revision ID: f1a2b3c4d5e6
Revises: eba20def18d0
Create Date: 2026-04-20
"""
import uuid
from alembic import op
import sqlalchemy as sa

revision = "f1a2b3c4d5e6"
down_revision = "eba20def18d0"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "agents",
        sa.Column("api_key", sa.String(), nullable=True),
    )
    # Back-fill existing agents with a unique api_key
    bind = op.get_bind()
    agents = bind.execute(sa.text("SELECT id FROM agents")).fetchall()
    for (agent_id,) in agents:
        key = uuid.uuid4().hex
        bind.execute(
            sa.text("UPDATE agents SET api_key = :key WHERE id = :id"),
            {"key": key, "id": agent_id},
        )


def downgrade():
    op.drop_column("agents", "api_key")
