"""
Wikipedia REST + MediaWiki API client for NebulaMind.

Endpoints:
  wp_summary(title)         → WikipediaSummary | None
  wp_external_links(title)  → list[str]
  wp_sections(title)        → list[dict]

Rules:
- User-Agent: "NebulaMind/1.0 (research; admin@nebulamind.net)" on EVERY call
- Accept: application/json on EVERY call
- Redis cache: 7-day TTL, keyed by (title, kind)
- ETag-aware on summary: if same revision in cache, return cached
- 429 backoff: respect Retry-After header, sleep, retry once; on 2nd 429 → log + return None
- No LLM calls
"""

from __future__ import annotations

import json
import logging
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime

logger = logging.getLogger(__name__)

_CACHE_TTL_7D = 7 * 24 * 3600  # seconds
_USER_AGENT = "NebulaMind/1.0 (research; admin@nebulamind.net)"
_HEADERS = {
    "User-Agent": _USER_AGENT,
    "Accept": "application/json",
}


# ---------------------------------------------------------------------------
# Redis helper
# ---------------------------------------------------------------------------

def _get_redis():
    """Lazy Redis client. Returns None if Redis unavailable (graceful degradation)."""
    try:
        import redis as redis_lib
        from app.config import settings
        return redis_lib.from_url(settings.REDIS_URL, decode_responses=True)
    except Exception:
        return None


# ---------------------------------------------------------------------------
# WikipediaSummary dataclass
# ---------------------------------------------------------------------------

@dataclass
class WikipediaSummary:
    title: str
    canonical_url: str
    extract: str             # plain text ≤ 1KB typical
    description: str | None  # 1-line subtitle
    revision: str            # revision id as string
    timestamp: str           # ISO 8601
    license: str = "CC BY-SA 4.0"
    fetched_at: datetime = field(default_factory=datetime.utcnow)

    def first_sentences(self, max_n: int = 2) -> str:
        """Return first N sentences. Never paraphrase — verbatim only."""
        import re
        sentences = re.split(r'(?<=[.!?])\s+', self.extract.strip())
        return " ".join(sentences[:max_n])


# ---------------------------------------------------------------------------
# Internal HTTP helper
# ---------------------------------------------------------------------------

