"""page orchestration registry v1

Revision ID: page_orchestration_registry_v1
Revises: pipeline_runs_observability_v1
Create Date: 2026-06-11
"""

from __future__ import annotations

import json

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "page_orchestration_registry_v1"
down_revision = "pipeline_runs_observability_v1"
branch_labels = None
depends_on = None


LANES_57 = {
    "autowiki": True,
    "deep_synthesis": True,
    "judges": True,
    "section_rewrite": True,
    "coherence": False,
    "research_ideas": True,
    "adversarial": True,
    "gap_detect": True,
    "evidence_drain": True,
    "verbatim_sync": True,
    "arxiv_feed_l2": True,
}


def upgrade() -> None:
    op.create_table(
        "page_orchestration",
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id", ondelete="CASCADE"), primary_key=True),
        sa.Column("status", sa.String(length=20), nullable=False, server_default="dormant"),
        sa.Column("enabled_lanes", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default=sa.text("'{}'::jsonb")),
        sa.Column("budget_caps", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default=sa.text("'{}'::jsonb")),
        sa.Column("calibration_config_path", sa.Text(), nullable=True),
        sa.Column("model_assignments", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default=sa.text("'{}'::jsonb")),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("status IN ('active','paused','onboarding','dormant')", name="ck_page_orchestration_status"),
    )
    op.create_index("ix_page_orchestration_status", "page_orchestration", ["status"])

    conn = op.get_bind()
    conn.execute(
        sa.text(
            """
            INSERT INTO page_orchestration
                (page_id, status, enabled_lanes, budget_caps, calibration_config_path, model_assignments, notes)
            SELECT id,
                   CASE WHEN id = 57 THEN 'active' ELSE 'dormant' END,
                   CASE WHEN id = 57 THEN CAST(:lanes_57 AS jsonb) ELSE '{}'::jsonb END,
                   '{}'::jsonb,
                   CASE
                       WHEN id = 57 THEN 'config/page_retrieval_calibration.galaxy-evolution.v2.yaml'
                       WHEN id = 9 THEN 'config/page_retrieval_calibration.active-galactic-nuclei.v2.yaml'
                       WHEN id = 11 THEN 'config/page_retrieval_calibration.exoplanets.v2.yaml'
                       ELSE NULL
                   END,
                   '{}'::jsonb,
                   CASE WHEN id = 57 THEN 'P2 registry seed: active, coherence disabled' ELSE NULL END
            FROM wiki_pages
            ON CONFLICT (page_id) DO NOTHING
            """
        ),
        {"lanes_57": json.dumps(LANES_57)},
    )
    conn.execute(
        sa.text(
            """
            INSERT INTO page_orchestration
                (page_id, status, enabled_lanes, calibration_config_path, notes)
            SELECT id, 'onboarding', '{"arxiv_feed_l2": true}'::jsonb,
                   CASE slug
                       WHEN 'active-galactic-nuclei' THEN 'config/page_retrieval_calibration.active-galactic-nuclei.v2.yaml'
                       WHEN 'exoplanets' THEN 'config/page_retrieval_calibration.exoplanets.v2.yaml'
                   END,
                   'P2 registry config-only onboarding candidate'
            FROM wiki_pages
            WHERE id IN (9, 11)
            ON CONFLICT (page_id) DO UPDATE
            SET status = EXCLUDED.status,
                enabled_lanes = EXCLUDED.enabled_lanes,
                calibration_config_path = EXCLUDED.calibration_config_path,
                notes = EXCLUDED.notes,
                updated_at = now()
            """
        )
    )


def downgrade() -> None:
    op.drop_index("ix_page_orchestration_status", table_name="page_orchestration")
    op.drop_table("page_orchestration")
