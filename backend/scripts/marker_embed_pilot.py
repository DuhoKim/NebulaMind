"""Pilot run of the claim marker embedding pipeline.

Usage:
    .venv/bin/python scripts/marker_embed_pilot.py --page-slug galaxy-evolution [--no-promote]

--no-promote: write a new PageVersion but leave wiki_pages.content unchanged.
              This is the pilot mode: review before promoting.
"""
import argparse
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("marker_embed_pilot")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--page-slug", default="galaxy-evolution")
    parser.add_argument("--no-promote", action="store_true",
                        help="Write PV but do not update wiki_pages.content")
    args = parser.parse_args()

    from app.database import SessionLocal
    from sqlalchemy import text
    from app.agent_loop.marker_embed.pipeline import run_pipeline

    db = SessionLocal()
    try:
        page_row = db.execute(
            text("SELECT id, content FROM wiki_pages WHERE slug = :slug"),
            {"slug": args.page_slug},
        ).fetchone()
        if not page_row:
            log.error("Page not found: %s", args.page_slug)
            sys.exit(1)

        page_id, content = page_row[0], page_row[1]
        log.info("Page id=%d slug=%s content_len=%d", page_id, args.page_slug, len(content))

        latest_pv = db.execute(
            text("SELECT version_num FROM page_versions WHERE page_id=:pid ORDER BY version_num DESC LIMIT 1"),
            {"pid": page_id},
        ).fetchone()
        source_version = latest_pv[0] if latest_pv else None

        claims_rows = db.execute(
            text("SELECT id, text, trust_level, section, order_idx FROM claims WHERE page_id=:pid ORDER BY section, order_idx"),
            {"pid": page_id},
        ).fetchall()

        claims = [
            {"id": r[0], "text": r[1], "trust_level": r[2], "section": r[3], "order_idx": r[4]}
            for r in claims_rows
        ]
        log.info("Loaded %d claims", len(claims))

        started_at = datetime.datetime.utcnow()
        new_content, stats = run_pipeline(
            page_id=page_id,
            content=content,
            claims=claims,
            source_version=source_version,
        )

        log.info("Pipeline complete: status=%s coverage=%.2f matched=%d/%d",
                 stats.status, stats.coverage_pct, stats.matched_claims, stats.total_claims)
        log.info("mean_confidence=%.3f judge_agreement_pct=%.2f",
                 stats.mean_confidence, stats.judge_agreement_pct)
        log.info("rejected: no_section=%d low_confidence=%d ambiguous=%d validation=%d",
                 stats.rejected_no_section, stats.rejected_low_confidence,
                 stats.rejected_ambiguous_span, stats.rejected_validation)

        if new_content is None:
            log.warning("Pipeline rolled back or no content produced. Notes: %s", stats.notes)
            sys.exit(0)

        # Write PageVersion (always)
        ver_row = db.execute(
            text("""
                INSERT INTO page_versions (page_id, version_num, content, created_at)
                VALUES (:pid, COALESCE((SELECT MAX(version_num) FROM page_versions WHERE page_id=:pid),0)+1, :content, NOW())
                RETURNING version_num
            """),
            {"pid": page_id, "content": new_content},
        ).fetchone()
        new_version = ver_row[0] if ver_row else None
        log.info("Wrote PageVersion v%s", new_version)

        if not args.no_promote:
            db.execute(
                text("UPDATE wiki_pages SET content = :c WHERE id = :pid"),
                {"c": new_content, "pid": page_id},
            )
            log.info("Promoted to wiki_pages.content (page_id=%d)", page_id)
        else:
            log.info("--no-promote: wiki_pages.content unchanged. PV v%s is in page_versions.", new_version)

        # Audit log
        db.execute(
            text("""
                INSERT INTO claim_marker_runs (
                    page_id, page_version, source_version,
                    total_claims, matched_claims,
                    rejected_low_confidence, rejected_no_section,
                    rejected_ambiguous_span, rejected_validation,
                    mean_confidence, judge_agreement_pct, coverage_pct,
                    status, run_started_at, run_finished_at, notes
                ) VALUES (
                    :page_id, :pv, :sv,
                    :total, :matched, :rej_conf, :rej_sec, :rej_amb, :rej_val,
                    :mean_conf, :judge_pct, :cov_pct,
                    :status, :started, NOW(), :notes
                )
            """),
            {
                "page_id": page_id,
                "pv": new_version,
                "sv": source_version,
                "total": stats.total_claims,
                "matched": stats.matched_claims,
                "rej_conf": stats.rejected_low_confidence,
                "rej_sec": stats.rejected_no_section,
                "rej_amb": stats.rejected_ambiguous_span,
                "rej_val": stats.rejected_validation,
                "mean_conf": stats.mean_confidence,
                "judge_pct": stats.judge_agreement_pct,
                "cov_pct": stats.coverage_pct,
                "status": "pilot_no_promote" if args.no_promote else stats.status,
                "started": started_at,
                "notes": stats.notes or None,
            },
        )
        db.commit()
        log.info("Audit log written to claim_marker_runs.")

    finally:
        db.close()


if __name__ == "__main__":
    main()
