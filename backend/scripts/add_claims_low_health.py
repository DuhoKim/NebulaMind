"""
Add 2-3 new claims to the 5 lowest-health pages (excluding galaxy-evolution).
Uses Mima (qwen3.6:35b-a3b-nvfp4) primary, Blanc (llama3.3:70b) fallback.
"""
import sys, os, json, urllib.request
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.page import WikiPage
from app.models.claim import Claim

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MIMA  = "qwen3.6:35b-a3b-nvfp4"
BLANC = "llama3.3:70b"

# 5 lowest health pages (excl. galaxy-evolution/page 57)
TARGET_PAGE_IDS = [40, 50, 37, 55, 38]  # Accretion Disks, Planetary Formation, ISM, Cosmic Web, Reionization

SYSTEM_PROMPT = """You are a scientific wiki editor for an astronomy knowledge base.
Your task: generate 2-3 NEW factual claims to add to an existing wiki page.

Rules:
- Each claim: a single, complete, verifiable sentence (15-60 words)
- Claims must be STANDALONE — no pronouns referring to other claims ("it", "they", "this phenomenon")
- Each claim states ONE distinct fact not already covered by existing claims
- Claims should add depth: focus on mechanisms, quantitative data, recent discoveries, or cross-topic links
- Do NOT repeat information already in the existing claims list

Return ONLY valid JSON (no markdown fences, no extra text):
{
  "new_claims": [
    {"section": "Properties", "text": "...", "connector": null},
    {"section": "Current Research", "text": "...", "connector": "Additionally,"}
  ]
}
connector is optional (null or a brief transitional phrase like "Additionally,", "Furthermore,", "In contrast,")"""


def call_ollama(model: str, system: str, user: str, timeout: int = 120) -> str:
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "stream": False,
        "temperature": 0.4,
    }).encode()
    req = urllib.request.Request(OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"]


def parse_json(raw: str) -> dict:
    cleaned = raw.strip()
    # Strip markdown fences if present
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    # Strip qwen3 <think> blocks
    if "<think>" in cleaned:
        cleaned = cleaned.split("</think>")[-1].strip()
    return json.loads(cleaned)


def get_existing_claim_texts(db, page_id: int) -> list[str]:
    claims = db.query(Claim).filter(Claim.page_id == page_id).all()
    return [c.text for c in claims]


def get_next_order_idx(db, page_id: int) -> int:
    from sqlalchemy import func
    result = db.query(func.max(Claim.order_idx)).filter(Claim.page_id == page_id).scalar()
    return (result or 0) + 1


def insert_new_claims(db, page_id: int, new_claims: list[dict], start_idx: int) -> int:
    inserted = 0
    for i, c in enumerate(new_claims):
        text = c.get("text", "").strip()
        if not text or len(text) < 20:
            continue
        claim = Claim(
            page_id=page_id,
            section=c.get("section", "Current Research")[:100],
            order_idx=start_idx + i,
            text=text[:800],
            connector=c.get("connector"),
            trust_level="unverified",
            claim_type="established",
        )
        db.add(claim)
        inserted += 1
    db.commit()
    return inserted


def process_page(db, page: WikiPage) -> int:
    existing = get_existing_claim_texts(db, page.id)
    existing_summary = "\n".join(f"- {t}" for t in existing[:20])

    user_prompt = (
        f"Page: {page.title}\n\n"
        f"Existing claims (do NOT repeat these):\n{existing_summary}\n\n"
        f"Page content excerpt:\n{page.content[:3000]}\n\n"
        f"Generate 2-3 new, distinct factual claims that add depth to this page."
    )

    raw = None
    model_used = None
    for model, label in [(MIMA, "Mima"), (BLANC, "Blanc")]:
        try:
            print(f"  Trying {label} ({model})...")
            raw = call_ollama(model, SYSTEM_PROMPT, user_prompt, timeout=150)
            model_used = label
            break
        except Exception as e:
            print(f"  {label} failed: {e}")

    if raw is None:
        print(f"  All models failed for {page.title}")
        return 0

    try:
        data = parse_json(raw)
    except Exception as e:
        print(f"  JSON parse error ({model_used}): {e}")
        print(f"  Raw: {raw[:300]}")
        return 0

    new_claims = data.get("new_claims", [])
    if not new_claims:
        print(f"  No claims returned")
        return 0

    start_idx = get_next_order_idx(db, page.id)
    n = insert_new_claims(db, page.id, new_claims, start_idx)
    print(f"  {model_used}: inserted {n} claims (start_idx={start_idx})")
    return n


def main():
    db = SessionLocal()
    results = []
    try:
        for page_id in TARGET_PAGE_IDS:
            page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
            if not page:
                print(f"Page {page_id} not found")
                continue
            existing_count = db.query(Claim).filter(Claim.page_id == page_id).count()
            print(f"\n[Page {page_id}] {page.title} — existing claims: {existing_count}, health: {page.health_score}")
            n = process_page(db, page)
            results.append((page.title, existing_count, n))
    finally:
        db.close()

    print("\n=== SUMMARY ===")
    for title, before, added in results:
        print(f"  {title}: {before} → {before + added} claims (+{added})")


if __name__ == "__main__":
    main()
