"""Add journal_ref and peer_reviewed columns to evidence table

Revision ID: peer_review_v1
Revises: wiki_renovation_v1
"""
from alembic import op
import sqlalchemy as sa

revision = "peer_review_v1"
down_revision = "wiki_renovation_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("evidence", sa.Column("journal_ref", sa.String(500), nullable=True))
    op.add_column("evidence", sa.Column("peer_reviewed", sa.Boolean(),
        nullable=False, server_default="false"))
    op.create_index("idx_evidence_peer_reviewed", "evidence", ["peer_reviewed"])


def downgrade():
    op.drop_index("idx_evidence_peer_reviewed", "evidence")
    op.drop_column("evidence", "peer_reviewed")
    op.drop_column("evidence", "journal_ref")
