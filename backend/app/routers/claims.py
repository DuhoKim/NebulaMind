from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy import text as _text
from typing import Optional
import math
import re
from datetime import datetime, timedelta
from datetime import datetime as _datetime

from app.config import settings
from app.database import get_db
from app.models.claim import Claim, Evidence, EvidenceVote, EvidenceComment, ClaimEditProposal, TrustAuditLog
from app.models.council import Escalation
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


# ---------------------------------------------------------------------------
# Trust v2 helpers
# ---------------------------------------------------------------------------

def _human_override_score(claim) -> float:
    """Map human_trust_override to a float contribution H."""
    mapping = {
        "consensus": 1.0,
        "accepted": 0.5,
        "debated": 0.0,
        "challenged": -0.5,
    }
    if not claim.human_trust_override:
        return 0.0
    return mapping.get(claim.human_trust_override, 0.0)


def _bucket_debate(claim, evidence: list) -> str:
    """Determine trust level for claim_type='debate' claims."""
    has_supports = any(e.stance == "supports" for e in evidence)
    has_challenges = any(e.stance == "challenges" for e in evidence)
    if has_supports and has_challenges:
        return "debated"
    elif has_supports:
        return "accepted"
    elif has_challenges:
        return "challenged"
    else:
        return "unverified"


def _has_recent_evidence(claim, days: int) -> bool:
    """Check if claim has any evidence added within `days` days (via created_at)."""
    # We check evidence.created_at via the claim's evidence relationship
    # This is called with the evidence list already loaded in recalculate_trust_v2
    # so we do a direct DB check using claim.id
    return False  # Implemented fully in recalculate_trust_v2 which passes evidence list


def _emit_event(event_name: str, **kwargs) -> None:
    """Emit a trust event. Phase 1: just print. Phase 4 will hook to Discord/Celery."""
    print(f"[trust_event] {event_name}: {kwargs}")


def _notify_trust_demotion(claim_id: int, old_level: str, new_level: str, claim_text: str) -> None:
    """Post hard demotion to #nebulamind-recruitment Discord channel."""
    try:
        import httpx
        msg = (
            f"🔴 **Hard demotion** — Claim #{claim_id} demoted: "
            f"{old_level} → **{new_level}**\n"
            f"*{claim_text}...*\n"
            f"View: https://nebulamind.net"
        )
        RECRUITMENT_WEBHOOK = "https://discord.com/api/webhooks/1489167759286997133/XspESjRMHz4x_jRT8zW3LkgF1riNNJcbykGweSkvXgfeghy0E4ETr_FaGfWtjfBg5h1K"
        httpx.post(RECRUITMENT_WEBHOOK, json={"content": msg}, timeout=5)
    except Exception:
        pass  # best-effort


