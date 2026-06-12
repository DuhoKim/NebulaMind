"""Fetch and cache paper introductions for evidence rescue paths."""
from __future__ import annotations

import datetime as dt
import html
import re
import urllib.error
import urllib.request

from sqlalchemy.orm import Session

from app.config import settings
import app.models.jury  # Ensure Evidence FK metadata is present when PaperIntro loads claim models.
from app.models.claim import PaperIntro


STUB_MIN_BYTES = 20_000
FAILURE_BLOCK_DAYS = 30
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9])")


def _clean_arxiv_id(arxiv_id: str) -> str:
    return arxiv_id.replace("arXiv:", "").strip().split()[0].rstrip(".")


def _new_style_year(arxiv_id: str) -> int | None:
    match = re.match(r"^(\d{2})(\d{2})\.\d{4,5}", arxiv_id)
    if not match:
        return None
    yy = int(match.group(1))
    return 2000 + yy if yy < 90 else 1900 + yy


def _strip_html(raw: str) -> str:
    lower = raw.lower()
    start = lower.find("introduction")
    if start == -1:
        start = 0
    chunk = raw[start : start + 80_000]
    for end_marker in ("references", "acknowledgements", "acknowledgments"):
        idx = chunk.lower().find(end_marker, 8_000)
        if idx != -1:
            chunk = chunk[:idx]
            break
    chunk = re.sub(r"<script.*?</script>|<style.*?</style>", " ", chunk, flags=re.I | re.S)
    chunk = re.sub(r"<[^>]+>", " ", chunk)
    return re.sub(r"\s+", " ", html.unescape(chunk)).strip()


def _fetch_url(url: str, timeout: int) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": "NebulaMind/1.0 (intro-fetch)"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = getattr(resp, "status", 200)
            return int(status or 200), resp.read()
    except urllib.error.HTTPError as exc:
        return int(exc.code), b""
    except Exception:
        return 0, b""


def _valid_payload(payload: bytes) -> bool:
    if len(payload) < STUB_MIN_BYTES:
        return False
    text = payload.decode("utf-8", errors="ignore").lower()
    return "ntroduction" in text


def _cache_row(db: Session, arxiv_id: str, text: str | None, status: int, source: str) -> None:
    now = dt.datetime.utcnow()
    row = db.get(PaperIntro, arxiv_id)
    if row is None:
        row = PaperIntro(arxiv_id=arxiv_id)
        db.add(row)
    row.intro_text = text
    row.http_status = status
    row.source = source
    row.fetched_at = now
    db.commit()


def fetch_intro(arxiv_id: str, db: Session) -> str | None:
    """Return cached/fetched intro text for an arXiv paper, or None on miss.

    Failed fetches are cached for 30 days so linker/backfill paths do not hammer
    ar5iv or arXiv native HTML when a paper has no usable introduction page.
    """
    if not settings.INTRO_FETCH_ENABLED or not arxiv_id:
        return None
    clean = _clean_arxiv_id(arxiv_id)
    now = dt.datetime.utcnow()
    cached = db.get(PaperIntro, clean)
    if cached:
        if cached.intro_text:
            return cached.intro_text
        if cached.fetched_at and cached.fetched_at > now - dt.timedelta(days=FAILURE_BLOCK_DAYS):
            return None

    timeout = max(1, int(settings.INTRO_FETCH_TIMEOUT_S))
    sources: list[tuple[str, str, int]] = [
        ("ar5iv", f"https://ar5iv.labs.arxiv.org/html/{clean}", timeout),
    ]
    if (_new_style_year(clean) or 0) >= 2024:
        sources.append(("arxiv", f"https://arxiv.org/html/{clean}", min(15, timeout)))

    last_status = 0
    last_source = "ar5iv"
    for source, url, source_timeout in sources:
        status, payload = _fetch_url(url, source_timeout)
        last_status = status
        last_source = source
        if status == 200 and _valid_payload(payload):
            text = _strip_html(payload.decode("utf-8", errors="ignore"))
            if text:
                _cache_row(db, clean, text, status, source)
                return text
    _cache_row(db, clean, None, last_status or 204, last_source)
    return None


def select_excerpt(intro_text: str | None, claim_text: str, cap: int = 1200) -> str | None:
    """Select 3-5 relevant intro sentences using deterministic keyword scoring."""
    if not intro_text:
        return None
    from app.services.paper_search import _claim_keywords

    sentences = [s.strip() for s in SENTENCE_RE.split(intro_text) if len(s.strip()) >= 30]
    if not sentences:
        return None
    keywords = _claim_keywords(claim_text)
    scored: list[tuple[int, int, str]] = []
    for idx, sentence in enumerate(sentences):
        words = set(re.findall(r"[A-Za-z][A-Za-z\-]+", sentence.lower()))
        score = len(keywords & words) if keywords else 0
        if score > 0:
            scored.append((score, idx, sentence))

    if scored:
        chosen = sorted(sorted(scored, key=lambda item: (-item[0], item[1]))[:5], key=lambda item: item[1])
        if len(chosen) < 3:
            seen = {idx for _, idx, _ in chosen}
            for idx, sentence in enumerate(sentences):
                if idx not in seen:
                    chosen.append((0, idx, sentence))
                if len(chosen) >= 3:
                    break
            chosen.sort(key=lambda item: item[1])
        selected = [sentence for _, _, sentence in chosen]
    else:
        selected = sentences[:3]

    excerpt = ""
    for sentence in selected[:5]:
        candidate = f"{excerpt} {sentence}".strip()
        if len(candidate) > cap:
            break
        excerpt = candidate
    return excerpt[:cap].strip() or None
