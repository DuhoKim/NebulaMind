#!/usr/bin/env python3
"""
Create D1–D10 debate claim rows for galaxy-evolution (page_id=57).

Design ref: 설계_GalaxyEvolution_Research_v1.md §A.4
Each row: claim_type='debate', trust_level='debated',
          section='Open Questions and Active Debates', page_id=57
No evidence attached yet — evidence wired in pre-stage script.
"""
import sys
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from app.database import SessionLocal
from app.models.claim import Claim
from app.models.agent import Agent

PAGE_ID = 57  # galaxy-evolution

# D1–D10 from §A.4 (locked 2026-05-08)
DEBATE_CLAIMS = [
    {
        "label": "D1",
        "text": (
            "Mass-quenching is separable from environment-quenching at fixed "
            "stellar mass and redshift, such that the two channels act "
            "independently on the galaxy population."
        ),
        "order_idx": 100,
    },
    {
        "label": "D2",
        "text": (
            "The most massive galaxies detected at z>10 in JWST imaging exceed "
            "stellar mass budgets permitted by ΛCDM, implying either anomalously "
            "high star-formation efficiency or unresolved systematic biases in "
            "photometric mass estimates."
        ),
        "order_idx": 101,
    },
    {
        "label": "D3",
        "text": (
            "The dust-obscured fraction of the cosmic star-formation-rate density "
            "at z=4–7 is ≥50%, meaning optical/UV surveys miss the majority of "
            "star formation in the early Universe."
        ),
        "order_idx": 102,
    },
    {
        "label": "D4",
        "text": (
            "Compact 'red nugget' galaxies at z~2 grow to present-day massive "
            "ellipticals primarily via dry minor mergers rather than wet major "
            "mergers or in-situ star formation."
        ),
        "order_idx": 103,
    },
    {
        "label": "D5",
        "text": (
            "AGN feedback at high redshift acts purely as a negative quenching "
            "mechanism, suppressing star formation without triggering compressive "
            "star-formation episodes in the host galaxy."
        ),
        "order_idx": 104,
    },
    {
        "label": "D6",
        "text": (
            "The Dressler morphology–density relation is driven by environment "
            "acting on galaxies after they form, not by initial conditions that "
            "predetermine morphology at the time of assembly."
        ),
        "order_idx": 105,
    },
    {
        "label": "D7",
        "text": (
            "Mpc-scale cosmic web geometry (filaments, voids, nodes) modulates "
            "galaxy star-formation rates and morphologies beyond what is explained "
            "by local overdensity alone."
        ),
        "order_idx": 106,
    },
    {
        "label": "D8",
        "text": (
            "Post-starburst (E+A) galaxies represent a major channel (>20%) for "
            "the quenching of star-forming galaxies at z<1, implying rapid "
            "quenching is at least as common as slow decline."
        ),
        "order_idx": 107,
    },
    {
        "label": "D9",
        "text": (
            "The star-forming main sequence exhibits a real high-mass turnover or "
            "flattening above M*~10^10.5 M☉, rather than remaining log-linear "
            "across the full mass range."
        ),
        "order_idx": 108,
    },
    {
        "label": "D10",
        "text": (
            "Satellite galaxy quenching is dominated by ram-pressure stripping "
            "(a fast, environment-driven process) rather than strangulation of "
            "the gas supply (a slow, halo-scale process)."
        ),
        "order_idx": 109,
    },
]


def main() -> None:
    db = SessionLocal()
    try:
        # Find a suitable agent (tori or first available)
        agent = (
            db.query(Agent).filter(Agent.name.ilike("%tori%")).first()
            or db.query(Agent).first()
        )
        agent_id = agent.id if agent else None
        print(f"Agent: {agent.name if agent else 'None'} (id={agent_id})")

        created = []
        for d in DEBATE_CLAIMS:
            claim = Claim(
                page_id=PAGE_ID,
                text=d["text"],
                claim_type="debate",
                trust_level="debated",
                section="Open Questions and Active Debates",
                order_idx=d["order_idx"],
                created_by_agent_id=agent_id,
            )
            db.add(claim)
            db.flush()  # get id without committing
            created.append((d["label"], claim.id, claim.text[:60]))
            print(f"  [{d['label']}] id={claim.id}  {claim.text[:60]}")

        db.commit()
        print(f"\n✓ Created {len(created)} debate claims (D1–D10) on page_id={PAGE_ID}")

        # Print IDs for use in the pre-stage script
        print("\nClaim ID map (for evidence wiring):")
        for label, cid, _ in created:
            print(f"  {label}: {cid}")

    except Exception as e:
        db.rollback()
        print(f"ERROR: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
