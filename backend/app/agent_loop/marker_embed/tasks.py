"""Celery task: claim_marker_embed_page.

Triggered by MARKER_REEMBED_REQUIRED events emitted at every content-rewrite
site. Diffs old vs. new content; no-ops if unchanged.
"""
import datetime
import logging

from celery import shared_task
from sqlalchemy import text

log = logging.getLogger(__name__)


@shared_task(
    name="app.agent_loop.marker_embed.tasks.claim_marker_embed_page",
    bind=True,
    max_retries=2,
    default_retry_delay=300,
)
def claim_marker_embed_page(self, page_id: int, section_key: str = None, expected_source_version: int = None) -> dict:
    """Run the marker embedding pipeline for a single page."""
    from app.database import SessionLocal
    from app.agent_loop.marker_embed.pipeline import run_pipeline
    from app.agent_loop.marker_embed.injector import strip_markers
    from app.models.page import WikiPage, PageVersion

    started_at = datetime.datetime.utcnow()
    db = SessionLocal()
    try:
        page = db.execute(
            text("SELECT id, content FROM wiki_pages WHERE id = :pid"),
            {"pid": page_id},
        ).fetchone()
        if not page:
            return {"skip": "page_not_found", "page_id": page_id}

        content = page[1]

        # Get source version for audit log
        latest_pv = db.execute(
            text(
                "SELECT version_num FROM page_versions "
                "WHERE page_id = :pid ORDER BY version_num DESC LIMIT 1"
            ),
            {"pid": page_id},
        ).fetchone()
        source_version = latest_pv[0] if latest_pv else None

        # Load active section-owned claims. Phase 3 uses
        # claim_section_assignments.owner_section_key as the section identity.
        query = """
            SELECT c.id, c.text, c.trust_level, a.owner_section_key, c.order_idx
            FROM claims c
            JOIN claim_section_assignments a ON a.claim_id = c.id
            WHERE c.page_id = :pid AND a.page_id = :pid
              AND a.assignment_status = 'active'
        """
        params = {"pid": page_id}
        if section_key:
            query += " AND a.owner_section_key = :section_key"
            params["section_key"] = section_key
        query += " ORDER BY a.owner_section_key, c.order_idx"

        rows = db.execute(text(query), params).fetchall()

        if not rows:
            return {"skip": "no_claims", "page_id": page_id}

        claims = [
            {
                "id": r[0],
                "text": r[1],
                "trust_level": r[2],
                "section": r[3],
                "order_idx": r[4],
            }
            for r in rows
        ]

        log.info(
            "claim_marker_embed_page: page_id=%d claims=%d source_v=%s",
            page_id,
            len(claims),
            source_version,
        )

        if expected_source_version and source_version != expected_source_version:
            log.warning("[claim_marker] Version mismatch: expected %s, got %s. Aborting.", expected_source_version, source_version)
            return {"status": "aborted_version_mismatch"}
            
        new_content, stats = run_pipeline(
            page_id=page_id,
            content=content,
            claims=claims,
            source_version=source_version,
            section_key=section_key
        )

        # Write audit log regardless of outcome
        new_version = None
        if new_content is not None:
            # Write new PageVersion + update wiki_pages.content
            ver_row = db.execute(
                text("""
                    INSERT INTO page_versions (page_id, version_num, content, created_at)
                    VALUES (
                        :pid,
                        COALESCE((SELECT MAX(version_num) FROM page_versions WHERE page_id=:pid), 0) + 1,
                        :content, NOW()
                    )
                    RETURNING version_num
                """),
                {"pid": page_id, "content": new_content},
            ).fetchone()
            new_version = ver_row[0] if ver_row else None
            db.execute(
                text("UPDATE wiki_pages SET content = :c WHERE id = :pid"),
                {"c": new_content, "pid": page_id},
            )

        finished_at = datetime.datetime.utcnow()
        db.execute(
            text("""
                INSERT INTO claim_marker_runs (
                    page_id, page_version, source_version,
                    total_claims, matched_claims,
                    rejected_low_confidence, rejected_no_section,
                    rejected_ambiguous_span, rejected_validation,
                    mean_confidence, judge_agreement_pct, coverage_pct,
                    status, run_started_at, run_finished_at, notes,
                    asserted_count, topical_anchor_count, tier_breakdown
                ) VALUES (
                    :page_id, :page_version, :source_version,
                    :total_claims, :matched_claims,
                    :rej_conf, :rej_sec, :rej_amb, :rej_val,
                    :mean_conf, :judge_pct, :coverage_pct,
                    :status, :started, :finished, :notes,
                    :asserted, :topical, :tier
                )
            """),
            {
                "page_id": page_id,
                "page_version": new_version,
                "source_version": source_version,
                "total_claims": stats.total_claims,
                "matched_claims": stats.matched_claims,
                "rej_conf": stats.rejected_low_confidence,
                "rej_sec": stats.rejected_no_section,
                "rej_amb": stats.rejected_ambiguous_span,
                "rej_val": stats.rejected_validation,
                "mean_conf": stats.mean_confidence,
                "judge_pct": stats.judge_agreement_pct,
                "coverage_pct": stats.coverage_pct,
                "status": stats.status,
                "started": started_at,
                "finished": finished_at,
                "notes": stats.notes or None,
                "asserted": getattr(stats, "asserted_count", stats.matched_claims),
                "topical": getattr(stats, "topical_anchor_count", 0),
                "tier": __import__('json').dumps(getattr(stats, "tier_breakdown", {"verbatim": stats.matched_claims, "sentence": 0, "topic": 0})),
            },
        )
        db.commit()

        log.info(
            "claim_marker_embed_page: page_id=%d status=%s coverage=%.2f matched=%d/%d",
            page_id,
            stats.status,
            stats.coverage_pct,
            stats.matched_claims,
            stats.total_claims,
        )

        return {
            "page_id": page_id,
            "status": stats.status,
            "coverage_pct": stats.coverage_pct,
            "matched": stats.matched_claims,
            "total": stats.total_claims,
            "new_version": new_version,
        }

    except Exception as exc:
        db.rollback()
        log.exception("claim_marker_embed_page: page_id=%d failed: %s", page_id, exc)
        raise self.retry(exc=exc)
    finally:
        db.close()


def emit_reembed(page_id: int, section_key: str = None, expected_source_version: int = None) -> None:
    """
    Fire-and-forget helper called at every content-rewrite site.
    Dispatches claim_marker_embed_page.delay(page_id, section_key, expected_source_version) safely.
    Must be called AFTER the database transaction commits to avoid race conditions reading stale pages.
    """
    try:
        claim_marker_embed_page.delay(page_id, section_key, expected_source_version)
        log.debug("MARKER_REEMBED_REQUIRED dispatched for page_id=%d section_key=%s v=%s", page_id, section_key, expected_source_version)
    except Exception as exc:
        log.warning("emit_reembed: dispatch failed page_id=%d err=%s", page_id, exc)
