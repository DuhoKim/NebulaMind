"""Coverage screen for generated research ideas.

The screen can prove that an idea is already covered or detect confabulated
entities. A pass means no covering work was found in the retrieved ADS sample.
"""

from __future__ import annotations

import json
import logging
import os
import re
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.config import settings
from app.services.paper_search import PaperRecord, PaperSearchError, ads_search

log = logging.getLogger(__name__)

COVERAGE_PASS_STATUSES = {"screened_pass", "partial"}
FAILED_STATUSES = {"covered", "failed_entity"}
VALID_STATUSES = COVERAGE_PASS_STATUSES | FAILED_STATUSES | {"inconclusive"}
CALIBRATION_FIXTURE_MODEL_CHAIN = "novelty-calibration-fixture-v2"

CONTROLLED_VOCAB = {
    "DESI",
    "SDSS",
    "HST",
    "JWST",
    "Chandra",
    "Spitzer",
    "Herschel",
    "Euclid",
    "LSST",
    "Rubin",
    "Roman",
    "SKA",
    "ALMA",
    "VLA",
    "MeerKAT",
    "eROSITA",
    "HSC",
    "NIRCam",
    "NIRSpec",
    "MIRI",
    "WISE",
    "GALEX",
    "2MASS",
    "COSMOS",
    "CANDELS",
    "CEERS",
    "JADES",
    "PRIMER",
    "RUBIES",
    "ASPECS",
    "REBELS",
    "CRISTAL",
}

KNOWN_BAD_ENTITIES = {
    "DESI Legacy Survey of Space and Time",
    "DESI Legacy Survey of Space & Time",
}

ENTITY_RE = re.compile(
    r"\b(?:[A-Z][A-Za-z0-9]*(?:[- ][A-Z0-9][A-Za-z0-9]*){0,6}|eROSITA|MeerKAT)\b"
)
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9-]{3,}")
STOPWORDS = {
    "with", "from", "that", "this", "does", "show", "test", "fixed", "mass",
    "galaxy", "galaxies", "stellar", "survey", "surveys", "catalog", "public",
    "released", "measure", "compare", "relation", "fraction", "using",
}


@dataclass(frozen=True)
class EntityValidationResult:
    ok: bool
    offending_terms: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class RetrievedWork:
    bibcode: str | None
    title: str
    abstract: str
    year: int | None = None
    authors: list[str] = field(default_factory=list)
    citation_count: int | None = None


@dataclass(frozen=True)
class ScreenResult:
    idea_id: int
    coverage_status: str
    closest_prior_work: list[dict[str, Any]] = field(default_factory=list)
    papers_checked: int = 0
    offending_terms: list[str] = field(default_factory=list)
    retrieval_queries: list[str] = field(default_factory=list)
    raw_adjudication: dict[str, Any] | None = None

    @property
    def factual_verified(self) -> bool:
        return self.coverage_status in COVERAGE_PASS_STATUSES


def derive_factual_verified(coverage_status: str | None) -> bool:
    return coverage_status in COVERAGE_PASS_STATUSES


def registry_terms(db: Session) -> set[str]:
    terms = set(CONTROLLED_VOCAB)
    table_columns = {
        "surveys": ("name", "slug"),
        "survey_datasets": ("name", "slug", "full_name"),
    }
    for table_name, columns in table_columns.items():
        try:
            rows = db.execute(text(f"SELECT {', '.join(columns)} FROM {table_name}")).fetchall()
        except Exception:
            continue
        for row in rows:
            for column in columns:
                value = getattr(row, column, None)
                if value:
                    terms.add(str(value))
                    terms.add(str(value).upper())
    return terms


def _known_term(term: str, registry: set[str]) -> bool:
    if term in registry or term.upper() in registry:
        return True
    normalized = term.replace("-", " ").strip()
    if normalized in registry or normalized.upper() in registry:
        return True
    pieces = [piece for piece in re.split(r"\s+", normalized) if piece]
    return len(pieces) > 1 and all(_known_term(piece, registry) for piece in pieces)


def validate_entities(idea: Any, db: Session, registry: set[str] | None = None) -> EntityValidationResult:
    registry = registry or registry_terms(db)
    text_blob = f"{getattr(idea, 'approach', '')}\n{getattr(idea, 'why_now', '')}"
    offending: list[str] = []

    for bad in KNOWN_BAD_ENTITIES:
        if re.search(r"\b" + re.escape(bad) + r"\b", text_blob, re.I):
            offending.append(bad)

    for match in ENTITY_RE.finditer(text_blob):
        term = match.group(0).strip()
        if len(term) < 3 or term in {"For", "The", "Compare", "Measure"}:
            continue
        if any(char.isdigit() for char in term) and "-" not in term:
            continue
        if term.lower() in STOPWORDS:
            continue
        if term.isupper() or any(c.isupper() for c in term[1:]):
            if not _known_term(term, registry):
                offending.append(term)

    deduped = sorted(set(offending), key=str.lower)
    return EntityValidationResult(ok=not deduped, offending_terms=deduped)


