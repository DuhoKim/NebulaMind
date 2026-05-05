import datetime as dt
from sqlalchemy import ForeignKey, String, Text, Integer, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Claim(Base):
    __tablename__ = "claims"
    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"), index=True)
    section: Mapped[str] = mapped_column(String(100), default="Overview")
    order_idx: Mapped[int] = mapped_column(default=0)
    connector: Mapped[str | None] = mapped_column(String(50), nullable=True)
    text: Mapped[str] = mapped_column(Text)
    trust_level: Mapped[str] = mapped_column(String(20), default="unverified")
    claim_type: Mapped[str] = mapped_column(String(20), default="established")
    debate_topic: Mapped[str | None] = mapped_column(String(200), nullable=True)
    debate_stance: Mapped[str | None] = mapped_column(String(20), nullable=True)
    created_by_agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[dt.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    trust_score: Mapped[float] = mapped_column(default=0.0)
    trust_score_updated_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    evidence_search_attempted_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    human_trust_override: Mapped[str | None] = mapped_column(String(20), nullable=True)
    human_override_by: Mapped[int | None] = mapped_column(nullable=True)
    human_override_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    human_override_reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    human_override_locked: Mapped[bool] = mapped_column(default=False)
    last_adversarial_probe_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)

class Evidence(Base):
    __tablename__ = "evidence"
    id: Mapped[int] = mapped_column(primary_key=True)
    claim_id: Mapped[int] = mapped_column(ForeignKey("claims.id"), index=True)
    arxiv_id: Mapped[str | None] = mapped_column(String(30), nullable=True)
    doi: Mapped[str | None] = mapped_column(String(100), nullable=True)
    url: Mapped[str | None] = mapped_column(Text, nullable=True)
    title: Mapped[str] = mapped_column(Text)
    authors: Mapped[str | None] = mapped_column(Text, nullable=True)
    year: Mapped[int | None] = mapped_column(nullable=True)
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    stance: Mapped[str] = mapped_column(String(20), default="supports")
    added_by_agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    quality: Mapped[float] = mapped_column(default=0.50)
    abstract: Mapped[str | None] = mapped_column(Text, nullable=True)
    ads_bibcode: Mapped[str | None] = mapped_column(String(30), nullable=True)
    s2_paper_id: Mapped[str | None] = mapped_column(String(60), nullable=True)
    verified_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    stance_jury_run_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    source_channel: Mapped[str] = mapped_column(String(40), default="manual", server_default="manual")
    arxiv_verified: Mapped[bool] = mapped_column(Boolean, default=False, server_default="false")
    # === Open Agent Council ===
    consensus_vote: Mapped[int | None] = mapped_column(Integer, nullable=True)
    consensus_settled_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)

class EvidenceVote(Base):
    __tablename__ = "evidence_votes"
    id: Mapped[int] = mapped_column(primary_key=True)
    evidence_id: Mapped[int] = mapped_column(ForeignKey("evidence.id"), index=True)
    value: Mapped[int]
    agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    weight: Mapped[float] = mapped_column(default=1.0)
    voter_type: Mapped[str] = mapped_column(String(20), default="agent")

class EvidenceComment(Base):
    __tablename__ = "evidence_comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    evidence_id: Mapped[int] = mapped_column(ForeignKey("evidence.id"), index=True)
    body: Mapped[str] = mapped_column(Text)
    agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())

class ClaimEditProposal(Base):
    __tablename__ = "claim_edit_proposals"
    id: Mapped[int] = mapped_column(primary_key=True)
    claim_id: Mapped[int] = mapped_column(ForeignKey("claims.id"), index=True)
    original_text: Mapped[str] = mapped_column(Text)
    new_text: Mapped[str] = mapped_column(Text)
    arxiv_evidence: Mapped[str] = mapped_column(String(50))  # arXiv ID 필수
    evidence_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    email: Mapped[str | None] = mapped_column(String(200), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    votes_approve: Mapped[int] = mapped_column(default=0)
    votes_reject: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())


class TrustAuditLog(Base):
    __tablename__ = "trust_audit_log"
    id: Mapped[int] = mapped_column(primary_key=True)
    claim_id: Mapped[int] = mapped_column(ForeignKey("claims.id"), index=True)
    old_level: Mapped[str | None] = mapped_column(String(20), nullable=True)
    new_level: Mapped[str] = mapped_column(String(20))
    old_score: Mapped[float | None] = mapped_column(nullable=True)
    new_score: Mapped[float] = mapped_column()
    e_component: Mapped[float | None] = mapped_column(nullable=True)
    v_component: Mapped[float | None] = mapped_column(nullable=True)
    t_component: Mapped[float | None] = mapped_column(nullable=True)
    h_component: Mapped[float | None] = mapped_column(nullable=True)
    trigger: Mapped[str] = mapped_column(String(40))
    triggered_by_agent_id: Mapped[int | None] = mapped_column(nullable=True)
    triggered_by_human_id: Mapped[int | None] = mapped_column(nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
