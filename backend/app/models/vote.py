import datetime as dt

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Vote(Base):
    __tablename__ = "votes"

    id: Mapped[int] = mapped_column(primary_key=True)
    edit_id: Mapped[int] = mapped_column(ForeignKey("edit_proposals.id"))
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"))
    value: Mapped[int]  # +1 approve, -1 reject
    reason: Mapped[str] = mapped_column(default="")
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())

    edit: Mapped["EditProposal"] = relationship(back_populates="votes")  # noqa: F821
    agent: Mapped["Agent"] = relationship()  # noqa: F821
