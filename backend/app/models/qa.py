import datetime as dt

from sqlalchemy import ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class QAQuestion(Base):
    __tablename__ = "qa_questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"))
    question: Mapped[str] = mapped_column(Text)
    difficulty: Mapped[str] = mapped_column(String(20), default="intermediate")
    upvotes: Mapped[int] = mapped_column(default=0)
    created_by_agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())


class QAAnswer(Base):
    __tablename__ = "qa_answers"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("qa_questions.id"))
    body: Mapped[str] = mapped_column(Text)
    agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    is_accepted: Mapped[bool] = mapped_column(default=False)
    upvotes: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
