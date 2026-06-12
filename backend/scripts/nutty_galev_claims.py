#!/usr/bin/env python3
"""Nutty (gpt-oss:20b) — generate new claims for galaxy-evolution targeting judge weak spots."""
import sys, json, time, re
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')
import httpx
from app.database import SessionLocal
from app.models.page import WikiPage
from app.models.claim import Claim
from app.models.agent import Agent
from app.services.llm_utils import strip_think_blocks

NUTTY_URL = "http://localhost:11434/v1/chat/completions"
NUTTY_MODEL = "gpt-oss:20b"
PAGE_ID = 57

PROMPT = """You are an astronomy knowledge engineer. Generate 5 new specific claims for a galaxy evolution wiki page.

The judge flagged these weaknesses:
1. JWST/DESI frontier mentioned but superficial — need claims with specific observational results
2. Open questions named but not interrogated — need claims about what evidence exists for each side
3. Citations not all top-tier — need claims referencing Nature/ApJ/A&A results 2022-2025

Existing claim topics (do NOT duplicate):
{existing}

Generate 5 NEW claims. Each must:
- Be specific and quantitative (include redshifts, masses, percentages, timescales)
- Reference a real finding from 2020-2025
- Cover JWST discoveries, DESI results, or quenching mechanisms specifically

Return JSON array:
[{{"text": "...", "claim_type": "established", "section": "## Current Surveys & Missions", "connector": "Notably"}}]"""

def strip_think(text):
    return strip_think_blocks(text)

def main():
    db = SessionLocal()
    page = db.query(WikiPage).filter(WikiPage.id == PAGE_ID).first()
    existing = db.query(Claim).filter(Claim.page_id == PAGE_ID).all()
    existing_texts = [c.text[:80] for c in existing]
    agent = db.query(Agent).filter(Agent.model_name == "gpt-oss:20b").first()
    if not agent: agent = db.query(Agent).first()

    print(f"galaxy-evolution: {len(existing)} existing claims → generating 5 more", flush=True)
    try:
        resp = httpx.post(NUTTY_URL, json={
            "model": NUTTY_MODEL,
            "messages": [{"role": "user", "content": PROMPT.format(existing="\n".join(f"- {t}" for t in existing_texts))}],
            "temperature": 0.4,
        }, timeout=120)
        resp.raise_for_status()
        text = strip_think(resp.json()["choices"][0]["message"]["content"])
        m = re.search(r'\[.*\]', text, re.DOTALL)
        if not m:
            print("✗ No JSON array found", flush=True)
            return
        new_claims = json.loads(m.group())
        added = 0
        for i, cd in enumerate(new_claims):
            if not cd.get("text"): continue
            c = Claim(
                page_id=PAGE_ID,
                text=cd["text"],
                claim_type=cd.get("claim_type","established"),
                section=cd.get("section","## Current Surveys & Missions"),
                connector=cd.get("connector","Furthermore"),
                created_by_agent_id=agent.id,
                order_idx=len(existing)+i,
            )
            db.add(c)
            added += 1
            print(f"  + {cd['text'][:75]}...", flush=True)
        db.commit()
        print(f"\n✅ Added {added} claims to galaxy-evolution.", flush=True)
    except Exception as e:
        print(f"✗ {e}", flush=True)
    db.close()

if __name__ == "__main__":
    main()
