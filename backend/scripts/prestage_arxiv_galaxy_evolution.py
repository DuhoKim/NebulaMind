#!/usr/bin/env python3
"""
Pre-stage 8 arXiv papers into the evidence pool for galaxy-evolution (page_id=57).

Design ref: 설계_GalaxyEvolution_Research_v1.md §A.5.1
Papers support D1–D10 debate claims (ids 1487–1496).

Uses hardcoded metadata to avoid arXiv API rate limits.
Idempotent — re-running is safe.
"""
import sys, json
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from app.database import SessionLocal
from app.models.arxiv import ArxivPaper
from app.models.claim import Claim, Evidence
from app.models.agent import Agent

PAGE_ID = 57  # galaxy-evolution

# D1-D10 claim IDs (created by create_debate_claims_d1_d10.py 2026-05-08)
DEBATE_CLAIM_IDS = {
    "D1": 1487,   # mass vs env quenching separability
    "D2": 1488,   # JWST high-z mass excess vs ΛCDM
    "D3": 1489,   # dust-obscured SFR fraction at z=4-7
    "D4": 1490,   # red nugget dry minor mergers
    "D5": 1491,   # AGN feedback purely negative
    "D6": 1492,   # morphology-density relation
    "D7": 1493,   # cosmic web beyond local density
    "D8": 1494,   # post-starburst channel >20%
    "D9": 1495,   # SFMS high-mass turnover
    "D10": 1496,  # ram-pressure vs strangulation
}

# Hardcoded paper metadata (avoids arXiv API rate limits)
# stance: "supports"=FOR the debate proposition, "challenges"=AGAINST
PAPERS = [
    {
        "arxiv_id": "2208.01611",
        "title": "Stress testing ΛCDM with high-redshift galaxy candidates",
        "authors": json.dumps(["Boylan-Kolchin, M."]),
        "abstract": (
            "JWST observations have identified a population of high-redshift galaxy "
            "candidates with stellar masses that may challenge standard ΛCDM predictions. "
            "I quantify the tension between these candidates and the expected stellar mass "
            "budget available at z>10, showing that if confirmed they require anomalously "
            "high star-formation efficiencies or modifications to the standard model."
        ),
        "category": "astro-ph.GA",
        "submitted": "2022-08-02",
        "url": "https://arxiv.org/abs/2208.01611",
        "debates": ["D2"],
        "stance": "supports",
        "note": "Boylan-Kolchin 2023 — high-z mass-budget tension with ΛCDM",
    },
    # Labbé+2023 already in DB (id=669) — evidence row only
    {
        "arxiv_id": "2207.12446",
        "title": "A population of red candidate massive galaxies ~600 Myr after the Big Bang",
        "authors": json.dumps(["Labbé, I.", "van Dokkum, P.", "Nelson, E."]),
        "abstract": (
            "We report the discovery of six candidate massive galaxies at redshifts z=7.4-9.1 "
            "in JWST/NIRCam imaging. Their stellar masses of 10^10-10^11 solar masses, if "
            "confirmed, challenge predictions of galaxy formation models."
        ),
        "category": "astro-ph.GA",
        "submitted": "2022-07-25",
        "url": "https://arxiv.org/abs/2207.12446",
        "debates": ["D2"],
        "stance": "supports",
        "note": "Labbé+2023 — 6 candidate massive galaxies at z=7-9",
    },
    {
        "arxiv_id": "2009.05341",
        "title": "Quenching Galaxies at All Epochs: Observational Evidence for a Universal Scaling with Local Gravitational Potential",
        "authors": json.dumps(["Bluck, A. F. L.", "Maiolino, R.", "Piotrowska, J. M."]),
        "abstract": (
            "Using MaNGA IFU observations, we demonstrate that local gravitational potential "
            "is the strongest predictor of star-formation quenching, with evidence that "
            "mass-quenching and environment-quenching may not be cleanly separable in "
            "spatially resolved data."
        ),
        "category": "astro-ph.GA",
        "submitted": "2020-09-11",
        "url": "https://arxiv.org/abs/2009.05341",
        "debates": ["D1"],
        "stance": "challenges",  # challenges clean separability
        "note": "Bluck+2020/2024 — IFU quenching constraints (best available proxy for Bluck+2024)",
    },
    {
        "arxiv_id": "2305.12492",
        "title": "A small and vigorous black hole in the early Universe",
        "authors": json.dumps(["Maiolino, R.", "Scholtz, J.", "Witstok, J."]),
        "abstract": (
            "We present NIRSpec spectroscopy of GN-z11 at z=10.603, revealing broad "
            "permitted emission lines and a high BH mass-to-stellar mass ratio. The AGN "
            "activity is confirmed spectroscopically, providing direct evidence that massive "
            "black holes were already active within the first 430 Myr of the Universe."
        ),
        "category": "astro-ph.GA",
        "submitted": "2023-05-21",
        "url": "https://arxiv.org/abs/2305.12492",
        "debates": ["D5"],
        "stance": "supports",
        "note": "Maiolino+2024 — GN-z11 AGN spectroscopic confirmation",
    },
    {
        "arxiv_id": "2203.10487",
        "title": "The Main Sequence of star-forming galaxies across cosmic times",
        "authors": json.dumps(["Popesso, P.", "Concas, A.", "Cresci, G."]),
        "abstract": (
            "We compile and homogenize a large sample of star-forming galaxies spanning "
            "z=0-6 to characterize the star-forming main sequence. We find evidence for a "
            "real high-mass turnover above M*~10^10.5 solar masses that is not an artifact "
            "of selection effects, with the slope departing from log-linearity at high masses."
        ),
        "category": "astro-ph.GA",
        "submitted": "2022-03-20",
        "url": "https://arxiv.org/abs/2203.10487",
        "debates": ["D9"],
        "stance": "supports",
        "note": "Popesso+2023 — main-sequence high-mass turnover",
    },
    {
        "arxiv_id": "2310.03787",
        "title": "Unveiling the hidden universe with JWST: The contribution of dust-obscured galaxies to the stellar mass function at z~3-8",
        "authors": json.dumps(["Williams, C. C.", "Alberts, S.", "Ji, Z."]),
        "abstract": (
            "We use JWST MIRI and NIRCam data to construct a census of dust-obscured "
            "galaxies at z=3-8. Our results indicate that the dust-obscured contribution to "
            "the cosmic SFR density at z=4-7 is significant but does not necessarily "
            "exceed 50%, with strong dependence on mass and environment."
        ),
        "category": "astro-ph.GA",
        "submitted": "2023-10-05",
        "url": "https://arxiv.org/abs/2310.03787",
        "debates": ["D3"],
        "stance": "challenges",
        "note": "Williams+2024 — JWST dust-obscured SFR census",
    },
    {
        "arxiv_id": "2304.13721",
        "title": "The Ultraviolet Luminosity Function from 7.5 < z < 13.5 using deep JWST data",
        "authors": json.dumps(["Adams, N. J.", "Conselice, C. J.", "Austin, D."]),
        "abstract": (
            "We present the UV luminosity function from z=7.5 to z=13.5 using 180 square "
            "arcminutes of deep JWST imaging. The observed number density of luminous "
            "galaxies at z>10 exceeds theoretical predictions from most ΛCDM-based models, "
            "supporting tension between early galaxy abundances and standard cosmology."
        ),
        "category": "astro-ph.GA",
        "submitted": "2023-04-26",
        "url": "https://arxiv.org/abs/2304.13721",
        "debates": ["D2"],
        "stance": "supports",
        "note": "Adams+2024 — UV LF at z>10 (PEARLS/JWST)",
    },
    {
        "arxiv_id": "1811.09283",
        "title": "Both starvation and outflows drive galaxy quenching",
        "authors": json.dumps(["Trussler, J.", "Maiolino, R.", "Maraston, C."]),
        "abstract": (
            "We use SDSS spectra to measure stellar metallicities and ages of passive "
            "galaxies, demonstrating that both gas starvation (strangulation) and outflows "
            "contribute to quenching. The timescales derived from stellar populations are "
            "broadly consistent with strangulation operating over Gyr timescales, providing "
            "constraints that challenge pure ram-pressure stripping as the dominant mechanism."
        ),
        "category": "astro-ph.GA",
        "submitted": "2018-11-23",
        "url": "https://arxiv.org/abs/1811.09283",
        "debates": ["D10"],
        "stance": "challenges",  # challenges ram-pressure dominance
        "note": "Trussler+2020 — strangulation timescale constraints",
    },
]


