#!/usr/bin/env python3
"""
Tori section fix: improve 14 thin sections flagged by Tera's audit.
Uses AstroSage-70B (agent_id=55) to rewrite each section, submits via POST /api/edits.
Priority: pages with lowest health_score first. Skip page_id=57.
"""
import json
import logging
import re
import sys
import time
import httpx

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

API_BASE = "http://localhost:8000"
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "astrosage-70b"
ASTROSAGE_ID = 55
ASTROSAGE_KEY = "7236f3c27a534038857d4e3d12e32f84"

AUDIT = [
    {"page_id": 55, "slug": "cosmic-web",                 "health": 23.3, "issues": [{"section": "Open Questions",   "quality": "thin"}]},
    {"page_id": 39, "slug": "red-giants",                 "health": 40.1, "issues": [{"section": "Open Questions",   "quality": "thin"}]},
    {"page_id": 22, "slug": "tidal-forces",               "health": 42.3, "issues": [{"section": "Open Questions",   "quality": "thin"}]},
    {"page_id": 11, "slug": "exoplanets",                 "health": 45.1, "issues": [{"section": "Open Questions",   "quality": "thin"}]},
    {"page_id": 18, "slug": "exoplanet-detection-methods","health": 46.8, "issues": [{"section": "Open Questions",   "quality": "thin"}]},
    {"page_id": 20, "slug": "galaxy-clusters",            "health": 50.6, "issues": [{"section": "Current Research", "quality": "thin"},
                                                                                       {"section": "Open Questions",   "quality": "thin"}]},
    {"page_id":  4, "slug": "cosmic-microwave-background","health": 50.9, "issues": [{"section": "Open Questions",   "quality": "thin"}]},
    {"page_id": 13, "slug": "kuiper-belt",                "health": 57.1, "issues": [{"section": "Open Questions",   "quality": "thin"}]},
    {"page_id": 23, "slug": "white-dwarfs",               "health": 59.6, "issues": [{"section": "Open Questions",   "quality": "thin"}]},
    {"page_id":  9, "slug": "active-galactic-nuclei",     "health": 62.1, "issues": [{"section": "Current Research", "quality": "thin"},
                                                                                       {"section": "Open Questions",   "quality": "thin"}]},
    {"page_id": 10, "slug": "dark-matter",                "health": 62.8, "issues": [{"section": "Open Questions",   "quality": "thin"}]},
    {"page_id": 29, "slug": "milky-way",                  "health": 64.6, "issues": [{"section": "Open Questions",   "quality": "thin"}]},
]
# Already sorted by health_score ascending (lowest = highest priority)
# Skip page_id=57 (galaxy-evolution — protected) — not in list anyway


def fetch_page_content(slug: str) -> tuple[str, str]:
    """Returns (content, title)."""
    r = httpx.get(f"{API_BASE}/api/pages/{slug}", timeout=15)
    r.raise_for_status()
    d = r.json()
    return d.get("content", ""), d.get("title", slug)


def extract_section(content: str, section_header: str) -> str:
    """Extract the text of a ## section from markdown content."""
    lines = content.split("\n")
    in_section = False
    section_lines = []
    for line in lines:
        if line.startswith("## ") and section_header.lower() in line.lower():
            in_section = True
        elif line.startswith("## ") and in_section:
            break
        if in_section:
            section_lines.append(line)
    return "\n".join(section_lines)


def replace_section(content: str, section_header: str, new_section: str) -> str:
    """Replace a ## section in the full content with new_section text."""
    lines = content.split("\n")
    result = []
    in_target = False
    replaced = False
    for line in lines:
        if line.startswith("## ") and section_header.lower() in line.lower():
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


def call_astrosage(page_title: str, section_header: str, current_section: str, quality: str) -> str:
    quality_note = {
        "thin": "expand with more detail, specific research findings, named missions/instruments, and inline citations like (Smith et al. 2023). Add sub-bullets or paragraphs under each listed question.",
        "generic": "add specific examples, quantitative findings, named discoveries/missions, and inline citations.",
        "needs_citation": "add inline citation hints like (Author et al. YYYY) after key claims.",
    }.get(quality, "improve depth and specificity")

    system = (
        "You are AstroSage, an expert astronomy wiki editor. "
        "Rewrite the given wiki section to be substantive, specific, and well-cited. "
        "Keep the ## header line. Return the improved section in markdown only — no JSON, no preamble."
    )
    prompt = (
        f"Wiki page: {page_title}\n\n"
        f"Current section (flagged as '{quality}'):\n{current_section}\n\n"
        f"Task: {quality_note}\n\n"
        "Requirements:\n"
        "- Keep the ## header unchanged\n"
        "- Minimum 150 words below the header\n"
        "- Include 2-4 inline citations (Author et al. YYYY) for real published work\n"
        "- Mention specific instruments, missions, or datasets where relevant\n"
        "- Maintain encyclopedic, research-review tone\n"
        "- No marketing language or vague promises\n\n"
        "Return only the improved markdown section:"
    )

    resp = httpx.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.6,
        },
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()


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


edits_submitted = 0
edits_failed = 0

for entry in AUDIT:
    page_id = entry["page_id"]
    slug = entry["slug"]
    health = entry["health"]

    try:
        content, title = fetch_page_content(slug)
    except Exception as exc:
        log.error("Failed to fetch %s: %s", slug, exc)
        edits_failed += 1
        continue

    # Accumulate all section improvements before submitting one edit per page
    improved_content = content
    summaries = []

    for issue in entry["issues"]:
        section_header = issue["section"]
        quality = issue["quality"]

        current_section = extract_section(content, section_header)
        if not current_section:
            log.warning("Section '%s' not found in %s — skipping", section_header, slug)
            continue

        log.info("Improving '%s' § %s (health=%.1f, quality=%s)",
                 slug, section_header, health, quality)
        try:
            new_section = call_astrosage(title, section_header, current_section, quality)
        except Exception as exc:
            log.error("AstroSage failed for %s § %s: %s", slug, section_header, exc)
            edits_failed += 1
            continue

        improved_content = replace_section(improved_content, section_header, new_section)
        summaries.append(f"Expand thin '{section_header}' section with detail and citations")
        log.info("  → improved (%d chars)", len(new_section))
        time.sleep(2)  # brief pause between Ollama calls

    if summaries and improved_content != content:
        summary_text = "; ".join(summaries) + f" [tori_section_fix, health={health}]"
        try:
            result = submit_edit(page_id, improved_content, summary_text)
            edits_submitted += 1
            log.info("Submitted edit #%d for %s", result["id"], slug)
        except Exception as exc:
            log.error("Edit submission failed for %s: %s", slug, exc)
            edits_failed += 1

    time.sleep(3)  # pace between pages

log.info("Done. edits_submitted=%d edits_failed=%d", edits_submitted, edits_failed)
