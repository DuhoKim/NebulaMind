// The measurements catalog for the Lab "Research" step.
//
// Curated by the Trikitear crew. Research = the galaxy-evolution relations the
// pipeline computes, each run identically on every survey and on the simulation,
// so a disagreement that survives is physics, not apples-vs-oranges.
//
// Honesty (respected throughout): the *methods* are real, fixed recipes and the
// dispersion scores are a meta-analysis of the PUBLISHED literature's disagreement
// (N = 10–785 studies per quantity). Any specific number the pipeline auto-produces
// is DESCRIPTIVE — a draft, not a validated measurement — until a human clears it.
// So we say "computes / maps / the literature disperses by", never "we measured / found".
//
// The dispersion score is the PDG scale factor S = sqrt(chi2/(N-1)) over independent
// measurements matched by redshift AND stellar mass. S≈1 → they agree (settled);
// S≫1 → they disagree past their error bars (contested). We report the mass-controlled S.

export type Verdict = "contested" | "settled" | "z-driven" | "mzr-fixed" | "method";

export const VERDICT_META: Record<Verdict, { color: string; label: string; blurb: string }> = {
  contested: { color: "#f47272", label: "contested", blurb: "independent studies disagree past their error bars — a live frontier" },
  settled:   { color: "#4ad6c4", label: "settled",   blurb: "studies agree — solid ground to build on" },
  "z-driven":{ color: "#4ad6c4", label: "z-driven",  blurb: "the spread is cosmic evolution, not disagreement — settled once redshift is controlled" },
  "mzr-fixed":{ color: "#e0a458", label: "z>7 only",  blurb: "most of the spread is a mass mismatch; real disagreement survives only in the early universe" },
  method:    { color: "#6b7386", label: "diagnostic", blurb: "a structural diagnostic, not a single dispersion quantity" },
};

export type Source = "SDSS" | "JWST" | "COSMOS2020" | "IllustrisTNG";

export const SOURCE_META: Record<Source, { z: string; sim?: boolean }> = {
  SDSS: { z: "z≈0" },
  JWST: { z: "z=4–10" },
  COSMOS2020: { z: "photo-z" },
  IllustrisTNG: { z: "simulation", sim: true },
};

export type Measurement = {
  name: string;
  group: string;
  measures: string;
  method: string;
  tests: string;
  data: Source[];
  verdict: Verdict;
  S: number | null;      // mass-controlled PDG scale factor, where scored
  frontier?: string;     // the ranked frontier it feeds, if contested
};

export type ResearchGroup = { key: string; title: string; desc: string };

export const RESEARCH_GROUPS: ResearchGroup[] = [
  { key: "sf",    title: "Star formation",              desc: "How fast galaxies make stars, and how that rate has changed over cosmic time." },
  { key: "enrich",title: "Chemical enrichment",         desc: "How galaxies build up heavy elements as they form generations of stars." },
  { key: "mass",  title: "Mass assembly",               desc: "How galaxies grow their stellar mass — and how many exist at each mass." },
  { key: "quench",title: "Quenching",                   desc: "How and when galaxies stop forming stars and settle onto the red sequence." },
  { key: "bh",    title: "Black-hole growth",           desc: "Accretion onto supermassive black holes, and how it tracks the host galaxy." },
  { key: "reion", title: "Reionization & escaping light", desc: "The early universe — which galaxies lit it up and re-ionized the gas between them." },
  { key: "confront", title: "The confrontation",        desc: "The same relation computed identically in the flagship simulation and in the data — the sharpest test." },
];

