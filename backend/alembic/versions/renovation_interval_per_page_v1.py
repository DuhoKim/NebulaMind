"""renovation_interval_per_page_v1

Adds wiki_pages.renovation_interval_days INTEGER NULL to allow per-page renovation
cadence override. queue_next_renovation uses COALESCE(p.renovation_interval_days, 14)
to compute the eligibility window. NULL = use the global default (14 days).

Revision ID: renovation_interval_per_page_v1
Revises: dfbbbacc63c2
"""
from alembic import op
import sqlalchemy as sa


revision = "renovation_interval_per_page_v1"
down_revision = "dfbbbacc63c2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "wiki_pages",
        sa.Column("renovation_interval_days", sa.Integer(), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("wiki_pages", "renovation_interval_days")
