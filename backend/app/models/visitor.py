import datetime as dt

from sqlalchemy import String, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Visit(Base):
    __tablename__ = "visits"

    id: Mapped[int] = mapped_column(primary_key=True)
    visitor_type: Mapped[str] = mapped_column(String(10))  # human or agent
    ip_address: Mapped[str | None] = mapped_column(String(64), nullable=True)
    path: Mapped[str | None] = mapped_column(String(500), nullable=True)
    user_agent: Mapped[str | None] = mapped_column(String(500), nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
