"""SQLAlchemy models for facility profiles, news items, and calendar subscriptions."""
import datetime as dt
from sqlalchemy import Boolean, Float, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class FacilityProfile(Base):
    __tablename__ = "facility_profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(String(80), unique=True)
    full_name: Mapped[str] = mapped_column(String(200))
    short_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    operator: Mapped[str | None] = mapped_column(String(100), nullable=True)
    operator_country: Mapped[str | None] = mapped_column(String(50), nullable=True)
    facility_kind: Mapped[str | None] = mapped_column(String(30), nullable=True)
    operating_status: Mapped[str] = mapped_column(String(20), default="active")
    data_portals: Mapped[str | None] = mapped_column(Text, nullable=True)
    documentation_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    proposal_portal_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    homepage_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    first_light_date: Mapped[str | None] = mapped_column(String(20), nullable=True)
    decommission_date: Mapped[str | None] = mapped_column(String(20), nullable=True)
    last_verified_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())

    news_items: Mapped[list["FacilityNewsItem"]] = relationship(back_populates="facility")


class FacilityNewsItem(Base):
    __tablename__ = "facility_news_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    facility_id: Mapped[int | None] = mapped_column(ForeignKey("facility_profiles.id"), nullable=True)
    title: Mapped[str] = mapped_column(String(300))
    slug: Mapped[str] = mapped_column(String(200), unique=True)
    kind: Mapped[str] = mapped_column(String(40))
    track: Mapped[str] = mapped_column(String(20), default="data")
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    expert_context: Mapped[str | None] = mapped_column(Text, nullable=True)
    occurs_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    occurs_at_confidence: Mapped[str] = mapped_column(String(20), default="hard")
    occurrence_status: Mapped[str] = mapped_column(String(20), default="upcoming")
    source_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    data_portal_urls: Mapped[str | None] = mapped_column(Text, nullable=True)
    related_page_slugs: Mapped[str | None] = mapped_column(Text, nullable=True)
    related_arxiv_ids: Mapped[str | None] = mapped_column(Text, nullable=True)
    credibility_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    credibility_model: Mapped[str | None] = mapped_column(String(50), nullable=True)
    credibility_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    featured: Mapped[bool] = mapped_column(Boolean, default=False)
    do_not_feature: Mapped[bool] = mapped_column(Boolean, default=False)
    # v2: general-news fields (NULL for facility-origin items)
    source_publication: Mapped[str | None] = mapped_column(String(80), nullable=True)
    source_tier: Mapped[str | None] = mapped_column(String(1), nullable=True)
    paper_arxiv_id: Mapped[str | None] = mapped_column(String(40), nullable=True, index=True)
    paper_doi: Mapped[str | None] = mapped_column(String(200), nullable=True)
    paper_venue: Mapped[str | None] = mapped_column(String(80), nullable=True)
    is_press_release: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    advance_type: Mapped[str | None] = mapped_column(String(40), nullable=True)
    popsci_flags: Mapped[str | None] = mapped_column(Text, nullable=True)
    topic_tags: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())

    facility: Mapped["FacilityProfile | None"] = relationship(back_populates="news_items")
    subscriptions: Mapped[list["CalendarSubscription"]] = relationship(back_populates="news_item")


class CalendarSubscription(Base):
    """
    Schema (from DB):
      id, facility_news_item_id (FK→facility_news_items.id), email,
      unsubscribe_token, notify_when (default 'completed'),
      notified_at, created_at
    """
    __tablename__ = "calendar_subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    facility_news_item_id: Mapped[int] = mapped_column(ForeignKey("facility_news_items.id"))
    email: Mapped[str] = mapped_column(String(255))
    unsubscribe_token: Mapped[str] = mapped_column(String(64))
    notify_when: Mapped[str | None] = mapped_column(String(30), default="completed")
    notified_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())

    news_item: Mapped["FacilityNewsItem"] = relationship(back_populates="subscriptions")
