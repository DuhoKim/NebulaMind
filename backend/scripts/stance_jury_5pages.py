"""
Task 15: Stance jury pass on new evidence for the 5 low-health pages.

Enqueues run_stance_jury_for_evidence for all unjudged evidence on:
  - Accretion Disks    (id=40)
  - Planetary Formation (id=50)
  - Interstellar Medium (id=37)
  - Cosmic Web          (id=55)
  - Reionization        (id=38)

Blanc (llama3.3:70b) is already part of STANCE_JURY_MODELS and provides
quality signal. The full 4-model parallel jury runs for each evidence item.

Run from the backend/ directory:
  .venv/bin/python3 scripts/stance_jury_5pages.py
"""
from __future__ import annotations

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.claim import Claim, Evidence

TARGET_PAGES = [40, 50, 37, 55, 38]
STAGGER_SECONDS = 2  # match drain_stance_jury_backlog countdown


def main():
    db = SessionLocal()
    try:
        from app.agent_loop.tasks import run_stance_jury_for_evidence

        total_queued = 0

        for page_id in TARGET_PAGES:
            claims = db.query(Claim).filter(Claim.page_id == page_id).all()
            claim_ids = [c.id for c in claims]
            if not claim_ids:
                continue

            unjudged = (
                db.query(Evidence)
                .filter(
                    Evidence.claim_id.in_(claim_ids),
                    Evidence.stance_jury_run_at.is_(None),
                )
                .order_by(Evidence.id)
                .all()
            )

            print(f"Page {page_id}: {len(unjudged)} unjudged evidence items")
            for i, ev in enumerate(unjudged):
                run_stance_jury_for_evidence.apply_async(
                    args=[ev.id],
                    countdown=i * STAGGER_SECONDS,
                )
                print(f"  Queued evidence {ev.id} (claim {ev.claim_id}, countdown={i * STAGGER_SECONDS}s)")
                total_queued += 1

        print(f"\nTask 15 complete. Total stance jury tasks queued: {total_queued}")

    finally:
        db.close()


if __name__ == "__main__":
    main()
