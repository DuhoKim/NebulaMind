"""
Rakon judge wrapper — §13 (judge_v4-14b, 2026-05-12).

v4 changes vs v3 (saturation fix):
- Hybrid scoring: 5 Python-computed objective dims (citation density,
  recency density 2020+, recency density 2023+, instrument breadth,
  voice purity) + 5 judge-rated qualitative dims (quantitative
  specificity, mechanism specificity, debate interrogation depth,
  synthesis signal, citation authority).
- Continuous float dims in [0,1] @ 0.05 granularity (was integer
  0..3/0..2/0..1 — 12 distinct raw values). Now ~21^5 = 4M judge-side
  combinations × 100s of Python-side combinations.
- Conjunctive tier gates: u >= 9.5 requires synthesis_signal >= 0.85
  AND debate_interrogation >= 0.85 AND voice_purity == 1.0. u >= 9.0
  requires >=7 of 10 dims >= 0.80. u >= 8.5 requires citation_density
  >= 0.50 AND recency_density_2023 >= 0.40. See docs/autowiki_loop_v1.md
  §13.5.
- Prompt loaded from autowiki/prompts/judge_v4.md.
- Anonymized framing retained from v3.
- N=3 calls, temp=0.1 (same as v3).
- Content-hash cache keyed on (PROMPT_VERSION, page_id, content_hash,
  hero_facts_hash, claims_hash) — PROMPT_VERSION="judge_v4-14b" so v3
  entries auto-invalidate.
"""
import hashlib
import json
import re
import statistics
from pathlib import Path
from typing import NamedTuple

import httpx

from app.config import settings

_PROMPT_PATH = Path(__file__).parents[4] / "autowiki" / "prompts" / "judge_v4.md"
PROMPT_VERSION = "judge_v4-14b"
_CACHE_TTL = 7200  # 2h
_N = 3

# 5 qualitative dims — these are what the judge returns
JUDGE_DIM_KEYS = [
    "quantitative_specificity",
    "mechanism_specificity",
    "debate_interrogation",
    "synthesis_signal",
    "citation_authority",
]
# 5 objective dims — computed by Python
PYTHON_DIM_KEYS = [
    "citation_density",
    "recency_density_2020",
    "recency_density_2023",
    "instrument_breadth",
    "voice_purity",
]
# Full 10-dim union, used for tier-gate counting
ALL_DIM_KEYS = PYTHON_DIM_KEYS + JUDGE_DIM_KEYS

# v3 compatibility — judge_panel etc. import RUBRIC_KEYS. Point at JUDGE_DIM_KEYS.
RUBRIC_KEYS = JUDGE_DIM_KEYS

# Weights — see §13.3
DIM_WEIGHTS = {
    "citation_density":          0.10,
    "recency_density_2020":      0.06,
    "recency_density_2023":      0.08,
    "instrument_breadth":        0.06,
    "voice_purity":              0.05,
    "quantitative_specificity":  0.12,
    "mechanism_specificity":     0.10,
    "debate_interrogation":      0.12,
    "synthesis_signal":          0.20,
    "citation_authority":        0.11,
}
assert abs(sum(DIM_WEIGHTS.values()) - 1.0) < 1e-9, "weights must sum to 1.0"

# Banned phrases for voice_purity — §13.4
_BANNED_PHRASES = [
    "we will explore",
    "future work",
    "this page covers",
    "in this article",
    "plays a crucial role",
    "plays a key role",
    "in conclusion",
    "in summary",
    "various aspects",
    "plays a vital role",
    "it should be noted",
    "it is important to note",
]

# Frontier instrument whitelist — §13.4
_FRONTIER_INSTRUMENTS = [
    "JWST", "DESI", "Euclid", "Rubin", "LSST", "Vera Rubin",
    "ALMA", "Roman", "IceCube", "LIGO", "MUSE", "Gaia", "TESS",
    "KMTNet", "ZTF",
]

# Pre-compiled regex
_RE_AUTHOR_YEAR = re.compile(
    r"\b[A-Z][a-z]+(?:\s+et\s+al\.?)?(?:\s+&\s+[A-Z][a-z]+)?\s+\(?\b(20\d{2}|19\d{2})\b\)?"
)
_RE_ARXIV = re.compile(r"\b\d{4}\.\d{4,5}\b")
_RE_YEAR_2020 = re.compile(r"\b(202\d)\b")
_RE_YEAR_2023 = re.compile(r"\b(202[3-9])\b")


class JudgeResult(NamedTuple):
    utility: float          # 0-10
    raw_scores: list[dict]  # up to 3 judge dim dicts (5 keys each)
    rubric_median: dict     # merged 10-dim dict (judge median + python dims)
    rationale: str
    prompt_version: str
    model_used: str         # "rakon" or "buddle"


