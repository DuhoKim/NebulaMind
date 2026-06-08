from __future__ import annotations

import asyncio
import datetime as dt
import html
import json
import re
import time
import urllib.request
from dataclasses import dataclass, field
from typing import Any, Literal

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.config import settings
from app.models.agent import Agent
from app.models.claim import Claim, Evidence, EvidenceVote
import app.models.jury  # Ensure ForeignKey metadata is fully resolved to avoid NoReferencedTableError on flush
from app.models.seminal import SeminalClaimMap
from app.services.llm_utils import strip_think_blocks
from app.services.paper_search import (
    PaperRecord,
    PaperSearchError,
    ads_citing_papers,
    s2_citation_contexts,
)


SOURCE_CHANNEL = "citation_context_mining"
TRUST_TRIGGER = "ccm_citation_context"
DEFAULT_MIN_YEAR = dt.datetime.utcnow().year - 2
DEFAULT_ADS_ROWS = 200
DEFAULT_MAX_MAPS = 16
DEFAULT_MAX_CANDIDATES_PER_MAP = 20
DEFAULT_MAX_EVIDENCE_PER_CLAIM = 6
DEFAULT_ARXIV_INTRO_CAP = 5
PICO_TIMEOUT_SECONDS = 60

CCM_SYSTEM_PROMPT = """You are a precise astronomy citation-context classifier for a knowledge base.

You are given:
  CLAIM: a settled, foundational astronomy statement.
  SEMINAL WORK: the historical paper that the claim attributes the result to.
  CITATION CONTEXT: one sentence from a MODERN paper that cites the SEMINAL WORK.

Decide how the modern sentence uses the seminal work, with respect to the CLAIM:

  SUPPORTIVE  - The sentence treats the seminal result as accepted background,
                standard framework, established method, or a premise the modern
                paper builds on or assumes.

  NONSUPPORTIVE - The sentence cites the seminal work to dispute, revise,
                  challenge, correct, or contrast against it.

  OFFTOPIC    - The sentence cites the seminal work for a reason unrelated to
                the substance of the CLAIM, or is only a passing list citation
                with no assertion about the claim's content.

Hard rules:
1. Judge ONLY the provided sentence. Do not use outside knowledge about the paper.
2. SUPPORTIVE requires that the sentence actually concerns the CLAIM's subject.
3. If the sentence both builds on AND partially disputes, choose NONSUPPORTIVE.
4. Do not be generous. A vague mention with no clear stance is OFFTOPIC.
5. Output ONLY the final block, nothing after it.

Output EXACTLY:
###LABEL: <SUPPORTIVE|NONSUPPORTIVE|OFFTOPIC>
###CONFIDENCE: <LOW|MEDIUM|HIGH>"""

LABEL_RE = re.compile(r"###LABEL:\s*(SUPPORTIVE|NONSUPPORTIVE|OFFTOPIC)", re.I)
CONF_RE = re.compile(r"###CONFIDENCE:\s*(LOW|MEDIUM|HIGH)", re.I)
MARKER_RE = re.compile(r"<!--.*?-->", re.DOTALL)
SPACE_RE = re.compile(r"\s+")
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")


@dataclass(frozen=True)
class CitationContext:
    claim_id: int
    claim_text: str
    seminal_map_id: int
    seminal_label: str
    seminal_bibcode: str
    citing_bibcode: str | None
    citing_arxiv_id: str | None
    citing_doi: str | None
    citing_title: str
    citing_year: int | None
    context_sentence: str
    context_source: Literal["s2_context", "abstract", "arxiv_intro"]
    s2_intent: str | None
    keyphrase_hits: int
    citing_record: PaperRecord


@dataclass(frozen=True)
class PicoVerdict:
    label: Literal["SUPPORTIVE", "NONSUPPORTIVE", "OFFTOPIC", "HOLD"]
    confidence: Literal["LOW", "MEDIUM", "HIGH"] | None
    raw: str = ""
    latency_ms: int | None = None

    @property
    def quality(self) -> float | None:
        if self.label != "SUPPORTIVE":
            return None
        if self.confidence == "HIGH":
            return 0.80
        if self.confidence == "MEDIUM":
            return 0.68
        return None


