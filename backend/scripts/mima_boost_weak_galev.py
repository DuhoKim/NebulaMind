#!/usr/bin/env python3
"""Boost galaxy-evolution claims with ev=2 using Mima (qwen3.6:35b-a3b-nvfp4). Add 2 arXiv evidence rows each."""
import sys, json, time, re
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')
import httpx
from app.database import SessionLocal
from app.models.claim import Claim, Evidence
from app.services.llm_utils import strip_think_blocks
from sqlalchemy import func

MIMA_URL = "http://localhost:11434/v1/chat/completions"
MIMA_MODEL = "qwen3.6:35b-a3b-nvfp4"
PAGE_ID = 57
LOG = "/Users/duhokim/NebulaMind/logs/mima_galev_weak_boost.log"

PROMPT = """You are an astronomy literature expert. For this galaxy evolution claim, suggest 3 real arXiv papers that directly support or contextualize it.

Claim: {claim_text}

Rules:
- Only suggest papers you are CONFIDENT exist (real arXiv IDs)
- Format: YYMM.NNNNN or YYYY.NNNNN
- Papers must be peer-reviewed astronomy/astrophysics
- Must directly address the specific claim

Return JSON only (no markdown, no explanation):
[{{"arxiv_id": "2301.12345", "stance": "supports", "title": "paper title", "year": 2023}}]"""

def call_mima(claim_text):
    try:
        prompt = PROMPT.format(claim_text=claim_text)
        resp = httpx.post(MIMA_URL, json={
            "model": MIMA_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1,
        }, timeout=120)
        resp.raise_for_status()
        text = resp.json()["choices"][0]["message"]["content"]
        text = strip_think_blocks(text)
        m = re.search(r'\[.*\]', text, re.DOTALL)
        if m:
            return json.loads(m.group())
    except Exception as e:
        log(f"  mima error: {e}")
    return []

def log(msg):
    print(msg, flush=True)
    with open(LOG, 'a') as f:
        f.write(msg + "\n")

def main():
    with open(LOG, 'w') as f:
        f.write("Galaxy-evolution weak claim boost (ev<=2)\n\n")

    db = SessionLocal()
    claims = db.query(Claim).filter(Claim.page_id==PAGE_ID).all()
    ev_counts = dict(db.query(Evidence.claim_id, func.count(Evidence.id)).filter(
        Evidence.claim_id.in_([c.id for c in claims])
    ).group_by(Evidence.claim_id).all())

    weak = [c for c in claims if ev_counts.get(c.id, 0) <= 2]
    log(f"Found {len(weak)} claims with ev<=2\n")

    total_inserted = 0
    for c in weak:
        existing_arxiv = {e.arxiv_id for e in db.query(Evidence).filter(Evidence.claim_id == c.id).all()}
        log(f"claim:{c.id} (ev={len(existing_arxiv)}): {c.text[:70]}")

        suggestions = call_mima(c.text)
        added = 0
        for s in suggestions[:2]:
            arxiv_id = s.get("arxiv_id", "").strip()
            if not arxiv_id or arxiv_id in existing_arxiv:
                continue
            ev = Evidence(
                claim_id=c.id,
                arxiv_id=arxiv_id,
                title=s.get("title", ""),
                year=s.get("year"),
                stance=s.get("stance", "supports"),
                quality=0.5,
                source_channel="mima-galev-boost",
                arxiv_verified=False,
            )
            db.add(ev)
            existing_arxiv.add(arxiv_id)
            added += 1
            total_inserted += 1
            log(f"  + {arxiv_id}: {s.get('title','')[:60]}")

        db.commit()
        log(f"  done: +{added} evidence rows\n")
        time.sleep(2)

    db.close()
    log(f"Complete. {total_inserted} evidence rows inserted across {len(weak)} claims.")

if __name__ == "__main__":
    main()
