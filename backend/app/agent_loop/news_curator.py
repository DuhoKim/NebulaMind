"""Daily news curation — fetches, scores credibility, and stores astronomy news items."""
import re
import json
import hashlib
import datetime as dt

import httpx

from app.agent_loop.worker import celery_app
from app.config import settings
from app.database import SessionLocal
from app.models.facility import FacilityProfile, FacilityNewsItem
from app.services.llm_utils import strip_think_blocks

OLLAMA_BASE = "http://localhost:11434"
OLLAMA_MODEL = settings.ASTRO_SCORER_MODEL

# RSS / scrape sources per facility slug
FACILITY_FEEDS = {
    "desi": [
        "https://www.desi.lbl.gov/feed/",
        "https://www.desi.lbl.gov/category/news/feed/",
    ],
    "jwst": [
        "https://webbtelescope.org/news/news-releases/rss.xml",
        "https://science.nasa.gov/mission/webb/newsroom/rss.xml",
    ],
    "euclid": [
        "https://www.euclid-ec.org/?page_id=4128&format=feed&type=rss",
        "https://www.esa.int/rssfeed/Our_Activities/Space_Science",
    ],
    "lsst-rubin": [
        "https://www.lsst.org/news/rss.xml",
        "https://rubinobservatory.org/news/rss.xml",
        "https://community.lsst.org/latest.rss",
    ],
    "alma": [
        "https://www.almaobservatory.org/en/news/feed/",
        "https://www.almaobservatory.org/en/press-releases/feed/",
    ],
    "vla": [
        "https://public.nrao.edu/news/feed/",
        "https://science.nrao.edu/news/feed/",
    ],
}

# General astronomy feeds — Tier A/B. Updated 2026-05-18 (v1.1):
#   A&A Highlights (404) → Sky & Telescope (B-tier editorial)
#   Chandra (404 all paths) → NOIRLab (A-tier; covers Rubin/Gemini/SOAR)
#   ESA Science (404) → esa.int/rssfeed/Science (15 items, working)
GENERAL_FEEDS = [
    {"source_publication": "AAS Nova",        "tier": "A", "url": "https://aasnova.org/feed/"},
    {"source_publication": "Nature Astronomy", "tier": "A", "url": "https://www.nature.com/natastron.rss"},
    {"source_publication": "Sky & Telescope", "tier": "B", "url": "https://skyandtelescope.org/feed/"},
    {"source_publication": "ESO",             "tier": "A", "url": "https://www.eso.org/public/news/feed/"},
    {"source_publication": "NOIRLab",         "tier": "A", "url": "https://noirlab.edu/public/news/feed/"},
    {"source_publication": "ESA Science",     "tier": "A", "url": "https://www.esa.int/rssfeed/Science"},
]

GENERAL_SCORE_FLOOR: dict[str, float] = {
    "A": settings.GENERAL_NEWS_SCORE_FLOOR_A,
    "B": settings.GENERAL_NEWS_SCORE_FLOOR_B,
    "C": settings.GENERAL_NEWS_SCORE_FLOOR_C,
}

_ARXIV_ID_RE = re.compile(r"(?:arxiv[:/]\s*|arxiv\.org/abs/)(\d{4}\.\d{4,5})", re.IGNORECASE)

CREDIBILITY_PROMPT = """\
You review astronomy facility news for professional astronomers and astrophysicists.

Title: {title}
Excerpt: {excerpt}
Facility: {facility}

Reply with ONLY valid JSON, no extra text:
{{
  "credibility_score": <float 0.0-1.0; 1.0=primary science announcement from the facility>,
  "summary": "<2-3 sentence professional summary — what happened, what data/results are available>",
  "kind": "<release|proposal_call|milestone|facility_news>",
  "occurs_at": "<YYYY-MM-DD or null>",
  "occurrence_status": "<upcoming|ongoing|completed>"
}}
Scoring guide:
  0.9+: official data release, new science results from the facility
  0.7-0.9: proposal call, instrument milestone, commissioning update
  0.5-0.7: general facility news, partnership announcements
  <0.5: press fluff, human interest, tangentially related"""

