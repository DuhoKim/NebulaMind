#!/usr/bin/env python3
"""Bootstrap wikipedia_title for all 42 NebulaMind wiki pages.
Run once. Idempotent (safe to re-run).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from app.database import SessionLocal

WIKIPEDIA_TITLE_MAP = {
    "accretion-disks":              "Accretion disk",
    "active-galactic-nuclei":       "Active galactic nucleus",
    "asteroid-belt":                "Asteroid belt",
    "baryon-acoustic-oscillations": "Baryon acoustic oscillations",
    "binary-stars":                 "Binary star",
    "black-hole-mergers":           "Black hole merger",
    "black-holes":                  "Black hole",
    "cosmic-inflation":             "Cosmic inflation",
    "cosmic-microwave-background":  "Cosmic microwave background",
    "cosmic-web":                   "Cosmic Web",
    "dark-energy":                  "Dark energy",
    "dark-matter":                  "Dark matter",
    "exoplanet-detection-methods":  "Exoplanet detection methods",
    "exoplanets":                   "Exoplanet",
    "fast-radio-bursts":            "Fast radio burst",
    "galaxy-clusters":              "Galaxy cluster",
    "galaxy-formation":             "Galaxy formation and evolution",
    "gamma-ray-bursts":             "Gamma-ray burst",
    "gravitational-lensing":        "Gravitational Lensing",
    "gravitational-waves":          "Gravitational wave",
    "habitable-zone":               "Habitable zone",
    "hawking-radiation":            "Hawking radiation",
    "hubble-constant":              "Hubble Constant",
    "interstellar-medium":          "Interstellar medium",
    "kuiper-belt":                  "Kuiper belt",
    "magnetars":                    "Magnetar",
    "milky-way":                    "Milky Way",
    "nebulae":                      "Nebula",
    "neutron-stars":                "Neutron star",
    "oort-cloud":                   "Oort cloud",
    "planetary-formation":          "Planetary formation",
    "planetary-nebulae":            "Planetary nebula",
    "pulsars":                      "Pulsar",
    "quasars":                      "Quasar",
    "red-giants":                   "Red giant",
    "reionization":                 "Reionization",
    "spacetime":                    "Spacetime",
    "stellar-evolution":            "Stellar evolution",
    "supernovae":                   "Supernova",
    "tidal-forces":                 "Tidal force",
    "white-dwarfs":                 "White dwarf",
    "wormholes":                    "Wormhole",
}

def main():
    db = SessionLocal()
    try:
        mapped = 0
        skipped = 0
        for slug, wp_title in WIKIPEDIA_TITLE_MAP.items():
            result = db.execute(
                text("UPDATE wiki_pages SET wikipedia_title = :wp WHERE slug = :s"),
                {"wp": wp_title, "s": slug}
            )
            if result.rowcount > 0:
                mapped += 1
                print(f"  ✓ {slug} → {wp_title}")
            else:
                skipped += 1
                print(f"  ⚠ slug not found: {slug}")
        db.commit()
        print(f"\nDone. Mapped: {mapped}, Not found: {skipped}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
