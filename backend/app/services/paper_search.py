"""Paper search service: ADS primary, Semantic Scholar fallback/cross-check.

No LLM calls here — deterministic, cacheable, testable.
"""
from __future__ import annotations

import json
import math
import re
import re as _re
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime

from app.config import settings

# ---------------------------------------------------------------------------
# URL helpers (used by wikipedia bibliography miner)
# ---------------------------------------------------------------------------

_ARXIV_URL_RE = _re.compile(r'arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)')
_DOI_URL_RE = _re.compile(r'(?:doi\.org/|dx\.doi\.org/)(.+?)(?:\s|$)')


def extract_arxiv_id(url: str) -> str | None:
    """Extract arXiv ID from a URL. Returns bare ID like '2301.12345'."""
    m = _ARXIV_URL_RE.search(url)
    return m.group(1).split('v')[0] if m else None


def is_arxiv(url: str) -> bool:
    return bool(_ARXIV_URL_RE.search(url))


def extract_doi(url: str) -> str | None:
    """Extract DOI from a doi.org URL."""
    m = _DOI_URL_RE.search(url)
    return m.group(1).rstrip('/') if m else None


def is_doi(url: str) -> bool:
    return 'doi.org/' in url

ADS_SEARCH_URL = "https://api.adsabs.harvard.edu/v1/search/query"
S2_SEARCH_URL  = "https://api.semanticscholar.org/graph/v1/paper/search"
S2_PAPER_URL   = "https://api.semanticscholar.org/graph/v1/paper/{id}"

ADS_FIELDS = "bibcode,title,abstract,author,year,doi,identifier,citation_count,pub"
S2_FIELDS  = "title,abstract,authors,year,externalIds,citationCount,venue"


@dataclass
class PaperRecord:
    """Canonical paper record — source-agnostic."""
    title: str
    abstract: str | None = None
    authors: list[str] = field(default_factory=list)
    year: int | None = None
    arxiv_id: str | None = None
    doi: str | None = None
    bibcode: str | None = None
    s2_id: str | None = None
    citation_count: int | None = None
    venue: str | None = None
    source: str = "ads"        # "ads" | "s2" | "merged"

    def to_evidence_dict(self) -> dict:
        """Map to the existing `evidence` table columns."""
        return {
            "arxiv_id": self.arxiv_id,
            "doi": self.doi,
            "title": self.title,
            "authors": json.dumps(self.authors[:5]) if self.authors else None,
            "year": self.year,
            "abstract": self.abstract,
            "ads_bibcode": self.bibcode,
            "s2_paper_id": self.s2_id,
            "url": (f"https://arxiv.org/abs/{self.arxiv_id}" if self.arxiv_id
                    else (f"https://doi.org/{self.doi}" if self.doi else None)),
        }


class PaperSearchError(Exception):
    pass


# ---------------------------------------------------------------------------
# ADS
# ---------------------------------------------------------------------------

def ads_search(query: str, *, rows: int = 5, sort: str = "date desc",
               fq: str | None = "database:astronomy") -> list[PaperRecord]:
    """Run an ADS search. Empty token → raises immediately (caller falls back to S2)."""
    if not settings.ADS_API_KEY:
        raise PaperSearchError("ADS_API_KEY not configured")

    params: dict = {"q": query, "fl": ADS_FIELDS, "rows": rows, "sort": sort}
    if fq:
        params["fq"] = fq
    url = f"{ADS_SEARCH_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {settings.ADS_API_KEY}",
        "User-Agent": "NebulaMind/1.0 (trust-mechanics)",
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        raise PaperSearchError(f"ADS request failed: {e}") from e

    return [_ads_to_record(d) for d in data.get("response", {}).get("docs", [])]


def ads_lookup_arxiv(arxiv_id: str) -> PaperRecord | None:
    """Resolve a known arXiv ID to a full paper record (used by the verifier)."""
    clean = arxiv_id.replace("arXiv:", "").strip()
    try:
        results = ads_search(f'identifier:"{clean}"', rows=1, sort="date desc", fq=None)
    except PaperSearchError:
        return None
    return results[0] if results else None


