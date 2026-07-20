// Shared per-stage items — used by the top-nav dropdowns (LabTopTabs) and the
// stage panel (LabStages).
export type SubItem = { value: string; label: string; sub?: string; desc?: string; rows?: [string, string][] };

export const TOPIC_ITEMS: SubItem[] = [
  { value: "corpus", label: "1 · Corpus", sub: "the whole library",
    desc: "We read the whole field, not a hand-picked sample — every galaxy-evolution and cosmology paper since 2009 (120,676 of them), each one wired to the papers it cites." },
  { value: "embedding", label: "2 · Embedding", sub: "papers → points on a map",
    desc: "We place every paper on a map of meaning, so papers about the same physics land right next to each other — the computer can tell what a paper is about, not just match keywords." },
  { value: "clustering", label: "3 · Clustering", sub: "57 self-organized topics",
    desc: "We let the papers sort themselves: left alone on the map, they clump into 57 research topics — nobody drew the boundaries or named the fields." },
  { value: "overlay", label: "4 · Activity overlay", sub: "where it’s unsettled",
    desc: "We light up the same map by what’s still being argued about — how hard the field is still citing each topic shows which are live frontiers and which have settled." },
  { value: "ranking", label: "5 · Ranking", sub: "frontiers rise to the top",
    desc: "We rank topics by disagreement, not popularity: where independent measurements of the same thing (matched by redshift and galaxy mass) fail to agree, the field has an open question worth attacking. JWST high-z, black-hole accretion, LyC escape and quenching rise to the top and become the studies." },
];

export const DATA_ITEMS: SubItem[] = [
  { value: "SDSS", label: "SDSS", sub: "SkyServer SQL · z≈0 anchor", rows: [
    ["What", "The Sloan Digital Sky Survey — ~10⁶ nearby galaxies with spectra. We read galSpecExtra (stellar masses, gas metallicities) and galSpecLine (emission-line fluxes)."],
    ["How", "Live SQL against the SkyServer DR18 service; plus GSWLC-2 (GALEX+WISE SFRs) and MPA-JHU catalogs via VizieR TAP."],
    ["Anchors", "The local benchmark — mass–metallicity relation, the star-forming main sequence, and the FMR that high-z is measured against."],
    ["Caveat", "Tremonti O/H sits ~0.24 dex above Tₑ-anchored scales; reconciled before any cross-survey comparison."],
  ] },
  { value: "JWST", label: "JWST", sub: "VizieR catalogs · high-z frontier", rows: [
    ["What", "Rest-frame optical spectra of galaxies at z≈4–10 from NIRSpec — the first statistical look at early chemical evolution."],
    ["How", "VizieR TAP (ADQL): Nakajima+23 (180 NIRSpec), Lisiecki+25 (3743 MIRI/CEERS), Chworowsky+24 (massive z≈4–7)."],
    ["Enables", "The mass–metallicity relation and main sequence out to the JWST frontier; the massive-galaxy tension."],
    ["Caveat", "Small samples, selection effects, and strong-line calibrations pushed far from where they were derived."],
  ] },
  { value: "COSMOS2020", label: "COSMOS2020", sub: "VizieR · photometric masses to z≈5", rows: [
    ["What", "~1.7M photometric galaxies over the COSMOS field with LePhare/EAZY stellar masses and photo-z."],
    ["How", "VizieR TAP; used in the overnight run for stellar-mass-function and main-sequence evolution across redshift."],
    ["Enables", "Mass assembly — the number density of massive galaxies vs z; the main sequence out to z≈3."],
    ["Caveat", "Photometric-redshift scatter; uncorrected for completeness / Vmax."],
  ] },
  { value: "IllustrisTNG", label: "IllustrisTNG", sub: "simulation API · sim vs obs", rows: [
    ["What", "A flagship cosmological hydrodynamic simulation. We read TNG100-1 group catalogs (subhalo masses, SFRs, metallicities)."],
    ["How", "The TNG public API, snapshot by snapshot (z=0/4/5/6); h=0.6774, f_b=0.1575."],
    ["Tests", "Whether the simulation reproduces the observed scaling relations and mass functions."],
    ["Caveat", "TNG is tuned to a few z≈0 observables; the real test is its predictions away from that calibration."],
  ] },
];

