// Curated AGN-feedback "status / debate map" — a reader-facing view of the
// docs-only Claim Ledger Contract v1 worked example (16 claims over 26 source
// papers), organized onto four debate axes. This is a *curated scaffold*, not a
// live database query, and it is descriptive — not validated. It mirrors the
// structure the Lab uses internally to keep counter-evidence attached to each
// claim (built + validated PASS in the status/debate-map gate, G6).
//
// Source of truth: docs/claim_ledger_contract_v1_agn_20260703T0830Z + the
// generated status_debate_map_v1.json. Kept as static data on purpose so the
// reader view can never silently drift from a live table.

export type AxisStatusKey = "settled" | "emerging" | "debated" | "model-dependent";

export type DebateClaim = {
  /** short ledger entry id, for provenance */
  id: string;
  text: string;
};

export type CounterLink = {
  text: string;
  relation: "contradicts" | "qualifies" | "same-axis position";
  /** what it pushes back on, in plain words */
  against: string;
};

export type DebateAxis = {
  key: string;
  label: string;
  question: string;
  status: AxisStatusKey;
  statusLabel: string;
  /** the reader guardrail carried verbatim from the map */
  guide: string;
  claims: DebateClaim[];
  counters: CounterLink[];
};

export const AGN_DEBATE_MAP = {
  title: "AGN feedback — what's settled vs. what's debated",
  intro:
    "A curated debate map over a 16-claim worked example (26 full-text source papers), sorted onto four axes. " +
    "It is a descriptive scaffold the Lab uses to keep the counter-evidence attached to every claim — not a live query, and not human-validated.",
  provenance: "Claim Ledger Contract v1 · status/debate map v1 · 16 claims / 4 axes / counter-evidence preserved",
  axes: [
    {
      key: "mechanism",
      label: "Mechanism",
      question: "Can AGN feedback actually remove or heat star-forming gas?",
      status: "settled",
      statusLabel: "Widely supported (scoped)",
      guide: "Can occur / can drive quenching in scoped contexts — but keep ejective outflows distinct from preventive maintenance/heating.",
      claims: [
        { id: "clc_agn2299_001", text: "AGN / SMBH feedback can expel, heat, or deplete gas in scoped contexts." },
        { id: "clc_agn_001", text: "AGN activity can drive gas outflows capable of removing or depleting star-forming fuel in selected massive or AGN-host galaxies." },
        { id: "clc_agn_004", text: "Preventive / maintenance heating is distinct from ejective outflows — and is model-dependent in this worked example." },
      ],
      counters: [
        { text: "In typical low-redshift galaxies, cold-gas outflows may be driven by star formation rather than AGN activity.", relation: "contradicts", against: "AGN as the driver of the outflows" },
        { text: "Lower central-kpc molecular gas fractions in some local AGN hosts are a scoped, local result — not global quenching.", relation: "qualifies", against: "the reach of the ejective mechanism" },
      ],
    },
    {
      key: "prevalence",
      label: "Prevalence",
      question: "How common are these outflows, really?",
      status: "emerging",
      statusLabel: "Emerging — sample-limited",
      guide: "Substantial subsets in selected samples, never universal. The measured fractions (17% MOSDEF, 46% JWST) are preserved; the single D'Eugenio case is not a prevalence anchor.",
      claims: [
        { id: "clc_agn2299_002", text: "Outflow signatures appear in substantial subsets of selected samples, with fractions and scope stated — they are not universal." },
        { id: "clc_agn_002a", text: "In the MOSDEF z = 1.4–3.8 AGN sample, ionized outflows are detected in 17% of AGNs." },
        { id: "clc_agn_002b", text: "In one JWST massive z ~ 2 sample, excess Na I D absorption is detected in 46% of massive galaxies." },
      ],
      counters: [
        { text: "The D'Eugenio 2024 GS-10578 result is a single direct z = 3 case example — not a prevalence anchor.", relation: "qualifies", against: "reading any one case as 'how common'" },
      ],
    },
    {
      key: "dominance_debate",
      label: "Dominance",
      question: "Is AGN feedback the main driver of quenching?",
      status: "debated",
      statusLabel: "Actively debated",
      guide: "AGN is one important axis, but its dominance vs. stellar feedback, gas retention, strangulation, stripping, and halo/environment channels stays debated. Alternatives are positions within the debate, not a denial that it is debated.",
      claims: [
        { id: "clc_agn2299_003", text: "AGN feedback is one important axis, but dominance relative to stellar feedback, gas retention, strangulation, stripping, halo/environment, and satellite channels remains debated and context-dependent." },
        { id: "clc_agn_009", text: "Central properties (bulge mass, velocity dispersion, black-hole mass) are a real quenching-predictor axis." },
        { id: "clc_agn_010", text: "Halo, environment, and satellite quenching are also real quenching axes — and must stay separate from central/BH predictors." },
      ],
      counters: [
        { text: "Gas retention and low star-formation efficiency can qualify simple gas-removal accounts of quenching.", relation: "qualifies", against: "AGN gas-removal as the dominant story" },
        { text: "Strangulation, environmental stripping, and cold-gas pathways remain mandatory alternative quenching channels.", relation: "same-axis position", against: "AGN being the sole driver" },
      ],
    },
    {
      key: "simulation_support",
      label: "Simulation support",
      question: "What only holds inside the models?",
      status: "model-dependent",
      statusLabel: "Model-dependent",
      guide: "In simulations / under named model assumptions — never an observed frequency. The observational maintenance-heating gap is flagged, not filled.",
      claims: [
        { id: "clc_agn_011", text: "Simulations support AGN-feedback mechanisms under named model assumptions, but do not by themselves establish observed prevalence." },
        { id: "clc_agn_004", text: "Preventive / maintenance AGN feedback is distinct from ejective outflows and is currently model-dependent in this worked example." },
      ],
      counters: [
        { text: "Model support is not observed frequency — simulations alone cannot establish how common the effect is.", relation: "qualifies", against: "treating model behavior as measured prevalence" },
      ],
    },
  ] as DebateAxis[],
};
