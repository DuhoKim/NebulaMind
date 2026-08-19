// Flagship study DATA, server-safe (no "use client"): the homepage is a server
// component and importing from FlagshipStudies.tsx (a client module) turned the
// array into a client-reference proxy whose .slice() crashed SSR (2026-08-20).
export type Flagship = { title: string; summary: string; meta: string; verdict: string; pdf: string; updated: string; review?: string; methods?: string[]; frontier?: number };

export const FLAGSHIP: Flagship[] = [
  {
    title: "The Machine-Readable Bright End: an Eligibility-Audited Census of Public z>8 Rest-UV Catalogues",
    summary: "Four independent channels were opened to measure how fast the bright end declines over z=8\u201314 from public data, and every one closed with its reason quoted from the sources. The confirmed spectroscopic bright end of the entire machine-readable record is dozens of objects \u2014 and none above z=11.5.",
    meta: "6,417 in-slice rows \u00b7 112-table eligibility layer: 67 counted, 31 closed per verdict, 4 disqualified, 10 skipped \u2014 every exclusion with its reason recorded \u00b7 92 of 112 candidates reachable ONLY by UCD metadata \u00b7 contract sha-pinned before the first fetch \u00b7 referee ESTABLISHED, 8 findings raised and closed",
    verdict: "REVIEW-READY",
    pdf: "/studies/c41-brightend-uvlf-archival-gap.pdf",
    updated: "2026-08-05 19:40",
    review: "/studies/c41-brightend-uvlf-archival-gap_review_loop.md",
    methods: ["mzr"],
    frontier: 41,
  },
  {
    title: "A Systematics-Bounded Redshift Sweep of the Reionization Ionizing-Photon Budget",
    summary: "Under frozen literature anchors, the required-vs-inferred escape-fraction mismatch becomes robust to the stated systematics only above z\u22488 (crossing z_c=8.05, bootstrap 8.03\u20138.06); removing the JWST-motivated SFRD boost strengthens the shortfall (z_c\u21927.62). Proxy transport is named as the only remaining escape route.",
    meta: "z=6\u201310 sweep (\u0394z=0.5, 40k-draw systematic MC each, fixed seed) \u00b7 referee MINOR \u2192 all four revisions applied \u00b7 referee-reproduced numbers (max dev 2.2e-16) \u00b7 4-seat merit mean 5.4 (DR abstained)",
    verdict: "REVIEW-READY",
    pdf: "/studies/fesc-zsweep-photon-budget.pdf",
    updated: "2026-08-04 21:39",
    review: "/studies/fesc-zsweep-photon-budget_review_loop.md",
    methods: ["fesc"],
    frontier: 16,
  },
  {
    title: "The Public-Archive Direct-Te Anchor Gap at z>3: A Contract-Grade Census",
    summary: "A frozen-contract census of every public VizieR table yields five contract-grade direct-Te metallicity anchors at z>3 (vs ~25 conservatively forecast) \u2014 no mass bin reaches the pre-committed minimum, so no deficit verdict is possible at contract-grade public statistics. The debate's resolution currently rests on data not publicly quotable at uniform rigor.",
    meta: "79 tables \u2192 748 z>3 auroral rows \u2192 5 anchors (S/N\u22655, source-tabulated errors, joined masses) \u00b7 reviewed-script protocol (1 review + 6 micro-deltas) \u00b7 forensics: all 5 anchors reproduced to the digit \u00b7 referee MINOR \u2192 fixed",
    verdict: "REVIEW-READY",
    pdf: "/studies/c41-highz-mzr-calibration-anchored.pdf",
    updated: "2026-08-04 21:39",
    review: "/studies/c41-highz-mzr-calibration-anchored_review_loop.md",
    methods: ["mzr"],
    frontier: 41,
  },
];
