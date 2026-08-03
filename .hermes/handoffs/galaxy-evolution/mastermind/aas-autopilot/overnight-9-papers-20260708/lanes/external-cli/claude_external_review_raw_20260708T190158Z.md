I've reviewed all three manuscripts plus the source-integration packet. All cited files are present. Below is my read-only critique.

---

## Overall verdict

These are honest, unusually well-guarded pilot drafts: each repeatedly demotes its result from causal AGN-feedback proof to an optical-association / denominator diagnostic, which is the correct posture for SDSS-only line-ratio work. The dominant weakness is not overclaiming but **incompleteness and inconsistency across the set**: RP-1 is a near-complete short paper, while M2 P3 and M3 P1 are single-table addenda that lack introductions, in-text citations, and — critically — the selection-function disclosure that RP-1 carries. Two substantive methodological issues in RP-1 (the control sample is *defined* to be star-forming, and MPA-JHU sSFR uses a different estimator for AGN) are not surfaced and materially affect how the headline −1.31 dex should be read.

---

## M1 RP-1 — SDSS AGN/sSFR matched-control pilot

**Strongest element.** The selection-function disclosure (Table 1) and the S/N + optical-subclass robustness ladder (Table 2) are genuinely good practice: showing the offset weakening from −1.31 → −0.74 dex (S/N≥10) and splitting the Seyfert-like (−0.76) vs LINER-like (−1.47) branches pre-empts the obvious referee attack and is the paper's real contribution.

**Blocker / major issues.**
1. **The control class is defined to be star-forming, so a large deficit is partly tautological.** Controls are drawn only from BPT star-forming galaxies (below the Kauffmann line, i.e. on the main sequence). Any non-SF target matched only in (M⋆, z) will show a ~1 dex deficit *by construction*, because the comparison baseline is selected to have high sSFR. The −1.31 dex is therefore closer to "distance from the main sequence" than "AGN-induced suppression." This needs to be stated explicitly, and a mass-matched *all-galaxy* (or quiescent) control should bracket the result. The draft defers this to future work but does not flag that it drives the magnitude.
2. **MPA-JHU sSFR uses a different estimator for AGN vs SF galaxies.** In the Brinchmann/MPA-JHU framework, SFRs for AGN and composite hosts are not measured from the (AGN-contaminated) emission lines but inferred from the D4000–sSFR relation, whereas SF galaxies use the lines directly. Comparing the two classes partly compares two estimators, which can systematically depress the AGN side. This is arguably the single most important uncaught systematic and belongs in Data/Methods and Discussion.

**Overclaim risks.** Low overall — the guarding is thorough. Residual risk: the abstract still leads with −1.31 dex before the robustness caveat; a reader skimming will carry the large number. Recommend leading with the bracketed range (≈ −0.7 to −1.5 dex depending on subclass/S/N).

**Reproducibility gaps.** (a) `SELECT TOP 60000 ... ORDER BY s.specObjID` is not a random draw — specObjID ordering correlates with plate/observation sequence, so the 24% cache may carry a spatial/plate bias beyond the row cap; the draft attributes non-randomness only to the cap. (b) Matching is 1:1 nearest-neighbour *with replacement*, no caliper and no common-support check, despite AGN being ~0.8 dex more massive at the median (10.79 vs 10.02) — the massive SF tail is reused heavily. Report reuse rate and overlap. (c) The regression adjusts for mass and z linearly only; the main sequence is curved, so a linear term under-adjusts.

**Next 2–3 steps.** (1) Add a mass-matched quiescent/all-galaxy control arm to separate "off-main-sequence" from "AGN-associated." (2) State the MPA-JHU AGN-SFR estimator caveat and, if feasible, redo with a single consistent sSFR estimator. (3) Add a caliper + common-support diagnostic and report control-reuse.

---

## M2 P3 — mass transition in quenching and optical AGN incidence

**Strongest element.** Replacing a bare qualitative claim with an explicit numerator/denominator table (bins sum correctly to 60,000) is the right move; the co-rise of quenched (0.005→0.729) and BPT-AGN (0.003→0.520) fractions with mass is a clean, honestly framed diagnostic.

