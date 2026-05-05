"""
Decompose blank pages (zero claims) into claims using local Ollama.
Also fix hero_facts for pages with broken values.
Run from ~/NebulaMind/NebulaMind/backend/
"""
import sys, os, json, time, requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app.models.page import WikiPage
from app.models.claim import Claim
from sqlalchemy import text

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.3:70b"  # fast local model

CLAIM_PROMPT = """You are decomposing an astronomy wiki page into factual claims.

Page title: {title}
Page content:
{content}

Extract 8-15 specific, verifiable factual claims from this page. Each claim should be:
- A single, clear factual statement
- 1-2 sentences max
- Specific (include numbers/measurements when available)
- From the content above (no hallucination)

Return ONLY a JSON array of strings. Example:
["Black holes form when massive stars collapse.", "The event horizon marks the point of no return."]

Claims:"""

def ollama_generate(prompt, model=MODEL):
    try:
        r = requests.post(OLLAMA_URL, json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.3, "num_ctx": 4096}
        }, timeout=120)
        return r.json().get("response", "").strip()
    except Exception as e:
        print(f"  Ollama error: {e}")
        return None

def extract_json_array(text):
    """Extract JSON array from LLM response."""
    import re
    # Try to find array
    match = re.search(r'\[.*?\]', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            pass
    # Try full text
    try:
        return json.loads(text)
    except:
        return []

def main():
    db = SessionLocal()
    try:
        # Find blank pages
        blank_slugs = ['accretion-disks', 'baryon-acoustic-oscillations', 'cosmic-web',
                       'gravitational-lensing', 'interstellar-medium', 'planetary-formation',
                       'red-giants', 'reionization']

        # Find editor agent
        from app.models.agent import Agent
        editor = db.query(Agent).filter(Agent.name.ilike('%editor%')).first()
        if not editor:
            editor = db.query(Agent).first()
        print(f"Using agent: {editor.name if editor else 'None'}")

        for slug in blank_slugs:
            page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
            if not page or not page.content:
                print(f"SKIP {slug}: no content")
                continue

            print(f"\n[{slug}] Generating claims with {MODEL}...")
            prompt = CLAIM_PROMPT.format(title=page.title, content=page.content[:3000])
            response = ollama_generate(prompt)

            if not response:
                print(f"  FAILED: no response")
                continue

            claims_text = extract_json_array(response)
            if not claims_text:
                print(f"  FAILED: could not parse JSON from: {response[:200]}")
                continue

            print(f"  Got {len(claims_text)} claims")
            inserted = 0
            for claim_text in claims_text:
                if not claim_text or len(claim_text) < 10:
                    continue
                claim = Claim(
                    page_id=page.id,
                    text=claim_text.strip(),
                    claim_type='established',
                    trust_level='unverified',
                    added_by_agent_id=editor.id if editor else None,
                )
                db.add(claim)
                inserted += 1

            db.flush()
            db.commit()
            print(f"  Inserted {inserted} claims for {slug}")
            time.sleep(2)

        # Summary
        total_claims = db.execute(text("SELECT COUNT(*) FROM claims")).scalar()
        print(f"\nDone. Total claims now: {total_claims}")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    main()
