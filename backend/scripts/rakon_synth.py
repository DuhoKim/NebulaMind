#!/usr/bin/env python3
"""
Generic Rakon synthesis script — any NebulaMind wiki page.

Generalizes rakon_synth_galaxy_evolution.py to accept --page-slug / --page-id.
Builds a rigorous, 9-section graduate-level astronomy wiki page via deepseek-r1:671b.

Usage:
    python3 scripts/rakon_synth.py --page-slug dark-matter --page-id 10 --apply
    python3 scripts/rakon_synth.py --page-slug oort-cloud  --page-id 30            # dry-run
    python3 scripts/rakon_synth.py --page-slug dark-matter --page-id 10 --apply --section Overview
"""
import sys, json, re, urllib.request, argparse, time
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from app.database import SessionLocal
from app.models.page import WikiPage, PageVersion
from app.models.claim import Claim, Evidence
from app.services.llm_utils import strip_think_blocks
from app.models.agent import Agent

RAKON_URL = "http://192.188.0.4:11434/v1/chat/completions"
MODEL     = "deepseek-r1:671b"
TIMEOUT   = 600  # 10 min per section

PROVENANCE_FOOTER = "\n\n🤖 Synthesized by 671B model"

# ---------------------------------------------------------------------------
# §A.7.3 Prompt templates (locked 2026-05-08)
# ---------------------------------------------------------------------------
SYSTEM_TEMPLATE = """You are writing a section of a graduate-research-grade astronomy wiki page.
Audience: PhD astronomers and postdocs. Tone: rigorous, citation-rich,
no pop-science framing. Length: 800-1200 chars per section unless specified.

Section: {section_name}
Page: {page_slug}
Page title: {page_title}
Existing prose (reference only, you may ignore): {existing_text}
Required content beats: {section_beats}
Available high-quality evidence (use these citations): {top_evidence}
Required claim count: {claim_count}
Each claim must be a clean, falsifiable, single-sentence proposition that
can stand alone as a Claim row. Mark each [CLAIM:established] or
[CLAIM:debate] inline so downstream parsing can extract them.

Constraints:
- No phrases like "scientists have discovered", "groundbreaking", "unlocks
  the secrets of", "biodiversity", or any pop-science framing.
- Cite specific papers by author + year + arXiv ID when available.
- Numbers, regimes, and uncertainties wherever possible.
- No first-person ("we", "our").
- DO NOT include URLs, dataset links, or download instructions. The page is
  a pure scientific narrative; tooling lives in a separate feature."""

USER_TEMPLATE = "Write the ## {section_name} section now."

