#!/usr/bin/env python3
"""Push 6 lowest-health queued renovation plans into the gather→synthesize pipeline."""
import sys, time
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from app.database import SessionLocal
from app.models.page import WikiPage, RenovationPlan
from app.agent_loop.tasks import gather_renovation_evidence

TARGET_COUNT = 6

def main():
    db = SessionLocal()
    plans = (
        db.query(RenovationPlan)
        .filter(RenovationPlan.status == "queued")
        .join(WikiPage, WikiPage.id == RenovationPlan.page_id)
        .order_by(WikiPage.health_score.asc())
        .limit(TARGET_COUNT)
        .all()
    )
    pairs = [
        (p.id, db.query(WikiPage).filter(WikiPage.id == p.page_id).first().slug,
         db.query(WikiPage).filter(WikiPage.id == p.page_id).first().health_score)
        for p in plans
    ]
    db.close()

    print(f"Enqueueing {len(pairs)} renovation plans:", flush=True)
    for pid, slug, score in pairs:
        print(f"  plan#{pid} {slug} health={score:.1f}", flush=True)
        gather_renovation_evidence.delay(pid)
        time.sleep(1)

    print(f"\nDone — {len(pairs)} plans enqueued into Celery (gather→synthesize→commit chain).")

if __name__ == "__main__":
    main()
