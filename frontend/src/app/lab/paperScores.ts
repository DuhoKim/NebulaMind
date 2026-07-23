// Independent scientific-merit scores — an ADVISORY, automated assessment of each
// paper's originality × significance, scored SEPARATELY by a five-member panel:
// DR (literature-grounded) + the Quartet (Hwao, Tori, Kun, Goru), each through a
// distinct lens. NOT a validated peer-review judgment; the grounded reasons matter
// more than the number. Merit = mean over all 5 evaluators × both axes.
export type Evaluator = "dr" | "hwao" | "tori" | "kun" | "goru";
export type EvalScore = { originality: number; significance: number; note: string };
export type Merit = { scores: Record<Evaluator, EvalScore> };

export const EVALUATORS: { key: Evaluator; label: string; lens: string }[] = [
  { key: "dr", label: "DR", lens: "literature precedent" },
  { key: "hwao", label: "Hwao", lens: "synthesis & field impact" },
  { key: "tori", label: "Tori", lens: "framing & motivation" },
  { key: "kun", label: "Kun", lens: "adversarial" },
  { key: "goru", label: "Goru", lens: "rigor & result-solidity" },
];

export const PAPER_SCORES: Record<string, Merit> = {
  "/studies/z9-10-unlensed-metallicity-deficit.pdf": { scores: {
    dr: { originality: 5, significance: 7, note: "The z>7 MZR-normalization debate (Langeroodi/Sarkar/Nakajima/Isobe/Curti) is heavily worked and Isobe+2026 already reports a comparable stacked deficit, so the question isn't new; originality lives only in the specific unlensed-field + single-Te-scale + anchor-robustness (Curti vs Andrews&Martini, 0.04 dex) framing. Significance is real because it sits squarely on cluster-41 (JWST high-z, scoreV1 0.371, the #1 frontier) and honestly settles the SIGN of the metal-poor deficit, but is capped by being systematic-limited (~4.5sigma, N=5-6, not a detection)." },
    hwao: { originality: 6, significance: 8, note: "The early-MZR normalization is a genuinely top-ranked open frontier, and isolating unlensed field anchors on a single Te scale is a real adjudication of a contested question — though it's a careful re-analysis of existing compilations rather than a new line of attack, and it stays sign-only (N=5) short of settling the value." },
    tori: { originality: 8, significance: 9, note: "Sharp, honestly-posed wedge: it isolates the two systematics (lensing and anchor-extrapolation) that both bite exactly the disputed normalization, then neutralizes both with an unlensed field sample on one Te scale — a genuinely fresh way to adjudicate a live, high-stakes debate." },
    kun: { originality: 4, significance: 6, note: "Originality capped: it re-measures a known z>7 MZR offset on a curated N=5 unlensed subset — the only new angle is the lensing/anchor control, not a new question; significance held at 6 because it does adjudicate the sign of a genuinely live z9-10 MZR debate on lensing-free single-scale footing, but is explicitly NOT a detection and is floored by the irreducible 0.1-0.2 dex Te-scale systematic." },
    goru: { originality: 6, significance: 8, note: "Truly differential Te-anchored deficit, robustness-tested across two anchors and an independent 1500-gal stack, and disciplined enough to deflate its own 22σ to ~4.5σ and refuse a detection — the most solid result here, docked only because the z9-10-specific value still rests on ~5-6 galaxies." },
  } },
  "/agent-reports/research-frontiers/reionization-fesc-budget-landscape.pdf": { scores: {
    dr: { originality: 3, significance: 6, note: "The xi_ion-SFRD-fesc emissivity degeneracy is textbook (Robertson 2015) and fesc-as-least-constrained is long-established (Mitra 2013/2023, Fernandez 2011); the paper re-quantifies that known degeneracy and adds no new discriminating datum, so 'the crisis is a prior statement' is a clean synthesis, not a discovery. Significance is moderate: reionization/LyC (cluster 16, 0.161) is a genuinely two-sided live dispute (Munoz/Davies vs Duncan/Madau), but mapping the envelope without narrowing it does little to advance resolution." },
    hwao: { originality: 7, significance: 7, note: "Reframing the reionization 'photon-budget crisis' as a statement about the ξion/SFRD priors rather than f_esc is a clever, clarifying move on a first-tier question, but it points at what to measure instead of moving the field to a verdict, which caps its field impact." },
    tori: { originality: 8, significance: 7, note: "Clever inversion of the narrative — it reframes the celebrated 'photon-budget crisis' as an artifact of the adopted xi_ion and SFRD priors rather than of f_esc, which is a real and deflationary reconception, though what it ultimately settles ('the data favour neither') is more modest than the question's stakes." },
    kun: { originality: 3, significance: 4, note: "Originality capped: it re-quantifies a already-understood xi_ion/SFRD degeneracy by grinding the standard Robertson maintenance equation over a systematics grid with zero new data; significance capped at 4 because its own conclusion is that neither the crisis nor the closure position is favored — it narrows nothing and concedes the discriminating datum does not exist yet." },
    goru: { originality: 5, significance: 6, note: "A clean, non-circular designed sensitivity analysis whose O32/β swap is an explicit non-circularity check, but it re-quantifies a known ξion/SFRD degeneracy with no new discriminating datum — it maps the envelope rather than narrowing it." },
  } },
  "/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf": { scores: {
    dr: { originality: 3, significance: 3, note: "Its own central SFMS-elevation claim is withdrawn as a selection artifact (de-biased lower envelope reaches <=0 dex below z~6, pure selection not excluded); the surviving z>6 residual and -0.4 dex MZR deficit are duplicated in papers 1 and 6, and per project memory a z~0 SDSS anchor is not a standalone paper. The only durable contribution is the emission-line selection forward-model, which is carried into #6 - as a standalone it resolves no contested claim, so both axes are low." },
    hwao: { originality: 5, significance: 4, note: "The selection-aware posture is honest and methodologically worthwhile, but the paper withdraws its own central SFR-evolution claim and its surviving pieces (z>6 residual, MZR deficit) are carried by the flagship — so as a field contribution it's mostly cautionary." },
    tori: { originality: 5, significance: 4, note: "Intellectually honest but self-defeating as framed: its headline SFMS-elevation claim is withdrawn as a selection artifact and the surviving MZR result is deferred to a companion, so the motivation collapses to a caveat-forward posture rather than a question it can answer on its own." },
    kun: { originality: 3, significance: 2, note: "Significance floored: the headline z<6 SFR-elevation claim is WITHDRAWN as a pure-selection artifact (de-biased lower envelope reaches <=0 at every bin), and the two surviving pieces (z>6 residual, MZR deficit) are reported in companion papers #1/#6 — leaving no standalone result; the selection forward-model is the only mildly original element and it exists mainly to demolish the paper's own claim." },
    goru: { originality: 5, significance: 4, note: "Now honestly selection-aware — the forward-modeled emission-line debiasing is a competent method — but the headline SFMS-elevation/rapid-enrichment claim has collapsed to a null below z≈6 (pure selection unexcluded), leaving a deflationary result whose only survivors are a thin z>6 residual and an MZR deficit owned by the companion paper." },
  } },
  "/agent-reports/research-frontiers/tng-massive-galaxy-abundance-systematics.pdf": { scores: {
    dr: { originality: 4, significance: 7, note: "The conclusion that the 'too massive too early' abundance is erased by stellar-mass systematics and consistent with LCDM is the emerging field consensus by 2026 - Krishnan 2026 is literally 'Resolution of the massive early JWST galaxy tension' via steep-MF systematic asymmetry, plus Boylan-Kolchin 2023 / Chen 2023 - so the question isn't new; originality is the itemized 6-axis mass ledger (0.55 dex) and the epsilon~0.20 'TNG-calibration-not-LCDM' reframe. Significance is high because it poses one falsifiable question on the single most-cited cluster-41 frontier (scoreV1 0.371), though it delivers a bounded null and honestly leaves the z>6 quiescent ~2 dex excess and z7-9 case unresolved." },
    hwao: { originality: 6, significance: 7, note: "Cleanly separating 'ΛCDM stress test' from 'TNG calibration tension' and deflating the headline too-massive-too-early z~5 claim with an itemized mass budget is a valuable conceptual clarification of a much-hyped JWST tension, while honestly flagging the quiescent-galaxy residual that actually survives." },
    tori: { originality: 7, significance: 8, note: "Cleanly separates two questions the 'too massive too early' discourse routinely conflates — a mismatch against TNG's specific calibration versus a breach of LambdaCDM feasibility — and replaces a hand-waved '~1 dex' budget with an itemized ledger; a well-motivated, clarifying framing of a much-hyped tension." },
    kun: { originality: 4, significance: 5, note: "Originality capped: 'the too-massive-too-early tension dissolves under stellar-mass systematics' is a crowded genre — the aperture-matched n(>M) plus itemized budget is careful bookkeeping, not a new question; the one sharp original point is the epsilon~=0.20 'TNG-calibration-not-LambdaCDM' reframe. Significance capped at 5: it touches a top-tier controversy but the z~5 verdict rests on ONE observational point vs ~20 simulated galaxies with a +-0.1 dex Poisson floor, and z7-9 is conceded as marginal/photometric." },
    goru: { originality: 4, significance: 7, note: "A standard number-density confrontation but rigorously executed: disjoint-by-construction (non-circular), and the aperture fix I verified against real TNG100-1 strengthens it (required shift 0.28→0.20 dex, IMF-independent) — solid bounded null, dinged because the anchor is only 15-20 Poisson-fragile objects against a single obs point." },
  } },
  "/agent-reports/research-frontiers/mzr-aperture-calibration-framework.pdf": { scores: {
    dr: { originality: 2, significance: 3, note: "Self-admitted G4 novelty FAIL - a synthesis of known, settled MZR systematics (0.7 dex calibration-scale offset, aperture bias, 30-60% DIG) with no original measurement; it adjudicates no contested question because nobody disputes these are systematics. Useful as a practitioner reference (the calibration-scale offset is load-bearing for any MZR-evolution claim), but as a frontier paper both axes are near the floor." },
    hwao: { originality: 3, significance: 4, note: "A competent synthesis of known calibration/aperture/DIG systematics and useful plumbing for any MZR-evolution claim, but it restates established effects without a new result and moves no open question by itself." },
    tori: { originality: 4, significance: 5, note: "A tidy, honest housekeeping synthesis that separates calibration-scale from aperture bias, but it poses no sharp research question of its own — it organizes known systematics into a checklist, useful plumbing for the other papers rather than a framing with its own stakes." },
    kun: { originality: 2, significance: 2, note: "Both axes floored: it is a methods review of calibration-scale, aperture, and DIG systematics that are already textbook (Kewley & Ellison 2008, Sanchez 2021 ARA&A) with no new measurement or datum — it structurally cannot clear a non-circular-result bar and the field already operates on these recommendations." },
    goru: { originality: 3, significance: 2, note: "A synthesis/review that makes no measurement — trivially non-circular because there is no result to be circular, and correspondingly empty of any testable, defensible finding." },
  } },
  "/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf": { scores: {
    dr: { originality: 6, significance: 7, note: "'Calibration is not validation' is an old principle, but the execution is the most genuinely novel of the six: two-level differencing (subtract TNG's own z~0 residual before comparing internal evolution) combined with selection-de-biasing and Te-scale matching isolates a constructed, non-circular discrepancy - TNG over-forms stars at high z while its chemistry is consistent once scales match - rather than a re-measurement or a null. Significance is high (sits on the sim-vs-physics validation the pipeline itself ranked most contested, cluster 41), and the SFR-over-evolution gap survives and widens under de-biasing as a lower bound; capped by the still-unmatched mass-aperture caveat and a selection-biased obs anchor." },
    hwao: { originality: 7, significance: 8, note: "Sim-versus-physics validation is the field's most contested frontier, and the two-level 'calibration is not validation' differencing plus like-for-like selection/aperture handling isolates a specific, reproducible, non-circular TNG failing (too much high-z star formation) — the kind of falsifiable result that actually steers simulation work." },
    tori: { originality: 8, significance: 8, note: "'Calibration is not validation' is a genuinely sharp methodological framing — the insistence on subtracting TNG's own z~0 residual before comparing evolution shows a naive test would have hidden the real star-formation over-evolution and invented a spurious chemical failure; a well-motivated attack on the field's most contested frontier." },
    kun: { originality: 5, significance: 6, note: "Originality highest of the six: the two-level differencing that subtracts TNG's OWN z~0 calibration residual before comparing evolution is a genuinely sharp method that flips an apparent agreement into a real +0.41-0.49 dex SF over-evolution gap AND unmasks the 'chemical failure' as an abundance-scale artifact; capped at 5/6 because it is still a descriptive, human-unvalidated differential on the same public SDSS/TNG/JWST data everyone has, and 'TNG forms stars too vigorously at high z' is a hardening of a partly-known sim result, not a new discovery." },
    goru: { originality: 7, significance: 7, note: "The two-level differencing (subtract TNG's own z≈0 residual, compare internal evolution) is the portfolio's cleverest move for escaping the calibration≠validation trap, and its SFR over-evolution survives AND widens after selection debiasing — robust and near-a-lower-bound, held back only by an uncorrected 2R½-vs-SED mass-definition mismatch of comparable magnitude to the signal." },
  } },
};

export function meritOf(pdf?: string | null): number | null {
  if (!pdf) return null;
  const m = PAPER_SCORES[pdf];
  if (!m) return null;
  const vals = Object.values(m.scores).flatMap((s) => [s.originality, s.significance]);
  return vals.reduce((a, b) => a + b, 0) / vals.length;
}

// Panel means per axis (for compact displays like the ranking leaderboard).
export function axisMeans(pdf?: string | null): { orig: number; sig: number } | null {
  if (!pdf) return null;
  const m = PAPER_SCORES[pdf];
  if (!m) return null;
  const ss = Object.values(m.scores);
  return {
    orig: ss.reduce((a, s) => a + s.originality, 0) / ss.length,
    sig: ss.reduce((a, s) => a + s.significance, 0) / ss.length,
  };
}