def recalculate_trust_v2(
    claim_id: int,
    db: Session,
    *,
    trigger: str = "manual",
    actor_agent_id: int | None = None,
    actor_human_id: int | None = None,
) -> tuple[str, float]:
    """Compute and persist the v2 trust score for a claim.

    Returns (new_level, trust_score).
    """
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        return "unverified", 0.0

    evidence = db.query(Evidence).filter(Evidence.claim_id == claim_id).all()

    # ---- E component ----
    if not evidence:
        E = 0.0
        n_supports = n_challenges = 0
    else:
        E_sup  = sum(e.quality for e in evidence if e.stance == "supports")
        E_chal = sum(e.quality for e in evidence if e.stance == "challenges")
        # neutral counts as 0 in the numerator (context only)
        E = math.tanh((E_sup - E_chal) / 1.5)
        n_supports   = sum(1 for e in evidence if e.stance == "supports")
        n_challenges = sum(1 for e in evidence if e.stance == "challenges")

    # ---- V component ----
    if evidence:
        ev_ids = [e.id for e in evidence]
        votes = db.query(EvidenceVote).filter(EvidenceVote.evidence_id.in_(ev_ids)).all()
        n_pos = sum(v.weight for v in votes if v.value > 0)
        n_neg = sum(v.weight for v in votes if v.value < 0)
        n_total = n_pos + n_neg
        if n_total > 0:
            raw = (n_pos - n_neg) / n_total
            confidence = 1.0 - math.exp(-n_total / settings.VOTE_CONFIDENCE_HALF_LIFE)
            V = raw * confidence
        else:
            V = 0.0
    else:
        V = 0.0

    # ---- T component ----
    sup_years = [e.year for e in evidence if e.stance == "supports" and e.year]
    if sup_years:
        years_since = datetime.utcnow().year - max(sup_years)
        T = -0.05 * max(0, years_since - settings.DECAY_FREE_YEARS) / 5.0
        T = max(T, -settings.DECAY_MAX_PENALTY)
    else:
        T = 0.0

    # ---- H component ----
    H = _human_override_score(claim)

    # === Phase F: Wikipedia cross-check signal ===
    if settings.WIKIPEDIA_CROSSCHECK_ENABLED:
        from app.models.page import WikiPage
        from app.services.wikipedia_ingest import wikipedia_cross_check_score
        try:
            page = db.query(WikiPage).get(claim.page_id)
            if page and page.wikipedia_title and page.wiki_summary:
                bonus = wikipedia_cross_check_score(claim, page)
                bonus = min(bonus, settings.WIKIPEDIA_CROSSCHECK_MAX_BONUS)
                if bonus > 0:
                    V = min(1.0, V + bonus)
        except Exception:
            pass  # cross-check is advisory; never fail trust computation

    # ---- Combine ----
    TS = (
        settings.TRUST_W_EVIDENCE * E
        + settings.TRUST_W_VOTES * V
        + settings.TRUST_W_TEMPORAL * T
        + settings.TRUST_W_HUMAN * H
    )

    # ---- Bucket ----
    if claim.human_trust_override and claim.human_override_locked:
        new_level = claim.human_trust_override
    elif claim.claim_type == "debate":
        new_level = _bucket_debate(claim, evidence)
    elif not evidence and TS == 0:
        new_level = "unverified"
    elif (TS >= settings.TRUST_CONSENSUS_MIN
          and n_supports >= settings.TRUST_CONSENSUS_MIN_SUPPORTS
          and n_challenges == 0):
        new_level = "consensus"
    elif TS >= settings.TRUST_ACCEPTED_MIN:
        new_level = "accepted"
    elif TS <= settings.TRUST_CHALLENGED_MAX:
        new_level = "challenged"
    elif n_supports >= 1 and n_challenges >= 1:
        new_level = "debated"
    else:
        new_level = "unverified"

    # ---- Freshness floor ----
    if (new_level == "consensus" and sup_years
            and (datetime.utcnow().year - max(sup_years)) > settings.FRESHNESS_FLOOR_YEARS):
        # Check if any evidence was added recently
        cutoff = datetime.utcnow() - timedelta(days=settings.FRESHNESS_FLOOR_NEW_EVIDENCE_DAYS)
        recent = any(e.created_at >= cutoff for e in evidence)
        if not recent:
            new_level = "accepted"
            _emit_event("claim.stale", claim_id=claim_id)

    # ---- Persist + audit ----
    old_level = claim.trust_level
    old_score = getattr(claim, "trust_score", None)
    claim.trust_level = new_level
    claim.trust_score = TS
    claim.trust_score_updated_at = datetime.utcnow()

    # Hard demotion notification
    if new_level == "challenged" and old_level != "challenged":
        _notify_trust_demotion(claim_id, old_level, new_level, claim.text[:120] if claim.text else "")

    db.add(TrustAuditLog(
        claim_id=claim_id,
        old_level=old_level,
        new_level=new_level,
        old_score=old_score,
        new_score=TS,
        e_component=E,
        v_component=V,
        t_component=T,
        h_component=H,
        trigger=trigger,
        triggered_by_agent_id=actor_agent_id,
        triggered_by_human_id=actor_human_id,
    ))
    return new_level, TS


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
            "evidence_count": ev_count,
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
    "human_corrected":   {"icon": "✋", "color": "orange"},
    "decayed":           {"icon": "🍂", "color": "brown"},
}


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

    # Burst-grouping query: condense same-trigger runs within 1 hour
    sql = _text("""
        WITH filtered AS (
          SELECT *
          FROM trust_audit_log
          WHERE claim_id = :cid
            AND (
              :include_noop
              OR (old_level IS NOT NULL AND old_level != new_level)
              OR trigger IN ('migration','p1_consensus_push','manual_admin',
                             'human_override','p1_fix','p2_consensus_push')
            )
          ORDER BY created_at
        ),
        numbered AS (
          SELECT *,
            ROW_NUMBER() OVER (ORDER BY created_at) AS rn
          FROM filtered
        ),
        with_prev AS (
          SELECT
            a.*,
            LAG(a.trigger) OVER (ORDER BY a.created_at) AS prev_trigger,
            LAG(a.created_at) OVER (ORDER BY a.created_at) AS prev_at
          FROM filtered a
        ),
        bursts AS (
          SELECT *,
            SUM(CASE
              WHEN prev_at IS NULL THEN 1
              WHEN EXTRACT(EPOCH FROM (created_at - prev_at)) > 3600 THEN 1
              WHEN trigger != prev_trigger THEN 1
              ELSE 0
            END) OVER (ORDER BY created_at) AS burst_id
          FROM with_prev
        )
        SELECT
          burst_id,
          MIN(created_at) AS started_at,
          MAX(created_at) AS ended_at,
          MIN(trigger) AS trigger,
          (array_agg(old_level ORDER BY created_at))[1] AS level_before,
          (array_agg(new_level ORDER BY created_at DESC))[1] AS level_after,
          COALESCE(MIN(old_score), 0) AS score_before,
          COALESCE(MAX(new_score), 0) AS score_after,
          COUNT(*) AS raw_count
        FROM bursts
        GROUP BY claim_id, burst_id
        ORDER BY started_at
        LIMIT :limit
    """)

    rows = db.execute(sql, {
        "cid": claim_id,
        "include_noop": include_noop,
        "limit": min(limit, 100),
    }).fetchall()

    total_rows = db.execute(
        _text("SELECT COUNT(*) FROM trust_audit_log WHERE claim_id = :cid"),
        {"cid": claim_id}
    ).scalar() or 0

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
