import sys
import re
from sqlalchemy import func
from app.database import SessionLocal
from app.models.page import WikiPage
import app.models.agent
from app.models.page import PageVersion
from app.agent_loop.autowiki.tasks import sonnet_section_rewrite

def run_pass():
    db = SessionLocal()
    page = db.query(WikiPage).filter(WikiPage.id == 57).first()
    
    # Run 6 more times to get through the rest of the 9 sections
    for i in range(6):
        res = sonnet_section_rewrite(page_id=57)
        print(f"Rewrite loop {i+1} result: {res}")

    page = db.query(WikiPage).filter(WikiPage.id == 57).first()
    final_markers = len(re.findall(r"<!--claim:\d+-->", page.content))
    print(f"Final visible markers: {final_markers}")
    
    db.close()

if __name__ == "__main__":
    run_pass()
