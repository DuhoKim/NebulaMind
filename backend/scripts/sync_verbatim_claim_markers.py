#!/usr/bin/env python3
"""Additive verbatim claim-marker sync for a single wiki page.

For each claim whose `claim.text` appears verbatim (or as a unique prefix) in
the page content but is NOT yet wrapped by a marker, insert
`<!--claim:N--> ... <!--/claim:N-->` around the matched span.

Design:
- Additive only. Never strips existing markers; never touches their spans.
- Reuses `app.agent_loop.marker_embed.injector._compute_forbidden_ranges` to
  avoid inserting into headings, code blocks, links, math, list bullets, or
  pre-existing markers.
- Match strategy per claim: try the full claim text first, then progressively
  shorter prefixes (250, 200, 160, 120, 80, 60, --min-chars). The first
  prefix that occurs exactly once in unforbidden territory wins.
- Per-page run logged to `claim_marker_runs` with status='committed_verbatim_sync'.
- No new claims, no trust_level updates, no writer pipeline.

CLI:
  python3 scripts/sync_verbatim_claim_markers.py --page-id 57            # dry run
  python3 scripts/sync_verbatim_claim_markers.py --page-id 57 --commit   # write
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
BACKEND = HERE.parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from sqlalchemy import text  # noqa: E402

from app.database import SessionLocal  # noqa: E402
from app.agent_loop.marker_embed.injector import (  # noqa: E402
    _compute_forbidden_ranges,
    _in_forbidden,
)

_PREFIX_TRIES = (250, 200, 160, 120, 80, 60)
_MARKER_OPEN_RE = re.compile(r"<!--claim:([\d,\s]+)-->")
_MARKER_PAIR_RE = re.compile(r"<!--claim:([\d,\s]+)-->.*?<!--/claim:\1-->", re.DOTALL)


def _expand_claim_groups(groups: list[str]) -> list[int]:
    ids: list[int] = []
    for group in groups:
        for token in group.split(","):
            token = token.strip()
            if token:
                ids.append(int(token))
    return ids


def _norm_for_match(value: str) -> str:
    """Collapse runs of whitespace so DB text with line breaks still matches
    content rendered as a single paragraph."""
    return re.sub(r"\s+", " ", value).strip()


def _find_unique_span(
    claim_text: str,
    content: str,
    forbidden: list[tuple[int, int]],
    min_chars: int,
) -> tuple[int, int] | None:
    """Return (start, end) of the longest unique non-forbidden verbatim
    occurrence of claim_text's prefix in content, or None."""
    raw = (claim_text or "").strip()
    if len(raw) < min_chars:
        return None

    # First: try the raw text (handles content stored verbatim with same line breaks).
    candidates: list[str] = []
    if len(raw) >= min_chars:
        candidates.append(raw)
    for n in _PREFIX_TRIES:
        if min_chars <= n < len(raw):
            candidates.append(raw[:n].strip())
    if min_chars not in _PREFIX_TRIES and min_chars <= len(raw):
        candidates.append(raw[:min_chars].strip())

    # Try each candidate, prefer longer.
    candidates = [c for c in candidates if len(c) >= min_chars]
    seen: set[str] = set()
    for cand in candidates:
        if cand in seen:
            continue
        seen.add(cand)
        positions = [m.start() for m in re.finditer(re.escape(cand), content)]
        if len(positions) != 1:
            continue
        start = positions[0]
        end = start + len(cand)
        if _in_forbidden(start, end, forbidden):
            continue
        return (start, end)
    return None


def _existing_marker_ranges(content: str) -> list[tuple[int, int]]:
    """Return (start, end) of every full marker-wrapped span so new markers
    cannot land inside them."""
    return [(m.start(), m.end()) for m in _MARKER_PAIR_RE.finditer(content)]


