# Frontier scoring — v2 queue memo (measurement-dispersion)

Decision (Trikitear, 2026-07-19): the frontier ranking was biased toward *activity/popularity*, not
*contestation*. Measurement seat proved controversy is a genuinely different signal from activity
(Spearman rho = 0.194 across the 57 clusters; ~0 on the broad lexicon). v1 (tension-lexicon reweight,
scope/tractability-gated, saturating activity floor) is SHIPPED. This memo queues v2.

## Why v2 (the real fix)
v1 uses a strict tension *lexicon* over abstracts. It works (Hubble/dark-energy cluster tops it) but is a
proxy for *prose*. The least-gameable, object-level signal is MEASUREMENT-DISPERSION: when independent
studies report discrepant values of the same physical quantity beyond their quoted errors, the spread
itself is the open question. This is exactly the metallicity-calibration-scale gotcha, generalized.

## v2 design — PDG scale-factor over extracted quantities
1. EXTRACT: Ollama judges read all 120,676 abstracts, emit (quantity, value, uncertainty, method) tuples
   (astro headline numbers are usually in the abstract). Normalize quantity names + units; keep method tag
   (to catch systematic offsets, e.g. Tremonti vs PP04 O/H).
2. DISPERSE: per well-populated quantity, compute the PDG scale factor S = sqrt(chi2/(N-1)) across the
   independent measurements (or a simpler over-dispersion ratio: inter-study scatter / median quoted sigma).
   S >> 1 = a contested quantity. Split by method to separate genuine tension from calibration offsets.
3. MAP: attribute each contested quantity back to its cluster(s); a cluster's v2 tension = aggregate
   dispersion of the quantities it argues about.
4. OPTIONAL cross-vote: citation-network modularity over time per cluster (Shwed & Bearman 2010) — rival
   camps that don't cite each other = live contestation. Cheap on our 57 cluster subgraphs. Use as a
   second, structural vote; a topic contested on BOTH text-dispersion and structure is high-confidence.

## Guardrails (carry over from v1)
- Tractability veto stays: only count dispersion on observables our held data (SDSS z~0 / JWST high-z /
  TNG / COSMOS) can actually move; CO-dominant / out-of-scope clusters vetoed.
- Keep the "string tension / brane tension / surface tension" physics-sense strip (cluster 30 false pos).
- ABLATE before shipping: does v2 change top-K vs v1, and do the changes survive novelty + expected-value
  gates at a higher rate? Keep only if it moves outcomes.
- Controversy is a RANKING signal, not a new gate. Existing novelty / expected-value / citation-entailment
  gates stay authoritative. Add a per-theme cap so top-N isn't one fight (memory: broaden beyond AGN).

## References (science-of-science)
- Measurement dispersion / PDG scale factor: Verde, Treu & Riess 2019 (Nat Astron); Di Valentino+ 2021 (CQG);
  Particle Data Group scale-factor method.
- Text disagreement (v1 basis): Lamers et al. 2021, eLife "Investigating disagreement in the scientific
  literature" (validated cue phrases; code at github.com/murrayds/sci-text-disagreement).
- Structural dissensus: Shwed & Bearman 2010, ASR "Temporal Structure of Scientific Consensus Formation".
- Citation sentiment (disputing citations): scite.ai (Nicholson+ 2021, QSS); SciCite (Cohan+ 2019, NAACL).
- NOT controversy (novelty axis, keep separate): CD/disruption index (Funk & Owen-Smith 2017; Wu, Wang &
  Evans 2019; Park, Leahey & Funk 2023); atypical combinations (Uzzi+ 2013). Sleeping Beauties (Ke+ 2015)
  as a velocity de-confounder.
