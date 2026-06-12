"""P2 Week 2: Agent ban enforcement — add banned_until column

Revision ID: security_p2_week2_ban_v1
Revises: security_p2_week1_v1
"""
from alembic import op
import sqlalchemy as sa

revision = "security_p2_week2_ban_v1"
down_revision = "security_p2_week1_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("agents", sa.Column(
        "banned_until", sa.TIMESTAMP(), nullable=True
    ))


def downgrade():
    op.drop_column("agents", "banned_until")
