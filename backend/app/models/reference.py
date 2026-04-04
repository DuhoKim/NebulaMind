import datetime as dt

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Reference(Base):
    __tablename__ = "references"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"))
    arxiv_id: Mapped[str | None] = mapped_column(nullable=True)
    doi: Mapped[str | None] = mapped_column(nullable=True)
    url: Mapped[str | None] = mapped_column(nullable=True)
    title: Mapped[str] = mapped_column(default="")
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
