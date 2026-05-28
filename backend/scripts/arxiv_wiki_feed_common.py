#!/usr/bin/env python3
"""Shared helpers for the arXiv -> wiki evidence feed one-shot scripts."""

from __future__ import annotations

import datetime as dt
import json
import math
import os
import re
import subprocess
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from sqlalchemy import create_engine, text

BACKEND_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_ROOT = Path("/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed")
REPORT_PATH = Path("/Users/duhokim/.openclaw/workspace/Report_ArxivWikiFeed_v1_galaxy-evolution_2026-05-24.md")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://nebula:nebula@localhost:5432/nebulamind")
OLLAMA_BASE = os.getenv("ARXIV_WIKI_OLLAMA_BASE", "http://localhost:11434")
ATOM_MODEL = os.getenv("ARXIV_WIKI_ATOM_MODEL", "vanta-research/atom-astronomy-7b:latest")
ASTROSAGE_MODEL = os.getenv("ARXIV_WIKI_ASTROSAGE_MODEL", "astrosage-70b:latest")
PROMPT_VERSION = "arxiv_wiki_feed_v1_2_strict_support_20260524"

STRICT_SUPPORT_ONLY = True

STOPWORDS = frozenset(
    """
    a about above after against all also am an and any are as at be because been before
    being below between both but by can cannot could did do does doing down during each
    few for from further had has have having he her here hers him his how i if in into
    is it its itself may more most must my no nor not of off on once only or other our
    out over own same she should so some such than that the their them then there these
    they this those through to too under until up very was we were what when where which
    while who whom why will with would you your
    galaxy galaxies galactic evolution formation stellar star stars redshift cosmic
    universe astronomical astrophysical observations observed using based study studies
    model models simulation simulations data analysis results show shows suggest suggests
    paper research system systems
    """.split()
)


def db_engine():
    return create_engine(DATABASE_URL)


def now_key() -> str:
    return dt.datetime.now().strftime("%Y%m%d_%H%M%S")


def code_version() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=BACKEND_ROOT,
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return out or "unknown"
    except Exception:
        return "unknown"


def run_key(page_slug: str, suffix: str | None = None) -> str:
    stamp = suffix or now_key()
    return f"arxiv_wiki_feed_v1_{page_slug.replace('-', '_')}_{stamp}"


def artifact_dir(key: str) -> Path:
    path = ARTIFACT_ROOT / key
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")


def tokenize(text_value: str | None) -> list[str]:
    tokens = re.findall(r"[a-z][a-z0-9\-]{2,}", (text_value or "").lower())
    return [t for t in tokens if t not in STOPWORDS and not t.isdigit()]


def paper_year(submitted: str | None) -> int | None:
    if not submitted:
        return None
    m = re.search(r"(19|20)\d{2}", submitted)
    return int(m.group(0)) if m else None


def clean_arxiv_id(arxiv_id: str | None) -> str:
    value = (arxiv_id or "").strip()
    value = value.replace("oai:arXiv.org:", "").replace("arXiv:", "")
    return value


def arxiv_url(arxiv_id: str | None, fallback: str | None = None) -> str | None:
    clean = clean_arxiv_id(arxiv_id)
    if clean:
        return f"https://arxiv.org/abs/{clean}"
    return fallback


def claim_key_overlap(claim_tokens: list[str], paper_token_set: set[str]) -> tuple[float, list[str]]:
    key_terms = [t for t in claim_tokens if t not in STOPWORDS]
    if not key_terms:
        return 0.0, []
    counts = Counter(key_terms)
    matched = [term for term, _ in counts.most_common() if term in paper_token_set]
    return len(set(matched)) / max(1, len(set(key_terms))), matched[:20]


def build_idf(docs: list[list[str]]) -> dict[str, float]:
    total = len(docs) or 1
    df = Counter()
    for doc in docs:
        df.update(set(doc))
    return {term: math.log((total + 1) / (count + 0.5)) + 1.0 for term, count in df.items()}


def tfidf(tokens: list[str], idf: dict[str, float]) -> dict[str, float]:
    counts = Counter(tokens)
    total = sum(counts.values()) or 1
    return {term: (count / total) * idf.get(term, 1.0) for term, count in counts.items()}


def cosine(left: dict[str, float], right: dict[str, float]) -> float:
    if not left or not right:
        return 0.0
    dot = sum(value * right.get(term, 0.0) for term, value in left.items())
    norm_l = math.sqrt(sum(value * value for value in left.values()))
    norm_r = math.sqrt(sum(value * value for value in right.values()))
    if not norm_l or not norm_r:
        return 0.0
    return dot / (norm_l * norm_r)


