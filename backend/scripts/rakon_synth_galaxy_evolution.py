#!/usr/bin/env python3
"""
Rakon synthesis for galaxy-evolution page (page_id=57) — v3 dissolution model.

Implements §A.v3.5 prompt template from 설계_GalaxyEvolution_Research_v1.md (LOCKED).
8 content sections; debates D1-D10 woven into topical prose with HTML comment markers.
No standalone "Open Questions" or "Recent Advances" sections.

Usage:
    python3 scripts/rakon_synth_galaxy_evolution.py           # dry-run
    python3 scripts/rakon_synth_galaxy_evolution.py --apply   # send to Rakon + save PageVersion
    python3 scripts/rakon_synth_galaxy_evolution.py --section "Star Formation"  # single section
"""
import sys, json, re, urllib.request, urllib.error, argparse, time
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from app.database import SessionLocal
from app.models.page import WikiPage, PageVersion
from app.services.llm_utils import strip_think_blocks
from app.models.claim import Claim, Evidence
from app.models.agent import Agent

PAGE_ID   = 57
PAGE_SLUG = "galaxy-evolution"
RAKON_URL = "http://192.188.0.4:11434/v1/chat/completions"
MODEL     = "deepseek-r1:671b"
TIMEOUT   = 7200  # 2h hard cap (streaming keeps socket alive — this is a safety net only)
WARMUP_TIMEOUT = 300  # 5 min to confirm Rakon is responsive before synthesis

PROVENANCE_FOOTER = "\n\n🤖 Synthesized by 671B model"

# §A.v3.5 base template — filled per section
SYSTEM_TEMPLATE = """\
You are writing one section of a graduate-research-grade astronomy wiki page on \
galaxy evolution. Audience: PhD astronomers and postdocs. Tone: rigorous, citation-rich, \
no pop-science framing. Voice: Nature Reviews / Annual Reviews article — established science \
and contested ground appear in the same prose flow, not in separate containers.

Section: {section_name}
Target length: {target_chars} chars
Page: galaxy-evolution
Existing prose (reference only, you may ignore): {existing_text}
Required content beats: {section_beats}
Available high-quality evidence (use these citations): {top_evidence}
Required claim count for this section: {claim_count}

Each claim is a clean, falsifiable, single-sentence proposition that can stand alone as a \
Claim row. Mark each [CLAIM:established] inline so downstream parsing can extract them.

{debate_block}\
{highlight_block}\
Constraints:
- No phrases like "scientists have discovered", "groundbreaking", "unlocks the secrets of", \
"biodiversity", "revolutionized", "fundamentally altering", "unprecedented", \
"providing insights".
- Cite specific papers by Author+Year (arXiv:XXXX.XXXXX).
- Numbers, regimes, and uncertainties wherever possible.
- No first-person ("we", "our").
- DO NOT include URLs, dataset links, or download instructions. Tooling lives in a separate feature.
- DO NOT wrap your output in ```markdown code fences``` — emit raw markdown.
- Output a single section starting with the appropriate `## {section_name}` h2 and ending \
at the next h2 boundary (do not emit subsequent sections).\
"""

USER_TEMPLATE = "Write the ## {section_name} section now."

DEBATE_PREAMBLE = """\
DEBATES ASSIGNED TO THIS SECTION (weave each into the topical prose):
For each debate below:
- State the contested proposition naturally in the topical narrative.
- Cite at least one supporting paper and one challenging paper inline.
- Use phrasing like "remains debated", "competing interpretations", \
"while X argues ... Y finds ...", "recent JWST data suggests ...".
- Wrap the contested paragraph in HTML comments on lines of their own:
  <!-- claim:NNNN -->
  (paragraph text)
  <!-- /claim:NNNN -->
  (where NNNN is the numeric claim id listed below)
- Do NOT use a separate header, callout, or list for the debate.
- Do NOT use any of: D-numbering visible to reader, "Open Questions", \
"research agenda", "high-impact open problem", "where to dig next", "jump to debates".

{debate_items}
"""

HIGHLIGHT_PREAMBLE = """\
RECENT-ADVANCE HIGHLIGHT(S) ASSIGNED TO THIS SECTION (cite inline):
For each highlight below, weave naturally into the prose (one or two sentences referencing the paper):
{highlight_items}

"""

