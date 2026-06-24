from __future__ import annotations

import asyncio
import datetime as dt
import json
import logging
import re
import time
from dataclasses import dataclass, field
from typing import Any

from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from app.config import settings
from app.models.claim import Claim, Evidence
from app.services.llm_utils import strip_think_blocks
from app.services.paper_search import (
    PaperRecord,
    PaperSearchError,
    ads_reference_bibcodes,
    ads_search,
    s2_references,
)

from app.agent_loop.citation_context.miner import (
    CitationContext,
    LABEL_RE,
    CONF_RE,
    PICO_TIMEOUT_SECONDS,
    SOURCE_CHANNEL as CCM_SOURCE_CHANNEL,
    already_attached,
    ccm_already_linked,
    extract_arxiv_intro_context,
    normalize_text,
)


DCCM_SOURCE_CHANNEL = "dynamic_citation_context_mining"
DCCM_TRUST_TRIGGER = "dccm_dynamic_citation"
logger = logging.getLogger(__name__)
DCCM_MAX_EVIDENCE_PER_CLAIM_LIFETIME = 6
DCCM_MAX_CLAIMS_PER_SEED = 3
DCCM_MIN_SEED_QUALITY = 0.50
TRANSITIVE_CHANNELS = {CCM_SOURCE_CHANNEL, DCCM_SOURCE_CHANNEL}

DCCM_SYSTEM_PROMPT = """You are a precise astronomy citation-context classifier for a knowledge base.

You are given:
  CLAIM: an astronomy statement. It may be recent and still under active study.
  CITED WORK: a paper already in our evidence base that the CLAIM relies on.
  CITATION CONTEXT: one sentence from a NEWER paper that cites the CITED WORK.

Decide how the newer sentence uses the cited work, WITH RESPECT TO THE CLAIM:

  SUPPORTIVE   - The newer paper adopts, confirms, extends, or builds on the
                 cited result as a premise it accepts, AND the sentence concerns
                 the CLAIM's specific subject.

  NONSUPPORTIVE - The newer paper disputes, revises, contrasts, fails to
                  reproduce, or finds tension with the cited result.

  OFFTOPIC     - The citation is generic/list-style, concerns a different result
                 of the cited work, or merely acknowledges existence without
                 endorsing the CLAIM's substance.

Hard rules:
1. Judge ONLY the provided sentence. No outside knowledge about either paper.
2. SUPPORTIVE requires endorsement of the CLAIM's substance, not mere topical overlap.
3. For recent or contested claims, be conservative.
4. Any disputing or in-tension framing => NONSUPPORTIVE.
5. Output ONLY the final block.

Output EXACTLY:
###LABEL: <SUPPORTIVE|NONSUPPORTIVE|OFFTOPIC>
###CONFIDENCE: <LOW|MEDIUM|HIGH>"""

STOPWORDS = {
    "about", "above", "after", "again", "against", "among", "because", "between",
    "claim", "could", "early", "evidence", "galaxies", "galaxy", "large", "model",
    "paper", "result", "results", "small", "their", "there", "these", "those",
    "through", "using", "where", "which", "while", "within",
}


@dataclass(frozen=True)
class DynamicSeed:
    evidence_id: int
    claim_id: int
    claim_text: str
    seed_bibcode: str | None
    seed_doi: str | None
    seed_arxiv_id: str | None
    seed_title: str
    seed_year: int | None
    seed_quality: float
    source_channel: str | None

    @property
    def label(self) -> str:
        year = f" ({self.seed_year})" if self.seed_year else ""
        return f"{self.seed_title[:120]}{year}"


@dataclass(frozen=True)
class DynamicHit:
    seed: DynamicSeed
    new_record: PaperRecord
    cited_record: PaperRecord
    context_sentence: str
    context_source: str
    s2_intent: str | None
    relevance_hits: int


@dataclass
class DccmDecision:
    hit: DynamicHit
    verdict_label: str
    confidence: str | None
    quality: float | None
    action: str


@dataclass
class DccmRunReport:
    dry_run: bool
    seed_count: int = 0
    references_seen: int = 0
    intersections: int = 0
    contexts_fetched: int = 0
    supportive: int = 0
    rejected: int = 0
    held: int = 0
    inserted: int = 0
    capped: int = 0
    primary_floor_blocked: int = 0
    recalculated: dict[int, tuple[str, float]] = field(default_factory=dict)
    decisions: list[DccmDecision] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


