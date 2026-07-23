// Independent scientific-merit scores — an ADVISORY, automated assessment of each
// paper's originality × significance, scored SEPARATELY by DR (literature-grounded via
// the ADS/120k-index tool + the frontier-controversy ranking) and Kun (adversarial).
// This is NOT a validated peer-review judgment — like everything on the board it is
// descriptive, not validated; the grounded reasons matter more than the number.
// Merit = mean(DR.orig, DR.sig, Kun.orig, Kun.sig).
export type Merit = {
  originality: { dr: number; kun: number };
  significance: { dr: number; kun: number };
  drNote: string;
  kunNote: string;
};

export const PAPER_SCORES: Record<string, Merit> = {
  "/studies/z9-10-unlensed-metallicity-deficit.pdf": {
    originality: { dr: 5, kun: 4 },
    significance: { dr: 7, kun: 6 },
    drNote: "The z>7 MZR-normalization debate (Langeroodi/Sarkar/Nakajima/Isobe/Curti) is heavily worked and Isobe+2026 already reports a comparable stacked deficit, so the question isn't new; originality lives only in the specific unlensed-field + single-Te-scale + anchor-robustness (Curti vs Andrews&Martini, 0.04 dex) framing. Significance is real because it sits squarely on cluster-41 (JWST high-z, scoreV1 0.371, the #1 frontier) and honestly settles the SIGN of the metal-poor deficit, but is capped by being systematic-limited (~4.5sigma, N=5-6, not a detection).",
    kunNote: "Originality capped: it re-measures a known z>7 MZR offset on a curated N=5 unlensed subset — the only new angle is the lensing/anchor control, not a new question; significance held at 6 because it does adjudicate the sign of a genuinely live z9-10 MZR debate on lensing-free single-scale footing, but is explicitly NOT a detection and is floored by the irreducible 0.1-0.2 dex Te-scale systematic.",
  },
  "/agent-reports/research-frontiers/reionization-fesc-budget-landscape.pdf": {
    originality: { dr: 3, kun: 3 },
    significance: { dr: 6, kun: 4 },
    drNote: "The xi_ion-SFRD-fesc emissivity degeneracy is textbook (Robertson 2015) and fesc-as-least-constrained is long-established (Mitra 2013/2023, Fernandez 2011); the paper re-quantifies that known degeneracy and adds no new discriminating datum, so 'the crisis is a prior statement' is a clean synthesis, not a discovery. Significance is moderate: reionization/LyC (cluster 16, 0.161) is a genuinely two-sided live dispute (Munoz/Davies vs Duncan/Madau), but mapping the envelope without narrowing it does little to advance resolution.",
    kunNote: "Originality capped: it re-quantifies a already-understood xi_ion/SFRD degeneracy by grinding the standard Robertson maintenance equation over a systematics grid with zero new data; significance capped at 4 because its own conclusion is that neither the crisis nor the closure position is favored — it narrows nothing and concedes the discriminating datum does not exist yet.",
  },
  "/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf": {
    originality: { dr: 3, kun: 3 },
    significance: { dr: 3, kun: 2 },
    drNote: "Its own central SFMS-elevation claim is withdrawn as a selection artifact (de-biased lower envelope reaches <=0 dex below z~6, pure selection not excluded); the surviving z>6 residual and -0.4 dex MZR deficit are duplicated in papers 1 and 6, and per project memory a z~0 SDSS anchor is not a standalone paper. The only durable contribution is the emission-line selection forward-model, which is carried into #6 - as a standalone it resolves no contested claim, so both axes are low.",
    kunNote: "Significance floored: the headline z<6 SFR-elevation claim is WITHDRAWN as a pure-selection artifact (de-biased lower envelope reaches <=0 at every bin), and the two surviving pieces (z>6 residual, MZR deficit) are reported in companion papers #1/#6 — leaving no standalone result; the selection forward-model is the only mildly original element and it exists mainly to demolish the paper's own claim.",
  },
  "/agent-reports/research-frontiers/tng-massive-galaxy-abundance-systematics.pdf": {
    originality: { dr: 4, kun: 4 },
    significance: { dr: 7, kun: 5 },
    drNote: "The conclusion that the 'too massive too early' abundance is erased by stellar-mass systematics and consistent with LCDM is the emerging field consensus by 2026 - Krishnan 2026 is literally 'Resolution of the massive early JWST galaxy tension' via steep-MF systematic asymmetry, plus Boylan-Kolchin 2023 / Chen 2023 - so the question isn't new; originality is the itemized 6-axis mass ledger (0.55 dex) and the epsilon~0.20 'TNG-calibration-not-LCDM' reframe. Significance is high because it poses one falsifiable question on the single most-cited cluster-41 frontier (scoreV1 0.371), though it delivers a bounded null and honestly leaves the z>6 quiescent ~2 dex excess and z7-9 case unresolved.",
    kunNote: "Originality capped: 'the too-massive-too-early tension dissolves under stellar-mass systematics' is a crowded genre — the aperture-matched n(>M) plus itemized budget is careful bookkeeping, not a new question; the one sharp original point is the epsilon~=0.20 'TNG-calibration-not-LambdaCDM' reframe. Significance capped at 5: it touches a top-tier controversy but the z~5 verdict rests on ONE observational point vs ~20 simulated galaxies with a +-0.1 dex Poisson floor, and z7-9 is conceded as marginal/photometric.",
  },
  "/agent-reports/research-frontiers/mzr-aperture-calibration-framework.pdf": {
    originality: { dr: 2, kun: 2 },
    significance: { dr: 3, kun: 2 },
    drNote: "Self-admitted G4 novelty FAIL - a synthesis of known, settled MZR systematics (0.7 dex calibration-scale offset, aperture bias, 30-60% DIG) with no original measurement; it adjudicates no contested question because nobody disputes these are systematics. Useful as a practitioner reference (the calibration-scale offset is load-bearing for any MZR-evolution claim), but as a frontier paper both axes are near the floor.",
    kunNote: "Both axes floored: it is a methods review of calibration-scale, aperture, and DIG systematics that are already textbook (Kewley & Ellison 2008, Sanchez 2021 ARA&A) with no new measurement or datum — it structurally cannot clear a non-circular-result bar and the field already operates on these recommendations.",
  },
  "/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf": {
    originality: { dr: 6, kun: 5 },
    significance: { dr: 7, kun: 6 },
    drNote: "'Calibration is not validation' is an old principle, but the execution is the most genuinely novel of the six: two-level differencing (subtract TNG's own z~0 residual before comparing internal evolution) combined with selection-de-biasing and Te-scale matching isolates a constructed, non-circular discrepancy - TNG over-forms stars at high z while its chemistry is consistent once scales match - rather than a re-measurement or a null. Significance is high (sits on the sim-vs-physics validation the pipeline itself ranked most contested, cluster 41), and the SFR-over-evolution gap survives and widens under de-biasing as a lower bound; capped by the still-unmatched mass-aperture caveat and a selection-biased obs anchor.",
    kunNote: "Originality highest of the six: the two-level differencing that subtracts TNG's OWN z~0 calibration residual before comparing evolution is a genuinely sharp method that flips an apparent agreement into a real +0.41-0.49 dex SF over-evolution gap AND unmasks the 'chemical failure' as an abundance-scale artifact; capped at 5/6 because it is still a descriptive, human-unvalidated differential on the same public SDSS/TNG/JWST data everyone has, and 'TNG forms stars too vigorously at high z' is a hardening of a partly-known sim result, not a new discovery.",
  },
};

export function meritOf(pdf?: string | null): number | null {
  if (!pdf) return null;
  const s = PAPER_SCORES[pdf];
  if (!s) return null;
  return (s.originality.dr + s.originality.kun + s.significance.dr + s.significance.kun) / 4;
}
