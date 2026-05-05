"""Wiki Renovation Phase 1: health score + renovation_plans

Revision ID: wiki_renovation_v1
Revises: tiered_council_v1
"""
from alembic import op
import sqlalchemy as sa

revision = "wiki_renovation_v1"
down_revision = "tiered_council_v1"
branch_labels = None
depends_on = None


def upgrade():
    # do_not_renovate flag and health columns on wiki_pages
    op.add_column("wiki_pages", sa.Column("do_not_renovate", sa.Boolean(),
        nullable=False, server_default="false"))
    op.add_column("wiki_pages", sa.Column("last_renovated_at", sa.TIMESTAMP(), nullable=True))
    op.add_column("wiki_pages", sa.Column("health_score", sa.Numeric(5, 2), nullable=True))
    op.add_column("wiki_pages", sa.Column("health_updated_at", sa.TIMESTAMP(), nullable=True))

    # renovation_plans table
    op.create_table("renovation_plans",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id"), nullable=False),
        sa.Column("health_score", sa.Numeric(5, 2), nullable=False),
        sa.Column("components", sa.JSON(), nullable=False),
        sa.Column("weakest_dimensions", sa.Text(), nullable=True),   # comma-separated
        sa.Column("missing_subtopics", sa.Text(), nullable=True),    # JSON array
        sa.Column("status", sa.String(20), nullable=False, server_default="queued"),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("started_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("completed_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("edit_proposal_id", sa.Integer(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
    )
    op.create_index("idx_renovation_status", "renovation_plans", ["status", "health_score"])
    op.create_index("idx_renovation_page", "renovation_plans", ["page_id"])


def downgrade():
    op.drop_index("idx_renovation_page", "renovation_plans")
    op.drop_index("idx_renovation_status", "renovation_plans")
    op.drop_table("renovation_plans")
    op.drop_column("wiki_pages", "health_updated_at")
    op.drop_column("wiki_pages", "health_score")
    op.drop_column("wiki_pages", "last_renovated_at")
    op.drop_column("wiki_pages", "do_not_renovate")
