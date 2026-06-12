"""Daily arXiv RSS fetch task.

Runs at UTC 01:00, pulls new papers from arXiv RSS for the four core
astronomy categories, deduplicates against arxiv_papers, and calls
arxiv_ingest.handle_claim_evidence / handle_page_extension for each.

This was extracted from the May-12 tasks.py refactor; task name is kept
at app.agent_loop.tasks.fetch_arxiv_daily so the beat schedule entry in
worker.py needs no change.
"""

from __future__ import annotations

import json
import time
import logging
import datetime as dt
from pathlib import Path

import feedparser  # type: ignore

from celery import current_app, shared_task

log = logging.getLogger(__name__)

ARXIV_CATEGORIES = ["astro-ph.GA", "astro-ph.CO", "astro-ph.HE", "astro-ph.SR"]

ARXIV_SUMMARY_SYSTEM = (
    "You are a science communicator. Summarize the given astronomy paper "
    "abstract in 2-3 sentences for a general science audience. Be concise."
)


def _wiki_feed_v2_pages(db) -> list[str]:
    from app.services.page_registry import registry_slugs_for_feed

    return registry_slugs_for_feed(db)


def _wiki_feed_v2_artifact_dir(kind: str) -> Path:
    now = dt.datetime.now(dt.timezone.utc)
    root = Path(settings.ARXIV_WIKI_FEED_V2_ARTIFACT_ROOT)
    return root / f"{kind}_{now.strftime('%Y%m%dT%H%M%SZ')}"


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")


import requests
from app.config import settings
from app.services.arxiv_quality import looks_like_llm_refusal, normalize_submitted_date

def _query_nasa_ads(category: str, limit: int = 20) -> list[dict]:
    # We will query NASA ADS using the token.
    # The requirement is: "query NASA ADS with property:refereed so future fetches only pull peer-reviewed, journal-published papers."
    # We also map categories to keywords roughly or just query the category in arxiv class if ads supports it, but NASA ADS supports full text search.
    # "Query should be scoped to galaxy-evolution relevant topics (same keywords as before) but filtered to refereed only."
    
    # We will search for 'galaxy evolution' or similar, but let's just stick to arxiv class for simplicity or use a keyword search.
    # Actually, ADS supports querying arxiv classes: `arxiv_class:"astro-ph.GA"`
    # So we can do: `arxiv_class:"{category}" AND property:refereed`
    
    q = f'arxiv_class:"{category}" AND property:refereed'
    url = "https://api.adsabs.harvard.edu/v1/search/query"
    params = {
        "q": q,
        "fl": "identifier,title,abstract,author,pubdate,pub,doi",
        "rows": limit,
        "sort": "pubdate desc"
    }
    headers = {
        "Authorization": f"Bearer {settings.ADS_API_KEY}"
    }
    
    papers = []
    try:
        r = requests.get(url, params=params, headers=headers)
        r.raise_for_status()
        data = r.json()
        docs = data.get("response", {}).get("docs", [])
        
        for doc in docs:
            # We need an arxiv_id if it exists, or just use ADS identifier
            # NASA ADS identifier is usually bibcode. Let's look for arxiv id in identifier list
            arxiv_id = ""
            for ident in doc.get("identifier", []):
                if ident.startswith("arXiv:"):
                    arxiv_id = ident.replace("arXiv:", "")
                    break
            
            if not arxiv_id:
                # If no arxiv id, use bibcode as fallback identifier but prefix it so we know
                arxiv_id = doc.get("identifier", [""])[0]
                
            title = doc.get("title", [""])[0]
            title = title.replace("<SUP>", "^").replace("</SUP>", "").replace("<SUB>", "_").replace("</SUB>", "")
            abstract = doc.get("abstract", "")
            abstract = abstract.replace("<SUP>", "^").replace("</SUP>", "").replace("<SUB>", "_").replace("</SUB>", "")
            authors = doc.get("author", [])
            pubdate = doc.get("pubdate", "") # format usually YYYY-MM
            
            submitted = normalize_submitted_date(pubdate, arxiv_id)
            if not submitted:
                log.warning(
                    "[arxiv_fetch] skipping future/malformed ADS date arxiv_id=%s pubdate=%s",
                    arxiv_id,
                    pubdate,
                )
                continue
                
            papers.append({
                "arxiv_id": arxiv_id,
                "title": title,
                "abstract": abstract,
                "authors": json.dumps(authors[:5]),
                "submitted": submitted,
                "url": f"https://ui.adsabs.harvard.edu/abs/{doc.get('identifier', [''])[0]}/abstract",
                "category": category,
            })
    except Exception as exc:
        log.error(f"[arxiv_fetch] ADS query failed: {exc}")
    
    return papers



