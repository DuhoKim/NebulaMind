"""add gap_type, conflicting_claim_ids, bridge_section_pair to research_ideas (Karpathy v2)

Revision ID: 20260519_001_add_gap_type_karpathy_v2
Revises: pipeline_v2_2026_05_15, doi_resolution_log_v1
Create Date: 2026-05-19
"""
from alembic import op
import sqlalchemy as sa

revision = "karpathy_v2_schema_v1"
down_revision = ("pipeline_v2_2026_05_15", "doi_resolution_log_v1")
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_cols = {c["name"] for c in insp.get_columns("research_ideas")}

    new_cols = {
        "gap_type": (
            "VARCHAR(20) "
            "CHECK (gap_type IN ('gap', 'tension', 'bridge', 'frontier', 'synergy'))"
        ),
        "gap_type_source": (
            "VARCHAR(20) "
            "CHECK (gap_type_source IN ('karpathy_v2', 'atom_backfill', 'manual'))"
        ),
        "conflicting_claim_ids": "INTEGER[]",
        "bridge_section_pair": "TEXT[]",
    }
    for col, typedef in new_cols.items():
        if col not in existing_cols:
            op.execute(f"ALTER TABLE research_ideas ADD COLUMN {col} {typedef}")


def downgrade():
    op.execute("ALTER TABLE research_ideas DROP COLUMN IF EXISTS gap_type")
    op.execute("ALTER TABLE research_ideas DROP COLUMN IF EXISTS gap_type_source")
    op.execute("ALTER TABLE research_ideas DROP COLUMN IF EXISTS conflicting_claim_ids")
    op.execute("ALTER TABLE research_ideas DROP COLUMN IF EXISTS bridge_section_pair")