def normalize_identifier(kind: str, value: str | None) -> str | None:
    if not value:
        return None
    cleaned = normalize_text(value)
    if not cleaned:
        return None
    if kind == "doi":
        cleaned = cleaned.lower().removeprefix("doi:")
        return f"doi:{cleaned}"
    if kind == "arxiv":
        cleaned = cleaned.replace("arXiv:", "").replace("arxiv:", "").lower()
        return f"arxiv:{cleaned}"
    if kind == "bibcode":
        return f"bibcode:{cleaned}"
    return cleaned.lower()


def record_identifier_keys(record: PaperRecord) -> set[str]:
    keys = set()
    for kind, value in (
        ("bibcode", record.bibcode),
        ("doi", record.doi),
        ("arxiv", record.arxiv_id),
    ):
        key = normalize_identifier(kind, value)
        if key:
            keys.add(key)
    return keys


def seed_identifier_keys(seed: DynamicSeed) -> set[str]:
    keys = set()
    for kind, value in (
        ("bibcode", seed.seed_bibcode),
        ("doi", seed.seed_doi),
        ("arxiv", seed.seed_arxiv_id),
    ):
        key = normalize_identifier(kind, value)
        if key:
            keys.add(key)
    return keys


def load_dynamic_seeds(db: Session) -> list[DynamicSeed]:
    rows = (
        db.query(Evidence, Claim)
        .join(Claim, Claim.id == Evidence.claim_id)
        .filter(Evidence.stance == "supports")
        .filter(Evidence.peer_reviewed.is_(True))
        .filter(Evidence.quality >= DCCM_MIN_SEED_QUALITY)
        .filter(or_(Evidence.ads_bibcode.isnot(None), Evidence.doi.isnot(None)))
        .filter(Claim.claim_type != "debate")
        .filter(Claim.human_override_locked.is_(False))
        .order_by(Evidence.claim_id, Evidence.quality.desc(), Evidence.id)
        .all()
    )
    seeds: list[DynamicSeed] = []
    for ev, claim in rows:
        seeds.append(
            DynamicSeed(
                evidence_id=ev.id,
                claim_id=ev.claim_id,
                claim_text=claim.text,
                seed_bibcode=ev.ads_bibcode,
                seed_doi=ev.doi,
                seed_arxiv_id=ev.arxiv_id,
                seed_title=ev.title,
                seed_year=ev.year,
                seed_quality=float(ev.quality or 0.0),
                source_channel=ev.source_channel,
            )
        )
    return seeds


def build_seed_index(seeds: list[DynamicSeed]) -> dict[str, list[DynamicSeed]]:
    index: dict[str, list[DynamicSeed]] = {}
    for seed in seeds:
        for key in seed_identifier_keys(seed):
            index.setdefault(key, []).append(seed)
    for key in list(index):
        index[key].sort(key=lambda seed: (-seed.seed_quality, seed.claim_id, seed.evidence_id))
    return index


def claim_keyphrases(claim_text: str, limit: int = 12) -> list[str]:
    text = normalize_text(claim_text).lower()
    words = re.findall(r"[a-z][a-z-]{4,}", text)
    out: list[str] = []
    seen = set()
    for word in words:
        if word in STOPWORDS or word in seen:
            continue
        seen.add(word)
        out.append(word)
        if len(out) >= limit:
            break
    return out


def relevance_hits(seed: DynamicSeed, record: PaperRecord, context_sentence: str = "") -> int:
    terms = claim_keyphrases(seed.claim_text)
    haystack = normalize_text(f"{record.title} {record.abstract or ''} {context_sentence}").lower()
    return sum(1 for term in terms if re.search(r"\b" + re.escape(term) + r"\b", haystack))


def has_primary_support(db: Session, claim_id: int) -> bool:
    return bool(
        db.query(Evidence.id)
        .filter(
            Evidence.claim_id == claim_id,
            Evidence.stance == "supports",
            Evidence.source_channel.notin_(TRANSITIVE_CHANNELS),
        )
        .first()
    )


def dynamic_lifetime_count(db: Session, claim_id: int) -> int:
    return int(
        db.query(func.count(Evidence.id))
        .filter(Evidence.claim_id == claim_id, Evidence.source_channel == DCCM_SOURCE_CHANNEL)
        .scalar()
        or 0
    )


def s2_new_paper_identifier(record: PaperRecord) -> str | None:
    if record.doi:
        return f"DOI:{record.doi}"
    if record.arxiv_id:
        return f"arXiv:{record.arxiv_id}"
    if record.s2_id:
        return record.s2_id
    if record.bibcode:
        return f"ADS:{record.bibcode}"
    return None


