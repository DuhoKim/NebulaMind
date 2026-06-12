#!/usr/bin/env python3
"""
Two tasks for galaxy-evolution (page_id=57):
  1. Prune evidence id=13679 (cosmic rays, off-topic): set quality=0.0, stance='mismatch'
  2. Re-score evidence with quality<0.5 on page_id=57 using Atom-7B
"""
import sys, re, time, httpx
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from app.database import SessionLocal
from app.models.claim import Claim, Evidence

ATOM_URL = "http://localhost:11434/v1/chat/completions"
ATOM_MODEL = "vanta-research/atom-astronomy-7b"
PAGE_ID = 57
PRUNE_ID = 13679

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
        m = re.search(r'\{.*?"score"\s*:\s*([0-9.]+)', text, re.DOTALL)
        if m:
            score = float(m.group(1))
            return max(0.0, min(1.0, score))
    except Exception as e:
        print(f"    atom error: {e}", flush=True)
    return None


def main():
    db = SessionLocal()

    # ── Task 1: Prune id=13679 ──────────────────────────────────────────────
    print(f"\n=== Task 1: Pruning evidence id={PRUNE_ID} ===", flush=True)
    ev_prune = db.query(Evidence).filter(Evidence.id == PRUNE_ID).first()
    if ev_prune:
        old_q = ev_prune.quality
        old_stance = ev_prune.stance
        ev_prune.quality = 0.0
        ev_prune.stance = "mismatch"
        db.add(ev_prune)
        db.commit()
        print(f"  ✅ id={PRUNE_ID} updated: quality {old_q} → 0.0, stance '{old_stance}' → 'mismatch'", flush=True)
    else:
        print(f"  ⚠️  id={PRUNE_ID} not found in DB", flush=True)

    # ── Task 2: Re-score quality<0.5 on page_id=57 ─────────────────────────
    print(f"\n=== Task 2: Re-scoring low-quality evidence on page_id={PAGE_ID} ===", flush=True)

    rows = (
        db.query(Evidence, Claim)
        .join(Claim, Evidence.claim_id == Claim.id)
        .filter(Claim.page_id == PAGE_ID)
        .filter(Evidence.quality < 0.5)
        .filter(Evidence.id != PRUNE_ID)  # already handled above
        .all()
    )
    print(f"  Found {len(rows)} items with quality<0.5 (excluding id={PRUNE_ID})", flush=True)

    improved = 0
    skipped = 0
    results = []

    for i, (ev, claim) in enumerate(rows):
        if not ev.title and not ev.summary and not ev.abstract:
            skipped += 1
            print(f"  [{i+1}/{len(rows)}] ev_id={ev.id} — skipped (no text)", flush=True)
            continue

        print(f"  [{i+1}/{len(rows)}] ev_id={ev.id} q={ev.quality:.2f} '{(ev.title or '')[:50]}'", flush=True)
        score = call_atom(claim.text, ev)

        if score is not None:
            old_q = ev.quality
            ev.quality = score
            db.add(ev)
            db.commit()
            above = score > 0.5
            if above:
                improved += 1
            results.append((ev.id, old_q, score, above))
            print(f"    → {old_q:.2f} → {score:.2f} {'↑ above 0.5' if above else ''}", flush=True)
        else:
            skipped += 1

        time.sleep(0.5)

    db.commit()
    db.close()

    print(f"\n=== Summary ===", flush=True)
    print(f"  Task 1: id={PRUNE_ID} → quality=0.0, stance=mismatch", flush=True)
    print(f"  Task 2: {len(rows)} items scored, {improved} improved above 0.5, {skipped} skipped", flush=True)
    if results:
        print(f"\n  Score details:", flush=True)
        for ev_id, old_q, new_q, above in results:
            print(f"    ev_id={ev_id}: {old_q:.2f} → {new_q:.2f} {'✓' if above else '✗'}", flush=True)


if __name__ == "__main__":
    main()
