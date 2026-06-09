#!/usr/bin/env python3
"""Targeted ADS evidence miner with strict abstract-screening jury.

Default behavior is read-only. Use --commit to insert Evidence and EvidenceVote
rows after the ADS pre-gate and 2-of-3 SUPPORTS jury consensus pass.
"""

from __future__ import annotations

import argparse
import asyncio
import datetime as dt
import json
import os
import random
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Literal

import httpx
from sqlalchemy import or_
from sqlalchemy.orm import Session

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from app.config import settings
from app.database import SessionLocal
from app.models.claim import Claim, Evidence, EvidenceVote
from app.models.agent import Agent
from app.services.paper_search import PaperRecord, PaperSearchError, ads_search
from app.services.prompt_registry import PromptRegistry
from app.services.llm_utils import clean_llm_response, strip_think_blocks
from app.utils.premium_dispatch import log_llm_spend

Verdict = Literal["SUPPORTS", "REFUTES", "ABSTAIN"]
Confidence = Literal["LOW", "MEDIUM", "HIGH"]

ROWS = 8
MIN_HITS = 3
CLAIM_TEXT_LIMIT = 600
ABSTRACT_LIMIT = 1800
JURY_TIMEOUT_SECONDS = 360
MIN_SUPPORT_VOTES = 2
SCREEN_MODEL = "gemini-2.5-flash"
SCREEN_TIMEOUT_SECONDS = 45

SECTION_CLASS_MAP: dict[str, tuple[str, str | None]] = {
    "Physical Mechanisms": ("astro-ph.GA", "astro-ph.CO"),
    "High-Redshift Evolution and the JWST Tension": ("astro-ph.GA", "astro-ph.CO"),
    "Star Formation, Quenching & Color Bimodality": ("astro-ph.GA", None),
    "AGN Feedback & Quenching Debates": ("astro-ph.GA", "astro-ph.HE"),
    "Environmental Effects": ("astro-ph.GA", "astro-ph.CO"),
    "Galaxy Scaling Relations & Size Evolution": ("astro-ph.GA", "astro-ph.CO"),
    "Observational Evidence & Multi-Wavelength Surveys": ("astro-ph.GA", "astro-ph.IM"),
    "Open Questions & Frontier Debates": ("astro-ph.GA", "astro-ph.CO"),
}

DOMAIN_KEYPHRASES = [
    "ram-pressure stripping",
    "morphology-density relation",
    "cold-mode accretion",
    "cold streams",
    "Kelvin-Helmholtz instability",
    "baryonic Tully-Fisher relation",
    "stellar-to-halo mass relation",
    "M-sigma relation",
    "AGN feedback",
    "kinetic-mode feedback",
    "star-forming main sequence",
    "mass-metallicity relation",
    "circumgalactic medium",
    "jellyfish galaxies",
    "green valley",
    "quenching",
    "initial mass function",
    "velocity dispersion",
    "cooling flow",
    "supermassive black hole",
    "host galaxy",
    "early-type galaxies",
    "projected surface density",
]

NAMED_ENTITIES = [
    "SDSS",
    "JWST",
    "NIRSpec",
    "NIRCam",
    "COSMOS",
    "CANDELS",
    "3D-HST",
    "ALMA",
    "MUSE",
    "VLA",
    "MeerKAT",
    "IllustrisTNG",
    "EAGLE",
    "FIRE",
    "SPARC",
    "GASP",
    "ATLAS3D",
    "SAMI",
    "COS-Halos",
]

STOPWORDS = frozenset(
    """
    a about above after against all also an and any are as at be because been before
    being below between both but by can cannot could did do does doing down during each
    few for from further had has have having how if in into is it its itself may more
    most no nor not of off on once only or other our out over own same should so some
    such than that the their them then there these they this those through to under
    until up very was were what when where which while who whom why will with would
    observations analysis framework mechanism process evidence results study model
    models paradigm regime population properties galaxy galaxies galactic stellar
    astronomy astronomical astrophysics astrophysical paper papers
    """.split()
)

CLAIM_MARKER_RE = re.compile(r"<!--/?claim:[\d,\s]+-->")
TRUST_TAG_RE = re.compile(r"<!--(?:accepted|challenged|consensus|unverified|debated)-->")
CITATION_RE = re.compile(
    r"\([A-Z][A-Za-z\-]+(?: et al\.| &amp; [A-Z][A-Za-z]+)? \d{4}[a-z]?\)"
)
LATEX_RE = re.compile(r"\$\$.*?\$\$|\$[^$]*\$", re.S)
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9\-]{3,}")
VERDICT_RE = re.compile(r"###VERDICT:\s*(SUPPORTS|REFUTES|ABSTAIN)", re.I)
SENTENCE_RE = re.compile(r"###SENTENCE:\s*(.+)")
CONF_RE = re.compile(r"###CONFIDENCE:\s*(LOW|MEDIUM|HIGH)", re.I)

try:
    JURY_SYSTEM_PROMPT = PromptRegistry().render("stance", {}, policy="permissive_v1")
