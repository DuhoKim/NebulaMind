#!/usr/bin/env python3
"""
Nutty (gpt-oss:20b) claim booster.
Generates new claims for sparse pages (<10 claims).
Target pages: fast-radio-bursts, nebulae, binary-stars, gamma-ray-bursts, exoplanet-detection-methods

Run: python3 nutty_claim_boost.py
"""
import sys, json, time, re
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

import httpx
from app.database import SessionLocal
from app.models.page import WikiPage
from app.models.claim import Claim
from app.models.agent import Agent
from app.services.llm_utils import strip_think_blocks
from sqlalchemy import func

NUTTY_URL = "http://localhost:11434/v1/chat/completions"
NUTTY_MODEL = "gpt-oss:20b"

TARGET_SLUGS = [
    "fast-radio-bursts", "nebulae", "binary-stars",
    "gamma-ray-bursts", "exoplanet-detection-methods"
]
CLAIMS_PER_PAGE = 3

PROMPT = """You are an astronomy knowledge engineer. Generate {n} new factual claims for a wiki page about {topic}.

Existing claims (do not duplicate):
{existing}

Page content summary:
{content}

Generate {n} NEW claims that:
- Are specific, verifiable, quantitative where possible
- Cover different aspects not already mentioned
- Are suitable for a professional astronomy wiki
- Cite real findings from the last 5 years when possible

Return a JSON array of claim objects:
[
  {{
    "text": "claim text here (1-2 sentences, specific and factual)",
    "claim_type": "established",
    "section": "## Overview",
    "connector": "Furthermore"
  }}
]
Return ONLY the JSON array, no other text."""


def strip_think(text: str) -> str:
    return strip_think_blocks(text)


def call_nutty(topic: str, existing_claims: list[str], content: str, n: int = 3) -> list[dict]:
    existing_str = "\n".join(f"- {c}" for c in existing_claims[:10])
    prompt = PROMPT.format(
        n=n, topic=topic,
        existing=existing_str or "(none yet)",
        content=content[:800],
    )
    try:
        resp = httpx.post(NUTTY_URL, json={
            "model": NUTTY_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
        }, timeout=90)
        resp.raise_for_status()
        text = strip_think(resp.json()["choices"][0]["message"]["content"])
        # Extract JSON array
        m = re.search(r'\[.*\]', text, re.DOTALL)
        if m:
            return json.loads(m.group())
    except Exception as e:
        print(f"  nutty error: {e}", flush=True)
    return []


def get_or_find_agent(db) -> int:
    agent = db.query(Agent).filter(Agent.name == "Nutty").first()
    if not agent:
        agent = db.query(Agent).filter(Agent.model_name == "gpt-oss:20b").first()
    if not agent:
        agent = db.query(Agent).first()
    return agent.id if agent else None


def main():
    db = SessionLocal()
    agent_id = get_or_find_agent(db)

    for slug in TARGET_SLUGS:
        page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
        if not page:
            print(f"  Page {slug} not found, skipping", flush=True)
            continue

        existing_claims = db.query(Claim).filter(Claim.page_id == page.id).all()
        existing_texts = [c.text for c in existing_claims]
        current_count = len(existing_texts)

        print(f"\n[{page.title}] health={page.health_score} claims={current_count}", flush=True)

        new_claims = call_nutty(
            page.title,
            existing_texts,
            page.content or page.summary or "",
            n=CLAIMS_PER_PAGE,
        )

        if not new_claims:
            print(f"  ✗ No claims generated", flush=True)
            continue

        added = 0
        for i, claim_data in enumerate(new_claims):
            if not isinstance(claim_data, dict) or not claim_data.get("text"):
                continue
            claim = Claim(
                page_id=page.id,
                text=claim_data["text"],
                claim_type=claim_data.get("claim_type", "established"),
                section=claim_data.get("section", "## Overview"),
                connector=claim_data.get("connector", "Furthermore"),
                created_by_agent_id=agent_id,
                order_idx=current_count + i,
            )
            db.add(claim)
            added += 1
            print(f"  + claim: {claim_data['text'][:70]}...", flush=True)

        db.commit()
        print(f"  ✓ Added {added} claims to {page.title}", flush=True)
        time.sleep(2)

    db.close()
    print("\n✅ Nutty claim boost complete.", flush=True)


if __name__ == "__main__":
    main()