def bm25_score(query_tokens: list[str], doc_tokens: list[str], idf: dict[str, float], avgdl: float) -> float:
    if not query_tokens or not doc_tokens:
        return 0.0
    k1 = 1.5
    b = 0.75
    freqs = Counter(doc_tokens)
    doc_len = len(doc_tokens)
    score = 0.0
    for term in set(query_tokens):
        tf = freqs.get(term, 0)
        if not tf:
            continue
        denom = tf + k1 * (1 - b + b * doc_len / max(avgdl, 1.0))
        score += idf.get(term, 1.0) * (tf * (k1 + 1)) / denom
    return float(score)


def load_page_scope(page_slug: str, min_abstract_chars: int) -> dict[str, Any]:
    engine = db_engine()
    with engine.begin() as conn:
        page = conn.execute(
            text("SELECT id, title, slug FROM wiki_pages WHERE slug = :slug"),
            {"slug": page_slug},
        ).mappings().first()
        if not page:
            raise SystemExit(f"Page not found: {page_slug}")

        claims = list(
            conn.execute(
                text(
                    """
                    SELECT id, page_id, section, order_idx, text
                    FROM claims
                    WHERE page_id = :page_id
                    ORDER BY section, order_idx, id
                    """
                ),
                {"page_id": page["id"]},
            ).mappings()
        )

        papers = list(
            conn.execute(
                text(
                    """
                    SELECT id, arxiv_id, title, authors, abstract, abstract_summary,
                           category, submitted, url, related_pages
                    FROM arxiv_papers
                    WHERE related_pages ILIKE :needle
                      AND arxiv_id IS NOT NULL
                      AND title IS NOT NULL
                      AND length(coalesce(abstract, '')) >= :min_abstract_chars
                    ORDER BY id
                    """
                ),
                {"needle": f"%{page_slug}%", "min_abstract_chars": min_abstract_chars},
            ).mappings()
        )

        duplicates = {
            (row["claim_id"], clean_arxiv_id(row["arxiv_id"])): row["id"]
            for row in conn.execute(
                text(
                    """
                    SELECT claim_id, arxiv_id, id
                    FROM evidence
                    WHERE claim_id = ANY(:claim_ids)
                      AND arxiv_id IS NOT NULL
                    """
                ),
                {"claim_ids": [row["id"] for row in claims] or [-1]},
            ).mappings()
        }

    return {"page": dict(page), "claims": [dict(r) for r in claims], "papers": [dict(r) for r in papers], "duplicates": duplicates}


def ollama_chat(model: str, prompt: str, timeout: int = 120) -> tuple[str, dict[str, Any]]:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": 0.0, "num_ctx": 4096, "num_predict": 420},
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        f"{OLLAMA_BASE}/api/chat",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    started = time.time()
    with urllib.request.urlopen(request, timeout=timeout) as response:
        raw = response.read().decode("utf-8", errors="replace")
    parsed = json.loads(raw)
    content = ((parsed.get("message") or {}).get("content") or "").strip()
    meta = {
        "duration_seconds": round(time.time() - started, 3),
        "eval_count": parsed.get("eval_count"),
        "prompt_eval_count": parsed.get("prompt_eval_count"),
    }
    return content, meta