def ads_lookup_doi(doi: str) -> PaperRecord | None:
    """Look up a paper by DOI in ADS. Returns None on miss or error."""
    from app.config import settings
    if not settings.ADS_API_KEY:
        return None
    try:
        encoded = urllib.parse.quote(f'doi:"{doi}"', safe="")
        url = (
            f"https://api.adsabs.harvard.edu/v1/search/query"
            f"?q={encoded}&fl=bibcode,title,author,year,arxiv_class,identifier,abstract,doi&rows=1"
        )
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {settings.ADS_API_KEY}",
            "Accept": "application/json",
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        docs = data.get("response", {}).get("docs", [])
        return _ads_to_record(docs[0]) if docs else None
    except Exception:
        return None


def _ads_to_record(d: dict) -> PaperRecord:
    ids = d.get("identifier", []) or []
    arxiv = next((i.replace("arXiv:", "").strip() for i in ids if "arXiv" in i), None)
    return PaperRecord(
        title=(d.get("title", [""]) or [""])[0],
        abstract=d.get("abstract"),
        authors=d.get("author", []) or [],
        year=int(d["year"]) if d.get("year") else None,
        arxiv_id=arxiv,
        doi=(d.get("doi", []) or [None])[0],
        bibcode=d.get("bibcode"),
        citation_count=d.get("citation_count"),
        venue=d.get("pub"),
        source="ads",
    )


# ---------------------------------------------------------------------------
# Semantic Scholar (fallback / cross-check)
# ---------------------------------------------------------------------------

def s2_search(query: str, *, rows: int = 5) -> list[PaperRecord]:
    """S2 free tier: 100 req/sec, no key required for low rate."""
    params = {"query": query, "limit": rows, "fields": S2_FIELDS}
    url = f"{S2_SEARCH_URL}?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        raise PaperSearchError(f"S2 request failed: {e}") from e
    return [_s2_to_record(p) for p in data.get("data", [])]


def _s2_to_record(p: dict) -> PaperRecord:
    ext = p.get("externalIds", {}) or {}
    return PaperRecord(
        title=p.get("title", "") or "",
        abstract=p.get("abstract"),
        authors=[a.get("name", "") for a in (p.get("authors") or [])],
        year=p.get("year"),
        arxiv_id=ext.get("ArXiv"),
        doi=ext.get("DOI"),
        s2_id=p.get("paperId"),
        citation_count=p.get("citationCount"),
        venue=p.get("venue"),
        source="s2",
    )


# ---------------------------------------------------------------------------
# Public surface: combined search
# ---------------------------------------------------------------------------

def search_papers(query: str, *, rows: int = 5, prefer_recent: bool = True) -> list[PaperRecord]:
    """ADS first, S2 union/fallback. Deduped by (arxiv_id|doi|title).

    Used by the new evidence linker. Caller is expected to further filter
    via verify_for_claim() before persisting.
    """
    out: list[PaperRecord] = []
    seen: set[str] = set()

    sort = "date desc" if prefer_recent else "citation_count desc"
    try:
        for r in ads_search(query, rows=rows, sort=sort):
            key = r.arxiv_id or r.doi or r.title.lower().strip()
            if key and key not in seen:
                seen.add(key)
                out.append(r)
    except PaperSearchError as e:
        print(f"[paper_search] ADS unavailable: {e}")

    if len(out) < rows:
        try:
            for r in s2_search(query, rows=rows):
                key = r.arxiv_id or r.doi or r.title.lower().strip()
                if key and key not in seen:
                    seen.add(key)
                    out.append(r)
        except PaperSearchError as e:
            print(f"[paper_search] S2 unavailable: {e}")

    return out[:rows * 2]   # Allow some headroom; ranker decides final cut


# ---------------------------------------------------------------------------
# Verification & quality scoring
# ---------------------------------------------------------------------------

try:
    from rapidfuzz import fuzz as _fuzz
    _HAS_RAPIDFUZZ = True
except ImportError:
    _HAS_RAPIDFUZZ = False


@dataclass
class VerifiedPaper:
    """PaperRecord plus computed quality + stance hint."""
    record: PaperRecord
    quality: float                # 0.0 – 1.0, persisted to evidence.quality
    keyword_overlap: float        # 0.0 – 1.0
    title_match: float            # 0.0 – 1.0
    recency_bonus: float          # 0.0 – 1.0
    cross_confirmed: bool
    stance_hint: str | None       # "supports" | "challenges" | None (LLM jury decides final)


