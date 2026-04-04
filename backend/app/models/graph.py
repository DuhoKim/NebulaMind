import datetime as dt

from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class PageRelation(Base):
    __tablename__ = "page_relations"

    id: Mapped[int] = mapped_column(primary_key=True)
    source_page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"))
    target_page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"))
    relation_type: Mapped[str] = mapped_column(String(30), default="related")
    weight: Mapped[float] = mapped_column(default=0.5)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
