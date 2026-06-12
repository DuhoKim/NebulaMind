#!/usr/bin/env python3
"""
AstroSage-70B batch renovation — targets lowest-health pages.
Uses proposers.py (AstroSage on localhost:11434) for:
  - 2x ClaimInsert per page (established subtopic coverage)
  - 1x HeroUpgrade per page
  - 1x SectionRewrite per page (lowest-scoring section)

Run: python3 astrosage_reno_batch.py
"""
import sys, time, json
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from app.database import SessionLocal
from app.models.page import WikiPage, PageVersion
from app.models.claim import Claim
from app.models.edit import EditProposal, EditStatus
from app.models.agent import Agent
from app.agent_loop.autowiki.proposers import (
    propose_claim_insert,
    propose_hero_upgrade,
    propose_section_rewrite,
)
from app.agent_loop.autowiki.program_loader import load_program
from app.services.subtopic_maps import get_required_subtopics

# Target pages (lowest health, exclude galaxy-evolution id=57)
TARGET_PAGE_IDS = [40, 50, 37, 55, 38]  # accretion-disks, planetary-formation, interstellar-medium, cosmic-web, reionization

def get_latest_content(db, page_id: int) -> str:
    page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
    if page and page.content:
        return page.content
    # fallback to latest PageVersion
    pv = db.query(PageVersion).filter(
        PageVersion.page_id == page_id
    ).order_by(PageVersion.id.desc()).first()
    return pv.content if pv else ""

def get_or_create_agent(db) -> Agent:
    agent = db.query(Agent).filter(Agent.name == "AstroSage-70B").first()
    if not agent:
        agent = Agent(name="AstroSage-70B", model_name="astrosage-70b", role="drafter", contributor_type="agent", is_active=True)
        db.add(agent)
        db.commit()
        db.refresh(agent)
    return agent

def save_proposal(db, page_id: int, agent_id: int, kind: str, content: dict):
    proposal = EditProposal(
        page_id=page_id,
        agent_id=agent_id,
        edit_type=kind,
        proposed_content=json.dumps(content),
        status=EditStatus.pending,
    )
    db.add(proposal)
    db.commit()
    print(f"  ✓ Saved {kind} proposal (id={proposal.id})", flush=True)

def get_missing_subtopics(db, page, content: str) -> list[str]:
    required = get_required_subtopics(page.slug)
    if not required:
        return []
    # Use section headers present in content as coverage proxy
    covered = set()
    for line in content.split('\n'):
        if line.startswith('## ') or line.startswith('### '):
            covered.add(line.lstrip('#').strip().lower())
    return [s for s in required if s.lower().replace('_', ' ') not in covered][:3]

def pick_weakest_section(content: str) -> str:
    """Pick a ## section that looks thin (fewest words)."""
    sections = {}
    current = None
    for line in content.split('\n'):
        if line.startswith('## '):
            current = line[3:].strip()
            sections[current] = 0
        elif current:
            sections[current] += len(line.split())
    if not sections:
        return "Overview"
    skip = {"See Also", "References", "Further Reading", "External Links"}
    candidates = {k: v for k, v in sections.items() if k not in skip and v > 0}
    if not candidates:
        return list(sections.keys())[0]
    return min(candidates, key=candidates.get)

def main():
    db = SessionLocal()
    agent = get_or_create_agent(db)

    for page_id in TARGET_PAGE_IDS:
        page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
        if not page:
            print(f"Page {page_id} not found, skipping", flush=True)
            continue

        print(f"\n{'='*60}", flush=True)
        print(f"Page: {page.title} (id={page.id}, health={page.health_score:.1f})", flush=True)
        print(f"{'='*60}", flush=True)

        content = get_latest_content(db, page.id)
        if not content:
            print(f"  No content found, skipping", flush=True)
            continue

        program = load_program(page.slug) or f"Write accurate, detailed astronomy wiki content about {page.title}."
        missing_subs = get_missing_subtopics(db, page, content)

        # 1. ClaimInsert x2
        for i in range(2):
            try:
                print(f"  → ClaimInsert #{i+1} (missing_subs={missing_subs[:1]})", flush=True)
                result = propose_claim_insert(
                    content, page.id, program,
                    claim_type="established",
                    missing_subtopics=missing_subs[i:i+1] if i < len(missing_subs) else None
                )
                if result.gate_passed:
                    save_proposal(db, page.id, agent.id, "claim_insert", result.payload.__dict__)
                else:
                    print(f"  ✗ ClaimInsert failed: {result.gate_reason}", flush=True)
            except Exception as e:
                print(f"  ✗ ClaimInsert exception: {e}", flush=True)
            time.sleep(2)

        # 2. HeroUpgrade x1
        try:
            print(f"  → HeroUpgrade", flush=True)
            result = propose_hero_upgrade(content, page.hero_facts, program)
            if result.gate_passed:
                save_proposal(db, page.id, agent.id, "hero_upgrade", result.payload.__dict__)
            else:
                print(f"  ✗ HeroUpgrade failed: {result.gate_reason}", flush=True)
        except Exception as e:
            print(f"  ✗ HeroUpgrade exception: {e}", flush=True)
        time.sleep(2)

        # 3. SectionRewrite x1
        try:
            weakest = pick_weakest_section(content)
            print(f"  → SectionRewrite: '{weakest}'", flush=True)
            result = propose_section_rewrite(content, weakest, program)
            if result.gate_passed:
                save_proposal(db, page.id, agent.id, "section_rewrite", result.payload.__dict__)
            else:
                print(f"  ✗ SectionRewrite failed: {result.gate_reason}", flush=True)
        except Exception as e:
            print(f"  ✗ SectionRewrite exception: {e}", flush=True)
        time.sleep(2)

        print(f"  ✓ Done with {page.title}", flush=True)

    db.close()
    print("\n\n✅ AstroSage batch renovation complete.", flush=True)

if __name__ == "__main__":
    main()
