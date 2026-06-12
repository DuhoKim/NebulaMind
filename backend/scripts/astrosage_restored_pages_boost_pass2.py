#!/usr/bin/env python3
"""
AstroSage-70B quality boost — pass 2.
Same 10 lowest-health restored pages as pass 1, but targets the NEXT weakest
section — skipping any section already >= 200 words (already improved).
"""
import json
import logging
import sys
import time

import httpx

sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')
from app.database import SessionLocal
from app.models.page import WikiPage

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger(__name__)

API_BASE = "http://localhost:8000"
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "astrosage-70b"
ASTROSAGE_ID = 55
ASTROSAGE_KEY = "7236f3c27a534038857d4e3d12e32f84"
TOP_N = 10
IMPROVED_WORD_THRESHOLD = 200

RESTORED_SLUGS = [
    "tidal-forces", "interstellar-medium", "binary-stars",
    "exoplanet-detection-methods", "reionization", "spacetime",
    "supernovae", "white-dwarfs", "cosmic-inflation",
    "cosmic-microwave-background", "planetary-formation", "black-holes",
    "magnetars", "fast-radio-bursts", "milky-way", "galaxy-clusters",
    "black-hole-mergers", "dark-matter", "red-giants",
    "baryon-acoustic-oscillations", "habitable-zone", "planetary-nebulae",
    "oort-cloud", "kuiper-belt", "exoplanets", "galaxy-formation",
    "hawking-radiation", "gamma-ray-bursts",
]

SKIP_SECTIONS = {"see also", "references", "further reading", "external links", "bibliography"}

REWRITE_SYSTEM = (
    "You are AstroSage, an expert astronomy wiki editor. "
    "Rewrite the given wiki section to be substantive, specific, and well-cited. "
    "Keep the ## header line unchanged. Return only the improved section in markdown — "
    "no JSON, no preamble, no trailing commentary."
)

REWRITE_PROMPT = """\
Wiki page: {title}

Current section (needs quality improvement — it is the shortest/weakest section):
{section}

Requirements:
- Keep the ## header line exactly as-is
- Minimum 200 words below the header
- Include 2–4 inline citations (Author et al. YYYY) for real published work
- Mention specific instruments, missions, datasets, or quantitative findings
- Maintain encyclopedic, research-review tone
- No vague statements or marketing language

Return only the improved markdown section:"""


def get_lowest_health_pages(slugs: list[str], top_n: int) -> list[dict]:
    db = SessionLocal()
    try:
        pages = (
            db.query(WikiPage.id, WikiPage.slug, WikiPage.title, WikiPage.health_score)
            .filter(WikiPage.slug.in_(slugs))
            .filter(WikiPage.id != 57)
            .all()
        )
        ranked = sorted(
            [{"id": p.id, "slug": p.slug, "title": p.title, "health": float(p.health_score or 0)}
             for p in pages],
            key=lambda x: x["health"],
        )
        log.info("Found %d pages in DB, selecting %d lowest-health", len(ranked), top_n)
        for p in ranked[:top_n]:
            log.info("  [%.1f] %s (id=%d)", p["health"], p["slug"], p["id"])
        return ranked[:top_n]
    finally:
        db.close()


def fetch_page_content(slug: str) -> tuple[str, str]:
    r = httpx.get(f"{API_BASE}/api/pages/{slug}", timeout=20)
    r.raise_for_status()
    d = r.json()
    return d.get("content", ""), d.get("title", slug)


def section_word_count(lines: list[str]) -> int:
    return sum(len(l.split()) for l in lines)


def pick_next_weakest_section(content: str) -> tuple[str, str]:
    """Return (header, text) of the shortest non-reference section that is < 200 words.

    Sections already >= IMPROVED_WORD_THRESHOLD are considered done from pass 1 and skipped.
    """
    sections: list[tuple[str, list[str]]] = []
    current_header = None
    current_lines: list[str] = []

    for line in content.split("\n"):
        if line.startswith("## "):
            if current_header is not None:
                sections.append((current_header, current_lines))
            current_header = line
            current_lines = [line]
        elif current_header is not None:
            current_lines.append(line)

    if current_header is not None:
        sections.append((current_header, current_lines))

    candidates = [
        (hdr, lines)
        for hdr, lines in sections
        if (
            hdr.lstrip("# ").strip().lower() not in SKIP_SECTIONS
            and len(lines) > 1
            and section_word_count(lines) < IMPROVED_WORD_THRESHOLD
        )
    ]

    if not candidates:
        log.info("  All non-reference sections are already >= %d words — nothing to rewrite",
                 IMPROVED_WORD_THRESHOLD)
        return "", ""

    hdr, lines = min(candidates, key=lambda x: section_word_count(x[1]))
    return hdr, "\n".join(lines)


