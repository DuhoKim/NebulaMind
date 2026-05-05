"""Trust mechanics Phase 1: evidence quality + audit log + claim retry tracking."""
from alembic import op
import sqlalchemy as sa

revision = "p1trust1"
down_revision = "a1b2c3d4e5f6"
branch_labels = None
depends_on = None


def upgrade():
    # --- evidence: quality, abstract, source IDs ---
    op.add_column("evidence", sa.Column("quality", sa.Float(), nullable=False, server_default="0.50"))
    op.add_column("evidence", sa.Column("abstract", sa.Text(), nullable=True))
    op.add_column("evidence", sa.Column("ads_bibcode", sa.String(30), nullable=True))
    op.add_column("evidence", sa.Column("s2_paper_id", sa.String(60), nullable=True))
    op.add_column("evidence", sa.Column("verified_at", sa.TIMESTAMP(), nullable=True))
    op.add_column("evidence", sa.Column("stance_jury_run_at", sa.TIMESTAMP(), nullable=True))
    op.create_index("idx_evidence_quality", "evidence", ["quality"])
    op.create_index("idx_evidence_year", "evidence", ["year"])

    # --- claims: trust score, retry tracking, override scaffolding ---
    op.add_column("claims", sa.Column("trust_score", sa.Float(), nullable=False, server_default="0.0"))
    op.add_column("claims", sa.Column("trust_score_updated_at", sa.TIMESTAMP(), nullable=True))
    op.add_column("claims", sa.Column("evidence_search_attempted_at", sa.TIMESTAMP(), nullable=True))
    op.add_column("claims", sa.Column("human_trust_override", sa.String(20), nullable=True))
    op.add_column("claims", sa.Column("human_override_by", sa.Integer(), nullable=True))
    op.add_column("claims", sa.Column("human_override_at", sa.TIMESTAMP(), nullable=True))
    op.add_column("claims", sa.Column("human_override_reason", sa.Text(), nullable=True))
    op.add_column("claims", sa.Column("human_override_locked", sa.Boolean(), nullable=False, server_default=sa.false()))

    # --- evidence_votes: weight + voter type ---
    op.add_column("evidence_votes", sa.Column("weight", sa.Float(), nullable=False, server_default="1.0"))
    op.add_column("evidence_votes", sa.Column("voter_type", sa.String(20), nullable=False, server_default="agent"))

    # --- trust_audit_log ---
    op.create_table(
        "trust_audit_log",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("claim_id", sa.Integer, sa.ForeignKey("claims.id"), nullable=False, index=True),
        sa.Column("old_level", sa.String(20), nullable=True),
        sa.Column("new_level", sa.String(20), nullable=False),
        sa.Column("old_score", sa.Float, nullable=True),
        sa.Column("new_score", sa.Float, nullable=False),
        sa.Column("e_component", sa.Float, nullable=True),
        sa.Column("v_component", sa.Float, nullable=True),
        sa.Column("t_component", sa.Float, nullable=True),
        sa.Column("h_component", sa.Float, nullable=True),
        sa.Column("trigger", sa.String(40), nullable=False),
        sa.Column("triggered_by_agent_id", sa.Integer, nullable=True),
        sa.Column("triggered_by_human_id", sa.Integer, nullable=True),
        sa.Column("notes", sa.Text, nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.func.now()),
    )
    # Two separate simple indexes instead of DESC composite
    op.create_index("idx_trust_audit_claim_id", "trust_audit_log", ["claim_id"])
    op.create_index("idx_trust_audit_created_at", "trust_audit_log", ["created_at"])

    # --- hero_facts versioning (Addendum A H1) ---
    op.add_column("wiki_pages", sa.Column("hero_facts_version", sa.Integer, nullable=False, server_default="1"))
    op.add_column("wiki_pages", sa.Column("hero_facts_legacy", sa.Text(), nullable=True))
    op.add_column("wiki_pages", sa.Column("hero_facts_validated", sa.Boolean(), nullable=False, server_default=sa.false()))
    op.add_column("wiki_pages", sa.Column("hero_facts_updated_at", sa.TIMESTAMP(), nullable=True))


def downgrade():
    op.drop_column("wiki_pages", "hero_facts_updated_at")
    op.drop_column("wiki_pages", "hero_facts_validated")
    op.drop_column("wiki_pages", "hero_facts_legacy")
    op.drop_column("wiki_pages", "hero_facts_version")

    op.drop_index("idx_trust_audit_created_at", table_name="trust_audit_log")
    op.drop_index("idx_trust_audit_claim_id", table_name="trust_audit_log")
    op.drop_table("trust_audit_log")

    op.drop_column("evidence_votes", "voter_type")
    op.drop_column("evidence_votes", "weight")

    op.drop_column("claims", "human_override_locked")
    op.drop_column("claims", "human_override_reason")
    op.drop_column("claims", "human_override_at")
    op.drop_column("claims", "human_override_by")
    op.drop_column("claims", "human_trust_override")
    op.drop_column("claims", "evidence_search_attempted_at")
    op.drop_column("claims", "trust_score_updated_at")
    op.drop_column("claims", "trust_score")

    op.drop_index("idx_evidence_year", table_name="evidence")
    op.drop_index("idx_evidence_quality", table_name="evidence")
    op.drop_column("evidence", "stance_jury_run_at")
    op.drop_column("evidence", "verified_at")
    op.drop_column("evidence", "s2_paper_id")
    op.drop_column("evidence", "ads_bibcode")
    op.drop_column("evidence", "abstract")
    op.drop_column("evidence", "quality")