GENERAL_NEWS_PROMPT = """\
You review astronomy news for professional astronomers and astrophysicists. \
Distinguish genuine research advances from press releases or popular-science framing. \
Your audience reads ApJ, MNRAS, A&A regularly.

Title: {title}
Excerpt: {excerpt}
Source: {source}
Source tier: {tier}

Reply with ONLY valid JSON, no extra text:
{{
  "credibility_score": <float 0.0-1.0; see scoring guide>,
  "advance_type": "<refereed_paper|preprint_highlight|data_release|press_release|milestone|anniversary|opinion|other>",
  "summary": "<2-3 sentences in professional voice — what was found, methods, key numbers if available. NO popsci framing.>",
  "paper_arxiv_id": "<XXXX.XXXXX or null>",
  "paper_doi": "<10.xxxx/yyyy or null>",
  "paper_venue": "<journal/preprint name or null, e.g. 'ApJL', 'Nature Astronomy', 'arXiv'>",
  "is_press_release": <true|false>,
  "popsci_flags": [<list of red-flag phrases found, e.g. "rewrite the textbooks", "stunning images", "scientists baffled">],
  "topic_tags": [<2-4 short tags, e.g. "exoplanet", "high-z galaxies", "binary pulsar", "weak lensing">]
}}

Scoring guide (be strict):
  0.95+: Refereed paper coverage with quantitative results, OR primary data release.
  0.80-0.94: Refereed-paper coverage with mostly qualitative summary, OR arXiv preprint highlighted by a high-credibility editorial venue.
  0.65-0.79: Press release tied to a specific paper, written for general audience, but the paper is identified and linkable.
  0.50-0.64: Press release with no clear paper anchor; conference/collaboration update.
  0.30-0.49: Anniversary, human-interest, mission-ops update.
  <0.30: Speculation, opinion, popsci framing.

Hard rules:
- If popsci_flags is non-empty, cap the score at 0.65.
- If advance_type is "anniversary" or "opinion", cap at 0.45.
- If paper_arxiv_id and paper_doi are both null AND advance_type is "refereed_paper" or "preprint_highlight", cap at 0.70."""


def _slug(facility_slug: str, title: str) -> str:
    h = hashlib.md5(title.lower().encode()).hexdigest()[:8]
    safe = re.sub(r"[^a-z0-9]+", "-", title.lower())[:60].strip("-")
    return f"{facility_slug}-{safe}-{h}"


def _fetch_feed(url: str) -> list[dict]:
    """Fetch RSS feed, return list of {title, content, link} dicts."""
    try:
        import feedparser  # type: ignore
        feed = feedparser.parse(url)
        items = []
        for e in feed.entries[:15]:
            title = getattr(e, "title", "") or ""
            content = (
                getattr(e, "summary", "")
                or getattr(e, "description", "")
                or ""
            )
            link = getattr(e, "link", None)
            if title:
                items.append({"title": title, "content": content[:1000], "link": link})
        return items
    except ImportError:
        pass
    except Exception as ex:
        print(f"[news_curator] feed error {url}: {ex}")
    return []


def _ollama_call(prompt: str) -> dict | None:
    """Post a prompt to local Ollama and return parsed JSON."""
    try:
        resp = httpx.post(
            f"{OLLAMA_BASE}/v1/chat/completions",
            json={
                "model": OLLAMA_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1,
                "stream": False,
            },
            timeout=60,
        )
        resp.raise_for_status()
        text = strip_think_blocks(resp.json()["choices"][0]["message"]["content"])
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if m:
            return json.loads(m.group())
    except Exception as ex:
        print(f"[news_curator] ollama error: {ex}")
    return None


def _ollama_review(title: str, content: str, facility: str) -> dict | None:
    return _ollama_call(CREDIBILITY_PROMPT.format(title=title, excerpt=content[:600], facility=facility))


def _ollama_general_review(title: str, content: str, source: str, tier: str) -> dict | None:
    return _ollama_call(GENERAL_NEWS_PROMPT.format(title=title, excerpt=content[:600], source=source, tier=tier))


def _extract_arxiv_id(title: str, content: str, link: str | None) -> str | None:
    for s in (title, content, link or ""):
        if m := _ARXIV_ID_RE.search(s):
            return m.group(1)
    return None


