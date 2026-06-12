#!/usr/bin/env python3
"""
Atom-7B batch evidence quality scorer.
Scores evidence with quality=None or quality<0.5 using vanta-research/atom-astronomy-7b.
Updates evidence.quality in-place.

Run: python3 atom_score_evidence.py [--limit N]
"""
import sys, json, time, re
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

import httpx
from sqlalchemy import or_
from app.database import SessionLocal
from app.models.claim import Claim, Evidence

ATOM_URL = "http://localhost:11434/v1/chat/completions"
ATOM_MODEL = "vanta-research/atom-astronomy-7b"
BATCH_SIZE = 50
LIMIT = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[1] == "--limit" else 400

SCORE_PROMPT = """You are an astronomy evidence quality scorer. Score the relevance and quality of this evidence item for its associated claim.

Claim: {claim_text}

Evidence:
- Title: {title}
- arXiv: {arxiv_id}
- Year: {year}
- Summary: {summary}

Score from 0.0 to 1.0 where:
- 1.0 = directly supports/refutes the claim with clear methodology
- 0.7-0.9 = strongly relevant, good source
- 0.4-0.6 = partially relevant or indirect
- 0.1-0.3 = tangentially related
- 0.0 = irrelevant or not a real paper

Return ONLY a JSON object: {{"score": 0.XX, "reason": "one sentence"}}"""


def call_atom(claim_text: str, ev: Evidence, timeout: int = 30) -> float | None:
    prompt = SCORE_PROMPT.format(
        claim_text=claim_text[:300],
        title=ev.title or "Unknown",
        arxiv_id=ev.arxiv_id or "N/A",
        year=ev.year or "N/A",
        summary=(ev.summary or ev.abstract or "No summary available")[:300],
    )
    try:
        resp = httpx.post(
            ATOM_URL,
            json={
                "model": ATOM_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.0,
            },
            timeout=timeout,
        )
        resp.raise_for_status()
        text = resp.json()["choices"][0]["message"]["content"].strip()
        # Extract JSON
        m = re.search(r'\{.*?"score"\s*:\s*([0-9.]+)', text, re.DOTALL)
        if m:
            score = float(m.group(1))
            return max(0.0, min(1.0, score))
    except Exception as e:
        print(f"    atom error: {e}", flush=True)
    return None


def main():
    db = SessionLocal()
    
    # Fetch low-quality evidence with their claims
    query = db.query(Evidence, Claim).join(
        Claim, Evidence.claim_id == Claim.id
    ).filter(
        or_(Evidence.quality == None, Evidence.quality < 0.5)
    ).limit(LIMIT)
    
    rows = query.all()
    print(f"Scoring {len(rows)} low-quality evidence items with Atom-7B...", flush=True)
    
    updated = 0
    skipped = 0
    
    for i, (ev, claim) in enumerate(rows):
        if not ev.title and not ev.summary and not ev.abstract:
            skipped += 1
            continue
        
        print(f"  [{i+1}/{len(rows)}] ev_id={ev.id} claim_id={ev.claim_id} '{(ev.title or '')[:40]}'", flush=True)
        
        score = call_atom(claim.text, ev)
        if score is not None:
            old_q = ev.quality
            ev.quality = score
            db.add(ev)
            if (i + 1) % 10 == 0:
                db.commit()
                print(f"    → committed batch (last: {old_q:.2f} → {score:.2f})", flush=True)
            updated += 1
        else:
            skipped += 1
        
        time.sleep(0.5)  # small pause between calls
    
    db.commit()
    db.close()
    
    print(f"\n✅ Atom-7B scoring complete: {updated} updated, {skipped} skipped", flush=True)


if __name__ == "__main__":
    main()