def _paper_from_s2_ref(item: dict[str, Any]) -> PaperRecord | None:
    paper = item.get("citedPaper") or {}
    if not paper:
        return None
    external = paper.get("externalIds") or {}
    return PaperRecord(
        title=paper.get("title") or "",
        abstract=paper.get("abstract"),
        authors=[],
        year=paper.get("year"),
        arxiv_id=external.get("ArXiv"),
        doi=external.get("DOI"),
        bibcode=external.get("ADS"),
        s2_id=paper.get("paperId"),
        source="s2",
    )


def fetch_s2_reference_index(record: PaperRecord) -> tuple[dict[str, list[dict[str, Any]]], list[PaperRecord]]:
    identifier = s2_new_paper_identifier(record)
    if not identifier:
        return {}, []
    try:
        rows = s2_references(identifier)
    except PaperSearchError:
        return {}, []
    index: dict[str, list[dict[str, Any]]] = {}
    records: list[PaperRecord] = []
    for item in rows:
        cited = _paper_from_s2_ref(item)
        if not cited:
            continue
        records.append(cited)
        for key in record_identifier_keys(cited):
            index.setdefault(key, []).append(item)
    return index, records


def fetch_references_for_paper(record: PaperRecord) -> tuple[list[PaperRecord], dict[str, list[dict[str, Any]]]]:
    s2_index, s2_records = fetch_s2_reference_index(record)
    if record.bibcode:
        try:
            ads_refs = ads_reference_bibcodes(record.bibcode)
            if ads_refs:
                return ads_refs, s2_index
        except PaperSearchError:
            pass
    return s2_records, s2_index


def first_s2_reference_context(seed: DynamicSeed, s2_index: dict[str, list[dict[str, Any]]]) -> tuple[str, str | None] | None:
    for key in seed_identifier_keys(seed):
        for item in s2_index.get(key, []):
            contexts = [normalize_text(c) for c in (item.get("contexts") or []) if normalize_text(c)]
            if contexts:
                intents = item.get("intents") or []
                return contexts[0], (str(intents[0]) if intents else None)
    return None


def extract_dynamic_context(
    seed: DynamicSeed,
    new_record: PaperRecord,
    s2_index: dict[str, list[dict[str, Any]]],
    *,
    arxiv_intro_budget: list[int],
) -> tuple[str, str, str | None] | None:
    s2_context = first_s2_reference_context(seed, s2_index)
    if s2_context:
        return s2_context[0], "s2_context", s2_context[1]
    if new_record.abstract:
        return normalize_text(new_record.abstract)[:1200], "abstract", None
    if new_record.arxiv_id and arxiv_intro_budget[0] > 0:
        arxiv_intro_budget[0] -= 1
        intro = extract_arxiv_intro_context(new_record.arxiv_id, seed.label)
        if intro:
            return intro[:1200], "arxiv_intro", None
    return None


def resolve_intersections(
    db: Session,
    new_record: PaperRecord,
    references: list[PaperRecord],
    s2_index: dict[str, list[dict[str, Any]]],
    *,
    max_claims_per_seed: int = DCCM_MAX_CLAIMS_PER_SEED,
    arxiv_intro_budget: list[int] | None = None,
) -> tuple[list[DynamicHit], int]:
    seeds = load_dynamic_seeds(db)
    seed_index = build_seed_index(seeds)
    budget = arxiv_intro_budget or [5]
    hits: list[DynamicHit] = []
    seen_claim_record: set[tuple[int, str]] = set()
    for ref in references:
        candidate_seeds: list[DynamicSeed] = []
        for key in record_identifier_keys(ref):
            candidate_seeds.extend(seed_index.get(key, [])[:max_claims_per_seed])
        for seed in sorted(candidate_seeds, key=lambda item: (-item.seed_quality, item.claim_id))[:max_claims_per_seed]:
            new_key = next(iter(record_identifier_keys(new_record)), normalize_text(new_record.title).lower())
            dedup_key = (seed.claim_id, new_key)
            if dedup_key in seen_claim_record:
                continue
            seen_claim_record.add(dedup_key)
            if ccm_already_linked(db, seed.claim_id, new_record):
                continue
            extracted = extract_dynamic_context(seed, new_record, s2_index, arxiv_intro_budget=budget)
            if not extracted:
                continue
            context_sentence, context_source, s2_intent = extracted
            hits_count = relevance_hits(seed, new_record, context_sentence)
            if hits_count < 1:
                continue
            hits.append(
                DynamicHit(
                    seed=seed,
                    new_record=new_record,
                    cited_record=ref,
                    context_sentence=context_sentence,
                    context_source=context_source,
                    s2_intent=s2_intent,
                    relevance_hits=hits_count,
                )
            )
    return hits, len(seeds)


