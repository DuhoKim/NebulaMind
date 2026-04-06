import datetime as dt

from sqlalchemy import ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Spotlight(Base):
    __tablename__ = "spotlights"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(index=True)  # submitter email (no login required for now)
    arxiv_id: Mapped[str] = mapped_column(index=True)
    title: Mapped[str]
    authors: Mapped[str] = mapped_column(Text, default="[]")  # JSON array
    summary: Mapped[str] = mapped_column(Text, default="")  # AI generated
    related_pages: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON array of slugs
    status: Mapped[str] = mapped_column(String(20), default="active")  # active | expired | rejected
    featured: Mapped[bool] = mapped_column(default=False, server_default="false")
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    expires_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)  # 30 days after creation
