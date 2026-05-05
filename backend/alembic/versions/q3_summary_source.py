"""Add summary_source and summary_source_url to wiki_pages."""
from alembic import op
import sqlalchemy as sa

revision = "q3_summary_src"
down_revision = "ext_sources_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("wiki_pages", sa.Column("summary_source", sa.String(40), nullable=True))
    op.add_column("wiki_pages", sa.Column("summary_source_url", sa.Text(), nullable=True))


def downgrade():
    op.drop_column("wiki_pages", "summary_source")
    op.drop_column("wiki_pages", "summary_source_url")
