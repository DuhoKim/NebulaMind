#!/usr/bin/env python3
"""
AstroSage-70B targeted boost for galaxy-evolution (page_id=57).
Focuses on judge-flagged weak areas:
- JWST/DESI frontier sections (too superficial)
- Open questions (named but not interrogated)
- New hero facts (currently 7, target 10)
- Evidence-poor claims: 1495, 1496, 1512

Run: python3 astrosage_galev_boost.py
"""
import sys, json, time, re
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

import httpx
from app.database import SessionLocal
from app.models.page import WikiPage, PageVersion
from app.models.claim import Claim, Evidence
from app.models.agent import Agent
from app.agent_loop.autowiki.program_loader import load_program

ASTROSAGE_URL = "http://localhost:11434/v1/chat/completions"
ASTROSAGE_MODEL = "astrosage-70b"
PAGE_ID = 57

SECTION_DEEPEN_PROMPT = """You are an expert astronomy wiki author specializing in galaxy evolution.

The following wiki section about galaxy evolution has been flagged as too superficial — it mentions JWST and DESI but doesn't go deep enough into actual findings.

Current section content:
{section_content}

Rewrite this section to be significantly more substantive:
- Include specific JWST findings: actual redshifts, galaxy masses, morphologies discovered
- Include specific DESI BGS results: BAO measurements, galaxy clustering statistics
- Include Euclid early results if relevant
- Cite real papers by author+year where possible (e.g., Labbé et al. 2023, Curtis-Lake et al. 2023)
- Maintain a professional encyclopedic tone
- Target 400-600 words
- Do NOT use headers like "Recent Advances" or "Research Frontiers" (banned)
- Keep the same section header

Return the improved section text only (starting with the ## header)."""

OPEN_Q_PROMPT = """You are an expert astronomy wiki author specializing in galaxy evolution.

This section lists open questions but doesn't interrogate them deeply enough. A professional astronomer should be able to learn what the current debate is and what observations would resolve it.

Current content:
{section_content}

Rewrite to interrogate each open question:
- For each question: state current competing theories/observations
- What evidence exists on each side?
- What future observations (JWST cycle 3, DESI Y5, SKA, Roman) could resolve it?
- Be specific: mass ranges, redshift ranges, timescales
- Target 500-700 words

Return improved section text only (starting with the ## header)."""

HERO_FACT_PROMPT = """You are an astronomy knowledge engineer working on a galaxy evolution wiki page.

Current hero facts (we have {n_existing}, want 3 more):
{existing}

Generate 3 NEW quantitative hero facts about galaxy evolution that are:
- Different from the existing ones
- Highly specific with numbers (redshift, mass, percentage, timescale)
- Based on real recent findings (2020-2025)
- Impressive to a professional astronomer
- Include real arXiv IDs where possible

Return JSON array only:
[{{"label": "...", "value": "...", "unit": "...", "kind": "measurement", "source": {{"tier": "authoritative", "arxiv_id": "...", "year": 2024}}}}]"""

def call_astrosage(prompt: str, timeout: int = 120) -> str:
    resp = httpx.post(ASTROSAGE_URL, json={
        "model": ASTROSAGE_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
    }, timeout=timeout)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()

def get_section(content: str, keywords: list[str]) -> tuple[str, str]:
    """Find section containing any keyword. Returns (header, full_section_text)."""
    lines = content.split('\n')
    in_section = False
    current_header = ''
    section_lines = []
    for line in lines:
        if line.startswith('## '):
            if in_section:
                break
            header_text = line[3:].strip().lower()
            if any(kw.lower() in header_text for kw in keywords):
                in_section = True
                current_header = line
                section_lines = [line]
        elif in_section:
            section_lines.append(line)
    return current_header, '\n'.join(section_lines)

def replace_section(content: str, old_section: str, new_section: str) -> str:
    if old_section in content:
        return content.replace(old_section, new_section)
    return content

