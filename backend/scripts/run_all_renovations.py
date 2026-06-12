#!/usr/bin/env python3
"""Run full renovation pipeline synchronously for all queued pages."""
import sys, time
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from app.database import SessionLocal
from app.models.page import WikiPage, RenovationPlan
from app.agent_loop.tasks import (
    gather_renovation_evidence,
    synthesize_renovation,
    commit_renovation_proposal,
)


def run_pipeline(plan_id: int, slug: str) -> bool:
    print(f"\n=== {slug} (plan #{plan_id}) ===", flush=True)

    # Step 1: gather if needed
    db = SessionLocal()
    plan = db.query(RenovationPlan).filter(RenovationPlan.id == plan_id).first()
    status = plan.status if plan else None
    db.close()

    if status == "queued":
        try:
            gather_renovation_evidence(plan_id)
            print("  ✓ gathered", flush=True)
        except Exception as e:
            print(f"  gather ERROR: {e}", flush=True)
            return False

    # Step 2: synthesize
    db = SessionLocal()
    plan = db.query(RenovationPlan).filter(RenovationPlan.id == plan_id).first()
    status = plan.status if plan else None
    db.close()

    if status == "synthesizing":
        try:
            synthesize_renovation(plan_id)
            print("  ✓ synthesized", flush=True)
        except Exception as e:
            print(f"  synthesize ERROR: {e}", flush=True)
            return False

    # Step 3: commit
    db = SessionLocal()
    plan = db.query(RenovationPlan).filter(RenovationPlan.id == plan_id).first()
    notes = plan.notes if plan else None
    db.close()

    if notes and "synthesized_section" in str(notes):
        try:
            commit_renovation_proposal(plan_id)
            print("  ✓ PROPOSAL SUBMITTED!", flush=True)
            return True
        except Exception as e:
            print(f"  commit ERROR: {e}", flush=True)
    else:
        db = SessionLocal()
        plan = db.query(RenovationPlan).filter(RenovationPlan.id == plan_id).first()
        print(f"  No section, final status={plan.status if plan else 'unknown'}", flush=True)
        db.close()
    return False


def main():
    db = SessionLocal()
    plans = (
        db.query(RenovationPlan)
        .filter(RenovationPlan.status.in_(["queued", "synthesizing", "gathering"]))
        .join(WikiPage, WikiPage.id == RenovationPlan.page_id)
        .order_by(WikiPage.health_score.asc())
        .all()
    )
    pairs = [
        (p.id, db.query(WikiPage).filter(WikiPage.id == p.page_id).first().slug)
        for p in plans
    ]
    db.close()

    print(f"Processing {len(pairs)} renovation plans...", flush=True)
    submitted = 0
    for pid, slug in pairs:
        if run_pipeline(pid, slug):
            submitted += 1
        time.sleep(5)

    print(f"\n{'='*50}")
    print(f"Done. {submitted}/{len(pairs)} proposals submitted.")


if __name__ == "__main__":
    main()
