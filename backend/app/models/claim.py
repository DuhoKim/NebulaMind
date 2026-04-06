import datetime as dt
from sqlalchemy import ForeignKey, String, Text, Integer, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Claim(Base):
    __tablename__ = "claims"
    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"), index=True)
    section: Mapped[str] = mapped_column(String(100), default="Overview")
    order_idx: Mapped[int] = mapped_column(default=0)
    text: Mapped[str] = mapped_column(Text)
    trust_level: Mapped[str] = mapped_column(String(20), default="unverified")
    created_by_agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[dt.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

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

class EvidenceVote(Base):
    __tablename__ = "evidence_votes"
    id: Mapped[int] = mapped_column(primary_key=True)
    evidence_id: Mapped[int] = mapped_column(ForeignKey("evidence.id"), index=True)
    value: Mapped[int]
    agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())

class EvidenceComment(Base):
    __tablename__ = "evidence_comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    evidence_id: Mapped[int] = mapped_column(ForeignKey("evidence.id"), index=True)
    body: Mapped[str] = mapped_column(Text)
    agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
