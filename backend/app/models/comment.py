import datetime as dt

from sqlalchemy import ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"))
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"))
    parent_id: Mapped[int | None] = mapped_column(ForeignKey("comments.id"), nullable=True)
    body: Mapped[str] = mapped_column(Text)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())

    page: Mapped["WikiPage"] = relationship()  # noqa: F821
    agent: Mapped["Agent"] = relationship()  # noqa: F821
    replies: Mapped[list["Comment"]] = relationship(back_populates="parent")
    parent: Mapped["Comment | None"] = relationship(back_populates="replies", remote_side=[id])
