#!/usr/bin/env python3
"""Align inline author-year citations to evidence rows and dynamic cite markers."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable

from sqlalchemy import text

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/backend")

from app.database import SessionLocal
from app.models import agent as _agent_models  # noqa: F401 - load FK targets
from app.models.claim import Evidence
from app.models.page import PageVersion, WikiPage


OUTER_PAREN_RE = re.compile(r"\(([^()\n]{2,300})\)")
SINGLE_AUTHORYEAR_RE = re.compile(
    r"(?:(?:e\.g\.|i\.e\.|cf\.|see)\s*,?\s*)?"          # optional discourse marker
    r"(?P<authors>[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’.\-]+"
    r"(?:\s+et\s+al\.?"
    r"|\s*&\s*[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’.\-]+"
    r"|\s+and\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’.\-]+)?)"
    r"\s*,?\s+(?P<year>(?:19|20)\d{2})[a-z]?",
    re.UNICODE,
)
CITE_MARKER_RE = re.compile(r"<!--cite:([0-9,\s]+)-->")
CLAIM_MARKER_RE = re.compile(r"<!--\s*(/?)claim:([0-9,\s]+)\s*-->")


@dataclass(frozen=True)
class CitationMatch:
    start: int
    end: int
    raw: str
    author_year_key: str
    first_author: str
    year: int


@dataclass
class ResolvedCitation:
    match: CitationMatch
    evidence_id: int | None
    method: str
    confidence: float


def _clean_author(author: str) -> str:
    author = re.sub(r"\bet\s+al\.?\s*\.?", "et al.", author, flags=re.I)
    author = re.sub(r"\s+", " ", author.replace("’", "'")).strip(" ,.")
    return author


def _first_author_last(author_key: str) -> str:
    first = re.split(r"\s*(?:,|;|&|\band\b)\s*", author_key, maxsplit=1, flags=re.I)[0]
    first = re.sub(r"\bet\s+al\.?\b|\bCollaboration\b", "", first, flags=re.I).strip(" ,.")
    return first.split()[-1] if first.split() else first


def _canonical_key(author_text: str, year: str) -> tuple[str, str, int]:
    authors = _clean_author(author_text)
    yr = int(year[:4])
    return f"{authors} {yr}", _first_author_last(authors), yr


def tokenize_paren_citations(content: str) -> list[CitationMatch]:
    """Return one CitationMatch per atomic author-year, even if the source
    parenthetical contained multiple semicolon-separated citations."""
    matches: list[CitationMatch] = []
    for outer in OUTER_PAREN_RE.finditer(content):
        body = outer.group(1)
        # Drop obvious non-citation parens early: must contain a 4-digit year
        if not re.search(r"\b(?:19|20)\d{2}", body):
            continue
        # Split on ';' (unambiguous multi-cite separator)
        parts = [p.strip() for p in body.split(";")]
        # Also split on ',' if and only if multiple year-tokens appear and no '&'
        if len(parts) == 1 and len(re.findall(r"\b(?:19|20)\d{2}", body)) >= 2 and "&" not in body:
            parts = [p.strip() for p in body.split(",")]
        # Compute offsets into the original document for replacement
        first_atom = True
        for part in parts:
            for m in SINGLE_AUTHORYEAR_RE.finditer(part):
                key, first, yr = _canonical_key(m.group("authors"), m.group("year"))
                # Anchor the replacement on the FULL outer paren on first encounter,
                # and emit zero-width markers for subsequent atoms (so the closing
                # `)` is collapsed exactly once).
                if first_atom:
                    matches.append(CitationMatch(
                        start=outer.start(),
                        end=outer.end(),
                        raw=outer.group(0),
                        author_year_key=key,
                        first_author=first,
                        year=yr,
                    ))
                    first_atom = False
                else:
                    matches.append(CitationMatch(
                        start=outer.end(),
                        end=outer.end(),
                        raw="",
                        author_year_key=key,
                        first_author=first,
                        year=yr,
                    ))
    return sorted(matches, key=lambda c: c.start)


def extract_citations(content: str) -> list[CitationMatch]:
    return tokenize_paren_citations(content)


def _similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def _author_blob(authors: str | None) -> str:
    if not authors:
        return ""
    try:
        parsed = json.loads(authors)
        if isinstance(parsed, list):
            return " ".join(str(a) for a in parsed)
    except Exception:
        pass
    return authors


def _evidence_author_year_key(ev: Evidence) -> str:
    authors = _author_blob(ev.authors)
    if authors:
        first = re.split(r"\s*,\s*|\s+;\s*", authors, maxsplit=1)[0].strip(" []\"'")
        last = first.split()[-1] if first.split() else first
        author = f"{last} et al." if "," in authors or "[" in authors else first
    else:
        author = (ev.title or f"Evidence {ev.id}")[:80]
    return f"{author} {ev.year}" if ev.year else author[:120]


def find_evidence(db, citation: CitationMatch) -> tuple[int | None, str, float]:
    candidates = (
        db.query(Evidence)
        .filter(Evidence.year == citation.year, Evidence.authors.ilike(f"%{citation.first_author}%"))
        .order_by(Evidence.quality.desc().nullslast(), Evidence.id.desc())
        .limit(20)
        .all()
    )
    if len(candidates) == 1:
        return candidates[0].id, "exact_key", 1.0

    scored: list[tuple[float, Evidence]] = []
    for ev in candidates:
        blob = _author_blob(ev.authors)
        score = max(_similarity(citation.first_author, token) for token in re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ'’-]+", blob) or [""])
        if score >= 0.80:
            scored.append((score, ev))
    if scored:
        scored.sort(key=lambda pair: (pair[0], pair[1].quality or 0, pair[1].id), reverse=True)
        method = "exact_key" if scored[0][0] >= 0.90 else "fuzzy_author_year"
        return scored[0][1].id, method, scored[0][0]
    return None, "unmatched", 0.0


def upsert_link(db, page_id: int, evidence_id: int, author_year_key: str, method: str, confidence: float) -> None:
    db.execute(
        text(
            """
            INSERT INTO page_citation_links
                (page_id, evidence_id, author_year_key, match_method, match_confidence, updated_at)
            VALUES
                (:page_id, :evidence_id, :author_year_key, :match_method, :match_confidence, now())
            ON CONFLICT (page_id, author_year_key)
            DO UPDATE SET
                evidence_id = EXCLUDED.evidence_id,
                match_method = EXCLUDED.match_method,
                match_confidence = EXCLUDED.match_confidence,
                updated_at = now()
            """
        ),
        {
            "page_id": page_id,
            "evidence_id": evidence_id,
            "author_year_key": author_year_key[:120],
            "match_method": method,
            "match_confidence": confidence,
        },
    )


def bootstrap_page_links(db, page_id: int | None = None) -> int:
    sql = """
        INSERT INTO page_citation_links
            (page_id, evidence_id, author_year_key, match_method, match_confidence, updated_at)
        SELECT
            c.page_id,
            e.id,
            LEFT(
                COALESCE(
                    NULLIF(regexp_replace(e.authors, '^\\[?\"?([^\",\\]]+).*$', '\\1'), ''),
                    NULLIF(e.title, ''),
                    'Evidence ' || e.id::text
                ) || COALESCE(' ' || e.year::text, ''),
                120
            ) AS author_year_key,
            'claim_evidence_bootstrap',
            0.75,
            now()
        FROM evidence e
        JOIN claims c ON c.id = e.claim_id
        WHERE (:page_id IS NULL OR c.page_id = :page_id)
        ON CONFLICT (page_id, author_year_key) DO NOTHING
    """
    result = db.execute(text(sql), {"page_id": page_id})
    return result.rowcount or 0


def replace_citations(content: str, resolved: Iterable[ResolvedCitation]) -> str:
    def marker_for(item: ResolvedCitation) -> str:
        if item.evidence_id:
            return f"<!--cite:{item.evidence_id}-->"
        return f"<!--cite-unmatched:{item.match.author_year_key}-->"

    items = sorted(resolved, key=lambda r: (r.match.start, r.match.end))
    new_content_parts: list[str] = []
    cursor = 0
    i = 0
    while i < len(items):
        item = items[i]
        if item.match.start < cursor:
            i += 1
            continue

        grouped = [item]
        j = i + 1
        if item.match.raw.startswith("(") and item.match.end > item.match.start:
            while (
                j < len(items)
                and items[j].match.start == item.match.end
                and items[j].match.end == item.match.end
                and items[j].match.raw == ""
            ):
                grouped.append(items[j])
                j += 1

        new_content_parts.append(content[cursor:item.match.start])
        new_content_parts.append("".join(marker_for(grouped_item) for grouped_item in grouped))
        cursor = item.match.end
        i = j

    new_content_parts.append(content[cursor:])
    new_content = "".join(new_content_parts)
    new_content = re.sub(r"\s+([.,;:])", r"\1", new_content)
    return new_content


def insert_claim_citation_markers(db, page_id: int, content: str) -> str:
    rows = db.execute(
        text(
            """
            SELECT DISTINCT ON (e.claim_id)
                e.claim_id,
                pcl.evidence_id
            FROM page_citation_links pcl
            JOIN evidence e ON e.id = pcl.evidence_id
            WHERE pcl.page_id = :pid
              AND e.claim_id IS NOT NULL
            ORDER BY e.claim_id, COALESCE(e.quality, 0.0) DESC, pcl.id
            """
        ),
        {"pid": page_id},
    ).fetchall()
    evidence_by_claim = {int(row.claim_id): int(row.evidence_id) for row in rows}
    if not evidence_by_claim:
        return content

    def repl(match: re.Match) -> str:
        ids = [int(part) for part in re.findall(r"\d+", match.group(1))]
        cite_ids = []
        for claim_id in ids:
            evidence_id = evidence_by_claim.get(claim_id)
            if evidence_id and evidence_id not in cite_ids:
                cite_ids.append(evidence_id)
        if not cite_ids:
            return match.group(0)
        lookahead = content[match.end(): match.end() + 40]
        if lookahead.lstrip().startswith("<!--cite:"):
            return match.group(0)
        return f"{match.group(0)}<!--cite:{','.join(str(x) for x in cite_ids)}-->"

    return re.sub(r"<!--\s*/claim:([0-9,\s]+)\s*-->", repl, content)


def strip_hallucinated_cites(db, page_id: int, content: str) -> tuple[str, list[int]]:
    ids = {int(x) for group in CITE_MARKER_RE.findall(content) for x in re.findall(r"\d+", group)}
    if not ids:
        return content, []
    known = {
        row[0]
        for row in db.execute(
            text("SELECT evidence_id FROM page_citation_links WHERE page_id = :pid AND evidence_id = ANY(:ids)"),
            {"pid": page_id, "ids": list(ids)},
        ).fetchall()
    }
    unknown = sorted(ids - known)
    if not unknown:
        return content, []

    def repl(match: re.Match) -> str:
        kept = [part for part in re.findall(r"\d+", match.group(1)) if int(part) in known]
        return f"<!--cite:{','.join(kept)}-->" if kept else ""

    return CITE_MARKER_RE.sub(repl, content), unknown


def align_page(db, page: WikiPage, dry_run: bool = False, bootstrap: bool = False) -> dict:
    if bootstrap:
        bootstrap_page_links(db, page.id)

    from app.services.content_canonicalizer import canonicalize

    content = page.content or ""
    # Run canonicalizer first
    canon_res = canonicalize(content)
    content = canon_res.new_content
    if not dry_run and page.content != content:
        page.content = content
        db.commit()

    matches = extract_citations(content)
    resolved: list[ResolvedCitation] = []
    unmatched: list[str] = []
    for match in matches:
        evidence_id, method, confidence = find_evidence(db, match)
        resolved.append(ResolvedCitation(match, evidence_id, method, confidence))
        if evidence_id:
            upsert_link(db, page.id, evidence_id, match.author_year_key, method, confidence)
        else:
            unmatched.append(match.author_year_key)

    matched = sum(1 for item in resolved if item.evidence_id)
    total = len(matches)
    match_rate = (matched / total) if total else 1.0
    quality_gate = "pass"
    if total and match_rate < 0.05:
        quality_gate = "skip_low_match_rate"
        new_content = content
        unknown_cite_ids = []
    else:
        new_content = replace_citations(content, resolved)
        new_content, unknown_cite_ids = strip_hallucinated_cites(db, page.id, new_content)
    new_content = insert_claim_citation_markers(db, page.id, new_content)
    new_content, unknown_cite_ids_after_claims = strip_hallucinated_cites(db, page.id, new_content)
    unknown_cite_ids = sorted(set(unknown_cite_ids + unknown_cite_ids_after_claims))
    changed = new_content != content

    if changed and not dry_run:
        last_version = (
            db.query(PageVersion)
            .filter(PageVersion.page_id == page.id)
            .order_by(PageVersion.version_num.desc())
            .first()
        )
        next_num = (last_version.version_num + 1) if last_version else 1
        db.add(PageVersion(page_id=page.id, version_num=next_num, content=new_content))
        page.content = new_content

    return {
        "page_id": page.id,
        "slug": page.slug,
        "total_parentheticals": total,
        "matched": matched,
        "unmatched": total - matched,
        "sample_unmatched": unmatched[:10],
        "changed": changed,
        "match_rate": round(match_rate, 3),
        "quality_gate": quality_gate,
        "unknown_cite_ids": unknown_cite_ids,
    }


def selected_pages(db, page_id: int | None, all_pages: bool) -> list[WikiPage]:
    q = db.query(WikiPage)
    if page_id is not None:
        q = q.filter(WikiPage.id == page_id)
    elif not all_pages:
        raise SystemExit("Use --page-id or --all-pages")
    return q.order_by(WikiPage.id).all()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--page-id", type=int)
    parser.add_argument("--all-pages", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report")
    parser.add_argument("--bootstrap", action="store_true")
    args = parser.parse_args()

    with SessionLocal() as db:
        reports = []
        if args.bootstrap:
            inserted = bootstrap_page_links(db, args.page_id)
            print(f"bootstrap_inserted={inserted}")
        for page in selected_pages(db, args.page_id, args.all_pages):
            report = align_page(db, page, dry_run=args.dry_run, bootstrap=False)
            reports.append(report)
            print(json.dumps(report, ensure_ascii=False))
        if args.dry_run:
            db.rollback()
        else:
            db.commit()
        if args.report:
            Path(args.report).write_text(json.dumps(reports, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
