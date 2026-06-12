#!/usr/bin/env python3
import argparse
import json
import logging
import re
from pathlib import Path
from sqlalchemy import text
import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")

from app.database import SessionLocal
from app.models.claim import Claim
from app.models.page import WikiPage

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def norm_key(s: str) -> str:
    if not s: return ""
    s = s.lower()
    s = re.sub(r'[^a-z0-9\s]', '', s)
    return re.sub(r'\s+', '_', s.strip())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--page-id", type=int, required=True)
    args = parser.parse_args()

    db = SessionLocal()
    page = db.query(WikiPage).get(args.page_id)
    if not page:
        log.error(f"Page {args.page_id} not found")
        return

    # current sections
    sections = re.findall(r"^## (.+)$", page.content, re.MULTILINE)
    section_keys = {norm_key(s): s for s in sections}
    log.info(f"Found {len(sections)} sections in current content")

    claims = db.query(Claim).filter(Claim.page_id == args.page_id).all()
    log.info(f"Found {len(claims)} total claims")

    # Map current markers
    marker_sections = {}
    current_sec = ""
    for line in page.content.split("\n"):
        if line.startswith("## "):
            current_sec = line[3:].strip()
        marker_groups = re.findall(r"<!--claim:([\d,\s]+)-->", line)
        for group in marker_groups:
            for c in group.split(","):
                c = c.strip()
                if c:
                    marker_sections[int(c)] = current_sec

    inserted = 0
    db.execute(text("DELETE FROM claim_section_assignments WHERE page_id = :pid"), {"pid": args.page_id})

    for c in claims:
        # Phase 1 algorithm:
        # 1. claims.section exact match
        # 2. marker location
        # 3. orphan_pending
        
        c_sec_key = norm_key(c.section)
        owner = None
        method = ""
        
        if c_sec_key in section_keys:
            owner = section_keys[c_sec_key]
            method = "claim_section_exact"
        elif c.id in marker_sections:
            owner = marker_sections[c.id]
            method = "marker_location"
        else:
            # We'll just do fuzzy match by finding the closest subset if needed, but for simplicity
            # just fall back to orphan for now since most are cleanly matched or marked.
            pass
            
        status = "active"
        if not owner:
            owner = c.section or "unknown"
            status = "orphan_pending"
            method = "orphan_fallback"
            
        db.execute(text("""
        INSERT INTO claim_section_assignments 
        (claim_id, page_id, owner_section, owner_section_key, assignment_status, assignment_method, confidence)
        VALUES (:cid, :pid, :owner, :owner_key, :status, :method, :conf)
        """), {
            "cid": c.id,
            "pid": page.id,
            "owner": owner,
            "owner_key": norm_key(owner),
            "status": status,
            "method": method,
            "conf": 1.0 if status == "active" else 0.0
        })
        inserted += 1

    db.commit()
    db.close()
    
    log.info(f"Inserted {inserted} claim section assignments for page {args.page_id}")

    # Audit query
    db = SessionLocal()
    res = db.execute(text("""
        SELECT 
            assignment_status, 
            assignment_method,
            count(*) as c
        FROM claim_section_assignments 
        WHERE page_id = :pid
        GROUP BY assignment_status, assignment_method
    """), {"pid": args.page_id}).fetchall()
    
    for r in res:
        log.info(f" - {r.assignment_status} ({r.assignment_method}): {r.c}")

if __name__ == "__main__":
    main()