except Exception as e:
    # Fallback to hardcoded strict/permissive system prompt if needed
    JURY_SYSTEM_PROMPT = """You are a rigorous scientific evidence juror for an astronomy knowledge base.
Your job is to decide whether a paper's ABSTRACT explicitly supports, explicitly
refutes, or does neither, for a single CLAIM.

Be rigorous but objective. The paper supports the claim if it asserts the same physical 
relationship, measurable factor, or physical mechanism, even if it uses equivalent words 
or synonyms. It does not need to repeat the exact wording of the claim.

Hard rules:
1. Vote SUPPORTS if the abstract contains a sentence (or adjacent sentences) that 
   clearly supports the substance of the claim. You MUST quote the most relevant 
   supporting sentence, copied verbatim from the abstract, as proof. No quote => no SUPPORTS.
2. Vote REFUTES only if the abstract contains a sentence that clearly
   contradicts the claim. You MUST quote that exact sentence verbatim.
3. Otherwise vote ABSTAIN. Topical overlap, same subfield, or "related work" without 
   specific evidence is NOT support.
4. Do not use outside knowledge. Judge ONLY the text of the abstract provided.
5. The quoted sentence must appear character-for-character in the abstract. Do
   not paraphrase, complete, or correct it when quoting. If you cannot copy it exactly, ABSTAIN.

You may reason step by step. When finished, output your decision as the LAST
lines of your reply, using EXACTLY this format and nothing after it:

###VERDICT: <SUPPORTS|REFUTES|ABSTAIN>
###SENTENCE: <verbatim sentence, or the single word NONE>
###CONFIDENCE: <LOW|MEDIUM|HIGH>
"""


@dataclass(frozen=True)
class Term:
    text: str
    weight: float
    kind: Literal["phrase", "named", "noun"]


@dataclass(frozen=True)
class JurorResult:
    label: str
    verdict: Verdict
    sentence: str | None
    confidence: Confidence
    raw: str
    downgraded: bool = False


@dataclass(frozen=True)
class JuryDecision:
    stance: Literal["supports", "refutes", "neutral"]
    merge_eligible: bool
    quality: float
    results: list[JurorResult]


@dataclass(frozen=True)
class ClaimSnapshot:
    id: int
    text: str
    section: str | None
    claim_type: str | None


@dataclass(frozen=True)
class Candidate:
    claim: ClaimSnapshot
    record: PaperRecord
    terms: list[Term]
    query: str


@dataclass(frozen=True)
class ScreenItem:
    ref: int
    candidate: Candidate


@dataclass(frozen=True)
class ScreenBatch:
    items: list[ScreenItem]


@dataclass(frozen=True)
class ScreenOutcome:
    ref: int
    pre_filter: Literal["KEEP", "DISCARD"]
    fail_open: bool = False


def snapshot_claim(claim: Claim) -> ClaimSnapshot:
    return ClaimSnapshot(
        id=claim.id,
        text=claim.text,
        section=claim.section,
        claim_type=claim.claim_type,
    )


def normalize_claim_text(text: str) -> str:
    cleaned = CLAIM_MARKER_RE.sub(" ", text)
    cleaned = TRUST_TAG_RE.sub(" ", cleaned)
    cleaned = CITATION_RE.sub(" ", cleaned)
    cleaned = LATEX_RE.sub(" ", cleaned)
    cleaned = unicodedata.normalize("NFKD", cleaned)
    cleaned = re.sub(r"[\u2070-\u209f]", " ", cleaned)
    cleaned = re.sub(r"(?<![A-Za-z])[+-]?\d+(?:\.\d+)?(?:e[+-]?\d+)?\b", " ", cleaned, flags=re.I)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip().lower()


def _phrase_in_text(phrase: str, text: str) -> bool:
    pattern = r"\b" + re.escape(phrase.lower()).replace(r"\ ", r"\s+") + r"\b"
    return bool(re.search(pattern, text.lower()))


def load_keyphrases() -> list[str]:
    path = BACKEND_ROOT / "data" / "astro_keyphrases.txt"
    if not path.exists():
        return DOMAIN_KEYPHRASES
    extra = [line.strip() for line in path.read_text(encoding="utf-8").splitlines()]
    return [p for p in [*DOMAIN_KEYPHRASES, *extra] if p and not p.startswith("#")]


def extract_terms(claim_text: str) -> list[Term]:
    text = normalize_claim_text(claim_text)
    out: dict[str, Term] = {}
    for phrase in load_keyphrases():
        if _phrase_in_text(phrase, text):
            out[phrase.lower()] = Term(phrase, 3.0, "phrase")
    for entity in NAMED_ENTITIES:
        if re.search(r"\b" + re.escape(entity) + r"\b", claim_text, re.I):
            out[entity.lower()] = Term(entity, 2.5, "named")

    covered_words = {
        word
        for term in out.values()
        for word in re.findall(r"[a-z]+", term.text.lower())
    }
    counts: dict[str, int] = {}
    for token in TOKEN_RE.findall(text):
        token_l = token.lower()
        if token_l in STOPWORDS or token_l in covered_words:
            continue
        counts[token_l] = counts.get(token_l, 0) + 1

    for token, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:10]:
        out.setdefault(token, Term(token, 1.0 + min(count, 3) * 0.1, "noun"))

    return sorted(
        out.values(),
        key=lambda t: ({"phrase": 3, "named": 2, "noun": 1}[t.kind], t.weight, len(t.text)),
        reverse=True,
    )


def _ads_quote(text: str) -> str:
    return text.replace('"', r"\"")


def build_query(terms: list[Term], arxiv_class: str, *, strict: bool) -> str:
    preferred = [t for t in terms if t.kind in {"phrase", "named"}] or terms
    selected = preferred[: (3 if strict else 5)]
    if not selected:
        selected = [Term("galaxy evolution", 1.0, "phrase")]
    op = " AND " if strict else " OR "
    clauses = [f'abs:"{_ads_quote(t.text)}"' for t in selected]
    return f"({op.join(clauses)}) AND arxiv_class:\"{arxiv_class}\" AND property:refereed"