# ---------------------------------------------------------------------------
# Python-computed dims — deterministic, no judge variance
# ---------------------------------------------------------------------------

def compute_python_dims(content: str) -> dict:
    """Return the 5 Python-computed dims as floats in [0,1]."""
    if not content:
        return {k: 0.0 for k in PYTHON_DIM_KEYS}

    nc = max(len(content) / 1000.0, 0.001)  # per 1000 chars; floor avoids div0

    cit_authyear = len(_RE_AUTHOR_YEAR.findall(content))
    cit_arxiv = len(_RE_ARXIV.findall(content))
    refs_per_kc = (cit_authyear + cit_arxiv) / nc

    y2020 = len(_RE_YEAR_2020.findall(content))
    y2023 = len(_RE_YEAR_2023.findall(content))

    distinct_instruments = sum(1 for inst in _FRONTIER_INSTRUMENTS if inst in content)

    content_lower = content.lower()
    banned_hits = sum(content_lower.count(p) for p in _BANNED_PHRASES)

    return {
        "citation_density":     round(min(1.0, refs_per_kc / 3.0), 4),
        "recency_density_2020": round(min(1.0, (y2020 / nc) / 2.0), 4),
        "recency_density_2023": round(min(1.0, (y2023 / nc) / 1.5), 4),
        "instrument_breadth":   round(min(1.0, distinct_instruments / 5.0), 4),
        "voice_purity":         round(max(0.0, 1.0 - 0.10 * banned_hits), 4),
    }


# ---------------------------------------------------------------------------
# Utility computation — tier gates + weighted sum
# ---------------------------------------------------------------------------

def compute_utility(judge_dims: dict, python_dims: dict) -> float:
    """Combine 5 judge dims + 5 python dims into utility ∈ [0, 10]."""
    all_dims: dict = {**python_dims, **judge_dims}
    raw = sum(DIM_WEIGHTS[k] * float(all_dims.get(k, 0.0)) for k in DIM_WEIGHTS)
    raw = max(0.0, min(1.0, raw))

    # Tier gates — §13.5
    if raw >= 0.95:
        gate_ok = (
            float(judge_dims.get("synthesis_signal", 0.0)) >= 0.85
            and float(judge_dims.get("debate_interrogation", 0.0)) >= 0.85
            and float(python_dims.get("voice_purity", 0.0)) >= 1.0 - 1e-9
        )
        if not gate_ok:
            raw = 0.94

    if raw >= 0.90:
        n_high = sum(1 for k in ALL_DIM_KEYS if float(all_dims.get(k, 0.0)) >= 0.80)
        if n_high < 7:
            raw = 0.89

    if raw >= 0.85:
        gate_ok = (
            float(python_dims.get("citation_density", 0.0)) >= 0.50
            and float(python_dims.get("recency_density_2023", 0.0)) >= 0.40
        )
        if not gate_ok:
            raw = 0.84

    return round(raw * 10.0, 4)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_prompt() -> str:
    if _PROMPT_PATH.exists():
        return _PROMPT_PATH.read_text(encoding="utf-8")
    # Minimal inline fallback — full prompt should be on disk
    return (
        "You are judging an astronomy reference text. Return JSON with five "
        "floats in [0,1] @ 0.05 granularity: quantitative_specificity, "
        "mechanism_specificity, debate_interrogation, synthesis_signal, "
        "citation_authority, plus rationale (4 sentences)."
    )


def _get_redis():
    try:
        import redis as redis_lib
        return redis_lib.from_url(settings.REDIS_URL, decode_responses=True)
    except Exception:
        return None


def _hash4(page_id: int, content: str, hero_facts: str | None, claims_text: str) -> str:
    h = hashlib.sha256(
        f"{PROMPT_VERSION}|{page_id}|{content}|{hero_facts or ''}|{claims_text}".encode()
    ).hexdigest()[:40]
    return f"autowiki:judge:{h}"


def _parse_rubric(text: str) -> dict | None:
    """Extract judge dims dict from a model response. Returns None on malformed."""
    start = text.find("{")
    end = text.rfind("}") + 1
    if start == -1 or end <= start:
        return None
    try:
        obj = json.loads(text[start:end])
    except (json.JSONDecodeError, ValueError):
        return None
    for k in JUDGE_DIM_KEYS:
        if k not in obj or not isinstance(obj[k], (int, float)):
            return None
        v = float(obj[k])
        if not (0.0 <= v <= 1.0):
            return None
        obj[k] = v
    return obj


def _median_judge_dims(results: list[dict]) -> dict:
    medians: dict = {}
    for k in JUDGE_DIM_KEYS:
        vals = [float(r[k]) for r in results if isinstance(r.get(k), (int, float))]
        medians[k] = round(statistics.median(vals), 4) if vals else 0.0
    rationales = [r.get("rationale", "") for r in results if r.get("rationale")]
    medians["rationale"] = rationales[0] if rationales else ""
    return medians


