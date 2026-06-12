import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.agent_loop.marker_embed.pipeline import run_pipeline
from app.models.page import WikiPage
from sqlalchemy import text

db = SessionLocal()
page = db.query(WikiPage).get(57)

# just to see what the pipeline does
res, stats = run_pipeline(page.id, page.content, [], dry_run=True)
print(stats)
