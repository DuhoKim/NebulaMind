import sys
import re
from sqlalchemy import text
from app.database import SessionLocal
from app.models.page import WikiPage
from app.agent_loop.autowiki.tasks import sonnet_section_rewrite

def run():
    db = SessionLocal()
    # Reset quality scores temporarily so it will rewrite everything
    from app.models.autowiki import AutowikiRun
    runs = db.query(AutowikiRun).filter(AutowikiRun.page_id == 57).all()
    for r in runs:
        if r.q1 and r.q1 >= 0.85:
            r.q1 = 0.80
    db.commit()
    db.close()
    
    res = sonnet_section_rewrite(page_id=57)
    print(f"Result: {res}")

if __name__ == "__main__":
    run()