export const RESEARCH_ITEMS: SubItem[] = [
  { value: "ms", label: "Star-forming main sequence", sub: "scaling-relation evolution", rows: [
    ["Measures", "Median log SFR in stellar-mass bins for star-forming galaxies (an sSFR cut)."],
    ["How", "Bin in mass, take medians, fit slope + normalisation; repeat across redshift."],
    ["Tests", "How the SFR–mass relation rises with redshift — the cosmic star-formation history."],
  ] },
  { value: "mzr", label: "Mass–metallicity relation", sub: "chemical evolution", rows: [
    ["Measures", "12+log(O/H) vs stellar mass; and the FMR (metallicity at fixed mass + SFR)."],
    ["How", "Median O/H in mass bins on a matched abundance scale; an aperture check for the FMR."],
    ["Tests", "How galaxies enrich over time; whether the FMR is real or an aperture artifact."],
  ] },
  { value: "smf", label: "Stellar mass function", sub: "abundance / assembly", rows: [
    ["Measures", "Comoving number density of galaxies per dex of stellar mass."],
    ["How", "Count in mass bins, divide by the comoving volume of each redshift shell."],
    ["Tests", "Mass assembly and the JWST ‘too many massive galaxies too early’ tension."],
  ] },
  { value: "eff", label: "SF efficiency / baryon budget", sub: "M★ vs halo", rows: [
    ["Measures", "The stellar-to-baryon ratio M★/(f_b M_halo) vs halo mass."],
    ["How", "Match stellar masses to halo masses (abundance matching / native centrals)."],
    ["Tests", "Whether the baryon budget even allows the observed massive-galaxy counts (Boylan-Kolchin)."],
  ] },
  { value: "simobs", label: "Simulation vs observation", sub: "confrontation", rows: [
    ["Measures", "The same relations, computed identically in TNG and in the data."],
    ["How", "Overlay the simulated and observed relations on a matched scale."],
    ["Tests", "Where the flagship simulation departs from reality — the sharpest science."],
  ] },
];

export const PAPER_ITEMS: SubItem[] = [
  { value: "progress", label: "Papers in progress", sub: "the live board",
    desc: "Every paper the Lab is currently working, live from the pipeline — where each run stopped, the referee’s verdict, and the descriptive draft PDF you can open. Honest attrition: most stop early and none is validated.",
    rows: [
    ["Live", "Reads the Lab’s own run pipeline and refreshes on load — the real runs, not a snapshot."],
    ["Shows", "A funnel by stage, the referee-verdict mix, and a card per run with its draft PDF and figure."],
    ["Honest", "0 accepted, 0 validated. The PDFs are descriptive drafts a human has not yet vouched for — not published papers."],
  ] },
  { value: "draft", label: "AASTeX draft + figures", sub: "the manuscript", rows: [
    ["What", "A journal-style manuscript: title, abstract, method, the study’s figure, results, and honest caveats."],
    ["How", "Filled from the study’s real numbers and compiled to PDF with tectonic (the AAS aastex631 class)."],
  ] },
  { value: "review", label: "Referee → revise loop", sub: "hardening", rows: [
    ["What", "An automated referee (astrosage-70b) reads the draft and issues a verdict: ACCEPT / MINOR / MAJOR / REJECT."],
    ["How", "On MAJOR/REJECT the author revises — softening overclaims, adding caveats, never inventing numbers — then re-reviews, until it holds."],
  ] },
  { value: "gates", label: "Gates & honest labeling", sub: "the bar", rows: [
    ["Gates", "Before a draft counts, it must clear a novelty gate (is the result actually new?) and a citation-entailment gate (does every cited paper really support the claim?)."],
    ["Honest label", "Bounded automated results are labeled descriptive — not validated measurements — until a human review clears them; a MINOR referee verdict means small fixes, not acceptance."],
  ] },
];

export function itemsFor(tab: string): SubItem[] {
  if (tab === "topic") return TOPIC_ITEMS;
  if (tab === "data") return DATA_ITEMS;
  if (tab === "research") return RESEARCH_ITEMS;
  return PAPER_ITEMS;
}
