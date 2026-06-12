"""Arxiv wiki feed v1 shadow tables.

Revision ID: arxiv_wiki_feed_shadow_v1
Revises: merge_marker_and_news_v1
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "arxiv_wiki_feed_shadow_v1"
down_revision = "merge_marker_and_news_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "arxiv_wiki_feed_runs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("run_key", sa.Text(), nullable=False),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id"), nullable=True),
        sa.Column("page_slug", sa.Text(), nullable=True),
        sa.Column("run_scope", sa.Text(), nullable=False),
        sa.Column("paper_query", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("candidate_params", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("validator_params", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("status", sa.Text(), nullable=False, server_default="started"),
        sa.Column("started_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("finished_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("created_by", sa.Text(), nullable=False, server_default="tori"),
        sa.Column("code_version", sa.Text(), nullable=False),
        sa.Column("report_path", sa.Text(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
    )
    op.create_unique_constraint("uq_arxiv_wiki_feed_runs_run_key", "arxiv_wiki_feed_runs", ["run_key"])
    op.create_index("idx_arxiv_wiki_feed_runs_page_started", "arxiv_wiki_feed_runs", ["page_slug", "started_at"])
    op.create_index("idx_arxiv_wiki_feed_runs_status", "arxiv_wiki_feed_runs", ["status"])

    op.create_table(
        "arxiv_wiki_evidence_candidates",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("run_id", sa.Integer(), sa.ForeignKey("arxiv_wiki_feed_runs.id"), nullable=False),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id"), nullable=False),
        sa.Column("page_slug", sa.Text(), nullable=False),
        sa.Column("claim_id", sa.Integer(), sa.ForeignKey("claims.id"), nullable=False),
        sa.Column("claim_text_snapshot", sa.Text(), nullable=False),
        sa.Column("claim_section_snapshot", sa.Text(), nullable=True),
        sa.Column("arxiv_paper_id", sa.Integer(), sa.ForeignKey("arxiv_papers.id"), nullable=False),
        sa.Column("arxiv_id", sa.String(30), nullable=False),
        sa.Column("paper_title_snapshot", sa.Text(), nullable=False),
        sa.Column("paper_abstract_snapshot", sa.Text(), nullable=False),
        sa.Column("paper_authors_snapshot", sa.Text(), nullable=True),
        sa.Column("paper_year", sa.Integer(), nullable=True),
        sa.Column("paper_url", sa.Text(), nullable=True),
        sa.Column("candidate_rank", sa.Integer(), nullable=False),
        sa.Column("bm25_score", sa.Double(), nullable=False),
        sa.Column("tfidf_score", sa.Double(), nullable=True),
        sa.Column("claim_key_overlap", sa.Double(), nullable=False),
        sa.Column("matched_terms", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default=sa.text("'[]'::jsonb")),
        sa.Column("candidate_source", sa.Text(), nullable=False),
        sa.Column("status", sa.Text(), nullable=False, server_default="shadow_proposed"),
        sa.Column("validator_label", sa.Text(), nullable=True),
        sa.Column("validator_score", sa.Double(), nullable=True),
        sa.Column("validator_agreement", sa.Double(), nullable=True),
        sa.Column("validator_model_set", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("evidence_stance", sa.Text(), nullable=True),
        sa.Column("evidence_summary", sa.Text(), nullable=True),
        sa.Column("quality", sa.Double(), nullable=True),
        sa.Column("duplicate_evidence_id", sa.Integer(), sa.ForeignKey("evidence.id"), nullable=True),
        sa.Column("promoted_evidence_id", sa.Integer(), nullable=True),
        sa.Column("promotion_batch_id", sa.Text(), nullable=True),
        sa.Column("promotion_gate", sa.Text(), nullable=True),
        sa.Column("promoted_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("rollback_reason", sa.Text(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
    )
    op.create_unique_constraint(
        "uq_arxiv_wiki_candidates_run_claim_arxiv",
        "arxiv_wiki_evidence_candidates",
        ["run_id", "claim_id", "arxiv_id"],
    )
    op.create_index("idx_arxiv_wiki_candidates_page_status", "arxiv_wiki_evidence_candidates", ["page_id", "status"])
    op.create_index("idx_arxiv_wiki_candidates_claim_status", "arxiv_wiki_evidence_candidates", ["claim_id", "status"])
    op.create_index("idx_arxiv_wiki_candidates_arxiv_status", "arxiv_wiki_evidence_candidates", ["arxiv_id", "status"])
    op.create_index(
        "uq_arxiv_wiki_candidates_live_claim_arxiv",
        "arxiv_wiki_evidence_candidates",
        ["claim_id", "arxiv_id"],
        unique=True,
        postgresql_where=sa.text("status in ('validated_ready','promoted')"),
    )

    op.create_table(
        "arxiv_wiki_evidence_validations",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("candidate_id", sa.Integer(), sa.ForeignKey("arxiv_wiki_evidence_candidates.id"), nullable=False),
        sa.Column("run_id", sa.Integer(), sa.ForeignKey("arxiv_wiki_feed_runs.id"), nullable=False),
        sa.Column("model_name", sa.Text(), nullable=False),
        sa.Column("host", sa.Text(), nullable=False),
        sa.Column("prompt_version", sa.Text(), nullable=False),
        sa.Column("label", sa.Text(), nullable=False),
        sa.Column("stance", sa.Text(), nullable=True),
        sa.Column("score", sa.Double(), nullable=False),
        sa.Column("claim_key_overlap_seen", sa.Double(), nullable=True),
        sa.Column("rationale", sa.Text(), nullable=True),
        sa.Column("quoted_evidence_span", sa.Text(), nullable=True),
        sa.Column("failure_mode", sa.Text(), nullable=True),
        sa.Column("raw_response_path", sa.Text(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("idx_arxiv_wiki_validations_candidate_model", "arxiv_wiki_evidence_validations", ["candidate_id", "model_name"])
    op.create_index("idx_arxiv_wiki_validations_run_label", "arxiv_wiki_evidence_validations", ["run_id", "label"])


def downgrade():
    op.drop_index("idx_arxiv_wiki_validations_run_label", table_name="arxiv_wiki_evidence_validations")
    op.drop_index("idx_arxiv_wiki_validations_candidate_model", table_name="arxiv_wiki_evidence_validations")
    op.drop_table("arxiv_wiki_evidence_validations")

    op.drop_index("uq_arxiv_wiki_candidates_live_claim_arxiv", table_name="arxiv_wiki_evidence_candidates")
    op.drop_index("idx_arxiv_wiki_candidates_arxiv_status", table_name="arxiv_wiki_evidence_candidates")
    op.drop_index("idx_arxiv_wiki_candidates_claim_status", table_name="arxiv_wiki_evidence_candidates")
    op.drop_index("idx_arxiv_wiki_candidates_page_status", table_name="arxiv_wiki_evidence_candidates")
    op.drop_constraint("uq_arxiv_wiki_candidates_run_claim_arxiv", "arxiv_wiki_evidence_candidates", type_="unique")
    op.drop_table("arxiv_wiki_evidence_candidates")

    op.drop_index("idx_arxiv_wiki_feed_runs_status", table_name="arxiv_wiki_feed_runs")
    op.drop_index("idx_arxiv_wiki_feed_runs_page_started", table_name="arxiv_wiki_feed_runs")
    op.drop_constraint("uq_arxiv_wiki_feed_runs_run_key", "arxiv_wiki_feed_runs", type_="unique")
    op.drop_table("arxiv_wiki_feed_runs")
