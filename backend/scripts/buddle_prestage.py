#!/usr/bin/env python3
"""
Buddle pre-staging: Mac Studio local Buddle preps arXiv papers + claim
skeletons + evidence links for pages queued for Rakon synthesis.

Runs concurrently with renovate_fast.py (Rakon 671b).
While Rakon synthesizes current page, Buddle pre-stages next pages
so they feed straight into Rakon with no cold-start arXiv delay.
"""
import sys, time, json, re, urllib.request, datetime as dt
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from app.database import SessionLocal
from app.config import settings
from app.models.page import WikiPage
from app.models.claim import Claim, Evidence
from app.models.agent import Agent
from app.services.paper_search import search_papers
from app.services.subtopic_maps import get_required_subtopics
from app.services.llm_utils import strip_think_blocks

BUDDLE_URL = f"{settings.BUDDLE_BASE_URL.rstrip('/')}/v1/chat/completions"
BUDDLE_MODEL = settings.BUDDLE_MODEL

# Pages to pre-stage — queue order for Rakon after it finishes early pages
# Add slugs here; script skips already-renovated pages automatically.
TARGET_SLUGS = [
    "supernovae",        # score 59.5 — Rakon will hit this early
    "dark-matter",       # score 62.8
    "oort-cloud",        # may already be done; script will skip
    "galaxy-formation",  # same
    "reionization",      # same
    # Add more if Ollama overload clears other pages first:
    "white-dwarfs",
    "quasars",
    "stellar-evolution",
    "active-galactic-nuclei",
    "neutron-stars",
    "black-holes",
]