# ---------------------------------------------------------------------------
# Model calls
# ---------------------------------------------------------------------------

def _ollama_base() -> str:
    url = settings.OLLAMA_BASE_URL.rstrip("/")
    if not url.endswith("/v1"):
        url += "/v1"
    return url


def _call_nutty(system: str, user_msg: str, timeout: int = 180) -> dict | None:
    base = _ollama_base()
    try:
        resp = httpx.post(
            f"{base}/chat/completions",
            json={
                "model": settings.OLLAMA_STUDIO_FAST_MODEL,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user_msg},
                ],
                "temperature": 0.1,
                "options": {"num_ctx": 8192},
                "keep_alive": "1h",
            },
            timeout=timeout,
        )
        resp.raise_for_status()
        text = resp.json()["choices"][0]["message"]["content"]
        return _parse_rubric(text)
    except Exception:
        return None


def _call_buddle(system: str, user_msg: str) -> dict | None:
    base = settings.BUDDLE_BASE_URL.rstrip("/")
    if not base.endswith("/v1"):
        base += "/v1"
    try:
        resp = httpx.post(
            f"{base}/chat/completions",
            json={
                "model": settings.BUDDLE_MODEL,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user_msg},
                ],
                "temperature": 0.1,
                "options": {"num_ctx": 8192},
            },
            timeout=120,
        )
        resp.raise_for_status()
        text = resp.json()["choices"][0]["message"]["content"]
        return _parse_rubric(text)
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def judge_page(
    page_id: int,
    content: str,
    hero_facts: str | None,
    claims_text: str,
    force: bool = False,
) -> JudgeResult:
    """Judge a page state. Returns JudgeResult.

    v4: 5 judge calls + Python dims. Caches by (PROMPT_VERSION, page hash).
    """
    cache_key = _hash4(page_id, content, hero_facts, claims_text)
    r = _get_redis()

    if not force and r:
        try:
            cached = r.get(cache_key)
            if cached:
                obj = json.loads(cached)
                return JudgeResult(**obj)
        except Exception:
            pass

    system = _load_prompt()
    user_msg = (
        f"===PAGE===\n{content[:4000]}\n\n"
        f"===CLAIMS===\n{claims_text[:1500]}"
    )

    raw_results: list[dict] = []
    malformed = 0
    for _ in range(_N):
        result = _call_nutty(system, user_msg)
        if result is not None:
            raw_results.append(result)
        else:
            malformed += 1

    model_used = settings.OLLAMA_STUDIO_FAST_MODEL
    if malformed > _N // 2:
        buddle = _call_buddle(system, user_msg)
        if buddle:
            raw_results = [buddle]
        model_used = "buddle"

    python_dims = compute_python_dims(content)

    if not raw_results:
        merged = {**python_dims, **{k: 0.0 for k in JUDGE_DIM_KEYS}}
        merged["rationale"] = "All judge calls failed."
        return JudgeResult(
            utility=0.0,
            raw_scores=[],
            rubric_median=merged,
            rationale=merged["rationale"],
            prompt_version=PROMPT_VERSION,
            model_used="none",
        )

    judge_median = _median_judge_dims(raw_results)
    rationale = judge_median.pop("rationale", "")

    # Merged 10-dim dict for autowiki_runs.judge_rationale and downstream
    merged = {**python_dims, **judge_median, "rationale": rationale}

    utility = compute_utility(judge_median, python_dims)

    jr = JudgeResult(
        utility=utility,
        raw_scores=raw_results,
        rubric_median=merged,
        rationale=rationale,
        prompt_version=PROMPT_VERSION,
        model_used=model_used,
    )

    if r:
        try:
            r.setex(cache_key, _CACHE_TTL, json.dumps(jr._asdict()))
        except Exception:
            pass

    return jr


# Backward-compat shim — judge_panel.py imports _rubric_to_utility from us.
# v4: callers should use compute_utility(judge_dims, python_dims). This shim
# computes Python dims from the page content stashed on the rubric dict (when
# panel callers pass merged dicts) or returns 0 if neither is available.
def _rubric_to_utility(rubric: dict, content: str = "") -> float:
    """Deprecated v3-shaped helper. Pass content for accurate v4 score; without
    it the Python dims default to 0 and the utility is judge-only."""
    judge_dims = {k: float(rubric.get(k, 0.0)) for k in JUDGE_DIM_KEYS}
    python_dims = compute_python_dims(content) if content else {
        k: 0.0 for k in PYTHON_DIM_KEYS
    }
    return compute_utility(judge_dims, python_dims)
