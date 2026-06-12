"""Autowiki loop — runs audit table + targets table

Revision ID: autowiki_v1
Revises: wiki_renovation_v1
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "autowiki_v1"
down_revision = "wiki_renovation_v1"
branch_labels = None
depends_on = None


def upgrade():
    # --- autowiki_runs (§4.3 full schema) ---
    op.create_table(
        "autowiki_runs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id"), nullable=False),
        sa.Column("started_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("finished_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("proposal_type", sa.String(40), nullable=True),
        sa.Column("model_proposer", sa.String(80), nullable=True),
        sa.Column("model_judge", sa.String(80), nullable=True),
        # structural
        sa.Column("h0_struct", sa.Float(), nullable=True),
        sa.Column("h1_struct", sa.Float(), nullable=True),
        sa.Column("components_before", JSONB(), nullable=True),
        sa.Column("components_after", JSONB(), nullable=True),
        # utility (LLM-judged)
        sa.Column("u0_median", sa.Float(), nullable=True),
        sa.Column("u1_median", sa.Float(), nullable=True),
        sa.Column("u0_runs", JSONB(), nullable=True),   # list of 3 raw rubric dicts
        sa.Column("u1_runs", JSONB(), nullable=True),
        sa.Column("judge_rationale", sa.Text(), nullable=True),
        sa.Column("judge_prompt_version", sa.String(20), nullable=True),
        # composite + decision
        sa.Column("q0", sa.Float(), nullable=True),
        sa.Column("q1", sa.Float(), nullable=True),
        sa.Column("delta_q", sa.Float(), nullable=True),
        sa.Column(
            "decision", sa.String(20), nullable=True
        ),  # commit|rollback|skip|gate_reject|guard_reject|error
        sa.Column("reject_reason", sa.Text(), nullable=True),
        sa.Column(
            "committed_version_id",
            sa.Integer(),
            sa.ForeignKey("page_versions.id"),
            nullable=True,
        ),
        # observability
        sa.Column("latency_ms_breakdown", JSONB(), nullable=True),
        sa.Column("error_text", sa.Text(), nullable=True),
    )
    op.create_index("idx_autowiki_runs_page_time", "autowiki_runs", ["page_id", "started_at"])
    op.create_index("idx_autowiki_runs_decision", "autowiki_runs", ["decision"])

    # --- autowiki_targets ---
    op.create_table(
        "autowiki_targets",
        sa.Column(
            "page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id"), primary_key=True
        ),
        sa.Column("target_q", sa.Float(), nullable=False, server_default="0.78"),
        sa.Column("last_raised_at", sa.TIMESTAMP(), nullable=True),
    )

    # Seed row: galaxy-evolution (id=57)
    op.execute(
        "INSERT INTO autowiki_targets (page_id, target_q) VALUES (57, 0.78) "
        "ON CONFLICT DO NOTHING"
    )


def downgrade():
    op.drop_table("autowiki_targets")
    op.drop_index("idx_autowiki_runs_decision", "autowiki_runs")
    op.drop_index("idx_autowiki_runs_page_time", "autowiki_runs")
    op.drop_table("autowiki_runs")
