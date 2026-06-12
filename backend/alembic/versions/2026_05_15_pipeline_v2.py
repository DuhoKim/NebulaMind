"""pipeline v2 — 5 new quality-signal tables (K2/X4/Mima/Tera/Takji)

Revision ID: pipeline_v2_2026_05_15
Revises: autowiki_idea_signals_v1
Create Date: 2026-05-15
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "pipeline_v2_2026_05_15"
down_revision = "autowiki_idea_signals_v1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "claim_migration_proposals",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("claim_id", sa.Integer, sa.ForeignKey("claims.id", ondelete="CASCADE"), nullable=False),
        sa.Column("target_page_id", sa.Integer, sa.ForeignKey("wiki_pages.id", ondelete="CASCADE"), nullable=False),
        sa.Column("rationale", sa.Text, nullable=False),
        sa.Column("proposer_model", sa.String(80), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=False), server_default=sa.text("NOW()"), nullable=False),
        sa.Column("status", sa.String(20), server_default="pending", nullable=False),
    )
    op.create_index("ix_claim_migration_proposals_claim_id", "claim_migration_proposals", ["claim_id"])
    op.create_index("ix_claim_migration_proposals_target_page_id", "claim_migration_proposals", ["target_page_id"])

    op.create_table(
        "evidence_mismatches",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("evidence_link_id", sa.Integer, sa.ForeignKey("evidence.id", ondelete="CASCADE"), nullable=False),
        sa.Column("mismatch_reason", sa.Text, nullable=False),
        sa.Column("detected_by_model", sa.String(80), nullable=True),
        sa.Column("detected_at", sa.DateTime(timezone=False), server_default=sa.text("NOW()"), nullable=False),
        sa.Column("resolved_at", sa.DateTime(timezone=False), nullable=True),
    )
    op.create_index("ix_evidence_mismatches_evidence_link_id", "evidence_mismatches", ["evidence_link_id"])

    op.create_table(
        "schema_violations",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("table_name", sa.String(80), nullable=False),
        sa.Column("row_id", sa.Integer, nullable=False),
        sa.Column("violation_kind", sa.String(120), nullable=False),
        sa.Column("auto_fixed", sa.Boolean, server_default="false", nullable=False),
        sa.Column("flagged_for_hwao", sa.Boolean, server_default="false", nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=False), server_default=sa.text("NOW()"), nullable=False),
    )

    op.create_table(
        "coverage_reports",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("page_id", sa.Integer, sa.ForeignKey("wiki_pages.id", ondelete="CASCADE"), nullable=False),
        sa.Column("generated_at", sa.DateTime(timezone=False), server_default=sa.text("NOW()"), nullable=False),
        sa.Column("generator_model", sa.String(80), nullable=True),
        sa.Column("missing_subtopics_jsonb", JSONB, nullable=True),
        sa.Column("split_merge_suggestions_jsonb", JSONB, nullable=True),
        sa.Column("orphan_section_flags_jsonb", JSONB, nullable=True),
    )
    op.create_index("ix_coverage_reports_page_id", "coverage_reports", ["page_id"])

    op.create_table(
        "claim_decay_candidates",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("claim_id", sa.Integer, sa.ForeignKey("claims.id", ondelete="CASCADE"), nullable=False, unique=True),
        sa.Column("decay_score", sa.Float, nullable=False),
        sa.Column("flagged_at", sa.DateTime(timezone=False), server_default=sa.text("NOW()"), nullable=False),
        sa.Column("flagged_by_model", sa.String(80), nullable=True),
        sa.Column("status", sa.String(20), server_default="pending", nullable=False),
    )
    op.create_index("ix_claim_decay_candidates_claim_id", "claim_decay_candidates", ["claim_id"])


def downgrade() -> None:
    op.drop_table("claim_decay_candidates")
    op.drop_table("coverage_reports")
    op.drop_table("schema_violations")
    op.drop_table("evidence_mismatches")
    op.drop_table("claim_migration_proposals")
