import datetime as dt

from sqlalchemy import Float, ForeignKey, Integer, String, Text, func, JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class AutowikiRun(Base):
    __tablename__ = "autowiki_runs"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"), nullable=False)
    started_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    finished_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
    proposal_type: Mapped[str | None] = mapped_column(String(40), nullable=True)
    model_proposer: Mapped[str | None] = mapped_column(String(80), nullable=True)
    model_judge: Mapped[str | None] = mapped_column(String(80), nullable=True)
    judge_model: Mapped[str | None] = mapped_column(String(40), nullable=True)

    # structural
    h0_struct: Mapped[float | None] = mapped_column(Float, nullable=True)
    h1_struct: Mapped[float | None] = mapped_column(Float, nullable=True)
    components_before: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    components_after: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    # utility (LLM-judged)
    u0_median: Mapped[float | None] = mapped_column(Float, nullable=True)
    u1_median: Mapped[float | None] = mapped_column(Float, nullable=True)
    u0_runs: Mapped[list | None] = mapped_column(JSON, nullable=True)
    u1_runs: Mapped[list | None] = mapped_column(JSON, nullable=True)
    judge_rationale: Mapped[str | None] = mapped_column(Text, nullable=True)
    judge_prompt_version: Mapped[str | None] = mapped_column(String(20), nullable=True)

    # composite + decision
    q0: Mapped[float | None] = mapped_column(Float, nullable=True)
    q1: Mapped[float | None] = mapped_column(Float, nullable=True)
    delta_q: Mapped[float | None] = mapped_column(Float, nullable=True)
    decision: Mapped[str | None] = mapped_column(String(20), nullable=True)
    reject_reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    committed_version_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("page_versions.id"), nullable=True
    )

    # observability
    latency_ms_breakdown: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    error_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    idea_signals_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)


class AutowikiTarget(Base):
    __tablename__ = "autowiki_targets"

    page_id: Mapped[int] = mapped_column(
        ForeignKey("wiki_pages.id"), primary_key=True
    )
    target_q: Mapped[float] = mapped_column(Float, default=0.78)
    last_raised_at: Mapped[dt.datetime | None] = mapped_column(nullable=True)
