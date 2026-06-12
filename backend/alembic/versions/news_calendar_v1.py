"""News, Calendar & Newsletter v1 migration."""
from alembic import op
import sqlalchemy as sa

revision = "news_calendar_v1"
down_revision = ("oac_v1", "naai_benchmark_v1")
branch_labels = "news_calendar"
depends_on = None


def upgrade():
    # Facility profiles (long-lived entities)
    op.create_table(
        "facility_profiles",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("slug", sa.String(80), unique=True, nullable=False, index=True),
        sa.Column("full_name", sa.String(200), nullable=False),
        sa.Column("short_name", sa.String(50), nullable=True),
        sa.Column("operator", sa.String(100), nullable=True),
        sa.Column("operator_country", sa.String(50), nullable=True),
        sa.Column("facility_kind", sa.String(30), nullable=True),  # spectroscopic, imaging, radio, space, etc
        sa.Column("operating_status", sa.String(20), nullable=False, server_default="active"),  # active, planned, decommissioned
        sa.Column("data_portals", sa.Text(), nullable=True),  # JSON array of {label, url}
        sa.Column("documentation_url", sa.Text(), nullable=True),
        sa.Column("proposal_portal_url", sa.Text(), nullable=True),
        sa.Column("homepage_url", sa.Text(), nullable=True),
        sa.Column("first_light_date", sa.String(20), nullable=True),
        sa.Column("decommission_date", sa.String(20), nullable=True),
        sa.Column("last_verified_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
    )

    # Facility news items (events: releases, milestones, deadlines)
    op.create_table(
        "facility_news_items",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("facility_id", sa.Integer(), sa.ForeignKey("facility_profiles.id"), nullable=True, index=True),
        sa.Column("title", sa.String(300), nullable=False),
        sa.Column("slug", sa.String(200), unique=True, nullable=False, index=True),
        sa.Column("kind", sa.String(40), nullable=False),  # release, proposal_call, milestone, embargo_lift, facility_news
        sa.Column("track", sa.String(20), nullable=False, server_default="data"),  # data, results, facilities
        sa.Column("summary", sa.Text(), nullable=True),  # professional-level 2-3 sentences
        sa.Column("expert_context", sa.Text(), nullable=True),  # why it matters to the field
        sa.Column("occurs_at", sa.DateTime(), nullable=True),  # when it happens
        sa.Column("occurs_at_confidence", sa.String(20), server_default="hard"),  # hard, soft, approximate
        sa.Column("occurrence_status", sa.String(20), server_default="upcoming"),  # upcoming, completed, delayed, cancelled
        sa.Column("source_url", sa.Text(), nullable=True),
        sa.Column("data_portal_urls", sa.Text(), nullable=True),  # JSON [{label, url}]
        sa.Column("related_page_slugs", sa.Text(), nullable=True),  # JSON array of wiki slugs
        sa.Column("related_arxiv_ids", sa.Text(), nullable=True),  # JSON array
        sa.Column("credibility_score", sa.Float(), nullable=True),  # 0-1, from local model review
        sa.Column("credibility_model", sa.String(50), nullable=True),
        sa.Column("credibility_notes", sa.Text(), nullable=True),
        sa.Column("featured", sa.Boolean(), server_default="false"),
        sa.Column("do_not_feature", sa.Boolean(), server_default="false"),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.func.now()),
    )
    op.create_index("ix_facility_news_items_occurs_at", "facility_news_items", ["occurs_at"])
    op.create_index("ix_facility_news_items_kind", "facility_news_items", ["kind"])

    # Calendar subscriptions ("Notify me")
    op.create_table(
        "calendar_subscriptions",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("facility_news_item_id", sa.Integer(), sa.ForeignKey("facility_news_items.id"), nullable=False, index=True),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("unsubscribe_token", sa.String(64), nullable=False),
        sa.Column("notify_when", sa.String(30), server_default="completed"),  # completed, any_status_change
        sa.Column("notified_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
    )

    # Daily news digest state
    op.create_table(
        "news_digest_runs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("run_date", sa.String(10), nullable=False, unique=True),  # YYYY-MM-DD
        sa.Column("papers_processed", sa.Integer(), server_default="0"),
        sa.Column("items_featured", sa.Integer(), server_default="0"),
        sa.Column("newsletter_sent", sa.Boolean(), server_default="false"),
        sa.Column("newsletter_sent_at", sa.DateTime(), nullable=True),
        sa.Column("model_used", sa.String(50), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
    )


def downgrade():
    op.drop_table("news_digest_runs")
    op.drop_table("calendar_subscriptions")
    op.drop_index("ix_facility_news_items_kind", "facility_news_items")
    op.drop_index("ix_facility_news_items_occurs_at", "facility_news_items")
    op.drop_table("facility_news_items")
    op.drop_table("facility_profiles")
