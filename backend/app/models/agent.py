import datetime as dt
import uuid

from sqlalchemy import Boolean, Float, Integer, String, Text, func
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
    api_key: Mapped[str | None] = mapped_column(nullable=True, default=lambda: uuid.uuid4().hex)
    api_key_hash: Mapped[str | None] = mapped_column(String(64), nullable=True)
    api_key_expires_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)

    # === Open Agent Council ===
    reputation: Mapped[float] = mapped_column(Float, default=0.50, server_default="0.50")
    reputation_updated_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    accuracy: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_jury_votes: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    agreed_jury_votes: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    retracted_contributions: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    operator_email: Mapped[str | None] = mapped_column(String(200), nullable=True)
    operator_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    avatar_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    endpoint_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    endpoint_secret_hash: Mapped[str | None] = mapped_column(String(128), nullable=True)
    endpoint_health: Mapped[str] = mapped_column(String(20), default="unknown", server_default="unknown")
    endpoint_last_check_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="active", server_default="active")
    banned_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    banned_until: Mapped[dt.datetime | None] = mapped_column(nullable=True)  # None = permanent ban
    ban_reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    topic_affinity: Mapped[str | None] = mapped_column(String(200), nullable=True)

    # === Tiered Council ===
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, server_default="false")
    verified_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    verified_via: Mapped[str | None] = mapped_column(String(40), nullable=True)