def call_buddle(system: str, user: str, timeout: int = 150) -> str:
    payload = json.dumps({
        "model": BUDDLE_MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": False,
        "temperature": 0.15,
    }).encode()
    req = urllib.request.Request(
        BUDDLE_URL, data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        content = json.loads(r.read())["choices"][0]["message"]["content"]
        return strip_think_blocks(content)


def fetch_papers(page: WikiPage, max_papers: int = 15):
    """Fetch arXiv papers for a page, covering topic + missing subtopics."""
    papers = []
    seen = set()

    def add(p):
        if p.arxiv_id and p.arxiv_id not in seen and len(papers) < max_papers:
            papers.append(p)
            seen.add(p.arxiv_id)

    try:
        for p in search_papers(f"{page.title} astronomy 2024 2025", rows=6, prefer_recent=True):
            add(p)
    except Exception as e:
        print(f"  [fetch] primary search error: {e}", flush=True)

    subtopics = get_required_subtopics(page.slug)
    for sid, keywords in list(subtopics.items())[:4]:
        if len(papers) >= max_papers:
            break
        try:
            for p in search_papers(f"{page.title} {keywords[0]}", rows=3, prefer_recent=True):
                add(p)
        except Exception:
            pass
        time.sleep(0.5)

    return papers


def extract_claims_via_buddle(page: WikiPage, papers) -> list[dict]:
    """Ask Buddle to extract structured claim skeletons from paper list."""
    ev_text = "\n".join(
        f"- [{p.arxiv_id}] {p.title} ({p.year}): {(p.abstract or '')[:280]}"
        for p in papers[:12]
    )

    SYSTEM = """You are an astronomy knowledge extractor. Given a list of arXiv papers,
extract claim skeletons for a wiki page.

Output ONLY a valid JSON array — no prose, no markdown fences, no think blocks.

Schema:
[
  {
    "text": "Specific, citable claim statement ending with [arXiv:ID].",
    "section": "Current Research",
    "claim_type": "established|emerging|contested",
    "arxiv_id": "THE_PAPER_ID_THIS_CITES",
    "beat": "subtopic keyword this claim addresses"
  }
]

Rules:
- 5 to 8 claims
- Each claim MUST cite one arxiv_id from the provided list (exact ID)
- claim_type: "established" = scientific consensus, "emerging" = 2024/2025 finding, "contested" = active debate
- "beat" = the specific subtopic this claim covers (e.g. "dark matter halo", "nucleosynthesis yield")
- Claims must be specific and informative, not generic
- Never invent arxiv IDs"""

    USER = f"""Wiki page: "{page.title}"

arXiv papers available:
{ev_text}

Extract 5-8 claim skeletons as JSON."""

    try:
        raw = call_buddle(SYSTEM, USER, timeout=150)
        match = re.search(r'\[.*?\]', raw, re.DOTALL)
        if not match:
            # Try broader match
            match = re.search(r'\[', raw)
            if match:
                raw_slice = raw[match.start():]
                # Find balanced bracket
                depth = 0
                end = 0
                for i, ch in enumerate(raw_slice):
                    if ch == '[':
                        depth += 1
                    elif ch == ']':
                        depth -= 1
                        if depth == 0:
                            end = i + 1
                            break
                if end:
                    match_str = raw_slice[:end]
                    return json.loads(match_str)
            print(f"  [buddle] no JSON array in response", flush=True)
            return []
        return json.loads(match.group())
    except Exception as e:
        print(f"  [buddle] parse error: {e}", flush=True)
        return []


def extract_section_beats(page: WikiPage, papers) -> list[str]:
    """Ask Buddle for ordered section beats (subtopic outline) for Rakon."""
    ev_titles = "; ".join(p.title for p in papers[:8])
    subtopics = get_required_subtopics(page.slug)
    topic_list = ", ".join(list(subtopics.keys())[:8])

    SYSTEM = """You are an astronomy editor. Given a page topic and available papers,
output an ordered list of 6-8 section beats (subtopic sentences) that a comprehensive
'Current Research' section should cover.

Output ONLY a JSON array of strings — no prose, no markdown.
Example: ["Dark matter halo mass function from DESI DR1.", "Constraints on WIMPs from LUX-ZEPLIN 2024.", ...]"""

    USER = f"""Page: "{page.title}"
Required subtopics: {topic_list}
Available papers: {ev_titles}

Output ordered section beats as JSON string array."""

    try:
        raw = call_buddle(SYSTEM, USER, timeout=90)
        match = re.search(r'\[.*?\]', raw, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception as e:
        print(f"  [buddle] beats error: {e}", flush=True)
    return []


def prestage_page(page: WikiPage, db) -> dict:
    """Full pre-staging: papers → claims → evidence → beats."""
    print(f"\n[BUDDLE] {page.slug} (score={page.health_score:.1f})", flush=True)

    # 1. Fetch papers
    papers = fetch_papers(page)
    if not papers:
        print(f"  No papers found", flush=True)
        return {"claims": 0, "beats": 0}
    print(f"  Found {len(papers)} papers", flush=True)

    # 2. Extract claim skeletons
    claims_data = extract_claims_via_buddle(page, papers)
    print(f"  Buddle returned {len(claims_data)} claim skeletons", flush=True)

    # 3. Get ArxivBot agent for attribution
    arxivbot = db.query(Agent).filter(Agent.name == "ArxivBot").first()
    agent_id = arxivbot.id if arxivbot else None

    # 4. Avoid duplicates
    existing_texts = {
        c.text[:120]
        for c in db.query(Claim).filter(Claim.page_id == page.id).all()
    }
    paper_map = {p.arxiv_id: p for p in papers}

    inserted_claims = 0
    existing_count = db.query(Claim).filter(Claim.page_id == page.id).count()

    for i, cd in enumerate(claims_data):
        text = (cd.get("text") or "").strip()
        if not text or len(text) < 20:
            continue
        if text[:120] in existing_texts:
            continue

        claim = Claim(
            page_id=page.id,
            section=cd.get("section", "Current Research"),
            order_idx=existing_count + i,
            text=text,
            trust_level="unverified",
            claim_type=cd.get("claim_type", "established"),
            created_by_agent_id=agent_id,
        )
        db.add(claim)
        db.flush()

        arxiv_id = cd.get("arxiv_id")
        if arxiv_id and arxiv_id in paper_map:
            paper = paper_map[arxiv_id]
            db.add(Evidence(
                claim_id=claim.id,
                arxiv_id=arxiv_id,
                title=paper.title,
                year=paper.year,
                abstract=(paper.abstract or "")[:600],
                stance="supports",
                added_by_agent_id=agent_id,
                source_channel="buddle_prestage",
                quality=0.65,
            ))

        existing_texts.add(text[:120])
        inserted_claims += 1

    # 5. Extract section beats and store as page metadata (annotation)
    beats = extract_section_beats(page, papers)
    if beats:
        beats_json = json.dumps(beats, ensure_ascii=False)
        # Store in page.staging_beats if column exists, else log
        if hasattr(page, 'staging_beats'):
            page.staging_beats = beats_json
        else:
            print(f"  Beats: {beats[:3]}...", flush=True)

    db.commit()
    print(f"  ✓ {inserted_claims} claims + evidence inserted | {len(beats)} beats", flush=True)
    return {"claims": inserted_claims, "beats": len(beats)}


def main():
    db = SessionLocal()
    total_claims = 0
    processed = 0

    for slug in TARGET_SLUGS:
        page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
        if not page:
            print(f"[SKIP] {slug} — not found in DB", flush=True)
            continue
        if page.last_renovated_at:
            print(f"[SKIP] {slug} — already renovated", flush=True)
            continue

        result = prestage_page(page, db)
        total_claims += result["claims"]
        processed += 1
        time.sleep(4)  # avoid hammering Buddle back-to-back

    db.close()
    print(f"\n{'='*50}")
    print(f"Buddle done: {processed} pages pre-staged, {total_claims} claim skeletons inserted")


if __name__ == "__main__":
    main()