def extract_json_object(text_value: str) -> dict[str, Any]:
    stripped = text_value.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```[a-zA-Z0-9_-]*\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    try:
        return json.loads(stripped)
    except Exception:
        pass
    match = re.search(r"\{.*\}", stripped, re.DOTALL)
    if not match:
        raise ValueError("no JSON object found")
    return json.loads(match.group(0))


def clamp_score(value: Any) -> float:
    try:
        score = float(value)
    except Exception:
        return 0.0
    return max(0.0, min(1.0, score))


def validator_prompt(candidate: dict[str, Any], model_role: str) -> str:
    return f"""You are validating whether an arXiv abstract is evidence for one existing astronomy wiki claim.

V1 policy: only `strict_support` may be production-promotable. Do not label topical similarity as support.

Return ONLY one JSON object with these keys:
{{
  "label": "strict_support|strict_challenge|adjacent_support|neutral_or_unclear|needs_human",
  "stance": "supports|challenges|none",
  "score": 0.0,
  "rationale": "one concise sentence naming the exact claim-paper link",
  "quoted_evidence_span": "short abstract phrase, max 20 words",
  "failure_mode": null
}}

Rubric:
- strict_support: the title/abstract directly supports the claim as written.
- strict_challenge: the title/abstract directly contradicts the claim as written. In v1 this is annotate-only, not promotable.
- adjacent_support: right topic, useful paper, but it supports a weaker/broader/different claim.
- neutral_or_unclear: topical-only, weak, insufficient, or unclear relationship.
- needs_human: ambiguous, model uncertainty, or support requires full text beyond abstract.

Calibration rules:
- Atom-7B: reserve strict_support for direct mechanism, quantity, relation, threshold, or observational-result matches. Topical overlap, same variable family, same redshift domain, or same broad process must be adjacent_support or neutral_or_unclear.
- Atom-7B: if your rationale contains "does not address", "related but not direct", "related", "different aspect", "broader", or "not directly", the label must not be strict_support.
- AstroSage-70B: citation-name mismatch is OK when the scientific assertion matches. strict_support is allowed for self-contained claim clauses even if citation names differ.
- AstroSage-70B: do not require the same named citation as the claim, but do require the same scientific assertion.

Examples:
- Claim about the M-sigma relation; paper about black-hole mass vs dark-matter halo concentration: adjacent_support, not strict_support.
- Claim about quasar radiative mode and Eddington ratios; paper about dust evolution in galaxy models: neutral_or_unclear.
- Claim about inside-out quenching; paper whose abstract reports spatially resolved inside-out quenching with central sSFR suppression: strict_support.

Model role: {model_role}

Claim:
- id: {candidate['claim_id']}
- section: {candidate.get('claim_section_snapshot') or 'Unknown'}
- text: {candidate['claim_text_snapshot']}

Paper:
- arXiv: {candidate['arxiv_id']}
- title: {candidate['paper_title_snapshot']}
- authors: {(candidate.get('paper_authors_snapshot') or '')[:300]}
- year: {candidate.get('paper_year') or 'unknown'}
- url: {candidate.get('paper_url') or ''}
- abstract: {candidate['paper_abstract_snapshot'][:2200]}

Candidate features:
- bm25_score: {candidate.get('bm25_score')}
- tfidf_score: {candidate.get('tfidf_score')}
- claim_key_overlap: {candidate.get('claim_key_overlap')}
- matched_terms: {candidate.get('matched_terms')}
"""


def normalize_validation(raw: dict[str, Any]) -> dict[str, Any]:
    allowed = {"strict_support", "strict_challenge", "adjacent_support", "neutral_or_unclear", "needs_human"}
    label = str(raw.get("label") or "needs_human").strip()
    if label not in allowed:
        label = "needs_human"
    stance = str(raw.get("stance") or "none").strip()
    if stance not in {"supports", "challenges", "none"}:
        stance = "none"
    score = clamp_score(raw.get("score"))
    failure_mode = raw.get("failure_mode")
    rationale = str(raw.get("rationale") or "").strip()[:1000]
    if label == "strict_support" and score < 0.50:
        original_rationale = rationale
        label = "needs_human"
        stance = "none"
        failure_mode = "strict_support_low_score_inconsistent"
        rationale = (
            "Forced relabel from strict_support to needs_human because validator score "
            f"{score:.2f} is below 0.50."
        )
        if original_rationale:
            rationale = f"{rationale} Original rationale: {original_rationale}"[:1000]
    elif label == "strict_challenge" and score < 0.50:
        label = "needs_human"
        stance = "none"
        failure_mode = "strict_challenge_low_score_inconsistent"
    elif label == "strict_support":
        stance = "supports"
    elif label == "strict_challenge":
        stance = "challenges"
    return {
        "label": label,
        "stance": stance,
        "score": score,
        "rationale": rationale,
        "quoted_evidence_span": str(raw.get("quoted_evidence_span") or "").strip()[:300] or None,
        "failure_mode": failure_mode,
    }


def quality_score(atom_score: float, astrosage_score: float, peer_review_bonus: int = 0) -> float:
    return min(0.95, 0.55 + 0.25 * atom_score + 0.15 * astrosage_score + 0.05 * peer_review_bonus)


def summarize_counts(rows: list[dict[str, Any]], key: str) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[str(row.get(key) or "unknown")] += 1
    return dict(sorted(counts.items()))


def latest_artifact(pattern: str) -> Path:
    matches = sorted(ARTIFACT_ROOT.glob(f"*/{pattern}"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not matches:
        raise SystemExit(f"No artifact found for pattern: {pattern}")
    return matches[0]


def http_error_text(exc: Exception) -> str:
    if isinstance(exc, urllib.error.HTTPError):
        try:
            body = exc.read().decode("utf-8", errors="replace")
        except Exception:
            body = ""
        return f"{exc} {body[:500]}"
    return str(exc)