# ---------------------------------------------------------------------------
# §A.v3.3 Debate → section assignment with anchor papers
# ---------------------------------------------------------------------------
DEBATES = {
    1487: {
        "label": "D1", "section": "Star Formation & Quenching",
        "proposition": "Mass-quenching is separable from environment-quenching at fixed stellar mass and redshift",
        "supports": "Peng+2010 (arXiv:1003.4747)",
        "challenges": "Wetzel+2013; Bluck+2024",
    },
    1488: {
        "label": "D2", "section": "Dark Matter & Structure Formation",
        "proposition": "The most massive galaxies detected at z>10 in JWST imaging exceed stellar mass budgets permitted by ΛCDM",
        "supports": "Boylan-Kolchin 2023 (arXiv:2208.01611); Labbé+2023 (arXiv:2207.12446)",
        "challenges": "Lovell+2023; Adams+2024 (arXiv:2304.13721)",
    },
    1489: {
        "label": "D3", "section": "Star Formation & Quenching",
        "proposition": "The dust-obscured fraction of the cosmic star-formation-rate density at z=4–7 is ≥50%",
        "supports": "Zavala+2021; Algera+2023",
        "challenges": "Williams+2024 (arXiv:2310.03787)",
    },
    1490: {
        "label": "D4", "section": "Physical Mechanisms",
        "proposition": "Compact 'red nugget' galaxies at z~2 grow to present-day massive ellipticals primarily via dry minor mergers",
        "supports": "van Dokkum+2010; Naab+2009",
        "challenges": "Hopkins+2010; Gao+2024",
    },
    1491: {
        "label": "D5", "section": "AGN Feedback",
        "proposition": "AGN feedback at high redshift acts purely as a negative quenching mechanism, suppressing star formation",
        "supports": "Silk 2013; Maiolino+2024 (arXiv:2305.12492)",
        "challenges": "Kalfountzou+2017; Übler+2024",
    },
    1492: {
        "label": "D6", "section": "Environmental Effects",
        "proposition": "The Dressler morphology–density relation is driven by environment acting on galaxies after they form",
        "supports": "Dressler 1980; Smith+2005",
        "challenges": "van der Wel & Meidt 2025 (arXiv:2509.02847)",
    },
    1493: {
        "label": "D7", "section": "Environmental Effects",
        "proposition": "Mpc-scale cosmic web geometry modulates galaxy star-formation rates and morphologies beyond local density",
        "supports": "Tempel+2013; Daikuhara+2025 (arXiv:2510.12393)",
        "challenges": "Kuutma+2017; Winkel+2021",
    },
    1494: {
        "label": "D8", "section": "Star Formation & Quenching",
        "proposition": "Post-starburst (E+A) galaxies represent a major channel (>20%) for the quenching of star-forming galaxies at z<1",
        "supports": "Goto 2007; Wild+2009; Rasmussen+2026 (arXiv:2603.00287)",
        "challenges": "French+2018",
    },
    1495: {
        "label": "D9", "section": "Star Formation & Quenching",
        "proposition": "The star-forming main sequence exhibits a real high-mass turnover or flattening above M*~10^10.5 M☉",
        "supports": "Whitaker+2014; Popesso+2023 (arXiv:2203.10487)",
        "challenges": "Schreiber+2015; Leslie+2020",
    },
    1496: {
        "label": "D10", "section": "Environmental Effects",
        "proposition": "Satellite galaxy quenching is dominated by ram-pressure stripping (fast) not strangulation (slow)",
        "supports": "Wetzel+2013",
        "challenges": "Trussler+2020 (arXiv:1811.09283); Oxland+2024 (arXiv:2403.07742)",
    },
}

