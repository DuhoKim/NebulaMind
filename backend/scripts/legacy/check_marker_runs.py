import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from sqlalchemy import text

db = SessionLocal()
print("\n--- LATEST 15 Claim Marker Runs ---")
runs = db.execute(text("""
    SELECT id, page_id, page_version, source_version, total_claims, matched_claims, rejected_ambiguous_span, status, run_started_at, run_finished_at, notes, asserted_count
    FROM claim_marker_runs
    ORDER BY id DESC
    LIMIT 15
""")).fetchall()

for r in runs:
    print(f"ID: {r[0]} | Page ID: {r[1]} | Page Ver: {r[2]} | Src Ver: {r[3]} | Total Claims: {r[4]} | Matched: {r[5]} | Rejected Ambiguous: {r[6]} | Status: {r[7]} | Started: {r[8]} | Finished: {r[9]} | Notes: {r[10]}")

db.close()
