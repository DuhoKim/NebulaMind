#!/usr/bin/env python3
"""Run one-shot full backfill canonicalization on all wiki pages."""

from __future__ import annotations
import argparse
import sys
import json
import subprocess
from pathlib import Path

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/backend")

from app.database import SessionLocal, engine
from app.models.agent import Agent  # noqa: F401 - required for PageVersion FK metadata
from app.models.page import ContentQuarantine, WikiPage, PageVersion
from app.services.content_canonicalizer import canonicalize


def _git_metadata() -> dict[str, object]:
    repo = Path(__file__).resolve().parents[2]

    def run(*args: str) -> str:
        return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()

    try:
        sha = run("rev-parse", "HEAD")
        status = run("status", "--porcelain")
        return {
            "canonicalizer_git_sha": sha,
            "git_dirty": bool(status),
            "git_status_porcelain": status.splitlines(),
        }
    except Exception as exc:
        return {
            "canonicalizer_git_sha": None,
            "git_dirty": None,
            "git_metadata_error": str(exc),
        }

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print diff stats without committing")
    parser.add_argument("--report", help="Path to write JSON report")
    args = parser.parse_args()

    db = SessionLocal()
    ContentQuarantine.__table__.create(bind=engine, checkfirst=True)
    pages = db.query(WikiPage).order_by(WikiPage.id).all()
    reports = []
    
    print(f"Found {len(pages)} pages to canonicalize.")
    
    total_changes = {
        "latex_paren": 0,
        "num_sup": 0,
        "symbol": 0,
        "bare_sub": 0,
        "orphan_us": 0,
        "composite": 0,
        "cite": 0,
        "math_safety": 0,
        "bare_tex": 0,
        "bare_tex_lines": 0,
        "bare_latex_sub": 0,
        "reference_sections": 0,
        "numeric_refs": 0,
        "legacy_display_fences": 0,
        "markdown_fence": 0,
        "nested_math": 0,
        "final_unicode": 0,
        "entity_decode": 0,
        "orphan_span": 0,
    }
    
    changed_pages_count = 0
    quarantine_count = 0
    would_quarantine_count = 0

    for page in pages:
        content = page.content or ""
        result = canonicalize(content)
        
        has_changes = any(count > 0 for count in result.changes.values())
        would_quarantine = not result.invariants_ok
        if would_quarantine:
            would_quarantine_count += 1
        
        page_report = {
            "page_id": page.id,
            "slug": page.slug,
            "title": page.title,
            "has_changes": has_changes,
            "changes": result.changes,
            "invariants_ok": result.invariants_ok,
            "would_quarantine": would_quarantine,
            "violations": result.violations or [],
        }
        reports.append(page_report)
        
        if has_changes:
            changed_pages_count += 1
            for k, count in result.changes.items():
                total_changes[k] = total_changes.get(k, 0) + count
                
            print(f"Page {page.id} ({page.slug}): {result.changes} | invariants_ok={result.invariants_ok}")
        elif would_quarantine:
            print(f"Page {page.id} ({page.slug}): no changes | invariants_ok=False | violations={result.violations}")
            
        if would_quarantine and not args.dry_run:
            quarantine_count += 1
            db.add(
                ContentQuarantine(
                    page_id=page.id,
                    source_tag="canonicalize_corpus_v2",
                    violations=json.dumps(result.violations or [], ensure_ascii=False),
                    content=result.new_content,
                )
            )
            db.flush()
            continue

        if has_changes and not args.dry_run:
            # Update page content
            page.content = result.new_content
            page.content_canonicalize_failed_at = None
            page.content_canonicalize_failure_reason = None
            
            # Get next version number
            last_pv = (
                db.query(PageVersion)
                .filter(PageVersion.page_id == page.id)
                .order_by(PageVersion.version_num.desc())
                .first()
            )
            next_vnum = (last_pv.version_num + 1) if last_pv else 1
            
            # Write page version
            pv = PageVersion(
                page_id=page.id,
                version_num=next_vnum,
                content=result.new_content,
                source_note="canonicalize_backfill_v2"
            )
            db.add(pv)
            
            db.flush()

    if not args.dry_run:
        db.commit()
        print("Committed all canonicalization changes.")
    else:
        db.rollback()
        print("[DRY-RUN] Rolled back all changes.")

    print("\n=== Summary Stats ===")
    print(f"Total pages updated: {changed_pages_count} / {len(pages)}")
    print(f"Total pages quarantined: {quarantine_count}")
    print(f"Total pages that would quarantine: {would_quarantine_count}")
    print(f"Total change details: {total_changes}")

    if args.report:
        payload = {
            "metadata": {
                **_git_metadata(),
                "dry_run": args.dry_run,
                "page_count": len(pages),
                "changed_pages_count": changed_pages_count,
                "quarantine_count": quarantine_count,
                "would_quarantine_count": would_quarantine_count,
                "total_changes": total_changes,
            },
            "pages": reports,
        }
        Path(args.report).write_text(json.dumps(payload, ensure_ascii=False, indent=2))
        print(f"Report written to {args.report}")

if __name__ == "__main__":
    main()
