#!/usr/bin/env python3
"""Repair broken hero_facts using local Ollama qwen3:30b."""
import sys, os, json, urllib.request, re, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.page import WikiPage

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "phi4:14b"

BROKEN_SLUGS = [
    "asteroid-belt", "binary-stars", "black-holes",
    "dark-matter", "exoplanet-detection-methods", "fast-radio-bursts",
    "galaxy-formation", "gamma-ray-bursts", "nebulae", "planetary-nebulae",
    "spacetime", "white-dwarfs", "wormholes",
]

SYSTEM = """You are a precision astronomy data extractor. Generate exactly 3 hero facts.
Rules:
- Values MUST be numeric or scientific notation (e.g. "1.4", "10⁶–10¹⁰", "~13.8", "5–100")
- FORBIDDEN in value: "millions", "billions", "trillions", "thousands", "hundreds", "milliseconds", "energy", "effects", "daily", "gravitational", "estimated", "typical"
- FORBIDDEN: year 1916 unless the page is specifically about general relativity
- Units: real physical units, "year", "Gyr", or empty string
- Labels: 2-4 words max
Return ONLY a JSON array: [{"label":"...","value":"...","unit":"..."},...]
No thinking, no explanation, just the JSON array."""

FORBIDDEN = {"millions","billions","trillions","thousands","hundreds",
             "milliseconds","energy","effects","daily","gravitational","estimated","typical"}

def log(msg):
    print(msg, flush=True)

def call_ollama(user: str, temperature: float = 0.2) -> str:
    # Use Ollama native API to disable thinking explicitly
    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
        "stream": False,
        "temperature": temperature,
        "options": {"num_predict": 512},
    }).encode()
    req = urllib.request.Request(OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        resp = json.loads(r.read())
    content = resp["choices"][0]["message"]["content"]
    # Strip <think>...</think> tags from qwen3 responses
    content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()
    return content

def is_valid(facts) -> bool:
    if not isinstance(facts, list) or len(facts) != 3:
        return False
    for f in facts:
        v = str(f.get("value", "")).lower()
        if any(w in v for w in FORBIDDEN):
            return False
        if not f.get("label") or not str(f.get("value", "")).strip():
            return False
    return True

def parse_json(raw: str):
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    m = re.search(r'\[.*\]', cleaned, re.DOTALL)
    if m:
        return json.loads(m.group())
    return json.loads(cleaned)

def main():
    db = SessionLocal()
    fixed = 0
    skipped = 0
    try:
        for slug in BROKEN_SLUGS:
            page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
            if not page:
                log(f"SKIP {slug}: not found")
                skipped += 1
                continue

            log(f"\n--- {slug} ({page.title}) ---")
            log(f"  OLD: {page.hero_facts}")
            user_prompt = (
                f"Page: {page.title}\n\nContent excerpt:\n{(page.content or '')[:1500]}\n\n"
                f"Generate 3 precise hero facts. Use specific numbers.\n"
                f"Good examples: {{\"label\":\"Stellar mass\",\"value\":\"5–100\",\"unit\":\"M☉\"}}\n"
                f"Return ONLY the JSON array. /no_think"
            )

            facts = None
            for attempt in range(2):
                try:
                    t0 = time.time()
                    raw = call_ollama(user_prompt, temperature=0.1 if attempt else 0.2)
                    dt = time.time() - t0
                    log(f"  Attempt {attempt+1} ({dt:.1f}s): {raw[:300]}")
                    facts = parse_json(raw)
                    if is_valid(facts):
                        break
                    else:
                        log(f"  Attempt {attempt+1} invalid")
                        facts = None
                except Exception as e:
                    log(f"  Attempt {attempt+1} error: {e}")
                    facts = None

            if facts:
                page.hero_facts = json.dumps(facts, ensure_ascii=False)
                db.commit()
                log(f"  NEW: {page.hero_facts}")
                log(f"  FIXED: {slug}")
                fixed += 1
            else:
                log(f"  SKIPPED: {slug} (validation failed)")
                skipped += 1

    except Exception as e:
        db.rollback()
        log(f"Fatal error: {e}")
        raise
    finally:
        db.close()

    log(f"\n{'='*50}")
    log(f"Done: {fixed} fixed, {skipped} skipped")

if __name__ == "__main__":
    main()