# §A.v3.4 Recent-advance highlights per section
HIGHLIGHTS_BY_SECTION = {
    "Physical Mechanisms": [
        ("Pinna et al. 2026 (arXiv:2512.03999)",
         "M74 NSC fossil record from JWST+AO reveals two-phase galactic archaeology — inner NSC formed first, outer disk accreted later"),
    ],
    "Star Formation & Quenching": [
        ("Rasmussen et al. 2026 (arXiv:2603.00287)",
         "EMBERS I survey: post-starburst galaxies retain CO-detected molecular gas despite quenched UV, constraining PSB depletion timescales"),
    ],
    "AGN Feedback": [
        ("Castignani et al. 2025 (arXiv:2504.20538)",
         "NOEMA/ALMA imaging of BCG at z~0.4 detects cold molecular gas filaments — evidence for AGN-regulated cooling in cool-core clusters"),
    ],
    "Environmental Effects": [
        ("van der Wel & Meidt 2025 (arXiv:2509.02847)",
         "EASE survey: short-lived spiral morphologies in dense environments constrain harassment timescales to <1 Gyr"),
        ("Oxland et al. 2024 (arXiv:2403.07742)",
         "Satellite quenching morphology from HST+JWST: ram-pressure stripping signatures dominate at <500 kpc projected separation"),
    ],
}

