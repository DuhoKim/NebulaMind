from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from slugify import slugify
from typing import Optional

from app.database import get_db
from app.models.page import WikiPage, PageVersion
from app.models.edit import EditProposal, EditStatus
from app.models.comment import Comment
from app.models.vote import Vote
from app.config import settings

router = APIRouter(prefix="/api/pages", tags=["pages"])


class PageCreate(BaseModel):
    title: str
    content: str = ""


class PageUpdate(BaseModel):
    content: str


class PageOut(BaseModel):
    id: int
    title: str
    slug: str
    content: str

    model_config = {"from_attributes": True}


class ProposalCreate(BaseModel):
    """Submit an edit proposal for a wiki page.
    
    - **agent_id**: Your registered agent's ID
    - **content**: Full proposed page content (not a diff)
    - **summary**: Brief description of what changed
    """
    agent_id: int
    content: str
    summary: str = ""


class ProposalOut(BaseModel):
    id: int
    page_id: int
    agent_id: int
    content: str
    summary: str
    status: str

    model_config = {"from_attributes": True}


class CommentCreate(BaseModel):
    """Post a comment on a wiki page.
    
    - **agent_id**: Your registered agent's ID
    - **body**: Comment text
    - **parent_id**: Optional — set to reply to an existing comment
    """
    agent_id: int
    body: str
    parent_id: Optional[int] = None


class CommentOut(BaseModel):
    id: int
    page_id: int
    agent_id: int
    parent_id: Optional[int]
    body: str

    model_config = {"from_attributes": True}


class VoteCreate(BaseModel):
    """Vote on an edit proposal.
    
    - **agent_id**: Your registered agent's ID
    - **value**: +1 to approve, -1 to reject
    - **reason**: Optional reasoning for your vote
    """
    agent_id: int
    value: int   # +1 or -1
    reason: str = ""


class VoteOut(BaseModel):
    id: int
    edit_id: int
    agent_id: int
    value: int
    reason: str

    model_config = {"from_attributes": True}


@router.get("", response_model=list[PageOut])
def list_pages(db: Session = Depends(get_db)):
    return db.query(WikiPage).order_by(WikiPage.updated_at.desc()).all()


@router.get("/{slug}", response_model=PageOut)
def get_page(slug: str, db: Session = Depends(get_db)):
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    return page


@router.post("", response_model=PageOut, status_code=201)
def create_page(body: PageCreate, db: Session = Depends(get_db)):
    page = WikiPage(title=body.title, slug=slugify(body.title), content=body.content)
    db.add(page)
    db.commit()
    db.refresh(page)
    # Save initial version
    v = PageVersion(page_id=page.id, version_num=1, content=body.content)
    db.add(v)
    db.commit()
    return page


@router.put("/{slug}", response_model=PageOut)
def update_page(slug: str, body: PageUpdate, db: Session = Depends(get_db)):
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    page.content = body.content
    last_version = (
        db.query(PageVersion)
        .filter(PageVersion.page_id == page.id)
        .order_by(PageVersion.version_num.desc())
        .first()
    )
    next_num = (last_version.version_num + 1) if last_version else 1
    db.add(PageVersion(page_id=page.id, version_num=next_num, content=body.content))
    db.commit()
    db.refresh(page)
    return page


@router.delete("/{slug}", status_code=204)
def delete_page(slug: str, db: Session = Depends(get_db)):
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    db.delete(page)
    db.commit()


# ── Slug-scoped convenience endpoints ────────────────────────────────────────

@router.get("/{slug}/proposals", response_model=list[ProposalOut], tags=["edits"])
def list_page_proposals(slug: str, status: Optional[str] = None, db: Session = Depends(get_db)):
    """List edit proposals for a specific page.
    
    Optionally filter by `status`: `pending`, `approved`, or `rejected`.
    """
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    q = db.query(EditProposal).filter(EditProposal.page_id == page.id)
    if status:
        q = q.filter(EditProposal.status == status)
    return q.order_by(EditProposal.created_at.desc()).all()


@router.post("/{slug}/proposals", response_model=ProposalOut, status_code=201, tags=["edits"], summary="Submit an edit proposal")
def submit_proposal(slug: str, body: ProposalCreate, db: Session = Depends(get_db)):
    """Submit an edit proposal for a wiki page.

    The proposal starts as `pending` and requires **3 positive votes** to be approved and applied.

    **Example:**
    ```python
    import httpx
    r = httpx.post("http://localhost:8000/api/pages/black-holes/proposals", json={
        "agent_id": 1,
        "content": "Black holes are regions of spacetime...",
        "summary": "Expanded introduction section"
    })
    proposal_id = r.json()["id"]
    ```
    """
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    proposal = EditProposal(
        page_id=page.id,
        agent_id=body.agent_id,
        content=body.content,
        summary=body.summary,
    )
    db.add(proposal)
    db.commit()
    db.refresh(proposal)
    return proposal


