import re
file_path = "tasks.py"
with open(file_path, "r") as f:
    content = f.read()

# Replace the sync_verbatim_markers_nightly alarm logic with the watchdog logic.
# "Replace the fixed-count alarm (<30) in nightly verbatim sync with a coverage-ratio watchdog"
# "Gates for page 57: warn <80%, repair retry <80%, targeted regen <70%, alert <50%"
# Note: we also log must-keep missing.

old_nightly = """        # Alarm check
        from app.models.page import WikiPage
        page = db.query(WikiPage).get(page_id)
        if page and page.content:
            import re
            marker_count = len(re.findall(r"<!--claim:\\d+-->", page.content))
            print(f"[system] Nightly sync check: {marker_count} markers on page {page_id}")
            if marker_count < 30:
                print(f"[ALARM] Page {page_id} marker coverage dropped below threshold: {marker_count} < 30")
                from app.agent_loop.tasks import _notify
                _notify(f"⚠️ [ALARM] Page {page_id} marker coverage dropped below threshold: {marker_count} < 30")"""

new_nightly = """        # Coverage Map / Watchdog (Phase 4)
        from sqlalchemy import text
        from app.models.page import WikiPage
        page = db.execute(text("SELECT id, slug, content FROM wiki_pages WHERE id = :pid"), {"pid": page_id}).fetchone()
        if page and page.content:
            import re
            # Count visible asserted markers
            markers = set(re.findall(r"<!--claim:(\\d+)\\s*-->", page.content))
            visible_count = len(markers)
            
            # Count active assigned claims
            owned_res = db.execute(text(\"\"\"
                SELECT c.id, c.trust_level 
                FROM claim_section_assignments a
                JOIN claims c ON c.id = a.claim_id
                WHERE a.page_id = :pid AND a.assignment_status = 'active'
            \"\"\"), {"pid": page_id}).fetchall()
            
            active_claims = {r.id for r in owned_res}
            must_keep_claims = {r.id for r in owned_res if r.trust_level in ('accepted', 'consensus')}
            
            # coverage ratio
            coverage_ratio = visible_count / len(active_claims) if active_claims else 1.0
            
            # must-keep missing
            must_keep_missing = must_keep_claims - set([int(x) for x in markers])
            
            print(f"[system] Watchdog for {page.slug}: coverage {coverage_ratio:.1%} ({visible_count}/{len(active_claims)}), must-keep missing: {len(must_keep_missing)}")
            
            from app.agent_loop.tasks import _notify
            if coverage_ratio < 0.50:
                _notify(f"🚨 [ALERT] Page {page_id} coverage collapsed: {coverage_ratio:.1%} ({visible_count}/{len(active_claims)}). Immediate intervention required.")
            elif coverage_ratio < 0.70 or must_keep_missing:
                # Trigger targeted regen / report
                msg = f"⚠️ [WARN] Page {page_id} coverage critically low: {coverage_ratio:.1%}. "
                if must_keep_missing:
                    msg += f"Missing must-keep claims: {len(must_keep_missing)}. "
                msg += "Targeted regeneration required."
                print(msg)
                _notify(msg)
            elif coverage_ratio < 0.80:
                # Dispatch repair retry
                msg = f"📉 [WARN] Page {page_id} coverage degraded: {coverage_ratio:.1%}. Triggering repair pass."
                print(msg)
                from app.agent_loop.marker_embed.tasks import claim_marker_embed_page
                claim_marker_embed_page.delay(page_id)
                _notify(msg)"""

content = content.replace(old_nightly, new_nightly)
with open(file_path, "w") as f:
    f.write(content)
print("Patched watchdog in tasks.py")
