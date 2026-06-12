#!/usr/bin/env python3
"""
One-shot: enrich wiki pages' Current Research sections with top evidence.
Uses local Ollama qwen3.6:27b-nvfp4. ~30s per page, ~21 min for all 42.

Usage:
  .venv/bin/python3 scripts/enrich_pages_from_evidence.py --dry-run --limit 3
  .venv/bin/python3 scripts/enrich_pages_from_evidence.py --apply
"""
import sys, os, argparse, json, urllib.request, re, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.page import WikiPage
from app.models.claim import Claim, Evidence
from app.services.llm_utils import strip_think_blocks

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "qwen3.6:27b-nvfp4"

SYSTEM = """You are an astronomy wiki editor enriching a 'Current Research' section with recent findings.

Rules:
- Preserve ALL existing factual content from the current section
- Integrate 3-5 new findings from the provided papers naturally
- Cite papers inline as (Author Year) — use the first author's last name
- Output ONLY the new section starting with ## Current Research
- Length: 800-1500 characters
- Do not invent claims not supported by the abstracts
- Write in clear, encyclopedic English"""

def call_ollama(user: str) -> str:
    data = json.dumps({
        "model": MODEL,
        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
        "stream": False,
        "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(OLLAMA_URL, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        content = json.loads(r.read())["choices"][0]["message"]["content"]
        content = strip_think_blocks(content)
        return content

def extract_section(content: str, section_name: str) -> str:
    pattern = rf'(## {re.escape(section_name)}.*?)(?=\n## |\Z)'
    m = re.search(pattern, content, re.DOTALL)
    return m.group(1).strip() if m else ""

def replace_section(content: str, section_name: str, new_section: str) -> str:
    pattern = rf'(## {re.escape(section_name)}.*?)(?=\n## |\Z)'
    m = re.search(pattern, content, re.DOTALL)
    if m:
        return content[:m.start()] + new_section + "\n\n" + content[m.end():]
    # If section doesn't exist, append it
    return content.rstrip() + "\n\n" + new_section

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", default=False)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    db = SessionLocal()
    try:
        pages = db.query(WikiPage).filter(WikiPage.content != "").all()
        if args.limit:
            pages = pages[:args.limit]

        mode = "APPLYING" if args.apply else "DRY RUN"
        print(f"{'='*60}")
        print(f"EVIDENCE ENRICHMENT — {mode}")
        print(f"Pages: {len(pages)}")
        print()

        enriched = 0
        for i, page in enumerate(pages, 1):
            # Get top 5 evidence
            top_ev = (
                db.query(Evidence)
                .join(Claim, Evidence.claim_id == Claim.id)
                .filter(Claim.page_id == page.id, Evidence.quality >= 0.40, Evidence.abstract.isnot(None))
                .order_by(Evidence.quality.desc(), Evidence.year.desc())
                .limit(5)
                .all()
            )
            if not top_ev:
                print(f"[{i}/{len(pages)}] {page.slug}: no quality evidence, skip")
                continue

            current_section = extract_section(page.content, "Current Research")
            if not current_section:
                print(f"[{i}/{len(pages)}] {page.slug}: no Current Research section, skip")
                continue

            papers_text = "\n\n".join(
                f"{j+1}. {ev.title} ({ev.year or 'n.d.'})\n   "
                + (ev.abstract[:400] + "..." if ev.abstract else "No abstract.")
                for j, ev in enumerate(top_ev)
            )
            user_prompt = (
                f"Page: {page.title}\n\n"
                f"Current 'Current Research' section:\n{current_section}\n\n"
                f"5 papers to integrate:\n{papers_text}\n\n"
                f"Rewrite the Current Research section integrating findings from these papers."
            )

            try:
                print(f"[{i}/{len(pages)}] {page.slug}... ", end="", flush=True)
                new_section = call_ollama(user_prompt)
                if not new_section.startswith("## Current Research"):
                    print(f"SKIP (malformed output)")
                    continue
                old_len = len(current_section)
                new_len = len(new_section)
                print(f"OK ({old_len} → {new_len} chars)")
                if args.apply:
                    page.content = replace_section(page.content, "Current Research", new_section)
                    db.commit()
                    enriched += 1
                time.sleep(2)
            except Exception as e:
                print(f"ERROR: {e}")

        print(f"\n{'='*60}")
        print(f"Done: {enriched} pages enriched" if args.apply else "Dry run complete")
    finally:
        db.close()

if __name__ == "__main__":
    main()