def dynamic_quality(label: str, confidence: str | None) -> float | None:
    if label != "SUPPORTIVE":
        return None
    if confidence == "HIGH":
        return 0.72
    if confidence == "MEDIUM":
        return 0.60
    return None


def parse_dynamic_pico_response(raw: str | None) -> tuple[str, str | None]:
    cleaned = strip_think_blocks(raw or "")
    label_matches = LABEL_RE.findall(cleaned)
    conf_matches = CONF_RE.findall(cleaned)
    if not cleaned or not label_matches or not conf_matches:
        return "HOLD", None
    return label_matches[-1].upper(), conf_matches[-1].upper()


def dynamic_user_prompt(ctx: CitationContext) -> str:
    return f"""CLAIM:
{normalize_text(ctx.claim_text)}

CITED WORK: {ctx.seminal_label} (bibcode {ctx.seminal_bibcode})

CITATION CONTEXT (from {ctx.citing_year or 'unknown-year'} paper "{normalize_text(ctx.citing_title)[:180]}"):
"{normalize_text(ctx.context_sentence)}"

CONTEXT SOURCE: {ctx.context_source}
S2 INTENT HINT: {ctx.s2_intent or 'None'}"""


async def classify_dynamic_context_async(ctx: CitationContext, *, model: str | None = None) -> tuple[str, str | None, str, int]:
    from app.services.inference_scheduler import InferenceScheduler

    base_url = (settings.OLLAMA_STUDIO_BASE_URL or "http://localhost:11434/v1").rstrip("/")
    if not base_url.endswith("/v1"):
        base_url = f"{base_url}/v1"
    spec = {
        "base_url": base_url,
        "api_key": "ollama",
        "model": model or settings.ASTRO_SCORER_MODEL or "vanta-research/atom-astronomy-7b",
        "label": "DCCM-Pico",
        "temperature": 0.0,
    }
    started = time.time()
    raw = await InferenceScheduler().execute(
        spec,
        dynamic_user_prompt(ctx),
        PICO_TIMEOUT_SECONDS,
        system_prompt=DCCM_SYSTEM_PROMPT,
    )
    latency_ms = int((time.time() - started) * 1000)
    label, confidence = parse_dynamic_pico_response(raw)
    return label, confidence, raw or "", latency_ms


def classify_dynamic_context(ctx: CitationContext, *, model: str | None = None) -> tuple[str, str | None, str, int]:
    return asyncio.run(classify_dynamic_context_async(ctx, model=model))


def dynamic_hit_to_context(hit: DynamicHit) -> CitationContext:
    return CitationContext(
        claim_id=hit.seed.claim_id,
        claim_text=hit.seed.claim_text,
        seminal_map_id=0,
        seminal_label=hit.seed.label,
        seminal_bibcode=hit.seed.seed_bibcode or hit.seed.seed_doi or "",
        citing_bibcode=hit.new_record.bibcode,
        citing_arxiv_id=hit.new_record.arxiv_id,
        citing_doi=hit.new_record.doi,
        citing_title=hit.new_record.title,
        citing_year=hit.new_record.year,
        context_sentence=hit.context_sentence,
        context_source=hit.context_source,  # type: ignore[arg-type]
        s2_intent=hit.s2_intent,
        keyphrase_hits=hit.relevance_hits,
        citing_record=hit.new_record,
    )


def insert_dynamic_evidence(
    db: Session,
    hit: DynamicHit,
    *,
    quality: float,
    confidence: str | None,
    raw: str,
    latency_ms: int,
) -> Evidence:
    record = hit.new_record
    data = record.to_evidence_dict()
    now = dt.datetime.utcnow()
    ev = Evidence(
        claim_id=hit.seed.claim_id,
        arxiv_id=data.get("arxiv_id"),
        doi=data.get("doi"),
        url=data.get("url") or (f"https://ui.adsabs.harvard.edu/abs/{record.bibcode}/abstract" if record.bibcode else None),
        title=data.get("title") or record.title,
        authors=data.get("authors"),
        year=data.get("year"),
        summary=normalize_text(hit.context_sentence)[:500],
        stance="supports",
        quality=quality,
        abstract=data.get("abstract"),
        ads_bibcode=data.get("ads_bibcode"),
        s2_paper_id=data.get("s2_paper_id"),
        verified_at=now,
        stance_jury_run_at=now,
        source_channel=DCCM_SOURCE_CHANNEL,
        arxiv_verified=bool(record.arxiv_id),
        peer_reviewed=True,
    )
    db.add(ev)
    db.flush()
    logger.info(
        "dccm_evidence_inserted_provisional_no_vote %s",
        {
            "evidence_id": ev.id,
            "claim_id": ev.claim_id,
            "source_channel": DCCM_SOURCE_CHANNEL,
            "latency_ms": latency_ms,
        },
    )
    return ev