def sync_page(page_id: int, *, commit: bool, min_chars: int) -> dict:
    started = datetime.datetime.utcnow()
    db = SessionLocal()
    try:
        page_row = db.execute(
            text("SELECT id, slug, content FROM wiki_pages WHERE id=:pid"),
            {"pid": page_id},
        ).fetchone()
        if not page_row:
            return {"error": "page_not_found", "page_id": page_id}
        slug = page_row[1]
        content = page_row[2] or ""

        source_version_row = db.execute(
            text(
                "SELECT MAX(version_num) FROM page_versions WHERE page_id=:pid"
            ),
            {"pid": page_id},
        ).fetchone()
        source_version = source_version_row[0] if source_version_row else None

        already_markered = set(_expand_claim_groups(_MARKER_OPEN_RE.findall(content)))

        claim_rows = db.execute(
            text(
                "SELECT id, text, trust_level, section, order_idx "
                "FROM claims WHERE page_id=:pid ORDER BY id"
            ),
            {"pid": page_id},
        ).fetchall()

        # Build forbidden zones: injector's standard set + existing markered spans.
        forbidden = list(_compute_forbidden_ranges(content))
        forbidden.extend(_existing_marker_ranges(content))

        rejected = {
            "already_markered_skipped": 0,
            "no_unique_span": 0,
            "overlaps_new_placement": 0,
        }
        placements: list[tuple[int, int, int]] = []  # (start, end, claim_id)
        occupied: list[tuple[int, int]] = []

        for cid, ctxt, _trust, _section, _order in claim_rows:
            if cid in already_markered:
                rejected["already_markered_skipped"] += 1
                continue
            best = _find_unique_span(ctxt, content, forbidden, min_chars)
            if best is None:
                rejected["no_unique_span"] += 1
                continue
            s, e = best
            if any(s < pe and e > ps for ps, pe in occupied):
                rejected["overlaps_new_placement"] += 1
                continue
            placements.append((s, e, cid))
            occupied.append((s, e))

        # Apply in reverse offset order so earlier offsets stay valid.
        result = content
        for s, e, cid in sorted(placements, key=lambda x: x[0], reverse=True):
            open_tag = f"<!--claim:{cid}-->"
            close_tag = f"<!--/claim:{cid}-->"
            result = result[:s] + open_tag + result[s:e] + close_tag + result[e:]

        opens = _expand_claim_groups(_MARKER_OPEN_RE.findall(result))
        pairs = _expand_claim_groups(_MARKER_PAIR_RE.findall(result))

        stats = {
            "page_id": page_id,
            "slug": slug,
            "source_version": source_version,
            "total_claims": len(claim_rows),
            "claims_already_markered": len(already_markered),
            "new_markers_added": len(placements),
            "result_marker_opens": len(opens),
            "result_marker_pairs": len(pairs),
            "delta_chars": len(result) - len(content),
            "rejected": rejected,
            "commit": commit,
        }

        if not commit:
            stats["dry_run"] = True
            return stats

        if not placements:
            stats["wrote"] = False
            stats["reason"] = "no_new_markers_to_add"
            return stats

        if len(opens) != len(pairs):
            raise RuntimeError(
                f"validation_failed_unpaired: opens={len(opens)} pairs={len(pairs)}"
            )
        if len(opens) != len(already_markered) + len(placements):
            raise RuntimeError(
                "validation_failed_count: "
                f"opens={len(opens)} expected={len(already_markered)+len(placements)}"
            )

        finished = datetime.datetime.utcnow()
        version_row = db.execute(
            text(
                "INSERT INTO page_versions (page_id, version_num, content, created_at) "
                "VALUES (:pid, COALESCE((SELECT MAX(version_num) FROM page_versions WHERE page_id=:pid), 0)+1, :content, NOW()) "
                "RETURNING version_num"
            ),
            {"pid": page_id, "content": result},
        ).fetchone()
        new_version = version_row[0] if version_row else None
        db.execute(
            text("UPDATE wiki_pages SET content = :c WHERE id = :pid"),
            {"c": result, "pid": page_id},
        )
        db.execute(
            text(
                "INSERT INTO claim_marker_runs ("
                "  page_id, page_version, source_version, total_claims, matched_claims, "
                "  rejected_low_confidence, rejected_no_section, rejected_ambiguous_span, "
                "  rejected_validation, mean_confidence, judge_agreement_pct, coverage_pct, "
                "  status, run_started_at, run_finished_at, notes"
                ") VALUES ("
                "  :pid, :pv, :sv, :total, :matched, 0, 0, :rej_amb, 0, 0.0, 0.0, :cov, "
                "  :status, :started, :finished, :notes"
                ")"
            ),
            {
                "pid": page_id,
                "pv": new_version,
                "sv": source_version,
                "total": len(claim_rows),
                "matched": len(placements),
                "rej_amb": rejected["overlaps_new_placement"],
                "cov": (len(opens) / len(claim_rows)) if claim_rows else 0.0,
                "status": "committed_verbatim_sync",
                "started": started,
                "finished": finished,
                "notes": json.dumps(
                    {
                        "rejected": rejected,
                        "min_chars": min_chars,
                        "delta_chars": stats["delta_chars"],
                        "already_markered": len(already_markered),
                    }
                ),
            },
        )
        db.commit()
        stats["wrote"] = True
        stats["new_version"] = new_version
        return stats
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    p.add_argument("--page-id", type=int, required=True)
    p.add_argument(
        "--commit",
        action="store_true",
        help="Write the updated content + version + run row. Default is dry-run.",
    )
    p.add_argument(
        "--min-chars",
        type=int,
        default=40,
        help="Minimum prefix length to attempt matching (default 40).",
    )
    args = p.parse_args(argv)
    result = sync_page(args.page_id, commit=args.commit, min_chars=args.min_chars)
    print(json.dumps(result, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
