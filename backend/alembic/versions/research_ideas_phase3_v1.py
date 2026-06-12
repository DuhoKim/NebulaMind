"""research_ideas Phase 3 — survey_datasets, research_idea_datasets, claim_id, well_posed, axes votes

Revision ID: research_ideas_phase3_v1
Revises: merge_phase3_heads
Create Date: 2026-05-14
"""
from alembic import op
import sqlalchemy as sa

revision = "research_ideas_phase3_v1"
down_revision = "merge_phase3_heads"
branch_labels = None
depends_on = None

DATASET_SEEDS = [
    # (slug, survey_slug, name, full_name, data_type, release_year, release_label, redshift_range,
    #  sky_coverage_deg2, sample_size, primary_url, registry, license, description)
    ("desi-dr1-bgs", "desi", "DESI DR1 BGS", "DESI DR1 Bright Galaxy Survey", "spectroscopic_catalog", 2024, "DR1", "z = 0.01 - 0.6", 14000.0, 14000000, "https://data.desi.lbl.gov/doc/releases/dr1/", "noirlab", "CC-BY-4.0", "DESI DR1 bright galaxy spectroscopic catalog with ~14M redshifts at z<0.6."),
    ("desi-dr1-lrg", "desi", "DESI DR1 LRG", "DESI DR1 Luminous Red Galaxy Survey", "spectroscopic_catalog", 2024, "DR1", "z = 0.4 - 1.1", 14000.0, 2900000, "https://data.desi.lbl.gov/doc/releases/dr1/", "noirlab", "CC-BY-4.0", "DESI DR1 luminous red galaxy spectroscopic sample at z=0.4-1.1."),
    ("desi-dr1-elg", "desi", "DESI DR1 ELG", "DESI DR1 Emission Line Galaxy Survey", "spectroscopic_catalog", 2024, "DR1", "z = 0.6 - 1.6", 14000.0, 4000000, "https://data.desi.lbl.gov/doc/releases/dr1/", "noirlab", "CC-BY-4.0", "DESI DR1 emission line galaxy sample at z=0.6-1.6."),
    ("desi-dr1-qso", "desi", "DESI DR1 QSO", "DESI DR1 Quasar Catalog", "qso_catalog", 2024, "DR1", "z = 0.8 - 4.2", 14000.0, 1800000, "https://data.desi.lbl.gov/doc/releases/dr1/", "noirlab", "CC-BY-4.0", "DESI DR1 quasar catalog including Lyman-alpha forest tracers."),
    ("sdss-mpa-jhu", "sdss", "SDSS MPA-JHU", "SDSS MPA-JHU Value-Added Catalog", "spectroscopic_catalog", 2004, "DR8", "z = 0.001 - 0.3", 8000.0, 900000, "https://wwwmpa.mpa-garching.mpg.de/SDSS/DR7/", "vizier", "Public", "Classic MPA-JHU value-added catalog with SFRs, stellar masses, metallicities."),
    ("sdss-dr17", "sdss", "SDSS DR17", "SDSS Data Release 17", "spectroscopic_catalog", 2022, "DR17", "z = 0.0 - 3.5", 14555.0, 5000000, "https://www.sdss4.org/dr17/", "vizier", "Public", "Final SDSS-IV data release with optical spectroscopy over 14555 deg2."),
    ("hst-candels", "hst", "HST CANDELS", "Cosmic Assembly Near-infrared Deep Extragalactic Legacy Survey", "imaging", 2014, "v1.0", "z = 0 - 8", 800.0, None, "https://candels.ucolick.org/", "mast", "Public", "HST WFC3/ACS deep imaging in 5 fields covering ~800 arcmin2."),
    ("hst-hdf", "hst", "HST HDF", "Hubble Deep Field", "imaging", 1996, "v1.0", "z = 0 - 6", 5.3, None, "https://www.stsci.edu/hst/instrumentation/wfpc2/science/the-hubble-deep-field", "mast", "Public", "Foundational Hubble Deep Field WFC2 imaging survey."),
    ("hst-hudf", "hst", "HST HUDF", "Hubble Ultra Deep Field", "imaging", 2004, "v2.0", "z = 0 - 10", 11.0, None, "https://www.stsci.edu/hst/instrumentation/wfc3/science/hubble-ultra-deep-field", "mast", "Public", "Deepest optical/NIR HST imaging; central region of GOODS-South."),
    ("jwst-ceers", "jwst", "JWST CEERS", "Cosmic Evolution Early Release Science Survey", "imaging", 2023, "v1.0", "z = 0 - 15", 100.0, None, "https://ceers.github.io/", "mast", "Public", "JWST NIRCam and MIRI mosaics over EGS field; primary high-z morphology survey."),
    ("jwst-jades", "jwst", "JWST JADES", "JWST Advanced Deep Extragalactic Survey", "spectroscopic_catalog", 2024, "DR1", "z = 0.5 - 15", 25.0, 5000, "https://jades-survey.github.io/", "mast", "Public", "JWST NIRSpec deep prism and G395M spectroscopy with ~5000 spectra in GOODS fields."),
    ("jwst-primer", "jwst", "JWST PRIMER", "Public Release IMaging for Extragalactic Research", "imaging", 2024, "v1.0", "z = 0 - 12", 400.0, None, "https://primer-jwst.github.io/", "mast", "Public", "Wide-area JWST NIRCam mosaic in COSMOS and UDS, ~400 arcmin2."),
    ("jwst-rubies", "jwst", "JWST RUBIES", "Red Unknowns: Bright Infrared Extragalactic Survey", "spectroscopic_catalog", 2025, "v1.0", "z = 0.5 - 8", None, 5000, "https://rubies-jwst.github.io/", "mast", "Public", "JWST NIRSpec MOS targeted spectroscopy of red galaxy candidates."),
    ("euclid-q1", "euclid", "Euclid Q1", "Euclid Quick Release 1", "photometric_catalog", 2026, "Q1", "z = 0 - 3", 63.0, 30000000, "https://www.cosmos.esa.int/web/euclid/euclid-survey", "esa_euclid", "Public", "Euclid Quick Release 1 morphological and photometric catalog, March 2026."),
    ("euclid-edf", "euclid", "Euclid EDF", "Euclid Deep Field Photometry", "imaging", 2026, "Q1", "z = 0 - 6", 53.0, None, "https://www.cosmos.esa.int/web/euclid/euclid-deep-fields", "esa_euclid", "Public", "Euclid deep field imaging in EDF-N, EDF-F, EDF-S."),
    ("lsst-dp02", "lsst", "LSST DP0.2", "Rubin LSST Data Preview 0.2", "photometric_catalog", 2023, "DP0.2", "z = 0 - 3", 300.0, 2000000, "https://dp0-2.lsst.io/", "lsst", "Public", "Precursor simulated Rubin LSST data release for pipeline validation."),
    ("hsc-ssp-pdr3", "hsc", "HSC SSP PDR3", "Hyper Suprime-Cam Subaru Strategic Program Public Data Release 3", "photometric_catalog", 2022, "PDR3", "z = 0 - 4", 1200.0, 1000000000, "https://hsc-release.mtk.nao.ac.jp/doc/", "vizier", "Public", "HSC grizy wide-area photometric catalog with shear measurements."),
    ("hsc-deep", "hsc", "HSC Deep", "HSC SSP Deep+UltraDeep Imaging", "imaging", 2022, "PDR3", "z = 0 - 7", 28.0, None, "https://hsc-release.mtk.nao.ac.jp/doc/", "vizier", "Public", "Deep and UltraDeep HSC coadd imaging with best seeing for morphology."),
    ("alma-aspecs", "alma", "ALMA ASPECS", "ALMA Spectroscopic Survey in the Hubble Ultra Deep Field", "interferometric_visibility", 2020, "v1.0", "z = 0 - 10", None, 70, "https://almascience.nrao.edu/alma-data/science-verification/aspecs", "alma", "Public", "CO molecular gas survey in HUDF, CO(3-2) to CO(6-5), 4.5 arcmin2."),
    ("alma-rebels", "alma", "ALMA REBELS", "Reionization Era Bright Emission Line Survey", "interferometric_visibility", 2022, "v1.0", "z = 6 - 9", None, 40, "https://almascience.eso.org/alma-data/science-verification", "alma_eso", "Public", "ALMA [CII] survey of z=6-9 galaxies targeting 40 sources."),
    ("alma-cristal", "alma", "ALMA CRISTAL", "ALMA Resolved [CII] Survey", "interferometric_visibility", 2024, "v1.0", "z = 4 - 7", None, 30, "https://almascience.nrao.edu/", "alma", "Public", "Resolved [CII] kinematics of z=4-7 main-sequence galaxies."),
    ("vla-cosmos", "vla", "VLA-COSMOS 3GHz", "Very Large Array COSMOS 3GHz Large Project", "imaging", 2017, "v1.0", "z = 0 - 6", 2.0, 10830, "https://irsa.ipac.caltech.edu/data/COSMOS/", "ipac", "Public", "VLA 3GHz radio continuum mosaic of COSMOS field, 2.6 deg2."),
    ("vla-first", "vla", "VLA FIRST", "Faint Images of the Radio Sky at Twenty-centimeters", "imaging", 2014, "2014", "z = 0 - 3", 10575.0, 900000, "https://sundog.stsci.edu/", "vizier", "Public", "Wide-area VLA 1.4 GHz survey, 900K sources over 10575 deg2."),
    ("gaia-dr3", "gaia", "Gaia DR3", "Gaia Data Release 3", "photometric_catalog", 2022, "DR3", "z = 0", 41252.0, 1800000000, "https://www.cosmos.esa.int/web/gaia/dr3", "vizier", "CC-BY-4.0", "Gaia full-sky astrometry and photometry with 1.8B sources."),
    ("galex-gr67", "galex", "GALEX GR6/7", "GALEX General Release 6/7", "photometric_catalog", 2014, "GR6/7", "z = 0 - 0.5", 26000.0, 82000000, "https://galex.stsci.edu/GalexView/", "mast", "Public", "GALEX UV photometry catalog GR6 and GR7, 82M sources."),
    ("wise-allwise", "wise", "AllWISE", "AllWISE Source Catalog", "photometric_catalog", 2014, "AllWISE", "z = 0 - 2", 41252.0, 747000000, "https://wise2.ipac.caltech.edu/docs/release/allwise/", "ipac", "Public", "Mid-IR all-sky WISE catalog with 747M sources in W1-W4 bands."),
    ("2mass-xsc", "2mass", "2MASS XSC", "2MASS Extended Source Catalog", "photometric_catalog", 2003, "v1.0", "z = 0 - 0.1", 41252.0, 1647599, "https://irsa.ipac.caltech.edu/Missions/2mass.html", "ipac", "Public", "Near-IR photometry for 1.6M extended sources across full sky."),
    ("cosmos2020", "cosmos", "COSMOS2020", "COSMOS2020 Photometric Catalog", "photometric_catalog", 2022, "v1.0", "z = 0 - 7", 2.0, 1700000, "https://cosmos2020.calet.org/", "vizier", "Public", "Multi-band photometric redshift catalog in COSMOS field, Weaver+ 2022."),
    ("cdf-s", "cdf-s", "CDF-S 7Ms", "Chandra Deep Field South 7 Megasecond", "imaging", 2017, "7Ms", "z = 0 - 7", 0.13, 1008, "https://cxc.cfa.harvard.edu/cda/Contrib/CDF-S_7MS/", "vizier", "Public", "Deepest Chandra X-ray survey with 1008 sources in 0.13 deg2."),
    ("erosita-edr", "erosita", "eROSITA eFEDS", "eROSITA Final Equatorial Depth Survey", "photometric_catalog", 2022, "eFEDS", "z = 0 - 4", 140.0, 27910, "https://erosita.mpe.mpg.de/edr/", "vizier", "Public", "eROSITA X-ray catalog in eFEDS 140 deg2 equatorial field."),
    ("planck-pr3", "planck", "Planck PR3", "Planck 2018 Full-Mission CMB Maps", "cmb_map", 2018, "PR3", None, 41252.0, None, "https://pla.esac.esa.int/", "esa_archive", "Public", "Planck 2018 full-mission temperature and polarization CMB maps."),
    ("act-dr6", "act", "ACT DR6", "Atacama Cosmology Telescope Data Release 6", "cmb_map", 2024, "DR6", None, 18000.0, None, "https://lambda.gsfc.nasa.gov/product/act/actpol_dr6_maps_get.html", "vizier", "Public", "High-resolution CMB temperature and polarization maps from ACT DR6."),
    ("decals-dr10", "decals", "DECaLS DR10", "Dark Energy Camera Legacy Survey Data Release 10", "imaging", 2023, "DR10", "z = 0 - 3", 14000.0, None, "https://www.legacysurvey.org/dr10/", "noirlab", "Public", "DESI Legacy Imaging Survey grz photometry used for DESI targeting."),
    ("pan-starrs-dr2", "pan-starrs", "Pan-STARRS DR2", "Pan-STARRS Data Release 2", "photometric_catalog", 2019, "DR2", "z = 0 - 1", 30000.0, 3000000000, "https://catalogs.mast.stsci.edu/panstarrs/", "mast", "Public", "Pan-STARRS grizy photometry for 3B sources across 3/4 of sky."),
    ("viking-dr5", "viking", "VIKING DR5", "VISTA Kilo-degree Infrared Galaxy Survey DR5", "photometric_catalog", 2019, "DR5", "z = 0 - 3", 1350.0, None, "https://www.eso.org/sci/observing/phase3/data_releases/viking_dr5.html", "esa_archive", "Public", "NIR ZYJHKs imaging survey over KiDS+GAMA footprint."),
    ("unions-dr1", "unions", "UNIONS DR1", "Ultraviolet Near-Infrared Optical Northern Survey DR1", "imaging", 2023, "DR1", "z = 0 - 3", 4861.0, None, "https://www.cfht.hawaii.edu/Science/UNIONS/", "vizier", "Public", "u-band and r-band weak lensing survey in the northern sky."),
]

