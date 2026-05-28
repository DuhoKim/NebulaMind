#!/usr/bin/env python3
"""Add hero_tagline, hero_facts, did_you_know, category to the 8 Group-B bare pages."""
import sys, os, json, urllib.request, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.page import WikiPage
from app.services.llm_utils import strip_think_blocks

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "phi4:14b"

FORBIDDEN = {"millions", "billions", "trillions", "thousands", "hundreds", "million", "billion"}

SLUGS = [
    "accretion-disks", "baryon-acoustic-oscillations", "cosmic-web",
    "gravitational-lensing", "interstellar-medium", "planetary-formation",
    "red-giants", "reionization",
]

CATEGORIES = {
    "accretion-disks": "stellar",
    "baryon-acoustic-oscillations": "cosmology",
    "cosmic-web": "cosmology",
    "gravitational-lensing": "observational",
    "interstellar-medium": "observational",
    "planetary-formation": "stellar",
    "red-giants": "stellar",
    "reionization": "cosmology",
}

SYSTEM = """You are an astronomy wiki editor. Generate metadata for a wiki page.

Return ONLY a JSON object:
{
  "tagline": "<compelling 1-sentence description, ~100 chars>",
  "facts": [
    {"label": "<2-3 word label>", "value": "<specific number or range>", "unit": "<unit>"},
    {"label": "<2-3 word label>", "value": "<specific number or range>", "unit": "<unit>"},
    {"label": "<2-3 word label>", "value": "<specific number or range>", "unit": "<unit>"}
  ],
  "dyk": [
    "<short surprising fact with specific number>",
    "<short surprising fact with specific number>",
    "<short surprising fact with specific number>"
  ]
}

Rules for facts:
- Values MUST be specific numbers (no "millions", "billions", "thousands", "hundreds", "million", "billion")
- Units must be real physical units
- Labels 2-3 words max

Rules for dyk:
- Each fact 1 sentence max 80 words
- FORBIDDEN: "millions", "billions", "trillions"
- Must have specific numbers"""

def call(user):
    data = json.dumps({"model": MODEL, "messages": [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": user}
    ], "stream": False, "temperature": 0.2}).encode()
    req = urllib.request.Request(OLLAMA_URL, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        content = json.loads(r.read())["choices"][0]["message"]["content"]
        return strip_think_blocks(content)

def parse(raw):
    c = raw.strip()
    if c.startswith("```"): c = c.split("\n",1)[1].rsplit("```",1)[0].strip()
    start = c.find("{"); end = c.rfind("}")
    return json.loads(c[start:end+1]) if start >= 0 else json.loads(c)

def is_valid_facts(facts):
    for f in facts:
        v = str(f.get("value","")).lower()
        if any(w in v for w in FORBIDDEN): return False
        if not f.get("label") or not str(f.get("value","")).strip(): return False
    return len(facts) == 3

db = SessionLocal()
fixed = 0
for slug in SLUGS:
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if not page:
        print(f"SKIP {slug}: not found")
        continue

    print(f"\n{slug}...", end="", flush=True)
    prompt = (
        f"Page: {page.title}\n\n"
        f"Content (first 2000 chars):\n{(page.content or '')[:2000]}\n\n"
        f"Generate tagline, 3 hero facts, and 3 did-you-know facts for this page."
    )

    for attempt in range(2):
        try:
            raw = call(prompt)
            data = parse(raw)
            if not is_valid_facts(data.get("facts", [])):
                print(f" attempt {attempt+1} invalid facts", end="", flush=True)
                continue

            page.hero_tagline = data["tagline"][:200]
            page.hero_facts = json.dumps(data["facts"][:3])
            page.did_you_know = json.dumps([str(d)[:200] for d in data.get("dyk", [])[:3]])
            page.category = CATEGORIES.get(slug, "observational")
            db.commit()
            print(f" ✅ tagline: {page.hero_tagline[:60]}...")
            fixed += 1
            break
        except Exception as e:
            print(f" error: {e}", end="", flush=True)
    else:
        print(f" SKIPPED")

db.close()
print(f"\nDone: {fixed}/{len(SLUGS)} pages enriched")
