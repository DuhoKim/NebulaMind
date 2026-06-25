"""Phase 1 backfill script.

Run once after `alembic upgrade head` for Phase 1.

  1. Count evidence rows where arxiv_id IS NULL AND doi IS NULL (hallucinated).
  2. In --apply mode:
     - Delete those rows.
     - Set quality=0.50 for all surviving evidence rows.
     - Recompute trust_score for all claims via recalculate_trust_v2.
     - Write trust_audit_log rows with trigger='migration'.
  3. Print before/after stats.

Usage:
    python scripts/backfill_phase1.py            # dry-run
    python scripts/backfill_phase1.py --apply    # actually write
"""
from __future__ import annotations

import argparse
import sys
import os

# Ensure project root is on the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from app.config import settings
from app.models.claim import Claim, Evidence, TrustAuditLog


def main(apply: bool = False) -> None:
    engine = create_engine(settings.DATABASE_URL)

    with Session(engine) as db:
        # ---- Stats before ----
        total_evidence = db.query(Evidence).count()
        hallucinated = (
            db.query(Evidence)
            .filter(Evidence.arxiv_id.is_(None), Evidence.doi.is_(None))
            .count()
        )
        total_claims = db.query(Claim).count()

        print("=" * 60)
        print("PHASE 1 BACKFILL — DRY RUN" if not apply else "PHASE 1 BACKFILL — APPLYING")
        print("=" * 60)
        print(f"Total evidence rows:        {total_evidence}")
        print(f"Hallucinated (no arXiv/DOI): {hallucinated}  ({hallucinated/max(total_evidence,1)*100:.1f}%)")
        print(f"Will survive:               {total_evidence - hallucinated}")
        print(f"Total claims:               {total_claims}")
        print()

        if not apply:
            print("DRY RUN — use --apply to execute changes.")
            return

        # ---- Step 1: Delete hallucinated evidence ----
        deleted = (
            db.query(Evidence)
            .filter(Evidence.arxiv_id.is_(None), Evidence.doi.is_(None))
            .delete(synchronize_session=False)
        )
        print(f"Deleted {deleted} hallucinated evidence rows.")

        # ---- Step 2: Set quality=0.50 for survivors ----
        updated = (
            db.query(Evidence)
            .update({"quality": 0.50}, synchronize_session=False)
        )
        print(f"Set quality=0.50 for {updated} surviving evidence rows.")
        db.flush()

        # ---- Step 3: Recompute trust for all claims ----
        from app.services.trust_calculation import recalculate_trust_v2

        claims = db.query(Claim).all()
        level_counts: dict[str, int] = {}
        for claim in claims:
            new_level, ts = recalculate_trust_v2(
                claim.id, db,
                trigger="migration",
                actor_agent_id=None,
                actor_human_id=None,
            )
            level_counts[new_level] = level_counts.get(new_level, 0) + 1

        db.commit()

        # ---- Stats after ----
        total_evidence_after = db.query(Evidence).count()
        print()
        print("=" * 60)
        print("AFTER BACKFILL")
        print("=" * 60)
        print(f"Remaining evidence rows: {total_evidence_after}")
        print(f"Trust level distribution:")
        for level, count in sorted(level_counts.items(), key=lambda x: -x[1]):
            print(f"  {level:15s}: {count}")
        print()
        print("Backfill complete. Check trust_audit_log for details.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase 1 backfill for NebulaMind trust mechanics.")
    parser.add_argument("--apply", action="store_true", help="Actually apply changes (default: dry-run)")
    args = parser.parse_args()
    main(apply=args.apply)
