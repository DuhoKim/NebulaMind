"""Phase 1 bulk run.

Step 1: For every Evidence row, verify its arxiv_id (if any) and persist
        `arxiv_verified` and `quality`.

Step 2: For every Claim, run the new Phase 1 `recalculate_trust()` and report
        the trust-level transitions.

Run from backend/:
    PYTHONPATH=. .venv/bin/python3 scripts/recalculate_trust_all.py
"""
from __future__ import annotations

import sys
import time
from collections import Counter

from app.database import SessionLocal
from app.models.claim import Claim, Evidence
from app.services.paper_search import verify_arxiv_id
from app.services.trust_calculator import recalculate_trust


def verify_all_evidence(db, *, sleep_between: float = 0.05) -> dict:
    """Mark every Evidence row's arxiv_verified flag.

    Fast path: rows that already have `verified_at` set AND a real `arxiv_id`
    were resolved via ADS by the v2 linker — trust them, no network call.

    Slow path: legacy rows (no verified_at) get a live verify_arxiv_id() check.

    Returns counters: {checked, fast_verified, slow_verified, no_arxiv_id, failed}.
    """
    rows = db.query(Evidence).all()
    counts = {
        "checked": 0, "fast_verified": 0, "slow_verified": 0,
        "no_arxiv_id": 0, "failed": 0,
    }

    # ---- Fast path: bulk-mark ADS-verified rows ----
    fast_n = 0
    for ev in rows:
        counts["checked"] += 1
        if ev.arxiv_verified:
            continue
        if not ev.arxiv_id:
            ev.arxiv_verified = False
            counts["no_arxiv_id"] += 1
            continue
        if ev.verified_at is not None:
            ev.arxiv_verified = True
            counts["fast_verified"] += 1
            fast_n += 1
            if fast_n % 1000 == 0:
                db.commit()
                print(f"  ...fast-verified {fast_n} rows")
    db.commit()
    print(f"  fast-path complete: {counts['fast_verified']} verified, "
          f"{counts['no_arxiv_id']} have no arxiv_id")

    # ---- Slow path: legacy rows that need real verification ----
    legacy = [
        e for e in rows
        if not e.arxiv_verified and e.arxiv_id and e.verified_at is None
    ]
    print(f"  slow path: {len(legacy)} legacy rows to verify")

    for i, ev in enumerate(legacy, 1):
        claim = db.query(Claim).get(ev.claim_id)
        claim_text = claim.text if claim else ""
        try:
            v = verify_arxiv_id(ev.arxiv_id, claim_text)
        except Exception as exc:
            print(f"  [ev #{ev.id}] verify error: {exc}")
            counts["failed"] += 1
            continue
        ev.arxiv_verified = v["verified"]
        if v["verified"] and v["quality"] > (ev.quality or 0.0):
            ev.quality = v["quality"]
        if v["verified"]:
            counts["slow_verified"] += 1
        if i % 25 == 0:
            db.commit()
            print(f"  ...verified {i}/{len(legacy)} legacy rows")
        time.sleep(sleep_between)

    db.commit()
    return counts


def recalc_all_claims(db) -> dict:
    """Run recalculate_trust() for every claim. Returns transition counter."""
    claims = db.query(Claim).all()
    transitions = Counter()
    new_levels = Counter()

    for c in claims:
        old = c.trust_level
        try:
            new = recalculate_trust(c.id, db)
        except Exception as exc:
            print(f"  [claim #{c.id}] recalc error: {exc}")
            db.rollback()
            continue
        new_levels[new] += 1
        if old != new:
            transitions[(old, new)] += 1

    return {"total": len(claims), "new_levels": new_levels, "transitions": transitions}


def main() -> int:
    db = SessionLocal()
    try:
        print("=== Phase 1 bulk recalculation ===\n")

        print("Step 1: verifying all evidence against arXiv ...")
        v_counts = verify_all_evidence(db)
        print(f"  checked        : {v_counts['checked']}")
        print(f"  fast-verified  : {v_counts['fast_verified']}")
        print(f"  slow-verified  : {v_counts['slow_verified']}")
        print(f"  no arxiv_id    : {v_counts['no_arxiv_id']}")
        print(f"  errors         : {v_counts['failed']}\n")

        print("Step 2: recalculating trust for all claims ...")
        r = recalc_all_claims(db)
        print(f"  total claims: {r['total']}")
        print("  new trust distribution:")
        for level, n in r["new_levels"].most_common():
            print(f"    {level:<12} {n}")
        if r["transitions"]:
            print("  transitions (old -> new : count):")
            for (old, new), n in r["transitions"].most_common():
                print(f"    {old or 'NULL':<12} -> {new:<12} {n}")
        else:
            print("  no trust-level transitions (all stable)")
        return 0
    finally:
        db.close()


if __name__ == "__main__":
    sys.exit(main())
