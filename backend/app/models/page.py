import datetime as dt

from sqlalchemy import ForeignKey, String, Text, func
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
    did_you_know: Mapped[str | None] = mapped_column(Text, nullable=True)

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
