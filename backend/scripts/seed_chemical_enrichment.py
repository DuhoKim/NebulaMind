#!/usr/bin/env python3
"""
Seed Chemical Enrichment & Stellar Populations claims for galaxy-evolution (page_id=57).
Covers section 7 of the target structure: Mass-Metallicity Relation,
alpha-element Abundances, and Stellar Population Gradients.
"""
import sys
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from app.database import SessionLocal
from sqlalchemy import text

PAGE_ID = 57
SECTION = "Chemical Enrichment & Stellar Populations"
AGENT_ID = 34  # ToriSonnet
START_ORDER_IDX = 260  # after current max of 252

CLAIMS = [
    # Mass-Metallicity Relation
    {
        "text": (
            "The Mass-Metallicity Relation "
            "The tight correlation between galaxy stellar mass and gas-phase oxygen abundance "
            "— the mass-metallicity relation (MZR) — spans over two orders of magnitude in "
            "mass and 0.5–1 dex in metallicity, with low-mass galaxies being systematically "
            "more metal-poor. SDSS spectroscopy established the local MZR (Tremonti et al. 2004), "
            "and subsequent surveys have shown the normalization decreases by ~0.3 dex from z=0 "
            "to z=2, reflecting the higher gas fractions and shorter depletion times at early epochs. "
            "The scatter around the MZR correlates with star-formation rate, giving rise to the "
            "fundamental metallicity relation (FMR; Mannucci et al. 2010) that is roughly "
            "redshift-invariant out to z~2.5."
        ),
        "claim_type": "established",
        "trust_level": "unverified",
        "order_idx": START_ORDER_IDX,
    },
    {
        "text": (
            "The shape and scatter of the mass-metallicity relation are primarily set by the "
            "interplay between metal-rich outflows driven by stellar feedback, metal-poor infall "
            "of pristine gas from cosmic filaments, and the metal retention efficiency that scales "
            "with halo mass. Semi-analytic and hydrodynamic simulations (FIRE, EAGLE, IllustrisTNG) "
            "reproduce the observed slope only when feedback-driven winds carry 3–10× more "
            "metals than are retained in low-mass galaxies (M★ < 10⁹ M☉). Observations of "
            "circumgalactic metal reservoirs with COS and MUSE confirm that a substantial fraction "
            "of nucleosynthetic oxygen resides outside the star-forming disk."
        ),
        "claim_type": "established",
        "trust_level": "unverified",
        "order_idx": START_ORDER_IDX + 1,
    },
    {
        "text": (
            "JWST NIRSpec observations at z=4–9 reveal that early galaxies follow a MZR that is "
            "offset by ~0.5 dex below the local relation at fixed stellar mass, with some "
            "high-ionisation systems at z>6 showing oxygen abundances as low as 5–10% solar "
            "(Curti et al. 2024; Nakajima et al. 2023). These extremely low metallicities, "
            "combined with high specific star-formation rates, indicate that pristine gas "
            "accretion from cosmic filaments dominated the baryonic budget of early galaxies, "
            "with insufficient time for stellar evolution to enrich the interstellar medium "
            "to levels typical of z~0 dwarfs."
        ),
        "claim_type": "established",
        "trust_level": "unverified",
        "order_idx": START_ORDER_IDX + 2,
    },
    # Alpha-element Abundances
    {
        "text": (
            "α-element Abundances and Star Formation Timescales "
            "The ratio of α-elements (O, Mg, Si, Ca, Ti) to iron tracks the star-formation "
            "timescale because core-collapse supernovae (SNe II) release α-elements on ~10 Myr "
            "timescales while Type Ia supernovae (SN Ia) inject iron on ~1–3 Gyr delay times. "
            "Massive elliptical galaxies with M★ > 10¹¹ M☉ are α-enhanced ([α/Fe] ~ +0.2 to +0.3), "
            "indicating rapid star formation completed within ~1 Gyr, whereas disk galaxies "
            "like the Milky Way show near-solar ratios in thin-disk populations reflecting "
            "extended enrichment over several gigayears (Thomas et al. 2005; Graves et al. 2010)."
        ),
        "claim_type": "established",
        "trust_level": "unverified",
        "order_idx": START_ORDER_IDX + 3,
    },
    {
        "text": (
            "The [α/Fe]–mass relation for early-type galaxies shows a positive slope: more "
            "massive systems are more α-enhanced, implying shorter star-formation timescales "
            "in the progenitors of high-mass ellipticals — the 'downsizing' pattern seen in "
            "the fossil record. ATLAS3D, MaNGA, and the LEGA-C survey have confirmed this "
            "trend with both integrated spectra and spatially resolved Lick-index measurements, "
            "ruling out simple monolithic collapse models in favour of rapid dissipational "
            "assembly followed by dry merging that redistributes stellar mass without diluting "
            "mean stellar metallicity."
        ),
        "claim_type": "established",
        "trust_level": "unverified",
        "order_idx": START_ORDER_IDX + 4,
    },
    # Stellar Population Gradients
    {
        "text": (
            "Stellar Population Gradients from IFU Surveys "
            "Integral field unit surveys (SAURON, ATLAS3D, CALIFA, MaNGA, SAMI) have established "
            "that early-type galaxies harbour negative metallicity gradients (centres more "
            "metal-rich by ~0.1–0.3 dex per decade in radius) and mildly negative age gradients, "
            "consistent with inside-out quenching where star formation ceases first in the "
            "central regions. Late-type galaxies show weaker metallicity gradients that flatten "
            "in the outer disk, a signature of radial mixing by bars, spiral arms, and radial "
            "migration of stellar populations over cosmic time (Sánchez-Blázquez et al. 2014; "
            "González Delgado et al. 2015)."
        ),
        "claim_type": "established",
        "trust_level": "unverified",
        "order_idx": START_ORDER_IDX + 5,
    },
    {
        "text": (
            "At high redshift (z~0.6–1), the LEGA-C survey's deep spectroscopy of ~3,000 "
            "galaxies demonstrates that the age and metallicity gradients of quiescent systems "
            "are already in place by z~1, with central regions 0.1–0.2 dex more metal-rich "
            "and ~1 Gyr older than effective-radius measurements. This indicates that the "
            "structural maturation of quiescent galaxies — driven by minor dry mergers that "
            "preferentially deposit accreted mass at large radii (van Dokkum et al. 2010) "
            "— does not significantly dilute the steep chemical gradients formed during the "
            "rapid early star-formation phase at z>2."
        ),
        "claim_type": "established",
        "trust_level": "unverified",
        "order_idx": START_ORDER_IDX + 6,
    },
    {
        "text": (
            "The nitrogen-to-oxygen (N/O) ratio and carbon abundance in high-redshift galaxies "
            "encode the contribution of asymptotic giant branch (AGB) stars and the integrated "
            "star-formation history. JWST NIRSpec detections of rest-frame UV nitrogen emission "
            "in compact z>4 galaxies (e.g. GN-z11, Cameron et al. 2023) suggest nitrogen "
            "super-solar enrichment from massive Wolf-Rayet stars or a top-heavy IMF, pointing "
            "to chemically distinct enrichment channels in the earliest star-forming systems "
            "that are not captured by standard chemical evolution models calibrated on "
            "the local universe."
        ),
        "claim_type": "established",
        "trust_level": "unverified",
        "order_idx": START_ORDER_IDX + 7,
    },
]


def main():
    db = SessionLocal()
    try:
        inserted = 0
        for c in CLAIMS:
            db.execute(text("""
                INSERT INTO claims (page_id, section, order_idx, text, trust_level,
                                   claim_type, created_by_agent_id)
                VALUES (:page_id, :section, :order_idx, :text, :trust_level,
                        :claim_type, :agent_id)
            """), {
                "page_id": PAGE_ID,
                "section": SECTION,
                "order_idx": c["order_idx"],
                "text": c["text"],
                "trust_level": c["trust_level"],
                "claim_type": c["claim_type"],
                "agent_id": AGENT_ID,
            })
            inserted += 1
        db.commit()
        print(f"Inserted {inserted} claims into '{SECTION}' for page_id={PAGE_ID}")

        # Verify
        result = db.execute(text(
            "SELECT id, order_idx, LEFT(text, 60) FROM claims "
            "WHERE page_id = :pid AND section = :sec ORDER BY order_idx"
        ), {"pid": PAGE_ID, "sec": SECTION}).fetchall()
        for r in result:
            print(f"  [{r[0]}] ord={r[1]}: {r[2]}")
    except Exception as e:
        db.rollback()
        print(f"ERROR: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
