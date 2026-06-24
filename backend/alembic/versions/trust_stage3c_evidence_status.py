"""trust_stage3c_evidence_status: evidence status flag

Revision ID: trust_stage3c_evidence_status
Revises: sentence_votes_v1
Create Date: 2026-06-24

Adds evidence.status so source-finding evidence can remain provisional until
promoted. Existing rows are active by default.

TODO: the promotion workflow must set provisional evidence to active and
recalculate affected claim trust; this migration only prepares the flag.

The evidence_votes unique constraint on (evidence_id, agent_id) is deliberately
deferred: production inventory found duplicate pairs, so dedupe must run first.
Use backend/scripts/evidence_vote_dedupe_report.py for a read-only retention
plan before any later destructive cleanup/constraint migration.
"""
from alembic import op
import sqlalchemy as sa


revision = "trust_stage3c_evidence_status"
down_revision = "sentence_votes_v1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()
    insp = sa.inspect(conn)
    columns = {col["name"] for col in insp.get_columns("evidence")}

    if "status" not in columns:
        op.add_column(
            "evidence",
            sa.Column("status", sa.String(length=20), nullable=False, server_default="active"),
        )
    conn.execute(sa.text("UPDATE evidence SET status = 'active' WHERE status IS NULL"))

    checks = {check["name"] for check in insp.get_check_constraints("evidence")}
    if conn.dialect.name != "sqlite" and "ck_evidence_status" not in checks:
        op.create_check_constraint(
            "ck_evidence_status",
            "evidence",
            "status IN ('active', 'provisional')",
        )

    indexes = {idx["name"] for idx in insp.get_indexes("evidence")}
    if "idx_evidence_status" not in indexes:
        op.create_index("idx_evidence_status", "evidence", ["status"])


def downgrade() -> None:
    conn = op.get_bind()
    insp = sa.inspect(conn)

    indexes = {idx["name"] for idx in insp.get_indexes("evidence")}
    if "idx_evidence_status" in indexes:
        op.drop_index("idx_evidence_status", table_name="evidence")

    checks = {check["name"] for check in insp.get_check_constraints("evidence")}
    if "ck_evidence_status" in checks:
        op.drop_constraint("ck_evidence_status", "evidence", type_="check")

    columns = {col["name"] for col in insp.get_columns("evidence")}
    if "status" in columns:
        op.drop_column("evidence", "status")
