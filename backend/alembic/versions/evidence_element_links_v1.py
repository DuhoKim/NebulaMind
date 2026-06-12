"""Element-scoped evidence links for arXiv wiki feed v2.

Revision ID: evidence_element_links_v1
Revises: candidate_grounded_atom_coverage_v1, retrieval_filter_element_rows_v1
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "evidence_element_links_v1"
down_revision = ("candidate_grounded_atom_coverage_v1", "retrieval_filter_element_rows_v1")
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "evidence_element_links",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("evidence_id", sa.Integer(), sa.ForeignKey("evidence.id"), nullable=False),
        sa.Column("source_claim_id", sa.Integer(), sa.ForeignKey("claims.id"), nullable=False),
        sa.Column("target_claim_id", sa.Integer(), sa.ForeignKey("claims.id"), nullable=False),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id"), nullable=False),
        sa.Column("page_slug", sa.Text(), nullable=False),
        sa.Column("element_id", sa.Text(), nullable=False),
        sa.Column("element_text_snapshot", sa.Text(), nullable=True),
        sa.Column("arxiv_id", sa.String(30), nullable=False),
        sa.Column("candidate_key", sa.Text(), nullable=True),
        sa.Column("validator_run_key", sa.Text(), nullable=True),
        sa.Column("promotion_run_id", sa.Integer(), sa.ForeignKey("arxiv_wiki_feed_runs.id"), nullable=True),
        sa.Column("rewrite_resolution_status", sa.Text(), nullable=False),
        sa.Column("rewrite_resolution_reason", sa.Text(), nullable=True),
        sa.Column(
            "provenance",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
            server_default=sa.text("'{}'::jsonb"),
        ),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.UniqueConstraint(
            "target_claim_id",
            "element_id",
            "arxiv_id",
            name="uq_evidence_element_links_target_element_arxiv",
        ),
    )
    op.create_index("idx_evidence_element_links_evidence", "evidence_element_links", ["evidence_id"])
    op.create_index("idx_evidence_element_links_source_claim", "evidence_element_links", ["source_claim_id"])
    op.create_index("idx_evidence_element_links_target_claim", "evidence_element_links", ["target_claim_id"])
    op.create_index("idx_evidence_element_links_candidate_key", "evidence_element_links", ["candidate_key"])

    op.add_column("arxiv_wiki_evidence_candidates", sa.Column("element_id", sa.Text(), nullable=True))
    op.add_column("arxiv_wiki_evidence_candidates", sa.Column("element_text_snapshot", sa.Text(), nullable=True))
    op.add_column("arxiv_wiki_evidence_candidates", sa.Column("source_claim_id", sa.Integer(), nullable=True))
    op.add_column("arxiv_wiki_evidence_candidates", sa.Column("target_claim_id", sa.Integer(), nullable=True))
    op.add_column("arxiv_wiki_evidence_candidates", sa.Column("rewrite_resolution_status", sa.Text(), nullable=True))
    op.add_column("arxiv_wiki_evidence_candidates", sa.Column("rewrite_resolution_reason", sa.Text(), nullable=True))
    op.create_foreign_key(
        "fk_arxiv_wiki_candidates_source_claim",
        "arxiv_wiki_evidence_candidates",
        "claims",
        ["source_claim_id"],
        ["id"],
    )
    op.create_foreign_key(
        "fk_arxiv_wiki_candidates_target_claim",
        "arxiv_wiki_evidence_candidates",
        "claims",
        ["target_claim_id"],
        ["id"],
    )


def downgrade():
    op.drop_constraint("fk_arxiv_wiki_candidates_target_claim", "arxiv_wiki_evidence_candidates", type_="foreignkey")
    op.drop_constraint("fk_arxiv_wiki_candidates_source_claim", "arxiv_wiki_evidence_candidates", type_="foreignkey")
    op.drop_column("arxiv_wiki_evidence_candidates", "rewrite_resolution_reason")
    op.drop_column("arxiv_wiki_evidence_candidates", "rewrite_resolution_status")
    op.drop_column("arxiv_wiki_evidence_candidates", "target_claim_id")
    op.drop_column("arxiv_wiki_evidence_candidates", "source_claim_id")
    op.drop_column("arxiv_wiki_evidence_candidates", "element_text_snapshot")
    op.drop_column("arxiv_wiki_evidence_candidates", "element_id")

    op.drop_index("idx_evidence_element_links_candidate_key", table_name="evidence_element_links")
    op.drop_index("idx_evidence_element_links_target_claim", table_name="evidence_element_links")
    op.drop_index("idx_evidence_element_links_source_claim", table_name="evidence_element_links")
    op.drop_index("idx_evidence_element_links_evidence", table_name="evidence_element_links")
    op.drop_table("evidence_element_links")
