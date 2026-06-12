"""SQLAlchemy models for NAAI Benchmark — NebulaMind Astronomy AI Index."""
import datetime as dt
from sqlalchemy import ForeignKey, String, Text, Float, Integer, Boolean, Date, JSON, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class BenchmarkTask(Base):
    __tablename__ = "benchmark_tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(Text)
    correct_answer: Mapped[str] = mapped_column(Text)  # stored hashed
    category: Mapped[str | None] = mapped_column(String(40), nullable=True)
    difficulty: Mapped[str] = mapped_column(String(20), default="intermediate")
    source_claim_id: Mapped[int | None] = mapped_column(nullable=True)
    answer_choices: Mapped[list | None] = mapped_column(JSON, nullable=True)  # MCQ options
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())


class BenchmarkSubmission(Base):
    __tablename__ = "benchmark_submissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("benchmark_tasks.id"))
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"))
    submitted_answer: Mapped[str] = mapped_column(Text)
    confidence: Mapped[float] = mapped_column(Float)
    is_correct: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    brier_contribution: Mapped[float | None] = mapped_column(Float, nullable=True)
    submitted_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())


class BenchmarkScore(Base):
    __tablename__ = "benchmark_scores"

    id: Mapped[int] = mapped_column(primary_key=True)
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"))
    backing_model: Mapped[str | None] = mapped_column(String(100), nullable=True)
    total_votes: Mapped[int] = mapped_column(default=0)
    correct_votes: Mapped[int] = mapped_column(default=0)
    accuracy: Mapped[float | None] = mapped_column(Float, nullable=True)
    brier_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    calibration: Mapped[float | None] = mapped_column(Float, nullable=True)
    naai_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    qualified: Mapped[bool] = mapped_column(Boolean, default=False)
    snapshot_date: Mapped[dt.date] = mapped_column(Date, server_default=func.current_date())
    computed_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
