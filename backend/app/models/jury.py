import datetime as dt
from sqlalchemy import ForeignKey, String, Text, Float, Integer, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from app.models import JSONB


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


class PromptRevision(Base):
    __tablename__ = "prompt_revisions"
    id: Mapped[int] = mapped_column(primary_key=True)
    prompt_id: Mapped[str] = mapped_column(String(80), nullable=False)
    policy_id: Mapped[str] = mapped_column(String(80), nullable=False)
    prompt_sha256: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    system_text: Mapped[str] = mapped_column(Text, nullable=False)
    user_template: Mapped[str] = mapped_column(Text, nullable=False)
    aggregation: Mapped[dict] = mapped_column(JSONB, nullable=False)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())


class JuryScorecard(Base):
    __tablename__ = "jury_scorecards"
    id: Mapped[int] = mapped_column(primary_key=True)
    evidence_id: Mapped[int] = mapped_column(ForeignKey("evidence.id", ondelete="CASCADE"), nullable=False)
    prompt_revision_id: Mapped[int] = mapped_column(ForeignKey("prompt_revisions.id"), nullable=False)
    relevance: Mapped[float] = mapped_column(Float, nullable=False)
    entailment: Mapped[float] = mapped_column(Float, nullable=False)
    rigor: Mapped[float] = mapped_column(Float, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    var_entailment: Mapped[float] = mapped_column(Float, nullable=False)
    quality_v2: Mapped[float] = mapped_column(Float, nullable=False)
    stance: Mapped[str] = mapped_column(String(20), nullable=False)
    jurors_used: Mapped[list] = mapped_column(JSONB, nullable=False)
    policy_id: Mapped[str] = mapped_column(String(80), nullable=False)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())


class JuryAgentProfile(Base):
    __tablename__ = "jury_agent_profiles"
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id", ondelete="CASCADE"), primary_key=True)
    tier_weight: Mapped[float] = mapped_column(Float, default=0.7, server_default="0.7")
    domain_weight: Mapped[float] = mapped_column(Float, default=0.85, server_default="0.85")
    reliability_weight: Mapped[float] = mapped_column(Float, default=0.6, server_default="0.6")
    calibration_temperature: Mapped[float] = mapped_column(Float, default=1.0, server_default="1.0")
    fallback_chain: Mapped[list] = mapped_column(JSONB, default=list, server_default="'[]'")
    last_calibrated_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

