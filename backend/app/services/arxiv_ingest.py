"""
arXiv paper ingest handlers (Phase B, PR-3).

Three handlers, one for each match_type from arxiv_classifier:
  - handle_claim_evidence   → verify paper via paper_search, insert Evidence
  - handle_page_extension   → propose a wiki edit via LLM (_chat with editor role)
  - handle_new_topic        → stage a NewPageProposal cluster entry

All handlers are idempotent, write exactly one ExternalSourceLog row, and
respect throttle settings from config.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timedelta
from typing import TYPE_CHECKING

from sqlalchemy.orm import Session

from app.config import settings

if TYPE_CHECKING:
    from app.models.arxiv import ArxivPaper
    from app.models.agent import Agent

log = logging.getLogger(__name__)


# --------------------------------------------------------------------------
# Internal helpers
# --------------------------------------------------------------------------

def _log_external(
    db: Session,
    *,
    source: str,
    external_id: str,
    page_id: int | None = None,
    claim_id: int | None = None,
    evidence_id: int | None = None,
    decision: str,
    quality: float | None = None,
    notes: str | None = None,
) -> None:
    from app.models.external import ExternalSourceLog
    db.add(ExternalSourceLog(
        source=source,
        external_id=external_id,
        page_id=page_id,
        claim_id=claim_id,
        evidence_id=evidence_id,
        decision=decision,
        quality=quality,
        notes=notes,
    ))


def _already_processed(db: Session, arxiv_id: str, source_channel: str) -> bool:
    """True if an Evidence row with this arxiv_id + source_channel already exists."""
    from app.models.claim import Evidence
    return db.query(Evidence).filter(
        Evidence.arxiv_id == arxiv_id,
        Evidence.source_channel == source_channel,
    ).first() is not None


def _maybe_fallback_page_extension(
    paper: "ArxivPaper",
    meta: dict,
    db: Session,
    agent: "Agent",
    best_page_score: float,
) -> None:
    """Re-route to page_extension when claim verify fails but page score qualifies."""
    if best_page_score >= settings.ARXIV_PAGE_EXTENSION_THRESHOLD:
        try:
            handle_page_extension(paper, meta, db, agent)
        except Exception as exc:
            log.debug("[arxiv_ingest] fallback page_extension failed: %s", exc)


def _pending_proposals_for_page(db: Session, page_id: int) -> int:
    """Count pending EditProposals for a page."""
    from app.models.edit import EditProposal
    return db.query(EditProposal).filter(
        EditProposal.page_id == page_id,
        EditProposal.status == "pending",
    ).count()


# --------------------------------------------------------------------------
# Handler 1 — claim_evidence
# --------------------------------------------------------------------------

def handle_claim_evidence(
    paper: "ArxivPaper",
    meta: dict,
    db: Session,
    agent: "Agent",
) -> None:
    """
    Verify a paper via ADS, then insert an Evidence row for the best claim.

    Steps:
    1. Guard: idempotent check, max-evidence-per-paper cap.
    2. Verify via paper_search.verify_for_claim().
    3. Insert Evidence with source_channel='arxiv_ingest'.
    4. Trigger recalculate_trust for the claim's page.
    5. Log to ExternalSourceLog.
    """
    arxiv_id = paper.arxiv_id
    if _already_processed(db, arxiv_id, "arxiv_ingest"):
        log.debug("[arxiv_ingest] already processed as evidence: %s", arxiv_id)
        return

    best_claim_id = meta.get("best_claim_id")
    best_page_id = meta.get("best_page_id")
    if not best_claim_id:
        _log_external(db, source="arxiv", external_id=arxiv_id,
                      page_id=best_page_id, claim_id=None,
                      decision="skipped_no_claim", notes="meta had no best_claim_id")
        return

    # Cap: don't produce more than ARXIV_MAX_EVIDENCE_PER_PAPER evidence rows per paper
    from app.models.claim import Evidence
    existing_count = db.query(Evidence).filter(
        Evidence.arxiv_id == arxiv_id
    ).count()
    if existing_count >= settings.ARXIV_MAX_EVIDENCE_PER_PAPER:
        _log_external(db, source="arxiv", external_id=arxiv_id,
                      page_id=best_page_id, claim_id=best_claim_id,
                      decision="skipped_evidence_cap",
                      notes=f"already {existing_count} evidence rows for this arxiv_id")
        return

    # Verify paper quality via Phase 1 paper_search.
    # 2026-05-12 fix: verify_for_claim() was refactored to take a PaperRecord
    # (not a bare arxiv_id string). The caller here hadn't been updated, so
    # every claim_evidence handler invocation since the refactor was throwing
    # `TypeError: verify_for_claim() got an unexpected keyword argument
    # 'arxiv_id'`, getting caught below, and logged as `verify_failed`. The
    # last successful Evidence row from this path was 2026-05-07. Now we
    # resolve arxiv_id → PaperRecord via ads_lookup_arxiv first, then verify.
    from app.services.paper_search import verify_for_claim, ads_lookup_arxiv
    from app.models.claim import Claim
    claim = db.query(Claim).get(best_claim_id)
    if not claim:
        _log_external(db, source="arxiv", external_id=arxiv_id,
                      page_id=best_page_id, claim_id=best_claim_id,
                      decision="skipped_claim_missing")
        return

    best_page_score = meta.get("best_page_score", 0.0)

    try:
        # Strip the `oai:arXiv.org:` OAI prefix that some classifier paths
        # emit — ads_lookup_arxiv expects a bare 2604.02823-style ID.
        clean_arxiv = arxiv_id.replace("oai:arXiv.org:", "").replace("arXiv:", "").strip()
        record = ads_lookup_arxiv(clean_arxiv)
        if record is None:
            # ADS hasn't indexed this paper yet — schedule a 48h retry.
            paper.verify_retry_at = datetime.utcnow() + timedelta(hours=48)
            _log_external(db, source="arxiv", external_id=arxiv_id,
                          page_id=best_page_id, claim_id=best_claim_id,
                          decision="verify_rejected_ads_lag",
                          notes="ads_lookup_arxiv returned None; retry scheduled at 48h")
            _maybe_fallback_page_extension(paper, meta, db, agent, best_page_score)
            return
        verified = verify_for_claim(record=record, claim_text=claim.text)
    except Exception as exc:
        _log_external(db, source="arxiv", external_id=arxiv_id,
                      page_id=best_page_id, claim_id=best_claim_id,
                      decision="verify_failed", notes=str(exc)[:300])
        return

    if verified is None:
        _log_external(db, source="arxiv", external_id=arxiv_id,
                      page_id=best_page_id, claim_id=best_claim_id,
                      decision="verify_rejected_quality",
                      notes="verify_for_claim returned None (quality floor)")
        _maybe_fallback_page_extension(paper, meta, db, agent, best_page_score)
        return

    if verified.quality is not None and verified.quality < 0.6:
        _log_external(db, source="arxiv", external_id=arxiv_id,
                      page_id=best_page_id, claim_id=best_claim_id,
                      decision="verify_rejected_quality",
                      notes=f"quality {verified.quality:.2f} below 0.6 floor")
        _maybe_fallback_page_extension(paper, meta, db, agent, best_page_score)
        return

    # Insert Evidence. Metadata now nests under verified.record.
    rec = verified.record
    authors_str = ", ".join(rec.authors) if isinstance(rec.authors, list) else (rec.authors or None)
    evidence = Evidence(
        claim_id=best_claim_id,
        arxiv_id=rec.arxiv_id,
        doi=rec.doi,
        url=f"https://arxiv.org/abs/{rec.arxiv_id}" if rec.arxiv_id else None,
        title=rec.title,
        authors=authors_str,
        year=rec.year,
        summary=rec.abstract[:500] if rec.abstract else None,
        abstract=rec.abstract,
        ads_bibcode=rec.bibcode,
        quality=verified.quality,
        stance=verified.stance_hint or "supports",
        added_by_agent_id=agent.id if agent else None,
        verified_at=datetime.utcnow(),
        source_channel="arxiv_ingest",
    )
    db.add(evidence)
    db.flush()  # get evidence.id

    _log_external(db, source="arxiv", external_id=arxiv_id,
                  page_id=best_page_id, claim_id=best_claim_id,
                  evidence_id=evidence.id, decision="evidence_inserted",
                  quality=verified.quality)

    # Trigger trust recalculation for this claim
    try:
        from app.routers.claims import recalculate_trust_v2
        recalculate_trust_v2(best_claim_id, db, trigger="arxiv_ingest_verification")
    except Exception:
        pass  # best-effort; trust will recalc on next scheduled run

    # T5 hook: fire lightweight research-idea generation for new arxiv paper (debounced 6h/page)
    try:
        from app.agent_loop.research_ideas.auto_improvement import process_lightweight_event
        process_lightweight_event.apply_async(
            args=[best_page_id, "new_arxiv", arxiv_id],
            countdown=0,
        )
    except Exception:
        pass

    log.info("[arxiv_ingest] evidence inserted: arxiv=%s claim=%d q=%.2f",
             arxiv_id, best_claim_id, verified.quality)


# --------------------------------------------------------------------------
# Handler 2 — page_extension
# --------------------------------------------------------------------------

def handle_page_extension(
    paper: "ArxivPaper",
    meta: dict,
    db: Session,
    agent: "Agent",
) -> None:
    """
    Propose a wiki edit for a page that this paper extends.

    Throttle: skip if the page already has >= ARXIV_MAX_PAGE_EDITS_PER_PAGE_PER_DAY
    pending proposals today, or if ARXIV_SKIP_PAGE_IF_PENDING_PROPOSALS is set
    and there are any pending proposals at all.
    """
    arxiv_id = paper.arxiv_id
    best_page_id = meta.get("best_page_id")
    if not best_page_id:
        return

    # Throttle check
    if settings.ARXIV_SKIP_PAGE_IF_PENDING_PROPOSALS:
        pending = _pending_proposals_for_page(db, best_page_id)
        if pending > 0:
            _log_external(db, source="arxiv", external_id=arxiv_id,
                          page_id=best_page_id, decision="skipped_pending_proposals",
                          notes=f"{pending} pending proposals exist")
            return

    # Idempotent: check ExternalSourceLog for recent page_extension decision
    from app.models.external import ExternalSourceLog
    recent = db.query(ExternalSourceLog).filter(
        ExternalSourceLog.source == "arxiv",
        ExternalSourceLog.external_id == arxiv_id,
        ExternalSourceLog.page_id == best_page_id,
        ExternalSourceLog.decision == "page_extension_proposed",
    ).first()
    if recent:
        return

    # Daily cap: how many page_extension proposals for this page today?
    today_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    today_count = db.query(ExternalSourceLog).filter(
        ExternalSourceLog.page_id == best_page_id,
        ExternalSourceLog.decision == "page_extension_proposed",
        ExternalSourceLog.created_at >= today_start,
    ).count()
    if today_count >= settings.ARXIV_MAX_PAGE_EDITS_PER_PAGE_PER_DAY:
        _log_external(db, source="arxiv", external_id=arxiv_id,
                      page_id=best_page_id, decision="skipped_daily_cap",
                      notes=f"daily cap {today_count}/{settings.ARXIV_MAX_PAGE_EDITS_PER_PAGE_PER_DAY}")
        return

    # Build LLM prompt and call _chat
    from app.models.page import WikiPage
    page = db.query(WikiPage).get(best_page_id)
    if not page:
        return

    prompt = (
        f"You are extending the NebulaMind wiki page titled '{page.title}'.\n\n"
        f"A new arXiv paper has been published that is relevant:\n"
        f"Title: {paper.title}\n"
        f"Abstract: {paper.abstract[:800] if paper.abstract else 'N/A'}\n\n"
        f"Current page summary:\n{page.summary or page.content[:600] if page.content else 'N/A'}\n\n"
        f"Write 1-3 sentences that could be added to the page to incorporate this paper's "
        f"findings. Be factual, concise, and cite the paper as (arXiv:{paper.arxiv_id})."
    )

    system_prompt = "You are a NebulaMind wiki editor. Be factual, concise, and encyclopedic."
    try:
        from app.agent_loop.tasks import _chat
        result = _chat(None, system_prompt, prompt, role="editor")
        if not result:
            raise ValueError("empty LLM response")
    except Exception as exc:
        _log_external(db, source="arxiv", external_id=arxiv_id,
                      page_id=best_page_id, decision="page_extension_llm_failed",
                      notes=str(exc)[:300])
        return

    # Insert EditProposal
    from app.models.edit import EditProposal
    proposal = EditProposal(
        page_id=best_page_id,
        agent_id=agent.id if agent else None,
        content=result,
        summary=f"arXiv:{arxiv_id} — {paper.title[:80]}",
    )
    db.add(proposal)
    db.flush()

    _log_external(db, source="arxiv", external_id=arxiv_id,
                  page_id=best_page_id, decision="page_extension_proposed",
                  notes=f"proposal_id={proposal.id}")

    log.info("[arxiv_ingest] page extension proposed: arxiv=%s page=%d", arxiv_id, best_page_id)


# --------------------------------------------------------------------------
# Handler 3 — new_topic_candidate
# --------------------------------------------------------------------------

def handle_new_topic(
    paper: "ArxivPaper",
    meta: dict,
    db: Session,
    agent: "Agent",
) -> None:
    """
    Stage a new-page proposal cluster entry.

    Papers accumulate in new_page_proposals until ARXIV_NEW_TOPIC_MIN_CLUSTER_SIZE
    papers share a centroid (via TF-IDF) — then a notification is sent to Discord.
    """
    arxiv_id = paper.arxiv_id

    # Idempotent: already staged?
    from app.models.external import ExternalSourceLog
    existing = db.query(ExternalSourceLog).filter(
        ExternalSourceLog.source == "arxiv",
        ExternalSourceLog.external_id == arxiv_id,
        ExternalSourceLog.decision == "new_topic_staged",
    ).first()
    if existing:
        return

    # Find existing proposals in the lookback window that might cluster with this paper
    lookback = datetime.utcnow() - timedelta(days=settings.ARXIV_NEW_TOPIC_LOOKBACK_DAYS)
    from app.models.external import NewPageProposal
    candidates = db.query(NewPageProposal).filter(
        NewPageProposal.status == "pending",
        NewPageProposal.created_at >= lookback,
    ).all()

    # Simple clustering: check centroid similarity using arxiv_classifier TF-IDF
    matched_proposal = None
    if candidates:
        try:
            from app.services.arxiv_classifier import _tokenize, _tfidf_vector, _cosine, _corpus
            paper_tokens = _tokenize(f"{paper.title} {paper.abstract or ''}")
            paper_vec = _tfidf_vector(paper_tokens, _corpus.idf or {})
            for proposal in candidates:
                # proposal.cluster_papers is a JSON list of arxiv_ids
                cluster_ids = json.loads(proposal.cluster_papers or "[]")
                if len(cluster_ids) < settings.ARXIV_NEW_TOPIC_MIN_CLUSTER_SIZE:
                    # Check if adding this paper would cross the threshold
                    # Use proposal title as centroid proxy
                    centroid_tokens = _tokenize(proposal.suggested_title)
                    centroid_vec = _tfidf_vector(centroid_tokens, _corpus.idf or {})
                    sim = _cosine(paper_vec, centroid_vec)
                    if sim >= settings.ARXIV_NEW_TOPIC_CENTROID_THRESHOLD:
                        matched_proposal = proposal
                        break
        except Exception as exc:
            log.debug("[arxiv_ingest] clustering failed: %s", exc)

    if matched_proposal:
        # Add this paper to the existing cluster
        cluster_ids = json.loads(matched_proposal.cluster_papers or "[]")
        cluster_ids.append(arxiv_id)
        matched_proposal.cluster_papers = json.dumps(cluster_ids)

        # Recompute centroid_similarity as mean pairwise TF-IDF cosine across all cluster papers
        try:
            from app.services.arxiv_classifier import _tokenize, _tfidf_vector, _cosine, _corpus
            from app.models.arxiv import ArxivPaper as _ArxivPaper
            cluster_objs = db.query(_ArxivPaper).filter(
                _ArxivPaper.arxiv_id.in_(cluster_ids)
            ).all()
            if len(cluster_objs) >= 2:
                vecs = [
                    _tfidf_vector(
                        _tokenize(f"{cp.title} {cp.abstract or ''}"),
                        _corpus.idf or {},
                    )
                    for cp in cluster_objs
                ]
                pairs = [
                    (vecs[i], vecs[j])
                    for i in range(len(vecs))
                    for j in range(i + 1, len(vecs))
                ]
                matched_proposal.centroid_similarity = (
                    sum(_cosine(a, b) for a, b in pairs) / len(pairs)
                )
        except Exception as _exc:
            log.debug("[arxiv_ingest] centroid recompute failed: %s", _exc)

        # If cluster now meets min size, schedule Discord notification
        if len(cluster_ids) >= settings.ARXIV_NEW_TOPIC_MIN_CLUSTER_SIZE:
            _maybe_notify_new_proposals(db)

        _log_external(db, source="arxiv", external_id=arxiv_id,
                      decision="new_topic_staged",
                      notes=f"added to cluster proposal_id={matched_proposal.id} size={len(cluster_ids)}")
    else:
        # Start a new cluster; size-1 is perfectly self-coherent → 1.0
        slug_candidate = _make_slug(paper.title)

        # D1 dedupe gate: skip slugs duplicating existing proposals/pages
        from app.services.proposal_triage import is_duplicate_slug
        dup_reason = is_duplicate_slug(db, slug_candidate)
        if dup_reason:
            _log_external(db, source="arxiv", external_id=arxiv_id,
                          decision="new_topic_dedupe_skipped",
                          notes=f"slug={slug_candidate} reason={dup_reason}")
            log.debug("[arxiv_ingest] new_topic dedupe skip %s: %s", slug_candidate, dup_reason)
            return

        proposal = NewPageProposal(
            suggested_slug=slug_candidate,
            suggested_title=paper.title[:200],
            cluster_papers=json.dumps([arxiv_id]),
            centroid_similarity=1.0,
            status="pending",
        )
        db.add(proposal)
        db.flush()
        _log_external(db, source="arxiv", external_id=arxiv_id,
                      decision="new_topic_staged",
                      notes=f"new cluster started proposal_id={proposal.id}")

    log.debug("[arxiv_ingest] new_topic_candidate staged: arxiv=%s", arxiv_id)


def _make_slug(title: str) -> str:
    """Convert a title to a URL-friendly slug."""
    import re
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower())
    slug = slug.strip("-")[:100]
    return slug


def _maybe_notify_new_proposals(db: Session) -> None:
    """
    Send Discord batch notification when >= NEW_PAGE_PROPOSAL_NOTIFY_BATCH_SIZE
    proposals are ready, or >= NEW_PAGE_PROPOSAL_NOTIFY_FLUSH_HOURS have passed.
    """
    from app.models.external import NewPageProposal
    unnotified = db.query(NewPageProposal).filter(
        NewPageProposal.status == "pending",
        NewPageProposal.notified_at.is_(None),
        NewPageProposal.cluster_papers.isnot(None),
    ).all()

    # Filter to clusters that meet min size
    ready = [
        p for p in unnotified
        if len(json.loads(p.cluster_papers or "[]")) >= settings.ARXIV_NEW_TOPIC_MIN_CLUSTER_SIZE
    ]

    flush_cutoff = datetime.utcnow() - timedelta(hours=settings.NEW_PAGE_PROPOSAL_NOTIFY_FLUSH_HOURS)
    old_enough = [p for p in ready if p.created_at < flush_cutoff]

    should_notify = (
        len(ready) >= settings.NEW_PAGE_PROPOSAL_NOTIFY_BATCH_SIZE
        or len(old_enough) > 0
    )
    if not should_notify:
        return

    # Build notification
    lines = [f"🌌 **{len(ready)} new page proposals** ready for review:"]
    for p in ready[:10]:
        n = len(json.loads(p.cluster_papers or "[]"))
        lines.append(f"  • `{p.suggested_slug}` ({n} arXiv papers)")
    if len(ready) > 10:
        lines.append(f"  … and {len(ready) - 10} more")
    lines.append("Review at: https://nebulamind.net/admin/proposals")
    message = "\n".join(lines)

    try:
        import subprocess
        import os
        webhook_url = os.getenv("DISCORD_NEBULAMIND_WEBHOOK", "")
        if webhook_url:
            subprocess.run(
                ["curl", "-s", "-X", "POST", webhook_url,
                 "-H", "Content-Type: application/json",
                 "-d", json.dumps({"content": message})],
                timeout=5, capture_output=True
            )
    except Exception as exc:
        log.warning("[arxiv_ingest] Discord notify failed: %s", exc)

    # Mark as notified
    now = datetime.utcnow()
    for p in ready:
        p.notified_at = now