# ---------------------------------------------------------------------------
# Generic 9-section template, per-page beats injected at runtime
# ---------------------------------------------------------------------------
GENERIC_SECTIONS = [
    {
        "name": "Overview",
        "h2": "## Overview",
        "claim_count": 2,
        "beats_template": (
            "Define {topic} as a quantitative astrophysical / cosmological subject. "
            "State the governing physics (1-2 regimes). "
            "Name the observational anchors that constrain the field. "
            "Anchor contemporary frontiers: what is actively contested or measured."
        ),
    },
    {
        "name": "Discovery and Historical Framework",
        "h2": "## Discovery and Historical Framework",
        "claim_count": 3,
        "beats_template": (
            "Trace the key milestones in understanding {topic}: "
            "early theoretical predictions, first observational confirmations, "
            "major surveys/experiments (1990s–2010s), and 2020s JWST/DESI/Euclid era. "
            "Cite specific papers with author + year."
        ),
    },
    {
        "name": "Physical Mechanisms",
        "h2": "## Physical Mechanisms",
        "claim_count": 5,
        "beats_template": (
            "Cover 3-4 subsections of core physics for {topic}: "
            "governing equations and parameter regimes, "
            "dominant interaction channels, "
            "energy/mass/time scales involved, "
            "theoretical frameworks (simulations, analytic models). "
            "Be quantitative: cite observational constraints and simulation results."
        ),
    },
    {
        "name": "Observations and Evidence",
        "h2": "## Observations and Evidence",
        "claim_count": 4,
        "beats_template": (
            "Survey observational probes of {topic}: "
            "flagship surveys and instruments (spectroscopic, photometric, radio, X-ray), "
            "key datasets and their statistical power, "
            "signal-to-noise / systematic floor reached, "
            "concordance/tension with theory. "
            "Prefer post-2015 results; include 2024-2026 where available."
        ),
    },
    {
        "name": "Connections to Other Fields",
        "h2": "## Connections to Other Fields",
        "claim_count": 2,
        "beats_template": (
            "Describe how {topic} connects to at least 3 other subfields of astrophysics "
            "or cosmology (e.g. galaxy formation, CMB, gravitational waves, stellar physics). "
            "Highlight where {topic} serves as an input to another field and vice versa."
        ),
    },
    {
        "name": "Open Questions and Active Debates",
        "h2": "## Open Questions and Active Debates",
        "claim_count": 4,
        "beats_template": (
            "Identify 4-6 specific contested claims or open questions in {topic} research. "
            "For each: frame the debate, name the competing models/camps, "
            "cite the key papers on each side, and state what observation would resolve it. "
            "Use [CLAIM:debate] markers inline. Be specific — no vague 'more research needed'."
        ),
    },
    {
        "name": "Recent Advances (2024–2026)",
        "h2": "## Recent Advances (2024–2026)",
        "claim_count": 2,
        "beats_template": (
            "Describe 4-5 concrete results from 2024-2026 on {topic}. "
            "Each result: ~150 chars, arXiv ID required if available, "
            "quantitative finding (measurement, detection, limit). "
            "Prefer results from JWST, DESI, Euclid, ALMA, or theoretical breakthroughs."
        ),
    },
    {
        "name": "See Also",
        "h2": "## See Also",
        "claim_count": 0,
        "beats_template": (
            "List 5-7 cross-links to related NebulaMind wiki pages (as slug names). "
            "This section is SHORT — just a bullet list, no prose needed."
        ),
    },
    {
        "name": "References",
        "h2": "## References",
        "claim_count": 0,
        "beats_template": (
            "List 15-22 key references for {topic} in standard academic format: "
            "Author(s) + year + abbreviated title + journal/arXiv ID. "
            "Cover foundational papers, major review articles, and 2024-2026 highlights. "
            "This section is a formatted list — no prose."
        ),
    },
]


def build_sections(page_slug: str, page_title: str) -> list[dict]:
    topic = page_title or page_slug.replace("-", " ")
    sections = []
    for s in GENERIC_SECTIONS:
        sec = dict(s)
        sec["beats"] = s["beats_template"].format(topic=topic)
        sections.append(sec)
    return sections


def call_rakon(system: str, user: str) -> str:
    payload = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user",   "content": user},
        ],
        "stream": False,
        "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(
        RAKON_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        content = json.loads(r.read())["choices"][0]["message"]["content"]
    return strip_think_blocks(content)


def get_evidence_for_page(db, page_id: int, limit: int = 15) -> list[dict]:
    rows = (
        db.query(Evidence)
        .join(Claim, Evidence.claim_id == Claim.id)
        .filter(Claim.page_id == page_id, Evidence.quality >= 0.50)
        .order_by(Evidence.quality.desc())
        .limit(limit)
        .all()
    )
    return [
        {
            "arxiv_id": e.arxiv_id or "n/a",
            "title": e.title or "",
            "year": e.year or "",
            "summary": (e.summary or "")[:200],
        }
        for e in rows
    ]


def get_section_text(content: str, section_h2: str) -> str:
    pattern = re.escape(section_h2) + r'(.*?)(?=\n## |\Z)'
    m = re.search(pattern, content, re.DOTALL)
    if m:
        return m.group(1).strip()[:800]
    return "(section not yet written)"


