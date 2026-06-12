"""
Push queued renovation plans into synthesis.
Queues synthesize_renovation tasks for plans that have papers gathered
but no synthesis yet, prioritizing lowest health score pages.
"""
from __future__ import annotations
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.page import RenovationPlan, WikiPage
from app.agent_loop.worker import celery_app
from sqlalchemy.orm import joinedload

BATCH_SIZE = 5  # how many to push at once

def main():
    db = SessionLocal()
    try:
        plans = (
            db.query(RenovationPlan)
            .join(WikiPage, WikiPage.id == RenovationPlan.page_id)
            .filter(
                RenovationPlan.status == "queued",
                RenovationPlan.notes.isnot(None),
                RenovationPlan.edit_proposal_id.is_(None),
            )
            .order_by(RenovationPlan.health_score.asc())
            .limit(BATCH_SIZE)
            .all()
        )

        if not plans:
            print("No eligible queued plans to push.")
            return

        pushed = []
        for plan in plans:
            notes = None
            notes_str = plan.notes or ""
            if notes_str.startswith('{"') or notes_str == "{}":
                try:
                    notes = json.loads(notes_str)
                except Exception:
                    pass
            if notes is None:
                try:
                    import ast
                    notes = ast.literal_eval(notes_str)
                    # Canonicalize to JSON
                    plan.notes = json.dumps(notes)
                    db.commit()
                except Exception:
                    pass
            if notes is None:
                print(f"  Plan {plan.id}: can't parse notes, skipping")
                continue

            papers = notes.get("papers", [])
            if not papers:
                print(f"  Plan {plan.id}: notes present but no papers, skipping")
                continue

            has_synth = bool(notes.get("synthesized_section"))
            page = db.query(WikiPage).filter(WikiPage.id == plan.page_id).first()
            slug = page.slug if page else f"page_{plan.page_id}"

            if has_synth:
                # Has synthesized section but not committed → verify
                plan.status = "synthesizing"
                db.commit()
                celery_app.send_task(
                    "app.agent_loop.tasks.verify_renovation",
                    args=[plan.id]
                )
                pushed.append((plan.id, slug, "verify"))
                print(f"  Plan {plan.id} ({slug}): has synth → queued verify_renovation")
            else:
                # Has papers but no synthesis → synthesize
                plan.status = "synthesizing"
                db.commit()
                celery_app.send_task(
                    "app.agent_loop.tasks.synthesize_renovation",
                    args=[plan.id]
                )
                pushed.append((plan.id, slug, "synthesize"))
                print(f"  Plan {plan.id} ({slug}): {len(papers)} papers → queued synthesize_renovation")

        print(f"\nPushed {len(pushed)} plans into synthesis.")
        for pid, slug, task in pushed:
            print(f"  - Plan {pid} ({slug}): {task}")

    finally:
        db.close()


if __name__ == "__main__":
    main()
