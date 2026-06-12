#!/usr/bin/env python3
"""
Move inline author-year citations on the galaxy-evolution page into evidence rows.

The page uses claim markers such as ``<!--claim:1627-->`` and
``<!--/claim:1627-->``. Citations immediately after a closing marker are mapped
to that preceding claim; citations inside an open marker are mapped to the
active claim.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/backend")

from app.database import SessionLocal
from app.models import agent as _agent_models  # noqa: F401 - load FK targets
from app.models import jury as _jury_models  # noqa: F401 - load FK targets
from app.models.claim import Claim, Evidence
from app.models.page import WikiPage


PAGE_ID = 57
PAGE_SLUG = "galaxy-evolution"
SOURCE_CHANNEL = "inline-citation-cleanup"

MARKER_RE = re.compile(r"<!--\s*(/?)claim:([0-9,\s]+)\s*-->")
CITATION_RE = re.compile(r"\(([^()\n]{0,180}?\b(?:19|20)\d{2}[a-z]?\b[^()\n]{0,80})\)")
YEAR_RE = re.compile(r"\b((?:19|20)\d{2})[a-z]?\b")
AUTHOR_YEAR_RE = re.compile(r"^\s*(?P<authors>.+?)\s+(?P<year>(?:19|20)\d{2})[a-z]?\s*$")

NON_CITATION_HINTS = (
    "z ",
    "z~",
    "km",
    "m☉",
    "m_",
    "t_",
    "p(",
    "δ",
    "sigma",
    "\\",
    "=",
)


@dataclass(frozen=True)
class CitationHit:
    start: int
    end: int
    raw: str
    claim_ids: tuple[int, ...]


def parse_claim_ids(raw: str) -> tuple[int, ...]:
    ids: list[int] = []
    for part in raw.split(","):
        part = part.strip()
        if part.isdigit():
            ids.append(int(part))
    return tuple(ids)


def citation_like(raw: str) -> bool:
    text = raw.strip()
    lower = text.lower()
    if not YEAR_RE.search(text):
        return False
    if ";" in text:
        return True
    if " et al." in lower or "collaboration" in lower:
        return True
    if "&" in text:
        return True
    if re.match(r"^[A-Z][A-Za-zÀ-ÖØ-öø-ÿ' -]+,?\s+(?:19|20)\d{2}[a-z]?$", text):
        return True
    if re.match(r"^[A-Z][A-Za-zÀ-ÖØ-öø-ÿ' -]+(?:\s+and\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ' -]+)?\s+(?:19|20)\d{2}[a-z]?$", text):
        return True
    return False


def contextual_author_year(content: str, start: int, raw: str) -> str | None:
    if not re.fullmatch(r"(?:19|20)\d{2}[a-z]?", raw.strip()):
        return None
    prefix = content[max(0, start - 90):start]
    prefix = re.sub(r"<!--[^>]+-->", " ", prefix)
    prefix = re.sub(r"\s+", " ", prefix).strip()
    match = re.search(
        r"((?:[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'.-]+|[A-Z]{2,})(?:\s+(?:&|and)\s+(?:[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'.-]+|[A-Z]{2,})|\s+et\s+al\.|\s+Collaboration|\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'.-]+){0,4})\s*$",
        prefix,
    )
    if not match:
        return None
    authors = re.sub(r"^(?:The|the)\s+", "", match.group(1).strip())
    if len(authors) < 3:
        return None
    return f"{authors} {raw.strip()}"


def split_references(raw: str) -> list[str]:
    refs: list[str] = []
    for part in raw.split(";"):
        ref = part.strip().strip(",")
        if ref and citation_like(ref):
            refs.append(ref)
    return refs


def normalize_ref(ref: str) -> str:
    return re.sub(r"\s+", " ", ref.strip()).lower()


def parse_ref(ref: str) -> tuple[str, int | None]:
    match = AUTHOR_YEAR_RE.match(ref.strip())
    if not match:
        year_match = YEAR_RE.search(ref)
        return ref.strip(), int(year_match.group(1)) if year_match else None
    return match.group("authors").strip(" ,"), int(match.group("year"))


def author_tokens(authors: str) -> set[str]:
    cleaned = re.sub(r"\bet\s+al\.?\b|\bcollaboration\b", " ", authors, flags=re.I)
    cleaned = cleaned.replace("&", " ").replace(" and ", " ")
    tokens = {
        token.lower()
        for token in re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ][A-Za-zÀ-ÖØ-öø-ÿ'-]+", cleaned)
        if len(token) > 2
    }
    return tokens


def evidence_text(ev: Evidence) -> str:
    return " ".join(
        part
        for part in [
            ev.title or "",
            ev.authors or "",
            ev.summary or "",
            ev.abstract or "",
        ]
        if part
    ).lower()


def same_reference(ev: Evidence, ref: str, authors: str, year: int | None) -> bool:
    if ev.source_channel == SOURCE_CHANNEL and normalize_ref(ev.title or "") == normalize_ref(ref):
        return True
    if year and ev.year and ev.year != year:
        return False
    tokens = author_tokens(authors)
    if not tokens:
        return False
    text = evidence_text(ev)
    return any(token in text for token in tokens)


def find_matching_evidence(db, claim_id: int, ref: str, authors: str, year: int | None) -> Evidence | None:
    claim_rows = db.query(Evidence).filter(Evidence.claim_id == claim_id).all()
    for ev in claim_rows:
        if same_reference(ev, ref, authors, year):
            return ev

    query = db.query(Evidence)
    if year:
        query = query.filter(Evidence.year == year)
    candidates = query.limit(1000).all()
    for ev in candidates:
        if same_reference(ev, ref, authors, year):
            return ev
    return None


def clone_or_create_evidence(db, claim_id: int, ref: str) -> tuple[Evidence, bool]:
    authors, year = parse_ref(ref)
    existing = find_matching_evidence(db, claim_id, ref, authors, year)
    if existing and existing.claim_id == claim_id:
        return existing, False

    if existing:
        ev = Evidence(
            claim_id=claim_id,
            arxiv_id=existing.arxiv_id,
            doi=existing.doi,
            url=existing.url,
            title=existing.title,
            authors=existing.authors or authors,
            year=existing.year or year,
            summary=existing.summary,
            abstract=existing.abstract,
            ads_bibcode=existing.ads_bibcode,
            s2_paper_id=existing.s2_paper_id,
            verified_at=existing.verified_at,
            stance="supports",
            quality=existing.quality or 0.45,
            source_channel=SOURCE_CHANNEL,
            arxiv_verified=existing.arxiv_verified,
            journal_ref=existing.journal_ref,
            peer_reviewed=existing.peer_reviewed,
            relevance=existing.relevance,
            entailment=existing.entailment,
            rigor=existing.rigor,
            confidence=existing.confidence,
        )
    else:
        ev = Evidence(
            claim_id=claim_id,
            title=ref,
            authors=authors,
            year=year,
            summary=f"Migrated from inline citation on {PAGE_SLUG}: {ref}.",
            stance="supports",
            quality=0.40,
            source_channel=SOURCE_CHANNEL,
        )
    db.add(ev)
    db.flush()
    return ev, True


def find_citations(content: str) -> list[CitationHit]:
    marker_iter = iter(sorted(MARKER_RE.finditer(content), key=lambda m: m.start()))
    next_marker = next(marker_iter, None)
    active: list[int] = []
    last_closed: tuple[int, ...] = ()
    hits: list[CitationHit] = []

    for match in CITATION_RE.finditer(content):
        while next_marker and next_marker.start() < match.start():
            closing = bool(next_marker.group(1))
            ids = parse_claim_ids(next_marker.group(2))
            if closing:
                active = [claim_id for claim_id in active if claim_id not in ids]
                last_closed = ids
            else:
                active.extend(ids)
            next_marker = next(marker_iter, None)

        raw = match.group(1).strip()
        if citation_like(raw):
            ref_text = raw
        else:
            ref_text = contextual_author_year(content, match.start(), raw)
            if not ref_text:
                continue
        if any(hint in raw.lower() for hint in NON_CITATION_HINTS) and not (" et al." in raw.lower() or "&" in raw):
            continue
        claim_ids = tuple(active) or last_closed
        if not claim_ids:
            continue
        hits.append(CitationHit(match.start(), match.end(), ref_text, claim_ids))
    return hits


def strip_citations(content: str, hits: list[CitationHit]) -> str:
    remove_ranges = [(hit.start, hit.end) for hit in hits]
    cleaned_parts: list[str] = []
    cursor = 0
    for start, end in remove_ranges:
        cleaned_parts.append(content[cursor:start])
        cursor = end
    cleaned_parts.append(content[cursor:])
    cleaned = "".join(cleaned_parts)
    cleaned = re.sub(r"[ \t]+([.,;:])", r"\1", cleaned)
    cleaned = re.sub(r" {2,}", " ", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Report actions without writing.")
    args = parser.parse_args()

    db = SessionLocal()
    try:
        page = db.query(WikiPage).filter(WikiPage.id == PAGE_ID, WikiPage.slug == PAGE_SLUG).one()
        content = page.content or ""
        hits = find_citations(content)

        refs_seen: set[tuple[int, str]] = set()
        linked = 0
        created = 0
        skipped = 0
        missing_claims = 0

        for hit in hits:
            for ref in split_references(hit.raw):
                for claim_id in hit.claim_ids:
                    key = (claim_id, normalize_ref(ref))
                    if key in refs_seen:
                        skipped += 1
                        continue
                    refs_seen.add(key)
                    if not db.query(Claim.id).filter(Claim.id == claim_id, Claim.page_id == PAGE_ID).first():
                        missing_claims += 1
                        continue
                    _ev, was_created = clone_or_create_evidence(db, claim_id, ref)
                    linked += 1
                    if was_created:
                        created += 1

        cleaned = strip_citations(content, hits)
        remaining = find_citations(cleaned)

        print(f"page_id={PAGE_ID} slug={PAGE_SLUG}")
        print(f"citations_found={len(hits)} unique_claim_reference_links={len(refs_seen)}")
        print(f"evidence_links_ensured={linked} evidence_rows_created={created} duplicates_skipped={skipped}")
        print(f"missing_claim_mappings={missing_claims}")
        print(f"content_chars_before={len(content)} content_chars_after={len(cleaned)}")
        print(f"remaining_citation_parentheticals={len(remaining)}")

        if args.dry_run:
            db.rollback()
            print("[DRY RUN] rolled back")
            return

        page.content = cleaned
        db.commit()
        print("Committed wiki_pages.content update and evidence links.")
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