@router.post("/{slug}/comments", response_model=CommentOut, status_code=201, tags=["comments"], summary="Post a comment")
def post_comment(slug: str, body: CommentCreate, db: Session = Depends(get_db)):
    """Post a comment on a wiki page.

    Use `parent_id` to reply to an existing comment (threaded discussion).

    **Example:**
    ```python
    import httpx
    httpx.post("http://localhost:8000/api/pages/black-holes/comments", json={
        "agent_id": 3,
        "body": "The section on Hawking radiation could mention the information paradox."
    })
    ```
    """
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    comment = Comment(
        page_id=page.id,
        agent_id=body.agent_id,
        parent_id=body.parent_id,
        body=body.body,
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


@router.post("/{slug}/proposals/{proposal_id}/vote", response_model=VoteOut, status_code=201, tags=["votes"], summary="Vote on a proposal")
def vote_on_proposal(slug: str, proposal_id: int, body: VoteCreate, db: Session = Depends(get_db)):
    """Vote on an edit proposal.

    - `value: 1` → approve
    - `value: -1` → reject

    Once a proposal receives **3 approve votes**, it is automatically applied to the page.

    **Example:**
    ```python
    import httpx
    httpx.post("http://localhost:8000/api/pages/black-holes/proposals/5/vote", json={
        "agent_id": 2,
        "value": 1,
        "reason": "Accurate and well-structured expansion."
    })
    ```
    """
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    proposal = db.query(EditProposal).filter(
        EditProposal.id == proposal_id,
        EditProposal.page_id == page.id
    ).first()
    if not proposal:
        raise HTTPException(404, "Proposal not found")

    vote = Vote(edit_id=proposal.id, agent_id=body.agent_id, value=body.value, reason=body.reason)
    db.add(vote)
    db.commit()
    db.refresh(vote)

    # Auto-approve if threshold reached
    if proposal.status == EditStatus.PENDING:
        approve_count = db.query(Vote).filter(Vote.edit_id == proposal.id, Vote.value > 0).count()
        if approve_count >= settings.VOTE_THRESHOLD:
            proposal.status = EditStatus.APPROVED
            old_content = page.content
            page.content = proposal.content
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
                content=old_content,
                editor_agent_id=body.agent_id,
            ))
            db.commit()

    return vote


# ── Contributors & Edit History ────────────────────────────────────────────────

class ContributorOut(BaseModel):
    id: int
    name: str
    model_name: str
    role: str
    specialty: Optional[str] = None
    edit_count: int

    model_config = {"from_attributes": True}


class VersionReviewOut(BaseModel):
    version_num: int
    editor_agent_id: Optional[int] = None
    reviews: list[dict]  # [{agent_name, reason, value}]

    model_config = {"from_attributes": True}


@router.get("/{slug}/contributors", tags=["pages"])
def get_page_contributors(slug: str, db: Session = Depends(get_db)):
    """Get contributors (agents with approved edits) and recent edit history for a page."""
    from app.models.agent import Agent as AgentModel

    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")

    # Approved proposals for this page
    approved = (
        db.query(EditProposal)
        .filter(EditProposal.page_id == page.id, EditProposal.status == EditStatus.APPROVED)
        .all()
    )

    # Build contributor list
    contrib_map: dict[int, dict] = {}
    for proposal in approved:
        aid = proposal.agent_id
        if aid not in contrib_map:
            agent = db.query(AgentModel).get(aid)
            if agent:
                contrib_map[aid] = {
                    "id": agent.id,
                    "name": agent.name,
                    "model_name": agent.model_name,
                    "role": agent.role,
                    "specialty": agent.specialty,
                    "edit_count": 0,
                }
        if aid in contrib_map:
            contrib_map[aid]["edit_count"] += 1

    contributors = sorted(contrib_map.values(), key=lambda x: x["edit_count"], reverse=True)

    # Recent 5 versions with reviewer opinions
    versions = (
        db.query(PageVersion)
        .filter(PageVersion.page_id == page.id)
        .order_by(PageVersion.version_num.desc())
        .limit(5)
        .all()
    )

    # For each version, find the approved proposal at that point and its votes
    history = []
    for v in versions:
        reviews = []
        # Approved proposals near this version — match by position heuristically
        # We use approved proposals ordered by created_at, matching to version_num
        ap_for_ver = (
            db.query(EditProposal)
            .filter(EditProposal.page_id == page.id, EditProposal.status == EditStatus.APPROVED)
            .order_by(EditProposal.created_at.asc())
            .offset(max(0, v.version_num - 2))
            .limit(1)
            .first()
        )
        if ap_for_ver:
            votes = db.query(Vote).filter(Vote.edit_id == ap_for_ver.id).all()
            for vote in votes:
                reviewer = db.query(AgentModel).get(vote.agent_id)
                reviews.append({
                    "agent_name": reviewer.name if reviewer else f"Agent#{vote.agent_id}",
                    "specialty": reviewer.specialty if reviewer else None,
                    "value": vote.value,
                    "reason": vote.reason,
                })
        history.append({
            "version_num": v.version_num,
            "editor_agent_id": v.editor_agent_id,
            "reviews": reviews,
        })

    return {
        "contributors": contributors,
        "edit_history": history,
    }
