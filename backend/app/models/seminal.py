import datetime as dt

from sqlalchemy import Boolean, ForeignKey, Index, String, Text, UniqueConstraint, func, text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class SeminalClaimMap(Base):
    __tablename__ = "seminal_claim_map"
    __table_args__ = (
        UniqueConstraint("claim_id", "canonical_bibcode", name="uq_seminal_claim_map_claim_bibcode"),
        Index("ix_seminal_claim_map_claim", "claim_id"),
        Index("ix_seminal_claim_map_bibcode", "canonical_bibcode"),
        Index("ix_seminal_claim_map_enabled", "enabled", postgresql_where=text("enabled")),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    claim_id: Mapped[int] = mapped_column(ForeignKey("claims.id", ondelete="CASCADE"))
    canonical_bibcode: Mapped[str] = mapped_column(String(30))
    canonical_label: Mapped[str] = mapped_column(String(120))
    canonical_doi: Mapped[str | None] = mapped_column(String(100), nullable=True)
    canonical_arxiv_id: Mapped[str | None] = mapped_column(String(30), nullable=True)
    topic_keyphrases: Mapped[str | None] = mapped_column(Text, nullable=True)
    enabled: Mapped[bool] = mapped_column(Boolean, default=True, server_default="true")
    added_by: Mapped[str] = mapped_column(String(40), default="manual", server_default="manual")
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[dt.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
