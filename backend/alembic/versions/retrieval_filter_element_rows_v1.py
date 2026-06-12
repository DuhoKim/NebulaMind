"""Element-level retrieval filter rows.

Revision ID: retrieval_filter_element_rows_v1
Revises: rewrite_status_claims_v1
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "retrieval_filter_element_rows_v1"
down_revision = "rewrite_status_claims_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "retrieval_filter_element_rows",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("run_id", sa.Integer(), sa.ForeignKey("arxiv_wiki_feed_runs.id"), nullable=False),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id"), nullable=False),
        sa.Column("page_slug", sa.Text(), nullable=False),
        sa.Column("section", sa.Text(), nullable=False),
        sa.Column("claim_id", sa.Integer(), sa.ForeignKey("claims.id"), nullable=False),
        sa.Column("element_id", sa.Text(), nullable=False),
        sa.Column("arxiv_paper_id", sa.Integer(), sa.ForeignKey("arxiv_papers.id"), nullable=True),
        sa.Column("arxiv_id", sa.String(30), nullable=False),
        sa.Column("retrieval_filter_version", sa.Text(), nullable=False),
        sa.Column("retrieval_filter_decision", sa.Text(), nullable=False),
        sa.Column("boundary_review_reason", sa.Text(), nullable=True),
        sa.Column("boundary_review_policy", sa.Text(), nullable=True),
        sa.Column(
            "boundary_review_features",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
            server_default=sa.text("'{}'::jsonb"),
        ),
        sa.Column("would_be_promotion_authority", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("retrieval_routes_to_validator", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("validator_status", sa.Text(), nullable=False, server_default="pending"),
        sa.Column("validator_priority", sa.Integer(), nullable=False, server_default="100"),
        sa.Column("label", sa.Text(), nullable=True),
        sa.Column("final_score", sa.Double(), nullable=True),
        sa.Column("combined_score", sa.Double(), nullable=True),
        sa.Column("context_score", sa.Double(), nullable=True),
        sa.Column("positive_score", sa.Double(), nullable=True),
        sa.Column("tags", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default=sa.text("'[]'::jsonb")),
        sa.Column(
            "drop_reasons",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
            server_default=sa.text("'[]'::jsonb"),
        ),
        sa.Column("row_payload", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.CheckConstraint(
            "retrieval_filter_decision IN ('keep', 'drop', 'downrank', 'boundary_review_keep')",
            name="ck_retrieval_filter_element_rows_decision",
        ),
        sa.CheckConstraint(
            "would_be_promotion_authority = false",
            name="ck_retrieval_filter_element_rows_no_promotion_authority",
        ),
        sa.UniqueConstraint("run_id", "section", "element_id", "arxiv_id", name="uq_retrieval_filter_element_rows_grain"),
    )
    op.create_index(
        "idx_retrieval_filter_element_rows_brk_queue",
        "retrieval_filter_element_rows",
        ["run_id", "validator_status", "created_at"],
        postgresql_where=sa.text("retrieval_filter_decision = 'boundary_review_keep'"),
    )
    op.create_index(
        "idx_retrieval_filter_element_rows_validator_queue",
        "retrieval_filter_element_rows",
        ["run_id", "retrieval_routes_to_validator", "validator_status"],
    )
    op.create_index(
        "idx_retrieval_filter_element_rows_section_decision",
        "retrieval_filter_element_rows",
        ["run_id", "section", "retrieval_filter_decision"],
    )
    op.create_index(
        "idx_retrieval_filter_element_rows_claim_paper",
        "retrieval_filter_element_rows",
        ["claim_id", "arxiv_id"],
    )
    op.create_index(
        "idx_retrieval_filter_element_rows_page_decision",
        "retrieval_filter_element_rows",
        ["page_id", "retrieval_filter_decision"],
    )


def downgrade():
    op.drop_index("idx_retrieval_filter_element_rows_page_decision", table_name="retrieval_filter_element_rows")
    op.drop_index("idx_retrieval_filter_element_rows_claim_paper", table_name="retrieval_filter_element_rows")
    op.drop_index("idx_retrieval_filter_element_rows_section_decision", table_name="retrieval_filter_element_rows")
    op.drop_index("idx_retrieval_filter_element_rows_validator_queue", table_name="retrieval_filter_element_rows")
    op.drop_index("idx_retrieval_filter_element_rows_brk_queue", table_name="retrieval_filter_element_rows")
    op.drop_table("retrieval_filter_element_rows")
