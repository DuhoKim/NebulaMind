"""External Sources Integration v1: arxiv classifier, wikipedia biblio, new-page proposals."""
from alembic import op
import sqlalchemy as sa

revision = "ext_sources_v1"
down_revision = "p1trust1"
branch_labels = None
depends_on = None


def upgrade():
    # ------------------------------------------------------------------ #
    # evidence: source_channel + CHECK constraint                          #
    # ------------------------------------------------------------------ #
    op.add_column(
        "evidence",
        sa.Column("source_channel", sa.String(40), nullable=False, server_default="manual"),
    )
    op.create_index("idx_evidence_source_channel", "evidence", ["source_channel"])
    op.execute(
        "ALTER TABLE evidence ADD CONSTRAINT no_wikipedia_evidence "
        "CHECK (url IS NULL OR url NOT LIKE '%wikipedia.org%')"
    )

    # ------------------------------------------------------------------ #
    # wiki_pages: Wikipedia summary + biblio columns                       #
    # ------------------------------------------------------------------ #
    op.add_column("wiki_pages", sa.Column("wikipedia_title", sa.String(200), nullable=True))
    op.add_column("wiki_pages", sa.Column("wiki_summary", sa.Text(), nullable=True))
    op.add_column("wiki_pages", sa.Column("wiki_summary_url", sa.Text(), nullable=True))
    op.add_column("wiki_pages", sa.Column("wiki_summary_revision", sa.String(40), nullable=True))
    op.add_column(
        "wiki_pages",
        sa.Column("wiki_summary_license", sa.String(60), nullable=True, server_default="CC BY-SA 4.0"),
    )
    op.add_column("wiki_pages", sa.Column("wiki_summary_fetched_at", sa.TIMESTAMP(), nullable=True))
    op.add_column("wiki_pages", sa.Column("wiki_biblio_mined_at", sa.TIMESTAMP(), nullable=True))
    op.create_index("idx_wiki_pages_wikipedia_title", "wiki_pages", ["wikipedia_title"])

    # ------------------------------------------------------------------ #
    # arxiv_papers: match_type + processed_at                             #
    # ------------------------------------------------------------------ #
    op.add_column("arxiv_papers", sa.Column("match_type", sa.String(30), nullable=True))
    op.add_column("arxiv_papers", sa.Column("processed_at", sa.TIMESTAMP(), nullable=True))
    op.create_index("idx_arxiv_papers_match_type", "arxiv_papers", ["match_type"])

    # ------------------------------------------------------------------ #
    # New table: external_source_log                                       #
    # ------------------------------------------------------------------ #
    op.create_table(
        "external_source_log",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("source", sa.String(20), nullable=False),
        sa.Column("external_id", sa.String(100), nullable=False),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id"), nullable=True),
        sa.Column("claim_id", sa.Integer(), sa.ForeignKey("claims.id"), nullable=True),
        sa.Column("evidence_id", sa.Integer(), sa.ForeignKey("evidence.id"), nullable=True),
        sa.Column("decision", sa.String(40), nullable=False),
        sa.Column("quality", sa.Float(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), server_default=sa.text("NOW()")),
    )
    op.create_index("idx_esl_source", "external_source_log", ["source"])
    op.create_index("idx_esl_page", "external_source_log", ["page_id"])
    op.create_index("idx_esl_created", "external_source_log", ["created_at"])

    # ------------------------------------------------------------------ #
    # New table: wikipedia_references                                      #
    # ------------------------------------------------------------------ #
    op.create_table(
        "wikipedia_references",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id"), nullable=False),
        sa.Column("wikipedia_title", sa.String(200), nullable=False),
        sa.Column("source_url", sa.Text(), nullable=True),
        sa.Column("arxiv_id", sa.String(30), nullable=True),
        sa.Column("doi", sa.String(100), nullable=True),
        sa.Column("processed", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("process_result", sa.String(40), nullable=True),
        sa.Column("last_attempted_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), server_default=sa.text("NOW()")),
    )
    op.create_index("idx_wpref_page", "wikipedia_references", ["page_id"])
    op.create_index("idx_wpref_processed", "wikipedia_references", ["processed"])

    # ------------------------------------------------------------------ #
    # New table: new_page_proposals                                        #
    # ------------------------------------------------------------------ #
    op.create_table(
        "new_page_proposals",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("suggested_slug", sa.String(120), nullable=False, unique=True),
        sa.Column("suggested_title", sa.String(200), nullable=False),
        sa.Column("cluster_papers", sa.Text(), nullable=False),
        sa.Column("centroid_similarity", sa.Float(), nullable=False),
        sa.Column("status", sa.String(20), nullable=False, server_default="pending"),
        sa.Column("notified_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("resulting_page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id"), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), server_default=sa.text("NOW()")),
    )


def downgrade():
    op.drop_table("new_page_proposals")
    op.drop_table("wikipedia_references")
    op.drop_index("idx_esl_created", table_name="external_source_log")
    op.drop_index("idx_esl_page", table_name="external_source_log")
    op.drop_index("idx_esl_source", table_name="external_source_log")
    op.drop_table("external_source_log")

    op.drop_index("idx_arxiv_papers_match_type", table_name="arxiv_papers")
    op.drop_column("arxiv_papers", "processed_at")
    op.drop_column("arxiv_papers", "match_type")

    op.drop_index("idx_wiki_pages_wikipedia_title", table_name="wiki_pages")
    op.drop_column("wiki_pages", "wiki_biblio_mined_at")
    op.drop_column("wiki_pages", "wiki_summary_fetched_at")
    op.drop_column("wiki_pages", "wiki_summary_license")
    op.drop_column("wiki_pages", "wiki_summary_revision")
    op.drop_column("wiki_pages", "wiki_summary_url")
    op.drop_column("wiki_pages", "wiki_summary")
    op.drop_column("wiki_pages", "wikipedia_title")

    op.execute("ALTER TABLE evidence DROP CONSTRAINT no_wikipedia_evidence")
    op.drop_index("idx_evidence_source_channel", table_name="evidence")
    op.drop_column("evidence", "source_channel")
