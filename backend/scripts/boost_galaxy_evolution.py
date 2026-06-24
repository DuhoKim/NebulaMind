"""
Targeted evidence boost for galaxy-evolution claims 1487-1496.

These 10 claims were added after the last biblio mine (May 5) so they only
have 3 evidence each (all debated). This script:
  1. Uses Nutty/Mima (via evidence_linker routing) to generate ADS queries
  2. Searches ADS + S2 for supporting/challenging papers
  3. Verifies quality and inserts up to EVIDENCE_INSERTS_PER_RUN per claim
  4. Recalculates trust after insertions
  5. Also resets wiki_biblio_mined_at so the nightly task can re-mine

Run from the backend/ directory:
  .venv/bin/python3 scripts/boost_galaxy_evolution.py
"""
from __future__ import annotations

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime as _dt

from app.database import SessionLocal
from app.models.claim import Claim, Evidence
from app.models.page import WikiPage
from app.models.agent import Agent
from app.services.paper_search import search_papers, verify_for_claim
from app.config import settings

PAGE_ID = 57
TARGET_CLAIMS = list(range(1487, 1497))  # 1487-1496
MIN_QUALITY = 0.35  # lower bar than normal — these are debated claims
MAX_EVIDENCE_PER_CLAIM = 8


def generate_queries(claim_text: str, topic: str) -> list[str]:
    """Generate ADS search queries using Nutty/Mima via routing table."""
    from app.agent_loop.tasks import _chat_parallel
    from app.services.llm_routing.routing import get_models

    sys_prompt = (
        "You translate scientific claims into 1-2 ADS-style search queries. "
        "Return ONLY a JSON array of strings. No prose. "
        "Use astronomy terminology, key physical quantities, and proper nouns. "
        "Do NOT invent specific arXiv IDs."
    )
    user_msg = (
        f'Topic: "{topic}"\nClaim: "{claim_text}"\n\n'
        f'Generate 1-2 search queries optimized for ADS that would find papers '
        f'either supporting or challenging this claim.'
    )

    models = get_models("evidence_linker")  # Nutty + Takji primary
    proposals = _chat_parallel(models, sys_prompt, user_msg, timeout=60)

    queries: list[str] = []
    for p in (proposals or []):
        try:
            cleaned = p["response"].strip()
            if cleaned.startswith("```"):
                cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0]
            arr = json.loads(cleaned)
            for q in (arr if isinstance(arr, list) else [arr]):
                if isinstance(q, str) and 5 < len(q) < 250:
                    queries.append(q)
        except Exception:
            continue

    if not queries:
        queries = [f'"{topic}" {claim_text[:80]}']

    return list(dict.fromkeys(queries))[:6]


def boost_claim(db, claim: Claim, page_title: str, arxivbot: Agent) -> int:
    """Search for evidence for a single claim. Returns number inserted."""
    from app.services.trust_calculation import recalculate_trust_v2

    existing_arxiv_ids = {
        e.arxiv_id for e in db.query(Evidence).filter(Evidence.claim_id == claim.id).all()
        if e.arxiv_id
    }
    current_count = len(existing_arxiv_ids)
    if current_count >= MAX_EVIDENCE_PER_CLAIM:
        print(f"  Claim {claim.id}: already has {current_count} evidence, skipping")
        return 0

    print(f"  Claim {claim.id} ({current_count} ev): {claim.text[:70]}...")
    queries = generate_queries(claim.text, page_title)
    print(f"    Queries: {queries}")

    all_records = []
    for q in queries:
        try:
            all_records.extend(search_papers(q, rows=6))
        except Exception as e:
            print(f"    search failed '{q[:40]}': {e}")

    seen: set[str] = set()
    unique = []
    for r in all_records:
        key = r.arxiv_id or r.doi or r.title.lower().strip()
        if key and key not in seen and (not r.arxiv_id or r.arxiv_id not in existing_arxiv_ids):
            seen.add(key)
            unique.append(r)

    verified = []
    for rec in unique[:15]:
        v = verify_for_claim(rec, claim.text, s2_cross_check=bool(rec.doi))
        if v and v.quality >= MIN_QUALITY:
            verified.append(v)
    verified.sort(key=lambda x: x.quality, reverse=True)

    added = 0
    for v in verified[:(MAX_EVIDENCE_PER_CLAIM - current_count)]:
        ed = v.record.to_evidence_dict()
        dup = db.query(Evidence).filter(
            Evidence.claim_id == claim.id,
            Evidence.arxiv_id == ed["arxiv_id"],
        ).first() if ed["arxiv_id"] else None
        if dup:
            continue

        ev = Evidence(
            claim_id=claim.id,
            arxiv_id=ed["arxiv_id"],
            doi=ed["doi"],
            url=ed["url"],
            title=ed["title"],
            authors=ed["authors"],
            year=ed["year"],
            summary=None,
            stance=v.stance_hint or "supports",
            added_by_agent_id=arxivbot.id,
            quality=v.quality,
            abstract=ed["abstract"],
            ads_bibcode=ed["ads_bibcode"],
            s2_paper_id=ed["s2_paper_id"],
            verified_at=_dt.utcnow(),
            arxiv_verified=bool(ed["arxiv_id"]),
            source_channel="evidence_boost",
        )
        db.add(ev)
        db.flush()
        added += 1
        print(f"    + [{ed['arxiv_id'] or ed['doi']}] {ed['title'][:60]} (q={v.quality:.2f})")

    if added:
        db.commit()
        try:
            recalculate_trust_v2(claim.id, db, trigger="evidence_boost", actor_agent_id=arxivbot.id)
            db.commit()
        except Exception as e:
            print(f"    trust recalc failed: {e}")

    return added


def main():
    db = SessionLocal()
    try:
        page = db.query(WikiPage).get(PAGE_ID)
        print(f"Page: {page.title} (id={PAGE_ID})")
        print(f"Last biblio mine: {page.wiki_biblio_mined_at}")

        arxivbot = db.query(Agent).filter(Agent.name == "ArxivBot").first()
        if not arxivbot:
            print("ERROR: ArxivBot not found")
            return

        claims = (
            db.query(Claim)
            .filter(Claim.page_id == PAGE_ID, Claim.id.in_(TARGET_CLAIMS))
            .order_by(Claim.id)
            .all()
        )
        print(f"Target claims: {[c.id for c in claims]}")
        print()

        total_added = 0
        for claim in claims:
            added = boost_claim(db, claim, page.title, arxivbot)
            total_added += added
            print(f"    -> {added} evidence added")
            print()

        # Reset biblio mined timestamp so nightly task can re-run
        page.wiki_biblio_mined_at = None
        db.commit()
        print(f"Reset wiki_biblio_mined_at for page {PAGE_ID}")
        print(f"\nDone. Total evidence added: {total_added}")

    finally:
        db.close()


if __name__ == "__main__":
    main()