# ---------------------------------------------------------------------------
# §A.v3.2 — 8 content sections + 2 chrome
# ---------------------------------------------------------------------------
SECTIONS = [
    {
        "name": "Overview & Historical Framework",
        "h2": "## Overview & Historical Framework",
        "target_chars": "1500–1800",
        "beats": (
            "Define galaxy evolution as the quantitative science of the baryon cycle, mass assembly, "
            "and structural transformation across cosmic time. "
            "Name the four governing physics regimes: gravity-driven assembly, "
            "gas accretion + cooling, star formation + stellar feedback, AGN feedback. "
            "Anchor contemporary frontiers: cosmic-noon SF, JWST high-z, environmental quenching, baryon cycle/CGM. "
            "Historical milestones: Hubble 1925 galaxy/island-universe resolution; Baade population dichotomy; "
            "Rubin rotation curves + dark matter; 1990s HDF + Madau-Dickinson SFR density; "
            "2000s SDSS bimodality (Strateva+2001, Baldry+2004); "
            "2010s ALMA cold gas at z>4, IllustrisTNG (Springel+2018), EAGLE (Schaye+2015); "
            "2020s JWST z>10 (CEERS, JADES), DESI 2024 III (arXiv:2404.03002), Euclid."
        ),
        "claim_count": 4,
        "debate_ids": [],
        "highlight_section": None,
    },
    {
        "name": "Physical Mechanisms",
        "h2": "## Physical Mechanisms",
        "target_chars": "1200–1500",
        "beats": (
            "Four compact paragraphs (no sub-headers in this section, internal references to 'subsections' OK): "
            "(1) Mass assembly: hierarchical merging vs smooth cold accretion through cosmic web filaments "
            "(Birnboim & Dekel 2003; Kereš+2005; updated by FIRE-3/IllustrisTNG). "
            "(2) Star formation regulation: SNe + radiation pressure + AGN feedback; "
            "gas regulator equilibrium model (Lilly+2013, Davé+2012) reproduces SFMS to first order. "
            "(3) Morphology and structural transformation: Hubble sequence as snapshot not evolutionary track; "
            "dry vs wet mergers; slow/fast rotators (Naab+2014); bar/disk secular evolution; "
            "weave D4 red-nugget debate here. "
            "(4) Chemical evolution + baryon cycle: mass-metallicity relation (MZR), fundamental metallicity "
            "relation (FMR; Mannucci+2010), CGM as dominant baryon reservoir "
            "(~50% of baryons; Tumlinson, Peeples & Werk 2017)."
        ),
        "claim_count": 5,
        "debate_ids": [1490],
        "highlight_section": "Physical Mechanisms",
    },
    {
        "name": "Dark Matter & Structure Formation",
        "h2": "## Dark Matter & Structure Formation",
        "target_chars": "900–1100",
        "beats": (
            "ΛCDM hierarchical structure formation: dark matter halos form first, baryons follow. "
            "Halo mass function and galaxy occupation distribution. "
            "Halo assembly bias (Gao+2005). "
            "The stellar-to-halo mass relation (SHMR) peak at M_h~10^12 M☉ (~Milky Way mass) "
            "where feedback efficiency (both SNe and AGN) is minimized. "
            "z>10 regime: JWST imaging reveals galaxies that appear too massive/luminous for their epoch. "
            "Weave D2 debate (ΛCDM excess) with both Boylan-Kolchin 2023 (arXiv:2208.01611) and "
            "Adams+2024 (arXiv:2304.13721) views. "
            "Labbé+2023 (arXiv:2207.12446) as observational anchor. "
            "Potential resolutions: bursty star formation boosting UV luminosity, IMF variation, "
            "modifying feedback prescriptions, or genuinely anomalous early galaxy formation."
        ),
        "claim_count": 4,
        "debate_ids": [1488],
        "highlight_section": None,
    },
    {
        "name": "Star Formation & Quenching",
        "h2": "## Star Formation & Quenching",
        "target_chars": "1800–2100",
        "beats": (
            "Use ### subsections: SFMS / Quenching Pathways / Mass vs Environment / PSB Galaxies / Dust-Obscured SFR. "
            "SFMS: log SFR ≈ α log M* + β, slope α~0.7–0.9; normalization rises ×20 from z=0 to z=2 "
            "(Noeske+2007; Speagle+2014; Whitaker+2014; Popesso+2023 arXiv:2203.10487). "
            "Quenching pathways: rapid (post-starburst PSB/E+A, sSFR depletion timescale <200 Myr) vs "
            "slow (declining SFH, strangulation). Green-valley transition (Schawinski+2014; Salim+2016). "
            "Mass vs environment separability: Peng+2010 (arXiv:1003.4747) separability claim — weave D1 debate "
            "with Wetzel+2013 and Bluck+2024 challenge; satellite vs central dichotomy. "
            "PSB as major quenching channel: weave D8 debate (Goto 2007; Wild+2009; Rasmussen+2026 arXiv:2603.00287 "
            "vs French+2018). "
            "SFMS high-mass turnover: weave D9 debate (Whitaker+2014; Popesso+2023 vs Schreiber+2015; Leslie+2020). "
            "Dust-obscured SFR: weave D3 debate (Zavala+2021; Algera+2023 vs Williams+2024 arXiv:2310.03787). "
            "AGN-dominated quenching at M*>10^10.5 M☉; environmental for satellites."
        ),
        "claim_count": 9,
        "debate_ids": [1487, 1489, 1494, 1495],
        "highlight_section": "Star Formation & Quenching",
    },
    {
        "name": "AGN Feedback",
        "h2": "## AGN Feedback",
        "target_chars": "900–1100",
        "beats": (
            "Two modes: radiative (quasar mode, high accretion rate, drives winds/outflows) vs "
            "kinetic (radio/jet mode, low accretion, heats hot halo gas in massive galaxies/BCGs). "
            "SMBH–bulge mass correlation (M-σ relation; Magorrian+1998; Gebhardt+2000; Gültekin+2009): "
            "implies co-evolution of BH and host galaxy. "
            "High-z AGN: JWST reveals over-massive BHs at z>4–6 (Maiolino+2024 arXiv:2305.12492). "
            "Weave D5 debate: AGN feedback purely negative at high z? "
            "(Silk 2013; Maiolino+2024 support) vs positive compressive triggering (Kalfountzou+2017; Übler+2024). "
            "Thermal vs mechanical feedback prescriptions in IllustrisTNG vs EAGLE. "
            "Preventive vs ejective feedback: distinction matters for CGM gas depletion."
        ),
        "claim_count": 4,
        "debate_ids": [1491],
        "highlight_section": "AGN Feedback",
    },
    {
        "name": "Environmental Effects",
        "h2": "## Environmental Effects",
        "target_chars": "1300–1500",
        "beats": (
            "Use ### subsections: Ram-Pressure Stripping / Harassment & Strangulation / Cosmic Web Environment. "
            "Dressler 1980 morphology-density relation: early types prefer dense environments. "
            "Ram-pressure stripping (Gunn & Gott 1972): effective in clusters, strips cold ISM on <1 Gyr timescales; "
            "observational evidence (jellyfish galaxies, HI tails). "
            "Harassment: repeated high-speed tidal encounters in clusters (Moore+1996). "
            "Strangulation: removal of hot halo gas supply (Larson+1980; Balogh+2000; Trussler+2020 arXiv:1811.09283). "
            "Weave D10 debate: ram-pressure (fast) vs strangulation (slow) for satellite quenching — "
            "(Wetzel+2013 vs Trussler+2020; Oxland+2024 arXiv:2403.07742). "
            "Weave D6 debate: morphology-density relation origin — "
            "environment post-formation (Dressler 1980; Smith+2005) vs initial conditions "
            "(van der Wel & Meidt 2025 arXiv:2509.02847). "
            "Weave D7 debate: Mpc-scale cosmic web (filaments, voids, nodes) modulates beyond local density "
            "(Tempel+2013; Daikuhara+2025 arXiv:2510.12393 vs Kuutma+2017; Winkel+2021). "
            "Pre-processing in groups before cluster infall."
        ),
        "claim_count": 7,
        "debate_ids": [1492, 1493, 1496],
        "highlight_section": "Environmental Effects",
    },
    {
        "name": "Observational Evidence",
        "h2": "## Observational Evidence",
        "target_chars": "1100–1400",
        "beats": (
            "Organize by waveband + redshift regime. "
            "UV/Optical: SDSS (z<0.3), HST deep fields (HUDF, CANDELS), JWST (z>0.5); color-magnitude diagram. "
            "IR/submm: Herschel, ALMA, SCUBA-2 detect dust-enshrouded SFR at z=2–6; cosmic SFRD peak at z~2. "
            "Radio: VLA HI surveys (ALFALFA, MeerKAT) track cold gas reservoirs; jet morphologies in radio AGN. "
            "X-ray: Chandra, XMM track hot halo gas; AGN census at z<2. "
            "IFU spectroscopy: SAMI, MaNGA, CALIFA resolve resolved SFR/metallicity gradients across galaxy disks. "
            "Spectroscopic redshift surveys: VVDS, zCOSMOS, VIPERS, DESI DR2 — stellar mass functions and "
            "quenched fractions to z~1.5. "
            "Strong lensing: probes compact high-z structures (van Dokkum+2010 red nuggets). "
            "Photometric redshift era: Euclid Wide + DES + UNIONS constrain shape of SMF and merger rates. "
            "Redshift regimes: z>10 (JWST era), cosmic noon z~1–3, z<0.5 (DESI era). "
            "Mention key papers with arXiv IDs. No D-debates in this section — pure methodology."
        ),
        "claim_count": 4,
        "debate_ids": [],
        "highlight_section": None,
    },
    {
        "name": "Current Surveys & Missions",
        "h2": "## Current Surveys & Missions",
        "target_chars": "900–1100",
        "beats": (
            "Two sub-groups: active vs upcoming. "
            "Active: JWST (NIRCam/NIRSpec/MIRI for z>0.5 to z~20 morphology + spectroscopy); "
            "DESI (5-yr spectroscopic survey, 40M galaxy redshifts to z~3.5); "
            "Euclid (weak lensing + photo-z survey, 15,000 deg²); "
            "Vera C. Rubin Observatory/LSST (first light 2025, 10-yr optical transient + deep co-add survey); "
            "ALMA Cycle 12 (cold gas at z>4); MeerKAT Galaxy Cluster Legacy Survey. "
            "Upcoming: Roman Space Telescope (wide-area NIR, 2026); SKA-Mid (HI galaxy survey to z~2, 2027+); "
            "ngVLA (radio continuum + spectral line). "
            "No URLs. Focus on survey capabilities and galaxy-evolution science cases. "
            "3 or fewer claims — this is a factual list section."
        ),
        "claim_count": 3,
        "debate_ids": [],
        "highlight_section": None,
    },
    {
        "name": "See Also",
        "h2": "## See Also",
        "target_chars": "50–100",
        "beats": (
            "Short list only — no prose. Internal /wiki/... links: "
            "dark-matter-halos, star-forming-regions, active-galactic-nuclei, galaxy-mergers, "
            "cosmological-simulations, cosmic-web, interstellar-medium, stellar-evolution. "
            "Output a simple markdown list."
        ),
        "claim_count": 0,
        "debate_ids": [],
        "highlight_section": None,
    },
    {
        "name": "References",
        "h2": "## References",
        "target_chars": "1200–1800",
        "beats": (
            "Numbered list of ≥22 entries per §A.6 (v2). Mix historical anchors + theoretical pillars + modern empirical. "
            "Required entries: Hubble 1925, Hubble 1929, Madau & Dickinson 2014, Kennicutt & Evans 2012, "
            "Conroy 2013, Tumlinson+2017, Naab & Ostriker 2017, Förster Schreiber & Wuyts 2020, "
            "Vogelsberger+2020, Peng+2010 (arXiv:1003.4747), Lilly+2013, Mannucci+2010, "
            "Springel+2018 (IllustrisTNG), Schaye+2015 (EAGLE), Hopkins+2023 (FIRE-3), "
            "Boylan-Kolchin 2023 (arXiv:2208.01611), Labbé+2023 (arXiv:2207.12446), "
            "DESI 2024 III (arXiv:2404.03002), Popesso+2023 (arXiv:2203.10487), "
            "Maiolino+2024 (arXiv:2305.12492), Williams+2024 (arXiv:2310.03787), "
            "Trussler+2020 (arXiv:1811.09283), Pinna+2026 (arXiv:2512.03999), "
            "Rasmussen+2026 (arXiv:2603.00287), van der Wel & Meidt 2025 (arXiv:2509.02847), "
            "Oxland+2024 (arXiv:2403.07742), Adams+2024 (arXiv:2304.13721). "
            "Output a formatted numbered list — no prose."
        ),
        "claim_count": 0,
        "debate_ids": [],
        "highlight_section": None,
    },
]


