import datetime as dt
import uuid

from sqlalchemy import String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Subscriber(Base):
    __tablename__ = "subscribers"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    name: Mapped[str | None] = mapped_column(nullable=True)
    categories: Mapped[str] = mapped_column(Text, default='["astro-ph.GA"]')  # JSON array
    frequency: Mapped[str] = mapped_column(String(10), default="daily")  # daily | weekly
    is_active: Mapped[bool] = mapped_column(default=True, server_default="true")
    unsubscribe_token: Mapped[str] = mapped_column(
        unique=True, default=lambda: uuid.uuid4().hex
    )
    specialty: Mapped[str | None] = mapped_column(String(50), default="general", nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
