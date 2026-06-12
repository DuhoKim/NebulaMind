#!/usr/bin/env python3
"""AstroSage-70B: deepen galaxy-evolution CONTENT sections. No hero facts."""
import sys, json, time, re
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')
import httpx
from app.database import SessionLocal
from app.models.page import WikiPage, PageVersion
from sqlalchemy import func

PAGE_ID = 57
ASTROSAGE_URL = "http://localhost:11434/v1/chat/completions"
ASTROSAGE_MODEL = "astrosage-70b"

DEEPEN_PROMPT = """You are an expert astronomy wiki author. Deepen and improve this section of the galaxy evolution article.

The section must:
- Add specific quantitative findings (redshifts, masses, percentages, timescales)
- Reference real recent discoveries (2020-2025) with author+year
- Include JWST, DESI, Euclid findings where relevant
- Minimum 400 words
- Professional encyclopedic tone
- Keep the same ## header
- Do NOT start with "Galaxy evolution is a fascinating field" or similar filler

Current section:
{section_content}

Return the improved section text only (starting with ## header):"""

def parse_sections(content):
    sections, cur_h, cur_lines = [], None, []
    for line in content.split('\n'):
        if line.startswith('## ') and not line.startswith('### '):
            if cur_h: sections.append((cur_h, '\n'.join(cur_lines)))
            cur_h, cur_lines = line, [line]
        elif cur_h:
            cur_lines.append(line)
    if cur_h: sections.append((cur_h, '\n'.join(cur_lines)))
    return sections

def word_count(text):
    return len(text.split())

def call_astrosage(prompt):
    resp = httpx.post(ASTROSAGE_URL, json={
        "model": ASTROSAGE_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
    }, timeout=150)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()

def main():
    db = SessionLocal()
    page = db.query(WikiPage).filter(WikiPage.id==PAGE_ID).first()
    content = page.content or ""
    
    # Find agent
    from app.models.agent import Agent
    agent = db.query(Agent).filter(Agent.model_name=="astrosage-70b").first()
    if not agent: agent = db.query(Agent).first()
    
    SKIP = {"See Also", "References", "Further Reading", "External Links"}
    sections = parse_sections(content)
    
    # Sort by word count — target thinnest content sections
    candidates = [(h, body, word_count(body)) for h,body in sections
                  if h.replace('## ','').strip() not in SKIP and word_count(body) < 300]
    candidates.sort(key=lambda x: x[2])
    
    print(f"galaxy-evolution: {len(sections)} sections, {len(candidates)} thin (<300 words)", flush=True)
    
    changes = []
    for header, section_text, wc in candidates[:4]:  # improve up to 4 thin sections
        print(f"\n→ Deepening: '{header}' ({wc} words)", flush=True)
        try:
            improved = call_astrosage(DEEPEN_PROMPT.format(section_content=section_text))
            if improved and improved.startswith('##') and word_count(improved) > wc:
                content = content.replace(section_text, improved)
                changes.append(header)
                print(f"  ✓ {wc} → {word_count(improved)} words", flush=True)
            else:
                print(f"  ✗ No improvement", flush=True)
        except Exception as e:
            print(f"  ✗ {e}", flush=True)
        time.sleep(3)
    
    if changes and len(content) > 10000:
        max_v = db.query(func.max(PageVersion.version_num)).filter(PageVersion.page_id==PAGE_ID).scalar() or 0
        pv = PageVersion(page_id=PAGE_ID, version_num=max_v+1, content=content, editor_agent_id=agent.id)
        db.add(pv)
        page.content = content
        db.add(page)
        db.commit()
        print(f"\n✅ Saved v{max_v+1} ({len(content)}c). Deepened: {changes}", flush=True)
    else:
        print("\n⚠️ No changes or content too short — not saving.", flush=True)
    db.close()

if __name__=="__main__": main()