def build_debate_block(debate_ids: list[int]) -> str:
    if not debate_ids:
        return ""
    items = []
    for cid in debate_ids:
        d = DEBATES[cid]
        items.append(
            f"- claim:{cid} ({d['label']}) — {d['proposition']}\n"
            f"  Supports: {d['supports']}\n"
            f"  Challenges: {d['challenges']}"
        )
    return DEBATE_PREAMBLE.format(debate_items="\n".join(items))


def build_highlight_block(section_name: str | None) -> str:
    if not section_name or section_name not in HIGHLIGHTS_BY_SECTION:
        return ""
    items = [
        f"- {ref}: {desc}"
        for ref, desc in HIGHLIGHTS_BY_SECTION[section_name]
    ]
    return HIGHLIGHT_PREAMBLE.format(highlight_items="\n".join(items))


def warmup_rakon() -> bool:
    """Send a minimal prompt to confirm Rakon is loaded and responsive before synthesis."""
    print("  🔥 Warming up Rakon (deepseek-r1:671b) — sending ping...")
    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": "Reply with: OK"}],
        "stream": False,
        "temperature": 0.0,
        "max_tokens": 5,
        "keep_alive": "24h",
    }).encode()
    req = urllib.request.Request(
        RAKON_URL, data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=WARMUP_TIMEOUT) as r:
            resp = json.loads(r.read())
            reply = resp["choices"][0]["message"]["content"].strip()
            print(f"  ✓ Rakon online — replied: {reply!r}")
            return True
    except Exception as e:
        print(f"  ✗ Warmup failed: {e}")
        return False


