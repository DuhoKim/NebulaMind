"""Surveys Directory v1: surveys table, survey_wiki_pages, seed data

Revision ID: surveys_directory_v1
Revises: wiki_renovation_v1
Create Date: 2026-05-13
"""
import json
import os
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "surveys_directory_v1"
down_revision = "wiki_renovation_v1"
branch_labels = None
depends_on = None

_DATA_FILE = os.path.join(os.path.dirname(__file__), "../../data/seed_surveys.json")


def upgrade():
    op.create_table(
        "surveys",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("slug", sa.String(40), nullable=False, unique=True),
        sa.Column("name", sa.String(60), nullable=False),
        sa.Column("full_name", sa.String(200), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("wavelength_range", sa.String(120), nullable=False),
        sa.Column("wavelength_band", sa.String(20), nullable=False),
        sa.Column("sky_coverage_deg2", sa.Numeric(10, 2), nullable=True),
        sa.Column("sky_coverage_note", sa.String(200), nullable=True),
        sa.Column("redshift_range", sa.String(120), nullable=True),
        sa.Column("instruments_json", JSONB(), nullable=False, server_default="[]"),
        sa.Column("current_data_release", sa.String(120), nullable=True),
        sa.Column("data_volume", sa.String(120), nullable=True),
        sa.Column("primary_science_goals", sa.Text(), nullable=False),
        sa.Column("flagship_programs_json", JSONB(), nullable=False, server_default="[]"),
        sa.Column("operator", sa.String(120), nullable=True),
        sa.Column("status", sa.String(20), nullable=False, server_default="operational"),
        sa.Column("archive_url", sa.Text(), nullable=True),
        sa.Column("mission_url", sa.Text(), nullable=True),
        sa.Column("emoji", sa.String(10), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("ix_surveys_wavelength_band", "surveys", ["wavelength_band"])
    op.create_index("ix_surveys_status", "surveys", ["status"])

    op.create_table(
        "survey_wiki_pages",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("survey_id", sa.Integer(), sa.ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id", ondelete="CASCADE"), nullable=False),
        sa.UniqueConstraint("survey_id", "page_id", name="uq_survey_wiki_pages"),
    )

    # Bulk-insert 18 seed surveys
    seed_path = os.path.normpath(_DATA_FILE)
    with open(seed_path) as f:
        seeds = json.load(f)

    conn = op.get_bind()
    surveys_table = sa.table(
        "surveys",
        sa.column("slug", sa.String),
        sa.column("name", sa.String),
        sa.column("full_name", sa.String),
        sa.column("description", sa.Text),
        sa.column("wavelength_range", sa.String),
        sa.column("wavelength_band", sa.String),
        sa.column("sky_coverage_deg2", sa.Numeric),
        sa.column("sky_coverage_note", sa.String),
        sa.column("redshift_range", sa.String),
        sa.column("instruments_json", JSONB),
        sa.column("current_data_release", sa.String),
        sa.column("data_volume", sa.String),
        sa.column("primary_science_goals", sa.Text),
        sa.column("flagship_programs_json", JSONB),
        sa.column("operator", sa.String),
        sa.column("status", sa.String),
        sa.column("archive_url", sa.Text),
        sa.column("mission_url", sa.Text),
        sa.column("emoji", sa.String),
    )
    conn.execute(surveys_table.insert(), seeds)

    # If research_ideas already exists, create the join table and backfill
    insp = sa.inspect(conn)
    existing_tables = insp.get_table_names()
    if "research_ideas" in existing_tables and "research_idea_surveys" not in existing_tables:
        _create_research_idea_surveys()
        _backfill_research_idea_surveys(conn)


def _create_research_idea_surveys():
    op.create_table(
        "research_idea_surveys",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("idea_id", sa.Integer(), sa.ForeignKey("research_ideas.id", ondelete="CASCADE"), nullable=False),
        sa.Column("survey_id", sa.Integer(), sa.ForeignKey("surveys.id", ondelete="RESTRICT"), nullable=False),
        sa.UniqueConstraint("idea_id", "survey_id", name="uq_research_idea_surveys"),
    )
    op.create_index("ix_research_idea_surveys_idea", "research_idea_surveys", ["idea_id"])
    op.create_index("ix_research_idea_surveys_survey", "research_idea_surveys", ["survey_id"])


def _backfill_research_idea_surveys(conn):
    import logging
    log = logging.getLogger("alembic.surveys_directory_v1.backfill")
    ideas = conn.execute(sa.text("SELECT id, survey_combo FROM research_ideas")).fetchall()
    for idea in ideas:
        tokens = [t.strip() for t in idea.survey_combo.split("+")]
        for token in tokens:
            row = conn.execute(
                sa.text("SELECT id FROM surveys WHERE UPPER(name) = UPPER(:t) OR UPPER(slug) = UPPER(:t)"),
                {"t": token},
            ).fetchone()
            if row is None:
                log.warning("backfill: no survey match for token %r (idea %s)", token, idea.id)
                continue
            try:
                conn.execute(
                    sa.text("INSERT INTO research_idea_surveys (idea_id, survey_id) VALUES (:iid, :sid) ON CONFLICT DO NOTHING"),
                    {"iid": idea.id, "sid": row.id},
                )
            except Exception as exc:
                log.warning("backfill: skipping idea %s / survey %s: %s", idea.id, row.id, exc)


def downgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_tables = insp.get_table_names()
    if "research_idea_surveys" in existing_tables:
        op.drop_index("ix_research_idea_surveys_survey", "research_idea_surveys")
        op.drop_index("ix_research_idea_surveys_idea", "research_idea_surveys")
        op.drop_table("research_idea_surveys")
    op.drop_table("survey_wiki_pages")
    op.drop_index("ix_surveys_status", "surveys")
    op.drop_index("ix_surveys_wavelength_band", "surveys")
    op.drop_table("surveys")
