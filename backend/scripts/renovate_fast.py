#!/usr/bin/env python3
"""Fast renovation using direct Ollama HTTP (no Celery queue contention)."""
import sys, time, json, re, urllib.request, datetime as dt
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from app.database import SessionLocal
from app.models.page import WikiPage, RenovationPlan
from app.models.edit import EditProposal, EditStatus
from app.models.agent import Agent
from app.services.subtopic_maps import get_required_subtopics
from app.services.paper_search import search_papers
from app.agent_loop.tasks import can_propose_edit
from app.services.llm_utils import strip_think_blocks

# Rakon: deepseek-r1:671b on Mac Pro — heavy synthesis
OLLAMA_URL = "http://192.188.0.4:11434/v1/chat/completions"
MODEL = "deepseek-r1:671b"


def call_ollama(system: str, user: str, timeout: int = 90) -> str:
    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "stream": False, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(OLLAMA_URL, data=payload,
                                  headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        content = json.loads(r.read())["choices"][0]["message"]["content"]
        # Strip think blocks
        return strip_think_blocks(content)


def run_renovation(page: WikiPage, db) -> bool:
    print(f"\n[{page.slug}] score={page.health_score:.1f}", flush=True)

    # Get required subtopics and find missing
    from app.models.claim import Claim
    from app.services.subtopic_maps import coverage_ratio
    claims = db.query(Claim).filter(Claim.page_id == page.id).all()
    claim_texts = [c.text for c in claims]
    ratio, missing = coverage_ratio(page.slug, claim_texts)
    subtopic_kw = get_required_subtopics(page.slug)
    print(f"  Coverage: {ratio:.0%}, missing: {missing[:3]}", flush=True)

    # Gather evidence
    papers = []
    seen = set()
    try:
        fresh = search_papers(f"{page.title} 2024 2025", rows=4, prefer_recent=True)
        for p in fresh:
            if p.arxiv_id and p.arxiv_id not in seen:
                papers.append({"id": p.arxiv_id, "title": p.title, "year": p.year,
                                "abstract": (p.abstract or "")[:300]})
                seen.add(p.arxiv_id)
    except Exception as e:
        print(f"  fresh search error: {e}", flush=True)

    for sid in missing[:3]:
        aliases = subtopic_kw.get(sid, [sid.replace("_", " ")])
        try:
            results = search_papers(f"{page.title} {aliases[0]}", rows=3, prefer_recent=True)
            for p in results:
                if p.arxiv_id and p.arxiv_id not in seen and len(papers) < 20:
                    papers.append({"id": p.arxiv_id, "title": p.title, "year": p.year,
                                    "abstract": (p.abstract or "")[:300]})
                    seen.add(p.arxiv_id)
        except Exception:
            pass

    if not papers:
        print(f"  No papers found, skipping", flush=True)
        return False
    print(f"  Found {len(papers)} papers", flush=True)

    # Find current section
    content = page.content or ""
    section_match = re.search(r'(## Current Research.*?)(?=\n## |\Z)', content, re.DOTALL)
    current_section = section_match.group(1)[:1500] if section_match else "## Current Research\n(empty)"

    missing_text = "\n".join(
        f"- {sid}: {', '.join(subtopic_kw.get(sid, [sid])[:2])}"
        for sid in missing[:3]
    )
    ev_text = "\n".join(
        f"- [{p['id']}] {p['title']} ({p['year']}): {p['abstract'][:200]}"
        for p in papers[:10]
    )

    SYSTEM = f"""Renovate the NebulaMind wiki page "{page.title}".
Rewrite ## Current Research to be genuinely representative.

RULES:
- Each claim must cite [arXiv:ID] from the evidence list.
- Missing subtopics: add only if actually applicable to {page.title}. Skip with "NOT_APPLICABLE" if not.
- Preserve any strong existing claims.
- No invented citations.
- Output ONLY the rewritten section starting with ## Current Research
- 6-10 claims with citations."""

    USER = f"""Evidence (arXiv papers):
{ev_text}

Missing subtopics:
{missing_text}

Current section:
{current_section}

Rewrite ## Current Research."""

    # Synthesize
    try:
        new_section = call_ollama(SYSTEM, USER, timeout=300)
        if not new_section.startswith("## Current Research"):
            new_section = f"## Current Research\n\n{new_section}"
        print(f"  ✓ synthesized ({len(new_section)} chars)", flush=True)
    except Exception as e:
        print(f"  synthesize ERROR: {e}", flush=True)
        return False

    # Build new content
    if re.search(r'## Current Research', content, re.DOTALL):
        new_content = re.sub(
            r'(## Current Research.*?)(?=\n## |\Z)',
            lambda m: new_section, content, flags=re.DOTALL
        )
    else:
        new_content = content.rstrip() + "\n\n" + new_section

    # Submit proposal
    arxivbot = db.query(Agent).filter(Agent.name == "ArxivBot").first()
    if not arxivbot:
        print("  ArxivBot not found", flush=True)
        return False

    # Papa approved full renovation — bypass daily throttle
    # allowed, reason = can_propose_edit(db, page.id, arxivbot.id)
    # if not allowed: return False

    proposal = EditProposal(
        page_id=page.id, agent_id=arxivbot.id,
        content=new_content, status=EditStatus.PENDING,
    )
    db.add(proposal)
    page.last_renovated_at = dt.datetime.utcnow()

    # Update renovation plan
    plan = db.query(RenovationPlan).filter(
        RenovationPlan.page_id == page.id,
        RenovationPlan.status.in_(["queued", "synthesizing", "gathering"])
    ).order_by(RenovationPlan.id.desc()).first()
    if plan:
        plan.status = "proposed"
        plan.completed_at = dt.datetime.utcnow()

    db.commit()
    print(f"  ✓ PROPOSAL #{proposal.id} submitted!", flush=True)
    return True


def main():
    db = SessionLocal()
    pages = (
        db.query(WikiPage)
        .filter(
            WikiPage.health_score.isnot(None),
            WikiPage.do_not_renovate == False,
            WikiPage.category.isnot(None),
        )
        .order_by(WikiPage.health_score.asc())
        .all()
    )
    print(f"Renovating {len(pages)} pages with qwen3.6:27b-nvfp4...\n", flush=True)

    submitted = 0
    skipped = 0
    for page in pages:
        # Check if already proposed
        existing = db.query(RenovationPlan).filter(
            RenovationPlan.page_id == page.id,
            RenovationPlan.status == "proposed"
        ).first()
        if existing:
            skipped += 1
            print(f"[{page.slug}] Already proposed, skipping", flush=True)
            continue

        if run_renovation(page, db):
            submitted += 1
        else:
            # Pause and retry on failure
            time.sleep(5)
        time.sleep(3)

    db.close()
    print(f"\n{'='*50}")
    print(f"Done: {submitted} proposals submitted, {skipped} skipped")


if __name__ == "__main__":
    main()
