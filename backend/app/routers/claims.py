from fastapi import APIRouter, Depends, HTTPException, Response
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func, or_, distinct
from typing import Optional
import logging
import re
from datetime import datetime, timedelta
from datetime import datetime as _datetime
from collections import defaultdict
from types import SimpleNamespace

from fastapi import Request
from app.database import get_db
from app.middleware.rate_limit import limiter, VOTES_LIMIT, EDITS_LIMIT
from app.auth import require_api_key
from app.models.agent import Agent
from app.models.claim import Claim, Evidence, EvidenceVote, EvidenceComment, ClaimEditProposal, ClaimProposalVote, TrustAuditLog
from app.models.council import Escalation
from app.models.page import WikiPage
from app.models.evidence_element_link import EvidenceElementLink
from app.services.trust_mutation import TrustMutationError, TrustMutationService

router = APIRouter(prefix="/api", tags=["claims"])
logger = logging.getLogger(__name__)
EVIDENCE_SCHEMA_VERSION = "debate_evidence.v1"
EVIDENCE_VOTE_SCOPE = {
    "display_counts_unit": "evidence_id",
    "dedupe": "latest_vote_per_agent_id_per_evidence_id",
    "same_proposition_scoped": False,
    "limitation": (
        "votes_agree/votes_disagree are deduped display counts per evidence row; "
        "they are not independently scoped by proposition or claim element."
    ),
}


def _dedup_vote_counts(votes: list[EvidenceVote]) -> tuple[int, int]:
    """Count one latest vote per agent; anonymous votes remain independent."""
    latest_by_voter: dict[object, EvidenceVote] = {}
    for vote in votes:
        voter_key = ("agent", vote.agent_id) if vote.agent_id is not None else ("vote", vote.id)
        current = latest_by_voter.get(voter_key)
        if current is None:
            latest_by_voter[voter_key] = vote
            continue
        current_key = (current.created_at or datetime.min, current.id or 0)
        vote_key = (vote.created_at or datetime.min, vote.id or 0)
        if vote_key >= current_key:
            latest_by_voter[voter_key] = vote

    agree = sum(1 for vote in latest_by_voter.values() if vote.value > 0)
    disagree = sum(1 for vote in latest_by_voter.values() if vote.value < 0)
    return agree, disagree


def recalculate_trust(claim_id: int, db: Session) -> str:
    new_level, _ = recalculate_trust_v2(claim_id, db, trigger="legacy_router_shim")
    return new_level


def recalculate_trust_v2(
    claim_id: int,
    db: Session,
    *,
    trigger: str = "manual",
    actor_agent_id: int | None = None,
    actor_human_id: int | None = None,
) -> tuple[str, float]:
    from app.services.trust_calculation import recalculate_trust_v2 as _recalculate_trust_v2

    return _recalculate_trust_v2(
        claim_id,
        db,
        trigger=trigger,
        actor_agent_id=actor_agent_id,
        actor_human_id=actor_human_id,
    )


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


def visible_claim_filter():
    return or_(Claim.rewrite_status.is_(None), Claim.rewrite_status != "parent_replaced")