@dataclass
class CcmDecision:
    context: CitationContext
    verdict: PicoVerdict
    action: str


@dataclass
class CcmRunReport:
    dry_run: bool
    maps_seen: int = 0
    ads_citers_seen: int = 0
    contexts_fetched: int = 0
    supportive: int = 0
    rejected: int = 0
    held: int = 0
    inserted: int = 0
    recalculated: dict[int, tuple[str, float]] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    decisions: list[CcmDecision] = field(default_factory=list)


def normalize_text(text: str | None) -> str:
    if not text:
        return ""
    return SPACE_RE.sub(" ", MARKER_RE.sub(" ", text)).strip()


def parse_keyphrases(raw: str | None) -> list[str]:
    if not raw:
        return []
    try:
        data = json.loads(raw)
    except Exception:
        return []
    if not isinstance(data, list):
        return []
    return [str(item).strip() for item in data if str(item).strip()]


def keyphrase_hits(keyphrases: list[str], text: str) -> int:
    haystack = normalize_text(text).lower()
    hits = 0
    for phrase in keyphrases:
        cleaned = normalize_text(phrase).lower()
        if cleaned and cleaned in haystack:
            hits += 1
    return hits


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


def ccm_already_linked(db: Session, claim_id: int, record: PaperRecord) -> bool:
    if already_attached(db, claim_id, record):
        return True
    if record.bibcode:
        return bool(
            db.query(Evidence.id)
            .filter(
                Evidence.claim_id == claim_id,
                Evidence.ads_bibcode == record.bibcode,
                Evidence.source_channel == SOURCE_CHANNEL,
            )
            .first()
        )
    return False


def record_key(record: PaperRecord) -> str:
    return (record.arxiv_id or record.doi or record.bibcode or record.title or "").lower().strip()


def s2_seminal_identifier(mapping: SeminalClaimMap) -> str:
    if mapping.canonical_doi:
        return f"DOI:{mapping.canonical_doi}"
    if mapping.canonical_arxiv_id:
        return f"arXiv:{mapping.canonical_arxiv_id}"
    return f"ADS:{mapping.canonical_bibcode}"


def s2_record_keys(item: dict[str, Any]) -> set[str]:
    citing = item.get("citingPaper") or {}
    external = citing.get("externalIds") or {}
    keys = set()
    for key in ("ArXiv", "DOI", "CorpusId", "MAG", "ACL", "PubMed"):
        value = external.get(key)
        if value:
            keys.add(str(value).lower().strip())
    title = citing.get("title")
    if title:
        keys.add(str(title).lower().strip())
    return keys


def record_lookup_keys(record: PaperRecord) -> set[str]:
    keys = set()
    for value in (record.arxiv_id, record.doi, record.s2_id, record.title):
        if value:
            keys.add(str(value).lower().strip())
    return keys


def fetch_s2_context_index(mapping: SeminalClaimMap) -> dict[str, list[dict[str, Any]]]:
    contexts: dict[str, list[dict[str, Any]]] = {}
    try:
        rows = s2_citation_contexts(s2_seminal_identifier(mapping))
    except PaperSearchError:
        return contexts
    for item in rows:
        for key in s2_record_keys(item):
            contexts.setdefault(key, []).append(item)
    return contexts


def first_s2_context(record: PaperRecord, index: dict[str, list[dict[str, Any]]]) -> tuple[str, str | None] | None:
    for key in record_lookup_keys(record):
        for item in index.get(key, []):
            contexts = [str(c).strip() for c in (item.get("contexts") or []) if str(c).strip()]
            if contexts:
                intents = item.get("intents") or []
                return contexts[0], (str(intents[0]) if intents else None)
    return None