def call_astrosage(title: str, section: str) -> str:
    resp = httpx.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": REWRITE_SYSTEM},
                {"role": "user", "content": REWRITE_PROMPT.format(title=title, section=section)},
            ],
            "temperature": 0.5,
        },
        timeout=150,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()


def replace_section_text(content: str, section_header: str, new_section: str) -> str:
    lines = content.split("\n")
    result = []
    in_target = False
    replaced = False
    for line in lines:
        if line.startswith("## ") and line.strip() == section_header.strip():
            in_target = True
            result.extend(new_section.split("\n"))
            replaced = True
            continue
        elif line.startswith("## ") and in_target:
            in_target = False
        if not in_target:
            result.append(line)
    if not replaced:
        result.extend(new_section.split("\n"))
    return "\n".join(result)


def submit_edit(page_id: int, new_content: str, summary: str) -> dict:
    r = httpx.post(
        f"{API_BASE}/api/edits",
        headers={"x-api-key": ASTROSAGE_KEY},
        json={
            "page_id": page_id,
            "agent_id": ASTROSAGE_ID,
            "content": new_content,
            "summary": summary,
        },
        timeout=20,
    )
    r.raise_for_status()
    return r.json()


def main():
    log.info("=== AstroSage Restored Pages Boost — Pass 2 ===")
    log.info("Skipping sections already >= %d words", IMPROVED_WORD_THRESHOLD)
    log.info("Selecting %d lowest-health pages from %d restored slugs", TOP_N, len(RESTORED_SLUGS))

    targets = get_lowest_health_pages(RESTORED_SLUGS, TOP_N)
    if not targets:
        log.error("No target pages found — aborting.")
        sys.exit(1)

    submitted = 0
    failed = 0
    skipped_all_done = 0

    for entry in targets:
        page_id = entry["id"]
        slug = entry["slug"]
        title = entry["title"]
        health = entry["health"]

        log.info("")
        log.info("=" * 60)
        log.info("Page: %s (id=%d, health=%.1f)", slug, page_id, health)
        log.info("=" * 60)

        try:
            content, api_title = fetch_page_content(slug)
            if api_title:
                title = api_title
        except Exception as exc:
            log.error("Failed to fetch %s: %s", slug, exc)
            failed += 1
            continue

        if not content:
            log.warning("Empty content for %s — skipping", slug)
            failed += 1
            continue

        section_header, section_text = pick_next_weakest_section(content)
        if not section_text:
            skipped_all_done += 1
            continue

        word_count = section_word_count(section_text.split("\n"))
        log.info("Target section: '%s' (%d words)", section_header, word_count)

        try:
            improved = call_astrosage(title, section_text)
        except Exception as exc:
            log.error("AstroSage call failed for %s: %s", slug, exc)
            failed += 1
            time.sleep(3)
            continue

        if not improved or not improved.startswith("##"):
            log.warning("AstroSage returned unexpected output for %s — skipping", slug)
            failed += 1
            time.sleep(2)
            continue

        new_content = replace_section_text(content, section_header, improved)

        if len(new_content) < len(content) * 0.9:
            log.error("Safety abort: new content too short (%d vs %d) for %s",
                      len(new_content), len(content), slug)
            failed += 1
            continue

        summary = (
            f"AstroSage-70B pass2 rewrite of '{section_header.lstrip('# ').strip()}' "
            f"[restored_pages_boost_p2, health={health:.1f}]"
        )

        try:
            result = submit_edit(page_id, new_content, summary)
            submitted += 1
            log.info("Submitted edit #%d for %s (+%d chars)",
                     result["id"], slug, len(new_content) - len(content))
        except Exception as exc:
            log.error("Edit submission failed for %s: %s", slug, exc)
            failed += 1

        time.sleep(4)

    log.info("")
    log.info("=== Done. submitted=%d failed=%d skipped_all_done=%d ===",
             submitted, failed, skipped_all_done)


if __name__ == "__main__":
    main()