def _is_dup_of_arxiv(db, arxiv_id: str) -> bool:
    from app.models.arxiv import ArxivPaper
    return db.query(ArxivPaper).filter_by(arxiv_id=arxiv_id).first() is not None


def _is_dup_by_title(db, title: str) -> str | None:
    """Return matching arxiv_id if title cosine ≥ threshold against any arxiv paper in the lookback window."""
    from app.models.arxiv import ArxivPaper
    cutoff = dt.datetime.utcnow() - dt.timedelta(days=settings.GENERAL_NEWS_DEDUP_LOOKBACK_DAYS)
    candidates = db.query(ArxivPaper).filter(ArxivPaper.created_at >= cutoff).all()
    if not candidates:
        return None
    try:
        from app.services.arxiv_classifier import _tokenize, _tfidf_vector, _cosine, _corpus
        idf = _corpus.idf or {}
        news_vec = _tfidf_vector(_tokenize(title), idf)
        for p in candidates:
            p_vec = _tfidf_vector(_tokenize(p.title), idf)
            if _cosine(news_vec, p_vec) >= settings.GENERAL_NEWS_DEDUP_TITLE_COSINE:
                return p.arxiv_id
    except Exception as ex:
        print(f"[news_curator] title dedup error: {ex}")
    return None


def _log_dup_suppression(db, slug: str, decision: str, notes: str) -> None:
    from app.models.external import ExternalSourceLog
    db.add(ExternalSourceLog(source="news_curator", external_id=slug[:100], decision=decision, notes=notes))


def _notify(msg: str) -> None:
    print(f"[news_curator] {msg}")


def _discord_summary(msg: str) -> None:
    if not settings.DISCORD_WEBHOOK_URL:
        return
    try:
        httpx.post(settings.DISCORD_WEBHOOK_URL, json={"content": msg}, timeout=10)
    except Exception as ex:
        print(f"[news_curator] discord error: {ex}")


def _curate_general_feeds(db) -> dict[str, dict]:
    """Fetch GENERAL_FEEDS, score, dedup, store. Return per-source {added, total} stats."""
    stats: dict[str, dict] = {}
    for src in GENERAL_FEEDS:
        pub = src["source_publication"]
        tier = src["tier"]
        stats[pub] = {"added": 0, "total": 0}
        items = _fetch_feed(src["url"])
        seen_titles: set[str] = set()
        for raw in items:
            title = raw["title"].strip()
            if not title or title in seen_titles:
                continue
            seen_titles.add(title)
            stats[pub]["total"] += 1

            slug_prefix = re.sub(r"[^a-z0-9]+", "-", pub.lower())
            slug = _slug(slug_prefix, title)

            if db.query(FacilityNewsItem).filter(FacilityNewsItem.slug == slug).first():
                continue

            review = _ollama_general_review(title, raw["content"], pub, tier)
            if not review:
                continue

            cred = review.get("credibility_score", 0.0)
            if cred < GENERAL_SCORE_FLOOR[tier]:
                continue

            arxiv_id = review.get("paper_arxiv_id") or _extract_arxiv_id(title, raw["content"], raw.get("link"))
            if arxiv_id:
                if _is_dup_of_arxiv(db, arxiv_id):
                    _log_dup_suppression(db, slug, "news_item_dup_of_arxiv", arxiv_id)
                    continue
            else:
                matched = _is_dup_by_title(db, title)
                if matched:
                    _log_dup_suppression(db, slug, "news_item_dup_by_title", matched)
                    continue

            advance_type = review.get("advance_type", "other")
            kind_map = {
                "refereed_paper":    "refereed_paper",
                "preprint_highlight": "preprint_highlight",
                "data_release":      "release",
                "press_release":     "press_release",
                "milestone":         "milestone",
                "anniversary":       "anniversary",
                "opinion":           "opinion",
            }
            kind = kind_map.get(advance_type, "news")
            # General editorial feeds (AAS Nova, Nature Astronomy, ESO, etc.) are News —
            # they cover research but the item itself is editorial coverage, not the paper.
            # Only genuine data releases and proposal calls get their own tracks.
            # `highlights` is reserved for autowiki paper picks (not used here).
            if advance_type == "data_release":
                track = "data"
            elif advance_type == "proposal_call":
                track = "tools"
            else:
                track = "results"

            item = FacilityNewsItem(
                facility_id=None,
                title=title[:300],
                slug=slug,
                kind=kind,
                track=track,
                summary=review.get("summary", raw["content"][:500]),
                source_url=raw.get("link"),
                credibility_score=cred,
                credibility_model=OLLAMA_MODEL,
                source_publication=pub,
                source_tier=tier,
                paper_arxiv_id=arxiv_id,
                paper_doi=review.get("paper_doi"),
                paper_venue=review.get("paper_venue"),
                is_press_release=bool(review.get("is_press_release")),
                advance_type=advance_type,
                popsci_flags=json.dumps(review.get("popsci_flags") or []),
                topic_tags=json.dumps(review.get("topic_tags") or []),
                featured=False,
            )
            db.add(item)
            db.flush()
            stats[pub]["added"] += 1

    return stats


