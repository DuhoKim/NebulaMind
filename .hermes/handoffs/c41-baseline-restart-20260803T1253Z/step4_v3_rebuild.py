import json

ledger = [
    {
        "entry_id": "c41_001",
        "assertion": "Rapid high-redshift galaxy formation produces widespread sub-solar S/O and Ar/O abundance ratios among star-forming populations.",
        "modality": "may_or_can",
        "scope": {
            "population": "high-redshift star-forming population",
            "sample": "high-redshift sample",
            "redshift": "high redshift",
            "mass": "source-specific",
            "environment": "source-specific",
            "simulation_context": None
        },
        "epistemic_type": "observational_sample",
        "source_access": "full_text",
        "method_or_model": "S3O3 and Ar3O3 calibrations",
        "source_bibcodes": ["2026ApJ..1003..228S"],
        "evidence_spans": [{
            "paper_id": "2026ApJ..1003..228S",
            "span_id": "bibcode:2026ApJ..1003..228S_99921_100194",
            "quote": "The rapidity of galaxy formation at high redshifts thus may result in sub-solar S/O and Ar/O. The offset observed in our high-redshift S3O3 and Ar3O3 calibrations suggests that this deficit in S/O and Ar/O is widespread among the high-redshift star-forming population.",
            "location": "C41_STEP3_V3",
            "rhetorical_zone": "finding",
            "stance": "supports",
            "rationale": "Directly supports the claim that rapid formation drives abundance ratio deficits.",
            "source_access": "full_text",
            "source_title": "Unknown Title",
            "source_year": "2026",
            "source_epistemic_type_original": "observational_sample"
        }],
        "certainty_dimensions": {
            "directness": "direct",
            "consistency": "single_source",
            "precision": "qualitative",
            "sample_size": "sample-specific",
            "model_dependence": "none"
        },
        "certainty_level": "emerging_sample_limited",
        "links": [],
        "as_of": "2026-08-04",
        "verification_status": "pending",
        "verification_note": "Awaiting human review.",
        "tags": ["formation_efficiency", "chemical_enrichment"]
    },
    {
        "entry_id": "c41_002",
        "assertion": "Direct t2 measurements are inconsistent with the values required to explain the Abundance Discrepancy Factor (ADF) in H II regions.",
        "modality": "is_are_does",
        "scope": {
            "population": "H II regions",
            "sample": "local observations",
            "redshift": "local",
            "mass": "source-specific",
            "environment": "source-specific",
            "simulation_context": None
        },
        "epistemic_type": "observational_sample",
        "source_access": "full_text",
        "method_or_model": "direct temperature measurements",
        "source_bibcodes": ["2026PASA...43...60H"],
        "evidence_spans": [{
            "paper_id": "2026PASA...43...60H",
            "span_id": "bibcode:2026PASA...43...60H_46679_47158",
            "quote": "From the results shown in Figure 7, we conclude that our direct measurements of t2 are generally inconsistent with the values needed to explain the ADF observed in H II regions of similar metallicity.",
            "location": "C41_STEP3_V3",
            "rhetorical_zone": "finding",
            "stance": "supports",
            "rationale": "Shows explicit inconsistency between measured t2 and required ADF values.",
            "source_access": "full_text",
            "source_title": "Unknown Title",
            "source_year": "2026",
            "source_epistemic_type_original": "observational_sample"
        }],
        "certainty_dimensions": {
            "directness": "direct",
            "consistency": "single_source",
            "precision": "qualitative",
            "sample_size": "sample-specific",
            "model_dependence": "none"
        },
        "certainty_level": "emerging_sample_limited",
        "links": [],
        "as_of": "2026-08-04",
        "verification_status": "pending",
        "verification_note": "Single-source observation.",
        "tags": ["chemical_enrichment"]
    },
    {
        "entry_id": "c41_003",
        "assertion": "Certain high-redshift star-forming galaxies have non-zero ionizing photon escape fractions necessary to reproduce their UV spectra.",
        "modality": "shows_can_occur",
        "scope": {
            "population": "high-redshift star-forming galaxies",
            "sample": "observational case",
            "redshift": "high redshift",
            "mass": "source-specific",
            "environment": "source-specific",
            "simulation_context": None
        },
        "epistemic_type": "single_case",
        "source_access": "full_text",
        "method_or_model": "SED modeling and ALMA/JWST",
        "source_bibcodes": ["2025A&A...696A..87C"],
        "evidence_spans": [{
            "paper_id": "2025A&A...696A..87C",
            "span_id": "bibcode:2025A&A...696A..87C_3188_3608",
            "quote": "Using prospector spectral energy distribution (SED) modeling and combining the ALMA data with JWST observations, we find Z = 0.17 Z⊙and a nonzero escape fraction of ionizing photons (∼11%), which is necessary by the code to reproduce the UV spectrum.",
            "location": "C41_STEP3_V3",
            "rhetorical_zone": "finding",
            "stance": "supports",
            "rationale": "Directly supports the existence of non-zero escape fraction for UV modeling.",
            "source_access": "full_text",
            "source_title": "Unknown Title",
            "source_year": "2025",
            "source_epistemic_type_original": "single_case"
        }],
        "certainty_dimensions": {
            "directness": "direct",
            "consistency": "single_source",
            "precision": "quantified",
            "sample_size": "single_case",
            "model_dependence": "none"
        },
        "certainty_level": "emerging_sample_limited",
        "links": [],
        "as_of": "2026-08-04",
        "verification_status": "pending",
        "verification_note": "Case study.",
        "tags": ["ionizing_output"]
    },
    {
        "entry_id": "c41_004",
        "assertion": "Spectroscopic constraints indicate a mild UV luminosity function evolution towards z~12, which creates tension with theoretical models of rapid evolution.",
        "modality": "mixed_debated",
        "scope": {
            "population": "high-redshift galaxies",
            "sample": "JWST z~12 sample",
            "redshift": "z~12",
            "mass": "source-specific",
            "environment": "source-specific",
            "simulation_context": None
        },
        "epistemic_type": "observational_sample",
        "source_access": "full_text",
        "method_or_model": "JWST spectroscopic constraints",
        "source_bibcodes": ["2024ApJ...960...56H"],
        "evidence_spans": [{
            "paper_id": "2024ApJ...960...56H",
            "span_id": "bibcode:2024ApJ...960...56H_3252_3835",
            "quote": "These UV luminosity function constraints are consistent with the previous photometric estimates within the uncertainties and indicate mild redshift evolution towards z \u223c 12 showing tensions with some theoretical models of rapid evolution.",
            "location": "C41_STEP3_V3",
            "rhetorical_zone": "interpretation",
            "stance": "supports",
            "rationale": "Presents direct evidence of tension between constraints and rapid evolution models.",
            "source_access": "full_text",
            "source_title": "Unknown Title",
            "source_year": "2024",
            "source_epistemic_type_original": "observational_sample"
        }],
        "certainty_dimensions": {
            "directness": "direct",
            "consistency": "single_source",
            "precision": "qualitative",
            "sample_size": "sample-specific",
            "model_dependence": "none"
        },
        "certainty_level": "actively_debated",
        "links": [],
        "as_of": "2026-08-04",
        "verification_status": "pending",
        "verification_note": "Captures a debate against theoretical models.",
        "tags": ["formation_efficiency", "debate_countercase"]
    },
    {
        "entry_id": "c41_005",
        "assertion": "Observations of specific high-redshift objects in diagnostic diagrams are inconsistent with model tracks produced by AGN-NLR ionization.",
        "modality": "shows_can_occur",
        "scope": {
            "population": "high-redshift objects",
            "sample": "case observation",
            "redshift": "high redshift",
            "mass": "source-specific",
            "environment": "source-specific",
            "simulation_context": None
        },
        "epistemic_type": "single_case",
        "source_access": "full_text",
        "method_or_model": "diagnostic diagrams",
        "source_bibcodes": ["2025A&A...697A..89C"],
        "evidence_spans": [{
            "paper_id": "2025A&A...697A..89C",
            "span_id": "bibcode:2025A&A...697A..89C_53319_53685",
            "quote": "In the C3He2-O3He2 diagram, GS-z9-0 occupies the region probed by low-C/O grids at low-to-intermediate metallicity from the SF-models, and appears inconsistent with the model tracks produced by AGN-NLR ionization.",
            "location": "C41_STEP3_V3",
            "rhetorical_zone": "finding",
            "stance": "supports",
            "rationale": "Directly supports inconsistency with AGN-NLR ionization tracks for this object.",
            "source_access": "full_text",
            "source_title": "Unknown Title",
            "source_year": "2025",
            "source_epistemic_type_original": "single_case"
        }],
        "certainty_dimensions": {
            "directness": "direct",
            "consistency": "single_source",
            "precision": "qualitative",
            "sample_size": "single_case",
            "model_dependence": "none"
        },
        "certainty_level": "emerging_sample_limited",
        "links": [],
        "as_of": "2026-08-04",
        "verification_status": "pending",
        "verification_note": "Single object countercase.",
        "tags": ["chemical_enrichment", "ionizing_output", "debate_countercase"]
    },
    {
        "entry_id": "c41_006",
        "assertion": "Metallicities derived using the [Si III] 1893 emission line exhibit large scatter and do not reliably correlate with optical metallicities.",
        "modality": "is_are_does",
        "scope": {
            "population": "star-forming galaxies",
            "sample": "observational sample",
            "redshift": "source-specific",
            "mass": "source-specific",
            "environment": "source-specific",
            "simulation_context": None
        },
        "epistemic_type": "observational_sample",
        "source_access": "full_text",
        "method_or_model": "UV and optical emission line calibration",
        "source_bibcodes": ["2020ApJ...893....1B"],
        "evidence_spans": [{
            "paper_id": "2020ApJ...893....1B",
            "span_id": "bibcode:2020ApJ...893....1B_89955_90177",
            "quote": "Metallicities derived using the [Si III] \u03bb1893 emission line do not reliably correlate with optical metallicities and show a comparatively large scatter, with an average offset of 0.35\u00b10.28 dex from the optical.",
            "location": "C41_STEP3_V3",
            "rhetorical_zone": "finding",
            "stance": "supports",
            "rationale": "Demonstrates the unreliability of this specific UV metallicity tracer.",
            "source_access": "full_text",
            "source_title": "Unknown Title",
            "source_year": "2020",
            "source_epistemic_type_original": "observational_sample"
        }],
        "certainty_dimensions": {
            "directness": "direct",
            "consistency": "single_source",
            "precision": "quantified",
            "sample_size": "sample-specific",
            "model_dependence": "none"
        },
        "certainty_level": "emerging_sample_limited",
        "links": [],
        "as_of": "2026-08-04",
        "verification_status": "pending",
        "verification_note": "Awaiting human review.",
        "tags": ["chemical_enrichment"]
    }
]

with open('C41_LEDGER.jsonl', 'w') as f:
    for entry in ledger:
        f.write(json.dumps(entry) + '\n')
