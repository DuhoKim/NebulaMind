"""intro_augmentation_v1: cache paper introductions and evidence excerpts

Revision ID: intro_augmentation_v1
Revises: survey_releases_catalog_v1
Create Date: 2026-06-12
"""
from alembic import op
import sqlalchemy as sa


revision = "intro_augmentation_v1"
down_revision = "survey_releases_catalog_v1"
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_tables = set(insp.get_table_names())

    if "paper_intros" not in existing_tables:
        op.create_table(
            "paper_intros",
            sa.Column("arxiv_id", sa.String(length=30), primary_key=True),
            sa.Column("intro_text", sa.Text(), nullable=True),
            sa.Column("http_status", sa.SmallInteger(), nullable=True),
            sa.Column("source", sa.String(length=10), nullable=True),
            sa.Column("fetched_at", sa.TIMESTAMP(), nullable=False, server_default=sa.func.now()),
        )

    evidence_columns = {
        col["name"] for col in insp.get_columns("evidence")
    } if "evidence" in existing_tables else set()
    if "intro_excerpt" not in evidence_columns:
        op.add_column("evidence", sa.Column("intro_excerpt", sa.Text(), nullable=True))
    if "intro_fetch_attempted_at" not in evidence_columns:
        op.add_column("evidence", sa.Column("intro_fetch_attempted_at", sa.TIMESTAMP(), nullable=True))


def downgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_tables = set(insp.get_table_names())
    if "evidence" in existing_tables:
        evidence_columns = {col["name"] for col in insp.get_columns("evidence")}
        if "intro_fetch_attempted_at" in evidence_columns:
            op.drop_column("evidence", "intro_fetch_attempted_at")
        if "intro_excerpt" in evidence_columns:
            op.drop_column("evidence", "intro_excerpt")
    if "paper_intros" in existing_tables:
        op.drop_table("paper_intros")
