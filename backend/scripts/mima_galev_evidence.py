#!/usr/bin/env python3
"""Mima (qwen3.6:35b-a3b-nvfp4) evidence linker — galaxy-evolution weak claims only."""
import sys, json, time, re
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')
import httpx
from app.database import SessionLocal
from app.models.claim import Claim, Evidence
from app.services.llm_utils import strip_think_blocks

MIMA_URL = "http://localhost:11434/v1/chat/completions"
MIMA_MODEL = "qwen3.6:35b-a3b-nvfp4"
# Weakest galaxy-evolution claims by evidence count
WEAK_CLAIM_IDS = [1495, 1496, 1512]

PROMPT = """You are an astronomy literature expert. For this galaxy evolution claim, suggest 3 real arXiv papers that directly support it.

Claim: {claim_text}

Rules:
- Only suggest papers you are CONFIDENT exist (real arXiv IDs)
- Format: YYMM.NNNNN or YYYY.NNNNN
- Papers must be peer-reviewed astronomy/astrophysics
- Must directly support the specific claim, not just be related

Return JSON only:
[{{"arxiv_id": "2301.12345", "stance": "supports", "title": "paper title", "year": 2023}}]"""

def call_mima(claim_text: str) -> list[dict]:
    try:
        resp = httpx.post(MIMA_URL, json={
            "model": MIMA_MODEL,
            "messages": [{"role": "user", "content": PROMPT.format(claim_text=claim_text)}],
            "temperature": 0.1,
        }, timeout=60)
        resp.raise_for_status()
        text = resp.json()["choices"][0]["message"]["content"]
        # strip think tags
        text = strip_think_blocks(text)
        m = re.search(r'\[.*\]', text, re.DOTALL)
        if m:
            return json.loads(m.group())
    except Exception as e:
        print(f"  mima error: {e}", flush=True)
    return []

def main():
    db = SessionLocal()
    for claim_id in WEAK_CLAIM_IDS:
        claim = db.query(Claim).filter(Claim.id == claim_id).first()
        if not claim:
            continue
        existing_arxiv = {e.arxiv_id for e in db.query(Evidence).filter(Evidence.claim_id == claim_id).all()}
        print(f"\nclaim:{claim_id} (ev={len(existing_arxiv)}): {claim.text[:70]}", flush=True)
        
        suggestions = call_mima(claim.text)
        added = 0
        for s in suggestions:
            arxiv_id = s.get("arxiv_id", "").strip()
            if not arxiv_id or arxiv_id in existing_arxiv:
                continue
            ev = Evidence(
                claim_id=claim_id,
                arxiv_id=arxiv_id,
                title=s.get("title", ""),
                year=s.get("year"),
                stance=s.get("stance", "supports"),
                quality=0.5,
                source_channel="mima-galev",
                arxiv_verified=False,
            )
            db.add(ev)
            existing_arxiv.add(arxiv_id)
            added += 1
            print(f"  + {arxiv_id}: {s.get('title','')[:50]}", flush=True)
        db.commit()
        print(f"  ✓ Added {added} evidence items", flush=True)
        time.sleep(2)
    db.close()
    print("\n✅ Mima galaxy-evolution evidence linking complete.", flush=True)

if __name__ == "__main__":
    main()
