import datetime as dt

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Agent(Base):
    __tablename__ = "agents"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    model_name: Mapped[str]
    role: Mapped[str]  # editor | reviewer | commenter
    contributor_type: Mapped[str] = mapped_column(default="agent")  # "agent" | "human"
    specialty: Mapped[str | None] = mapped_column(nullable=True)
    country: Mapped[str | None] = mapped_column(nullable=True)       # ISO 3166-1 alpha-2
    country_name: Mapped[str | None] = mapped_column(nullable=True)  # e.g. "South Korea"
    institution: Mapped[str | None] = mapped_column(nullable=True)   # e.g. "MIT", "KASI"
    is_active: Mapped[bool] = mapped_column(default=True)
    last_active: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
