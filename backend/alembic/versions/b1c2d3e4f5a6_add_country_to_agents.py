"""add_country_to_agents

Revision ID: b1c2d3e4f5a6
Revises: 64cf233a746e
Create Date: 2026-04-05 19:35:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'b1c2d3e4f5a6'
down_revision: Union[str, None] = '64cf233a746e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('agents', sa.Column('country', sa.String(), nullable=True))
    op.add_column('agents', sa.Column('country_name', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('agents', 'country_name')
    op.drop_column('agents', 'country')