def _label_author_year_tokens(label: str) -> tuple[list[str], str | None]:
    year_match = re.search(r"\b(19|20)\d{2}\b", label)
    year = year_match.group(0) if year_match else None
    before_year = label[: year_match.start()] if year_match else label
    before_year = before_year.replace("et al.", " ").replace("&", " ")
    surnames = [token for token in re.findall(r"[A-Z][A-Za-z-]+", before_year) if token.lower() not in {"the"}]
    return surnames[:3], year


def extract_arxiv_intro_context(arxiv_id: str, seminal_label: str, timeout: int = 20) -> str | None:
    surnames, year = _label_author_year_tokens(seminal_label)
    if not surnames and not year:
        return None
    url = f"https://ar5iv.labs.arxiv.org/html/{arxiv_id}"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="ignore")
    except Exception:
        return None
    lower = raw.lower()
    start = lower.find("introduction")
    if start == -1:
        start = 0
    chunk = raw[start : start + 30000]
    text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", chunk, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = normalize_text(html.unescape(text))
    for sentence in SENTENCE_RE.split(text):
        sent_lower = sentence.lower()
        surname_hit = any(surname.lower() in sent_lower for surname in surnames)
        year_hit = bool(year and year in sent_lower)
        if surname_hit and (year_hit or len(surnames) == 1):
            return sentence.strip()
    return None


def extract_context_for_record(
    mapping: SeminalClaimMap,
    record: PaperRecord,
    s2_index: dict[str, list[dict[str, Any]]],
    *,
    arxiv_intro_budget: list[int],
) -> tuple[str, str, str | None] | None:
    s2_context = first_s2_context(record, s2_index)
    if s2_context:
        return s2_context[0], "s2_context", s2_context[1]
    if record.abstract:
        return normalize_text(record.abstract)[:1200], "abstract", None
    if record.arxiv_id and arxiv_intro_budget[0] > 0:
        arxiv_intro_budget[0] -= 1
        intro = extract_arxiv_intro_context(record.arxiv_id, mapping.canonical_label)
        if intro:
            return intro[:1200], "arxiv_intro", None
    return None


def build_pico_user_prompt(ctx: CitationContext) -> str:
    title = normalize_text(ctx.citing_title)[:180]
    return f"""CLAIM:
{normalize_text(ctx.claim_text)}

SEMINAL WORK: {ctx.seminal_label} (bibcode {ctx.seminal_bibcode})

CITATION CONTEXT (from {ctx.citing_year or 'unknown-year'} paper "{title}"):
"{normalize_text(ctx.context_sentence)}"

CONTEXT SOURCE: {ctx.context_source}
S2 INTENT HINT: {ctx.s2_intent or 'None'}"""


def parse_pico_response(raw: str | None, latency_ms: int | None = None) -> PicoVerdict:
    cleaned = strip_think_blocks(raw or "")
    label_matches = LABEL_RE.findall(cleaned)
    conf_matches = CONF_RE.findall(cleaned)
    if not cleaned or not label_matches or not conf_matches:
        return PicoVerdict(label="HOLD", confidence=None, raw=cleaned, latency_ms=latency_ms)
    return PicoVerdict(
        label=label_matches[-1].upper(),  # type: ignore[arg-type]
        confidence=conf_matches[-1].upper(),  # type: ignore[arg-type]
        raw=cleaned,
        latency_ms=latency_ms,
    )


async def classify_context_async(ctx: CitationContext, *, model: str | None = None) -> PicoVerdict:
    from app.services.inference_scheduler import InferenceScheduler

    base_url = (settings.OLLAMA_STUDIO_BASE_URL or "http://localhost:11434/v1").rstrip("/")
    if not base_url.endswith("/v1"):
        base_url = f"{base_url}/v1"
    spec = {
        "base_url": base_url,
        "api_key": "ollama",
        "model": model or settings.ASTRO_SCORER_MODEL or "vanta-research/atom-astronomy-7b",
        "label": "CCM-Pico",
        "temperature": 0.0,
    }
    started = time.time()
    raw = await InferenceScheduler().execute(
        spec,
        build_pico_user_prompt(ctx),
        PICO_TIMEOUT_SECONDS,
        system_prompt=CCM_SYSTEM_PROMPT,
    )
    latency_ms = int((time.time() - started) * 1000)
    return parse_pico_response(raw, latency_ms=latency_ms)