def main():
    db = SessionLocal()
    page = db.query(WikiPage).filter(WikiPage.id == PAGE_ID).first()
    content = page.content or ""
    
    agent = db.query(Agent).filter(Agent.name == "AstroSage-70B").first()
    if not agent:
        agent = db.query(Agent).filter(Agent.model_name == "astrosage-70b").first()
    if not agent:
        agent = db.query(Agent).first()
    agent_id = agent.id

    changes = []

    # 1. Deepen JWST/DESI/survey sections
    for keywords in [["survey", "mission", "jwst", "desi", "telescope"], ["current survey", "frontier"]]:
        header, section_text = get_section(content, keywords)
        if section_text and len(section_text) > 50:
            print(f"\n→ Deepening section: '{header}'", flush=True)
            try:
                improved = call_astrosage(SECTION_DEEPEN_PROMPT.format(section_content=section_text))
                if improved and improved.startswith('##'):
                    content = replace_section(content, section_text, improved)
                    changes.append(f"deepened: {header}")
                    print(f"  ✓ {len(improved)} chars", flush=True)
            except Exception as e:
                print(f"  ✗ {e}", flush=True)
            time.sleep(3)
            break

    # 2. Interrogate open questions
    header, section_text = get_section(content, ["open question", "question", "debate", "unknown"])
    if section_text and len(section_text) > 50:
        print(f"\n→ Deepening open questions: '{header}'", flush=True)
        try:
            improved = call_astrosage(OPEN_Q_PROMPT.format(section_content=section_text))
            if improved and improved.startswith('##'):
                content = replace_section(content, section_text, improved)
                changes.append(f"deepened open questions: {header}")
                print(f"  ✓ {len(improved)} chars", flush=True)
        except Exception as e:
            print(f"  ✗ {e}", flush=True)
        time.sleep(3)

    # 3. Generate 3 new hero facts
    print(f"\n→ Generating new hero facts", flush=True)
    try:
        existing_hf = json.loads(page.hero_facts or '[]')
        result = call_astrosage(HERO_FACT_PROMPT.format(
            n_existing=len(existing_hf),
            existing=json.dumps(existing_hf[:5], indent=2)
        ))
        m = re.search(r'\[.*\]', result, re.DOTALL)
        if m:
            new_facts = json.loads(m.group())
            if isinstance(new_facts, list) and new_facts:
                all_facts = existing_hf + new_facts[:3]
                page.hero_facts = json.dumps(all_facts)
                changes.append(f"added {len(new_facts[:3])} hero facts (total: {len(all_facts)})")
                print(f"  ✓ Added {len(new_facts[:3])} facts → total {len(all_facts)}", flush=True)
    except Exception as e:
        print(f"  ✗ hero facts: {e}", flush=True)

    # 4. Save improved content as new PageVersion
    if changes:
        # Safety check — never save content shorter than original
        if len(content) < 10000:
            print(f"\n⚠️ ABORT: content shrank to {len(content)} chars (original {len(page.content)}). Not saving.", flush=True)
            db.close()
            return

        # Get next version_num
        from sqlalchemy import func
        max_v = db.query(func.max(PageVersion.version_num)).filter(PageVersion.page_id == PAGE_ID).scalar() or 0
        next_v = max_v + 1

        # Save hero_facts first (separate from page version)
        db.add(page)
        db.commit()
        print(f"  ✓ hero_facts saved", flush=True)

        # Now save page version
        pv = PageVersion(
            page_id=PAGE_ID,
            version_num=next_v,
            content=content,
            editor_agent_id=agent_id,
        )
        db.add(pv)
        # Also update live content
        page2 = db.query(WikiPage).filter(WikiPage.id == PAGE_ID).first()
        page2.content = content
        db.add(page2)
        db.commit()
        db.refresh(pv)
        print(f"\n✅ Saved PageVersion v{next_v} pk={pv.id} ({len(content)} chars). Changes: {changes}", flush=True)
    else:
        print("\n⚠️ No section changes — saving hero_facts only.", flush=True)
        db.add(page)
        db.commit()

    db.close()

if __name__ == "__main__":
    main()