def sort_for_claim(claim: Claim) -> str:
    return "citation_count desc" if claim.claim_type == "established" else "date desc"


def claim_ads_class(claim: Claim) -> str | None:
    mapped = SECTION_CLASS_MAP.get(claim.section or "")
    if mapped:
        return mapped[0]
    # Default to astro-ph.GA for general extragalactic and galactic topics, which covers the entire corpus safely
    return "astro-ph.GA"


def paper_key(record: PaperRecord) -> str:
    return record.arxiv_id or record.doi or record.bibcode or record.title.lower().strip()


def already_attached(db: Session, claim_id: int, record: PaperRecord) -> bool:
    filters = []
    if record.arxiv_id:
        filters.append(Evidence.arxiv_id == record.arxiv_id)
    if record.doi:
        filters.append(Evidence.doi == record.doi)
    if record.bibcode:
        filters.append(Evidence.ads_bibcode == record.bibcode)
    if not filters:
        return False
    return bool(db.query(Evidence.id).filter(Evidence.claim_id == claim_id, or_(*filters)).first())


def term_overlap_count(terms: Iterable[Term], abstract: str) -> int:
    text = abstract.lower()
    hits = 0
    for term in terms:
        if term.kind in {"phrase", "named"}:
            if _phrase_in_text(term.text, text):
                hits += 1
        elif re.search(r"\b" + re.escape(term.text.lower()) + r"\b", text):
            hits += 1
    return hits


def pre_gate(db: Session, claim: Claim, record: PaperRecord, terms: list[Term]) -> bool:
    if not (record.arxiv_id or record.doi or record.bibcode):
        return False
    if not record.abstract:
        return False
    if settings.EVIDENCE_REQUIRE_ARXIV and not record.arxiv_id:
        return False
    if term_overlap_count(terms, record.abstract) < 2:
        return False
    if already_attached(db, claim.id, record):
        return False
    return True


def retrieve_candidates(db: Session, claim: Claim) -> list[Candidate]:
    arxiv_class = claim_ads_class(claim)
    if arxiv_class is None:
        return []
    claim_snapshot = snapshot_claim(claim)
    terms = extract_terms(claim.text)
    sort = sort_for_claim(claim)
    strict_query = build_query(terms, arxiv_class, strict=True)
    try:
        records = ads_search(strict_query, rows=ROWS, sort=sort, fq="database:astronomy")
        used_query = strict_query
        if len(records) < MIN_HITS:
            loose_query = build_query(terms, arxiv_class, strict=False)
            records = ads_search(loose_query, rows=ROWS, sort=sort, fq="database:astronomy")
            used_query = loose_query
    except PaperSearchError as exc:
        print(f"claim {claim.id}: ADS search failed: {exc}")
        return []

    seen: set[str] = set()
    candidates: list[Candidate] = []
    for record in records:
        key = paper_key(record)
        if not key or key in seen:
            continue
        seen.add(key)
        if pre_gate(db, claim, record, terms):
            candidates.append(Candidate(claim=claim_snapshot, record=record, terms=terms, query=used_query))
    return candidates


def user_prompt(claim: Claim | ClaimSnapshot, record: PaperRecord) -> str:
    clean_claim = re.sub(r"\s+", " ", normalize_claim_text(claim.text)).strip()
    return (
        "CLAIM:\n"
        f"{clean_claim[:CLAIM_TEXT_LIMIT]}\n\n"
        "PAPER:\n"
        f"Title: {record.title[:300]}\n"
        f"Year: {record.year or 'n.d.'}\n"
        "Abstract:\n"
        f"{(record.abstract or '')[:ABSTRACT_LIMIT]}\n\n"
        "Decide: does this abstract explicitly SUPPORT, explicitly REFUTE, or NEITHER\n"
        "support nor refute the CLAIM? Follow the hard rules. Quote a verbatim sentence\n"
        "only if you vote SUPPORTS or REFUTES."
    )


def screen_models() -> list[dict[str, Any]]:
    return [
        {
            "label": SCREEN_MODEL,
            "base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
            "api_key": settings.GEMINI_API_KEY,
            "model": SCREEN_MODEL,
            "max_tokens": 2048,
        }
    ]


def build_screen_batches(candidates: list[Candidate], batch_size: int) -> list[ScreenBatch]:
    if batch_size <= 0:
        raise ValueError("screen batch size must be positive")
    items = [ScreenItem(ref=idx, candidate=candidate) for idx, candidate in enumerate(candidates)]
    return [ScreenBatch(items=items[idx : idx + batch_size]) for idx in range(0, len(items), batch_size)]


def screen_prompt(batch: ScreenBatch) -> str:
    grouped: dict[int, list[ScreenItem]] = {}
    claim_order: list[int] = []
    for item in batch.items:
        claim_id = item.candidate.claim.id
        if claim_id not in grouped:
            grouped[claim_id] = []
            claim_order.append(claim_id)
        grouped[claim_id].append(item)

    lines = [
        "You are a fast relevance pre-screener for an astronomy evidence pipeline.",
        "For each (claim, abstract) pair decide if the abstract could plausibly SUPPORT or REFUTE the claim's specific physical assertion.",
        "This is a RECALL gate, not a verdict: when uncertain, choose KEEP.",
        "Only choose DISCARD when the abstract is clearly off-topic or unrelated to the claim's specific mechanism/quantity.",
        "Return ONLY a JSON array, one object per ref, no prose.",
        "",
    ]
    for claim_id in claim_order:
        claim = grouped[claim_id][0].candidate.claim
        clean_claim = re.sub(r"\s+", " ", normalize_claim_text(claim.text)).strip()
        lines.append(f'CLAIM {claim_id}: "{clean_claim[:CLAIM_TEXT_LIMIT]}"')
        for item in grouped[claim_id]:
            record = item.candidate.record
            title = re.sub(r"\s+", " ", record.title or "Untitled").strip()[:300]
            abstract = re.sub(r"\s+", " ", record.abstract or "").strip()[:ABSTRACT_LIMIT]
            year = record.year or "n.d."
            lines.append(f'  [ref {item.ref}] "{title}" ({year}) - {abstract}')
        lines.append("")
    first_ref = batch.items[0].ref if batch.items else 0
    second_ref = batch.items[1].ref if len(batch.items) > 1 else first_ref
    lines.append(f'Return: [{{"ref": {first_ref}, "pre_filter": "KEEP"}}, {{"ref": {second_ref}, "pre_filter": "DISCARD"}}]')
    return "\n".join(lines)