_STOPWORDS = {
    "the", "a", "an", "of", "in", "on", "and", "or", "to", "for", "with",
    "is", "are", "was", "were", "be", "been", "by", "at", "from", "that",
    "this", "these", "those", "it", "its", "as", "can", "may", "will",
}


def _claim_keywords(claim_text: str, min_len: int = 4) -> set[str]:
    words = re.findall(r"[A-Za-z][A-Za-z\-]+", claim_text.lower())
    return {w for w in words if len(w) >= min_len and w not in _STOPWORDS}


_CHALLENGE_CUES = (
    "contradict", "refute", "inconsistent", "rules out", "ruled out",
    "disfavor", "in tension", "not supported", "argue against",
    "reject", "problem with", "fail", "cannot explain",
)
_SUPPORT_CUES = (
    "confirm", "consistent with", "support", "agree with", "validate",
    "corroborate", "in agreement", "reproduce", "as predicted",
)


def _stance_hint(claim_kw: set[str], abstract: str | None) -> str | None:
    """Heuristic stance hint from abstract; LLM jury makes the final call."""
    if not abstract:
        return None
    a = abstract.lower()
    chal = any(c in a for c in _CHALLENGE_CUES)
    supp = any(c in a for c in _SUPPORT_CUES)
    if chal and not supp:
        return "challenges"
    if supp and not chal:
        return "supports"
    return None


_OLLAMA_VERIFY_URL = "http://localhost:11434/api/generate"
_VERIFY_MODEL = "deepseek-r1:14b"  # Nutty — reasoning-tuned, good at claim/evidence matching


def _llm_stance_verify(claim_text: str, abstract: str, timeout: int = 30) -> str | None:
    """Call deepseek-r1:14b via Ollama to assess if abstract supports/refutes a claim.

    Returns 'supports', 'refutes', 'neutral', or None on any error (caller falls back
    to heuristic). Platoon assignment: Nutty (deepseek-r1:14b) — see ollama_model_policy_v1.md.
    """
    prompt = (
        "Does the abstract below support, refute, or neither address the claim?\n\n"
        f"Claim: {claim_text[:300]}\n\n"
        f"Abstract: {abstract[:600]}\n\n"
        "Answer with exactly one word: supports, refutes, or neutral."
    )
    payload = json.dumps({
        "model": _VERIFY_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"num_ctx": 4096, "temperature": 0},
    }).encode()
    try:
        req = urllib.request.Request(
            _OLLAMA_VERIFY_URL,
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read())
        response = data.get("response", "").lower()
        # R1 may emit chain-of-thought before the answer; scan for the keyword
        for word in ("refutes", "neutral", "supports"):
            if word in response:
                return word
        return "neutral"
    except Exception:
        return None


