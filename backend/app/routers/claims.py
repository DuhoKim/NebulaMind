from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional
import re

from app.database import get_db
from app.models.claim import Claim, Evidence, EvidenceVote, EvidenceComment
from app.models.page import WikiPage

router = APIRouter(prefix="/api", tags=["claims"])


def recalculate_trust(claim_id: int, db: Session) -> str:
    evidence = db.query(Evidence).filter(Evidence.claim_id == claim_id).all()
    if not evidence:
        return "unverified"
    supports = sum(1 for e in evidence if e.stance == "supports")
    challenges = sum(1 for e in evidence if e.stance == "challenges")
    total_agree = 0
    total_disagree = 0
    for e in evidence:
        total_agree += db.query(func.count(EvidenceVote.id)).filter(
            EvidenceVote.evidence_id == e.id, EvidenceVote.value == 1
        ).scalar() or 0
        total_disagree += db.query(func.count(EvidenceVote.id)).filter(
            EvidenceVote.evidence_id == e.id, EvidenceVote.value == -1
        ).scalar() or 0
    total_votes = total_agree + total_disagree
    if total_votes == 0:
        return "accepted" if supports >= 1 and challenges == 0 else "unverified"
    agree_ratio = total_agree / total_votes
    if supports >= 3 and challenges == 0 and agree_ratio >= 0.8:
        return "consensus"
    elif agree_ratio >= 0.5:
        return "accepted"
    elif agree_ratio >= 0.4:
        return "debated"
    else:
        return "challenged"


class ClaimOut(BaseModel):
    id: int
    section: str
    order_idx: int
    text: str
    trust_level: str
    evidence_count: int
    class Config:
        from_attributes = True


@router.get("/pages/{slug}/claims")
def get_claims(slug: str, db: Session = Depends(get_db)):
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    claims = db.query(Claim).filter(Claim.page_id == page.id).order_by(Claim.order_idx).all()
    result = []
    for c in claims:
        ev_count = db.query(func.count(Evidence.id)).filter(Evidence.claim_id == c.id).scalar() or 0
        result.append({
            "id": c.id, "section": c.section, "order_idx": c.order_idx,
            "text": c.text, "trust_level": c.trust_level, "evidence_count": ev_count
        })
    sections = {}
    for r in result:
        s = r["section"]
        if s not in sections:
            sections[s] = []
        sections[s].append(r)
    return {"page_id": page.id, "sections": [{"name": k, "claims": v} for k, v in sections.items()]}


class EvidenceCreate(BaseModel):
    title: str
    arxiv_id: Optional[str] = None
    doi: Optional[str] = None
    url: Optional[str] = None
    authors: Optional[str] = None
    year: Optional[int] = None
    summary: Optional[str] = None
    stance: str = "supports"
    agent_id: Optional[int] = None


@router.get("/claims/{claim_id}/evidence")
def get_evidence(claim_id: int, db: Session = Depends(get_db)):
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(404, "Claim not found")
    evidence = db.query(Evidence).filter(Evidence.claim_id == claim_id).all()
    result = []
    for e in evidence:
        agree = db.query(func.count(EvidenceVote.id)).filter(
            EvidenceVote.evidence_id == e.id, EvidenceVote.value == 1
        ).scalar() or 0
        disagree = db.query(func.count(EvidenceVote.id)).filter(
            EvidenceVote.evidence_id == e.id, EvidenceVote.value == -1
        ).scalar() or 0
        comments = db.query(func.count(EvidenceComment.id)).filter(
            EvidenceComment.evidence_id == e.id
        ).scalar() or 0
        result.append({
            "id": e.id, "title": e.title, "arxiv_id": e.arxiv_id,
            "url": e.url, "authors": e.authors, "year": e.year,
            "summary": e.summary, "stance": e.stance,
            "votes_agree": agree, "votes_disagree": disagree, "comments_count": comments
        })
    return {"claim_id": claim_id, "claim_text": claim.text, "trust_level": claim.trust_level, "evidence": result}


@router.post("/claims/{claim_id}/evidence", status_code=201)
def add_evidence(claim_id: int, body: EvidenceCreate, db: Session = Depends(get_db)):
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(404, "Claim not found")
    ev = Evidence(
        claim_id=claim_id, title=body.title, arxiv_id=body.arxiv_id,
        doi=body.doi, url=body.url, authors=body.authors, year=body.year,
        summary=body.summary, stance=body.stance, added_by_agent_id=body.agent_id
    )
    db.add(ev)
    db.flush()
    claim.trust_level = recalculate_trust(claim_id, db)
    db.commit()
    return {"id": ev.id, "trust_level": claim.trust_level}


class VoteCreate(BaseModel):
    value: int
    agent_id: Optional[int] = None
    reason: Optional[str] = None


@router.post("/evidence/{evidence_id}/vote")
def vote_evidence(evidence_id: int, body: VoteCreate, db: Session = Depends(get_db)):
    ev = db.query(Evidence).filter(Evidence.id == evidence_id).first()
    if not ev:
        raise HTTPException(404, "Evidence not found")
    vote = EvidenceVote(evidence_id=evidence_id, value=body.value, agent_id=body.agent_id, reason=body.reason)
    db.add(vote)
    db.flush()
    claim = db.query(Claim).filter(Claim.id == ev.claim_id).first()
    if claim:
        claim.trust_level = recalculate_trust(claim.id, db)
    db.commit()
    return {"trust_level": claim.trust_level if claim else None}


class CommentCreate(BaseModel):
    body: str
    agent_id: Optional[int] = None


@router.post("/evidence/{evidence_id}/comments", status_code=201)
def add_comment(evidence_id: int, body: CommentCreate, db: Session = Depends(get_db)):
    ev = db.query(Evidence).filter(Evidence.id == evidence_id).first()
    if not ev:
        raise HTTPException(404, "Evidence not found")
    comment = EvidenceComment(evidence_id=evidence_id, body=body.body, agent_id=body.agent_id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return {"id": comment.id}


@router.get("/evidence/{evidence_id}/comments")
def get_comments(evidence_id: int, db: Session = Depends(get_db)):
    comments = db.query(EvidenceComment).filter(EvidenceComment.evidence_id == evidence_id).all()
    return [{"id": c.id, "body": c.body, "agent_id": c.agent_id, "created_at": c.created_at.isoformat()} for c in comments]


@router.post("/pages/{slug}/decompose")
def decompose_page(slug: str, db: Session = Depends(get_db)):
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    existing = db.query(func.count(Claim.id)).filter(Claim.page_id == page.id).scalar()
    if existing > 0:
        return {"message": f"Already decomposed ({existing} claims)"}
    current_section = "Overview"
    order = 0
    created = 0
    for line in (page.content or "").split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("## "):
            current_section = line[3:].strip()
            continue
        if line.startswith("#") or line.startswith("---"):
            continue
        text = re.sub(r"\*\*(.+?)\*\*", r"\1", line.lstrip("-*\u2022\u25b8 ").strip())
        text = re.sub(r"\*(.+?)\*", r"\1", text)
        text = re.sub(r"`(.+?)`", r"\1", text)
        text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text).strip()
        if len(text) < 15:
            continue
        db.add(Claim(page_id=page.id, section=current_section, order_idx=order, text=text))
        order += 1
        created += 1
    db.commit()
    return {"created": created}
