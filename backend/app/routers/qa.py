from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.models.qa import QAQuestion, QAAnswer
from app.models.page import WikiPage

router = APIRouter(prefix="/api/qa", tags=["qa"])


class QuestionCreate(BaseModel):
    question: str
    page_id: int
    difficulty: str = "intermediate"


class AnswerCreate(BaseModel):
    body: str
    agent_id: int | None = None


class AnswerOut(BaseModel):
    id: int
    question_id: int
    body: str
    agent_id: int | None
    is_accepted: bool
    upvotes: int

    class Config:
        from_attributes = True


class QuestionListItem(BaseModel):
    id: int
    question: str
    difficulty: str
    upvotes: int
    page_title: str
    page_slug: str
    answer_count: int


class QuestionDetail(BaseModel):
    id: int
    question: str
    difficulty: str
    upvotes: int
    page_id: int
    page_title: str
    page_slug: str
    answers: list[AnswerOut]


@router.get("", response_model=list[QuestionListItem])
def list_questions(
    page_slug: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(QAQuestion)

    if page_slug:
        page = db.query(WikiPage).filter(WikiPage.slug == page_slug).first()
        if not page:
            raise HTTPException(404, "Page not found")
        query = query.filter(QAQuestion.page_id == page.id)

    questions = query.order_by(QAQuestion.created_at.desc()).all()
    result = []
    for q in questions:
        page = db.query(WikiPage).filter(WikiPage.id == q.page_id).first()
        answer_count = db.query(func.count(QAAnswer.id)).filter(QAAnswer.question_id == q.id).scalar() or 0
        result.append(
            QuestionListItem(
                id=q.id,
                question=q.question,
                difficulty=q.difficulty,
                upvotes=q.upvotes,
                page_title=page.title if page else "Unknown",
                page_slug=page.slug if page else "",
                answer_count=answer_count,
            )
        )
    return result


@router.post("", response_model=QuestionListItem, status_code=201)
def create_question(body: QuestionCreate, db: Session = Depends(get_db)):
    page = db.query(WikiPage).filter(WikiPage.id == body.page_id).first()
    if not page:
        raise HTTPException(404, "Page not found")

    q = QAQuestion(question=body.question, page_id=body.page_id, difficulty=body.difficulty)
    db.add(q)
    db.commit()
    db.refresh(q)

    return QuestionListItem(
        id=q.id,
        question=q.question,
        difficulty=q.difficulty,
        upvotes=q.upvotes,
        page_title=page.title,
        page_slug=page.slug,
        answer_count=0,
    )


@router.get("/{question_id}", response_model=QuestionDetail)
def get_question(question_id: int, db: Session = Depends(get_db)):
    q = db.query(QAQuestion).filter(QAQuestion.id == question_id).first()
    if not q:
        raise HTTPException(404, "Question not found")

    page = db.query(WikiPage).filter(WikiPage.id == q.page_id).first()
    answers = db.query(QAAnswer).filter(QAAnswer.question_id == q.id).order_by(QAAnswer.created_at).all()

    return QuestionDetail(
        id=q.id,
        question=q.question,
        difficulty=q.difficulty,
        upvotes=q.upvotes,
        page_id=q.page_id,
        page_title=page.title if page else "Unknown",
        page_slug=page.slug if page else "",
        answers=[
            AnswerOut(
                id=a.id,
                question_id=a.question_id,
                body=a.body,
                agent_id=a.agent_id,
                is_accepted=a.is_accepted,
                upvotes=a.upvotes,
            )
            for a in answers
        ],
    )


@router.post("/{question_id}/answers", response_model=AnswerOut, status_code=201)
def add_answer(question_id: int, body: AnswerCreate, db: Session = Depends(get_db)):
    q = db.query(QAQuestion).filter(QAQuestion.id == question_id).first()
    if not q:
        raise HTTPException(404, "Question not found")

    a = QAAnswer(question_id=question_id, body=body.body, agent_id=body.agent_id)
    db.add(a)
    db.commit()
    db.refresh(a)

    return AnswerOut(
        id=a.id,
        question_id=a.question_id,
        body=a.body,
        agent_id=a.agent_id,
        is_accepted=a.is_accepted,
        upvotes=a.upvotes,
    )


@router.post("/{question_id}/upvote")
def upvote_question(question_id: int, db: Session = Depends(get_db)):
    q = db.query(QAQuestion).filter(QAQuestion.id == question_id).first()
    if not q:
        raise HTTPException(404, "Question not found")
    q.upvotes += 1
    db.commit()
    return {"upvotes": q.upvotes}
