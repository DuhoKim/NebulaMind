import sys, os, json, urllib.request
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.page import WikiPage
from app.models.claim import Claim

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "llama3.3:70b"

ZERO_CLAIM_SLUGS = [
    "accretion-disks", "baryon-acoustic-oscillations", "cosmic-web",
    "gravitational-lensing", "interstellar-medium", "planetary-formation",
    "red-giants", "reionization",
]

SYSTEM_PROMPT = """You are a scientific wiki editor. Extract factual claims from astronomy wiki content.

Rules:
- Each claim must be a single, complete, verifiable sentence (15-60 words)
- Claims must be standalone (no pronouns referring to previous claims like "it", "they", "this")
- Each claim should state ONE fact
- Extract 8-15 claims per page
- Cover different sections of the page (Overview, Formation, Properties, Current Research, etc.)
- Group claims by logical section

Return ONLY a JSON object:
{
  "sections": [
    {
      "name": "Overview",
      "claims": [
        {"text": "...", "connector": null},
        {"text": "...", "connector": "Additionally,"}
      ]
    },
    {
      "name": "Properties",
      "claims": [...]
    }
  ]
}
connector is optional (null or a transitional word like "Additionally,", "Furthermore,", "However,")"""


def call_ollama(system, user):
    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "stream": False,
        "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"]


def insert_claims(db, page, sections_data):
    order = 0
    for section in sections_data.get("sections", []):
        section_name = section.get("name", "Overview")[:100]
        for claim_data in section.get("claims", []):
            text = claim_data.get("text", "").strip()
            if not text or len(text) < 20:
                continue
            claim = Claim(
                page_id=page.id,
                section=section_name,
                order_idx=order,
                text=text[:800],
                connector=claim_data.get("connector"),
                trust_level="unverified",
                claim_type="established",
            )
            db.add(claim)
            order += 1
    db.commit()
    return order


def main():
    db = SessionLocal()
    try:
        total_claims = 0
        for slug in ZERO_CLAIM_SLUGS:
            page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
            if not page or not page.content:
                print(f"SKIP {slug}: no content")
                continue

            print(f"\nProcessing: {slug} ({len(page.content)} chars)...")
            user_prompt = f"Wiki page: {page.title}\n\nContent:\n{page.content[:4000]}\n\nExtract 10-15 factual claims grouped by section."

            try:
                raw = call_ollama(SYSTEM_PROMPT, user_prompt)
                # Strip markdown fences
                cleaned = raw.strip()
                if cleaned.startswith("```"):
                    cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0]
                data = json.loads(cleaned)
                n = insert_claims(db, page, data)
                print(f"  DONE: {n} claims inserted")
                total_claims += n
            except Exception as e:
                print(f"  ERROR: {e}")
                import traceback; traceback.print_exc()
                db.rollback()

        print(f"\nTotal: {total_claims} claims created across {len(ZERO_CLAIM_SLUGS)} pages")
    finally:
        db.close()


if __name__ == "__main__":
    main()