def classify_context(ctx: CitationContext, *, model: str | None = None) -> PicoVerdict:
    return asyncio.run(classify_context_async(ctx, model=model))


def agent_id_for_label(db: Session, label: str, model_name: str) -> int:
    name = f"CCM-{label}"
    agent = db.query(Agent).filter(Agent.name == name).first()
    if not agent:
        agent = Agent(name=name, role="jury", model_name=model_name, specialty="astronomy")
        db.add(agent)
        db.flush()
    return agent.id


def insert_supportive_evidence(db: Session, ctx: CitationContext, verdict: PicoVerdict) -> Evidence:
    record = ctx.citing_record
    data = record.to_evidence_dict()
    now = dt.datetime.utcnow()
    ev = Evidence(
        claim_id=ctx.claim_id,
        arxiv_id=data.get("arxiv_id"),
        doi=data.get("doi"),
        url=data.get("url") or (f"https://ui.adsabs.harvard.edu/abs/{record.bibcode}/abstract" if record.bibcode else None),
        title=data.get("title") or record.title,
        authors=data.get("authors"),
        year=data.get("year"),
        summary=normalize_text(ctx.context_sentence)[:500],
        stance="supports",
        quality=verdict.quality or 0.68,
        abstract=data.get("abstract"),
        ads_bibcode=data.get("ads_bibcode"),
        s2_paper_id=data.get("s2_paper_id"),
        verified_at=now,
        stance_jury_run_at=now,
        source_channel=SOURCE_CHANNEL,
        arxiv_verified=bool(record.arxiv_id),
        peer_reviewed=True,
    )
    db.add(ev)
    db.flush()
    db.add(
        EvidenceVote(
            evidence_id=ev.id,
            value=1,
            agent_id=agent_id_for_label(db, "Pico", settings.ASTRO_SCORER_MODEL or "vanta-research/atom-astronomy-7b"),
            reason=normalize_text(ctx.context_sentence)[:500],
            weight=1.0,
            voter_type="agent",
            scheduled_via="ccm",
            latency_ms=verdict.latency_ms,
        )
    )
    return ev


def load_enabled_maps(
    db: Session,
    *,
    map_ids: list[int] | None = None,
    claim_ids: list[int] | None = None,
    limit: int | None = None,
) -> list[SeminalClaimMap]:
    query = db.query(SeminalClaimMap).filter(SeminalClaimMap.enabled.is_(True))
    if map_ids:
        query = query.filter(SeminalClaimMap.id.in_(map_ids))
    if claim_ids:
        query = query.filter(SeminalClaimMap.claim_id.in_(claim_ids))
    query = query.order_by(SeminalClaimMap.claim_id, SeminalClaimMap.id)
    if limit:
        query = query.limit(limit)
    return list(query.all())


