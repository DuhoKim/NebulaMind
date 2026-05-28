import datetime as dt
from sqlalchemy import ForeignKey, String, Text, Float, Integer, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class JuryTask(Base):
    __tablename__ = "jury_tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    evidence_id: Mapped[int] = mapped_column(ForeignKey("evidence.id"), unique=True)
    claim_id: Mapped[int] = mapped_column(ForeignKey("claims.id"))
    category: Mapped[str | None] = mapped_column(String(40), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="open")
    votes_received: Mapped[int] = mapped_column(default=0)
    votes_target: Mapped[int] = mapped_column(default=4)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    closed_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    expires_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)


class JuryAssignment(Base):
    __tablename__ = "jury_assignments"
    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("jury_tasks.id"))
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"))
    # Legacy columns from oac_v1 (still in DB)
    # assigned_at, voted_at, vote, reason
    # New columns added in oac_v2
    delivered_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    delivery_method: Mapped[str] = mapped_column(String(20), default="poll", server_default="poll")
    responded_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    vote_id: Mapped[int | None] = mapped_column(ForeignKey("evidence_votes.id"), nullable=True)
    expired: Mapped[bool] = mapped_column(Boolean, default=False)


class ReputationLog(Base):
    __tablename__ = "reputation_log"
    id: Mapped[int] = mapped_column(primary_key=True)
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"))
    delta: Mapped[float] = mapped_column(Float)
    old_value: Mapped[float] = mapped_column(Float)
    new_value: Mapped[float] = mapped_column(Float)
    old_reputation: Mapped[float] = mapped_column(Float, default=0.0)
    new_reputation: Mapped[float] = mapped_column(Float, default=0.0)
    reason: Mapped[str] = mapped_column(String(40))
    ref_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ref_type: Mapped[str | None] = mapped_column(String(20), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