def call_rakon(system: str, user: str) -> str:
    """Call Rakon using streaming to avoid socket idle timeouts on slow CPU inference."""
    payload = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user",   "content": user},
        ],
        "stream": True,
        "temperature": 0.2,
        "keep_alive": "24h",
    }).encode()
    req = urllib.request.Request(
        RAKON_URL, data=payload,
        headers={"Content-Type": "application/json"},
    )
    chunks = []
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        for raw_line in r:
            line = raw_line.decode("utf-8").strip()
            if not line or line == "data: [DONE]":
                continue
            if line.startswith("data: "):
                line = line[6:]
            try:
                delta = json.loads(line)["choices"][0]["delta"].get("content", "")
                if delta:
                    chunks.append(delta)
            except Exception:
                pass
    content = "".join(chunks)
    return strip_think_blocks(content)


def get_evidence_for_page(db, page_id: int, limit: int = 15) -> list[dict]:
    rows = (
        db.query(Evidence)
        .join(Claim, Evidence.claim_id == Claim.id)
        .filter(Claim.page_id == page_id)
        .order_by(Evidence.quality.desc() if hasattr(Evidence, 'quality') else Evidence.id.desc())
        .limit(limit)
        .all()
    )
    results = []
    for e in rows:
        results.append({
            "arxiv_id": getattr(e, 'arxiv_id', None) or "n/a",
            "title": getattr(e, 'title', None) or "",
            "summary": (getattr(e, 'summary', None) or "")[:200],
        })
    return results