FLAGSHIP_MAP = {
    "desi": "desi-dr1-bgs",
    "sdss": "sdss-mpa-jhu",
    "hst": "hst-candels",
    "jwst": "jwst-ceers",
    "euclid": "euclid-q1",
    "lsst": "lsst-dp02",
    "hsc": "hsc-ssp-pdr3",
    "alma": "alma-aspecs",
    "vla": "vla-cosmos",
}


def upgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_tables = set(insp.get_table_names())

    # 1. Create survey_datasets table
    if "survey_datasets" not in existing_tables:
        op.execute("""
            CREATE TABLE survey_datasets (
                id                  SERIAL PRIMARY KEY,
                survey_id           INT NOT NULL REFERENCES surveys(id) ON DELETE CASCADE,
                slug                VARCHAR(80) NOT NULL UNIQUE,
                name                VARCHAR(120) NOT NULL,
                full_name           VARCHAR(300) NOT NULL,
                description         TEXT NOT NULL,
                data_type           VARCHAR(40) NOT NULL,
                release_year        INT,
                release_label       VARCHAR(60),
                redshift_range      VARCHAR(60),
                sky_coverage_deg2   NUMERIC(10,2),
                sample_size         BIGINT,
                doi                 VARCHAR(200),
                primary_url         TEXT NOT NULL,
                archive_url         TEXT,
                bibcode             VARCHAR(40),
                registry            VARCHAR(40),
                license             VARCHAR(60),
                status              VARCHAR(20) NOT NULL DEFAULT 'active',
                url_verified_at     TIMESTAMP,
                url_verified_ok     BOOLEAN,
                url_verified_note   TEXT,
                created_at          TIMESTAMP NOT NULL DEFAULT NOW(),
                updated_at          TIMESTAMP NOT NULL DEFAULT NOW()
            )
        """)
        op.execute("CREATE INDEX ix_survey_datasets_survey ON survey_datasets(survey_id)")
        op.execute("CREATE INDEX ix_survey_datasets_type ON survey_datasets(data_type)")
        op.execute("CREATE INDEX ix_survey_datasets_status ON survey_datasets(status)")

    # 2. Create research_idea_datasets table
    if "research_idea_datasets" not in existing_tables:
        op.execute("""
            CREATE TABLE research_idea_datasets (
                id           SERIAL PRIMARY KEY,
                idea_id      INT NOT NULL REFERENCES research_ideas(id) ON DELETE CASCADE,
                dataset_id   INT NOT NULL REFERENCES survey_datasets(id) ON DELETE RESTRICT,
                role         VARCHAR(20) NOT NULL DEFAULT 'primary',
                note         TEXT,
                created_at   TIMESTAMP NOT NULL DEFAULT NOW(),
                UNIQUE (idea_id, dataset_id)
            )
        """)
        op.execute("CREATE INDEX ix_rid_dataset ON research_idea_datasets(dataset_id)")

    # 3. ALTER research_ideas — add Phase 3 columns
    existing_ri_cols = {c["name"] for c in insp.get_columns("research_ideas")}
    ri_new_cols = {
        "claim_id":             "INT REFERENCES claims(id) ON DELETE SET NULL",
        "well_posed_score":     "NUMERIC(3,2)",
        "well_posed_updated_at": "TIMESTAMP",
        "datasets_verified":    "BOOLEAN NOT NULL DEFAULT FALSE",
        "datasets_verified_at": "TIMESTAMP",
    }
    for col, typedef in ri_new_cols.items():
        if col not in existing_ri_cols:
            op.execute(f"ALTER TABLE research_ideas ADD COLUMN {col} {typedef}")

    # 4. ALTER research_idea_votes — add axis column, update unique constraint
    op.execute("ALTER TABLE research_idea_votes DROP CONSTRAINT IF EXISTS uq_research_idea_votes")

    existing_vote_cols = {c["name"] for c in insp.get_columns("research_idea_votes")}
    if "axis" not in existing_vote_cols:
        op.execute("ALTER TABLE research_idea_votes ADD COLUMN axis VARCHAR(20) NOT NULL DEFAULT 'overall'")

    op.execute(
        "CREATE UNIQUE INDEX IF NOT EXISTS uq_research_idea_votes_axis "
        "ON research_idea_votes(idea_id, COALESCE(user_id, -1), axis)"
    )

    # 5. Seed survey_datasets
    for row in DATASET_SEEDS:
        (slug, survey_slug, name, full_name, data_type, release_year, release_label,
         redshift_range, sky_coverage_deg2, sample_size, primary_url, registry,
         license_val, description) = row

        # Look up survey_id by slug
        survey_row = conn.execute(
            sa.text("SELECT id FROM surveys WHERE slug = :s"),
            {"s": survey_slug}
        ).fetchone()
        if survey_row is None:
            continue

        survey_id = survey_row[0]

        conn.execute(sa.text("""
            INSERT INTO survey_datasets
              (survey_id, slug, name, full_name, description, data_type,
               release_year, release_label, redshift_range, sky_coverage_deg2,
               sample_size, primary_url, registry, license, status)
            VALUES
              (:survey_id, :slug, :name, :full_name, :description, :data_type,
               :release_year, :release_label, :redshift_range, :sky_coverage_deg2,
               :sample_size, :primary_url, :registry, :license, 'active')
            ON CONFLICT(slug) DO NOTHING
        """), {
            "survey_id": survey_id,
            "slug": slug,
            "name": name,
            "full_name": full_name,
            "description": description,
            "data_type": data_type,
            "release_year": release_year,
            "release_label": release_label,
            "redshift_range": redshift_range,
            "sky_coverage_deg2": sky_coverage_deg2,
            "sample_size": sample_size,
            "primary_url": primary_url,
            "registry": registry,
            "license": license_val,
        })

    # 6. Backfill research_idea_datasets from research_idea_surveys using flagship map
    for survey_slug, dataset_slug in FLAGSHIP_MAP.items():
        conn.execute(sa.text("""
            INSERT INTO research_idea_datasets (idea_id, dataset_id, role)
            SELECT ris.idea_id, sd.id, 'primary'
            FROM research_idea_surveys ris
            JOIN surveys sv ON sv.id = ris.survey_id AND sv.slug = :survey_slug
            JOIN survey_datasets sd ON sd.slug = :dataset_slug
            ON CONFLICT (idea_id, dataset_id) DO NOTHING
        """), {"survey_slug": survey_slug, "dataset_slug": dataset_slug})


def downgrade():
    op.execute("DROP TABLE IF EXISTS research_idea_datasets")
    op.execute("DROP TABLE IF EXISTS survey_datasets")
    op.execute("ALTER TABLE research_idea_votes DROP COLUMN IF EXISTS axis")
    op.execute("DROP INDEX IF EXISTS uq_research_idea_votes_axis")
    op.execute("ALTER TABLE research_ideas DROP COLUMN IF EXISTS claim_id")
    op.execute("ALTER TABLE research_ideas DROP COLUMN IF EXISTS well_posed_score")
    op.execute("ALTER TABLE research_ideas DROP COLUMN IF EXISTS well_posed_updated_at")
    op.execute("ALTER TABLE research_ideas DROP COLUMN IF EXISTS datasets_verified")
    op.execute("ALTER TABLE research_ideas DROP COLUMN IF EXISTS datasets_verified_at")
