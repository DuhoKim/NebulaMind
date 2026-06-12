"""add rewrite_status to claims

Revision ID: rewrite_status_claims_v1
Revises: arxiv_wiki_feed_evidence_link_v1
"""
from alembic import op
import sqlalchemy as sa


revision = "rewrite_status_claims_v1"
down_revision = "arxiv_wiki_feed_evidence_link_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("claims", sa.Column("rewrite_status", sa.Text(), nullable=True))
    op.create_check_constraint(
        "ck_claims_rewrite_status",
        "claims",
        "rewrite_status IS NULL OR rewrite_status IN ('parent_replaced', 'rewritten_child', 'deferred_child')",
    )
    op.create_index("idx_claims_rewrite_status", "claims", ["rewrite_status"])

    op.execute(
        """
        UPDATE claims
        SET rewrite_status = 'rewritten_child'
        WHERE id IN (
            SELECT l.child_claim_id
            FROM claim_rewrite_lineage l
            JOIN claim_rewrite_batches b ON b.id = l.batch_id
            WHERE b.run_key = 'claim_rewrite_galaxy_evolution_v1_20260525_055620_step4_promote_35'
        )
        """
    )
    op.execute(
        """
        UPDATE claims
        SET rewrite_status = 'parent_replaced'
        WHERE id IN (
            SELECT DISTINCT l.parent_claim_id
            FROM claim_rewrite_lineage l
            JOIN claim_rewrite_batches b ON b.id = l.batch_id
            WHERE b.run_key = 'claim_rewrite_galaxy_evolution_v1_20260525_055620_step4_promote_35'
        )
        """
    )


def downgrade():
    op.drop_index("idx_claims_rewrite_status", table_name="claims")
    op.drop_constraint("ck_claims_rewrite_status", "claims", type_="check")
    op.drop_column("claims", "rewrite_status")
