"""intro synthesis v2 pilot schema

Revision ID: intro_synthesis_v2_ab_fold
Revises: pipeline_runs_schedule_name_widen_v1
"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "intro_synthesis_v2_ab_fold"
down_revision = "pipeline_runs_schedule_name_widen_v1"
branch_labels = None
depends_on = None


TRUST_LEVELS = "'consensus', 'accepted', 'debated', 'challenged', 'unverified', 'reported'"


def upgrade() -> None:
    op.create_table(
        "algorithms",
        sa.Column("algorithm_id", sa.Text(), primary_key=True),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("version", sa.Text(), nullable=False),
        sa.Column("method_prose", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
    )

    op.add_column("wiki_pages", sa.Column("algorithm_id", sa.Text(), nullable=True))
    op.create_foreign_key(
        "fk_wiki_pages_algorithm_id",
        "wiki_pages",
        "algorithms",
        ["algorithm_id"],
        ["algorithm_id"],
    )
    op.create_index("ix_wiki_pages_algorithm_id", "wiki_pages", ["algorithm_id"])

    op.create_table(
        "sentence_provenance",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id", ondelete="CASCADE"), nullable=False),
        sa.Column("page_version_id", sa.Integer(), sa.ForeignKey("page_versions.id", ondelete="CASCADE"), nullable=True),
        sa.Column("sentence_index", sa.Integer(), nullable=False),
        sa.Column("sentence_hash", sa.Text(), nullable=False),
        sa.Column("tier", sa.Integer(), nullable=False),
        sa.Column("relationship", sa.Text(), nullable=False),
        sa.Column("parent_sentence_provenance_id", sa.Integer(), sa.ForeignKey("sentence_provenance.id"), nullable=True),
        sa.Column("arxiv_id", sa.Text(), nullable=True),
        sa.Column(
            "source_span_ids",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
            server_default=sa.text("'[]'::jsonb"),
        ),
        sa.Column("source_span_id_primary", sa.Text(), nullable=True),
        sa.Column("tone_tier", sa.Text(), nullable=True),
        sa.Column("tone_tier_4", sa.Text(), nullable=True),
        sa.Column("source_span", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("match_method", sa.Text(), nullable=False, server_default="unresolved"),
        sa.Column("match_confidence", sa.Double(), nullable=True),
        sa.Column("resolved", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("tier IN (1, 2)", name="ck_sentence_provenance_tier"),
        sa.CheckConstraint("relationship IN ('source_of', 'cited_by_source')", name="ck_sentence_provenance_relationship"),
        sa.CheckConstraint(
            "tone_tier IS NULL OR tone_tier IN ('settled', 'contested')",
            name="ck_sentence_provenance_tone_tier_live",
        ),
        sa.CheckConstraint(
            f"tone_tier_4 IS NULL OR tone_tier_4 IN ({TRUST_LEVELS})",
            name="ck_sentence_provenance_tone_tier_4",
        ),
    )
    op.create_index("ix_sentence_provenance_page_version", "sentence_provenance", ["page_version_id", "sentence_index"])
    op.create_index("ix_sentence_provenance_sentence_hash", "sentence_provenance", ["sentence_hash"])
    op.create_index("ix_sentence_provenance_page", "sentence_provenance", ["page_id"])
    op.create_index("ix_sentence_provenance_arxiv", "sentence_provenance", ["arxiv_id"])

    op.create_table(
        "sentence_trust",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("page_version_id", sa.Integer(), sa.ForeignKey("page_versions.id", ondelete="CASCADE"), nullable=False),
        sa.Column("sentence_index", sa.Integer(), nullable=False),
        sa.Column("sentence_hash", sa.Text(), nullable=False),
        sa.Column("tone_tier", sa.Text(), nullable=False),
        sa.Column("vote_count", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("settled_votes", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("contested_votes", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("settled_share", sa.Double(), nullable=False, server_default="0"),
        sa.Column("trust_score", sa.Double(), nullable=False),
        sa.Column("trust_level", sa.Text(), nullable=False),
        sa.Column("single_source", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("contested_veto", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("tier2_density", sa.Double(), nullable=False, server_default="0"),
        sa.Column("tone_distribution", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default=sa.text("'{}'::jsonb")),
        sa.Column("tone_distribution_4", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("tone_tier IN ('settled', 'contested', 'mixed')", name="ck_sentence_trust_tone_tier"),
        sa.CheckConstraint(
            f"trust_level IN ({TRUST_LEVELS})",
            name="ck_sentence_trust_level",
        ),
        sa.UniqueConstraint("page_version_id", "sentence_index", name="uq_sentence_trust_page_version_sentence"),
    )
    op.create_index("ix_sentence_trust_sentence_hash", "sentence_trust", ["sentence_hash"])


def downgrade() -> None:
    op.drop_index("ix_sentence_trust_sentence_hash", table_name="sentence_trust")
    op.drop_table("sentence_trust")
    op.drop_index("ix_sentence_provenance_arxiv", table_name="sentence_provenance")
    op.drop_index("ix_sentence_provenance_page", table_name="sentence_provenance")
    op.drop_index("ix_sentence_provenance_sentence_hash", table_name="sentence_provenance")
    op.drop_index("ix_sentence_provenance_page_version", table_name="sentence_provenance")
    op.drop_table("sentence_provenance")
    op.drop_index("ix_wiki_pages_algorithm_id", table_name="wiki_pages")
    op.drop_constraint("fk_wiki_pages_algorithm_id", "wiki_pages", type_="foreignkey")
    op.drop_column("wiki_pages", "algorithm_id")
    op.drop_table("algorithms")
