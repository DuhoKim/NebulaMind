"""extend_claim_marker_runs_metrics

Revision ID: 9b26e14afeed
Revises: dfbbbacc63c2
Create Date: 2026-06-01 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9b26e14afeed'
down_revision: Union[str, None] = "renovation_interval_per_page_v1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('claim_marker_runs', sa.Column('asserted_count', sa.Integer(), nullable=True))
    op.add_column('claim_marker_runs', sa.Column('topical_anchor_count', sa.Integer(), nullable=True))
    op.add_column('claim_marker_runs', sa.Column('tier_breakdown', sa.JSON(), nullable=True))


def downgrade() -> None:
    op.drop_column('claim_marker_runs', 'tier_breakdown')
    op.drop_column('claim_marker_runs', 'topical_anchor_count')
    op.drop_column('claim_marker_runs', 'asserted_count')
