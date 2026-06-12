#!/usr/bin/env python3
"""
Tera (qwen3.6:27b-nvfp4) page section quality auditor.
Scans all wiki pages, classifies each ## section as: good / thin / generic / needs_citation
Writes results to ~/NebulaMind/logs/tera_section_audit.json for the renovation queue.

Run: python3 tera_section_audit.py
"""
import sys, json, time, re
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

import httpx
from app.database import SessionLocal
from app.models.page import WikiPage

TERA_URL = "http://localhost:11434/v1/chat/completions"
TERA_MODEL = "qwen3.6:27b-nvfp4"
OUTPUT = "/Users/duhokim/NebulaMind/logs/tera_section_audit.json"
SKIP_SECTIONS = {"See Also", "References", "Further Reading", "External Links"}

AUDIT_PROMPT = """You are a scientific wiki quality auditor. Classify this wiki section's quality.

Page: {page_title}
Section: {section_header}
Content (first 600 chars):
{content}

Classify as ONE of:
- "good" — substantive, specific, has data/numbers or citations
- "thin" — too short (<150 words), lacks depth
- "generic" — vague, no specifics, could describe any topic
- "needs_citation" — makes claims without citing sources

Return JSON only: {{"quality": "good|thin|generic|needs_citation", "word_count": N, "reason": "one sentence"}}"""

def parse_sections(content: str) -> list[tuple[str, str]]:
    """Extract (header, body) pairs from markdown."""
    sections = []
    current_header = None
    current_lines = []
    for line in content.split('\n'):
        if line.startswith('## ') and not line.startswith('### '):
            if current_header:
                sections.append((current_header, '\n'.join(current_lines)))
            current_header = line[3:].strip()
            current_lines = []
        elif current_header:
            current_lines.append(line)
    if current_header:
        sections.append((current_header, '\n'.join(current_lines)))
    return sections

def call_tera(page_title: str, section_header: str, content: str) -> dict | None:
    prompt = AUDIT_PROMPT.format(
        page_title=page_title,
        section_header=section_header,
        content=content[:600],
    )
    try:
        resp = httpx.post(TERA_URL, json={
            "model": TERA_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
        }, timeout=45)
        resp.raise_for_status()
        text = resp.json()["choices"][0]["message"]["content"].strip()
        m = re.search(r'\{.*?\}', text, re.DOTALL)
        if m:
            return json.loads(m.group())
    except Exception as e:
        print(f"    tera error: {e}", flush=True)
    return None

def main():
    db = SessionLocal()
    pages = db.query(WikiPage).filter(WikiPage.id != 57).all()  # skip galaxy-evolution (protected)
    db.close()

    results = []
    total_sections = 0
    issues = 0

    for page in pages:
        if not page.content:
            continue
        sections = parse_sections(page.content)
        page_issues = []

        for header, body in sections:
            if header in SKIP_SECTIONS:
                continue
            total_sections += 1
            print(f"  [{page.slug}] § {header[:40]}", flush=True)
            audit = call_tera(page.title, header, body)
            if audit and audit.get("quality") != "good":
                page_issues.append({
                    "section": header,
                    "quality": audit.get("quality"),
                    "word_count": audit.get("word_count", 0),
                    "reason": audit.get("reason", ""),
                })
                issues += 1
            time.sleep(1)

        if page_issues:
            results.append({
                "page_id": page.id,
                "slug": page.slug,
                "title": page.title,
                "health_score": page.health_score,
                "issues": page_issues,
            })
            print(f"  → {len(page_issues)} issues on {page.slug}", flush=True)

    with open(OUTPUT, "w") as f:
        json.dump({"total_sections": total_sections, "issues": issues, "pages": results}, f, indent=2)

    print(f"\n✅ Tera audit complete: {total_sections} sections, {issues} flagged → {OUTPUT}", flush=True)
    db_summary = {"total_sections": total_sections, "flagged": issues, "pages_with_issues": len(results)}
    print(json.dumps(db_summary), flush=True)

if __name__ == "__main__":
    main()
