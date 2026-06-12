import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.page import WikiPage
import re

db = SessionLocal()
p = db.query(WikiPage).get(57)
if p:
    raw_markers = re.findall(r"<!--claim:([\d,\s]+)\s*-->", p.content)
    all_ids = []
    for r in raw_markers:
        for val in r.split(","):
            val = val.strip()
            if val:
                all_ids.append(int(val))
    
    print("Found Raw Markers:", raw_markers)
    print("Unique Claim IDs:", sorted(list(set(all_ids))))
    print("Total Unique Claim IDs count:", len(set(all_ids)))
    print("Total Raw Markers count:", len(raw_markers))
else:
    print("Page not found")
db.close()
