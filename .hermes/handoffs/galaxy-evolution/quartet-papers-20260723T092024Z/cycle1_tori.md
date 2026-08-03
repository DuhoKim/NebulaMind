# Cycle 1 — Tori: motivation literature-grounding triage (6 papers)

Method: read each manuscript's claimed open question, then ground-checked with `tools/nm_fulltext_layer.py` against the local 120k / ADS index. Verdict axis = is the "open question / tension" a REAL, currently-contested, citable question — and does the paper frame/cite it that way.

### 1. z9–10 unlensed metallicity deficit
- **Motivation verdict:** grounded
- **Real open question?** Yes — MZR evolution into z>7 and whether early galaxies are as metal-poor as chemical-evolution models predict is live and contested (Sarkar 2025 "Revisiting the MZR with JWST/NIRSpec at 4<z<10"; Stanton 2026 EXCELS gas-phase metallicity evolution 2<z<8; Curti 2023 direct-Te at z~8). Intro cites the real anchors (Nakajima 2023, Pollock 2026, Isobe 2026, Curti 2020, Andrews & Martini 2013).
- **The one thing that would ground it:** State up front the specific contested claim it adjudicates (rapid-early-enrichment outliers vs. a metal-poor floor) rather than presenting the deficit as a standalone measurement — the motivation is real but the paper reads as "we measured X," not "we settle debate Y."

### 2. reionization f_esc photon-budget landscape
- **Motivation verdict:** grounded (strongest of the six)
- **Real open question?** Yes, and textbook-framed — the intro names BOTH sides of a genuine live dispute: "photon-budget crisis" (Muñoz 2024, Davies 2021) vs. star-forming galaxies suffice (Duncan & Conselice 2015, Madau 2017), with the ξion/SFRD/fesc decomposition from Robertson 2015. Grounding index corroborates fesc as the least-constrained, actively-modeled ingredient (Mitra 2013/2023, Fernandez 2011). The paper's thesis — the "crisis" is to first order a disagreement in ξion and SFRD priors — is exactly the contested pivot.
- **The one thing that would ground it:** Already grounded; only sharpen by quoting the specific published "required-fesc" numbers from the crisis-side papers it cites so the reader sees the prior-driven spread it reproduces.

### 3. galaxy scaling relations z0→JWST (draft, no verdict)
- **Motivation verdict:** thin (grounded framing, but the paper is largely an anchor + differential measurement)
- **Real open question?** The contested premise it invokes (early galaxies metal-poor "as expected" vs. rapid early enrichment; Nakajima 2023, Curti 2024, Sanders 2021) is real. But the deliverable is offsets of JWST galaxies from re-anchored z≈0 SDSS SFMS/MZR — and project memory is explicit that z≈0 SDSS relations are anchors, not standalone papers. It resolves no contested claim; it is a descriptive feeder for paper 6.
- **The one thing that would ground it:** Convert the "flat metallicity offset + enriched outliers" result into a direct test of one named model prediction (i.e., is the offset consistent/inconsistent with a specific hierarchical chemical-evolution prediction), so it attacks the contested question instead of characterizing the anchor.

### 4. TNG massive-galaxy abundance systematics
- **Motivation verdict:** grounded (flagship contested frontier)
- **Real open question?** Yes — the JWST "impossibly early / too-massive galaxies vs ΛCDM" tension is one of the most-cited open questions in the field (Boylan-Kolchin 2023 "Stress testing ΛCDM"; Lovell 2023 extreme-value ΛCDM tension; Labbé 2023, cited in intro; Krishnan 2026 "Resolution of the massive early JWST galaxy tension"). Both the tension AND the systematics-resolution it argues are densely citable. Poses a single falsifiable question (does the excess exceed the M* systematic budget).
- **The one thing that would ground it:** Add the halo-mass-function ceiling explicitly (Boylan-Kolchin/Lovell extreme-value framing) so the "erased by ~0.28 dex" result is benchmarked against the actual ΛCDM stress-test that made this a frontier.

### 5. MZR aperture/calibration framework (review-cleared)
- **Motivation verdict:** thin/ungrounded as a research motivation (grounded only as a methods review)
- **Real open question?** No contested OPEN question — the systematics it catalogs (0.7 dex calibration-scale offset, aperture bias, DIG) are real and citable but settled/known; the referee log itself records G4 novelty FAIL and re-labels it a "practitioner's framework," not a frontier attack. It synthesizes, it does not adjudicate a live dispute.
- **The one thing that would ground it:** Attach the framework to a specific unresolved MZR controversy it can move — e.g., demonstrate that the high-mass MZR turnover is aperture-induced vs physical on real IFU data — turning a synthesis into a contested claim.

### 6. TNG validation — calibration≠validation (draft, no verdict)
- **Motivation verdict:** grounded
- **Real open question?** Yes — "calibration is not validation": whether TNG's tuned-at-z≈0 physics predicts the correct evolution is a genuine sim-vs-observation frontier (Pillepich 2018, Nelson 2019 cited; same massive-galaxy/tension literature from paper 4's index applies). The result — TNG over-forms stars at high z (calibration-independent), while chemistry is consistent once abundance scales are matched — is non-circular and defensible by construction (two-level differencing removes the calibration offset).
- **The one thing that would ground it:** Cite an existing published claim of a TNG high-z SFMS/MZR discrepancy (or its absence) so the "over-strong main-sequence growth" result lands against a named prior expectation rather than only against TNG's own z≈0 residual.

---
**Ranking (motivation axis).** STRONGEST: #2 (reionization f_esc) and #4 (TNG massive-galaxy abundance) — each names a live, two-sided, densely-citable dispute and cites both camps; #6 (calibration≠validation) close behind. WEAKEST: #5 (methods synthesis, self-admitted no novelty, no contested question) and #3 (grounded framing but a z≈0-anchored descriptive offset, resolving no contested claim — the "anchors, not standalone papers" flag).
**Best-positioned to clear the publishable bar on motivation:** #4 — it attacks the single most-cited contested JWST-vs-ΛCDM frontier (Boylan-Kolchin/Labbé/Lovell/Krishnan), poses one falsifiable question, and both the tension and its systematic resolution are heavily grounded. #2 is a very close second.
