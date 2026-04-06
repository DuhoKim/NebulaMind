import datetime as dt

from sqlalchemy import Boolean, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class ArxivPaper(Base):
    __tablename__ = "arxiv_papers"

    id: Mapped[int] = mapped_column(primary_key=True)
    arxiv_id: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    title: Mapped[str] = mapped_column(Text)
    authors: Mapped[str] = mapped_column(Text)  # JSON array string
    abstract: Mapped[str] = mapped_column(Text)
    abstract_summary: Mapped[str] = mapped_column(Text, default="")
    category: Mapped[str] = mapped_column(String(30))  # astro-ph.GA, etc.
    submitted: Mapped[str] = mapped_column(String(20))  # "2026-04-06"
    url: Mapped[str] = mapped_column(Text)
    related_pages: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON array of slugs
    wiki_edit_proposed: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