def build_contexts_for_mapping(
    db: Session,
    mapping: SeminalClaimMap,
    *,
    min_year: int,
    ads_rows: int,
    max_candidates: int,
    arxiv_intro_budget: list[int],
) -> tuple[list[CitationContext], int]:
    claim = db.get(Claim, mapping.claim_id)
    if not claim:
        return [], 0
    try:
        records = ads_citing_papers(mapping.canonical_bibcode, rows=ads_rows, min_year=min_year)
    except PaperSearchError:
        return [], 0
    s2_index = fetch_s2_context_index(mapping)
    keyphrases = parse_keyphrases(mapping.topic_keyphrases)
    contexts: list[CitationContext] = []
    seen: set[str] = set()
    for record in records:
        if record.year is not None and record.year < min_year:
            continue
        key = record_key(record)
        if not key or key in seen:
            continue
        seen.add(key)
        if ccm_already_linked(db, mapping.claim_id, record):
            continue
        extracted = extract_context_for_record(mapping, record, s2_index, arxiv_intro_budget=arxiv_intro_budget)
        if not extracted:
            continue
        context_sentence, context_source, s2_intent = extracted
        hits = keyphrase_hits(keyphrases, f"{context_sentence} {record.title} {record.abstract or ''}")
        if hits < 1:
            continue
        contexts.append(
            CitationContext(
                claim_id=mapping.claim_id,
                claim_text=claim.text,
                seminal_map_id=mapping.id,
                seminal_label=mapping.canonical_label,
                seminal_bibcode=mapping.canonical_bibcode,
                citing_bibcode=record.bibcode,
                citing_arxiv_id=record.arxiv_id,
                citing_doi=record.doi,
                citing_title=record.title,
                citing_year=record.year,
                context_sentence=context_sentence,
                context_source=context_source,  # type: ignore[arg-type]
                s2_intent=s2_intent,
                keyphrase_hits=hits,
                citing_record=record,
            )
        )
        if len(contexts) >= max_candidates:
            break
    return contexts, len(records)


def run_ccm_cycle(
    db: Session,
    *,
    dry_run: bool,
    map_ids: list[int] | None = None,
    claim_ids: list[int] | None = None,
    min_year: int = DEFAULT_MIN_YEAR,
    max_maps: int = DEFAULT_MAX_MAPS,
    ads_rows: int = DEFAULT_ADS_ROWS,
    max_candidates_per_map: int = DEFAULT_MAX_CANDIDATES_PER_MAP,
    max_evidence_per_claim: int = DEFAULT_MAX_EVIDENCE_PER_CLAIM,
    arxiv_intro_cap: int = DEFAULT_ARXIV_INTRO_CAP,
    classify_fn=classify_context,
) -> CcmRunReport:
    report = CcmRunReport(dry_run=dry_run)
    maps = load_enabled_maps(db, map_ids=map_ids, claim_ids=claim_ids, limit=max_maps)
    report.maps_seen = len(maps)
    arxiv_intro_budget = [arxiv_intro_cap]
    inserted_by_claim: dict[int, int] = {}

    for mapping in maps:
        contexts, ads_seen = build_contexts_for_mapping(
            db,
            mapping,
            min_year=min_year,
            ads_rows=ads_rows,
            max_candidates=max_candidates_per_map,
            arxiv_intro_budget=arxiv_intro_budget,
        )
        report.ads_citers_seen += ads_seen
        report.contexts_fetched += len(contexts)
        for ctx in contexts:
            if inserted_by_claim.get(ctx.claim_id, 0) >= max_evidence_per_claim:
                continue
            verdict = classify_fn(ctx)
            if verdict.label == "SUPPORTIVE" and verdict.quality is not None:
                action = "would_insert" if dry_run else "inserted"
                report.supportive += 1
                if not dry_run:
                    if ccm_already_linked(db, ctx.claim_id, ctx.citing_record):
                        action = "duplicate_skipped"
                    else:
                        insert_supportive_evidence(db, ctx, verdict)
                        inserted_by_claim[ctx.claim_id] = inserted_by_claim.get(ctx.claim_id, 0) + 1
                        report.inserted += 1
                report.decisions.append(CcmDecision(ctx, verdict, action))
            elif verdict.label == "SUPPORTIVE":
                report.held += 1
                report.decisions.append(CcmDecision(ctx, verdict, "hold_low_confidence"))
            elif verdict.label == "HOLD":
                report.held += 1
                report.decisions.append(CcmDecision(ctx, verdict, "hold_empty_or_unparsed"))
            else:
                report.rejected += 1
                report.decisions.append(CcmDecision(ctx, verdict, "rejected"))
            time.sleep(0.3)

    if not dry_run and report.inserted:
        from app.routers.claims import recalculate_trust_v2

        for claim_id in sorted(inserted_by_claim):
            report.recalculated[claim_id] = recalculate_trust_v2(claim_id, db, trigger=TRUST_TRIGGER)
        db.commit()
    elif dry_run:
        db.rollback()
    return report
