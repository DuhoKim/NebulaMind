"""Subtopic coverage maps for the Wiki Page Renovation pipeline.

Each NebulaMind wiki page belongs to one of 7 categories defined in
``wiki_schema.md``. A page is considered "topically representative" only when
its claims cover the *core subtopics* expected for that category, plus any
page-specific subtopics that are essential for that particular topic.

The renovation pipeline (see ``설계_WikiRenovation_v1.md``) uses these maps to:

1. Compute the **depth** dimension of the Page Health Score: ratio of
   covered subtopics to required subtopics.
2. Drive the **evidence-gathering** stage: ADS searches per missing subtopic.
3. Steer the **synthesis** stage: tell parallel models which subtopics the
   rewrite must address.

Coverage detection is intentionally simple — a subtopic is "covered" if any
of its keyword aliases appears in any claim text on the page. False positives
are acceptable because the synthesizer skips already-covered subtopics; false
negatives just push for slightly more content. We can tighten later with
embedding similarity if needed.

To add or evolve subtopics: edit the dicts below, version-control the change.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# CORE SUBTOPICS BY CATEGORY
# ---------------------------------------------------------------------------
#
# Each entry is keyed by (subtopic_id) and maps to a list of keyword aliases
# used for coverage detection. Keyword matching is case-insensitive and tested
# against the concatenation of all claim texts on a page.
#
# Drafting principles applied throughout:
#   - 6-9 subtopics per category (Papa's "~8" guideline)
#   - Each subtopic = a question a comprehensive page should answer
#   - Aliases include both technical and lay phrasings
#   - Avoid topic-name bleeding (e.g., "stellar" alone is too generic for a
#     stellar-evolution subtopic — pair with disambiguating words)

CORE_SUBTOPICS: dict[str, dict[str, list[str]]] = {
    # -----------------------------------------------------------------------
    # STELLAR — stars, stellar evolution, stellar remnants
    # -----------------------------------------------------------------------
    "stellar": {
        "stellar_classification": [
            "spectral type", "spectral class",
            "OBAFGKM", "Hertzsprung-Russell", "HR diagram",
            "stellar classification", "luminosity class",
        ],
        "main_sequence_evolution": [
            "main sequence", "main-sequence",
            "hydrogen burning", "core fusion",
            "zero-age main sequence", "ZAMS",
        ],
        "nucleosynthesis": [
            "nucleosynthesis", "stellar fusion",
            "CNO cycle", "proton-proton chain", "pp chain",
            "alpha process", "s-process", "r-process",
            "element formation",
        ],
        "mass_radius_relation": [
            "mass-radius", "mass-luminosity",
            "stellar mass", "stellar radius",
            "scaling relation",
        ],
        "luminosity_temperature": [
            "luminosity", "effective temperature",
            "Stefan-Boltzmann", "bolometric", "surface temperature",
        ],
        "death_pathway": [
            "stellar death", "supernova", "white dwarf remnant",
            "neutron star formation", "black hole formation",
            "core collapse", "planetary nebula",
        ],
        "metallicity_effect": [
            "metallicity", "chemical abundance", "Population I",
            "Population II", "Population III",
            "iron abundance", "[Fe/H]",
        ],
        "binarity_role": [
            "binary star", "binary system",
            "mass transfer", "Roche lobe",
            "common envelope", "binary evolution",
        ],
    },
    # -----------------------------------------------------------------------
    # BLACKHOLE — black holes and extreme gravity phenomena
    # -----------------------------------------------------------------------
    "blackhole": {
        "formation_mechanism": [
            "black hole formation", "gravitational collapse",
            "core collapse", "primordial black hole",
            "direct collapse",
        ],
        "types_classification": [
            "stellar-mass black hole", "stellar mass black hole",
            "intermediate-mass black hole", "IMBH",
            "supermassive black hole", "SMBH",
            "black hole mass spectrum",
        ],
        "event_horizon": [
            "event horizon", "Schwarzschild radius",
            "horizon area", "no escape",
            "trapped surface",
        ],
        "spin_charge_metric": [
            "Kerr metric", "Schwarzschild metric",
            "Kerr-Newman", "spin parameter",
            "ergosphere", "no-hair theorem",
        ],
        "thermodynamics": [
            "black hole thermodynamics", "horizon entropy",
            "Bekenstein-Hawking", "area theorem",
            "first law of black hole",
        ],
        "hawking_radiation": [
            "Hawking radiation", "black hole evaporation",
            "thermal emission", "particle pair creation",
            "black hole temperature",
        ],
        "observational_evidence": [
            "EHT", "Event Horizon Telescope", "M87",
            "Sgr A*", "X-ray binary observation",
            "LIGO black hole", "gravitational wave detection",
        ],
        "open_questions": [
            "information paradox", "firewall paradox",
            "singularity problem", "quantum gravity",
            "black hole interior",
        ],
    },
    # -----------------------------------------------------------------------
    # GALAXY — galaxies, galactic structure, AGN
    # -----------------------------------------------------------------------
    "galaxy": {
        "morphology_hubble_sequence": [
            "Hubble sequence", "Hubble classification",
            "spiral galaxy", "elliptical galaxy",
            "lenticular", "irregular galaxy",
            "galaxy morphology",
        ],
        "formation_history": [
            "galaxy formation", "hierarchical assembly",
            "monolithic collapse", "high-z galaxies",
            "galaxy evolution",
        ],
        "dark_matter_halo": [
            "dark matter halo", "rotation curve",
            "NFW profile", "halo mass function",
            "subhalo",
        ],
        "star_formation": [
            "star formation rate", "SFR",
            "stellar mass function", "initial mass function",
            "starburst", "Kennicutt-Schmidt",
        ],
        "agn_feedback": [
            "AGN feedback", "active galactic nucleus",
            "quenching", "supermassive black hole feedback",
            "radio-mode feedback", "quasar-mode feedback",
        ],
        "mergers_evolution": [
            "galaxy merger", "interaction", "tidal stream",
            "minor merger", "major merger",
            "merger tree",
        ],
        "scaling_relations": [
            "Tully-Fisher", "Faber-Jackson",
            "fundamental plane", "M-sigma",
            "stellar mass-halo mass",
        ],
        "environments_clusters": [
            "galaxy cluster", "field galaxy",
            "voids and walls", "cluster red sequence",
            "harassment", "ram-pressure stripping",
        ],
    },
    # -----------------------------------------------------------------------
    # COSMOLOGY — large-scale structure, universe history
    # -----------------------------------------------------------------------
    "cosmology": {
        "expansion_history": [
            "Hubble expansion", "Hubble's law",
            "scale factor", "redshift",
            "expansion of the universe", "deceleration parameter",
        ],
        "structure_formation": [
            "structure formation", "primordial fluctuation",
            "growth of structure", "linear perturbation",
            "N-body simulation", "halo formation",
        ],
        "dark_energy_dark_matter": [
            "dark energy", "dark matter",
            "cosmological constant", "lambda CDM", "ΛCDM",
            "quintessence", "equation of state w",
        ],
        "cmb_anisotropy": [
            "CMB", "cosmic microwave background",
            "temperature anisotropy", "polarization",
            "Planck satellite", "WMAP",
            "acoustic peak",
        ],
        "inflation_era": [
            "cosmic inflation", "inflaton",
            "slow-roll", "horizon problem",
            "flatness problem",
        ],
        "nucleosynthesis_bbn": [
            "Big Bang nucleosynthesis", "BBN",
            "primordial abundance", "deuterium",
            "helium-4", "lithium problem",
        ],
        "open_questions_tensions": [
            "Hubble tension", "S8 tension", "sigma8 tension",
            "axis of evil", "cosmological tensions",
        ],
        "observational_probes": [
            "type Ia supernova", "BAO", "baryon acoustic oscillations",
            "weak lensing", "galaxy survey",
            "21-cm cosmology",
        ],
    },
    # -----------------------------------------------------------------------
    # HIGHENERGY — gamma-ray bursts, FRBs, GW, transients
    # -----------------------------------------------------------------------
    "highenergy": {
        "physical_mechanism": [
            "emission mechanism", "synchrotron emission",
            "inverse Compton", "magnetic reconnection",
            "shock acceleration",
        ],
        "observational_signatures": [
            "light curve", "spectrum", "afterglow",
            "polarization signature", "spectral break",
        ],
        "energy_scale": [
            "isotropic energy", "Eiso", "kinetic energy",
            "luminosity function", "energy budget",
        ],
        "duration_timescale": [
            "duration", "T90", "millisecond timescale",
            "short burst", "long burst",
            "rise time", "decay time",
        ],
        "host_environments": [
            "host galaxy", "host environment",
            "offset distribution", "host metallicity",
            "circumburst medium",
        ],
        "progenitor_models": [
            "progenitor", "compact binary merger",
            "magnetar engine", "collapsar",
            "binary neutron star",
        ],
        "rate_demographics": [
            "event rate", "volumetric rate",
            "luminosity function", "redshift distribution",
            "intrinsic rate",
        ],
        "multi_messenger_followup": [
            "multi-messenger", "GW170817", "kilonova",
            "neutrino counterpart", "follow-up observation",
            "alert network",
        ],
    },
    # -----------------------------------------------------------------------
    # SOLARSYSTEM — solar system bodies, exoplanets
    # -----------------------------------------------------------------------
    "solarsystem": {
        "formation": [
            "planetary formation", "protoplanetary disk",
            "core accretion", "pebble accretion",
            "planetesimal", "nebular hypothesis",
        ],
        "composition": [
            "bulk composition", "ice line", "snow line",
            "rocky composition", "gas giant composition",
            "volatile element",
        ],
        "dynamics_orbit": [
            "orbital element", "semi-major axis",
            "eccentricity", "inclination",
            "resonance", "Kozai-Lidov",
            "secular evolution",
        ],
        "thermal_history": [
            "thermal evolution", "radiogenic heating",
            "tidal heating", "internal cooling",
            "differentiation",
        ],
        "interior_structure": [
            "interior model", "core mantle crust",
            "equation of state", "seismic constraint",
            "moment of inertia",
        ],
        "atmosphere_surface": [
            "atmospheric composition", "surface composition",
            "greenhouse effect", "atmospheric escape",
            "spectral features",
        ],
        "interaction_with_sun": [
            "solar wind", "stellar wind",
            "irradiation", "heliosphere",
            "magnetosphere interaction",
        ],
        "habitability": [
            "habitability", "habitable zone",
            "liquid water", "biosignature",
            "atmospheric retention",
        ],
    },
    # -----------------------------------------------------------------------
    # INSTRUMENTATION — telescopes, observational methods, surveys
    # -----------------------------------------------------------------------
    "instrumentation": {
        "operating_principle": [
            "operating principle", "detector physics",
            "imaging principle", "interferometry",
            "spectroscopy method",
        ],
        "spectral_coverage": [
            "wavelength coverage", "spectral range",
            "X-ray", "ultraviolet", "infrared",
            "millimeter", "radio",
        ],
        "sensitivity_limits": [
            "sensitivity", "limiting magnitude",
            "noise floor", "systematic limit",
            "angular resolution",
        ],
        "key_results": [
            "key result", "first detection",
            "discovery", "milestone observation",
        ],
        "comparison_to_predecessors": [
            "improvement over", "predecessor",
            "compared to", "successor mission",
        ],
        "future_upgrades": [
            "future upgrade", "next generation",
            "planned mission", "roadmap",
        ],
    },
}


# ---------------------------------------------------------------------------
# PAGE SLUG → CATEGORY
# ---------------------------------------------------------------------------
#
# Authoritative assignment for the 43 existing pages. New pages should be
# added here at creation time. If a page genuinely straddles two categories,
# pick the more specific one (e.g., black-hole-mergers → blackhole, not
# highenergy, even though it produces gravitational waves).

PAGE_CATEGORY: dict[str, str] = {
    # blackhole
    "black-holes":            "blackhole",
    "black-hole-mergers":     "blackhole",
    "hawking-radiation":      "blackhole",
    "wormholes":              "blackhole",
    "spacetime":              "blackhole",
    "accretion-disks":        "blackhole",
    "gravitational-lensing":  "blackhole",
    # stellar
    "stellar-evolution":      "stellar",
    "binary-stars":           "stellar",
    "white-dwarfs":           "stellar",
    "neutron-stars":          "stellar",
    "pulsars":                "stellar",
    "magnetars":              "stellar",
    "red-giants":             "stellar",
    "supernovae":             "stellar",
    "planetary-nebulae":      "stellar",
    "nebulae":                "stellar",
    # galaxy
    "milky-way":              "galaxy",
    "galaxy-formation":       "galaxy",
    "galaxy-evolution":       "galaxy",
    "galaxy-clusters":        "galaxy",
    "active-galactic-nuclei": "galaxy",
    "quasars":                "galaxy",
    "interstellar-medium":    "galaxy",
    # cosmology
    "cosmic-inflation":              "cosmology",
    "cosmic-microwave-background":   "cosmology",
    "cosmic-web":                    "cosmology",
    "dark-matter":                   "cosmology",
    "dark-energy":                   "cosmology",
    "hubble-constant":               "cosmology",
    "reionization":                  "cosmology",
    "baryon-acoustic-oscillations":  "cosmology",
    # highenergy
    "gamma-ray-bursts":       "highenergy",
    "fast-radio-bursts":      "highenergy",
    "gravitational-waves":    "highenergy",
    "tidal-forces":           "highenergy",
    # solarsystem
    "exoplanets":                  "solarsystem",
    "exoplanet-detection-methods": "solarsystem",
    "habitable-zone":              "solarsystem",
    "asteroid-belt":               "solarsystem",
    "kuiper-belt":                 "solarsystem",
    "oort-cloud":                  "solarsystem",
    "planetary-formation":         "solarsystem",
    # instrumentation — none yet (placeholder for future pages)
}


# ---------------------------------------------------------------------------
# PAGE-SPECIFIC EXTENSIONS
# ---------------------------------------------------------------------------
#
# Some pages have essential subtopics beyond their category's core. These
# extensions are added (not replaced) unless the page is genuinely outside
# its category's normal scope, in which case ``override`` replaces the core
# entirely.
#
# Drafting rule: a page-specific subtopic is one that, if missing, would
# make the page conspicuously incomplete to a working astronomer.

PAGE_EXTENSIONS: dict[str, dict] = {
    # -- blackhole pages --
    "black-holes": {
        "extra": {
            "singularity_theorem": [
                "singularity theorem", "Penrose theorem",
                "geodesic incompleteness",
            ],
            "no_hair_theorem": [
                "no-hair theorem", "uniqueness theorem",
                "three parameter",
            ],
            "information_paradox": [
                "information paradox", "Page curve",
                "ER=EPR", "firewall",
            ],
        },
    },
    "black-hole-mergers": {
        "extra": {
            "inspiral_phase": [
                "inspiral", "post-Newtonian",
                "chirp mass", "orbital decay",
            ],
            "merger_ringdown": [
                "ringdown", "quasi-normal mode", "black hole spectroscopy",
                "final mass", "final spin",
            ],
            "ligo_virgo_detections": [
                "GW150914", "GW170817", "LIGO", "Virgo",
                "GWTC", "compact binary catalog",
            ],
        },
    },
    "hawking-radiation": {
        "extra": {
            "thermal_spectrum_temperature": [
                "Hawking temperature", "thermal spectrum",
                "T_H = ħc³/(8πGMk)",
            ],
            "evaporation_timescale": [
                "evaporation time", "lifetime",
                "primordial black hole evaporation",
            ],
            "trans_planckian_problem": [
                "trans-Planckian", "frequency redshift",
                "modes origin",
            ],
        },
    },
    "wormholes": {
        # Mostly theoretical; replace category core with topic-specific list
        "override": {
            "mathematical_solutions": [
                "Einstein-Rosen bridge", "Morris-Thorne",
                "traversable wormhole", "metric solution",
            ],
            "exotic_matter": [
                "exotic matter", "negative energy density",
                "phantom energy",
            ],
            "stability_traversability": [
                "stability", "traversable",
                "throat radius", "tidal force",
            ],
            "energy_conditions": [
                "energy condition", "null energy condition",
                "averaged null energy",
            ],
            "observational_search": [
                "observational signature", "lensing signature",
                "astrophysical search",
            ],
            "philosophical_implications": [
                "time travel", "causality", "chronology protection",
                "closed timelike curve",
            ],
        },
    },
    "spacetime": {
        "override": {
            "minkowski_special_relativity": [
                "Minkowski", "special relativity",
                "Lorentz invariance", "spacetime interval",
            ],
            "general_relativity": [
                "general relativity", "Einstein field equation",
                "metric tensor", "geodesic",
            ],
            "curvature_gravity": [
                "curvature", "Riemann tensor",
                "Ricci scalar", "Ricci tensor",
            ],
            "weak_field_tests": [
                "perihelion precession", "light deflection",
                "Shapiro delay", "frame dragging",
            ],
            "strong_field_regimes": [
                "strong-field test", "binary pulsar",
                "black hole shadow",
            ],
            "spacetime_topology": [
                "topology", "global structure",
                "Penrose diagram",
            ],
            "quantum_spacetime": [
                "quantum gravity", "loop quantum gravity",
                "spacetime foam",
            ],
        },
    },
    "accretion-disks": {
        "extra": {
            "alpha_viscosity_model": [
                "Shakura-Sunyaev", "alpha viscosity",
                "thin disk", "alpha disk",
            ],
            "advection_dominated": [
                "ADAF", "advection-dominated",
                "radiatively inefficient",
            ],
            "disk_corona_geometry": [
                "corona", "lamppost geometry",
                "disk truncation",
            ],
        },
    },
    "gravitational-lensing": {
        "extra": {
            "strong_lensing": [
                "strong lensing", "Einstein ring",
                "multiple image", "time delay",
            ],
            "weak_lensing": [
                "weak lensing", "shear", "cosmic shear",
                "galaxy-galaxy lensing",
            ],
            "microlensing": [
                "microlensing", "MACHO", "OGLE",
                "exoplanet microlensing",
            ],
        },
    },
    # -- stellar pages --
    "stellar-evolution": {
        "extra": {
            "evolutionary_tracks": [
                "evolutionary track", "isochrone",
                "stellar age",
            ],
            "post_main_sequence": [
                "subgiant", "red giant branch", "RGB",
                "horizontal branch", "asymptotic giant branch", "AGB",
            ],
        },
    },
    "binary-stars": {
        "extra": {
            "common_envelope_phase": [
                "common envelope", "spiral-in",
                "envelope ejection",
            ],
            "x_ray_binaries": [
                "X-ray binary", "low-mass X-ray binary", "LMXB",
                "high-mass X-ray binary", "HMXB",
            ],
            "binary_evolution_endpoints": [
                "double white dwarf", "double neutron star",
                "merger product",
            ],
        },
    },
    "white-dwarfs": {
        "extra": {
            "chandrasekhar_limit": [
                "Chandrasekhar limit", "1.4 solar mass",
                "electron degeneracy",
            ],
            "cooling_sequence": [
                "white dwarf cooling", "cooling age",
                "luminosity function",
            ],
            "type_ia_progenitor": [
                "Type Ia progenitor", "single degenerate",
                "double degenerate",
            ],
        },
    },
    "neutron-stars": {
        "extra": {
            "equation_of_state": [
                "equation of state", "EOS",
                "nuclear matter", "neutron matter",
            ],
            "tov_limit": [
                "Tolman-Oppenheimer-Volkoff", "TOV",
                "maximum neutron star mass",
            ],
            "merger_remnants": [
                "neutron star merger", "BNS merger",
                "kilonova", "remnant lifetime",
            ],
        },
    },
    "pulsars": {
        "extra": {
            "magnetic_dipole_radiation": [
                "magnetic dipole", "spin-down",
                "rotating dipole",
            ],
            "pulsar_timing": [
                "pulsar timing", "timing residual",
                "pulsar timing array", "PTA",
            ],
            "millisecond_pulsars": [
                "millisecond pulsar", "MSP",
                "recycled pulsar", "spin-up",
            ],
        },
    },
    "magnetars": {
        "extra": {
            "magnetic_field_origin": [
                "dynamo amplification", "fossil field",
                "proto-neutron star dynamo",
            ],
            "soft_gamma_repeaters": [
                "SGR", "soft gamma repeater",
                "anomalous X-ray pulsar", "AXP",
                "giant flare",
            ],
            "frb_link": [
                "FRB-magnetar", "SGR 1935+2154",
                "FRB 200428",
            ],
        },
    },
    "red-giants": {
        "extra": {
            "helium_flash": [
                "helium flash", "core helium ignition",
                "helium burning",
            ],
            "asymptotic_giant_branch": [
                "asymptotic giant branch", "AGB",
                "thermal pulse", "dredge-up",
            ],
        },
    },
    "supernovae": {
        "extra": {
            "type_classification": [
                "Type Ia", "Type II", "Type Ib", "Type Ic",
                "stripped envelope",
            ],
            "shock_breakout_lightcurve": [
                "shock breakout", "lightcurve",
                "plateau", "tail decay",
            ],
            "remnant_evolution": [
                "supernova remnant", "Sedov-Taylor",
                "free expansion",
            ],
        },
    },
    "planetary-nebulae": {
        "extra": {
            "morphology_shaping": [
                "bipolar morphology", "shaping mechanism",
                "binary central star",
            ],
            "central_star_evolution": [
                "central star", "post-AGB",
                "white dwarf precursor",
            ],
        },
    },
    "nebulae": {
        "extra": {
            "ionization_state": [
                "H II region", "emission nebula",
                "reflection nebula", "dark nebula",
            ],
            "molecular_clouds": [
                "molecular cloud", "giant molecular cloud", "GMC",
                "dense core",
            ],
        },
    },
    # -- galaxy pages --
    "milky-way": {
        "extra": {
            "galactic_components": [
                "galactic disk", "thin disk", "thick disk",
                "galactic bulge", "galactic halo",
                "stellar streams",
            ],
            "central_supermassive_black_hole": [
                "Sgr A*", "Sagittarius A",
                "central black hole", "S-stars",
            ],
            "satellite_galaxies": [
                "Magellanic Cloud", "satellite galaxy",
                "dwarf spheroidal",
            ],
        },
    },
    "galaxy-formation": {
        "extra": {
            "high_redshift_galaxies": [
                "high-z", "JWST early galaxy",
                "z > 10", "EoR galaxy",
            ],
            "first_stars_galaxies": [
                "Population III", "first galaxies",
                "primordial galaxy",
            ],
        },
    },
    "galaxy-evolution": {
        "extra": {
            "color_bimodality": [
                "red sequence", "blue cloud",
                "green valley",
            ],
            "size_growth": [
                "compact quiescent", "size evolution",
                "minor merger growth",
            ],
        },
    },
    "galaxy-clusters": {
        "extra": {
            "intracluster_medium": [
                "intracluster medium", "ICM",
                "X-ray cluster", "thermal Bremsstrahlung",
            ],
            "sunyaev_zeldovich_effect": [
                "Sunyaev-Zeldovich", "SZ effect",
                "thermal SZ", "kinematic SZ",
            ],
            "cluster_cosmology": [
                "cluster mass function", "cluster cosmology",
                "halo mass function constraint",
            ],
        },
    },
    "active-galactic-nuclei": {
        "extra": {
            "unified_model": [
                "AGN unification", "unified model",
                "torus geometry", "viewing angle",
            ],
            "agn_classes": [
                "Seyfert galaxy", "Type 1", "Type 2",
                "blazar", "BL Lac", "FSRQ",
                "radio galaxy",
            ],
            "jet_launching": [
                "relativistic jet", "Blandford-Znajek",
                "jet launching", "magnetic accretion",
            ],
        },
    },
    "quasars": {
        "extra": {
            "high_redshift_quasars": [
                "high-z quasar", "z > 6 quasar",
                "early SMBH",
            ],
            "broad_emission_lines": [
                "broad-line region", "BLR",
                "narrow-line region", "NLR",
                "reverberation mapping",
            ],
        },
    },
    "interstellar-medium": {
        "extra": {
            "phase_structure": [
                "cold neutral medium", "CNM",
                "warm neutral medium", "WNM",
                "warm ionized medium", "WIM",
                "hot ionized medium", "HIM",
            ],
            "dust_grains": [
                "interstellar dust", "extinction",
                "PAH", "polycyclic aromatic hydrocarbon",
            ],
            "cosmic_rays": [
                "cosmic ray", "primary cosmic ray",
                "spallation",
            ],
        },
    },
    # -- cosmology pages --
    "cosmic-inflation": {
        "extra": {
            "slow_roll_inflation": [
                "slow-roll", "inflaton potential",
                "single-field inflation",
            ],
            "quantum_fluctuations": [
                "quantum fluctuation", "scalar perturbation",
                "tensor perturbation",
            ],
            "observational_imprints": [
                "tensor-to-scalar ratio", "n_s spectral tilt",
                "primordial non-gaussianity",
            ],
        },
    },
    "cosmic-microwave-background": {
        "extra": {
            "acoustic_oscillations": [
                "acoustic oscillation", "first peak",
                "sound horizon at decoupling",
            ],
            "polarization_modes": [
                "E-mode", "B-mode", "polarization pattern",
                "primordial gravitational wave imprint",
            ],
            "secondary_anisotropies": [
                "lensing of CMB", "ISW", "Sachs-Wolfe",
                "Sunyaev-Zeldovich",
            ],
        },
    },
    "cosmic-web": {
        "extra": {
            "filaments_voids_nodes": [
                "cosmic filament", "cosmic void",
                "supercluster", "void density",
            ],
            "warm_hot_intergalactic_medium": [
                "WHIM", "warm-hot intergalactic medium",
                "missing baryon",
            ],
        },
    },
    "dark-matter": {
        "extra": {
            "candidates": [
                "WIMP", "axion", "primordial black hole",
                "sterile neutrino", "fuzzy dark matter",
            ],
            "direct_detection": [
                "direct detection", "XENON", "LUX",
                "PandaX", "nuclear recoil",
            ],
            "indirect_detection": [
                "indirect detection", "annihilation signal",
                "Fermi-LAT", "AMS",
            ],
            "cosmic_evidence": [
                "rotation curve evidence", "Bullet Cluster",
                "CMB evidence for dark matter",
            ],
        },
    },
    "dark-energy": {
        "extra": {
            "cosmological_constant": [
                "cosmological constant", "lambda",
                "vacuum energy", "Λ",
            ],
            "dynamical_dark_energy": [
                "dynamical dark energy", "quintessence",
                "phantom", "w0-wa",
            ],
            "observational_constraints": [
                "DESI", "supernova constraint",
                "BAO constraint", "CMB constraint",
            ],
        },
    },
    "hubble-constant": {
        "extra": {
            "hubble_tension": [
                "Hubble tension", "5-sigma tension",
                "early vs late universe",
            ],
            "distance_ladder_methods": [
                "Cepheid distance", "Type Ia supernova ladder",
                "tip of red giant branch", "TRGB",
            ],
            "cmb_inferred_value": [
                "Planck-inferred H0", "early universe H0",
                "CMB H0",
            ],
        },
    },
    "reionization": {
        "extra": {
            "sources_of_reionization": [
                "ionizing source", "Lyman continuum",
                "escape fraction", "first quasar",
            ],
            "21cm_signal": [
                "21-cm signal", "21cm cosmology",
                "EDGES", "global signal",
            ],
            "epoch_timing": [
                "EoR timing", "epoch of reionization",
                "neutral fraction evolution",
            ],
        },
    },
    "baryon-acoustic-oscillations": {
        "extra": {
            "sound_horizon_standard_ruler": [
                "sound horizon", "standard ruler",
                "150 Mpc",
            ],
            "bao_surveys": [
                "BOSS", "eBOSS", "DESI", "2dF",
                "redshift survey BAO",
            ],
        },
    },
    # -- highenergy pages --
    "gamma-ray-bursts": {
        "extra": {
            "short_long_dichotomy": [
                "short GRB", "long GRB",
                "T90 dichotomy", "compact merger origin",
            ],
            "fireball_model": [
                "fireball model", "internal shock",
                "external shock", "afterglow",
            ],
            "host_galaxy_context": [
                "GRB host galaxy", "host metallicity",
                "host offset",
            ],
        },
    },
    "fast-radio-bursts": {
        "extra": {
            "repeater_one_off": [
                "repeating FRB", "one-off FRB",
                "FRB 121102",
            ],
            "magnetar_origin": [
                "magnetar FRB origin", "SGR 1935+2154 burst",
                "Galactic FRB",
            ],
            "host_galaxies_offsets": [
                "FRB host galaxy", "host offset",
                "globular cluster host",
            ],
        },
    },
    "gravitational-waves": {
        "extra": {
            "ligo_virgo_kagra_detections": [
                "GW150914", "GW170817",
                "GWTC", "LIGO-Virgo-KAGRA",
            ],
            "frequency_bands": [
                "LIGO band", "LISA band",
                "pulsar timing array band",
                "nanohertz", "millihertz",
            ],
            "primordial_gravitational_waves": [
                "primordial GW", "B-mode",
                "stochastic GW background",
            ],
        },
    },
    "tidal-forces": {
        "extra": {
            "tidal_disruption_events": [
                "tidal disruption event", "TDE",
                "stellar tidal disruption",
            ],
            "tidal_locking_evolution": [
                "tidal locking", "synchronous rotation",
                "spin-orbit resonance",
            ],
        },
    },
    # -- solarsystem pages --
    "exoplanets": {
        "extra": {
            "demographics": [
                "exoplanet demographics", "occurrence rate",
                "small planet abundance",
            ],
            "characterization_methods": [
                "transmission spectroscopy", "secondary eclipse",
                "direct imaging characterization",
            ],
            "atmospheric_studies": [
                "atmosphere of exoplanet", "JWST exoplanet atmosphere",
                "biosignature search",
            ],
        },
    },
    "exoplanet-detection-methods": {
        "override": {
            "transit_method": [
                "transit method", "transit photometry",
                "Kepler", "TESS",
            ],
            "radial_velocity": [
                "radial velocity", "Doppler",
                "HARPS", "ESPRESSO",
            ],
            "direct_imaging": [
                "direct imaging", "high contrast",
                "coronagraph",
            ],
            "microlensing_detection": [
                "gravitational microlensing", "OGLE", "MOA",
            ],
            "astrometric_method": [
                "astrometric detection", "Gaia astrometry",
                "stellar wobble astrometry",
            ],
            "timing_method": [
                "transit timing variation", "TTV",
                "pulsar planet timing",
            ],
            "comparative_yields": [
                "method comparison", "detection bias",
                "selection effect",
            ],
        },
    },
    "habitable-zone": {
        "extra": {
            "stellar_dependence": [
                "stellar mass dependence", "M dwarf habitable zone",
                "F-type habitable zone",
            ],
            "atmospheric_factors": [
                "greenhouse effect", "carbonate-silicate cycle",
                "atmospheric composition",
            ],
            "extended_habitability": [
                "subsurface ocean", "moon habitability",
                "extended habitable",
            ],
        },
    },
    "asteroid-belt": {
        "extra": {
            "main_belt_structure": [
                "main belt", "Kirkwood gap",
                "asteroid family",
            ],
            "near_earth_asteroids": [
                "near-Earth asteroid", "NEA",
                "potentially hazardous",
            ],
            "asteroid_composition": [
                "C-type asteroid", "S-type asteroid",
                "M-type asteroid",
            ],
        },
    },
    "kuiper-belt": {
        "extra": {
            "tno_classes": [
                "trans-Neptunian object", "TNO",
                "classical KBO", "resonant KBO",
                "scattered disk",
            ],
            "neptune_resonance": [
                "Plutinos", "Neptune resonance",
                "3:2 resonance",
            ],
            "dwarf_planets": [
                "Pluto", "Eris", "Makemake", "Haumea",
                "Kuiper belt dwarf",
            ],
        },
    },
    "oort-cloud": {
        "extra": {
            "long_period_comets": [
                "long-period comet", "LPC",
                "comet origin",
            ],
            "outer_inner_oort": [
                "outer Oort cloud", "inner Oort cloud",
                "Hills cloud",
            ],
            "stellar_perturbation": [
                "stellar flyby", "galactic tide",
                "comet shower",
            ],
        },
    },
    "planetary-formation": {
        "extra": {
            "protoplanetary_disk_evolution": [
                "protoplanetary disk", "disk dispersal",
                "disk lifetime",
            ],
            "core_accretion_vs_gravitational_instability": [
                "core accretion", "gravitational instability",
                "GI vs CA",
            ],
            "migration_processes": [
                "Type I migration", "Type II migration",
                "planet migration",
            ],
        },
    },
}


# ---------------------------------------------------------------------------
# PUBLIC API
# ---------------------------------------------------------------------------

def get_required_subtopics(slug: str) -> dict[str, list[str]]:
    """Return the merged subtopic→aliases dict for a wiki page slug.

    Resolution order:
      1. Determine category from PAGE_CATEGORY (default: "instrumentation")
      2. Start with CORE_SUBTOPICS[category]
      3. If PAGE_EXTENSIONS[slug] has "override", REPLACE the dict
      4. Else, merge "extra" into the dict
    """
    category = PAGE_CATEGORY.get(slug, "instrumentation")
    base = dict(CORE_SUBTOPICS.get(category, {}))
    ext = PAGE_EXTENSIONS.get(slug, {})
    if "override" in ext:
        return dict(ext["override"])
    if "extra" in ext:
        merged = dict(base)
        merged.update(ext["extra"])
        return merged
    return base


def is_subtopic_covered(subtopic_aliases: list[str], claim_text_blob: str) -> bool:
    """Return True if any alias appears (case-insensitive) in the claim text blob."""
    if not subtopic_aliases:
        return False
    blob = (claim_text_blob or "").lower()
    return any(alias.lower() in blob for alias in subtopic_aliases)


def coverage_ratio(slug: str, claim_texts: list[str]) -> tuple[float, list[str]]:
    """Compute (coverage_ratio, missing_subtopics) for a page.

    Returns:
        coverage_ratio: covered / required, in [0, 1]
        missing_subtopics: list of subtopic_id strings not covered
    """
    required = get_required_subtopics(slug)
    if not required:
        return 1.0, []
    blob = " ".join(claim_texts or [])
    missing = []
    for subtopic_id, aliases in required.items():
        if not is_subtopic_covered(aliases, blob):
            missing.append(subtopic_id)
    covered = len(required) - len(missing)
    return covered / len(required), missing
