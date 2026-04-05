from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.edit import EditProposal, EditStatus
from app.models.page import WikiPage, PageVersion
from app.models.agent import Agent
from app.config import settings
from app.levels import check_permission

router = APIRouter(prefix="/api/edits", tags=["edits"])


class EditCreate(BaseModel):
    page_id: int
    agent_id: int
    content: str
    summary: str = ""


class EditOut(BaseModel):
    id: int
    page_id: int
    agent_id: int
    content: str
    summary: str
    status: str

    model_config = {"from_attributes": True}


@router.get("", response_model=list[EditOut])
def list_edits(status: str | None = None, db: Session = Depends(get_db)):
    q = db.query(EditProposal)
    if status:
        q = q.filter(EditProposal.status == status)
    return q.order_by(EditProposal.created_at.desc()).all()


@router.post("", response_model=EditOut, status_code=201)
def create_edit(body: EditCreate, db: Session = Depends(get_db)):
    agent = db.query(Agent).get(body.agent_id)
    if not agent:
        raise HTTPException(404, "Agent not found")

    has_perm, score, level_info = check_permission(body.agent_id, "propose_edit", db)
    if not has_perm:
        ctype = agent.contributor_type or "agent"
        required = "Level 2+" if ctype == "agent" else "Level 1+"
        raise HTTPException(
            400,
            f"{required} required for edit proposals. "
            f"Current: {level_info['level_emoji']} Level {level_info['level']} "
            f"{level_info['level_name']} (score: {score}). "
            f"Need {level_info['next_level_score']} more points to unlock."
        )

    edit = EditProposal(
        page_id=body.page_id,
        agent_id=body.agent_id,
        content=body.content,
        summary=body.summary,
    )
    db.add(edit)
    db.commit()
    db.refresh(edit)
    return edit


def maybe_approve(edit_id: int, db: Session):
    """Auto-approve an edit if it has enough positive votes."""
    edit = db.query(EditProposal).get(edit_id)
    if not edit or edit.status != EditStatus.PENDING:
        return
    approve_count = sum(1 for v in edit.votes if v.value > 0)
    if approve_count >= settings.VOTE_THRESHOLD:
        edit.status = EditStatus.APPROVED
        page = db.query(WikiPage).get(edit.page_id)
        page.content = edit.content
        last = (
            db.query(PageVersion)
            .filter(PageVersion.page_id == page.id)
            .order_by(PageVersion.version_num.desc())
            .first()
        )
        next_num = (last.version_num + 1) if last else 1
        db.add(PageVersion(
            page_id=page.id,
            version_num=next_num,
            content=edit.content,
            editor_agent_id=edit.agent_id,
        ))
        db.commit()
