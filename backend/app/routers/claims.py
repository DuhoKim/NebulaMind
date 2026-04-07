from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional
import re

from app.database import get_db
from app.models.claim import Claim, Evidence, EvidenceVote, EvidenceComment, ClaimEditProposal
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
    connector: str | None = None
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

    established = []
    debates_map = {}  # topic -> {pro: claim, con: claim}

    for c in claims:
        ev_count = db.query(func.count(Evidence.id)).filter(Evidence.claim_id == c.id).scalar() or 0
        claim_data = {
            "id": c.id, "section": c.section, "order_idx": c.order_idx,
            "text": c.text, "trust_level": c.trust_level,
            "claim_type": getattr(c, 'claim_type', 'established') or 'established',
            "debate_topic": getattr(c, 'debate_topic', None),
            "debate_stance": getattr(c, 'debate_stance', None),
            "connector": getattr(c, 'connector', None),
            "evidence_count": ev_count
        }

        ct = claim_data["claim_type"]
        if ct == "debate" and claim_data["debate_topic"]:
            topic = claim_data["debate_topic"]
            if topic not in debates_map:
                debates_map[topic] = {"pro": None, "con": None}
            stance = claim_data["debate_stance"]
            if stance in ("pro", "con"):
                debates_map[topic][stance] = claim_data
        else:
            established.append(claim_data)

    # Group established by section
    sections = {}
    for r in established:
        s = r["section"]
        if s not in sections:
            sections[s] = []
        sections[s].append(r)

    # Debates as list
    debates = [
        {"topic": topic, "pro": v["pro"], "con": v["con"]}
        for topic, v in debates_map.items()
        if v["pro"] or v["con"]
    ]

    return {
        "page_id": page.id,
        "sections": [{"name": k, "claims": v} for k, v in sections.items()],
        "debates": debates
    }


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


class ClaimEditCreate(BaseModel):
    new_text: str
    arxiv_evidence: str
    evidence_summary: Optional[str] = None
    email: Optional[str] = None

@router.post("/claims/{claim_id}/suggest-edit", status_code=201)
def suggest_edit(claim_id: int, body: ClaimEditCreate, db: Session = Depends(get_db)):
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(404, "Claim not found")
    if not body.arxiv_evidence.strip():
        raise HTTPException(400, "arXiv evidence ID is required")
    proposal = ClaimEditProposal(
        claim_id=claim_id, original_text=claim.text, new_text=body.new_text,
        arxiv_evidence=body.arxiv_evidence.strip()[:50],
        evidence_summary=body.evidence_summary, email=body.email,
    )
    db.add(proposal)
    db.commit()
    db.refresh(proposal)
    return {"id": proposal.id, "status": "pending"}

@router.post("/claim-proposals/{proposal_id}/vote")
def vote_claim_proposal(proposal_id: int, value: int = 1, db: Session = Depends(get_db)):
    proposal = db.query(ClaimEditProposal).filter(ClaimEditProposal.id == proposal_id).first()
    if not proposal:
        raise HTTPException(404)
    if value == 1:
        proposal.votes_approve += 1
    else:
        proposal.votes_reject += 1
    if proposal.votes_approve >= 3 and proposal.status == "pending":
        claim = db.query(Claim).filter(Claim.id == proposal.claim_id).first()
        if claim:
            claim.text = proposal.new_text
            claim.trust_level = "accepted"
            ev = Evidence(
                claim_id=claim.id,
                title=f"arXiv:{proposal.arxiv_evidence}",
                arxiv_id=proposal.arxiv_evidence[:30],
                url=f"https://arxiv.org/abs/{proposal.arxiv_evidence}",
                summary=proposal.evidence_summary or "Community-submitted evidence",
                stance="supports",
            )
            db.add(ev)
            proposal.status = "approved"
    elif proposal.votes_reject >= 3:
        proposal.status = "rejected"
    db.commit()
    return {"votes_approve": proposal.votes_approve, "votes_reject": proposal.votes_reject, "status": proposal.status}

@router.get("/claims/{claim_id}/proposals")
def get_claim_proposals(claim_id: int, db: Session = Depends(get_db)):
    proposals = db.query(ClaimEditProposal).filter(
        ClaimEditProposal.claim_id == claim_id,
        ClaimEditProposal.status == "pending"
    ).all()
    return [{"id": p.id, "new_text": p.new_text, "arxiv_evidence": p.arxiv_evidence,
             "votes_approve": p.votes_approve, "votes_reject": p.votes_reject} for p in proposals]