def get_section_text(content: str, section_h2: str) -> str:
    pattern = re.escape(section_h2) + r'(.*?)(?=\n## |\Z)'
    m = re.search(pattern, content, re.DOTALL)
    if m:
        return m.group(1).strip()[:800]
    return "(section not yet written)"


def unwrap_code_fence(content: str) -> str:
    """Strip outer ```markdown ... ``` fence if Rakon wraps output in one."""
    trimmed = content.strip()
    m = re.match(r'^```(?:markdown|md)?\s*\n([\s\S]*?)\n```\s*$', trimmed)
    return m.group(1).strip() if m else trimmed


def run_section(db, page: WikiPage, sec: dict, apply: bool) -> str | None:
    evidence = get_evidence_for_page(db, PAGE_ID, limit=15)
    # Supplement evidence list with hard-coded high-quality papers from design doc
    static_evidence = [
        "Peng+2010 (arXiv:1003.4747): Mass- and environment-quenching separability from SDSS+zCOSMOS",
        "Boylan-Kolchin 2023 (arXiv:2208.01611): Stress testing ΛCDM with z>10 JWST galaxies",
        "Labbé+2023 (arXiv:2207.12446): Red candidate massive galaxies ~600 Myr after Big Bang",
        "Adams+2024 (arXiv:2304.13721): UV LF from z=7.5–13.5 with JWST; ΛCDM consistent at 2σ",
        "Maiolino+2024 (arXiv:2305.12492): Small vigorous BH at z>4 — over-massive BH in early universe",
        "Williams+2024 (arXiv:2310.03787): Dust-obscured galaxies at z~3–8 via JWST; stellar mass function",
        "Popesso+2023 (arXiv:2203.10487): SFMS across cosmic times; high-mass flattening confirmed",
        "Trussler+2020 (arXiv:1811.09283): Both starvation and outflows drive quenching; metallicity constraints",
        "Pinna+2026 (arXiv:2512.03999): M74 NSC fossil record — two-phase galactic formation from JWST+AO",
        "Rasmussen+2026 (arXiv:2603.00287): EMBERS I PSB molecular gas survey — depletion timescales",
        "van der Wel & Meidt 2025 (arXiv:2509.02847): EASE short-lived spirals in dense environments",
        "Castignani+2025 (arXiv:2504.20538): BCG cold molecular gas — AGN-regulated cooling",
        "Oxland+2024 (arXiv:2403.07742): Satellite quenching morphology — ram-pressure dominance <500 kpc",
        "Madau & Dickinson 2014: Cosmic SFR density history — peak at z~2",
        "Springel+2018: IllustrisTNG — cosmological hydrodynamic simulation suite",
        "Schaye+2015: EAGLE — galaxy formation simulation; AGN feedback implementation",
    ]
    ev_text = "\n".join(static_evidence)
    if evidence:
        db_ev = "\n".join(
            f"- [{e['arxiv_id']}] {e['title']}: {e['summary']}"
            for e in evidence
        )
        ev_text = db_ev + "\n" + ev_text

    existing = get_section_text(page.content or "", sec["h2"])
    debate_block = build_debate_block(sec["debate_ids"])
    highlight_block = build_highlight_block(sec.get("highlight_section"))

    system = SYSTEM_TEMPLATE.format(
        section_name=sec["name"],
        target_chars=sec["target_chars"],
        existing_text=existing,
        section_beats=sec["beats"],
        top_evidence=ev_text,
        claim_count=sec["claim_count"],
        debate_block=debate_block,
        highlight_block=highlight_block,
    )
    user = USER_TEMPLATE.format(section_name=sec["name"])

    if not apply:
        print(f"\n{'='*60}")
        print(f"[DRY RUN] Section: {sec['name']}")
        print(f"Target chars: {sec['target_chars']}")
        print(f"Debates: {[DEBATES[d]['label'] for d in sec['debate_ids']]}")
        print(f"Highlights: {sec.get('highlight_section')}")
        print(f"System prompt length: {len(system)} chars")
        return None

    print(f"\n→ Synthesizing: {sec['name']} ({sec['target_chars']} chars) ...", flush=True)
    t0 = time.time()
    try:
        output = call_rakon(system, user)
        output = unwrap_code_fence(output)
        elapsed = time.time() - t0
        print(f"  ✓ {len(output)} chars in {elapsed:.0f}s", flush=True)

        # Validate HTML comment markers for debate sections
        for cid in sec["debate_ids"]:
            if f"<!-- claim:{cid} -->" not in output:
                print(f"  ⚠ WARNING: missing <!-- claim:{cid} --> marker in {sec['name']}", flush=True)
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
    print(f"\n✓ Saved PageVersion #{next_num} for page_id={page.id} (review_status=auto_held)")
    print("  → Kun: review against §A.v3.6 checklist and promote when satisfied")