def _keywords(*parts: str) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    text_blob = " ".join(p for p in parts if p)
    phrases = [
        "mass-metallicity relation",
        "star formation",
        "quenched fraction",
        "molecular gas",
        "weak lensing",
        "halo mass",
        "stellar age",
        "environment",
        "clustering bias",
        "morphology",
        "kinematics",
    ]
    lower = text_blob.lower()
    for phrase in phrases:
        if phrase in lower:
            seen.add(phrase)
            out.append(phrase)
    for token in TOKEN_RE.findall(text_blob):
        token_l = token.lower()
        if token_l in STOPWORDS or token_l in seen:
            continue
        seen.add(token_l)
        out.append(token_l)
        if len(out) >= 8:
            break
    return out


def build_ads_queries(idea: Any) -> list[str]:
    survey_terms = [t.strip() for t in str(getattr(idea, "survey_combo", "") or "").split("+") if t.strip()]
    keys = _keywords(getattr(idea, "question", ""), getattr(idea, "approach", ""), getattr(idea, "why_now", ""))
    if not keys:
        keys = ["galaxy evolution"]
    survey_clause = " OR ".join(f'abs:"{s}"' for s in survey_terms[:3]) or 'abs:"galaxy evolution"'
    focused = " AND ".join(f'abs:"{k}"' for k in keys[:3])
    broad = " OR ".join(f'abs:"{k}"' for k in keys[:5])
    titleish = " AND ".join(f'abs:"{k}"' for k in keys[:2])
    queries = [
        f"({survey_clause}) AND ({focused}) AND property:refereed",
        f"({survey_clause}) AND ({broad}) AND property:refereed",
        f"({titleish}) AND property:refereed",
    ]
    return list(dict.fromkeys(queries))


def _record_to_work(record: PaperRecord) -> RetrievedWork | None:
    if not record.abstract:
        return None
    return RetrievedWork(
        bibcode=record.bibcode,
        title=record.title,
        abstract=record.abstract,
        year=record.year,
        authors=record.authors,
        citation_count=record.citation_count,
    )


def retrieve_ads_works(idea: Any, *, rows: int = 20) -> tuple[list[RetrievedWork], list[str]]:
    works: list[RetrievedWork] = []
    seen: set[str] = set()
    queries = build_ads_queries(idea)
    for query in queries:
        try:
            records = ads_search(query, rows=rows, sort="citation_count desc", fq="database:astronomy")
        except PaperSearchError as exc:
            log.warning("ADS retrieval failed for idea %s: %s", getattr(idea, "id", "?"), exc)
            continue
        for record in records:
            key = record.bibcode or record.doi or record.arxiv_id or record.title.lower().strip()
            if not key or key in seen:
                continue
            work = _record_to_work(record)
            if work is None:
                continue
            seen.add(key)
            works.append(work)
            if len(works) >= rows:
                return works, queries
    return works, queries


def _extract_json(text_body: str) -> dict[str, Any]:
    try:
        return json.loads(text_body)
    except json.JSONDecodeError:
        match = re.search(r"\{[\s\S]*\}", text_body)
        if not match:
            raise
        return json.loads(match.group(0))


def adjudicate_coverage(idea: Any, works: Iterable[RetrievedWork]) -> dict[str, Any]:
    import anthropic

    api_key = settings.ANTHROPIC_API_KEY or os.getenv("NM_ANTHROPIC_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not configured")

    work_list = list(works)
    abstracts = "\n\n".join(
        f"[{i + 1}] bibcode={w.bibcode or 'n/a'} year={w.year or 'n/a'} title={w.title}\nabstract={w.abstract[:2200]}"
        for i, w in enumerate(work_list)
    )
    prompt = f"""
You adjudicate whether astronomy prior work covers a proposed research idea.

Return only JSON:
{{
  "paper_verdicts": [
    {{"bibcode": "...", "verdict": "covered|partial|unrelated", "one_line_reason": "..."}}
  ],
  "aggregate": "covered|partial|screened_pass",
  "closest_prior_work": [
    {{"bibcode": "...", "verdict": "covered|partial", "one_line_reason": "..."}}
  ]
}}

Use "covered" only if a paper already studies the same survey/instrument combination or an equivalent data set, the same measured relationship, and the same phenomenon. Use "partial" for close precursors that cover only part of the idea. Use "unrelated" for topical overlap without coverage.

Idea:
Question: {getattr(idea, "question", "")}
Survey combo: {getattr(idea, "survey_combo", "")}
Why now: {getattr(idea, "why_now", "")}
Approach: {getattr(idea, "approach", "")}

ADS abstracts:
{abstracts}
""".strip()
    client = anthropic.Anthropic(api_key=api_key)
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=3000,
        temperature=0,
        messages=[{"role": "user", "content": prompt}],
    )
    body = "".join(block.text for block in msg.content if getattr(block, "type", "") == "text")
    return _extract_json(body)


