import datetime as dt

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Agent(Base):
    __tablename__ = "agents"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    model_name: Mapped[str]  # e.g. "claude-sonnet-4-6", "gpt-4o" — free-form string
    role: Mapped[str]  # editor | reviewer | commenter
    is_active: Mapped[bool] = mapped_column(default=True)
    last_active: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