export const MEASUREMENTS: Measurement[] = [
  // --- Star formation ---
  { name: "Star-forming main sequence", group: "sf",
    measures: "median star-formation rate vs stellar mass, for star-forming galaxies",
    method: "bin in mass → median log SFR per bin → fit slope + normalisation → repeat across redshift",
    tests: "how the SFR–mass relation lifts with redshift — the cosmic star-formation history",
    data: ["SDSS", "JWST", "IllustrisTNG"], verdict: "contested", S: 3.10, frontier: "Quenching · Dust-hidden SF" },
  { name: "Cosmic SFR density · ψ(z)", group: "sf",
    measures: "total star formation per comoving volume as a function of redshift",
    method: "integrate SFRs over the mass function in each redshift shell",
    tests: "when the universe formed most of its stars; the dust-hidden budget",
    data: ["JWST", "COSMOS2020", "SDSS", "IllustrisTNG"], verdict: "contested", S: 2.85, frontier: "JWST high-z · SMGs" },
  { name: "SF efficiency · baryon budget", group: "sf",
    measures: "stellar-to-baryon ratio M✱/(f_b·M_halo) vs halo mass",
    method: "match stellar masses to halo masses (abundance matching / native centrals)",
    tests: "whether the baryon budget even permits the observed massive-galaxy counts",
    data: ["SDSS", "COSMOS2020", "IllustrisTNG"], verdict: "method", S: null },

  // --- Chemical enrichment ---
  { name: "Mass–metallicity relation · MZR / FMR", group: "enrich",
    measures: "gas metallicity 12+log(O/H) vs stellar mass; metallicity at fixed mass + SFR (FMR)",
    method: "median O/H in mass bins on a matched abundance scale → fit → aperture check for the FMR",
    tests: "how galaxies enrich over time; whether the FMR is real or an aperture artifact",
    data: ["SDSS", "JWST", "IllustrisTNG"], verdict: "mzr-fixed", S: 2.65, frontier: "JWST high-z galaxy formation" },

  // --- Mass assembly ---
  { name: "Stellar mass function", group: "mass",
    measures: "comoving number density of galaxies per dex of stellar mass",
    method: "count in mass bins → divide by the comoving volume of each redshift shell → fit Schechter",
    tests: "mass assembly, and the JWST 'too many massive galaxies too early' tension",
    data: ["COSMOS2020", "JWST", "SDSS", "IllustrisTNG"], verdict: "settled", S: 1.06 },

  // --- Quenching ---
  { name: "Quiescent fraction", group: "quench",
    measures: "fraction of galaxies below the star-forming sequence, vs mass and redshift",
    method: "classify by sSFR / colour cut → fraction per mass–redshift bin → track its build-up",
    tests: "when and at what mass quenching switches on; environment vs mass quenching",
    data: ["COSMOS2020", "JWST", "SDSS", "IllustrisTNG"], verdict: "contested", S: 3.32, frontier: "Quenching of star formation" },

  // --- Black-hole growth ---
  { name: "Eddington ratio · AGN accretion", group: "bh",
    measures: "accretion rate relative to the Eddington limit, for active black holes",
    method: "bin AGN by mass/redshift → median λ_Edd per bin → confront samples on a matched scale",
    tests: "how fast black holes feed, and how that tracks host-galaxy growth",
    data: ["SDSS", "JWST", "IllustrisTNG"], verdict: "contested", S: 3.53, frontier: "Black-hole accretion" },

  // --- Reionization & escaping light ---
  { name: "LyC escape fraction · f_esc", group: "reion",
    measures: "fraction of a galaxy's ionizing photons that escape into intergalactic gas",
    method: "bin emitters by mass/redshift → median f_esc → confront direct vs indirect estimators",
    tests: "whether galaxies supplied the photons that reionized the universe",
    data: ["JWST", "SDSS", "IllustrisTNG"], verdict: "contested", S: 3.20, frontier: "Escaping ionizing light (LAEs)" },
  { name: "UV-LF faint-end slope · α", group: "reion",
    measures: "steepness of the faint end of the UV luminosity function",
    method: "bin galaxies in UV magnitude → number density per bin → fit the faint-end slope α",
    tests: "whether faint dwarfs dominate the reionization photon budget",
    data: ["JWST", "COSMOS2020", "IllustrisTNG"], verdict: "z-driven", S: 1.42 },

  // --- The confrontation ---
  { name: "Simulation vs observation", group: "confront",
    measures: "all of the relations above, computed identically in IllustrisTNG and in the data",
    method: "overlay the simulated and observed relations on a matched scale, bin-for-bin",
    tests: "where the flagship simulation departs from reality — the sharpest science",
    data: ["IllustrisTNG", "SDSS", "JWST", "COSMOS2020"], verdict: "method", S: null },
];

// Graphic 2 — the eight literature-dispersion quantities, sorted by mass-controlled S.
// tag is a plain-word verdict for the counter-intuitive rows.
export const DISPERSION: { name: string; S: number; verdict: Verdict; tag?: string }[] = [
  { name: "Eddington ratio", S: 3.53, verdict: "contested" },
  { name: "Quiescent fraction", S: 3.32, verdict: "contested" },
  { name: "f_esc (LyC)", S: 3.20, verdict: "contested" },
  { name: "Main-seq. slope", S: 3.10, verdict: "contested" },
  { name: "SFR density ψ(z)", S: 2.85, verdict: "contested" },
  { name: "Metallicity O/H", S: 2.65, verdict: "mzr-fixed", tag: "z>7 only" },
  { name: "UV-LF slope α", S: 1.42, verdict: "z-driven", tag: "z-driven" },
  { name: "Stellar mass fn", S: 1.06, verdict: "settled", tag: "settled" },
];
