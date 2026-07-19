// The public-data landscape for galaxy-evolution research.
//
// Curated by the Trikitear crew from the 50-survey Surveys directory
// (backend/data/seed_surveys.json, mirrored at /surveys): 44 of 50 surveys are
// genuinely useful for galaxy evolution; 6 are set aside as pure CMB-cosmology
// (Planck, ACT, SPT, CMB-S4), Galactic astrometry (Gaia), or high-energy blazars
// (Fermi-LAT) — real data, wrong science for galaxy build-up.
//
// Every redshift span and one-liner is grounded in that catalog. The four sources
// the pipeline actually pulls and validates today are marked `inUse`; the rest is
// the wider landscape the field draws on and that NebulaMind could add next — it is
// NOT data we currently ingest.

export type Band = "radio" | "sub_mm" | "infrared" | "optical" | "uv" | "xray" | "multi";
export type SurveyStatus = "operational" | "commissioning" | "planned" | "retired";

export type LandscapeSurvey = {
  name: string;
  band: Band;
  status: SurveyStatus;
  z0: number;      // low-z end of the extragalactic range used
  z1: number;      // high-z end (display-clamped where noted)
  arrow?: boolean; // reaches beyond the plotted axis (z1 is a floor)
  group: string;   // group key
  line: string;    // what it gives galaxy-evolution research (<= 22 words)
  inUse?: boolean; // pulled & validated by the pipeline today
};

// Wavelength bands, long -> short, plus multi. Colors match the Surveys explorer.
export const BAND_META: Record<Band, { color: string; label: string }> = {
  radio:    { color: "#ef4444", label: "Radio" },
  sub_mm:   { color: "#f97316", label: "Sub-mm" },
  infrared: { color: "#d97706", label: "Infrared" },
  optical:  { color: "#3b82f6", label: "Optical" },
  uv:       { color: "#8b5cf6", label: "UV" },
  xray:     { color: "#c026d3", label: "X-ray" },
  multi:    { color: "#14b8a6", label: "Multi" },
};

export const BAND_ORDER: Band[] = ["radio", "sub_mm", "infrared", "optical", "uv", "xray", "multi"];

export const STATUS_META: Record<SurveyStatus, { color: string; label: string; note: string }> = {
  operational:   { color: "#4ad6c4", label: "Live data",   note: "taking data / public releases out" },
  commissioning: { color: "#e0a800", label: "Commissioning", note: "on sky, first science data still to come" },
  planned:       { color: "#7c86ff", label: "Planned",      note: "no public data yet — years away" },
  retired:       { color: "#6b7386", label: "Archival",     note: "finished, but still fully queryable" },
};

export const STATUS_ORDER: SurveyStatus[] = ["operational", "commissioning", "planned", "retired"];

export type LandscapeGroup = { key: string; title: string; sub: string; desc: string };

export const GROUPS: LandscapeGroup[] = [
  { key: "spectra",  title: "Spectra — masses, metals, motions", sub: "12 surveys",
    desc: "Optical/near-IR spectrographs that read stellar mass, star-formation rate, metallicity and kinematics straight off a galaxy's light." },
  { key: "imaging",  title: "Deep imaging — photometric masses & morphology", sub: "6 surveys",
    desc: "Deep pencil-beam fields: many-band photometry gives stellar masses and photo-z; sharp imaging gives resolved shapes." },
  { key: "lensing",  title: "Wide-field imaging & weak lensing", sub: "7 surveys",
    desc: "Wide surveys mapping structure, dark matter and morphology at scale — photo-z and shear over thousands of square degrees." },
  { key: "gas",      title: "Gas & dust — the fuel and the hidden half", sub: "8 surveys",
    desc: "Radio/mm arrays weigh the cold hydrogen and molecular gas that makes stars; sub-mm/far-IR catches the dust-obscured star formation optical light misses." },
  { key: "agn",      title: "Black holes & AGN", sub: "7 surveys",
    desc: "X-ray and low-frequency radio tracing accretion onto central black holes and the feedback it drives back into the galaxy." },
  { key: "context",  title: "All-sky context", sub: "4 surveys",
    desc: "Wide, shallow all-sky maps giving AGN selection, stellar-mass proxies and photo-z priors that anchor everything above." },
];

