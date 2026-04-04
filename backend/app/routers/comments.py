from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.comment import Comment

router = APIRouter(prefix="/api/comments", tags=["comments"])


class CommentCreate(BaseModel):
    page_id: int
    agent_id: int
    parent_id: int | None = None
    body: str


class CommentOut(BaseModel):
    id: int
    page_id: int
    agent_id: int
    parent_id: int | None
    body: str

    model_config = {"from_attributes": True}


@router.get("", response_model=list[CommentOut])
def list_comments(page_id: int, db: Session = Depends(get_db)):
    return db.query(Comment).filter(Comment.page_id == page_id).order_by(Comment.created_at).all()


@router.post("", response_model=CommentOut, status_code=201)
def create_comment(body: CommentCreate, db: Session = Depends(get_db)):
    comment = Comment(page_id=body.page_id, agent_id=body.agent_id, parent_id=body.parent_id, body=body.body)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment
