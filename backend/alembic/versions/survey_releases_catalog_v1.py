"""survey_releases_catalog_v1: release history and catalog field metadata

Revision ID: survey_releases_catalog_v1
Revises: merge_verified_heads_20260612
Create Date: 2026-06-12
"""
from alembic import op
import sqlalchemy as sa


revision = "survey_releases_catalog_v1"
down_revision = "merge_verified_heads_20260612"
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_tables = set(insp.get_table_names())

    if "survey_data_releases" not in existing_tables:
        op.create_table(
            "survey_data_releases",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("survey_id", sa.Integer(), sa.ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False),
            sa.Column("label", sa.String(length=60), nullable=False),
            sa.Column("release_date", sa.Date(), nullable=True),
            sa.Column("release_year", sa.Integer(), nullable=True),
            sa.Column("summary", sa.Text(), nullable=False),
            sa.Column("n_objects", sa.BigInteger(), nullable=True),
            sa.Column("sky_coverage_deg2", sa.Numeric(10, 2), nullable=True),
            sa.Column("data_volume_tb", sa.Float(), nullable=True),
            sa.Column("doi", sa.String(length=200), nullable=True),
            sa.Column("bibcode", sa.String(length=40), nullable=True),
            sa.Column("url", sa.Text(), nullable=True),
            sa.Column("status", sa.String(length=20), nullable=False, server_default="released"),
            sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.func.now()),
            sa.Column("updated_at", sa.TIMESTAMP(), nullable=False, server_default=sa.func.now()),
            sa.UniqueConstraint("survey_id", "label", name="uq_survey_data_releases_survey_label"),
            sa.CheckConstraint(
                "status IN ('planned', 'released', 'superseded', 'final')",
                name="ck_survey_data_releases_status",
            ),
        )
        op.create_index("ix_sdr_survey", "survey_data_releases", ["survey_id"])

    if "survey_catalog_fields" not in existing_tables:
        op.create_table(
            "survey_catalog_fields",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("dataset_id", sa.Integer(), sa.ForeignKey("survey_datasets.id", ondelete="CASCADE"), nullable=False),
            sa.Column("name", sa.String(length=80), nullable=False),
            sa.Column("dtype", sa.String(length=20), nullable=True),
            sa.Column("unit", sa.String(length=40), nullable=True),
            sa.Column("ucd", sa.String(length=80), nullable=True),
            sa.Column("description", sa.Text(), nullable=False),
            sa.Column("example", sa.String(length=120), nullable=True),
            sa.Column("is_key", sa.Boolean(), nullable=False, server_default=sa.text("false")),
            sa.Column("sort_order", sa.Integer(), nullable=False, server_default="0"),
            sa.Column("source_url", sa.Text(), nullable=False),
            sa.UniqueConstraint("dataset_id", "name", name="uq_survey_catalog_fields_dataset_name"),
        )
        op.create_index("ix_scf_dataset", "survey_catalog_fields", ["dataset_id"])


def downgrade():
    op.drop_index("ix_scf_dataset", table_name="survey_catalog_fields")
    op.drop_table("survey_catalog_fields")
    op.drop_index("ix_sdr_survey", table_name="survey_data_releases")
    op.drop_table("survey_data_releases")