def parse_screen_response(raw: str | None, refs: set[int]) -> tuple[dict[int, ScreenOutcome], bool]:
    outcomes = {ref: ScreenOutcome(ref=ref, pre_filter="KEEP", fail_open=True) for ref in refs}
    cleaned = clean_llm_response(raw)
    start = cleaned.find("[")
    end = cleaned.rfind("]")
    if start == -1 or end == -1 or end <= start:
        return outcomes, True
    try:
        parsed = json.loads(cleaned[start : end + 1])
    except Exception:
        return outcomes, True
    if not isinstance(parsed, list):
        return outcomes, True

    fallback = False
    seen: set[int] = set()
    for row in parsed:
        if not isinstance(row, dict):
            fallback = True
            continue
        try:
            ref = int(row.get("ref"))
        except (TypeError, ValueError):
            fallback = True
            continue
        if ref not in refs:
            fallback = True
            continue
        value = str(row.get("pre_filter") or row.get("decision") or row.get("label") or "").upper()
        if value not in {"KEEP", "DISCARD"}:
            fallback = True
            value = "KEEP"
        outcomes[ref] = ScreenOutcome(ref=ref, pre_filter=value, fail_open=False)  # type: ignore[arg-type]
        seen.add(ref)

    missing = refs - seen
    if not seen:
        fallback = True
    return outcomes, fallback


