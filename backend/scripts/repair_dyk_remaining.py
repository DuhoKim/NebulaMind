#!/usr/bin/env python3
"""Fix remaining 6 vague did_you_know entries using phi4:14b (fast)."""
import sys, os, json, urllib.request, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.page import WikiPage
from app.services.llm_utils import strip_think_blocks

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "phi4:14b"
SLUGS = ["magnetars", "milky-way", "neutron-stars", "quasars", "spacetime", "supernovae"]
FORBIDDEN = {"million", "billion", "trillion", "thousand", "hundred"}

SYSTEM = """Write 3 "Did You Know?" astronomy facts. Rules:
- SHORT (1 sentence, under 70 words each)
- SPECIFIC surprising numbers — no vague magnitudes
- FORBIDDEN: million, billion, trillion, thousand, hundred
- Return ONLY JSON array: ["fact1", "fact2", "fact3"]"""

def call(user):
    data = json.dumps({"model": MODEL, "messages": [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": user}
    ], "stream": False, "temperature": 0.3}).encode()
    req = urllib.request.Request(OLLAMA_URL, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        content = json.loads(r.read())["choices"][0]["message"]["content"]
        return strip_think_blocks(content)

def parse(raw):
    c = raw.strip()
    if c.startswith("```"): c = c.split("\n",1)[1].rsplit("```",1)[0].strip()
    m = re.search(r'\[.*\]', c, re.DOTALL)
    return json.loads(m.group() if m else c)

def ok(facts):
    if not isinstance(facts, list) or len(facts) < 2: return False
    for f in facts:
        if any(w in str(f).lower() for w in FORBIDDEN): return False
        if len(str(f).strip()) < 20: return False
    return True

db = SessionLocal()
fixed = 0
for slug in SLUGS:
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page: continue
    prompt = f"Page: {page.title}\nContent: {(page.content or '')[:1500]}\n\nWrite 3 specific Did You Know facts. Numbers only, no vague magnitudes."
    for _ in range(2):
        try:
            facts = parse(call(prompt))
            if ok(facts):
                page.did_you_know = json.dumps(facts[:3])
                db.commit()
                print(f"FIXED {slug}: {facts[0][:80]}")
                fixed += 1
                break
        except Exception as e:
            print(f"  retry {slug}: {e}")
    else:
        print(f"SKIP {slug}")
db.close()
print(f"\nDone: {fixed}/{len(SLUGS)} fixed")