def aggregate_status(adjudication: dict[str, Any]) -> tuple[str, list[dict[str, Any]]]:
    verdicts = adjudication.get("paper_verdicts") or []
    closest = adjudication.get("closest_prior_work") or []
    normalized = [str(v.get("verdict", "")).lower() for v in verdicts if isinstance(v, dict)]
    if "covered" in normalized:
        return "covered", [c for c in closest if c.get("verdict") in {"covered", "partial"}]
    if "partial" in normalized:
        return "partial", [c for c in closest if c.get("verdict") in {"partial", "covered"}]
    return "screened_pass", []


def screen_idea(idea: Any, db: Session, *, sleep_after_call: bool = True) -> ScreenResult:
    entity_result = validate_entities(idea, db)
    if not entity_result.ok:
        return ScreenResult(
            idea_id=idea.id,
            coverage_status="failed_entity",
            offending_terms=entity_result.offending_terms,
        )

    works, queries = retrieve_ads_works(idea, rows=20)
    if len(works) < 5:
        return ScreenResult(
            idea_id=idea.id,
            coverage_status="inconclusive",
            papers_checked=len(works),
            retrieval_queries=queries,
        )

    adjudication = adjudicate_coverage(idea, works)
    if sleep_after_call:
        time.sleep(0.3)
    status, closest = aggregate_status(adjudication)
    return ScreenResult(
        idea_id=idea.id,
        coverage_status=status,
        closest_prior_work=closest,
        papers_checked=len(works),
        retrieval_queries=queries,
        raw_adjudication=adjudication,
    )


def persist_screen_result(db: Session, result: ScreenResult) -> None:
    notes = {
        "papers_checked": result.papers_checked,
        "offending_terms": result.offending_terms,
        "retrieval_queries": result.retrieval_queries,
        "raw_adjudication": result.raw_adjudication,
    }
    db.execute(
        text(
            """
            UPDATE research_ideas
            SET coverage_status = :status,
                closest_prior_work = CAST(:closest AS jsonb),
                coverage_checked_at = :checked_at,
                factual_verified = :verified,
                factual_verified_at = CASE WHEN :verified THEN :checked_at ELSE factual_verified_at END,
                factual_verification_notes = COALESCE(factual_verification_notes, '{}'::jsonb) || CAST(:notes AS jsonb),
                updated_at = NOW()
            WHERE id = :idea_id
            """
        ),
        {
            "idea_id": result.idea_id,
            "status": result.coverage_status,
            "closest": json.dumps(result.closest_prior_work),
            "checked_at": datetime.now(timezone.utc),
            "verified": result.factual_verified,
            "notes": json.dumps(notes),
        },
    )


def calibration_candidates(db: Session) -> list[Any]:
    fixture_rows = db.execute(
        text(
            """
            SELECT *
            FROM research_ideas
            WHERE model_chain = :model_chain
              AND (status = 'covered' OR coverage_status = 'covered')
            ORDER BY id
            LIMIT 7
            """
        ),
        {"model_chain": CALIBRATION_FIXTURE_MODEL_CHAIN},
    ).fetchall()
    if len(fixture_rows) >= 7:
        return fixture_rows

    return db.execute(
        text(
            """
            SELECT *
            FROM research_ideas
            WHERE status = 'covered' OR coverage_status = 'covered'
            ORDER BY id
            LIMIT 7
            """
        )
    ).fetchall()


def run_calibration(db: Session) -> dict[str, Any]:
    rows = calibration_candidates(db)
    results: list[ScreenResult] = []
    for row in rows:
        result = screen_idea(row, db)
        results.append(result)
        log.info("calibration idea %s => %s", row.id, result.coverage_status)
    rediscovered = sum(1 for result in results if result.coverage_status == "covered")
    passed = len(results) >= 7 and rediscovered >= 6
    payload = {
        "passed": passed,
        "rediscovered": rediscovered,
        "total": len(results),
        "results": [{"idea_id": r.idea_id, "coverage_status": r.coverage_status} for r in results],
    }
    log.info("novelty screen calibration: %s", payload)
    return payload


def unscreened_query(
    limit: int,
    offset: int = 0,
    *,
    include_all_statuses: bool = False,
) -> tuple[str, dict[str, int]]:
    status_filter = "" if include_all_statuses else "AND status NOT IN ('rejected', 'superseded', 'stale', 'covered')"
    return (
        f"""
        SELECT *
        FROM research_ideas
        WHERE coverage_status IS NULL
          {status_filter}
        ORDER BY id
        LIMIT :limit OFFSET :offset
        """,
        {"limit": limit, "offset": offset},
    )
