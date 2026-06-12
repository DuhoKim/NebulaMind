import datetime as dt
import json

from sqlalchemy import Boolean, Float, ForeignKey, Numeric, String, Text, UniqueConstraint, event, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models import JSONB


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

    content_canonicalize_failed_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    content_canonicalize_failure_reason: Mapped[str | None] = mapped_column(Text, nullable=True)

    versions: Mapped[list["PageVersion"]] = relationship(back_populates="page", order_by="PageVersion.version_num")


class PageOrchestration(Base):
    __tablename__ = "page_orchestration"

    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id", ondelete="CASCADE"), primary_key=True)
    status: Mapped[str] = mapped_column(String(20), default="dormant", server_default="dormant", index=True)
    enabled_lanes: Mapped[dict] = mapped_column(JSONB, default=dict, server_default="{}")
    budget_caps: Mapped[dict] = mapped_column(JSONB, default=dict, server_default="{}")
    calibration_config_path: Mapped[str | None] = mapped_column(Text, nullable=True)
    model_assignments: Mapped[dict] = mapped_column(JSONB, default=dict, server_default="{}")
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[dt.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())


class ContentQuarantine(Base):
    __tablename__ = "content_quarantine"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int | None] = mapped_column(ForeignKey("wiki_pages.id"), nullable=True, index=True)
    source_tag: Mapped[str] = mapped_column(String(120), default="wiki_page_content_set")
    violations: Mapped[str] = mapped_column(Text)
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    resolved_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)


@event.listens_for(WikiPage.content, "set", retval=True)
def _canonicalize_wiki_page_content(target: WikiPage, value: str | None, oldvalue, initiator) -> str:
    if value is None:
        return ""
    if not isinstance(value, str):
        return value

    from app.services.content_canonicalizer import CanonicalizerError, canonicalize

    result = canonicalize(value)
    if not result.invariants_ok:
        target.content_canonicalize_failed_at = dt.datetime.utcnow()
        target.content_canonicalize_failure_reason = json.dumps(result.violations or [])
        raise CanonicalizerError(result.violations or ["unknown_violation"])

    target.content_canonicalize_failed_at = None
    target.content_canonicalize_failure_reason = None
    return result.new_content


class PageVersion(Base):
    __tablename__ = "page_versions"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"))
    version_num: Mapped[int]
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    editor_agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    source_note: Mapped[str | None] = mapped_column(Text, nullable=True)

    page: Mapped["WikiPage"] = relationship(back_populates="versions")


class PageCitationLink(Base):
    __tablename__ = "page_citation_links"
    __table_args__ = (
        UniqueConstraint("page_id", "author_year_key", name="uq_page_citation_links_page_key"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id", ondelete="CASCADE"), index=True)
    evidence_id: Mapped[int] = mapped_column(ForeignKey("evidence.id", ondelete="CASCADE"), index=True)
    author_year_key: Mapped[str] = mapped_column(String(120))
    match_method: Mapped[str] = mapped_column(String(32))
    match_confidence: Mapped[float] = mapped_column(Float, default=1.0, server_default="1.0")
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[dt.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())


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
