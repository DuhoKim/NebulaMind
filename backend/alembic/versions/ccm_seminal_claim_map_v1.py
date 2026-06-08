"""CCM seminal claim map

Revision ID: ccm_seminal_claim_map_v1
Revises: page_citation_links_v1
Create Date: 2026-06-08
"""
from alembic import op
import sqlalchemy as sa


revision = "ccm_seminal_claim_map_v1"
down_revision = "page_citation_links_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "seminal_claim_map",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("claim_id", sa.Integer(), sa.ForeignKey("claims.id", ondelete="CASCADE"), nullable=False),
        sa.Column("canonical_bibcode", sa.String(30), nullable=False),
        sa.Column("canonical_label", sa.String(120), nullable=False),
        sa.Column("canonical_doi", sa.String(100), nullable=True),
        sa.Column("canonical_arxiv_id", sa.String(30), nullable=True),
        sa.Column("topic_keyphrases", sa.Text(), nullable=True),
        sa.Column("enabled", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        sa.Column("added_by", sa.String(40), nullable=False, server_default="manual"),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), server_default=sa.text("now()")),
        sa.Column("updated_at", sa.TIMESTAMP(), server_default=sa.text("now()")),
        sa.UniqueConstraint("claim_id", "canonical_bibcode", name="uq_seminal_claim_map_claim_bibcode"),
    )
    op.create_index("ix_seminal_claim_map_claim", "seminal_claim_map", ["claim_id"])
    op.create_index("ix_seminal_claim_map_bibcode", "seminal_claim_map", ["canonical_bibcode"])
    op.create_index(
        "ix_seminal_claim_map_enabled",
        "seminal_claim_map",
        ["enabled"],
        postgresql_where=sa.text("enabled"),
    )


def downgrade():
    op.drop_index("ix_seminal_claim_map_enabled", table_name="seminal_claim_map")
    op.drop_index("ix_seminal_claim_map_bibcode", table_name="seminal_claim_map")
    op.drop_index("ix_seminal_claim_map_claim", table_name="seminal_claim_map")
    op.drop_table("seminal_claim_map")
