import datetime as dt

from sqlalchemy import Boolean, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column(nullable=True)
    message: Mapped[str] = mapped_column(Text)
    is_ai: Mapped[bool] = mapped_column(Boolean, default=False, server_default='false')
    ip_address: Mapped[str | None] = mapped_column(String(64), nullable=True)
    country: Mapped[str | None] = mapped_column(String(100), nullable=True)
    country_code: Mapped[str | None] = mapped_column(String(4), nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