def main() -> None:
    parser = argparse.ArgumentParser(description="Rakon synthesis for galaxy-evolution v3 (dissolution model)")
    parser.add_argument("--apply", action="store_true", help="actually call Rakon and save PageVersion")
    parser.add_argument("--section", help="synthesize only this section (by name substring)")
    args = parser.parse_args()

    db = SessionLocal()
    try:
        page = db.query(WikiPage).filter(WikiPage.id == PAGE_ID).first()
        assert page, f"page_id={PAGE_ID} not found"

        # Find 671B-tier agent for provenance
        agent = (
            db.query(Agent).filter(Agent.model_name.ilike("%671b%")).first()
            or db.query(Agent).filter(Agent.name.ilike("%tori%")).first()
            or db.query(Agent).first()
        )
        agent_id = agent.id if agent else None

        sections_to_run = SECTIONS
        if args.section:
            sections_to_run = [
                s for s in SECTIONS
                if args.section.lower() in s["name"].lower()
            ]
            if not sections_to_run:
                print(f"No section matching '{args.section}'")
                return

        if not args.apply:
            content_sections = [s for s in sections_to_run if s["claim_count"] > 0]
            total_min = sum(int(s["target_chars"].split("–")[0]) for s in content_sections)
            total_max = sum(int(s["target_chars"].split("–")[1]) for s in content_sections)
            print(f"DRY RUN — v3 dissolution model ({len(sections_to_run)} sections)")
            print(f"Model: {MODEL} @ {RAKON_URL}")
            print(f"Total prose target: {total_min:,}–{total_max:,} chars")
            print(f"Debate HTML markers: {sum(len(s['debate_ids']) for s in sections_to_run)} claim wrappers expected")
            for sec in sections_to_run:
                run_section(db, page, sec, apply=False)
            print("\nRun with --apply during 11–13 KST Rakon warm window tomorrow.")
            return

        # APPLY mode — warm up Rakon first
        print("\n[Warmup] Confirming Rakon is responsive before synthesis...")
        if not warmup_rakon():
            print("ERROR: Rakon warmup failed. Aborting. Try again when model is loaded.")
            return
        print()

        built_sections: dict[str, str] = {}
        for sec in sections_to_run:
            result = run_section(db, page, sec, apply=True)
            if result:
                built_sections[sec["h2"]] = result

        if not built_sections:
            print("No sections synthesized.")
            return

        # Assemble full content
        new_parts = [f"# {page.title}"]
        for sec in SECTIONS:
            if sec["h2"] in built_sections:
                new_parts.append(f"\n{sec['h2']}\n\n{built_sections[sec['h2']]}")
            else:
                existing = get_section_text(page.content or "", sec["h2"])
                if existing and existing != "(section not yet written)":
                    new_parts.append(f"\n{sec['h2']}\n\n{existing}")

        full_content = "\n".join(new_parts) + PROVENANCE_FOOTER

        # Validate acceptance criteria
        print("\n--- §A.v3.6 auto-checks ---")
        for cid in DEBATES:
            marker = f"<!-- claim:{cid} -->"
            status = "✓" if marker in full_content else "✗ MISSING"
            print(f"  {status}  <!-- claim:{cid} --> ({DEBATES[cid]['label']})")
        for bad_phrase in ["Open Questions and Active Debates", "Research Frontiers", "Recent Advances"]:
            if bad_phrase in full_content:
                print(f"  ✗ BANNED h2 present: '{bad_phrase}'")
            else:
                print(f"  ✓ No banned h2: '{bad_phrase}'")

        save_page_version(db, page, full_content, agent_id)

    finally:
        db.close()


if __name__ == "__main__":
    main()
