"""Research Ideas v1: research_ideas, anchors, votes, seeds for galaxy-evolution

Revision ID: research_ideas_v1
Revises: surveys_directory_v1
Create Date: 2026-05-13
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "research_ideas_v1"
down_revision = "surveys_directory_v1"
branch_labels = None
depends_on = None

# 15 seed ideas from Kun's design doc (§5). status='active', seeded=TRUE, model_chain='kun-seed'.
_SEEDS = [
    {
        "survey_combo": "JWST+DESI",
        "question": "Does the sub-kpc clumpy structure JWST/NIRCam resolves in z≈1.5–2.5 main-sequence galaxies correlate with the DESI ELG specific star-formation rate at fixed stellar mass?",
        "why_now": "Four 2026 DESI ELG papers report a steepening of the sSFR–environment slope at log(M*/M⊙)≈10, but disagree on whether the effect persists at log(M*)>10.5. JWST CEERS and PRIMER public mosaics now cover ~12% of the DESI ELG footprint with resolved NIRCam imaging. No cross-match has been published.",
        "approach": "Cross-match DESI ELG spectra (z=1.4–2.6, MILKY mask) with JWST NIRCam F200W within 1″. For ~400 expected matches, measure clumpiness (Gini-M20 and NIRCam-based clump count per Guo et al. clump finder) in 4 sSFR bins at fixed stellar mass. Compare slope vs. clumpiness fraction.",
        "systematics_json": ["PSF mismatch across NIRCam fields", "ELG selection bias toward [OIII] emitters", "DESI fiber-loss correction at z>2"],
        "novelty": 0.85,
        "feasibility": 0.75,
    },
    {
        "survey_combo": "JWST+DESI",
        "question": "Is the quenched fraction at fixed halo mass (DESI BGS group catalog) different for galaxies whose JWST/NIRSpec stellar age maps show an outside-in vs inside-out quenching pattern?",
        "why_now": "Papa's own DESI DR1 BGS analysis finds environment-driven sSFR suppression at z<0.4. The mechanism — gas stripping vs. starvation vs. AGN feedback — is degenerate from DESI alone. JWST NIRSpec IFU now has spatially-resolved stellar age maps for ~80 BGS-overlap galaxies in the GTO programs.",
        "approach": "For DESI BGS group catalog galaxies with NIRSpec IFU coverage, classify into outside-in vs inside-out quenchers from age gradient. Bin by halo mass (DESI group mass) and test the quenched fraction difference. N≈80 is small but the effect size predicted from gas-stripping vs starvation models is ~2×.",
        "systematics_json": ["Age-metallicity degeneracy in NIRSpec fits", "Halo mass uncertainty for low-richness DESI groups", "JWST GTO selection function"],
        "novelty": 0.80,
        "feasibility": 0.55,
    },
    {
        "survey_combo": "JWST+DESI",
        "question": "At z>4, does the stellar-mass–metallicity relation measured from JWST/NIRSpec emission lines agree with the relation extrapolated from DESI ELGs at z=1–3?",
        "why_now": "JWST NIRSpec prism programs (JADES, CEERS-MR) now have R~100 metallicity (R23, O3N2) for >300 z>4 galaxies. DESI publishes MZR slope and normalization at z=1–3 from O32. The Lyman-break extrapolation diverges between FIRE-2 and IllustrisTNG predictions at z~6 by 0.4 dex.",
        "approach": "Compile JWST MZR at z=4, 5, 6, 7 from NIRSpec prism samples. Extrapolate DESI z=1–3 MZR forward using power-law fit. Quantify residual vs. simulation predictions.",
        "systematics_json": ["Different metallicity calibrators between DESI (O32) and JWST (R23)", "Selection function of NIRSpec MR-mode"],
        "novelty": 0.65,
        "feasibility": 0.80,
    },
    {
        "survey_combo": "JWST+DESI",
        "question": "Do the kinematic disturbance signatures JWST/NIRSpec MOS detects in z=1–2 galaxies (rotation/dispersion ratio) anti-correlate with DESI-derived local galaxy density?",
        "why_now": "Cluster-environment kinematics at z=1–2 is the open question separating gas-stripping models. DESI provides density estimators (5th-nearest-neighbor) for galaxies in JWST footprint; no kinematic-environment cross-match exists at z>1.",
        "approach": "Compile NIRSpec MOS rotation curves (CEERS, RUBIES, JADES) for galaxies with z=1–2 DESI spec-z. Measure v/σ. Bin by Σ5 quartile. Compare with TNG predictions for stripping.",
        "systematics_json": ["PA/inclination from low-S/N NIRCam morphology", "MOS slit-loss correction", "DESI density sparsity at z>1"],
        "novelty": 0.75,
        "feasibility": 0.60,
    },
    {
        "survey_combo": "JWST+DESI",
        "question": "Is the AGN-host morphology bimodality (compact-disk vs. disturbed) JWST/MIRI sees in obscured AGN consistent with DESI's QSO clustering bias at z=1–2?",
        "why_now": "DESI QSO bias measurements imply host-halo masses ~10¹²·⁵ M⊙ at z=1.5, but JWST/MIRI shows a wide morphology distribution that doesn't fit a single host-halo class. Either the bias measurement is biased by AGN selection, or the morphology bimodality is environment-driven.",
        "approach": "For DESI QSOs at z=1–2 with MIRI imaging, classify morphology (CAS or visual). Compare clustering bias of compact-host vs. disturbed-host QSO subsamples.",
        "systematics_json": ["MIRI sample is small and not BCG-clean", "DESI QSO selection function near AGN"],
        "novelty": 0.70,
        "feasibility": 0.50,
    },
    {
        "survey_combo": "ALMA+Euclid",
        "question": "Does the dust-obscured star-formation fraction (ALMA Band 7 stacks) in z=0.5–1.5 galaxies correlate with the Euclid VIS+NISP morphological asymmetry index at fixed stellar mass?",
        "why_now": "Euclid Q1 (March 2026) released morphological catalogs over 1500 deg². ALMA archival Band 7 covers ~5% of this area to RMS ~0.1 mJy. The dust-obscuration vs. morphology link at intermediate z is contested — gas-rich-mergers model predicts asymmetric+dusty, but secular-disk model predicts symmetric+dusty.",
        "approach": "Stack ALMA Band 7 archival data on Euclid-defined asymmetry quartiles for z=0.5–1.5 galaxies, fixed stellar mass log(M*)=10.0–10.5. Compute IR/UV ratio per quartile.",
        "systematics_json": ["ALMA primary beam attenuation", "Archival coverage non-uniformity", "Euclid PSF-matching for asymmetry at small angular sizes"],
        "novelty": 0.80,
        "feasibility": 0.65,
    },
    {
        "survey_combo": "ALMA+Euclid",
        "question": "At z=2–3, do passive galaxies identified by Euclid NISP UVJ colors show molecular gas detections (ALMA CO 3-2) consistent with the 'frosting' model of residual cold gas?",
        "why_now": "The frosting model predicts residual CO in 30% of UVJ-quiescent z=2 galaxies; gas-poor classical-quenching models predict <5%. Sample sizes from individual ALMA programs are too small (<20 each) to distinguish. Euclid will yield ~10⁴ z=2 UVJ-quiescent candidates by 2027.",
        "approach": "Stack ALMA archival CO 3-2 data (e.g. ASPECS, REBELS) on Euclid UVJ-quiescent stacks. Measure mean detection significance and fit upper limit.",
        "systematics_json": ["UVJ contamination from dusty star-formers", "CO(3-2)-to-H2 conversion factor at z=2", "ALMA stacking correlations"],
        "novelty": 0.75,
        "feasibility": 0.55,
    },
    {
        "survey_combo": "ALMA+Euclid",
        "question": "Does the cold-gas fraction (ALMA CO 1-0 or [CII]) in field galaxies at z=4–6 scale with Euclid-measured halo overdensity, testing whether cosmological accretion or stochastic mergers drive gas supply?",
        "why_now": "Euclid deep fields will resolve halo overdensity at z>4 from Lyman-break number-density excess. ALMA REBELS, REBELSx and CRISTAL-Survey have [CII] for ~150 z=4–6 galaxies. Cross-match unreleased; theoretical prediction differs by factor of 3 between FIRE-2 and EAGLE.",
        "approach": "Cross-match [CII] detections with Euclid deep-field overdensity (5th nearest neighbor in projected density). Fit M_gas vs. δ_5 at fixed M_star.",
        "systematics_json": ["[CII] luminosity-to-M_gas calibration uncertainty (factor of 2)", "Euclid Lyman-break completeness at z>5"],
        "novelty": 0.85,
        "feasibility": 0.45,
    },
    {
        "survey_combo": "DESI+HSC",
        "question": "Does the DESI BGS group catalog reproduce the projected halo mass function from HSC weak-lensing stacking at log(M_h) = 12–14, or is there evidence for a halo-mass-dependent group-finder bias?",
        "why_now": "Group catalogs and weak lensing are usually published independently. DESI DR1 BGS group masses are calibrated against mocks; HSC SSP Year 3 weak lensing provides an independent halo-mass anchor for the same galaxies.",
        "approach": "Identify DESI BGS groups in the HSC SSP Year 3 footprint. Stack HSC shear around groups in DESI mass bins. Compare lensing-inferred mass to DESI-assigned mass.",
        "systematics_json": ["HSC photo-z bias for source galaxies", "DESI fiber-completeness in dense groups", "DESI mocks satellite/central decomposition"],
        "novelty": 0.65,
        "feasibility": 0.85,
    },
    {
        "survey_combo": "DESI+HSC",
        "question": "Is the central-galaxy color (HSC g–r) in DESI BGS groups a stronger predictor of group quenched fraction than halo mass at fixed environment?",
        "why_now": "Galactic conformity is a contested signature of pre-processing vs. AGN feedback. HSC depth lets central colors be measured cleanly; DESI provides redshifts and group memberships. Existing conformity measurements at z<0.1 (SDSS) saturate; DESI BGS extends to z<0.4 with N~50× SDSS.",
        "approach": "For DESI BGS groups, measure central HSC g–r. Bin satellites by central color quartile and halo mass. Test whether quenched fraction varies with central color at fixed M_h.",
        "systematics_json": ["Aperture-matched colors for HSC at varying z", "Satellite-central misclassification"],
        "novelty": 0.70,
        "feasibility": 0.85,
    },
    {
        "survey_combo": "DESI+HSC",
        "question": "Do DESI ELGs that lie on the high-mass tail of the HSC weak-lensing-inferred halo mass distribution show suppressed [OII] equivalent width relative to halo-mass-matched centrals?",
        "why_now": "ELG samples are usually assumed to live in low-mass halos; the high-mass tail of the ELG halo distribution (≳10% by HOD models) is a key probe of how ELGs populate massive halos. HSC weak lensing constrains the actual halo mass per ELG; DESI provides [OII] EW.",
        "approach": "Lensing-stack DESI ELGs in [OII] EW quartiles. Test whether the high-EW quartile is in lower-mass halos as predicted.",
        "systematics_json": ["ELG selection function as a function of halo mass", "[OII] dust correction", "Lensing depth in DESI footprint"],
        "novelty": 0.65,
        "feasibility": 0.80,
    },
    {
        "survey_combo": "JWST+ALMA",
        "question": "In z=4–6 galaxies, does the stellar-age gradient (JWST/NIRSpec Balmer break maps) correlate with the spatially-resolved [CII] dynamical mass (ALMA), testing inside-out growth at the epoch of reionization?",
        "why_now": "Inside-out growth is the dominant paradigm for high-z disks but largely untested kinematically. Resolved [CII] kinematics from ALMA (CRISTAL, REBELSx) now reach 0.2″ resolution; NIRSpec IFU provides Balmer breaks at matching resolution.",
        "approach": "Joint-fit NIRSpec age maps and ALMA [CII] velocity fields for the ~30 overlapping galaxies. Test for radial age-stellar mass slope.",
        "systematics_json": ["Differential PSF (NIRSpec vs ALMA)", "[CII] surface-brightness profile vs. stellar profile alignment", "Age-metallicity degeneracy"],
        "novelty": 0.85,
        "feasibility": 0.50,
    },
    {
        "survey_combo": "Euclid+HSC",
        "question": "Do Euclid-detected ultra-diffuse galaxies in HSC-mapped cluster outskirts at z=0.1–0.3 show stellar-population gradients consistent with quenching by ram-pressure stripping (HSC photometry) rather than starvation (Euclid morphology)?",
        "why_now": "UDG formation mechanisms are debated. Euclid Q1 reveals ~200 UDG candidates in cluster outskirts; HSC SSP has deep multi-band photometry for stellar-population gradient measurement on the same galaxies.",
        "approach": "For Euclid UDGs in HSC footprint, measure color profile from HSC g, r, i, z. Test gradient slope vs. distance-to-cluster-center prediction for each model.",
        "systematics_json": ["UDG completeness vs. surface brightness", "HSC sky background subtraction at UDG SB level"],
        "novelty": 0.70,
        "feasibility": 0.70,
    },
    {
        "survey_combo": "DESI+ALMA",
        "question": "At fixed stellar mass and z=0.5–1, does DESI-derived AGN classification (line-ratio BPT and WISE) predict ALMA molecular gas depletion timescale, testing AGN-feedback as a quenching mechanism?",
        "why_now": "AGN feedback signatures in molecular gas content are contested. DESI provides ~10⁶ AGN host galaxies; ALMA archival CO covers ~2% of these. The depletion-timescale–AGN-luminosity correlation predicted by simulations is order-of-magnitude testable.",
        "approach": "Cross-match DESI AGNs at z=0.5–1 with ALMA CO 1-0 or 2-1. Bin by AGN bolometric luminosity. Fit M_gas/SFR (depletion time) vs. L_AGN.",
        "systematics_json": ["SFR estimator in AGN hosts (DESI-derived may include AGN contamination)", "ALMA archival depth heterogeneity"],
        "novelty": 0.65,
        "feasibility": 0.60,
    },
    {
        "survey_combo": "JWST+HSC",
        "question": "Do JWST-revealed z>10 galaxy candidates that overlap the HSC Deep footprint show consistent photometric properties between the two instruments, or is there evidence for Lyman-break contaminants distinguishable only by joint fitting?",
        "why_now": "JWST high-z candidate samples have a non-trivial low-z interloper rate. HSC's deep g, r drop-out characterization is the strongest ground-based constraint. Several reported z>10 candidates lack systematic HSC cross-match papers.",
        "approach": "For JWST-published z>10 candidates in the HSC Deep footprint, run forced photometry in HSC g, r. Test for Lyman-break consistency. Flag inconsistent objects for re-classification.",
        "systematics_json": ["HSC depth varies across Deep fields", "Some JWST candidates near HSC noise floor"],
        "novelty": 0.55,
        "feasibility": 0.90,
    },
]


def upgrade():
    op.create_table(
        "research_ideas",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("page_id", sa.Integer(), sa.ForeignKey("wiki_pages.id", ondelete="CASCADE"), nullable=False),
        sa.Column("survey_combo", sa.String(40), nullable=False),
        sa.Column("question", sa.Text(), nullable=False),
        sa.Column("why_now", sa.Text(), nullable=False),
        sa.Column("approach", sa.Text(), nullable=False),
        sa.Column("systematics_json", JSONB(), nullable=True),
        sa.Column("novelty", sa.Numeric(3, 2), nullable=False),
        sa.Column("feasibility", sa.Numeric(3, 2), nullable=False),
        sa.Column("status", sa.String(20), nullable=False, server_default="active"),
        sa.Column("model_chain", sa.String(120), nullable=False),
        sa.Column("generated_by_run_id", sa.Integer(), sa.ForeignKey("autowiki_runs.id", ondelete="SET NULL"), nullable=True),
        sa.Column("saved_by_papa", sa.Boolean(), nullable=False, server_default="false"),
        sa.Column("seeded", sa.Boolean(), nullable=False, server_default="false"),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.Column("last_seen_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("ix_research_ideas_page_status", "research_ideas", ["page_id", "status"])
    op.create_index("ix_research_ideas_combo", "research_ideas", ["survey_combo"])

    op.create_table(
        "research_idea_anchors",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("idea_id", sa.Integer(), sa.ForeignKey("research_ideas.id", ondelete="CASCADE"), nullable=False),
        sa.Column("kind", sa.String(20), nullable=False),
        sa.Column("ref_id", sa.String(40), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("ix_research_idea_anchors_idea", "research_idea_anchors", ["idea_id"])
    op.create_index("ix_research_idea_anchors_kind", "research_idea_anchors", ["kind", "ref_id"])

    op.create_table(
        "research_idea_votes",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("idea_id", sa.Integer(), sa.ForeignKey("research_ideas.id", ondelete="CASCADE"), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("value", sa.SmallInteger(), nullable=False),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False, server_default=sa.text("now()")),
        sa.UniqueConstraint("idea_id", "user_id", name="uq_research_idea_votes"),
    )

    # Create join table if surveys exist but research_idea_surveys doesn't yet
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_tables = insp.get_table_names()
    if "surveys" in existing_tables and "research_idea_surveys" not in existing_tables:
        op.create_table(
            "research_idea_surveys",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("idea_id", sa.Integer(), sa.ForeignKey("research_ideas.id", ondelete="CASCADE"), nullable=False),
            sa.Column("survey_id", sa.Integer(), sa.ForeignKey("surveys.id", ondelete="RESTRICT"), nullable=False),
            sa.UniqueConstraint("idea_id", "survey_id", name="uq_research_idea_surveys"),
        )
        op.create_index("ix_research_idea_surveys_idea", "research_idea_surveys", ["idea_id"])
        op.create_index("ix_research_idea_surveys_survey", "research_idea_surveys", ["survey_id"])

    # Seed 15 ideas for galaxy-evolution page
    page_row = conn.execute(
        sa.text("SELECT id FROM wiki_pages WHERE slug = 'galaxy-evolution' LIMIT 1")
    ).fetchone()
    if page_row is None:
        import logging
        logging.getLogger("alembic.research_ideas_v1").warning(
            "No wiki page with slug 'galaxy-evolution' found — skipping seed insert"
        )
        return

    page_id = page_row[0]
    ideas_table = sa.table(
        "research_ideas",
        sa.column("page_id", sa.Integer),
        sa.column("survey_combo", sa.String),
        sa.column("question", sa.Text),
        sa.column("why_now", sa.Text),
        sa.column("approach", sa.Text),
        sa.column("systematics_json", JSONB),
        sa.column("novelty", sa.Numeric),
        sa.column("feasibility", sa.Numeric),
        sa.column("status", sa.String),
        sa.column("model_chain", sa.String),
        sa.column("seeded", sa.Boolean),
    )

    import json as _json
    rows = [
        {
            "page_id": page_id,
            "survey_combo": s["survey_combo"],
            "question": s["question"],
            "why_now": s["why_now"],
            "approach": s["approach"],
            "systematics_json": _json.dumps(s["systematics_json"]),
            "novelty": s["novelty"],
            "feasibility": s["feasibility"],
            "status": "active",
            "model_chain": "kun-seed",
            "seeded": True,
        }
        for s in _SEEDS
    ]
    conn.execute(ideas_table.insert(), rows)

    # Wire research_idea_surveys for the seeds if table exists
    if "surveys" not in existing_tables:
        return

    for seed_data in _SEEDS:
        idea_row = conn.execute(
            sa.text(
                "SELECT id FROM research_ideas WHERE page_id = :pid AND survey_combo = :combo AND model_chain = 'kun-seed' ORDER BY id LIMIT 1"
            ),
            {"pid": page_id, "combo": seed_data["survey_combo"]},
        ).fetchone()
        if idea_row is None:
            continue
        tokens = [t.strip() for t in seed_data["survey_combo"].split("+")]
        for token in tokens:
            survey_row = conn.execute(
                sa.text("SELECT id FROM surveys WHERE UPPER(name) = UPPER(:t) OR UPPER(slug) = UPPER(:t)"),
                {"t": token},
            ).fetchone()
            if survey_row is None:
                continue
            conn.execute(
                sa.text(
                    "INSERT INTO research_idea_surveys (idea_id, survey_id) VALUES (:iid, :sid) ON CONFLICT DO NOTHING"
                ),
                {"iid": idea_row.id, "sid": survey_row.id},
            )


def downgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_tables = insp.get_table_names()
    if "research_idea_surveys" in existing_tables:
        op.drop_index("ix_research_idea_surveys_survey", "research_idea_surveys")
        op.drop_index("ix_research_idea_surveys_idea", "research_idea_surveys")
        op.drop_table("research_idea_surveys")
    op.drop_table("research_idea_votes")
    op.drop_index("ix_research_idea_anchors_kind", "research_idea_anchors")
    op.drop_index("ix_research_idea_anchors_idea", "research_idea_anchors")
    op.drop_table("research_idea_anchors")
    op.drop_index("ix_research_ideas_combo", "research_ideas")
    op.drop_index("ix_research_ideas_page_status", "research_ideas")
    op.drop_table("research_ideas")
