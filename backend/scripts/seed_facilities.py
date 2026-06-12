"""Seed FacilityProfiles and FacilityNewsItems. Idempotent — skips existing slugs."""
import sys
import os
import datetime as dt

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.database import SessionLocal
from app.models.facility import FacilityProfile, FacilityNewsItem


FACILITIES = [
    dict(slug="desi", full_name="Dark Energy Spectroscopic Instrument", short_name="DESI",
         operator="NOIRLab", operator_country="US", facility_kind="survey",
         homepage_url="https://www.desi.lbl.gov", data_portals="https://data.desi.lbl.gov",
         operating_status="active"),
    dict(slug="jwst", full_name="James Webb Space Telescope", short_name="JWST",
         operator="STScI/NASA", operator_country="US", facility_kind="space_telescope",
         first_light_date="2022-07-12", homepage_url="https://jwst.nasa.gov",
         proposal_portal_url="https://www.stsci.edu/jwst/observing-programs/program-information",
         operating_status="active"),
    dict(slug="euclid", full_name="Euclid Space Mission", short_name="Euclid",
         operator="ESA", operator_country="EU", facility_kind="space_telescope",
         first_light_date="2024-01-01",
         homepage_url="https://www.esa.int/Science_Exploration/Space_Science/Euclid",
         operating_status="active"),
    dict(slug="lsst-rubin", full_name="Vera C. Rubin Observatory / LSST", short_name="Rubin/LSST",
         operator="NOIRLab/SLAC", operator_country="US", facility_kind="ground_telescope",
         first_light_date="2025-10-22", homepage_url="https://www.lsst.org",
         operating_status="active"),
    dict(slug="alma", full_name="Atacama Large Millimeter/submillimeter Array", short_name="ALMA",
         operator="ESO/NRAO/NAOJ", operator_country="intl", facility_kind="ground_telescope",
         homepage_url="https://www.almaobservatory.org", operating_status="active"),
    dict(slug="vla", full_name="Karl G. Jansky Very Large Array", short_name="VLA",
         operator="NRAO", operator_country="US", facility_kind="ground_telescope",
         homepage_url="https://public.nrao.edu/telescopes/vla/", operating_status="active"),
]