async def _call_screen_batch(client: httpx.AsyncClient, batch: ScreenBatch, model: dict[str, Any]) -> tuple[dict[int, ScreenOutcome], bool]:
    refs = {item.ref for item in batch.items}
    if not refs:
        return {}, False
    if not model.get("api_key"):
        return {ref: ScreenOutcome(ref=ref, pre_filter="KEEP", fail_open=True) for ref in refs}, True

    prompt = screen_prompt(batch)
    payload = {
        "model": model["model"],
        "messages": [
            {
                "role": "system",
                "content": "Return only JSON. Choose KEEP whenever uncertain. DISCARD only clearly irrelevant astronomy abstracts.",
            },
            {"role": "user", "content": prompt},
        ],
        "stream": False,
        "temperature": 0,
    }
    try:
        response = await client.post(
            f"{model['base_url'].rstrip('/')}/chat/completions",
            headers={"Authorization": f"Bearer {model['api_key']}"},
            json=payload,
            timeout=SCREEN_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        data = response.json()
        usage = data.get("usage") or {}
        log_llm_spend(
            "targeted_ads.fast_screen",
            model["model"],
            prompt_tokens=usage.get("prompt_tokens"),
            completion_tokens=usage.get("completion_tokens"),
            estimated_tokens=(len(prompt) // 4) + 500,
            metadata={"refs": sorted(refs), "batch_size": len(refs)},
        )
        raw = response_text_union(data)
        return parse_screen_response(raw, refs)
    except Exception as exc:
        print(f"fast-screen batch failed open: {exc}")
        log_llm_spend(
            "targeted_ads.fast_screen",
            model.get("model", SCREEN_MODEL),
            estimated_tokens=sum(len(item.candidate.record.abstract or "") for item in batch.items) // 4,
            status="failed_open",
            metadata={"refs": sorted(refs), "batch_size": len(refs), "error": str(exc)[:300]},
        )
        return {ref: ScreenOutcome(ref=ref, pre_filter="KEEP", fail_open=True) for ref in refs}, True


async def fast_screen_async(batches: list[ScreenBatch], concurrency: int | None = None) -> tuple[dict[int, ScreenOutcome], int]:
    if not batches:
        return {}, 0
    model = screen_models()[0]
    limit = max(1, int(concurrency or settings.SCREEN_CONCURRENCY))
    semaphore = asyncio.Semaphore(limit)

    async with httpx.AsyncClient() as client:
        async def run(batch: ScreenBatch) -> tuple[dict[int, ScreenOutcome], bool]:
            async with semaphore:
                return await _call_screen_batch(client, batch, model)

        results = await asyncio.gather(*(run(batch) for batch in batches))

    merged: dict[int, ScreenOutcome] = {}
    fallback_count = 0
    for outcomes, fallback in results:
        if fallback:
            fallback_count += 1
        merged.update(outcomes)
    return merged, fallback_count


def jury_models() -> list[dict[str, Any]]:
    studio_base = (settings.OLLAMA_STUDIO_BASE_URL or "http://localhost:11434/v1").rstrip("/")
    if studio_base and not studio_base.endswith("/v1"):
        studio_base = f"{studio_base}/v1"
    buddle_base = (settings.BUDDLE_BASE_URL or "http://localhost:11434").rstrip("/")
    if buddle_base and not buddle_base.endswith("/v1"):
        buddle_base = f"{buddle_base}/v1"
    return [
        {
            "label": "Mima",
            "base_url": studio_base,
            "api_key": "ollama",
            "model": os.getenv("TARGETED_ADS_MIMA_MODEL", "qwen3:30b"),
        },
        {
            "label": "Nutty-Heavy",
            "base_url": os.getenv("TARGETED_ADS_BUDDLE_BASE_URL", buddle_base),
            "api_key": "ollama",
            "model": os.getenv("TARGETED_ADS_BUDDLE_MODEL", "deepseek-r1:70b"),
        },
        {
            "label": "Atom-7B",
            "base_url": studio_base,
            "api_key": "ollama",
            "model": os.getenv("TARGETED_ADS_ATOM_MODEL", "vanta-research/atom-astronomy-7b:latest"),
        },
    ]


def response_text_union(data: dict[str, Any]) -> str:
    parts: list[str] = []
    for key in ("response", "content"):
        value = data.get(key)
        if isinstance(value, str) and value.strip():
            parts.append(value)
    for choice in data.get("choices", []) or []:
        if not isinstance(choice, dict):
            continue
        message = choice.get("message") or {}
        if isinstance(message, dict):
            for key in ("content",):
                value = message.get(key)
                if isinstance(value, str) and value.strip():
                    parts.append(value)
        text = choice.get("text")
        if isinstance(text, str) and text.strip():
            parts.append(text)
    return strip_think_blocks("\n".join(parts))


async def _call_juror(client: httpx.AsyncClient, model: dict[str, Any], prompt: str) -> dict[str, Any] | None:
    if not model["base_url"]:
        return None
    
    if settings.INFERENCE_SCHEDULER_ENABLED:
        from app.services.inference_scheduler import InferenceScheduler
        scheduler = InferenceScheduler()
        try:
            try:
                content = await asyncio.wait_for(
                    scheduler.execute(model, prompt, JURY_TIMEOUT_SECONDS, system_prompt=JURY_SYSTEM_PROMPT),
                    timeout=JURY_TIMEOUT_SECONDS + 120,
                )
            except asyncio.TimeoutError:
                print(f"jury {model['label']} watchdog cancellation after {JURY_TIMEOUT_SECONDS + 120}s")
                return None
            if content is None:
                return None
            return {"label": model["label"], "raw": content}
        except Exception as exc:
            print(f"jury {model['label']} via scheduler failed: {exc}")
            return None
    
    if "deepseek-r1" in model["model"].lower():
        messages = [
            {"role": "user", "content": f"{JURY_SYSTEM_PROMPT}\n\n{prompt}"}
        ]
    else:
        messages = [
            {"role": "system", "content": JURY_SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ]

    payload = {
        "model": model["model"],
        "messages": messages,
        "stream": False,
        "temperature": 0.6,
        "options": {"num_ctx": 8192, "temperature": 0.6},
    }
    try:
        response = await client.post(
            f"{model['base_url'].rstrip('/')}/chat/completions",
            headers={"Authorization": f"Bearer {model['api_key']}"},
            json=payload,
            timeout=JURY_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        data = response.json()
        raw = response_text_union(data)
        if not raw:
            raw = json.dumps(data, ensure_ascii=False)
        return {"label": model["label"], "raw": raw}
    except Exception as exc:
        print(f"jury {model['label']} failed: {exc}")
        return None


async def run_jury_async(claim: Claim | ClaimSnapshot, record: PaperRecord) -> list[dict[str, Any]]:
    prompt = user_prompt(claim, record)
    async with httpx.AsyncClient() as client:
        calls = [_call_juror(client, model, prompt) for model in jury_models()]
        try:
            results = await asyncio.wait_for(
                asyncio.gather(*calls, return_exceptions=True),
                timeout=600.0
            )
        except asyncio.TimeoutError:
            print("jury gather hard timeout after 600s")
            results = []
    filtered_results = []
    for r in results:
        if isinstance(r, dict) and r:
            filtered_results.append(r)
        elif isinstance(r, Exception):
            print(f"jury call exception captured: {r}")
    return filtered_results


def normalize_for_substring(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _last_match(pattern: re.Pattern[str], text: str) -> re.Match[str] | None:
    matches = list(pattern.finditer(text))
    return matches[-1] if matches else None


def parse_juror(label: str, raw: str, abstract: str) -> JurorResult | None:
    raw = strip_think_blocks(raw)
    raw = clean_llm_response(raw)
    
    verdict: Verdict | None = None
    sentence: str | None = None
    confidence: Confidence = "LOW"
    is_json_resp = False

    # Try parsing as JSON first for permissive_v1 policy
    trimmed_raw = raw.strip()
    json_start = trimmed_raw.find("{")
    json_end = trimmed_raw.rfind("}")
    if json_start != -1 and json_end != -1 and json_end > json_start:
        try:
            json_candidate = trimmed_raw[json_start:json_end+1]
            parsed = json.loads(json_candidate)
            is_json_resp = True
            if "vote" in parsed:
                vote_val = parsed["vote"]
                if vote_val == 1:
                    verdict = "SUPPORTS"
                elif vote_val == -1:
                    verdict = "REFUTES"
                else:
                    verdict = "ABSTAIN"
            elif "stance_correct" in parsed:
                if parsed["stance_correct"] is True:
                    verdict = "SUPPORTS"
                elif parsed["stance_correct"] is False:
                    verdict = "ABSTAIN"
            
            if "reason" in parsed:
                sentence = parsed["reason"]
            confidence = "MEDIUM"
        except Exception:
            pass

    # Fallback to standard parsing if not JSON or JSON parsing didn't yield a verdict
    if verdict is None:
        verdict_m = _last_match(VERDICT_RE, raw)
        sentence_m = _last_match(SENTENCE_RE, raw)
        conf_m = _last_match(CONF_RE, raw)

        verdict = verdict_m.group(1).upper() if verdict_m else None  # type: ignore[assignment]
        if verdict is None:
            lowered = raw.lower()
            for keyword in ("refutes", "abstain", "supports"):
                if keyword in lowered:
                    verdict = keyword.upper()  # type: ignore[assignment]
                    break
        if verdict is None:
            return None

        sentence = sentence_m.group(1).strip() if sentence_m else None
        confidence = conf_m.group(1).upper() if conf_m else "LOW"  # type: ignore[assignment]

    downgraded = False
    if verdict in {"SUPPORTS", "REFUTES"}:
        if not sentence or sentence.upper() == "NONE":
            verdict = "ABSTAIN"
            sentence = None
            downgraded = True
        else:
            norm_sentence = normalize_for_substring(sentence)
            norm_abstract = normalize_for_substring(abstract)
            # Skip verbatim quote substring check only if it was parsed as JSON (permissive peer review)
            if norm_sentence not in norm_abstract and not is_json_resp:
                verdict = "ABSTAIN"
                sentence = None
                downgraded = True

    if sentence and sentence.upper() == "NONE":
        sentence = None
    return JurorResult(
        label=label,
        verdict=verdict,
        sentence=sentence,
        confidence=confidence,
        raw=raw,
        downgraded=downgraded,
    )


def confidence_quality(results: list[JurorResult]) -> float:
    support_conf = [r.confidence for r in results if r.verdict == "SUPPORTS"]
    if not support_conf:
        return 0.50
    conf_rank = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
    min_conf = min(support_conf, key=lambda c: conf_rank[c])
    if min_conf == "HIGH":
        return 0.85
    if min_conf == "MEDIUM":
        return 0.65 if len(support_conf) >= 2 and all(c == "MEDIUM" for c in support_conf) else 0.75
    return 0.55


def aggregate_jury(raw_results: list[dict[str, Any]], abstract: str) -> JuryDecision:
    parsed = [
        juror
        for r in raw_results
        if (juror := parse_juror(r["label"], r["raw"], abstract)) is not None
    ]
    support_count = sum(1 for r in parsed if r.verdict == "SUPPORTS")
    refute_count = sum(1 for r in parsed if r.verdict == "REFUTES")
    if refute_count:
        stance: Literal["supports", "refutes", "neutral"] = "refutes"
    elif support_count >= MIN_SUPPORT_VOTES:
        stance = "supports"
    else:
        stance = "neutral"
    quality = confidence_quality(parsed)
    return JuryDecision(
        stance=stance,
        merge_eligible=(stance == "supports" and support_count >= MIN_SUPPORT_VOTES and quality >= 0.65),
        quality=quality,
        results=parsed,
    )


def agent_id_for_label(db: Session, label: str, model_name: str | None = None) -> int:
    name = f"TargetedADS-{label}"
    agent = db.query(Agent).filter(Agent.name == name).first()
    if not agent:
        agent = Agent(name=name, role="jury", model_name=model_name or label, specialty="astronomy")
        db.add(agent)
        db.flush()
    return agent.id


def insert_evidence(db: Session, candidate: Candidate, decision: JuryDecision) -> Evidence:
    record = candidate.record
    data = record.to_evidence_dict()
    ev = Evidence(
        claim_id=candidate.claim.id,
        arxiv_id=data.get("arxiv_id"),
        doi=data.get("doi"),
        url=data.get("url") or (f"https://ui.adsabs.harvard.edu/abs/{record.bibcode}/abstract" if record.bibcode else None),
        title=data.get("title") or record.title,
        authors=data.get("authors"),
        year=data.get("year"),
        summary=next((r.sentence for r in decision.results if r.sentence), None),
        stance=decision.stance if decision.stance != "neutral" else "neutral",
        quality=decision.quality,
        abstract=data.get("abstract"),
        ads_bibcode=data.get("ads_bibcode"),
        s2_paper_id=data.get("s2_paper_id"),
        verified_at=dt.datetime.utcnow() if decision.stance in {"supports", "refutes"} else None,
        stance_jury_run_at=dt.datetime.utcnow(),
        source_channel="targeted_ads_miner",
        arxiv_verified=bool(record.arxiv_id),
        peer_reviewed=True,
    )
    db.add(ev)
    db.flush()

    model_by_label = {model["label"]: model["model"] for model in jury_models()}
    vote_value = {"SUPPORTS": 1, "REFUTES": -1, "ABSTAIN": 0}
    for result in decision.results:
        db.add(
            EvidenceVote(
                evidence_id=ev.id,
                value=vote_value[result.verdict],
                agent_id=agent_id_for_label(db, result.label, model_by_label.get(result.label)),
                reason=(result.sentence or result.verdict)[:500],
                weight=1.0,
                voter_type="agent",
            )
        )
    return ev


def select_claims(db: Session, page_id: int, claim_ids: list[int], limit: int | None, min_claim_id: int | None = None) -> list[Claim]:
    query = db.query(Claim)
    if claim_ids:
        query = query.filter(Claim.id.in_(claim_ids))
    else:
        query = query.filter(Claim.page_id == page_id)
        query = query.filter(Claim.trust_level.in_(["unverified", "debated"]))
    if min_claim_id is not None:
        query = query.filter(Claim.id >= min_claim_id)
    query = query.order_by(Claim.id)
    claims = list(query.all())
    filtered = [claim for claim in claims if claim_ads_class(claim) is not None]
    if limit:
        return filtered[:limit]
    return filtered


async def _jury_candidates_async(candidates: list[Candidate], concurrency: int) -> list[tuple[Candidate, JuryDecision]]:
    semaphore = asyncio.Semaphore(max(1, concurrency))

    async def run(candidate: Candidate) -> tuple[Candidate, JuryDecision]:
        async with semaphore:
            raw_results = await run_jury_async(candidate.claim, candidate.record)
            decision = aggregate_jury(raw_results, candidate.record.abstract or "")
            return candidate, decision

    return await asyncio.gather(*(run(candidate) for candidate in candidates))


def _write_jury_result(db: Session, candidate: Candidate, decision: JuryDecision, *, commit: bool) -> dict[str, int]:
    from app.services.jury_shadow import execute_shadow_validation

    result = {"inserted": 0, "supports": int(decision.merge_eligible)}
    jurors_data = []
    for juror in decision.results:
        vote = 1 if juror.verdict == "SUPPORTS" else (-1 if juror.verdict == "REFUTES" else 0)
        jurors_data.append(
            {
                "agent_id": agent_id_for_label(db, juror.label),
                "vote": vote,
                "confidence_str": juror.confidence,
                "reason": juror.sentence or "",
                "model_name": juror.label,
            }
        )

    ev_id = None
    if commit and decision.merge_eligible:
        ev = insert_evidence(db, candidate, decision)
        db.flush()
        ev_id = ev.id
        result["inserted"] += 1

    execute_shadow_validation(
        db=db,
        evidence_id=ev_id,
        claim_id=candidate.claim.id,
        claim_text=candidate.claim.text,
        evidence_title=candidate.record.title,
        legacy_stance=decision.stance,
        legacy_quality=decision.quality,
        jurors_data=jurors_data,
    )
    if commit:
        db.commit()
    else:
        db.rollback()
    db.close()
    return result


_LAST_PING_TIME: float = 0.0

def ping_jury_agents(db: Session, labels: Iterable[str]) -> None:
    global _LAST_PING_TIME
    import time
    now_time = time.time()
    
    # Throttle: Only update the database once every 60 seconds to save CPU & disk I/O!
    if now_time - _LAST_PING_TIME < 60.0:
        return
        
    try:
        from sqlalchemy import text
        for label in labels:
            db.execute(
                text("UPDATE agents SET last_active = NOW() WHERE name = :n"),
                {"n": f"TargetedADS-{label}"},
            )
        db.commit()
        _LAST_PING_TIME = now_time
    except Exception:
        pass


def run_jury_on_candidates(
    db: Session,
    candidates: list[Candidate],
    *,
    commit: bool,
    concurrency: int,
    audit: bool = False,
) -> dict[str, int]:
    totals = {"supports": 0, "inserted": 0, "false_discard": 0}
    if not candidates:
        return totals

    results = asyncio.run(_jury_candidates_async(candidates, concurrency))
    for candidate, decision in results:
        prefix = "audit " if audit else ""
        verdicts = ", ".join(f"{r.label}:{r.verdict}" for r in decision.results)
        print(
            f"{prefix}claim {candidate.claim.id}: candidate {candidate.record.title[:90]}\n"
            f"  jury stance={decision.stance} quality={decision.quality:.2f} [{verdicts}]"
        )
        ping_jury_agents(db, [r.label for r in decision.results])
        if audit:
            totals["false_discard"] += int(decision.merge_eligible)
            db.rollback()
            db.close()
            continue
        written = _write_jury_result(db, candidate, decision, commit=commit)
        totals["supports"] += written["supports"]
        totals["inserted"] += written["inserted"]
    return totals


def process_claim(db: Session, claim: Claim, *, run_jury: bool, commit: bool, jury_concurrency: int = 1) -> dict[str, Any]:
    claim_snapshot = snapshot_claim(claim)
    candidates = retrieve_candidates(db, claim)
    db.close()
    result: dict[str, Any] = {
        "claim_id": claim_snapshot.id,
        "section": claim_snapshot.section,
        "candidates": len(candidates),
        "inserted": 0,
        "supports": 0,
    }
    for candidate in candidates:
        if not run_jury:
            print(f"claim {claim_snapshot.id}: candidate {candidate.record.title[:90]}")
            continue
    if run_jury:
        jury_totals = run_jury_on_candidates(
            db,
            candidates,
            commit=commit,
            concurrency=jury_concurrency,
        )
        result["supports"] += jury_totals["supports"]
        result["inserted"] += jury_totals["inserted"]
    return result


def collect_candidates(db: Session, claim_ids: list[int]) -> tuple[list[Candidate], dict[int, dict[str, Any]]]:
    all_candidates: list[Candidate] = []
    per_claim: dict[int, dict[str, Any]] = {}
    for claim_id in claim_ids:
        claim = db.get(Claim, claim_id)
        if claim is None:
            continue
        snapshot = snapshot_claim(claim)
        candidates = retrieve_candidates(db, claim)
        db.close()
        per_claim[claim_id] = {
            "claim_id": snapshot.id,
            "section": snapshot.section,
            "candidates": len(candidates),
            "inserted": 0,
            "supports": 0,
        }
        all_candidates.extend(candidates)
    return all_candidates, per_claim


def process_claims(
    db: Session,
    claim_ids: list[int],
    *,
    run_jury: bool,
    commit: bool,
    fast_screen: bool,
    screen_batch: int,
    screen_audit_frac: float | None,
    jury_concurrency: int,
) -> dict[str, Any]:
    candidates, per_claim = collect_candidates(db, claim_ids)
    totals: dict[str, Any] = {
        "claims": len(per_claim),
        "candidates": len(candidates),
        "screened_out": 0,
        "screen_keep": len(candidates),
        "screen_parse_fallback": 0,
        "screen_audited": 0,
        "false_discard": 0,
        "supports": 0,
        "inserted": 0,
    }
    if not run_jury:
        for candidate in candidates:
            print(f"claim {candidate.claim.id}: candidate {candidate.record.title[:90]}")
        return totals

    jury_candidates = candidates
    discard_candidates: list[Candidate] = []
    if fast_screen and candidates:
        batches = build_screen_batches(candidates, screen_batch)
        outcomes, fallback_batches = asyncio.run(fast_screen_async(batches))
        totals["screen_parse_fallback"] = fallback_batches
        keep: list[Candidate] = []
        for ref, candidate in enumerate(candidates):
            outcome = outcomes.get(ref, ScreenOutcome(ref=ref, pre_filter="KEEP", fail_open=True))
            if outcome.pre_filter == "DISCARD":
                discard_candidates.append(candidate)
            else:
                keep.append(candidate)
        jury_candidates = keep
        totals["screened_out"] = len(discard_candidates)
        totals["screen_keep"] = len(keep)
        keep_rate = len(keep) / len(candidates) if candidates else 1.0
        print(
            json.dumps(
                {
                    "fast_screen": True,
                    "candidates": len(candidates),
                    "keep": len(keep),
                    "discard": len(discard_candidates),
                    "keep_rate": round(keep_rate, 4),
                    "fallback_batches": fallback_batches,
                },
                indent=2,
            )
        )

        if discard_candidates:
            if screen_audit_frac is None:
                audit_frac = max(20 / len(discard_candidates), 0.02)
            else:
                audit_frac = max(0.0, screen_audit_frac)
            audit_candidates = [
                candidate for candidate in discard_candidates if random.random() < audit_frac
            ]
            if audit_candidates:
                audit_totals = run_jury_on_candidates(
                    db,
                    audit_candidates,
                    commit=False,
                    concurrency=jury_concurrency,
                    audit=True,
                )
                totals["screen_audited"] = len(audit_candidates)
                totals["false_discard"] = audit_totals["false_discard"]
                totals["false_discard_rate"] = (
                    audit_totals["false_discard"] / len(audit_candidates)
                )

    jury_totals = run_jury_on_candidates(
        db,
        jury_candidates,
        commit=commit,
        concurrency=jury_concurrency,
    )
    totals["supports"] = jury_totals["supports"]
    totals["inserted"] = jury_totals["inserted"]
    return totals


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Targeted ADS evidence miner")
    parser.add_argument("--page-id", type=int, default=57)
    parser.add_argument("--claim-id", action="append", type=int, default=[])
    parser.add_argument("--min-claim-id", type=int, default=None, help="Skip claims with id < this value.")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--commit", action="store_true", help="Insert evidence rows. Default is read-only.")
    parser.add_argument("--no-jury", action="store_true", help="Only run ADS query formulation and deterministic pre-gate.")
    parser.add_argument("--no-fast-screen", action="store_true", help="Disable Gemini fast-screen and run the local jury on every pre-gate survivor.")
    parser.add_argument("--screen-batch", type=int, default=None, help="Fast-screen batch size. Defaults to settings.SCREEN_BATCH.")
    parser.add_argument("--screen-audit-frac", type=float, default=None, help="Override DISCARD shadow-audit sample fraction.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not settings.ADS_API_KEY:
        raise SystemExit("ADS_API_KEY is not configured")
    db = SessionLocal()
    try:
        claims = select_claims(db, args.page_id, args.claim_id, args.limit, args.min_claim_id)
        print(
            json.dumps(
                {
                    "page_id": args.page_id,
                    "claims": len(claims),
                    "commit": args.commit,
                    "jury": not args.no_jury,
                    "mode": "A-citation-only-default/evidence-inserts-only",
                },
                indent=2,
            )
        )
        claim_ids = [claim.id for claim in claims]
        db.close()
        fast_screen = (
            bool(settings.TARGETED_ADS_FAST_SCREEN_ENABLED)
            and not args.no_fast_screen
            and not args.no_jury
        )
        screen_batch = int(args.screen_batch or settings.SCREEN_BATCH)
        if fast_screen:
            totals = process_claims(
                db,
                claim_ids,
                run_jury=not args.no_jury,
                commit=args.commit,
                fast_screen=True,
                screen_batch=screen_batch,
                screen_audit_frac=args.screen_audit_frac,
                jury_concurrency=int(settings.JURY_PAPER_CONCURRENCY),
            )
        else:
            totals = {"claims": 0, "candidates": 0, "supports": 0, "inserted": 0}
            for claim_id in claim_ids:
                claim = db.get(Claim, claim_id)
                if claim is None:
                    continue
                claim_result = process_claim(
                    db,
                    claim,
                    run_jury=not args.no_jury,
                    commit=args.commit,
                    jury_concurrency=1,
                )
                totals["claims"] += 1
                totals["candidates"] += claim_result["candidates"]
                totals["supports"] += claim_result["supports"]
                totals["inserted"] += claim_result["inserted"]
        print(json.dumps(totals, indent=2))
        return 0
    finally:
        db.close()


if __name__ == "__main__":
    raise SystemExit(main())
