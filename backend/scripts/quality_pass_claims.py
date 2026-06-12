"""
Quality pass: add 2-3 new claims per low-health-score page using Blanc (llama3.3:70b).
Run from: ~/NebulaMind/NebulaMind/backend/
"""
import sys, os, json, re, time, requests
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.page import WikiPage
from app.models.claim import Claim
from app.models.agent import Agent

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.3:70b"  # Blanc — fast, good quality

TARGET_SLUGS = [
    "accretion-disks",
    "planetary-formation",
    "interstellar-medium",
    "cosmic-web",
    "reionization",
]

CLAIM_PROMPT = """You are adding new factual claims to an astronomy wiki page.

Page title: {title}
Page section content (for context):
{content}

Existing claims (DO NOT repeat these):
{existing}

Generate exactly {n} NEW claims that are:
- Specific, verifiable factual statements (1-2 sentences each)
- NOT duplicating the existing claims above
- Include measurements, dates, or specific values where relevant
- Based on real astrophysics/cosmology (no hallucination)
- Focused on the most important or interesting aspects of {title}

Return ONLY a JSON array of {n} strings, like:
["Claim one here.", "Claim two here.", "Claim three here."]

New claims:"""


def ollama_generate(prompt, model=MODEL, retries=5):
    for attempt in range(retries):
        try:
            r = requests.post(OLLAMA_URL, json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0.4, "num_ctx": 8192}
            }, timeout=300)
            r.raise_for_status()
            return r.json().get("response", "").strip()
        except Exception as e:
            wait = 30 * (attempt + 1)
            print(f"  Ollama error (attempt {attempt+1}/{retries}): {e} — retrying in {wait}s...")
            time.sleep(wait)
    return None


def extract_json_array(text):
    match = re.search(r'\[.*?\]', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except Exception:
            pass
    try:
        return json.loads(text)
    except Exception:
        return []


def get_section_content(content, max_chars=3000):
    """Get a useful slice of page content for context."""
    if not content:
        return "(no content)"
    # Skip the first heading, get body
    lines = content.split('\n')
    body = '\n'.join(l for l in lines if not l.startswith('# '))
    return body[:max_chars]


def main():
    db = SessionLocal()
    try:
        agent = (
            db.query(Agent).filter(Agent.name.ilike('%blanc%')).first()
            or db.query(Agent).filter(Agent.name.ilike('%editor%')).first()
            or db.query(Agent).first()
        )
        print(f"Using agent: {agent.name if agent else 'None'}\n")

        total_added = 0
        results = []

        for slug in TARGET_SLUGS:
            page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
            if not page:
                print(f"[{slug}] NOT FOUND, skipping")
                continue

            existing = db.query(Claim).filter(Claim.page_id == page.id).all()
            existing_texts = [c.text for c in existing]
            claim_count = len(existing_texts)

            n_new = 3 if claim_count < 8 else 2

            existing_summary = "\n".join(f"- {t[:120]}" for t in existing_texts[:15])
            content_ctx = get_section_content(page.content)

            print(f"[{page.title}] {claim_count} claims → adding {n_new}...")

            prompt = CLAIM_PROMPT.format(
                title=page.title,
                content=content_ctx,
                existing=existing_summary,
                n=n_new,
            )

            raw = ollama_generate(prompt)
            if not raw:
                print(f"  ✗ no response")
                results.append((page.title, 0))
                continue

            new_claims = extract_json_array(raw)
            if not new_claims:
                print(f"  ✗ could not parse JSON from response:\n{raw[:300]}")
                results.append((page.title, 0))
                continue

            # Limit to n_new
            new_claims = [c for c in new_claims if isinstance(c, str) and len(c) > 20][:n_new]

            added = 0
            for text in new_claims:
                # Determine section
                c = Claim(
                    page_id=page.id,
                    section="Current Research",
                    text=text.strip(),
                    trust_level="unverified",
                    created_by_agent_id=agent.id if agent else None,
                    claim_type="factual",
                )
                db.add(c)
                added += 1
                print(f"  + {text[:100]}")

            db.commit()
            total_added += added
            results.append((page.title, added))
            print(f"  → {added} claims added\n")
            time.sleep(2)

        print("=" * 60)
        print(f"Quality pass complete. Total claims added: {total_added}")
        for title, n in results:
            print(f"  {title}: +{n}")

    finally:
        db.close()


if __name__ == "__main__":
    main()