@celery_app.task(name="app.agent_loop.news_curator.curate_daily_news")
def curate_daily_news():
    """Fetch recent news from top 6 facilities (and general feeds when enabled), score with local LLM, store new items."""
    db = SessionLocal()
    total_added = 0
    total_skipped = 0
    general_stats: dict[str, dict] = {}

    try:
        fac_map: dict[str, int] = {f.slug: f.id for f in db.query(FacilityProfile).all()}

        for facility_slug, feed_urls in FACILITY_FEEDS.items():
            facility_id = fac_map.get(facility_slug)
            added_for_facility = 0

            all_items: list[dict] = []
            for url in feed_urls:
                all_items.extend(_fetch_feed(url))

            seen_titles: set[str] = set()
            for raw in all_items:
                title = raw["title"].strip()
                if not title or title in seen_titles:
                    continue
                seen_titles.add(title)

                slug = _slug(facility_slug, title)

                existing = (
                    db.query(FacilityNewsItem)
                    .filter(FacilityNewsItem.slug == slug)
                    .first()
                )
                if existing:
                    total_skipped += 1
                    continue

                review = _ollama_review(title, raw["content"], facility_slug)

                cred = review.get("credibility_score", 0.0) if review else 0.0
                if cred < 0.5:
                    total_skipped += 1
                    continue

                occurs_at = None
                if review and review.get("occurs_at"):
                    try:
                        occurs_at = dt.datetime.strptime(review["occurs_at"], "%Y-%m-%d")
                    except Exception:
                        pass

                kind = review.get("kind", "facility_news") if review else "facility_news"
                track = "data" if kind in ("release", "proposal_call") else "facility"

                item = FacilityNewsItem(
                    facility_id=facility_id,
                    title=title[:300],
                    slug=slug,
                    kind=kind,
                    track=track,
                    summary=review.get("summary", raw["content"][:500]) if review else raw["content"][:500],
                    occurs_at=occurs_at,
                    occurrence_status=review.get("occurrence_status", "completed") if review else "completed",
                    source_url=raw.get("link"),
                    credibility_score=cred,
                    credibility_model=OLLAMA_MODEL,
                    featured=False,
                )
                db.add(item)
                db.flush()
                total_added += 1
                added_for_facility += 1

        if settings.GENERAL_NEWS_ENABLED:
            general_stats = _curate_general_feeds(db)
            gen_added = sum(s["added"] for s in general_stats.values())
            total_added += gen_added
            total_skipped += sum(s["total"] - s["added"] for s in general_stats.values())

        # Mark top 3 by credibility as featured for the day
        today_start = dt.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        recent_items = (
            db.query(FacilityNewsItem)
            .filter(FacilityNewsItem.created_at >= today_start)
            .filter(FacilityNewsItem.credibility_score.isnot(None))
            .filter(FacilityNewsItem.do_not_feature.is_(False))
            .order_by(FacilityNewsItem.credibility_score.desc())
            .limit(3)
            .all()
        )
        for item in recent_items:
            item.featured = True

        db.commit()

    except Exception as ex:
        db.rollback()
        _notify(f"ERROR: {ex}")
        raise
    finally:
        db.close()

    msg = f"📰 News curated: {total_added} new items, {total_skipped} skipped"
    _notify(msg)

    if general_stats:
        today_str = dt.date.today().isoformat()
        parts = [f"{pub} {s['added']}/{s['total']}" for pub, s in general_stats.items()]
        _discord_summary(f"📰 General news {today_str}: " + ", ".join(parts))

    if total_added > 0:
        try:
            from app.services.social_drafts import draft_posts_for_featured
            db2 = SessionLocal()
            try:
                drafted = draft_posts_for_featured(db2)
                _notify("Social drafts created: " + str(drafted))
            finally:
                db2.close()
        except Exception as ex:
            _notify("Social draft error: " + str(ex))


    # J6: Mima DR-classifier — rides news-curator window (design §3.2)
    try:
        from app.agent_loop.surveys_freshness import run_survey_dr_classifier_pass
        from app.database import SessionLocal as _SL6
        _all_items = [{"title": getattr(i, "title", ""), "url": getattr(i, "url", getattr(i, "link", ""))}
                      for i in (locals().get("all_new_items") or [])]
        _db6 = _SL6()
        try:
            _fresh = run_survey_dr_classifier_pass(_db6, _all_items)
            if _fresh.get("proposals_queued") or _fresh.get("auto_applied"):
                _notify("surveys freshness: " + str(_fresh))
        finally:
            _db6.close()
    except Exception as _j6_err:
        _notify("[J6] surveys freshness error: " + str(_j6_err))

    # J6b: event-driven autowiki-surveys DR ticks — emit per matching survey
    try:
        from app.agent_loop.autowiki_surveys.tasks import autowiki_surveys_tick
        from app.database import SessionLocal as _SL6b
        import re as _re6b

        _db6b = _SL6b()
        try:
            _survey_rows = _db6b.execute(
                __import__("sqlalchemy").text("SELECT id, slug, name FROM surveys")
            ).fetchall()
            _survey_list = [(r.id, r.slug, (r.name or "").lower()) for r in _survey_rows]
            _headline_items = [
                {"title": getattr(i, "title", ""), "url": getattr(i, "url", getattr(i, "link", ""))}
                for i in (locals().get("all_new_items") or [])
            ]
            for _item in _headline_items:
                _hl = (_item.get("title") or "").lower()
                _src = _item.get("url") or ""
                for _sid, _sslug, _sname in _survey_list:
                    if _sname and _sname in _hl:
                        autowiki_surveys_tick.delay(_sid, "event_dr", "drrefresh", _src, _hl)
        finally:
            _db6b.close()
    except Exception as _j6b_err:
        _notify("[J6b] autowiki-surveys DR tick error: " + str(_j6b_err))

    return {"added": total_added, "skipped": total_skipped}