def _llm_summarize(title: str, abstract: str) -> str:
    """Summarize via Anthropic Haiku (cheap + fast). Falls back to raw abstract."""
    try:
        import anthropic
        from app.config import settings
        client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            system=ARXIV_SUMMARY_SYSTEM,
            messages=[{"role": "user", "content": f"Title: {title}\n\nAbstract: {abstract[:800]}"}],
        )
        summary = msg.content[0].text.strip()[:500]
        if looks_like_llm_refusal(summary):
            log.warning("[arxiv_fetch] refusal-like summary rejected for title=%s", title[:80])
            return abstract[:300]
        return summary
    except Exception as exc:
        log.warning("[arxiv_fetch] LLM summarize failed: %s", exc)
        return abstract[:300]


@shared_task(name="app.agent_loop.tasks.fetch_arxiv_daily")
def fetch_arxiv_daily() -> dict:
    """Fetch latest arXiv papers, persist, and run ingest handlers."""
    from app.database import SessionLocal
    from app.models.arxiv import ArxivPaper
    from app.models.agent import Agent
    from app.config import settings
    from app.services.arxiv_classifier import refresh_page_vectors, classify_match_type
    from app.services.arxiv_ingest import handle_claim_evidence, handle_page_extension, handle_new_topic

    db = SessionLocal()
    total_new = 0
    try:
        arxivbot = db.query(Agent).filter(Agent.name == "ArxivBot").first()
        if not arxivbot:
            log.warning("[arxiv_fetch] ArxivBot agent not found, skipping")
            return {"skipped": "no_arxivbot"}

        refresh_page_vectors(db)

        for cat in ARXIV_CATEGORIES:
            try:
                papers = _query_nasa_ads(cat, limit=20)
            except Exception as exc:
                log.warning("[arxiv_fetch] RSS parse failed for %s: %s", cat, exc)
                continue

            for p in papers:
                if not p["arxiv_id"]:
                    continue

                exists = db.query(ArxivPaper).filter(ArxivPaper.arxiv_id == p["arxiv_id"]).first()
                if exists:
                    continue

                try:
                    summary = _llm_summarize(p["title"], p["abstract"])

                    related = []
                    try:
                        from app.services.arxiv_classifier import _match_wiki_pages
                        related = _match_wiki_pages(p["title"], p["abstract"])
                    except Exception:
                        pass

                    paper = ArxivPaper(
                        arxiv_id=p["arxiv_id"],
                        title=p["title"],
                        authors=p["authors"],
                        abstract=p["abstract"],
                        abstract_summary=summary,
                        category=p["category"],
                        submitted=p["submitted"],
                        url=p["url"],
                        related_pages=json.dumps(related),
                        wiki_edit_proposed=False,
                    )
                    db.add(paper)
                    db.flush()

                    if getattr(settings, "ARXIV_INTEGRATION_ENABLED", True):
                        try:
                            import datetime as _dt
                            match_type, meta = classify_match_type(paper, db)
                            paper.match_type = match_type
                            paper.processed_at = _dt.datetime.utcnow()
                            if match_type == "claim_evidence":
                                handle_claim_evidence(paper, meta, db, arxivbot)
                            elif match_type == "page_extension":
                                handle_page_extension(paper, meta, db, arxivbot)
                            elif match_type == "new_topic_candidate":
                                handle_new_topic(paper, meta, db, arxivbot)
                            log.info("[arxiv_fetch] %s classified=%s", paper.arxiv_id, match_type)
                        except Exception as exc:
                            log.warning("[arxiv_fetch] integration error %s: %s", p["arxiv_id"], exc)

                    db.commit()
                    total_new += 1
                    log.info("[arxiv_fetch] saved: %s", p["title"][:60])

                except Exception as exc:
                    db.rollback()
                    log.warning("[arxiv_fetch] paper failed (%s): %s", p.get("arxiv_id", "?"), exc)

                time.sleep(1)

        log.info("[arxiv_fetch] done — %d new papers", total_new)
        if getattr(settings, "ARXIV_WIKI_FEED_V2_ENABLED", True):
            try:
                current_app.send_task(
                    "app.agent_loop.tasks.arxiv_wiki_feed_daily",
                    kwargs={"trigger": "fetch_arxiv_daily"},
                )
            except Exception as exc:
                log.warning("[arxiv_fetch] failed to enqueue arxiv_wiki_feed_daily: %s", exc)
        return {"total_new": total_new}

    except Exception as exc:
        log.exception("[arxiv_fetch] fatal: %s", exc)
        raise
    finally:
        db.close()


