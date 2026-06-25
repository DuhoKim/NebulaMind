import datetime as dt

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Double,
    Float,
    ForeignKey,
    Index,
    Integer,
    SmallInteger,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models import JSONB


TRUST_LEVELS = "'consensus', 'accepted', 'debated', 'challenged', 'unverified', 'reported'"


class SentenceVote(Base):
    __tablename__ = "sentence_votes"
    __table_args__ = (
        CheckConstraint("value IN (-1, 1)", name="ck_sentence_votes_value"),
        UniqueConstraint(
            "page_version_id",
            "sentence_index",
            "sentence_hash",
            "arxiv_id",
            name="uq_sentence_votes_page_sentence_paper",
        ),
        Index("ix_sentence_votes_page_sentence", "page_version_id", "sentence_index"),
        Index("ix_sentence_votes_sentence_hash", "sentence_hash"),
        Index("ix_sentence_votes_arxiv_id", "arxiv_id"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    page_version_id: Mapped[int] = mapped_column(ForeignKey("page_versions.id", ondelete="CASCADE"), nullable=False)
    sentence_index: Mapped[int] = mapped_column(Integer, nullable=False)
    sentence_hash: Mapped[str] = mapped_column(Text, nullable=False)
    arxiv_id: Mapped[str] = mapped_column(String(30), nullable=False)
    value: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    stance_confidence: Mapped[float] = mapped_column(Float, nullable=False)
    tone_tier: Mapped[str] = mapped_column(String(20), nullable=False)
    voter_type: Mapped[str] = mapped_column(String(80), nullable=False)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())


class SentenceTrust(Base):
    __tablename__ = "sentence_trust"
    __table_args__ = (
        CheckConstraint("tone_tier IN ('settled', 'contested', 'mixed')", name="ck_sentence_trust_tone_tier"),
        CheckConstraint(f"trust_level IN ({TRUST_LEVELS})", name="ck_sentence_trust_level"),
        UniqueConstraint("page_version_id", "sentence_index", name="uq_sentence_trust_page_version_sentence"),
        Index("ix_sentence_trust_sentence_hash", "sentence_hash"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    page_version_id: Mapped[int] = mapped_column(ForeignKey("page_versions.id", ondelete="CASCADE"), nullable=False)
    sentence_index: Mapped[int] = mapped_column(Integer, nullable=False)
    sentence_hash: Mapped[str] = mapped_column(Text, nullable=False)
    tone_tier: Mapped[str] = mapped_column(Text, nullable=False, default="mixed")
    vote_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    settled_votes: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    contested_votes: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    settled_share: Mapped[float] = mapped_column(Double, nullable=False, default=0.0)
    trust_score: Mapped[float] = mapped_column(Double, nullable=False, default=0.0)
    trust_level: Mapped[str] = mapped_column(Text, nullable=False, default="unverified")
    single_source: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    contested_veto: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    tier2_density: Mapped[float] = mapped_column(Double, nullable=False, default=0.0)
    tone_distribution: Mapped[dict] = mapped_column(JSONB, nullable=False, default=dict)
    tone_distribution_4: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    updated_at: Mapped[dt.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
