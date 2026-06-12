"""auto_research_improvement_v1: columns + tables for living-ideas + surveys freshness

Revision ID: auto_research_improvement_v1
Revises: research_ideas_v1
Create Date: 2026-05-13
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "auto_research_improvement_v1"
down_revision = "research_ideas_v1"
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_cols = {c["name"] for c in insp.get_columns("research_ideas")}

    # 5.1 — extend research_ideas with lifecycle tracking columns
    new_cols = {
        "promoted_at":          "TIMESTAMP",
        "promoted_by":          "VARCHAR(40)",
        "last_refreshed_at":    "TIMESTAMP",
        "refresh_count":        "INT NOT NULL DEFAULT 0",
        "covered_by_arxiv_id":  "VARCHAR(30)",
        "covered_at":           "TIMESTAMP",
        "covered_confidence":   "NUMERIC(3,2)",
    }
    for col, typedef in new_cols.items():
        if col not in existing_cols:
            op.execute(f"ALTER TABLE research_ideas ADD COLUMN {col} {typedef}")

    # Indexes (CREATE INDEX IF NOT EXISTS for idempotency)
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_research_ideas_status_created "
        "ON research_ideas(status, created_at)"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_research_ideas_last_refreshed "
        "ON research_ideas(last_refreshed_at)"
    )

    existing_tables = set(insp.get_table_names())

    # 5.2 — refresh audit log
    if "research_idea_refresh_log" not in existing_tables:
        op.create_table(
            "research_idea_refresh_log",
            sa.Column("id",             sa.Integer(), primary_key=True),
            sa.Column("idea_id",        sa.Integer(), sa.ForeignKey("research_ideas.id", ondelete="CASCADE"), nullable=False),
            sa.Column("refreshed_at",   sa.TIMESTAMP(), nullable=False, server_default=sa.text("NOW()")),
            sa.Column("trigger_kind",   sa.String(40), nullable=False),
            sa.Column("trigger_ref_id", sa.String(40), nullable=True),
            sa.Column("model_chain",    sa.String(120), nullable=False),
            sa.Column("old_question",   sa.Text(), nullable=False),
            sa.Column("old_why_now",    sa.Text(), nullable=False),
            sa.Column("old_approach",   sa.Text(), nullable=False),
            sa.Column("new_question",   sa.Text(), nullable=False),
            sa.Column("new_why_now",    sa.Text(), nullable=False),
            sa.Column("new_approach",   sa.Text(), nullable=False),
            sa.Column("anchors_added",  JSONB(), nullable=True),
        )
        op.create_index("ix_research_idea_refresh_log_idea", "research_idea_refresh_log", ["idea_id"])

    # 5.3 — survey update proposals (high-stakes queue)
    if "survey_update_proposals" not in existing_tables:
        op.create_table(
            "survey_update_proposals",
            sa.Column("id",             sa.Integer(), primary_key=True),
            sa.Column("survey_id",      sa.Integer(), sa.ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False),
            sa.Column("field",          sa.String(40), nullable=False),
            sa.Column("current_value",  sa.Text(), nullable=True),
            sa.Column("proposed_value", sa.Text(), nullable=False),
            sa.Column("source_kind",    sa.String(20), nullable=False),
            sa.Column("source_url",     sa.Text(), nullable=True),
            sa.Column("source_excerpt", sa.Text(), nullable=True),
            sa.Column("confidence",     sa.Numeric(3, 2), nullable=True),
            sa.Column("status",         sa.String(20), nullable=False, server_default="pending"),
            sa.Column("created_at",     sa.TIMESTAMP(), nullable=False, server_default=sa.text("NOW()")),
            sa.Column("reviewed_at",    sa.TIMESTAMP(), nullable=True),
            sa.Column("reviewed_by",    sa.String(40), nullable=True),
        )
        op.create_index("ix_survey_update_proposals_status", "survey_update_proposals", ["status"])

    # 5.3b — low-stakes auto-apply log (Papa Q4 ruling)
    if "survey_autoapply_log" not in existing_tables:
        op.create_table(
            "survey_autoapply_log",
            sa.Column("id",             sa.Integer(), primary_key=True),
            sa.Column("survey_id",      sa.Integer(), sa.ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False),
            sa.Column("field",          sa.String(40), nullable=False),
            sa.Column("old_value",      sa.Text(), nullable=True),
            sa.Column("new_value",      sa.Text(), nullable=False),
            sa.Column("source_kind",    sa.String(20), nullable=False),
            sa.Column("source_url",     sa.Text(), nullable=True),
            sa.Column("source_excerpt", sa.Text(), nullable=True),
            sa.Column("confidence",     sa.Numeric(3, 2), nullable=True),
            sa.Column("applied_at",     sa.TIMESTAMP(), nullable=False, server_default=sa.text("NOW()")),
            sa.Column("reverted_at",    sa.TIMESTAMP(), nullable=True),
            sa.Column("reverted_by",    sa.String(40), nullable=True),
        )

    # 5.4 — coverage retirement candidates
    if "research_idea_coverage_candidates" not in existing_tables:
        op.create_table(
            "research_idea_coverage_candidates",
            sa.Column("id",           sa.Integer(), primary_key=True),
            sa.Column("idea_id",      sa.Integer(), sa.ForeignKey("research_ideas.id", ondelete="CASCADE"), nullable=False),
            sa.Column("arxiv_id",     sa.String(30), nullable=False),
            sa.Column("answers_kind", sa.String(10), nullable=False),
            sa.Column("confidence",   sa.Numeric(3, 2), nullable=False),
            sa.Column("rationale",    sa.Text(), nullable=True),
            sa.Column("status",       sa.String(20), nullable=False, server_default="pending"),
            sa.Column("retire_after", sa.TIMESTAMP(), nullable=True),
            sa.Column("detected_at",  sa.TIMESTAMP(), nullable=False, server_default=sa.text("NOW()")),
            sa.Column("reviewed_at",  sa.TIMESTAMP(), nullable=True),
            sa.Column("reviewed_by",  sa.String(40), nullable=True),
            sa.UniqueConstraint("idea_id", "arxiv_id", name="uq_coverage_candidates"),
        )
        op.create_index("ix_coverage_candidates_status", "research_idea_coverage_candidates", ["status"])

    # 5.5 — surveys orphans (unknown survey tokens from idea generation)
    if "surveys_orphans" not in existing_tables:
        op.create_table(
            "surveys_orphans",
            sa.Column("id",                     sa.Integer(), primary_key=True),
            sa.Column("raw_token",              sa.String(40), nullable=False, unique=True),
            sa.Column("idea_id",                sa.Integer(), sa.ForeignKey("research_ideas.id", ondelete="SET NULL"), nullable=True),
            sa.Column("first_seen_at",          sa.TIMESTAMP(), nullable=False, server_default=sa.text("NOW()")),
            sa.Column("last_seen_at",           sa.TIMESTAMP(), nullable=False, server_default=sa.text("NOW()")),
            sa.Column("occurrence_count",       sa.Integer(), nullable=False, server_default="1"),
            sa.Column("resolved_to_survey_id",  sa.Integer(), sa.ForeignKey("surveys.id", ondelete="SET NULL"), nullable=True),
        )

    # 5.6 — transient claim-match audit (new-survey cross-scan, kept 30 days)
    if "surveys_claim_matches" not in existing_tables:
        op.create_table(
            "surveys_claim_matches",
            sa.Column("id",         sa.Integer(), primary_key=True),
            sa.Column("survey_id",  sa.Integer(), sa.ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False),
            sa.Column("claim_id",   sa.Integer(), sa.ForeignKey("claims.id", ondelete="CASCADE"), nullable=False),
            sa.Column("score",      sa.Numeric(3, 2), nullable=False),
            sa.Column("matched_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("NOW()")),
            sa.UniqueConstraint("survey_id", "claim_id", name="uq_surveys_claim_matches"),
        )


def downgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_tables = set(insp.get_table_names())

    for tbl in ("surveys_claim_matches", "surveys_orphans", "research_idea_coverage_candidates",
                "survey_autoapply_log", "survey_update_proposals", "research_idea_refresh_log"):
        if tbl in existing_tables:
            op.drop_table(tbl)

    for col in ("promoted_at", "promoted_by", "last_refreshed_at", "refresh_count",
                "covered_by_arxiv_id", "covered_at", "covered_confidence"):
        op.execute(f"ALTER TABLE research_ideas DROP COLUMN IF EXISTS {col}")

    op.execute("DROP INDEX IF EXISTS ix_research_ideas_status_created")
    op.execute("DROP INDEX IF EXISTS ix_research_ideas_last_refreshed")