export const LANDSCAPE: LandscapeSurvey[] = [
  // --- Spectra ---
  { name: "SDSS", band: "optical", status: "operational", z0: 0, z1: 3.5, group: "spectra", inUse: true,
    line: "z≈0 benchmark — millions of optical spectra + MaNGA IFU fix the local mass–metallicity and star-forming main-sequence relations." },
  { name: "DESI", band: "optical", status: "operational", z0: 0, z1: 3.5, group: "spectra",
    line: "14,000 deg² of z=0–3.5 galaxy spectra (BGS/LRG/ELG) tracing mass and SFR growth across cosmic time." },
  { name: "4MOST", band: "optical", status: "operational", z0: 0, z1: 4, group: "spectra",
    line: "2,436-fibre spectrograph: galaxy spectra to z=4 and AGN to z=6 over 15,000 deg²." },
  { name: "GAMA", band: "optical", status: "retired", z0: 0, z1: 0.4, group: "spectra",
    line: "z<0.4 spectra + panchromatic data anchoring stellar-mass and SFR functions and group catalogues." },
  { name: "HETDEX", band: "optical", status: "operational", z0: 1.9, z1: 3.5, group: "spectra",
    line: "~1M spectra of Lyman-α emitters at z=1.9–3.5 — star-forming galaxies at cosmic noon." },
  { name: "DEEP2", band: "optical", status: "retired", z0: 0.7, z1: 1.5, group: "spectra",
    line: "53,000 Keck spectra at z=0.7–1.5 charting red-sequence build-up and the z~1 luminosity function." },
  { name: "VIPERS", band: "optical", status: "retired", z0: 0.5, z1: 1.2, group: "spectra",
    line: "91,000 redshifts at z=0.5–1.2 mapping luminosity-function evolution and galaxy–environment links." },
  { name: "zCOSMOS", band: "optical", status: "retired", z0: 0.1, z1: 3.0, group: "spectra",
    line: "VLT spectra z=0.1–3.0 in the COSMOS field calibrating photo-z and AGN-host studies." },
  { name: "PFS", band: "optical", status: "commissioning", z0: 0.1, z1: 4, group: "spectra",
    line: "2,394 fibres for galaxies z=0.1–2 and LAEs z>2; commissioning toward the ~2026 survey." },
  { name: "WEAVE", band: "optical", status: "commissioning", z0: 0, z1: 4, group: "spectra",
    line: "New WHT multi-object + IFU spectra for galaxies z=0–2 and LOFAR radio counterparts." },
  { name: "SDSS-V", band: "optical", status: "operational", z0: 0, z1: 5, group: "spectra",
    line: "Black Hole Mapper reverberation (AGN z=0–5) plus Local Volume Mapper IFU of nearby star formation." },
  { name: "ELT", band: "optical", status: "planned", z0: 0, z1: 10, arrow: true, group: "spectra",
    line: "39 m future spectroscopy of first galaxies (z=0–10+) and resolved nearby stellar populations." },

  // --- Deep imaging ---
  { name: "COSMOS2020", band: "multi", status: "operational", z0: 0.01, z1: 10, group: "imaging", inUse: true,
    line: "1.7M sources, 30+ bands, photo-z z=0.01–10 delivering stellar-mass functions to z≈5." },
  { name: "JWST", band: "infrared", status: "operational", z0: 0, z1: 15, arrow: true, group: "imaging", inUse: true,
    line: "The high-z frontier: NIR/MIR imaging + spectroscopy probing galaxy build-up z≈0–20 at cosmic dawn." },
  { name: "HST", band: "multi", status: "operational", z0: 0, z1: 6, group: "imaging",
    line: "Deep morphology and evolution z=0–6 (CANDELS, HUDF) — the original resolved-galaxy imaging workhorse." },
  { name: "UKIDSS", band: "infrared", status: "retired", z0: 0, z1: 6, group: "imaging",
    line: "7,500 deg² NIR imaging; the deep UDS field selects galaxies and quasars to z>6." },
  { name: "VIKING", band: "infrared", status: "retired", z0: 0.1, z1: 2, group: "imaging",
    line: "NIR ZYJHKs photometry z=0.1–2 giving stellar masses and photo-z for the KiDS fields." },
  { name: "GALEX", band: "uv", status: "retired", z0: 0, z1: 1.5, group: "imaging",
    line: "All-sky UV photometry z=0–1.5 tracing unobscured star-formation rates across galaxies." },

  // --- Wide-field lensing ---
  { name: "Euclid", band: "multi", status: "operational", z0: 0, z1: 3, group: "lensing",
    line: "Space imaging + grism over 14,000 deg²: morphology z<2, weak lensing, dark-matter mapping." },
  { name: "Rubin/LSST", band: "multi", status: "commissioning", z0: 0, z1: 3, group: "lensing",
    line: "18,000 deg² ugrizy imaging: photo-z z=0–3, morphology and weak lensing at scale." },
  { name: "DES", band: "optical", status: "retired", z0: 0, z1: 2.5, group: "lensing",
    line: "691M objects, grizY photo-z z=0–2.5, weak-lensing shear over 4,787 deg²." },
  { name: "KiDS", band: "optical", status: "retired", z0: 0.1, z1: 2, group: "lensing",
    line: "1,347 deg² cosmic-shear survey, photo-z z=0.1–2.0, mapping dark matter around galaxies." },
  { name: "HSC", band: "optical", status: "operational", z0: 0, z1: 6, group: "lensing",
    line: "Deep Subaru imaging, photo-z z=0–6, morphology z<3 and lensing source galaxies." },
  { name: "UNIONS", band: "optical", status: "operational", z0: 0.1, z1: 1.5, group: "lensing",
    line: "4,800 deg² northern multi-band imaging: weak lensing z=0.1–1.5 and DESI photo-z." },
  { name: "Roman", band: "infrared", status: "planned", z0: 0, z1: 4, group: "lensing",
    line: "Future 2,000 deg² space NIR imaging + grism z=0–4 for lensing and structure." },

  // --- Gas & dust ---
  { name: "VLA", band: "radio", status: "operational", z0: 0, z1: 6, group: "gas",
    line: "HI 21cm (CHILES) plus radio-continuum SFR/AGN tracers for galaxies z=0–6." },
  { name: "MeerKAT", band: "radio", status: "operational", z0: 0, z1: 2, group: "gas",
    line: "Deep HI 21cm (LADUMA) and continuum surveys tracing gas reservoirs z=0–2." },
  { name: "ASKAP/EMU", band: "radio", status: "operational", z0: 0, z1: 5, group: "gas",
    line: "WALLABY HI to z=0.26 plus radio-continuum galaxy/AGN mapping over 30,000 deg²." },
  { name: "HIPASS", band: "radio", status: "retired", z0: 0, z1: 0.04, group: "gas",
    line: "First HI all-sky survey z<0.04, fixing the local HI mass function." },
  { name: "SKA Phase 1", band: "radio", status: "planned", z0: 0, z1: 6, arrow: true, group: "gas",
    line: "Future HI 21cm across z=0–27 and continuum z=0–6 — a transformational neutral-gas census." },
  { name: "ngVLA", band: "radio", status: "planned", z0: 0, z1: 10, arrow: true, group: "gas",
    line: "Future molecular-gas machine: CO ladder and continuum for galaxies z=0–10." },
  { name: "ALMA", band: "sub_mm", status: "operational", z0: 0, z1: 10, arrow: true, group: "gas",
    line: "Cold molecular gas and dust continuum z=0–10+, tracing obscured star formation at every epoch." },
  { name: "H-ATLAS", band: "sub_mm", status: "retired", z0: 0, z1: 6, group: "gas",
    line: "660 deg² Herschel far-IR survey z=0–6 measuring dust-obscured star formation and lensed submm galaxies." },

  // --- Black holes & AGN ---
  { name: "Chandra", band: "xray", status: "operational", z0: 0, z1: 5, group: "agn",
    line: "Sub-arcsec X-ray imaging of AGN z=0–5, resolving obscured black-hole growth and hot cluster gas." },
  { name: "CDF-S", band: "xray", status: "retired", z0: 0.01, z1: 6.5, group: "agn",
    line: "Deepest 7 Ms X-ray field: faint AGN demographics z=0.01–6.5 and black-hole/galaxy co-evolution." },
  { name: "CDF-N", band: "xray", status: "retired", z0: 0.1, z1: 5.5, group: "agn",
    line: "2 Ms X-ray field of faint AGN and X-ray galaxies z=0.1–5.5." },
  { name: "XMM-Newton", band: "xray", status: "operational", z0: 0, z1: 5, group: "agn",
    line: "Large-grasp X-ray spectroscopy of AGN z=0–5 and cluster gas z=0–1." },
  { name: "eROSITA", band: "xray", status: "operational", z0: 0, z1: 5, group: "agn",
    line: "All-sky X-ray survey: ~900k sources, AGN z=0–5 and cluster demographics z=0–1." },
  { name: "ROSAT", band: "xray", status: "retired", z0: 0, z1: 2, group: "agn",
    line: "All-sky soft X-ray catalogue (135k sources), AGN/quasars z=0–2 and local clusters." },
  { name: "LOFAR", band: "radio", status: "operational", z0: 0, z1: 6, group: "agn",
    line: "144 MHz radio continuum z=0–6+ tracing AGN feedback and star formation over 5,720 deg²." },

  // --- All-sky context ---
  { name: "WISE", band: "infrared", status: "operational", z0: 0, z1: 3, group: "context",
    line: "All-sky mid-IR: W1–W2 AGN selection z=0–3, stellar-mass proxy and nearby-galaxy dust." },
  { name: "2MASS", band: "infrared", status: "retired", z0: 0, z1: 0.1, group: "context",
    line: "All-sky NIR z<0.1 stellar-mass anchor for local galaxies (the Large Galaxy Atlas)." },
  { name: "Pan-STARRS", band: "optical", status: "operational", z0: 0, z1: 6, group: "context",
    line: "30,000 deg² optical: galaxy photo-z z=0–6, quasar searches z>6, transient context." },
  { name: "SPHEREx", band: "infrared", status: "operational", z0: 0, z1: 6, group: "context",
    line: "All-sky NIR spectrophotometry delivering photo-z for a planned 450M galaxies z=0–6." },
];

// The four sources the pipeline pulls & validates today (3 surveys + 1 simulation).
export const IN_USE = [
  { name: "SDSS", band: "optical" as Band, z: "z 0–3.5", role: "z≈0 anchor — local scaling relations (MZR, main sequence)" },
  { name: "JWST", band: "infrared" as Band, z: "z 0–15+", role: "high-z frontier — reionization-era & cosmic-noon stellar mass" },
  { name: "COSMOS2020", band: "multi" as Band, z: "z 0–10", role: "photo-z bridge — stellar-mass functions across cosmic time" },
  { name: "IllustrisTNG", band: "sim" as const, z: "simulation", role: "physics baseline — model predictions to test observations against" },
];
