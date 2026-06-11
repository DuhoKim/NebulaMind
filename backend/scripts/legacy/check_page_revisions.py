import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.page import WikiPage, PageVersion
import re

db = SessionLocal()
versions = db.query(PageVersion).filter(PageVersion.page_id == 57).order_by(PageVersion.version_num.desc()).limit(15).all()

print("--- LATEST Page Versions for Page 57 ---")
for v in versions:
    markers = re.findall(r"<!--claim:(\d+)\s*-->", v.content)
    print(f"Version: {v.version_num} | Created At: {v.created_at} | Agent ID: {v.editor_agent_id} | Unique Markers: {len(set(markers))} | Total Markers: {len(markers)}")

db.close()
