import datetime as dt

from sqlalchemy import Boolean, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class WikiPage(Base):
    __tablename__ = "wiki_pages"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(index=True)
    slug: Mapped[str] = mapped_column(unique=True, index=True)
    content: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[dt.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    is_featured: Mapped[bool] = mapped_column(default=False, server_default="false")
    category: Mapped[str | None] = mapped_column(String(30), nullable=True)
    difficulty: Mapped[str | None] = mapped_column(String(20), nullable=True)
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    thumbnail_emoji: Mapped[str | None] = mapped_column(String(10), nullable=True)
    hero_tagline: Mapped[str | None] = mapped_column(Text, nullable=True)
    hero_facts: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Wikipedia integration (Phase A)
    wikipedia_title: Mapped[str | None] = mapped_column(String(200), nullable=True, index=True)
    wiki_summary_revision: Mapped[str | None] = mapped_column(String(40), nullable=True)
    wiki_summary_license: Mapped[str | None] = mapped_column(String(60), nullable=True, default="CC BY-SA 4.0")
    wiki_summary_fetched_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    wiki_biblio_mined_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    summary_source: Mapped[str | None] = mapped_column(String(40), nullable=True)
    summary_source_url: Mapped[str | None] = mapped_column(Text, nullable=True)

    do_not_renovate: Mapped[bool] = mapped_column(Boolean, default=False, server_default="false")
    last_renovated_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    health_score: Mapped[float | None] = mapped_column(nullable=True)
    health_updated_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)

    versions: Mapped[list["PageVersion"]] = relationship(back_populates="page", order_by="PageVersion.version_num")


class PageVersion(Base):
    __tablename__ = "page_versions"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"))
    version_num: Mapped[int]
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    editor_agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)

    page: Mapped["WikiPage"] = relationship(back_populates="versions")


class FactSource(Base):
    __tablename__ = "fact_sources"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"))
    fact_kind: Mapped[str] = mapped_column(String(20))
    fact_index: Mapped[int] = mapped_column()
    source_tier: Mapped[str] = mapped_column(String(20))
    authority: Mapped[str | None] = mapped_column(String(40), nullable=True)
    reference_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    reference_title: Mapped[str | None] = mapped_column(Text, nullable=True)
    retrieval_year: Mapped[int | None] = mapped_column(nullable=True)
    claim_id: Mapped[int | None] = mapped_column(ForeignKey("claims.id"), nullable=True)
    trust_level_snapshot: Mapped[str | None] = mapped_column(String(20), nullable=True)
    evidence_count_snapshot: Mapped[int | None] = mapped_column(nullable=True)
    representative_arxiv_id: Mapped[str | None] = mapped_column(String(30), nullable=True)
    generator: Mapped[str | None] = mapped_column(String(30), nullable=True)
    flagged: Mapped[bool] = mapped_column(Boolean, default=False)
    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    attribution: Mapped[str] = mapped_column(Text)
    cited_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    created_by_agent_id: Mapped[int | None] = mapped_column(nullable=True)
    superseded_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)


class RenovationPlan(Base):
    __tablename__ = "renovation_plans"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"))
    health_score: Mapped[float] = mapped_column(Numeric(5, 2))
    components: Mapped[str] = mapped_column(Text)  # JSON
    weakest_dimensions: Mapped[str | None] = mapped_column(Text, nullable=True)
    missing_subtopics: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="queued")
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    started_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    completed_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    edit_proposal_id: Mapped[int | None] = mapped_column(nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
