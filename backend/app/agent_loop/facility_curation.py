"""Daily facility news curation via RSS + qwen3.6:35b-a3b-nvfp4 credibility review."""
import re
import json
import hashlib
import datetime as dt
import requests
from celery import shared_task

try:
    import feedparser
except ImportError:
    feedparser = None

from app.database import SessionLocal
from app.models.facility import FacilityProfile, FacilityNewsItem
from app.config import settings

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = settings.OLLAMA_STUDIO_HEAVY_MODEL

RSS_FEEDS = [
    "https://www.nasa.gov/news/rss/",
    "https://www.esa.int/rssfeed/Our_Activities/Space_Science",
    "https://noirlab.edu/public/news/rss/",
]

FACILITY_KEYWORDS = {
    "desi": ["desi", "dark energy spectroscopic"],
    "jwst": ["jwst", "james webb", "webb space telescope"],
    "euclid": ["euclid"],
    "lsst-rubin": ["rubin", "lsst", "vera c. rubin", "simonyi"],
    "alma": ["alma", "atacama large"],
    "vla": ["vla", "very large array", "vlass"],
}

CREDIBILITY_PROMPT = """You are reviewing an astronomy facility news item for scientific credibility and relevance to researchers.

Title: {title}
Content: {content}

Respond in JSON only (no extra text):
{{
  "credibility_score": <0.0-1.0, where 1.0=authoritative primary source>,
  "summary": "<2-3 sentence professional summary for PIs and postdocs>",
  "expert_context": "<1-2 sentences: what should researchers do or know?>",
  "kind": "<one of: release|proposal_call|first_light|instrument|commissioning|milestone|other>",
  "occurs_at": "<YYYY-MM-DD or null>",
  "occurrence_status": "<upcoming|ongoing|completed>"
}}"""


def detect_facility(text: str) -> str | None:
    text_lower = text.lower()
    for slug, keywords in FACILITY_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            return slug
    return None


def item_slug(facility_slug: str, title: str) -> str:
    h = hashlib.md5(title.encode()).hexdigest()[:8]
    safe = re.sub(r"[^a-z0-9]+", "-", title.lower())[:50].strip("-")
    return f"{facility_slug}-{safe}-{h}"


def ollama_review(title: str, content: str) -> dict | None:
    prompt = CREDIBILITY_PROMPT.format(title=title, content=content[:800])
    try:
        r = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.1, "num_predict": 400},
        }, timeout=45)
        r.raise_for_status()
        text = r.json().get("response", "")
        # Extract JSON from response
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if m:
            return json.loads(m.group())
    except Exception as e:
        print(f"Ollama error: {e}")
    return None


@shared_task(name="facility_curation.run_daily")
def run_daily_curation():
    if feedparser is None:
        print("feedparser not installed; skipping RSS curation")
        return {"skipped": True, "reason": "feedparser missing"}

    db = SessionLocal()
    added = 0
    skipped = 0

    try:
        # Load known facility slugs
        fac_map = {f.slug: f.id for f in db.query(FacilityProfile).all()}

        for feed_url in RSS_FEEDS:
            try:
                feed = feedparser.parse(feed_url)
            except Exception as e:
                print(f"Feed error {feed_url}: {e}")
                continue

            for entry in feed.entries[:20]:  # limit per feed
                title = getattr(entry, "title", "") or ""
                content = getattr(entry, "summary", "") or getattr(entry, "description", "") or ""

                facility_slug = detect_facility(title + " " + content)
                if not facility_slug:
                    continue

                facility_id = fac_map.get(facility_slug)
                slug = item_slug(facility_slug, title)

                # Dedup check
                existing = db.query(FacilityNewsItem).filter(
                    FacilityNewsItem.slug == slug
                ).first()
                if existing:
                    skipped += 1
                    continue

                # LLM review
                review = ollama_review(title, content)
                if review and review.get("credibility_score", 0) < 0.5:
                    skipped += 1
                    continue

                occurs_at = None
                if review and review.get("occurs_at"):
                    try:
                        occurs_at = dt.datetime.strptime(review["occurs_at"], "%Y-%m-%d")
                    except Exception:
                        pass

                item = FacilityNewsItem(
                    facility_id=facility_id,
                    title=title[:300],
                    slug=slug,
                    kind=review.get("kind", "other") if review else "other",
                    track="data" if (review and review.get("kind") in ["release", "proposal_call", "cycle_open"]) else "facility",
                    summary=review.get("summary", content[:500]) if review else content[:500],
                    expert_context=review.get("expert_context") if review else None,
                    occurs_at=occurs_at,
                    occurrence_status=review.get("occurrence_status", "upcoming") if review else "upcoming",
                    source_url=getattr(entry, "link", None),
                    credibility_score=review.get("credibility_score") if review else None,
                    credibility_model=OLLAMA_MODEL if review else None,
                )
                db.add(item)
                added += 1

        db.commit()
    finally:
        db.close()

    return {"added": added, "skipped": skipped}
