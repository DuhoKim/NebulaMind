"""First-class coverage materialization rows for arXiv wiki feed v2.

Revision ID: arxiv_wiki_feed_coverage_materialization_v1
Revises: evidence_element_links_v1
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "arxiv_wiki_feed_coverage_materialization_v1"
down_revision = "evidence_element_links_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "arxiv_wiki_feed_coverage_rows",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("run_id", sa.Integer(), sa.ForeignKey("arxiv_wiki_feed_runs.id"), nullable=False),
        sa.Column("retrieval_filter_row_id", sa.Integer(), sa.ForeignKey("retrieval_filter_element_rows.id"), nullable=True),
        sa.Column("claim_id", sa.Integer(), sa.ForeignKey("claims.id"), nullable=False),
        sa.Column("element_id", sa.Text(), nullable=False),
        sa.Column("arxiv_paper_id", sa.Integer(), sa.ForeignKey("arxiv_papers.id"), nullable=True),
        sa.Column("arxiv_id", sa.String(30), nullable=False),
        sa.Column("candidate_key", sa.Text(), nullable=True),
        sa.Column("coverage_status", sa.Text(), nullable=False, server_default="coverage_pending"),
        sa.Column(
            "coverage_required_stages",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
            server_default=sa.text("'[]'::jsonb"),
        ),
        sa.Column(
            "coverage_missing_stages",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
            server_default=sa.text("'[]'::jsonb"),
        ),
        sa.Column(
            "coverage_stage_statuses",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
            server_default=sa.text("'{}'::jsonb"),
        ),
        sa.Column(
            "coverage_artifact_refs",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
            server_default=sa.text("'{}'::jsonb"),
        ),
        sa.Column(
            "source_hashes",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
            server_default=sa.text("'{}'::jsonb"),
        ),
        sa.Column("hydration_policy", sa.Text(), nullable=False, server_default="artifact_only_fail_closed"),
        sa.Column("hydration_db_reads_used", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("materializer_prompt_version", sa.Text(), nullable=False),
        sa.Column("materializer_model_version", sa.Text(), nullable=False),
        sa.Column("materialized_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.CheckConstraint(
            "coverage_status IN ('coverage_pending', 'coverage_ready', 'blocked_retryable', 'blocked_terminal')",
            name="ck_arxiv_wiki_feed_coverage_rows_status",
        ),
        sa.CheckConstraint(
            "hydration_db_reads_used = false",
            name="ck_arxiv_wiki_feed_coverage_rows_no_db_hydration",
        ),
        sa.UniqueConstraint(
            "run_id",
            "element_id",
            "arxiv_id",
            name="uq_arxiv_wiki_feed_coverage_rows_run_element_arxiv",
        ),
    )
    op.create_index(
        "idx_arxiv_wiki_feed_coverage_rows_run_status",
        "arxiv_wiki_feed_coverage_rows",
        ["run_id", "coverage_status"],
    )
    op.create_index(
        "idx_arxiv_wiki_feed_coverage_rows_claim_paper",
        "arxiv_wiki_feed_coverage_rows",
        ["claim_id", "arxiv_id"],
    )
    op.create_index(
        "idx_arxiv_wiki_feed_coverage_rows_retrieval_row",
        "arxiv_wiki_feed_coverage_rows",
        ["retrieval_filter_row_id"],
    )


def downgrade():
    op.drop_index("idx_arxiv_wiki_feed_coverage_rows_retrieval_row", table_name="arxiv_wiki_feed_coverage_rows")
    op.drop_index("idx_arxiv_wiki_feed_coverage_rows_claim_paper", table_name="arxiv_wiki_feed_coverage_rows")
    op.drop_index("idx_arxiv_wiki_feed_coverage_rows_run_status", table_name="arxiv_wiki_feed_coverage_rows")
    op.drop_table("arxiv_wiki_feed_coverage_rows")