NEWS_ITEMS = [
    dict(
        facility_slug="desi", slug="desi-dr2-2027q1",
        title="DESI DR2 — ~30M galaxy and quasar spectra expected Q1 2027",
        kind="release", track="data",
        occurs_at=dt.datetime(2027, 1, 1), occurs_at_confidence="soft",
        occurrence_status="upcoming",
        summary="DESI Data Release 2 will publicly release reduced spectra and large-scale-structure catalogs for approximately 30 million galaxies and quasars. Researchers should plan analysis pipelines around the documented mask and selection function.",
        expert_context="Begin pipeline development now; DR2 footprint and selection function documentation expected 6 months before release.",
        credibility_score=0.9, credibility_model="manual_seed", featured=True,
    ),
    dict(
        facility_slug="jwst", slug="jwst-cycle4-deadline-2026",
        title="JWST Cycle 4 GO Proposal Deadline — May 24 2026",
        kind="proposal_call", track="data",
        occurs_at=dt.datetime(2026, 5, 24), occurs_at_confidence="hard",
        occurrence_status="upcoming",
        summary="General Observer proposals for JWST Cycle 4 are due May 24, 2026. Cycle 4 offers ~6,000 hours of prime science time; competition is expected to be 5-6x oversubscribed.",
        expert_context="Submit well ahead of deadline; Astronomer Proposal Tool (APT) submissions close at 8:00 PM EDT.",
        source_url="https://www.stsci.edu/jwst/observing-programs/program-information",
        credibility_score=0.98, credibility_model="manual_seed", featured=True,
    ),
    dict(
        facility_slug="euclid", slug="euclid-q1-release-2026",
        title="Euclid Q1 Data Release — Mosaics and Source Catalogs (Apr 2026)",
        kind="release", track="data",
        occurs_at=dt.datetime(2026, 4, 1), occurs_at_confidence="hard",
        occurrence_status="completed",
        summary="Euclid released its Q1 dataset in April 2026, including deep mosaics and source catalogs from the first months of survey operations. The release covers early Euclid Deep Field observations.",
        expert_context="Q1 data is available via the Euclid Science Archive; check ESA Datalabs for analysis notebooks.",
        source_url="https://www.cosmos.esa.int/web/euclid/euclid-q1-data-release",
        credibility_score=0.95, credibility_model="manual_seed", featured=True,
    ),
    dict(
        facility_slug="euclid", slug="euclid-survey-14pct-2026",
        title="Euclid Wide Survey 14% Complete — on track for 2030 full coverage",
        kind="milestone", track="facility",
        occurs_at=None, occurrence_status="ongoing",
        summary="As of May 2026, Euclid has completed approximately 14% of its planned wide survey footprint, covering roughly 1,900 deg². The mission remains on schedule for full coverage by mid-2030.",
        expert_context="The 14% completion corresponds to early cosmological analysis possible for large-scale structure and weak lensing in surveyed regions.",
        credibility_score=0.9, credibility_model="manual_seed", featured=True,
    ),
    dict(
        facility_slug="lsst-rubin", slug="rubin-engineering-first-light-2025",
        title="Vera C. Rubin Observatory Engineering First Light — Oct 22 2025",
        kind="first_light", track="facility",
        occurs_at=dt.datetime(2025, 10, 22), occurs_at_confidence="hard",
        occurrence_status="completed",
        summary="Rubin Observatory recorded engineering first light with the Simonyi Survey Telescope on October 22 2025. The 8.4m primary mirror and 3.2-gigapixel LSSTCam performed within specifications.",
        expert_context="Science verification observations followed; the LSST 10-year survey is now underway.",
        credibility_score=0.95, credibility_model="manual_seed", featured=True,
    ),
    dict(
        facility_slug="lsst-rubin", slug="lsst-survey-start-2026",
        title="LSST 10-Year Survey Underway — Science Verification Complete",
        kind="milestone", track="facility",
        occurs_at=dt.datetime(2026, 1, 1), occurs_at_confidence="soft",
        occurrence_status="ongoing",
        summary="The LSST 10-year Legacy Survey of Space and Time is now in its main survey phase following successful science verification. Rubin will image the southern sky every 3 nights to a depth of r~24.5 mag.",
        expert_context="Early LSST data releases via the Rubin Science Platform; check DESC and LSST Science Collaborations for data access schedules.",
        credibility_score=0.9, credibility_model="manual_seed", featured=True,
    ),
    dict(
        facility_slug="alma", slug="alma-cycle12-deadline-2026",
        title="ALMA Cycle 12 Proposal Deadline — April 17 2026",
        kind="proposal_call", track="data",
        occurs_at=dt.datetime(2026, 4, 17), occurs_at_confidence="hard",
        occurrence_status="completed",
        summary="ALMA Cycle 12 proposals were due April 17 2026. Cycle 12 offers approximately 4,300 hours of 12m Array time plus ACA and stand-alone Compact Array time.",
        expert_context="Results expected August 2026; Cycle 13 call anticipated early 2027.",
        source_url="https://almascience.nrao.edu/proposing/call-for-proposals",
        credibility_score=0.95, credibility_model="manual_seed", featured=True,
    ),
    dict(
        facility_slug="vla", slug="vlass-epoch3-ongoing",
        title="VLASS Epoch 3 Ongoing — Full-Sky Radio Survey at 2-4 GHz",
        kind="milestone", track="facility",
        occurs_at=None, occurrence_status="ongoing",
        summary="The VLA Sky Survey (VLASS) Epoch 3 is currently underway, providing the third epoch of 2-4 GHz continuum imaging of the entire sky above declination -40°. Epoch 3 enables variability studies and new transient discovery.",
        expert_context="VLASS quicklook images are available within days of observation; final calibrated images follow on a longer cadence via CIRADA.",
        source_url="https://science.nrao.edu/vlass",
        credibility_score=0.92, credibility_model="manual_seed", featured=True,
    ),
]


def main():
    db = SessionLocal()
    try:
        # Facilities — upsert by slug
        fac_added = 0
        fac_map = {}
        for fd in FACILITIES:
            existing = db.query(FacilityProfile).filter_by(slug=fd["slug"]).first()
            if existing:
                fac_map[fd["slug"]] = existing.id
            else:
                f = FacilityProfile(**fd)
                db.add(f)
                db.flush()
                fac_map[f.slug] = f.id
                fac_added += 1

        # News items — insert only if slug doesn't exist
        news_added = 0
        for nd in NEWS_ITEMS:
            facility_slug = nd.pop("facility_slug")
            existing = db.query(FacilityNewsItem).filter_by(slug=nd["slug"]).first()
            if existing:
                nd["facility_slug"] = facility_slug  # restore for next iteration safety
                continue
            nd["facility_id"] = fac_map.get(facility_slug)
            item = FacilityNewsItem(**nd)
            db.add(item)
            news_added += 1

        db.commit()
        print(f"✅ Seeded: +{fac_added} facilities, +{news_added} news items "
              f"({len(FACILITIES)} total facilities, {len(NEWS_ITEMS)} target items).")

    except Exception as e:
        db.rollback()
        print(f"❌ Seed failed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
