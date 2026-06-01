from __future__ import annotations
from sqlalchemy import ForeignKey, String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class EvidenceElementLink(Base):
    __tablename__ = "evidence_element_links"
    id: Mapped[int] = mapped_column(primary_key=True)
    evidence_id: Mapped[int] = mapped_column(ForeignKey("evidence.id"), index=True)
    source_claim_id: Mapped[int] = mapped_column(ForeignKey("claims.id"), index=True)
    target_claim_id: Mapped[int] = mapped_column(ForeignKey("claims.id"), index=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"), index=True)
    page_slug: Mapped[str] = mapped_column(Text)
    element_id: Mapped[str] = mapped_column(Text)
    element_text_snapshot: Mapped[str | None] = mapped_column(Text, nullable=True)
    arxiv_id: Mapped[str] = mapped_column(String(30))