def verify_for_claim(
    record: PaperRecord,
    claim_text: str,
    *,
    s2_cross_check: bool = False,
) -> VerifiedPaper | None:
    """Compute quality `q` for a paper record relative to a specific claim.

    Returns None if the paper fails the hard gates (no resolvable identifier,
    no abstract, etc.). Otherwise returns a VerifiedPaper ready to persist.
    """
    # ---- Hard gates ----
    if not (record.arxiv_id or record.doi or record.bibcode):
        return None
    if not record.title or not record.abstract:
        return None
    if settings.EVIDENCE_REQUIRE_ARXIV and not record.arxiv_id:
        return None

    # ---- Title match ----
    # ADS title IS the ground truth — no second lookup needed
    title_match = 1.0

    # ---- Keyword overlap ----
    kw = _claim_keywords(claim_text)
    if kw:
        ab_words = set(re.findall(r"[A-Za-z][A-Za-z\-]+", record.abstract.lower()))
        overlap_count = len(kw & ab_words)
        keyword_overlap = min(1.0, overlap_count / max(2, len(kw) // 3))
    else:
        keyword_overlap = 0.5

    # ---- Recency ----
    if record.year:
        recency_bonus = max(0.0, min(1.0, (record.year - 1990) / 35.0))
    else:
        recency_bonus = 0.0

    # ---- Cross-confirm via Semantic Scholar ----
    cross_confirmed = False
    if s2_cross_check and record.doi:
        try:
            url = S2_PAPER_URL.format(id=f"DOI:{record.doi}") + f"?fields={S2_FIELDS}"
            with urllib.request.urlopen(url, timeout=10) as resp:
                hit = json.loads(resp.read())
            if _HAS_RAPIDFUZZ:
                cross_confirmed = bool(
                    hit.get("title") and
                    _fuzz.token_set_ratio(hit["title"], record.title) >= 90
                )
            else:
                # Fallback: simple substring check
                cross_confirmed = bool(
                    hit.get("title") and
                    record.title.lower()[:30] in hit["title"].lower()
                )
        except Exception:
            cross_confirmed = False

    # ---- Aggregate quality (matches §4.1 weights) ----
    q = (
        0.40 * (1.0 if record.arxiv_id else 0.0)    # resolvability
        + 0.25 * keyword_overlap                      # relevance
        + 0.15 * recency_bonus                        # recency
        + 0.10 * (1.0 if cross_confirmed else 0.0)    # cross-source
        # Remaining 0.10 is added later by the stance jury (§5.2)
    )
    q = round(min(1.0, max(0.0, q)), 3)

    # ---- Drop floor ----
    if q < settings.EVIDENCE_MIN_QUALITY_FOR_ACCEPTED * 0.75:
        return None

    # LLM stance pre-judge (deepseek-r1:14b / Nutty). Falls back to heuristic on
    # error so a cold Ollama or network hiccup doesn't block evidence insertion.
    llm_stance = _llm_stance_verify(claim_text, record.abstract or "")
    stance = llm_stance or _stance_hint(kw, record.abstract)

    return VerifiedPaper(
        record=record,
        quality=q,
        keyword_overlap=keyword_overlap,
        title_match=title_match,
        recency_bonus=recency_bonus,
        cross_confirmed=cross_confirmed,
        stance_hint=stance,
    )


# ---------------------------------------------------------------------------
# Phase 1 simple-API surface: verify_arxiv_id / lookup_ads
# ---------------------------------------------------------------------------

import difflib
from urllib.request import Request as _Req, urlopen as _urlopen


def _fetch_arxiv_metadata(arxiv_id: str) -> dict | None:
    """Hit export.arxiv.org/abs/{id} and parse <title>/<summary>.

    Returns {"title": str, "abstract": str, "year": int|None} or None on miss.
    Used as a no-key fallback when ADS is unavailable.
    """
    url = f"https://export.arxiv.org/abs/{arxiv_id}"
    try:
        req = _Req(url, headers={"User-Agent": "NebulaMind/1.0 (trust-phase1)"})
        with _urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception:
        return None

    title_m = re.search(r'<meta name="citation_title" content="([^"]+)"', html)
    abstract_m = re.search(r'<meta name="citation_abstract" content="([^"]+)"', html, re.S)
    date_m = re.search(r'<meta name="citation_date" content="(\d{4})', html)
    if not title_m:
        return None
    return {
        "title": title_m.group(1).strip(),
        "abstract": (abstract_m.group(1).strip() if abstract_m else ""),
        "year": int(date_m.group(1)) if date_m else None,
    }


def verify_arxiv_id(arxiv_id: str | None, claim_text: str) -> dict:
    """Verify that an arXiv ID exists and broadly relates to the claim.

    Returns {"verified": bool, "quality": float, "title": str, "year": int|None}.
    Quality is a 0.0-1.0 score combining title similarity and abstract keyword overlap.
    On any error, returns {"verified": False, "quality": 0.0, "title": "", "year": None}.
    """
    if not arxiv_id:
        return {"verified": False, "quality": 0.0, "title": "", "year": None}

    clean = arxiv_id.replace("arXiv:", "").strip()
    title = ""
    abstract = ""
    year = None

    # Prefer ADS when keyed; fall back to arxiv.org HTML scrape.
    try:
        rec = ads_lookup_arxiv(clean)
    except Exception:
        rec = None
    if rec and rec.title:
        title = rec.title
        abstract = rec.abstract or ""
        year = rec.year
    else:
        meta = _fetch_arxiv_metadata(clean)
        if not meta:
            return {"verified": False, "quality": 0.0, "title": "", "year": None}
        title = meta["title"]
        abstract = meta["abstract"]
        year = meta["year"]

    try:
        title_sim = difflib.SequenceMatcher(None, claim_text.lower(), title.lower()).ratio()
        kw = _claim_keywords(claim_text)
        if kw and abstract:
            ab_words = set(re.findall(r"[A-Za-z][A-Za-z\-]+", abstract.lower()))
            overlap = len(kw & ab_words) / max(2, len(kw) // 3)
            keyword_overlap = min(1.0, overlap)
        else:
            keyword_overlap = 0.0

        # Resolvability is the dominant signal — title overlap to a wiki claim
        # is naturally weak (claim ≠ paper title), so we don't let it dominate.
        quality = round(min(1.0, 0.50 + 0.30 * keyword_overlap + 0.20 * title_sim), 3)
        return {"verified": True, "quality": quality, "title": title, "year": year}
    except Exception:
        return {"verified": True, "quality": 0.50, "title": title, "year": year}


def _token_jaccard(s1: str, s2: str) -> float:
    """Token-set Jaccard similarity — order-insensitive, good for title matching."""
    t1 = set(re.findall(r"[a-z]+", s1.lower())) - {"the", "a", "an", "of", "in", "on", "and", "or"}
    t2 = set(re.findall(r"[a-z]+", s2.lower())) - {"the", "a", "an", "of", "in", "on", "and", "or"}
    if not t1 or not t2:
        return 0.0
    return len(t1 & t2) / len(t1 | t2)


def _venue_prefix_match(v1: str, v2: str) -> bool:
    """True if the two venue strings share a 4-char normalized prefix."""
    a = re.sub(r"[^a-z0-9]", "", v1.lower())[:4]
    b = re.sub(r"[^a-z0-9]", "", v2.lower())[:4]
    return bool(a) and a == b


def ads_lookup_by_title_and_venue(title: str, venue: str | None, *, rows: int = 3) -> list[PaperRecord]:
    """Search ADS by title (+ optional venue bibstem filter). Returns up to `rows` candidates."""
    if not settings.ADS_API_KEY:
        return []
    quoted = urllib.parse.quote(f'title:"{title}"')
    if venue:
        # Map common journal names to ADS bibstems (best-effort)
        bibstem_map = {
            "apj": "ApJ", "apjl": "ApJL", "apjs": "ApJS",
            "mnras": "MNRAS", "aap": "A&A", "aa": "A&A",
            "nature astronomy": "NatAs", "natastron": "NatAs",
            "aj": "AJ", "pasp": "PASP", "prd": "PhRvD",
        }
        norm = re.sub(r"[^a-z0-9]", "", venue.lower())
        bibstem = next((v for k, v in bibstem_map.items() if norm.startswith(re.sub(r"[^a-z0-9]", "", k))), None)
        if bibstem:
            quoted += urllib.parse.quote(f' bibstem:"{bibstem}"')
    url = (
        f"{ADS_SEARCH_URL}?q={quoted}&fl={ADS_FIELDS}&rows={rows}&sort=date+desc"
    )
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {settings.ADS_API_KEY}",
        "User-Agent": "NebulaMind/1.0 (doi-backfill)",
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        return [_ads_to_record(d) for d in data.get("response", {}).get("docs", [])]
    except Exception as e:
        print(f"[paper_search] ads_lookup_by_title_and_venue error: {e}")
        return []


def crossref_lookup_by_title_and_venue(title: str, venue: str | None, *, rows: int = 3) -> list[dict]:
    """Search CrossRef by bibliographic query. Returns raw CrossRef item dicts."""
    params: dict = {
        "query.bibliographic": title,
        "rows": rows,
        "select": "DOI,title,container-title,score",
        "mailto": "admin@nebulamind.net",
    }
    if venue:
        params["query.container-title"] = venue
    url = f"https://api.crossref.org/works?{urllib.parse.urlencode(params)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "NebulaMind/1.0 doi-backfill (admin@nebulamind.net)"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        return data.get("message", {}).get("items", [])
    except Exception as e:
        print(f"[paper_search] crossref_lookup error: {e}")
        return []


def lookup_ads(arxiv_id: str) -> bool:
    """True if NASA ADS knows about this arXiv ID. False on miss / no key / error."""
    if not arxiv_id or not settings.ADS_API_KEY:
        return False
    import requests
    clean = arxiv_id.replace("arXiv:", "").strip()
    url = f"https://api.adsabs.harvard.edu/v1/search/query?q=arxiv:{clean}&fl=bibcode"
    headers = {"Authorization": f"Bearer {settings.ADS_API_KEY}"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        return r.json().get("response", {}).get("numFound", 0) > 0
    except Exception:
        return False
