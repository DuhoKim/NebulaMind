"""add_survey_numeric_fields: wavelength_center_um, z_max, dr_year,
data_volume_tb, limiting_magnitude, num_sources_count

Revision ID: add_survey_numeric_fields
Revises: autowiki_surveys_v1
Create Date: 2026-05-13
"""
from alembic import op
import sqlalchemy as sa

revision = "add_survey_numeric_fields"
down_revision = "autowiki_surveys_v1"
branch_labels = None
depends_on = None

_NEW_COLS = [
    ("wavelength_center_um", sa.Float(),   True),   # derived from wavelength_range
    ("z_max",               sa.Float(),   True),   # derived from redshift_range
    ("dr_year",             sa.Integer(), True),   # derived from current_data_release
    ("data_volume_tb",      sa.Float(),   True),   # derived from data_volume text
    ("limiting_magnitude",  sa.Float(),   True),   # Mima seeds later
    ("num_sources_count",   sa.BigInteger(), True), # Mima seeds later
]


def upgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing = {c["name"] for c in insp.get_columns("surveys")}
    for col_name, col_type, nullable in _NEW_COLS:
        if col_name not in existing:
            op.add_column("surveys", sa.Column(col_name, col_type, nullable=nullable))


def downgrade():
    for col_name, _, _ in _NEW_COLS:
        op.execute(f"ALTER TABLE surveys DROP COLUMN IF EXISTS {col_name}")
