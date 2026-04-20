from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.auth import require_api_key
from app.database import get_db
from app.models.agent import Agent
from app.models.vote import Vote
from app.routers.edits import maybe_approve

router = APIRouter(prefix="/api/votes", tags=["votes"])


class VoteCreate(BaseModel):
    edit_id: int
    agent_id: int
    value: int  # +1 or -1
    reason: str = ""


class VoteOut(BaseModel):
    id: int
    edit_id: int
    agent_id: int
    value: int
    reason: str

    model_config = {"from_attributes": True}


@router.post("", response_model=VoteOut, status_code=201)
def cast_vote(body: VoteCreate, db: Session = Depends(get_db),
    _agent: Agent = Depends(require_api_key)):
    vote = Vote(edit_id=body.edit_id, agent_id=body.agent_id, value=body.value, reason=body.reason)
    db.add(vote)
    db.commit()
    db.refresh(vote)
    maybe_approve(body.edit_id, db)
    return vote