**Blocker / major issues.** (1) **The "quenched flag" threshold is never defined numerically** — "the pilot low-sSFR threshold used in the batch run" is not reproducible from the manuscript. (2) **No redshift control**: in a flux-limited sample higher-mass bins sit at higher z, so both quenched and AGN fractions are confounded by z; the mass trend needs z-stratification or a statement of the bias direction. (3) Structurally this is a table addendum, not a paper — no Introduction, no error bars, no in-text citations (the bibliography entries are uncited, which will throw LaTeX warnings and leaves every method claim ungrounded).

**Overclaim risks.** Well-controlled — the interpretation guard explicitly refuses stellar-vs-AGN feedback separation. Fine.

**Reproducibility gaps.** Missing quenched-flag value; no binomial/Wilson confidence intervals on the fractions (trivial to add and expected by referees); the 60,000 denominator inherits RP-1's 24%-cache selection function, undisclosed here.

**Next 2–3 steps.** (1) State the quenched sSFR threshold and add Wilson CIs per bin. (2) Add z-stratified fractions (or a z-controlled fit) so the mass transition isn't a redshift artefact. (3) Fold in the wave-3 mass-transition/bimodality citations (Kauffmann 2003, Peng 2012, Bluck 2023) as motivation/guards and merge into the parent manuscript rather than shipping as a standalone.

---

## M3 P1 — common-denominator optical tracer census

**Strongest element.** The S/N × tracer-definition grid makes the point that "prevalence" is not a single number but a function of selection — a legitimate methods contribution for common-denominator survey design.

**Blocker / major issues.** (1) **Several tracer definitions are undefined**: "red emission-line," "low-sSFR emission-line," and the "high [N II]/Hα" / "high [O III]/Hβ" thresholds have no numeric cuts, so the table is not reproducible. (2) **A non-monotonic result is unremarked**: high-[O III]/Hβ prevalence *rises* with stricter S/N (0.317 → 0.386) while BPT-AGN *falls* (0.136 → 0.069); this opposite behaviour is the most interesting thing in the table and deserves a sentence, not silence. (3) Like M2, it is a table fragment with no Introduction and no in-text citations.

**Overclaim risks.** Minimal — the guard cleanly restricts everything to optical and defers molecular/neutral/X-ray/radio phases.

**Reproducibility gaps.** Undefined tracer thresholds; no CIs; inherited 24%-cache selection function undisclosed; denominators (60,000/42,446/22,311) are consistent with RP-1 but the linkage isn't stated.

**Next 2–3 steps.** (1) Give explicit numeric definitions for every tracer row. (2) Add one paragraph interpreting the divergent S/N behaviour of [O III]/Hβ vs BPT-AGN. (3) Add the multiphase-outflow citations (Veilleux 2005, Cicone 2014, Fiore 2017, Bae & Woo 2018) strictly in background/future-work per the packet, and reframe explicitly as a "common-denominator design note" feeding the eventual multiphase parent.

---

## Cross-paper priorities (ranked)

1. **Propagate RP-1's selection-function disclosure to M2 P3 and M3 P1.** All three share the same capped 60,000-row cache (run SDSS-AGN-SFR-PILOT-20260708T122000Z) covering only 24.0% of the strict four-line denominator, but only RP-1 discloses it. The literature packet's own action #4 flags this. Highest priority and low effort.
2. **Define every threshold used across the set** — quenched-sSFR flag (M2), and "red / low-sSFR / high-ratio" tracer cuts (M3). Without numbers none of the tables reproduce.
3. **Add the two missing systematics to RP-1's headline** — control-class-is-SF-by-definition, and the MPA-JHU AGN-vs-SF sSFR estimator mismatch — since M2/M3 quenched/AGN statistics rest on the same sample and estimators.
4. **Integrate the wave-3 citations and convert M2/M3 from table-addenda into merged sections** of their parent manuscripts; add in-text `\citep` so the (currently uncited) bibliographies are actually used.
5. **Add confidence intervals everywhere fractions or medians appear** (Wilson intervals for M2/M3 fractions; the bootstrap CIs in RP-1 are already a good template to mirror).

No files were modified and no shell commands were run.
