#!/usr/bin/env python3
"""Trust audit — emits per-claim quality + flag summary for a page (or all pages).

Usage:
    .venv/bin/python scripts/trust_audit.py --page-id 57 --out /tmp/audit_page57.json
    .venv/bin/python scripts/trust_audit.py --all-pages --out /tmp/audit_all.json

Designed per setup in `docs/trust_calibration_design_v1.md` §2.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Allow running from anywhere — locate backend root by walking up.
here = Path(__file__).resolve()
backend_root = next((p for p in here.parents if (p / "app" / "database.py").exists()), None)
if backend_root is None:
    sys.exit("Could not locate backend root (looking for app/database.py)")
sys.path.insert(0, str(backend_root))

from app.database import SessionLocal  # type: ignore  # noqa: E402
from sqlalchemy import text  # noqa: E402


def audit_page(s, page_id: int) -> dict:
    page = s.execute(text(
        "SELECT id, slug, title, last_renovated_at, updated_at, health_score "
        "FROM wiki_pages WHERE id = :id"
    ), {"id": page_id}).mappings().first()
    if not page:
        return {"page_id": page_id, "error": "page not found"}

    claim_rows = s.execute(text(
        "SELECT id, section, trust_level, trust_score, trust_score_updated_at, "
        "       evidence_search_attempted_at, last_adversarial_probe_at, text, "
        "       human_trust_override, human_override_locked "
        "FROM claims WHERE page_id = :id ORDER BY id"
    ), {"id": page_id}).mappings().all()
    claim_ids = [c["id"] for c in claim_rows]

    ev_per_claim: dict[int, list] = defaultdict(list)
    if claim_ids:
        ph = ",".join(str(i) for i in claim_ids)
        ev = s.execute(text(
            f"SELECT id, claim_id, stance, quality, year, arxiv_verified, peer_reviewed "
            f"FROM evidence WHERE claim_id IN ({ph})"
        )).mappings().all()
        for e in ev:
            ev_per_claim[e["claim_id"]].append(dict(e))

    # Find duplicated trust_score (4dp) — SCORE_DEGENERATE
    score_buckets: dict[str, list[int]] = defaultdict(list)
    for c in claim_rows:
        if c["trust_score"] is not None:
            key = f"{c['trust_score']:.4f}"
            score_buckets[key].append(c["id"])
    degenerate_groups = {k: v for k, v in score_buckets.items() if len(v) >= 3}

    per_claim_out = []
    flag_counter: Counter[str] = Counter()
    for c in claim_rows:
        items = ev_per_claim.get(c["id"], [])
        stance = Counter((it["stance"] or "neutral") for it in items)
        supports = stance.get("supports", 0)
        challenges = stance.get("challenges", 0)
        contradicts = stance.get("contradicts", 0)
        contests = stance.get("contests", 0)
        mismatch = stance.get("mismatch", 0)
        neutral = len(items) - supports - challenges - contradicts - contests - mismatch
        opposing = challenges + contradicts + contests
        arxiv_v = sum(1 for it in items if it["arxiv_verified"])
        pr = sum(1 for it in items if it["peer_reviewed"])
        recent = sum(1 for it in items if it["year"] and it["year"] >= 2024)
        qs = [it["quality"] for it in items if it["quality"] is not None]
        avg_q = sum(qs) / len(qs) if qs else None

        flags = []
        if len(items) < 5:
            flags.append("LOW_EVIDENCE")
        if len(items) > 0 and arxiv_v / len(items) < 0.30:
            flags.append("UNVERIFIED_DOM")
        if c["trust_level"] in ("debated", "challenged") and (supports == 0 or opposing == 0):
            flags.append("STANCE_SKEW")
        score_key = f"{c['trust_score']:.4f}" if c["trust_score"] is not None else None
        if score_key in degenerate_groups:
            flags.append("SCORE_DEGENERATE")
        if c["trust_level"] == "debated" and c["trust_score"] is not None and abs(c["trust_score"]) >= 0.50:
            flags.append("LEVEL_MISMATCH")

        for f in flags:
            flag_counter[f] += 1

        per_claim_out.append({
            "id": c["id"],
            "section": c["section"],
            "text_preview": (c["text"] or "")[:120],
            "trust_level": c["trust_level"],
            "trust_score": c["trust_score"],
            "evidence_count": len(items),
            "supports": supports,
            "challenges": challenges,
            "contradicts": contradicts,
            "contests": contests,
            "mismatch": mismatch,
            "neutral": neutral,
            "opposing_total": opposing,
            "arxiv_verified": arxiv_v,
            "peer_reviewed": pr,
            "recent_2024_plus": recent,
            "avg_quality": avg_q,
            "evidence_search_attempted_at": c["evidence_search_attempted_at"].isoformat() if c["evidence_search_attempted_at"] else None,
            "last_adversarial_probe_at": c["last_adversarial_probe_at"].isoformat() if c["last_adversarial_probe_at"] else None,
            "flags": flags,
        })

    summary = {
        "page_id": page_id,
        "slug": page["slug"],
        "title": page["title"],
        "claim_count": len(claim_rows),
        "by_trust_level": dict(Counter(c["trust_level"] for c in claim_rows)),
        "flag_counts": dict(flag_counter),
        "degenerate_score_groups": degenerate_groups,
        "human_overrides": sum(1 for c in claim_rows if c["human_trust_override"]),
        "never_evidence_searched": sum(1 for c in claim_rows if c["evidence_search_attempted_at"] is None),
        "never_adversarial_probed": sum(1 for c in claim_rows if c["last_adversarial_probe_at"] is None),
    }

    return {"summary": summary, "claims": per_claim_out}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--page-id", type=int)
    ap.add_argument("--all-pages", action="store_true")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    with SessionLocal() as s:
        if args.all_pages:
            ids = [r[0] for r in s.execute(text("SELECT id FROM wiki_pages ORDER BY id")).all()]
            result = {"pages": [audit_page(s, pid) for pid in ids]}
        elif args.page_id is not None:
            result = audit_page(s, args.page_id)
        else:
            sys.exit("--page-id or --all-pages required")

    Path(args.out).write_text(json.dumps(result, default=str, indent=2))
    # Print compact summary to stdout for ops visibility.
    if args.all_pages:
        total_pages = len(result["pages"])
        total_flags = Counter()
        for p in result["pages"]:
            if "summary" in p:
                for k, v in p["summary"].get("flag_counts", {}).items():
                    total_flags[k] += v
        print(f"audited {total_pages} pages | flag totals = {dict(total_flags)} | wrote {args.out}")
    else:
        print(f"page_id={args.page_id} | {result['summary']} | wrote {args.out}")


if __name__ == "__main__":
    main()