def run_section(db, page: WikiPage, sec: dict, page_id: int, apply: bool) -> str | None:
    evidence = get_evidence_for_page(db, page_id, limit=15)
    ev_text = "\n".join(
        f"- [{e['arxiv_id']}] {e['title']} ({e['year']}): {e['summary']}"
        for e in evidence
    ) or "(no evidence rows yet)"

    existing = get_section_text(page.content or "", sec["h2"])

    system = SYSTEM_TEMPLATE.format(
        section_name=sec["name"],
        page_slug=page.slug,
        page_title=page.title or page.slug,
        existing_text=existing,
        section_beats=sec["beats"],
        top_evidence=ev_text,
        claim_count=sec["claim_count"],
    )
    user = USER_TEMPLATE.format(section_name=sec["name"])

    if not apply:
        print(f"\n{'='*60}")
        print(f"[DRY RUN] Section: {sec['name']}")
        print(f"System prompt length: {len(system)} chars")
        return None

    print(f"\n→ Synthesizing: {sec['name']} ...", flush=True)
    t0 = time.time()
    try:
        output = call_rakon(system, user)
        elapsed = time.time() - t0
        print(f"  ✓ {len(output)} chars in {elapsed:.0f}s", flush=True)
        return output
    except Exception as e:
        print(f"  ✗ ERROR: {e}", flush=True)
        return None


def save_page_version(db, page: WikiPage, full_content: str, agent_id: int | None) -> None:
    latest = (
        db.query(PageVersion)
        .filter(PageVersion.page_id == page.id)
        .order_by(PageVersion.version_num.desc())
        .first()
    )
    next_num = (latest.version_num + 1) if latest else 1
    pv = PageVersion(
        page_id=page.id,
        version_num=next_num,
        content=full_content,
        editor_agent_id=agent_id,
    )
    db.add(pv)
    db.commit()
    print(f"\n✓ Saved PageVersion #{next_num} for page_id={page.id} ({page.slug})")
    print("  → Review and promote when satisfied")


def main() -> None:
    parser = argparse.ArgumentParser(description="Rakon synthesis for any NebulaMind wiki page")
    parser.add_argument("--page-slug", required=True, help="Wiki page slug (e.g. dark-matter)")
    parser.add_argument("--page-id", required=True, type=int, help="Wiki page DB id")
    parser.add_argument("--apply", action="store_true", help="actually call Rakon and save")
    parser.add_argument("--section", help="synthesize only this section (by name substring)")
    args = parser.parse_args()

    db = SessionLocal()
    try:
        page = db.query(WikiPage).filter(WikiPage.id == args.page_id).first()
        if not page:
            print(f"ERROR: page_id={args.page_id} not found")
            return
        if page.slug != args.page_slug:
            print(f"WARNING: page_id={args.page_id} has slug '{page.slug}', not '{args.page_slug}'")

        agent = (
            db.query(Agent).filter(Agent.name.ilike("%tori%")).first()
            or db.query(Agent).first()
        )
        agent_id = agent.id if agent else None

        sections = build_sections(page.slug, page.title or "")

        sections_to_run = sections
        if args.section:
            sections_to_run = [s for s in sections if args.section.lower() in s["name"].lower()]
            if not sections_to_run:
                print(f"No section matching '{args.section}'")
                return

        if not args.apply:
            print(f"DRY RUN — page='{page.slug}' (id={page.id}), {len(sections_to_run)} sections")
            print(f"Model: {MODEL} @ {RAKON_URL}")
            for sec in sections_to_run:
                run_section(db, page, sec, args.page_id, apply=False)
            print("\nRun with --apply to send to Rakon.")
            return

        built_sections: dict[str, str] = {}
        for sec in sections_to_run:
            result = run_section(db, page, sec, args.page_id, apply=True)
            if result:
                built_sections[sec["h2"]] = result

        if not built_sections:
            print("No sections synthesized.")
            return

        new_content_parts = [f"# {page.title or page.slug.replace('-', ' ').title()}"]
        for sec in sections:
            if sec["h2"] in built_sections:
                new_content_parts.append(f"\n{sec['h2']}\n\n{built_sections[sec['h2']]}")
            else:
                existing = get_section_text(page.content or "", sec["h2"])
                if existing and existing != "(section not yet written)":
                    new_content_parts.append(f"\n{sec['h2']}\n\n{existing}")

        full_content = "\n".join(new_content_parts) + PROVENANCE_FOOTER
        save_page_version(db, page, full_content, agent_id)

    finally:
        db.close()


if __name__ == "__main__":
    main()
