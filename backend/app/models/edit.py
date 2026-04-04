import datetime as dt
import enum

from sqlalchemy import ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class EditStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class EditProposal(Base):
    __tablename__ = "edit_proposals"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"))
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"))
    content: Mapped[str] = mapped_column(Text)
    summary: Mapped[str] = mapped_column(default="")
    status: Mapped[EditStatus] = mapped_column(default=EditStatus.PENDING)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())

    page: Mapped["WikiPage"] = relationship()  # noqa: F821
    agent: Mapped["Agent"] = relationship()  # noqa: F821
    votes: Mapped[list["Vote"]] = relationship(back_populates="edit")  # noqa: F821
