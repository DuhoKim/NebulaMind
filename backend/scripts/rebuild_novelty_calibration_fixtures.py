#!/usr/bin/env python3
"""Rebuild DB-backed novelty-screen calibration fixtures."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from sqlalchemy import text

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from app.database import SessionLocal
from app.utils.novelty_screen import CALIBRATION_FIXTURE_MODEL_CHAIN, registry_terms, validate_entities


FIXTURES = [
    {
        "survey_combo": "SDSS",
        "question": "Does the stellar mass of low-redshift star-forming galaxies correlate with gas-phase metallicity in SDSS spectra?",
        "why_now": "This calibration fixture intentionally describes an established result using public SDSS spectroscopy.",
        "approach": "measure emission-line metallicities from SDSS galaxy spectra and compare the mass-metallicity relation across star-forming galaxies.",
    },
    {
        "survey_combo": "GALEX+SDSS",
        "question": "Do ultraviolet measurements from GALEX combined with SDSS photometry recover star formation rates for nearby galaxies?",
        "why_now": "This calibration fixture targets established nearby-galaxy star formation work using public GALEX and SDSS data.",
        "approach": "combine GALEX ultraviolet fluxes with SDSS optical photometry to estimate star formation rates and compare them with stellar mass.",
    },
    {
        "survey_combo": "ALMA",
        "question": "Does ALMA spectroscopy measure the molecular gas content of galaxies in the Hubble Ultra Deep Field?",
        "why_now": "This calibration fixture targets established molecular gas measurements from public ALMA deep-field spectroscopy.",
        "approach": "analyze ALMA spectral scans to identify carbon monoxide lines and infer molecular gas masses for galaxies in a deep extragalactic field.",
    },
    {
        "survey_combo": "SDSS",
        "question": "Does SDSS measure the low-redshift galaxy luminosity function from its redshift survey sample?",
        "why_now": "This calibration fixture targets established galaxy luminosity function work based on public SDSS spectroscopy.",
        "approach": "fit the galaxy luminosity function from SDSS redshift survey photometry and spectra, then compare number density by absolute magnitude.",
    },
    {
        "survey_combo": "DESI",
        "question": "Does DESI measure baryon acoustic oscillation distances with galaxies and quasars from its first-year sample?",
        "why_now": "This calibration fixture targets established cosmological distance measurements from public DESI first-year analyses.",
        "approach": "fit baryon acoustic oscillation distance scales from DESI galaxy and quasar clustering measurements over multiple redshift bins.",
    },
    {
        "survey_combo": "Gaia",
        "question": "Does Gaia DR3 provide parallaxes and proper motions for a large public sample of nearby stars?",
        "why_now": "This calibration fixture targets established astrometric catalog work from public Gaia data.",
        "approach": "compare Gaia parallaxes and proper motions for nearby stars and summarize the catalog precision and sample size.",
    },
    {
        "survey_combo": "eROSITA",
        "question": "Does the eROSITA first all-sky survey catalog identify galaxy clusters through extended X-ray emission?",
        "why_now": "This calibration fixture targets established cluster catalog work from public eROSITA all-sky survey data.",
        "approach": "build a galaxy cluster sample from eROSITA source detection and optical confirmation, then report cluster observables.",
    },
]


def rebuild_fixtures(page_id: int, *, dry_run: bool = False) -> dict[str, int]:
    with SessionLocal() as db:
        page = db.execute(text("SELECT id FROM wiki_pages WHERE id = :id"), {"id": page_id}).fetchone()
        if not page:
            raise RuntimeError(f"wiki_pages.id={page_id} does not exist")

        registry = registry_terms(db)
        invalid: list[tuple[int, list[str]]] = []
        for index, fixture in enumerate(FIXTURES, start=1):
            row = type("FixtureRow", (), fixture | {"id": index})()
            result = validate_entities(row, db, registry)
            if not result.ok:
                invalid.append((index, result.offending_terms))
        if invalid:
            raise RuntimeError(f"fixture entity validation failed: {invalid}")

        deleted = db.execute(
            text("DELETE FROM research_ideas WHERE model_chain = :model_chain"),
            {"model_chain": CALIBRATION_FIXTURE_MODEL_CHAIN},
        ).rowcount or 0

        inserted = 0
        for fixture in FIXTURES:
            db.execute(
                text(
                    """
                    INSERT INTO research_ideas (
                        page_id, survey_combo, question, why_now, approach,
                        systematics_json, novelty, feasibility, status, model_chain,
                        saved_by_papa, seeded, factual_verified, coverage_status,
                        closest_prior_work, coverage_checked_at
                    )
                    VALUES (
                        :page_id, :survey_combo, :question, :why_now, :approach,
                        CAST(:systematics_json AS jsonb), :novelty, :feasibility,
                        'covered', :model_chain, false, true, false, 'covered',
                        '[]'::jsonb, NULL
                    )
                    """
                ),
                {
                    "page_id": page_id,
                    "survey_combo": fixture["survey_combo"],
                    "question": fixture["question"],
                    "why_now": fixture["why_now"],
                    "approach": fixture["approach"],
                    "systematics_json": json.dumps(
                        {
                            "fixture": "novelty_screen_calibration",
                            "expected_screen_status": "covered",
                        }
                    ),
                    "novelty": 0.10,
                    "feasibility": 0.95,
                    "model_chain": CALIBRATION_FIXTURE_MODEL_CHAIN,
                },
            )
            inserted += 1

        if dry_run:
            db.rollback()
        else:
            db.commit()

    return {"deleted": deleted, "inserted": inserted}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page-id", type=int, default=57)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    result = rebuild_fixtures(args.page_id, dry_run=args.dry_run)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