def probe_feeds() -> list[dict]:
    """GET each configured feed URL; return list of {source, url, ok, items, error}."""
    import feedparser  # type: ignore
    results = []
    all_feeds = (
        [{"source_publication": slug, "url": u} for slug, urls in FACILITY_FEEDS.items() for u in urls]
        + GENERAL_FEEDS
    )
    for src in all_feeds:
        url = src["url"]
        pub = src["source_publication"]
        try:
            resp = httpx.get(url, timeout=15, follow_redirects=True)
            status = resp.status_code
            if status != 200:
                results.append({"source": pub, "url": url, "ok": False, "items": 0, "error": f"HTTP {status}"})
                continue
            feed = feedparser.parse(resp.content)
            n = len(feed.entries)
            results.append({"source": pub, "url": url, "ok": n > 0, "items": n, "error": None if n > 0 else "0 items"})
        except Exception as ex:
            results.append({"source": pub, "url": url, "ok": False, "items": 0, "error": str(ex)})
    return results


if __name__ == "__main__":
    import sys
    if "--probe-feeds" in sys.argv:
        rows = probe_feeds()
        failed = [r for r in rows if not r["ok"]]
        for r in rows:
            status = "OK" if r["ok"] else "FAIL"
            print(f"[{status}] {r['source']:<20} items={r['items']:<3} {r['url']}")
            if r["error"]:
                print(f"       error: {r['error']}")
        if failed:
            print(f"\n{len(failed)} feed(s) failed.")
            sys.exit(1)
        print(f"\nAll {len(rows)} feeds healthy.")
    else:
        print("Usage: python3 -m app.agent_loop.news_curator --probe-feeds")
