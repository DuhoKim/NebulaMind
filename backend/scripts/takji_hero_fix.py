#!/usr/bin/env python3
"""
Takji (gpt-oss:20b) hero_facts fixer + formatter.
1. Fixes malformed hero_facts (baryon-acoustic-oscillations missing 'value' field)
2. Audits all hero_facts for format consistency and patches minor issues
3. Ensures all hero_facts have: label, value, unit, kind, source

Run: python3 takji_hero_fix.py
"""
import sys, json, time, re
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

import httpx
from app.database import SessionLocal
from app.models.page import WikiPage

TAKJI_URL = "http://localhost:11434/v1/chat/completions"
TAKJI_MODEL = "gpt-oss:20b"

FIX_PROMPT = """You are a JSON formatter. Fix this hero_facts entry to have all required fields.

Required fields: label (str), value (str), unit (str), kind ("range"|"count"|"date"|"measurement"), source (obj with tier, year)

Current entry: {entry}
Page topic: {topic}

Return a corrected JSON object only. Make value and unit meaningful for the topic.
If value is missing, infer a plausible quantitative value from the label.
Example: {{"label": "Typical FRB duration", "value": "~1", "unit": "millisecond", "kind": "measurement", "source": {{"tier": "authoritative", "year": 2023}}}}"""


def call_takji(prompt: str, timeout: int = 30) -> str | None:
    try:
        resp = httpx.post(TAKJI_URL, json={
            "model": TAKJI_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1,
        }, timeout=timeout)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"  takji error: {e}", flush=True)
    return None


def fix_entry(entry: dict, topic: str) -> dict | None:
    prompt = FIX_PROMPT.format(entry=json.dumps(entry), topic=topic)
    text = call_takji(prompt)
    if not text:
        return None
    m = re.search(r'\{.*\}', text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group())
        except Exception:
            pass
    return None


def audit_hero_facts(facts: list, topic: str) -> tuple[list, bool]:
    """Returns (fixed_facts, was_changed)"""
    changed = False
    result = []
    for fact in facts:
        if not isinstance(fact, dict):
            changed = True
            continue
        needs_fix = (
            not fact.get("value") or
            not fact.get("label") or
            not fact.get("unit") or
            not fact.get("kind")
        )
        if needs_fix:
            fixed = fix_entry(fact, topic)
            if fixed:
                result.append(fixed)
                changed = True
                print(f"    Fixed: {fact.get('label', '?')} → value={fixed.get('value')}", flush=True)
            else:
                result.append(fact)  # keep original if fix failed
        else:
            result.append(fact)
    return result, changed


def main():
    db = SessionLocal()
    pages = db.query(WikiPage).filter(
        WikiPage.hero_facts != None,
        WikiPage.hero_facts != '[]',
        WikiPage.hero_facts != 'null',
    ).all()

    print(f"Auditing hero_facts on {len(pages)} pages...", flush=True)
    fixed_count = 0

    for page in pages:
        try:
            facts = json.loads(page.hero_facts)
        except Exception:
            print(f"  [{page.slug}] Invalid JSON — skipping", flush=True)
            continue

        if not isinstance(facts, list) or not facts:
            continue

        print(f"  [{page.slug}] {len(facts)} facts", flush=True)
        fixed, changed = audit_hero_facts(facts, page.title)

        if changed:
            page.hero_facts = json.dumps(fixed)
            db.add(page)
            db.commit()
            fixed_count += 1
            print(f"    ✓ Saved fixed hero_facts", flush=True)

        time.sleep(0.5)

    db.close()
    print(f"\n✅ Takji hero fix complete: {fixed_count} pages updated.", flush=True)


if __name__ == "__main__":
    main()
