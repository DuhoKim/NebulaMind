import datetime as dt
from sqlalchemy import ForeignKey, String, Text, Float, Integer, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Stage3Roll(Base):
    __tablename__ = "stage3_roll"

    id: Mapped[int] = mapped_column(primary_key=True)
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"), unique=True)
    seated_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    seated_by: Mapped[int | None] = mapped_column(nullable=True)
    seat_reason: Mapped[str] = mapped_column(String(40))
    removed_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    removal_reason: Mapped[str | None] = mapped_column(Text, nullable=True)


class Escalation(Base):
    __tablename__ = "escalations"

    id: Mapped[int] = mapped_column(primary_key=True)
    source_kind: Mapped[str] = mapped_column(String(40))
    source_id: Mapped[int] = mapped_column()
    current_stage: Mapped[int] = mapped_column()
    trigger_code: Mapped[str] = mapped_column(String(20))
    trigger_detail: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="open")
    resolution: Mapped[str | None] = mapped_column(String(40), nullable=True)
    votes_received: Mapped[int] = mapped_column(default=0)
    votes_target: Mapped[int] = mapped_column()
    veto_count: Mapped[int] = mapped_column(default=0)
    opened_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    expires_at: Mapped[dt.datetime] = mapped_column()
    resolved_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    opened_by_agent_id: Mapped[int | None] = mapped_column(nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)


class EscalationVote(Base):
    __tablename__ = "escalation_votes"

    id: Mapped[int] = mapped_column(primary_key=True)
    escalation_id: Mapped[int] = mapped_column(ForeignKey("escalations.id"))
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"))
    action: Mapped[str] = mapped_column(String(20))
    weight: Mapped[float] = mapped_column(Float)
    voter_tier: Mapped[int] = mapped_column()
    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