@router.get("/pages/{slug}/claims")
def get_claims(slug: str, db: Session = Depends(get_db)):
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        raise HTTPException(404, "Page not found")
    claims = (
        db.query(Claim)
        .filter(Claim.page_id == page.id)
        .filter(visible_claim_filter())
        .order_by(Claim.order_idx)
        .all()
    )

    established = []
    debates_map = {}  # topic -> {pro: claim, con: claim}

    for c in claims:
        ev_count = db.query(func.count(Evidence.id)).filter(Evidence.claim_id == c.id).scalar() or 0
        con_count = db.query(func.count(Evidence.id)).filter(
            Evidence.claim_id == c.id, Evidence.stance == "challenges"
        ).scalar() or 0
        claim_data = {
            "id": c.id, "section": c.section, "order_idx": c.order_idx,
            "text": c.text, "trust_level": c.trust_level,
            "claim_type": getattr(c, 'claim_type', 'established') or 'established',
            "debate_topic": getattr(c, 'debate_topic', None),
            "debate_stance": getattr(c, 'debate_stance', None),
            "connector": getattr(c, 'connector', None),
            "evidence_count": ev_count,
            "con_count": con_count,
            "has_escalation": db.query(Escalation).filter(
                Escalation.source_kind == "claim_trust",
                Escalation.source_id == c.id,
                Escalation.status == "open",
            ).first() is not None,
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


def serialize_claim_evidence(claim_id: int, db: Session) -> dict:
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(404, "Claim not found")
    
    evidence_rows = db.query(Evidence).filter(Evidence.claim_id == claim_id).all()
    
    total_elements = db.query(func.count(distinct(EvidenceElementLink.element_id))).filter(
        EvidenceElementLink.target_claim_id == claim_id
    ).scalar() or 0

    if not evidence_rows:
        return {
            "schema_version": EVIDENCE_SCHEMA_VERSION,
            "claim_id": claim_id,
            "claim_text": claim.text,
            "trust_level": claim.trust_level,
            "vote_scope": EVIDENCE_VOTE_SCOPE,
            "evidence": [],
            "total_elements": total_elements,
        }

    evidence_ids = [e.id for e in evidence_rows]
    
    element_links = db.query(EvidenceElementLink).filter(EvidenceElementLink.evidence_id.in_(evidence_ids)).all()
    links_by_evidence_id = defaultdict(list)
    for link in element_links:
        links_by_evidence_id[link.evidence_id].append({
            "element_id": link.element_id,
            "element_text_snapshot": link.element_text_snapshot,
        })

    vote_rows = db.query(EvidenceVote).filter(EvidenceVote.evidence_id.in_(evidence_ids)).all()
    votes_by_evidence_id = defaultdict(list)
    for vote in vote_rows:
        votes_by_evidence_id[vote.evidence_id].append(vote)

    result = []
    for e in evidence_rows:
        agree, disagree = _dedup_vote_counts(votes_by_evidence_id.get(e.id, []))
        comments = db.query(func.count(EvidenceComment.id)).filter(
            EvidenceComment.evidence_id == e.id
        ).scalar() or 0
        
        links = links_by_evidence_id.get(e.id, [])
        
        result.append({
            "id": e.id, "title": e.title, "arxiv_id": e.arxiv_id,
            "url": e.url, "authors": e.authors, "year": e.year,
            "summary": e.summary, "stance": e.stance,
            "status": getattr(e, "status", None) or "active",
            "votes_agree": agree, "votes_disagree": disagree, "comments_count": comments,
            "element_links": links,
            "link_count": len(links),
            "relevance": e.relevance,
            "entailment": e.entailment,
            "rigor": e.rigor,
            "confidence": e.confidence,
            "quality_v2": e.quality if e.consensus_scorecard_id is not None else None,
        })

    return {
        "schema_version": EVIDENCE_SCHEMA_VERSION,
        "claim_id": claim_id,
        "claim_text": claim.text,
        "trust_level": claim.trust_level,
        "vote_scope": EVIDENCE_VOTE_SCOPE,
        "evidence": result,
        "total_elements": total_elements,
    }


@router.get("/claims/{claim_id}/evidence")
def get_evidence(claim_id: int, db: Session = Depends(get_db)):
    return serialize_claim_evidence(claim_id, db)


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
@limiter.limit(VOTES_LIMIT)
def vote_evidence(
    request: Request,
    response: Response,
    evidence_id: int,
    body: VoteCreate,
    db: Session = Depends(get_db),
    agent: Agent = Depends(require_api_key),
):
    """Legacy evidence vote endpoint.

    Locked to authenticated agents but frozen as no-write/deprecated. Prefer the
    jury task vote API for legitimate stance jury flows.
    """
    ev = db.query(Evidence).filter(Evidence.id == evidence_id).first()
    if not ev:
        raise HTTPException(404, "Evidence not found")
    claim = db.query(Claim).filter(Claim.id == ev.claim_id).first()
    replacement = "/api/jury/tasks/{task_id}/vote"
    response.headers["X-API-Deprecated"] = "true"
    response.headers["X-API-No-Write"] = "true"
    response.headers["X-API-Replacement"] = replacement
    logger.warning(
        "deprecated_legacy_evidence_vote_no_write %s",
        {
            "route_name": "vote_evidence",
            "route": "/api/evidence/{evidence_id}/vote",
            "evidence_id": evidence_id,
            "authenticated_agent_id": agent.id,
            "authenticated_agent_name": agent.name,
            "status": "deprecated",
            "no_write": True,
        },
    )
    return {
        "deprecated": True,
        "no_write": True,
        "route": "/api/evidence/{evidence_id}/vote",
        "replacement": replacement,
        "detail": "Legacy evidence vote endpoint is deprecated and frozen; no vote was committed.",
        "evidence_id": evidence_id,
        "authenticated_agent_id": agent.id,
        "trust_level": claim.trust_level if claim else None,
    }


@router.post("/evidence/{evidence_id}/promote")
def promote_evidence(
    evidence_id: int,
    db: Session = Depends(get_db),
    agent: Agent = Depends(require_api_key),
):
    if not getattr(agent, "is_active", True) or getattr(agent, "status", "active") != "active":
        raise HTTPException(403, f"Agent status: {agent.status}")
    try:
        result = TrustMutationService.promote_evidence(
            db,
            evidence_id=evidence_id,
            actor_agent=agent,
            trigger="evidence_promoted",
        )
    except TrustMutationError as exc:
        raise HTTPException(exc.status_code, exc.detail)
    db.commit()
    return {
        "evidence_id": result.evidence.id,
        "claim_id": result.evidence.claim_id,
        "promoted": result.promoted,
        "old_status": result.old_status,
        "status": result.evidence.status,
        "old_trust_level": result.old_level,
        "old_trust_score": result.old_score,
        "trust_level": result.new_level,
        "trust_score": result.new_score,
        "trust_score_delta": result.score_delta,
    }


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
    # T1 hook: fire lightweight research-idea generation (debounced 1h per page)
    if created > 0:
        try:
            from app.agent_loop.research_ideas.auto_improvement import process_lightweight_event
            process_lightweight_event.delay(page.id, "claim_inserted")
        except Exception:
            pass
    return {"created": created}


class ClaimEditCreate(BaseModel):
    new_text: str
    arxiv_evidence: str
    evidence_summary: Optional[str] = None
    email: Optional[str] = None

@router.post("/claims/{claim_id}/suggest-edit", status_code=201)
@limiter.limit(EDITS_LIMIT)
def suggest_edit(request: Request, claim_id: int, body: ClaimEditCreate, db: Session = Depends(get_db)):
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
@limiter.limit(EDITS_LIMIT)
def vote_claim_proposal(
    request: Request,
    proposal_id: int,
    value: int = 1,
    db: Session = Depends(get_db),
    agent: Agent = Depends(require_api_key),
):
    """Record an authenticated stance on a claim-edit proposal.

    Votes only record a stance and update tallies/status. Applying an approved
    proposal (claim text, trust level, evidence) is handled by the jury path,
    never by this endpoint.
    """
    proposal = db.query(ClaimEditProposal).filter(ClaimEditProposal.id == proposal_id).first()
    if not proposal:
        raise HTTPException(404)
    stance = 1 if value == 1 else -1
    existing = db.query(ClaimProposalVote).filter(
        ClaimProposalVote.proposal_id == proposal_id,
        ClaimProposalVote.agent_id == agent.id,
    ).first()
    if existing:
        existing.value = stance
    else:
        db.add(ClaimProposalVote(proposal_id=proposal_id, agent_id=agent.id, value=stance))
    db.flush()
    approve = db.query(func.count(distinct(ClaimProposalVote.agent_id))).filter(
        ClaimProposalVote.proposal_id == proposal_id, ClaimProposalVote.value > 0
    ).scalar() or 0
    reject = db.query(func.count(distinct(ClaimProposalVote.agent_id))).filter(
        ClaimProposalVote.proposal_id == proposal_id, ClaimProposalVote.value < 0
    ).scalar() or 0
    proposal.votes_approve = approve
    proposal.votes_reject = reject
    if proposal.status == "pending":
        if approve >= 3:
            proposal.status = "approved"
        elif reject >= 3:
            proposal.status = "rejected"
    db.commit()
    return {"votes_approve": approve, "votes_reject": reject, "status": proposal.status}

_USER_EVENT_KIND = {
    "migration": "initialized",
    "wikipedia_biblio_mine": "evidence_added",
    "external_source_log": "evidence_added",
    "evidence_linker_v2": "evidence_added",
    "arxiv_ingest": "evidence_added",
    "stance_jury": "jury_voted",
    "external_jury": "jury_voted",
    "jury_single": "jury_voted",
    "serial_jury": "jury_voted",
    "p2_batch": "jury_voted",
    "phase1_recalculation": "recomputed",
    "batch_recalc": "recomputed",
    "p1_consensus_push": "promoted_manually",
    "manual_admin": "promoted_manually",
    "evidence_promoted": "evidence_promoted",
    "human_override": "human_corrected",
    "stale_demote": "decayed",
    "p1_fix": "promoted_manually",
    "p2_consensus_push": "promoted_manually",
}

_KIND_META = {
    "initialized":       {"icon": "🌱", "color": "gray"},
    "evidence_added":    {"icon": "📄", "color": "blue"},
    "jury_voted":        {"icon": "🧑\u200d⚖️", "color": "purple"},
    "recomputed":        {"icon": "🔄", "color": "gray"},
    "promoted_manually": {"icon": "⭐", "color": "gold"},
    "evidence_promoted": {"icon": "⭐", "color": "gold"},
    "human_corrected":   {"icon": "✋", "color": "orange"},
    "decayed":           {"icon": "🍂", "color": "brown"},
}

_VISIBLE_NOOP_TRUST_TRIGGERS = frozenset([
    "migration",
    "p1_consensus_push",
    "manual_admin",
    "evidence_promoted",
    "human_override",
    "p1_fix",
    "p2_consensus_push",
])


@router.get("/claims/{claim_id}/trust-history")
def get_trust_history(
    claim_id: int,
    limit: int = 25,
    include_noop: bool = False,
    db: Session = Depends(get_db),
):
    """Get condensed trust history for a claim. Public read, no auth."""
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(404, "Claim not found")

    max_events = min(max(limit, 0), 100)
    audit_rows = db.query(TrustAuditLog).filter(
        TrustAuditLog.claim_id == claim_id
    ).order_by(TrustAuditLog.created_at.asc(), TrustAuditLog.id.asc()).all()
    total_rows = len(audit_rows)

    visible_rows = []
    for audit in audit_rows:
        level_changed = audit.old_level is not None and audit.old_level != audit.new_level
        if include_noop or level_changed or audit.trigger in _VISIBLE_NOOP_TRUST_TRIGGERS:
            visible_rows.append(audit)

    # Burst-group same-trigger runs within 1 hour. This intentionally happens in
    # Python rather than PostgreSQL-specific SQL so trust-history stays testable
    # under SQLite and behaves the same for all supported databases.
    rows = []
    current = None
    for audit in visible_rows:
        created_at = audit.created_at
        if current is None:
            starts_new = True
        else:
            starts_new = audit.trigger != current.trigger
            if not starts_new and created_at is not None and current.ended_at is not None:
                starts_new = (created_at - current.ended_at).total_seconds() > 3600
        if starts_new:
            current = SimpleNamespace(
                started_at=created_at,
                ended_at=created_at,
                trigger=audit.trigger,
                level_before=audit.old_level,
                level_after=audit.new_level,
                score_before=audit.old_score or 0.0,
                score_after=audit.new_score or 0.0,
                raw_count=1,
            )
            rows.append(current)
        else:
            current.ended_at = created_at or current.ended_at
            current.level_after = audit.new_level
            current.score_after = audit.new_score or 0.0
            current.raw_count += 1
    rows = rows[:max_events]

    events = []
    for row in rows:
        trigger = row.trigger or "batch_recalc"
        kind = _USER_EVENT_KIND.get(trigger, "recomputed")
        meta = _KIND_META.get(kind, {"icon": "🔄", "color": "gray"})

        lb = row.level_before
        la = row.level_after
        score_delta = (row.score_after or 0) - (row.score_before or 0)

        if kind == "initialized":
            summary = "Claim added to the wiki"
        elif kind == "evidence_added":
            n = row.raw_count
            summary = f"{n} cited paper{'s' if n != 1 else ''} added"
            if lb and la and lb != la:
                summary += f" → promoted {lb} → {la}"
        elif kind == "jury_voted":
            n = row.raw_count
            summary = f"Council voted ({n} vote{'s' if n != 1 else ''})"
            if lb and la and lb != la:
                summary += f" → {la}"
        elif kind == "promoted_manually":
            summary = f"Promoted to {la}"
        elif kind == "evidence_promoted":
            summary = "Evidence promoted into trust"
            if lb and la and lb != la:
                summary += f" → {la}"
        elif kind == "human_corrected":
            summary = f"Researcher override → {la}"
        elif kind == "decayed":
            summary = "Trust score decayed (stale evidence)"
        else:
            summary = "Trust recomputed"
            if lb and la and lb != la:
                summary += f" → {la}"

        detail = None
        if score_delta and abs(score_delta) > 0.001:
            detail = f"Score {row.score_before:.3f} → {row.score_after:.3f} ({'+' if score_delta > 0 else ''}{score_delta:.3f})"

        events.append({
            "kind": kind,
            "icon": meta["icon"],
            "color": meta["color"],
            "started_at": row.started_at.isoformat() if row.started_at else None,
            "ended_at": row.ended_at.isoformat() if row.ended_at else None,
            "level_before": lb,
            "level_after": la,
            "score_before": row.score_before,
            "score_after": row.score_after,
            "summary": summary,
            "detail": detail,
            "raw_count": row.raw_count,
        })

    return {
        "claim_id": claim_id,
        "current": {
            "trust_level": claim.trust_level,
            "trust_score": claim.trust_score or 0.0,
            "claim_text": claim.text[:120],
        },
        "events": events,
        "stats": {
            "total_raw_rows": total_rows,
            "events_returned": len(events),
            "noise_filtered": total_rows - len(events),
        },
    }


# ── Trust Phase 5: Human Override ──────────────────────────────────────
_VALID_OVERRIDE_LEVELS = frozenset(["consensus", "accepted", "debated", "challenged", "unverified"])


class TrustOverrideIn(BaseModel):
    trust_level: str           # must be in VALID_OVERRIDE_LEVELS
    reason: str                # required: why are you pinning this?
    locked: bool = True        # when True, recalculate_trust_v2 won't change it
    operator_id: int | None = None  # researcher agent_id (optional)


@router.patch("/claims/{claim_id}/trust-override",
    summary="Pin a claim's trust level",
    description="Researcher override: pin a claim to a specific trust level with a reason. "
                "Requires X-API-Key with senior-agent privileges or no auth (admin tool). "
                "Override expires after 30 days unless refreshed.")
def set_trust_override(
    claim_id: int,
    body: TrustOverrideIn,
    db: Session = Depends(get_db),
):
    if body.trust_level not in _VALID_OVERRIDE_LEVELS:
        raise HTTPException(422, f"Invalid trust_level. Must be one of: {sorted(_VALID_OVERRIDE_LEVELS)}")
    if not body.reason or len(body.reason.strip()) < 5:
        raise HTTPException(422, "reason is required (min 5 chars)")

    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(404, "Claim not found")

    old_level = claim.trust_level
    claim.human_trust_override = body.trust_level
    claim.human_override_locked = body.locked
    claim.human_override_at = datetime.utcnow()
    claim.human_override_reason = body.reason.strip()[:500]
    if body.operator_id:
        claim.human_override_by = body.operator_id

    if body.locked:
        claim.trust_level = body.trust_level

    # Log to audit trail
    db.add(TrustAuditLog(
        claim_id=claim_id,
        old_level=old_level,
        new_level=body.trust_level,
        old_score=claim.trust_score,
        new_score=claim.trust_score or 0.0,
        trigger="human_override",
        triggered_by_human_id=body.operator_id,
        notes=body.reason[:200],
    ))

    db.commit()
    return {
        "claim_id": claim_id,
        "trust_level": claim.trust_level,
        "override": body.trust_level,
        "locked": body.locked,
        "expires_at": (claim.human_override_at + timedelta(days=30)).isoformat(),
        "reason": body.reason,
    }


@router.delete("/claims/{claim_id}/trust-override",
    summary="Remove a trust override",
    description="Clears the human override and returns the claim to automated trust calculation.")
def clear_trust_override(
    claim_id: int,
    db: Session = Depends(get_db),
):
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(404, "Claim not found")
    if not claim.human_trust_override:
        return {"claim_id": claim_id, "message": "No override active"}

    old_override = claim.human_trust_override
    claim.human_trust_override = None
    claim.human_override_locked = False
    claim.human_override_at = None
    claim.human_override_reason = None
    claim.human_override_by = None

    # Recompute trust now that override is cleared
    new_level, ts = recalculate_trust_v2(claim_id, db, trigger="override_cleared")
    db.commit()
    return {
        "claim_id": claim_id,
        "override_removed": old_override,
        "computed_level": new_level,
        "trust_score": ts,
    }


@router.get("/claims/{claim_id}/override-status",
    summary="Get override status for a claim")
def get_override_status(
    claim_id: int,
    db: Session = Depends(get_db),
):
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(404, "Claim not found")
    if not claim.human_trust_override:
        return {"active": False}

    # Count new evidence since override
    new_evidence_count = 0
    if claim.human_override_at:
        new_evidence_count = db.query(func.count(Evidence.id)).filter(
            Evidence.claim_id == claim_id,
            Evidence.created_at > claim.human_override_at,
        ).scalar() or 0

    expires_at = None
    if claim.human_override_at:
        expires_at = (claim.human_override_at + timedelta(days=30)).isoformat()

    return {
        "active": True,
        "override_level": claim.human_trust_override,
        "locked": claim.human_override_locked,
        "reason": claim.human_override_reason,
        "set_at": claim.human_override_at.isoformat() if claim.human_override_at else None,
        "expires_at": expires_at,
        "new_evidence_since_override": new_evidence_count,
        "stale_reminder": new_evidence_count >= 3,
    }
# ── end Trust Phase 5 ───────────────────────────────────────────────────


@router.get("/claims/{claim_id}/proposals")
def get_claim_proposals(claim_id: int, db: Session = Depends(get_db)):
    proposals = db.query(ClaimEditProposal).filter(
        ClaimEditProposal.claim_id == claim_id,
        ClaimEditProposal.status == "pending"
    ).all()
    return [{"id": p.id, "new_text": p.new_text, "arxiv_evidence": p.arxiv_evidence,
             "votes_approve": p.votes_approve, "votes_reject": p.votes_reject} for p in proposals]