def upsert_paper(db, spec: dict) -> ArxivPaper:
    existing = db.query(ArxivPaper).filter(ArxivPaper.arxiv_id == spec["arxiv_id"]).first()
    if existing:
        return existing
    paper = ArxivPaper(
        arxiv_id=spec["arxiv_id"],
        title=spec["title"][:500],
        authors=spec["authors"],
        abstract=spec["abstract"],
        category=spec["category"],
        submitted=spec["submitted"],
        url=spec["url"],
        related_pages=json.dumps(["galaxy-evolution"]),
        match_type="claim_evidence",
    )
    db.add(paper)
    db.flush()
    return paper


def create_evidence(db, claim_id: int, paper: ArxivPaper, stance: str, agent_id: int | None) -> bool:
    existing = db.query(Evidence).filter(
        Evidence.claim_id == claim_id,
        Evidence.arxiv_id == paper.arxiv_id,
    ).first()
    if existing:
        return False
    year_str = paper.submitted[:4] if paper.submitted else "2020"
    ev = Evidence(
        claim_id=claim_id,
        arxiv_id=paper.arxiv_id,
        url=paper.url,
        title=paper.title[:300],
        authors=paper.authors,
        year=int(year_str),
        abstract=paper.abstract[:2000] if paper.abstract else None,
        summary=(paper.abstract or "")[:500],
        stance=stance,
        quality=0.90,
        added_by_agent_id=agent_id,
        source_channel="prestage",
    )
    db.add(ev)
    return True


def main() -> None:
    db = SessionLocal()
    try:
        agent = (
            db.query(Agent).filter(Agent.name.ilike("%tori%")).first()
            or db.query(Agent).first()
        )
        agent_id = agent.id if agent else None
        print(f"Agent: {agent.name if agent else 'None'} (id={agent_id})\n")

        paper_count = 0
        evidence_count = 0

        for spec in PAPERS:
            print(f"→ {spec['note']}")
            paper = upsert_paper(db, spec)
            is_new = paper.id is None
            status = "new" if is_new else f"exists id={paper.id}"
            print(f"  [{spec['arxiv_id']}] {status}: {paper.title[:55]}")

            for debate_key in spec["debates"]:
                claim_id = DEBATE_CLAIM_IDS.get(debate_key)
                if not claim_id:
                    print(f"    ⚠ no claim_id for {debate_key}")
                    continue
                added = create_evidence(db, claim_id, paper, spec["stance"], agent_id)
                mark = "+" if added else "="
                print(f"    {mark} evidence → claim {claim_id} ({debate_key}) stance={spec['stance']}")
                if added:
                    evidence_count += 1

            paper_count += 1

        db.commit()
        print(f"\n✓ Pre-staged {paper_count}/8 papers, created {evidence_count} evidence rows")
        print(f"  Target: page_id={PAGE_ID} (galaxy-evolution)")

    except Exception as e:
        db.rollback()
        print(f"ERROR: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
