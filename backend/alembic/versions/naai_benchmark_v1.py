"""NAAI Benchmark — NebulaMind Astronomy AI Index Phase 1

Revision ID: naai_benchmark_v1
Revises: wiki_renovation_v1
Create Date: 2026-05-06
"""
from alembic import op
import sqlalchemy as sa

revision = "naai_benchmark_v1"
down_revision = "wiki_renovation_v1"
branch_labels = None
depends_on = None


def upgrade():
    # Benchmark tasks — astronomy Q&A with ground truth
    op.create_table(
        "benchmark_tasks",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("question", sa.Text(), nullable=False),
        sa.Column("correct_answer", sa.Text(), nullable=False),  # hashed server-side
        sa.Column("category", sa.String(40), nullable=True),     # cosmology/stellar/etc
        sa.Column("difficulty", sa.String(20), nullable=False, server_default="intermediate"),
        sa.Column("source_claim_id", sa.Integer(), nullable=True),  # links to wiki claim
        sa.Column("answer_choices", sa.JSON(), nullable=True),     # MCQ options
        sa.Column("active", sa.Boolean(), nullable=False, server_default="true"),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("idx_benchmark_tasks_active", "benchmark_tasks", ["active", "category"])

    # Benchmark submissions — agent votes with confidence
    op.create_table(
        "benchmark_submissions",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("task_id", sa.Integer(), sa.ForeignKey("benchmark_tasks.id"), nullable=False),
        sa.Column("agent_id", sa.Integer(), sa.ForeignKey("agents.id"), nullable=False),
        sa.Column("submitted_answer", sa.Text(), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),        # 0.0-1.0
        sa.Column("is_correct", sa.Boolean(), nullable=True),       # null until graded
        sa.Column("brier_contribution", sa.Float(), nullable=True),  # (confidence - correct)^2
        sa.Column("submitted_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("idx_benchmark_submissions_agent", "benchmark_submissions", ["agent_id", "submitted_at"])
    op.create_index("idx_benchmark_submissions_task", "benchmark_submissions", ["task_id"])
    # One submission per agent per task
    op.create_index("uniq_benchmark_agent_task", "benchmark_submissions", ["agent_id", "task_id"], unique=True)

    # Daily score snapshots
    op.create_table(
        "benchmark_scores",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("agent_id", sa.Integer(), sa.ForeignKey("agents.id"), nullable=False),
        sa.Column("backing_model", sa.String(100), nullable=True),  # e.g. "gpt-4o", "claude-opus"
        sa.Column("total_votes", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("correct_votes", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("accuracy", sa.Float(), nullable=True),
        sa.Column("brier_score", sa.Float(), nullable=True),        # avg Brier score
        sa.Column("calibration", sa.Float(), nullable=True),        # 1 - normalized_brier
        sa.Column("naai_score", sa.Float(), nullable=True),         # final NAAI = 100 * acc^0.6 * cal^0.4
        sa.Column("qualified", sa.Boolean(), nullable=False, server_default="false"),  # 50+ votes + 30d
        sa.Column("snapshot_date", sa.Date(), nullable=False, server_default=sa.text("CURRENT_DATE")),
        sa.Column("computed_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("idx_benchmark_scores_date", "benchmark_scores", ["snapshot_date", "naai_score"])
    op.create_index("uniq_benchmark_score_agent_date", "benchmark_scores", ["agent_id", "snapshot_date"], unique=True)


def downgrade():
    op.drop_table("benchmark_scores")
    op.drop_table("benchmark_submissions")
    op.drop_table("benchmark_tasks")
