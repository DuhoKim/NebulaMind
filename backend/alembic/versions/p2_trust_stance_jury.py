"""Trust Phase 2: Stance Jury + Adversarial Pass columns and indexes

Revision ID: p2trust1
Revises: q3_summary_src
Create Date: 2026-05-03
"""
from alembic import op
import sqlalchemy as sa

revision = "p2trust1"
down_revision = "q3_summary_src"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("claims", sa.Column("last_adversarial_probe_at", sa.TIMESTAMP(), nullable=True))
    op.create_index("idx_claims_adversarial_probe", "claims", ["last_adversarial_probe_at"])
    try:
        op.create_index(
            "idx_evidence_jury_pending",
            "evidence",
            ["stance_jury_run_at", "claim_id"],
            postgresql_where=sa.text("stance_jury_run_at IS NULL"),
        )
    except Exception:
        pass  # Index may already exist


def downgrade():
    op.drop_index("idx_evidence_jury_pending", table_name="evidence")
    op.drop_index("idx_claims_adversarial_probe", table_name="claims")
    op.drop_column("claims", "last_adversarial_probe_at")
