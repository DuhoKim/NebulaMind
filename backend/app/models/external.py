import datetime as dt
from sqlalchemy import ForeignKey, String, Text, Float, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class ExternalSourceLog(Base):
    __tablename__ = "external_source_log"

    id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str] = mapped_column(String(20))
    external_id: Mapped[str] = mapped_column(String(100))
    page_id: Mapped[int | None] = mapped_column(ForeignKey("wiki_pages.id"), nullable=True, index=True)
    claim_id: Mapped[int | None] = mapped_column(ForeignKey("claims.id"), nullable=True)
    evidence_id: Mapped[int | None] = mapped_column(ForeignKey("evidence.id"), nullable=True)
    decision: Mapped[str] = mapped_column(String(40))
    quality: Mapped[float | None] = mapped_column(Float, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())


class WikipediaReference(Base):
    __tablename__ = "wikipedia_references"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"), index=True)
    wikipedia_title: Mapped[str] = mapped_column(String(200))
    source_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    arxiv_id: Mapped[str | None] = mapped_column(String(30), nullable=True)
    doi: Mapped[str | None] = mapped_column(String(100), nullable=True)
    processed: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    process_result: Mapped[str | None] = mapped_column(String(40), nullable=True)
    last_attempted_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())


class NewPageProposal(Base):
    __tablename__ = "new_page_proposals"

    id: Mapped[int] = mapped_column(primary_key=True)
    suggested_slug: Mapped[str] = mapped_column(String(120), unique=True)
    suggested_title: Mapped[str] = mapped_column(String(200))
    cluster_papers: Mapped[str] = mapped_column(Text)  # JSON array of arxiv_ids
    centroid_similarity: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    notified_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    resulting_page_id: Mapped[int | None] = mapped_column(ForeignKey("wiki_pages.id"), nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
