#!/usr/bin/env python3
"""
§7.3 + §7.5 galaxy-evolution v2 rollout:
  - Strip artificial debate markers from PV 3587 (Rakon v3 output)
  - Save as new PageVersion
  - Promote to WikiPage.content
  - Trigger update_coverage_map_daily

Design ref: docs/galaxy_evolution_v2_revised.md §5 (R1) and §7
"""
import sys, re
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from app.database import SessionLocal
from app.models.page import WikiPage, PageVersion
from sqlalchemy.sql import func

SOURCE_PV_ID  = 3587
PAGE_ID       = 57
PAGE_SLUG     = "galaxy-evolution"
EDITOR_AGENT  = 34   # ToriSonnet
TARGET_IDS    = list(range(1487, 1497))   # D1-D10

MARKER_RE = re.compile(
    r'<!--\s*/?(claim):(' + '|'.join(str(i) for i in TARGET_IDS) + r')\s*-->',
)


def strip_artificial_debate_markers(content: str) -> tuple[str, int]:
    matches = MARKER_RE.findall(content)
    stripped = MARKER_RE.sub('', content)
    # Collapse extra blank lines left behind
    stripped = re.sub(r'\n{3,}', '\n\n', stripped).strip()
    return stripped, len(matches)


def main(dry_run: bool = False):
    db = SessionLocal()
    try:
        # Load source PageVersion
        source_pv = db.query(PageVersion).filter(PageVersion.id == SOURCE_PV_ID).one()
        original = source_pv.content or ''
        stripped, n_removed = strip_artificial_debate_markers(original)

        print(f'Source PV {SOURCE_PV_ID}: {len(original)} chars, {n_removed} markers removed')
        print(f'Stripped content: {len(stripped)} chars')

        # Verify no target markers remain
        remaining = MARKER_RE.findall(stripped)
        assert not remaining, f'Markers still present: {remaining}'
        print('Marker verification: PASS (0 remaining)')

        if dry_run:
            print('[DRY RUN] Stopping before writes.')
            return

        # Compute next version_num
        from sqlalchemy import func as sqlfunc
        max_vnum = db.query(sqlfunc.max(PageVersion.version_num)).filter(
            PageVersion.page_id == PAGE_ID
        ).scalar() or 0
        next_vnum = max_vnum + 1
        print(f'Next version_num: {next_vnum}')

        # Save new PageVersion
        new_pv = PageVersion(
            page_id=PAGE_ID,
            version_num=next_vnum,
            content=stripped,
            editor_agent_id=EDITOR_AGENT,
            created_at=func.now(),
        )
        db.add(new_pv)
        db.flush()
        print(f'New PageVersion id={new_pv.id}')

        # Promote to WikiPage.content
        page = db.query(WikiPage).filter(WikiPage.id == PAGE_ID).one()
        page.content = stripped
        db.flush()
        print(f'WikiPage id={PAGE_ID} ({PAGE_SLUG}) promoted to PV {new_pv.id}')

        db.commit()
        print('Committed.')

        # Trigger coverage map update via Celery
        try:
            from app.agent_loop.tasks import update_coverage_map_daily
            result = update_coverage_map_daily.delay()
            print(f'update_coverage_map_daily queued: task_id={result.id}')
        except Exception as e:
            print(f'[WARN] Could not queue update_coverage_map_daily: {e}')

    finally:
        db.close()


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--apply', action='store_true')
    args = p.parse_args()
    main(dry_run=not args.apply)
