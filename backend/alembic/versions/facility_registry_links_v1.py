"""facility_registry_links_v1: link survey catalog rows to facility profiles

Revision ID: facility_registry_links_v1
Revises: write_path_lockdown_v1
Create Date: 2026-06-13
"""
from alembic import op
import sqlalchemy as sa


revision = "facility_registry_links_v1"
down_revision = "write_path_lockdown_v1"
branch_labels = None
depends_on = None


SEED_LINKS = (
    ("alma", "alma", "Exact slug and mission URL match"),
    ("desi", "desi", "Exact slug; survey operator differs in wording only"),
    ("euclid", "euclid", "Exact slug; ESA mission"),
    ("jwst", "jwst", "Exact slug; mission URL variant NASA/ESA but same mission"),
    ("rubin-lsst", "lsst-rubin", "Same entity, slug-order mismatch only"),
    ("vla", "vla", "Exact slug; operator wording differs only"),
)


def upgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_tables = set(insp.get_table_names())

    if "survey_facility_links" not in existing_tables:
        op.create_table(
            "survey_facility_links",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("survey_id", sa.Integer(), sa.ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False),
            sa.Column("facility_profile_id", sa.Integer(), sa.ForeignKey("facility_profiles.id", ondelete="CASCADE"), nullable=False),
            sa.Column("relation_type", sa.String(length=40), nullable=False, server_default="same_facility"),
            sa.Column("is_primary", sa.Boolean(), nullable=False, server_default=sa.text("true")),
            sa.Column("confidence", sa.Numeric(3, 2), nullable=False, server_default="1.00"),
            sa.Column("source", sa.String(length=80), nullable=False, server_default="manual_seed_20260613"),
            sa.Column("notes", sa.Text(), nullable=True),
            sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.func.now()),
            sa.UniqueConstraint(
                "survey_id",
                "facility_profile_id",
                "relation_type",
                name="uq_survey_facility_links_relation",
            ),
        )
        op.create_index("ix_sfl_survey", "survey_facility_links", ["survey_id"])
        op.create_index("ix_sfl_facility", "survey_facility_links", ["facility_profile_id"])

    seed_sql = sa.text(
        """
        INSERT INTO survey_facility_links (
            survey_id, facility_profile_id, relation_type, is_primary,
            confidence, source, notes
        )
        SELECT s.id, fp.id, 'same_facility', true, 1.00,
               'manual_seed_20260613', :notes
        FROM surveys s
        JOIN facility_profiles fp ON fp.slug = :facility_slug
        WHERE s.slug = :survey_slug
        ON CONFLICT (survey_id, facility_profile_id, relation_type) DO NOTHING
        """
    )
    for survey_slug, facility_slug, notes in SEED_LINKS:
        conn.execute(seed_sql, {"survey_slug": survey_slug, "facility_slug": facility_slug, "notes": notes})


def downgrade():
    op.drop_table("survey_facility_links")
