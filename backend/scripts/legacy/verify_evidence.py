"""Verify evidence entries: check arXiv IDs exist, remove fake papers."""
import json
import re
import time
import urllib.request
import xml.etree.ElementTree as ET

from app.database import SessionLocal
from app.models.claim import Claim, Evidence

ARXIV_API = "http://export.arxiv.org/api/query?id_list={}"


def verify_arxiv_id(arxiv_id: str) -> dict | None:
    """Check if arXiv ID exists and return metadata."""
    if not arxiv_id:
        return None
    
    clean_id = arxiv_id.replace("arXiv:", "").strip()
    url = ARXIV_API.format(clean_id)
    
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read().decode()
        
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        root = ET.fromstring(data)
        entries = root.findall("atom:entry", ns)
        
        if not entries:
            return None
        
        entry = entries[0]
        title_el = entry.find("atom:title", ns)
        if title_el is None:
            return None
        
        title = title_el.text.strip().replace("\n", " ") if title_el.text else ""
        
        # Check if it's an error response
        if "Error" in title or not title:
            return None
        
        return {"title": title, "arxiv_id": clean_id}
    except Exception:
        return None


def run_verification():
    db = SessionLocal()
    try:
        evidences = db.query(Evidence).all()
        total = len(evidences)
        verified = 0
        removed = 0
        no_arxiv = 0
        errors = 0
        
        print(f"Verifying {total} evidence entries...")
        
        for i, ev in enumerate(evidences):
            if not ev.arxiv_id:
                no_arxiv += 1
                continue
            
            result = verify_arxiv_id(ev.arxiv_id)
            
            if result is None:
                # Fake paper — delete
                db.delete(ev)
                removed += 1
                print(f"  [{i+1}/{total}] REMOVED: {ev.arxiv_id} — {ev.title[:60]}")
            else:
                verified += 1
                if i % 50 == 0:
                    print(f"  [{i+1}/{total}] OK: {ev.arxiv_id}")
            
            # Rate limit: arXiv asks for 3 second delay
            time.sleep(3)
        
        db.commit()
        
        # Recalculate trust levels for claims that lost evidence
        claims_to_update = db.query(Claim).filter(Claim.trust_level == "accepted").all()
        downgraded = 0
        for claim in claims_to_update:
            ev_count = db.query(Evidence).filter(Evidence.claim_id == claim.id).count()
            if ev_count == 0:
                claim.trust_level = "unverified"
                downgraded += 1
        db.commit()
        
        print(f"\n=== Verification Complete ===")
        print(f"Total: {total}")
        print(f"Verified: {verified}")
        print(f"Removed (fake): {removed}")
        print(f"No arXiv ID: {no_arxiv}")
        print(f"Claims downgraded to unverified: {downgraded}")
        
    finally:
        db.close()


if __name__ == "__main__":
    run_verification()