def process_dynamic_paper(
    db: Session,
    new_record: PaperRecord,
    *,
    dry_run: bool,
    references: list[PaperRecord] | None = None,
    max_claims_per_seed: int = DCCM_MAX_CLAIMS_PER_SEED,
    lifetime_cap: int = DCCM_MAX_EVIDENCE_PER_CLAIM_LIFETIME,
    arxiv_intro_cap: int = 5,
    classify_fn=classify_dynamic_context,
) -> DccmRunReport:
    report = DccmRunReport(dry_run=dry_run)
    if references is None:
        references, s2_index = fetch_references_for_paper(new_record)
    else:
        s2_index, _ = fetch_s2_reference_index(new_record)
    report.references_seen = len(references)
    hits, seed_count = resolve_intersections(
        db,
        new_record,
        references,
        s2_index,
        max_claims_per_seed=max_claims_per_seed,
        arxiv_intro_budget=[arxiv_intro_cap],
    )
    report.seed_count = seed_count
    report.intersections = len(hits)
    report.contexts_fetched = len(hits)
    touched_claims: set[int] = set()

    for hit in hits:
        ctx = dynamic_hit_to_context(hit)
        label, confidence, raw, latency_ms = classify_fn(ctx)
        quality = dynamic_quality(label, confidence)
        if label == "SUPPORTIVE" and quality is not None:
            if not has_primary_support(db, hit.seed.claim_id):
                report.primary_floor_blocked += 1
                action = "primary_floor_blocked"
            elif dynamic_lifetime_count(db, hit.seed.claim_id) >= lifetime_cap:
                report.capped += 1
                action = "lifetime_cap_blocked"
            elif already_attached(db, hit.seed.claim_id, new_record):
                action = "duplicate_skipped"
            elif dry_run:
                report.supportive += 1
                action = "would_insert"
            else:
                insert_dynamic_evidence(
                    db,
                    hit,
                    quality=quality,
                    confidence=confidence,
                    raw=raw,
                    latency_ms=latency_ms,
                )
                report.supportive += 1
                report.inserted += 1
                touched_claims.add(hit.seed.claim_id)
                action = "inserted"
        elif label == "SUPPORTIVE":
            report.held += 1
            action = "hold_low_confidence"
        elif label == "HOLD":
            report.held += 1
            action = "hold_empty_or_unparsed"
        else:
            report.rejected += 1
            action = "rejected"
        report.decisions.append(DccmDecision(hit, label, confidence, quality, action))
        time.sleep(0.3)

    if dry_run:
        db.rollback()
    elif touched_claims:
        from app.routers.claims import recalculate_trust_v2

        for claim_id in sorted(touched_claims):
            report.recalculated[claim_id] = recalculate_trust_v2(claim_id, db, trigger=DCCM_TRUST_TRIGGER)
        db.commit()
    return report


def evidence_to_record(ev: Evidence) -> PaperRecord:
    authors = []
    if ev.authors:
        try:
            loaded = json.loads(ev.authors)
            if isinstance(loaded, list):
                authors = [str(item) for item in loaded]
        except Exception:
            authors = [ev.authors]
    return PaperRecord(
        title=ev.title,
        abstract=ev.abstract,
        authors=authors,
        year=ev.year,
        arxiv_id=ev.arxiv_id,
        doi=ev.doi,
        bibcode=ev.ads_bibcode,
        s2_id=ev.s2_paper_id,
        source="evidence",
    )


def resolve_new_record(
    db: Session,
    *,
    evidence_id: int | None = None,
    bibcode: str | None = None,
    doi: str | None = None,
    arxiv_id: str | None = None,
    title: str | None = None,
    abstract: str | None = None,
    year: int | None = None,
) -> PaperRecord:
    if evidence_id is not None:
        ev = db.get(Evidence, evidence_id)
        if not ev:
            raise ValueError(f"Evidence #{evidence_id} not found")
        return evidence_to_record(ev)
    if bibcode:
        try:
            records = ads_search(f'bibcode:"{bibcode}"', rows=1, fq=None)
            if records:
                return records[0]
        except PaperSearchError:
            pass
    if not (bibcode or doi or arxiv_id or title):
        raise ValueError("Provide evidence_id, bibcode, doi, arxiv_id, or title")
    return PaperRecord(
        title=title or bibcode or doi or arxiv_id or "Untitled paper",
        abstract=abstract,
        year=year,
        arxiv_id=arxiv_id,
        doi=doi,
        bibcode=bibcode,
        source="manual",
    )