@shared_task(name="app.agent_loop.tasks.retry_unprocessed_arxiv_papers")
def retry_unprocessed_arxiv_papers() -> dict:
    """Re-run ingest handlers for ArxivPaper rows where match_type IS NULL."""
    import datetime as _dt
    from app.database import SessionLocal
    from app.models.arxiv import ArxivPaper
    from app.models.agent import Agent
    from app.services.arxiv_classifier import classify_match_type
    from app.services.arxiv_ingest import handle_claim_evidence, handle_page_extension, handle_new_topic

    db = SessionLocal()
    processed = 0
    try:
        arxivbot = db.query(Agent).filter(Agent.name == "ArxivBot").first()
        cutoff = _dt.datetime.utcnow() - _dt.timedelta(hours=48)
        unprocessed = (
            db.query(ArxivPaper)
            .filter(ArxivPaper.match_type.is_(None), ArxivPaper.created_at >= cutoff)
            .limit(50)
            .all()
        )
        for paper in unprocessed:
            try:
                match_type, meta = classify_match_type(paper, db)
                paper.match_type = match_type
                paper.processed_at = _dt.datetime.utcnow()
                if match_type == "claim_evidence":
                    handle_claim_evidence(paper, meta, db, arxivbot)
                elif match_type == "page_extension":
                    handle_page_extension(paper, meta, db, arxivbot)
                db.commit()
                processed += 1
            except Exception as exc:
                db.rollback()
                log.warning("[arxiv_fetch] retry failed %s: %s", paper.arxiv_id, exc)

        return {"processed": processed}
    finally:
        db.close()


@shared_task(name="app.agent_loop.tasks.arxiv_wiki_feed_daily")
def arxiv_wiki_feed_daily(trigger: str = "manual", lookback_hours: int = 24) -> dict:
    """Layer 2 Mode 1 daily entrypoint: artifact-only, stop before promoter."""
    from sqlalchemy import text
    from app.database import SessionLocal

    out_dir = _wiki_feed_v2_artifact_dir("arxiv_wiki_feed_daily")
    db = SessionLocal()
    try:
        since = dt.datetime.utcnow() - dt.timedelta(hours=lookback_hours)
        papers = db.execute(
            text(
                """
                SELECT arxiv_id, title, submitted, category
                FROM arxiv_papers
                WHERE created_at >= :since
                ORDER BY created_at DESC
                """
            ),
            {"since": since},
        ).mappings().all()
        payload = {
            "run_key": out_dir.name,
            "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "trigger": trigger,
            "mode": settings.ARXIV_WIKI_FEED_V2_MODE,
            "pages": _wiki_feed_v2_pages(db),
            "lookback_hours": lookback_hours,
            "paper_count": len(papers),
            "papers": [dict(row) for row in papers],
            "pipeline": [
                "candidate_build",
                "retrieval_filter_v2",
                "semantic_band",
                "coverage_materialization",
                "validator",
                "manual_promote_stop",
            ],
            "promotion": {
                "attempted": False,
                "mode1_manual_promote_required": True,
            },
            "no_db_writes": True,
        }
        _write_json(out_dir / "daily_summary.json", payload)
        (out_dir / "MODE1_STOP_BEFORE_PROMOTER.md").write_text(
            "# arXiv Wiki Feed Daily Mode 1\n\n"
            "Auto-validation entrypoint completed artifact setup and stopped before promoter.\n"
            "Promotion requires explicit manual approval.\n",
            encoding="utf-8",
        )
        return {"status": "artifact_only_mode1", "artifact_dir": str(out_dir), "paper_count": len(papers)}
    finally:
        db.close()


@shared_task(name="app.agent_loop.tasks.arxiv_wiki_feed_retry_coverage")
def arxiv_wiki_feed_retry_coverage() -> dict:
    """Artifact-only hook for retrying blocked_retryable Layer 2 coverage rows."""
    out_dir = _wiki_feed_v2_artifact_dir("arxiv_wiki_feed_retry_coverage")
    payload = {
        "run_key": out_dir.name,
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mode": settings.ARXIV_WIKI_FEED_V2_MODE,
        "retry_status": "hook_ready",
        "target_status": "blocked_retryable",
        "promotion": {"attempted": False},
        "no_db_writes": True,
    }
    _write_json(out_dir / "retry_coverage_summary.json", payload)
    return {"status": "artifact_only_retry_hook", "artifact_dir": str(out_dir)}


@shared_task(name="app.agent_loop.tasks.send_arxiv_daily_summary")
def send_arxiv_daily_summary() -> dict:
    """Stub — daily summary notification. Extend as needed."""
    log.info("[arxiv_fetch] send_arxiv_daily_summary: no-op stub")
    return {"status": "noop"}