def _fetch_json(url: str) -> tuple[dict | None, int]:
    """
    Fetch URL with standard headers. Returns (parsed_json, status_code).
    On 429, returns (None, 429) with Retry-After already read from response headers
    so caller can handle backoff.
    """
    req = urllib.request.Request(url, headers=_HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read()
            return json.loads(body), resp.status
    except urllib.error.HTTPError as e:
        return None, e.code
    except Exception as e:
        logger.warning("Wikipedia fetch error for %s: %s", url, e)
        return None, 0


def _fetch_json_with_retry_after(url: str) -> tuple[dict | None, int, float]:
    """
    Like _fetch_json but also returns the Retry-After value (seconds) on 429.
    Returns (data, status_code, retry_after_seconds).
    """
    req = urllib.request.Request(url, headers=_HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read()
            return json.loads(body), resp.status, 0.0
    except urllib.error.HTTPError as e:
        retry_after = 0.0
        try:
            retry_after = float(e.headers.get("Retry-After", "5"))
        except (TypeError, ValueError):
            retry_after = 5.0
        return None, e.code, retry_after
    except Exception as ex:
        logger.warning("Wikipedia fetch error for %s: %s", url, ex)
        return None, 0, 0.0


# ---------------------------------------------------------------------------
# wp_summary
# ---------------------------------------------------------------------------

def wp_summary(title: str) -> WikipediaSummary | None:
    """Fetch Wikipedia summary for *title*. Returns WikipediaSummary or None."""
    encoded = urllib.parse.quote(title.replace(" ", "_"), safe="")
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded}"
    cache_key = f"nm:wp:summary:{title}"
    r = _get_redis()

    # --- cache read ---
    if r is not None:
        try:
            cached_raw = r.get(cache_key)
            if cached_raw:
                cached = json.loads(cached_raw)
                live_revision = _peek_revision(url)
                if live_revision is not None and str(cached.get("revision")) == str(live_revision):
                    return _parse_summary(cached)
                # revision changed → fall through to re-fetch
        except Exception as e:
            logger.debug("Redis read error (summary): %s", e)

    # --- fetch with 429 backoff ---
    data, status, retry_after = _fetch_json_with_retry_after(url)

    if status == 429:
        sleep_sec = retry_after if retry_after > 0 else 5.0
        logger.warning("Wikipedia 429 for %s; sleeping %.1fs then retrying", title, sleep_sec)
        time.sleep(sleep_sec)
        data, status, retry_after2 = _fetch_json_with_retry_after(url)
        if status == 429:
            logger.error("Wikipedia 429 again for %s; giving up", title)
            return None

    if status == 404:
        return None  # do NOT cache

    if data is None or status not in (200, 0):
        logger.warning("Wikipedia summary fetch failed for %s (status=%s)", title, status)
        return None

    # --- cache write ---
    if r is not None:
        try:
            r.set(cache_key, json.dumps(data), ex=_CACHE_TTL_7D)
        except Exception as e:
            logger.debug("Redis write error (summary): %s", e)

    return _parse_summary(data)


def _peek_revision(url: str) -> str | None:
    """Quick HEAD-like fetch to get just the revision. Returns None on any error."""
    data, status, _ = _fetch_json_with_retry_after(url)
    if data and status == 200:
        return str(data.get("revision", ""))
    return None


def _parse_summary(data: dict) -> WikipediaSummary | None:
    """Parse raw REST v1 summary JSON into WikipediaSummary."""
    try:
        extract = data.get("extract") or data.get("extract_html") or ""
        description = data.get("description")
        canonical_url = (
            (data.get("content_urls") or {})
            .get("desktop", {})
            .get("page", "")
        )
        revision = str(data.get("revision", ""))
        timestamp = data.get("timestamp", "")
        title = data.get("title", "")
        return WikipediaSummary(
            title=title,
            canonical_url=canonical_url,
            extract=extract,
            description=description,
            revision=revision,
            timestamp=timestamp,
        )
    except Exception as e:
        logger.warning("Failed to parse Wikipedia summary: %s", e)
        return None


# ---------------------------------------------------------------------------
# wp_external_links
# ---------------------------------------------------------------------------

def wp_external_links(title: str) -> list[str]:
    """Fetch external links for *title* from MediaWiki API."""
    cache_key = f"nm:wp:extlinks:{title}"
    r = _get_redis()

    if r is not None:
        try:
            cached = r.get(cache_key)
            if cached:
                return json.loads(cached)
        except Exception as e:
            logger.debug("Redis read error (extlinks): %s", e)

    encoded = urllib.parse.quote(title.replace(" ", "_"), safe="")
    url = (
        f"https://en.wikipedia.org/w/api.php"
        f"?action=parse&page={encoded}&prop=externallinks&format=json&formatversion=2"
    )

    data, status, retry_after = _fetch_json_with_retry_after(url)

    if status == 429:
        sleep_sec = retry_after if retry_after > 0 else 5.0
        time.sleep(sleep_sec)
        data, status, _ = _fetch_json_with_retry_after(url)
        if status == 429:
            logger.error("Wikipedia 429 again for extlinks %s; giving up", title)
            return []

    if data is None:
        return []

    links = (data.get("parse") or {}).get("externallinks", [])

    if r is not None:
        try:
            r.set(cache_key, json.dumps(links), ex=_CACHE_TTL_7D)
        except Exception as e:
            logger.debug("Redis write error (extlinks): %s", e)

    return links


# ---------------------------------------------------------------------------
# wp_sections
# ---------------------------------------------------------------------------

def wp_sections(title: str) -> list[dict]:
    """Fetch section list for *title* from MediaWiki API."""
    cache_key = f"nm:wp:sections:{title}"
    r = _get_redis()

    if r is not None:
        try:
            cached = r.get(cache_key)
            if cached:
                return json.loads(cached)
        except Exception as e:
            logger.debug("Redis read error (sections): %s", e)

    encoded = urllib.parse.quote(title.replace(" ", "_"), safe="")
    url = (
        f"https://en.wikipedia.org/w/api.php"
        f"?action=parse&page={encoded}&prop=sections&format=json&formatversion=2"
    )

    data, status, retry_after = _fetch_json_with_retry_after(url)

    if status == 429:
        sleep_sec = retry_after if retry_after > 0 else 5.0
        time.sleep(sleep_sec)
        data, status, _ = _fetch_json_with_retry_after(url)
        if status == 429:
            logger.error("Wikipedia 429 again for sections %s; giving up", title)
            return []

    if data is None:
        return []

    sections = (data.get("parse") or {}).get("sections", [])

    if r is not None:
        try:
            r.set(cache_key, json.dumps(sections), ex=_CACHE_TTL_7D)
        except Exception as e:
            logger.debug("Redis write error (sections): %s", e)

    return sections


# ---------------------------------------------------------------------------
# log_external utility
# ---------------------------------------------------------------------------

def log_external(
    db,
    source: str,
    external_id: str,
    decision: str,
    page_id: int | None = None,
    claim_id: int | None = None,
    evidence_id: int | None = None,
    quality: float | None = None,
    notes: str | None = None,
) -> None:
    """Write one row to external_source_log. Caller must commit."""
    from app.models.external import ExternalSourceLog
    db.add(ExternalSourceLog(
        source=source,
        external_id=str(external_id)[:100],
        page_id=page_id,
        claim_id=claim_id,
        evidence_id=evidence_id,
        decision=decision,
        quality=quality,
        notes=notes,
    ))
