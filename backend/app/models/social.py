"""SQLAlchemy model for social post drafts."""
import datetime as dt
from sqlalchemy import ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class SocialPostDraft(Base):
    __tablename__ = "social_post_drafts"

    id: Mapped[int] = mapped_column(primary_key=True)
    news_item_id: Mapped[int] = mapped_column(ForeignKey("facility_news_items.id"), nullable=False)
    platform: Mapped[str] = mapped_column(String(30))           # twitter | bluesky
    draft_text: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), default="draft")  # draft | approved | posted
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
