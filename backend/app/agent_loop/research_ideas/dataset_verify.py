import time
import logging
from datetime import datetime, timedelta

import httpx
from celery import shared_task
from sqlalchemy import text

from app.database import SessionLocal

logger = logging.getLogger(__name__)

USER_AGENT = "NebulaMind-Verifier/1.0 (papa@duhokim.org)"


@shared_task(name="dataset_verify.run_verification")
def run_dataset_verification():
    db = SessionLocal()
    try:
        _run(db)
    finally:
        db.close()


def _run(db):
    cutoff = datetime.utcnow() - timedelta(days=3)
    datasets = db.execute(text("""
        SELECT id, slug, primary_url, registry, url_verified_ok, url_verified_note, status
        FROM survey_datasets
        WHERE status != 'deprecated'
          AND (url_verified_at IS NULL OR (url_verified_ok = TRUE AND url_verified_at < :cutoff))
    """), {"cutoff": cutoff}).fetchall()

    logger.info(f"Dataset verifier: checking {len(datasets)} datasets")

    for ds in datasets:
        try:
            ok, note = _check_url(ds.primary_url, ds.registry)
        except Exception as e:
            ok, note = False, f"error: {e}"

        # Track consecutive failures
        fail_count = 0
        if not ok:
            prev_note = ds.url_verified_note or ""
            if prev_note.startswith("fail:"):
                try:
                    fail_count = int(prev_note.split(":")[1]) + 1
                except Exception:
                    fail_count = 1
            else:
                fail_count = 1
            note = f"fail:{fail_count} {note}"

        new_status = ds.status
        if not ok and fail_count >= 3:
            new_status = "deprecated"
            logger.warning(f"Dataset {ds.slug} deprecated after {fail_count} failures")

        db.execute(text("""
            UPDATE survey_datasets
            SET url_verified_at = NOW(), url_verified_ok = :ok,
                url_verified_note = :note, status = :status, updated_at = NOW()
            WHERE id = :id
        """), {"ok": ok, "note": note, "status": new_status, "id": ds.id})
        db.commit()

        # Update datasets_verified on linked ideas
        _refresh_idea_verified(db, ds.id)

        time.sleep(1)

    logger.info("Dataset verifier: done")


def _check_url(url: str, registry: str | None) -> tuple[bool, str]:
    with httpx.Client(timeout=10, headers={"User-Agent": USER_AGENT}, follow_redirects=True) as client:
        r = client.head(url)
        if r.status_code < 400:
            return True, "ok"
        return False, f"http:{r.status_code}"


def _refresh_idea_verified(db, dataset_id: int):
    idea_rows = db.execute(text("""
        SELECT DISTINCT idea_id FROM research_idea_datasets WHERE dataset_id = :did
    """), {"did": dataset_id}).fetchall()

    for row in idea_rows:
        total_primary = db.execute(text("""
            SELECT COUNT(*) FROM research_idea_datasets rid
            JOIN survey_datasets sd ON sd.id = rid.dataset_id
            WHERE rid.idea_id = :iid AND rid.role = 'primary'
        """), {"iid": row.idea_id}).scalar()

        verified_primary = db.execute(text("""
            SELECT COUNT(*) FROM research_idea_datasets rid
            JOIN survey_datasets sd ON sd.id = rid.dataset_id
            WHERE rid.idea_id = :iid AND rid.role = 'primary'
              AND sd.url_verified_ok = TRUE
              AND sd.url_verified_at > NOW() - INTERVAL '30 days'
        """), {"iid": row.idea_id}).scalar()

        all_ok = total_primary > 0 and verified_primary == total_primary
        db.execute(text("""
            UPDATE research_ideas SET datasets_verified = :v, datasets_verified_at = NOW()
            WHERE id = :iid
        """), {"v": all_ok, "iid": row.idea_id})
    db.commit()
