#!/usr/bin/env python3
"""Regenerate did_you_know facts using local Ollama qwen3:30b."""
import sys, os, json, urllib.request, re, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.page import WikiPage

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "qwen3:30b"

FORBIDDEN_WORDS = {"millions", "billions", "trillions", "thousands", "hundreds", "million", "billion"}

SYSTEM = """You are a science communicator writing "Did You Know?" facts for an astronomy wiki.

Rules:
- Each fact must be SHORT (1 sentence, under 80 words)
- Must be SPECIFIC and SURPRISING — real numbers, not vague magnitudes
- FORBIDDEN in facts: "millions", "billions", "trillions", "thousands", "hundreds", "million", "billion"
- Facts should make the reader think "wow, I didn't know that!"
- Write 3 facts per page

Return ONLY a JSON array of 3 strings:
["Fact 1 sentence.", "Fact 2 sentence.", "Fact 3 sentence."]"""

def call_ollama(user: str) -> str:
    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
        "stream": False,
        "temperature": 0.4,
    }).encode()
    req = urllib.request.Request(OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        content = json.loads(r.read())["choices"][0]["message"]["content"]
        # Strip qwen3 thinking blocks
        content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()
        return content

def parse_json(raw: str):
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    m = re.search(r'\[.*\]', cleaned, re.DOTALL)
    if m:
        return json.loads(m.group())
    return json.loads(cleaned)

def is_valid(facts) -> bool:
    if not isinstance(facts, list) or len(facts) < 2:
        return False
    for f in facts:
        fl = str(f).lower()
        if any(w in fl for w in FORBIDDEN_WORDS):
            return False
        if len(str(f).strip()) < 20:
            return False
    return True

def main():
    db = SessionLocal()
    fixed = 0
    skipped = 0
    try:
        # Get all pages with content (34 pages in Group A)
        pages = db.query(WikiPage).filter(
            WikiPage.hero_tagline.isnot(None),
            WikiPage.content != ""
        ).order_by(WikiPage.slug).all()
        
        print(f"Processing {len(pages)} pages...")
        
        for page in pages:
            print(f"\n{page.slug}...")
            user_prompt = (
                f"Page: {page.title}\n\nContent excerpt:\n{(page.content or '')[:2000]}\n\n"
                f"Write 3 surprising 'Did You Know?' facts about {page.title}. "
                f"Use specific numbers. No vague magnitudes. Return JSON array of 3 strings."
            )
            
            facts = None
            for attempt in range(2):
                try:
                    raw = call_ollama(user_prompt)
                    facts = parse_json(raw)
                    if is_valid(facts):
                        break
                    else:
                        print(f"  attempt {attempt+1} invalid: {facts[:1] if facts else 'parse error'}")
                        facts = None
                        time.sleep(1)
                except Exception as e:
                    print(f"  attempt {attempt+1} error: {e}")
                    facts = None
            
            if facts:
                old_val = page.did_you_know
                page.did_you_know = json.dumps(facts[:3])
                db.commit()
                print(f"  FIXED: {facts[0][:70]}...")
                fixed += 1
            else:
                print(f"  SKIPPED: validation failed")
                skipped += 1
    
    except Exception as e:
        db.rollback()
        print(f"Fatal: {e}")
        raise
    finally:
        db.close()
    
    print(f"\n{'='*50}")
    print(f"Done: {fixed} fixed, {skipped} skipped")

if __name__ == "__main__":
    main()
