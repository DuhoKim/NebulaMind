import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.page import PageVersion
import re

db = SessionLocal()
versions = db.query(PageVersion).filter(PageVersion.page_id == 57).order_by(PageVersion.created_at.desc()).limit(15).all()

print("--- Chronological Latest Versions ---")
for v in versions:
    raw_markers = re.findall(r"<!--claim:([\d,\s]+)\s*-->", v.content)
    all_ids = []
    for r in raw_markers:
        for val in r.split(","):
            val = val.strip()
            if val:
                all_ids.append(int(val))
    print(f"Version Num: {v.version_num} | Created At (UTC): {v.created_at} | Unique Claims: {len(set(all_ids))} | Markers: {len(raw_markers)}")
db.close()
