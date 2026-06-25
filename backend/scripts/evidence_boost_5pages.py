"""
Task 14: Evidence linker v2 pass on 15 new claims (3 per page × 5 pages).

Pages targeted:
  - Accretion Disks    (id=40)
  - Planetary Formation (id=50)
  - Interstellar Medium (id=37)
  - Cosmic Web          (id=55)
  - Reionization        (id=38)

These claims were added by add_claims_low_health.py (Task 13) with
trust_level='unverified' and no existing evidence — ideal targets for the
evidence linker v2 pipeline (Nutty primary, Takji fallback).

Run from the backend/ directory:
  .venv/bin/python3 scripts/evidence_boost_5pages.py
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

TARGET_PAGES = [
    (40, "Accretion Disks"),
    (50, "Planetary Formation"),
    (37, "Interstellar Medium"),
    (55, "Cosmic Web"),
    (38, "Reionization"),
]
MIN_QUALITY = 0.35
MAX_EVIDENCE_PER_CLAIM = 8


def generate_queries(claim_text: str, topic: str) -> list[str]:
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

    models = get_models("evidence_linker")  # Nutty (gpt-oss:20b) + Takji (gpt-oss:20b)
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
    from app.services.trust_calculation import recalculate_trust_v2

    existing_arxiv_ids = {
        e.arxiv_id for e in db.query(Evidence).filter(Evidence.claim_id == claim.id).all()
        if e.arxiv_id
    }
    current_count = db.query(Evidence).filter(Evidence.claim_id == claim.id).count()
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
        arxivbot = db.query(Agent).filter(Agent.name == "ArxivBot").first()
        if not arxivbot:
            print("ERROR: ArxivBot not found in DB")
            return

        grand_total = 0

        for page_id, page_name in TARGET_PAGES:
            page = db.query(WikiPage).get(page_id)
            if not page:
                print(f"WARNING: page id={page_id} ({page_name}) not found, skipping")
                continue

            # Only target new unverified claims with no existing evidence
            all_unverified = (
                db.query(Claim)
                .filter(Claim.page_id == page_id, Claim.trust_level == "unverified")
                .order_by(Claim.id.desc())
                .all()
            )
            claims = [
                c for c in all_unverified
                if db.query(Evidence).filter(Evidence.claim_id == c.id).count() == 0
            ]

            print(f"\n=== {page.title} (id={page_id}) — {len(claims)} unverified/no-evidence claims ===")
            if not claims:
                print("  Nothing to process.")
                continue

            page_total = 0
            for claim in claims:
                added = boost_claim(db, claim, page.title, arxivbot)
                page_total += added
                print(f"    -> {added} evidence added\n")

            print(f"  Page subtotal: {page_total} evidence added")
            grand_total += page_total

        print(f"\n{'='*60}")
        print(f"Task 14 complete. Grand total evidence added: {grand_total}")

    finally:
        db.close()


if __name__ == "__main__":
    main()
