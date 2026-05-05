"""
new_page_proposals router (Phase E / PR-10)

Endpoints:
  GET    /api/new-page-proposals              - list proposals (paginated)
  GET    /api/new-page-proposals/{id}         - detail with cluster paper titles
  POST   /api/new-page-proposals/{id}/accept  - accept and create WikiPage
  POST   /api/new-page-proposals/{id}/reject  - reject proposal
"""
import json
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.external import NewPageProposal
from app.models.page import WikiPage

router = APIRouter(prefix="/api/new-page-proposals", tags=["new-page-proposals"])


# ---------------------------------------------------------------------------
# Schemas
# ---------------------------------------------------------------------------

class AcceptBody(BaseModel):
    slug: Optional[str] = None
    category: Optional[str] = None


class RejectBody(BaseModel):
    reason: Optional[str] = None


# ---------------------------------------------------------------------------
# GET /api/new-page-proposals
# ---------------------------------------------------------------------------

@router.get("")
def list_proposals(
    status: Optional[str] = "pending",
    offset: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
):
    """List new-page proposals (default: pending, paginated)."""
    q = db.query(NewPageProposal)
    if status:
        q = q.filter(NewPageProposal.status == status)
    total = q.count()
    proposals = q.order_by(NewPageProposal.created_at.desc()).offset(offset).limit(limit).all()

    return {
        "total": total,
        "offset": offset,
        "limit": limit,
        "items": [
            {
                "id": p.id,
                "suggested_slug": p.suggested_slug,
                "suggested_title": p.suggested_title,
                "centroid_similarity": p.centroid_similarity,
                "status": p.status,
                "notified_at": p.notified_at.isoformat() if p.notified_at else None,
                "created_at": p.created_at.isoformat() if p.created_at else None,
                "paper_count": len(json.loads(p.cluster_papers)) if p.cluster_papers else 0,
            }
            for p in proposals
        ],
    }


# ---------------------------------------------------------------------------
# GET /api/new-page-proposals/{id}
# ---------------------------------------------------------------------------

@router.get("/{proposal_id}")
def get_proposal(proposal_id: int, db: Session = Depends(get_db)):
    """Detail view: includes cluster paper arxiv IDs."""
    p = db.query(NewPageProposal).filter(NewPageProposal.id == proposal_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Proposal not found")

    arxiv_ids: list[str] = json.loads(p.cluster_papers) if p.cluster_papers else []

    return {
        "id": p.id,
        "suggested_slug": p.suggested_slug,
        "suggested_title": p.suggested_title,
        "centroid_similarity": p.centroid_similarity,
        "status": p.status,
        "notified_at": p.notified_at.isoformat() if p.notified_at else None,
        "created_at": p.created_at.isoformat() if p.created_at else None,
        "resulting_page_id": p.resulting_page_id,
        "paper_count": len(arxiv_ids),
        "cluster_papers": arxiv_ids,
    }


# ---------------------------------------------------------------------------
# POST /api/new-page-proposals/{id}/accept
# ---------------------------------------------------------------------------

@router.post("/{proposal_id}/accept")
def accept_proposal(proposal_id: int, body: AcceptBody, db: Session = Depends(get_db)):
    """Accept a proposal: creates a new WikiPage and marks proposal accepted."""
    p = db.query(NewPageProposal).filter(NewPageProposal.id == proposal_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Proposal not found")
    if p.status != "pending":
        raise HTTPException(status_code=409, detail=f"Proposal is already '{p.status}'")

    final_slug = (body.slug or p.suggested_slug).strip()
    if not final_slug:
        raise HTTPException(status_code=422, detail="slug must not be empty")

    # Guard against duplicate slugs
    existing = db.query(WikiPage).filter(WikiPage.slug == final_slug).first()
    if existing:
        raise HTTPException(status_code=409, detail=f"A page with slug '{final_slug}' already exists")

    new_page = WikiPage(
        title=p.suggested_title,
        slug=final_slug,
        content="",
        category=body.category,
    )
    db.add(new_page)
    db.flush()  # populate new_page.id

    p.status = "accepted"
    p.resulting_page_id = new_page.id
    db.commit()
    db.refresh(new_page)

    return {
        "id": p.id,
        "status": "accepted",
        "page_id": new_page.id,
        "slug": new_page.slug,
    }


# ---------------------------------------------------------------------------
# POST /api/new-page-proposals/{id}/reject
# ---------------------------------------------------------------------------

@router.post("/{proposal_id}/reject")
def reject_proposal(proposal_id: int, body: RejectBody, db: Session = Depends(get_db)):
    """Reject a proposal."""
    p = db.query(NewPageProposal).filter(NewPageProposal.id == proposal_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Proposal not found")
    if p.status != "pending":
        raise HTTPException(status_code=409, detail=f"Proposal is already '{p.status}'")

    p.status = "rejected"
    db.commit()

    return {"id": p.id, "status": "rejected"}
