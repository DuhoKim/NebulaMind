"""claim_marker_runs table for marker-embed pipeline audit log

Revision ID: claim_marker_runs_v1
Revises: arxiv_phase_d_v1
Create Date: 2026-05-20
"""
from alembic import op
import sqlalchemy as sa

revision = "claim_marker_runs_v1"
down_revision = "arxiv_phase_d_v1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "claim_marker_runs",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("page_id", sa.Integer, sa.ForeignKey("wiki_pages.id", ondelete="CASCADE"), nullable=False),
        sa.Column("page_version", sa.Integer, nullable=True),
        sa.Column("source_version", sa.Integer, nullable=True),
        sa.Column("total_claims", sa.Integer, nullable=True),
        sa.Column("matched_claims", sa.Integer, nullable=True),
        sa.Column("rejected_low_confidence", sa.Integer, nullable=True),
        sa.Column("rejected_no_section", sa.Integer, nullable=True),
        sa.Column("rejected_ambiguous_span", sa.Integer, nullable=True),
        sa.Column("rejected_validation", sa.Integer, nullable=True),
        sa.Column("mean_confidence", sa.Float, nullable=True),
        sa.Column("judge_agreement_pct", sa.Float, nullable=True),
        sa.Column("coverage_pct", sa.Float, nullable=True),
        sa.Column("status", sa.String(32), nullable=True),
        sa.Column("run_started_at", sa.DateTime(timezone=False), nullable=True),
        sa.Column("run_finished_at", sa.DateTime(timezone=False), nullable=True),
        sa.Column("notes", sa.Text, nullable=True),
    )
    op.create_index("ix_claim_marker_runs_page_id", "claim_marker_runs", ["page_id"])


def downgrade() -> None:
    op.drop_index("ix_claim_marker_runs_page_id", "claim_marker_runs")
    op.drop_table("claim_marker_runs")
