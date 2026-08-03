# Massive-galaxy paper — DR review changelog

## Cycle 1 (2026-07-17 ~11:40 KST) — applied
DR flagged 5 verified issues; all addressed:
1. **Abundance-matching**: observed ε(z) recast as *illustrative only* (assigning all objects n=1e-5 is not rigorous AM); added explicit need for redshift-binned, completeness-corrected SMFs + forward-modelled scatter/selection; dropped claim of a measured ε(z).
2. **TNG wind physics (was WRONG)**: corrected to v_w ∝ σ_DM·(H0/H(z))^1/3 with floor → nearly z-independent at fixed halo mass; removed "denser high-z halos → faster winds."
3. **AGN**: kinetic mode disfavored for small BH, but *thermal* mode NOT excluded (needs BH mass/Eddington/energy check).
4. **FFB (Dekel+23)**: recast as *plausible-but-unproven hypothesis*; ε=0.2–1 labeled a model-assumed bracket (not derived); threshold ~5.8e11 Msun near quenching; noted FFB not resolved/explicit in TNG; **removed the hard ε≥0.4 target**.
5. **"9×" gap**: now "~3× median (9× at the observed 90th percentile)."
- **Recast headline** to a descriptive **stellar-mass-function stress test** (title + abstract); removed causal "pinpoints feedback"; feedback section retitled "Candidate mechanisms (hypotheses)."

## Cycle 1.5 addendum (3 independent audits) — applied
- (a) Added two-directional scatter caveat: intrinsic SMHM scatter (duty<1) shifts rare selected galaxies to lower-mass hosts → raises inferred ε; measurement/Eddington bias inflates observed masses → lowers deconvolved true masses.
- (b) Added satellites/centrals inconsistency caveat (abundance-match used all subhalos vs distinct-halo HMF). **Native centrals+M200c recompute DEFERRED** — TNG data server 504-timing-out on Group_M_Crit200 / SubhaloMass extractions (retried, persistent). Qualitative non-rise unaffected.
- (c) Clarified FFB ε=0.2–1 is the *instantaneous* accretion efficiency SFR/(f_b·Ṁ_h) (Li+2024 assumed bracket), distinct from the *cumulative* M*/(f_b·M_h) we compute — do not equate.
- (d) Added Ferrara, Manzoni & Ntormousi 2025 (doi:10.33232/001c.144792) contesting FFB ε≥0.4 via pre-SN Lyα radiation pressure.
- IMF: flagged Labbé=Salpeter, Chworowsky=Chabrier, Weibel=BPASS/Kroupa (~0.2 dex offsets) as additional mass systematic.

## Cycle 2 (direct-PDF audit; Gemini fetch failed→discarded) — applied
LANDED confirmed: AGN thermal, 3x median, IMF. Fixed the 5 BLOCKERS + partials:
- B1: baryon-budget conclusions (abstract/Sec4/concl) recast as *conditional illustration*; removed "model-independent"/"required"/"ΛCDM permits→astrophysical" verdicts.
- B2: efficiency relabeled "effective deterministic fixed-n conversion proxy" (not achieved/required physical efficiency); removed "ceiling/reservoir/crux"; regenerated Fig-baryon (removed "forbidden"/"impossible"→"conditional"), Fig-eff & Fig-smhm titles→"proxy". Section titles softened.
- B3: DELETED robustness overclaims ("14 well-sampled/volume-robust", "0.3 dex preserves trend", "evolves wrong way") → replaced with explicit "What we do NOT yet claim" (needs GSMF inversion + native M200c + TNG100/300 convergence).
- B4: removed satellite-caveat assertion that native recompute "would only change normalization"; now "no claim until done".
- B5: conclusion "decisive" → requires completeness-corrected GSMF + TNG100/300 convergence + spec masses.
- Wind: removed "H(z) lowers it" overclaim; added energy/mass-loading/metallicity nuance.
- FFB: Li 2024 added to bibliography + \citep; called Li a population prescription; added prerequisites.
- Bib: fixed Ferrara initial (Manzoni D. not G.); added Li et al. 2024.
DEFERRED (data-blocked): native centrals+M200c (TNG server 504s), observed-GSMF inversion, HMF mdef bracket, TNG100/300 convergence.

## Cycle 3 (verified via plain-text after PDF-fetch denial) — applied
Most blockers confirmed LANDED; precision residuals fixed:
- Wind: "approximately cancels the virial redshift scaling of σ_DM" (was "weak/mildly").
- FFB: added ~1 Myr feedback-free interval; added prerequisites (low-Z, rapid cooling, self-shielding); reworded threshold as Li-population-prescription onset near 5.8e11 Msun (not a direct density→halo conversion).
- Sec6: removed "limited equally" + causal "would point to feedback"; now states deficit could be intrinsic/observational/both, undistinguished.
- L86: "flat or falls (as in TNG)" → "as the current TNG fixed-n proxy does".
- L67: deleted confusing "characteristic mass grows" clause → "peak halo mass lower at higher redshift".
- Ferrara bib completed (The Open Journal of Astrophysics + DOI).
- Figures: Fig-baryon "plausible max"→"reference", colorbar "ε_req"→"ε (implied)"; Fig-eff y-axis→"effective fixed-n efficiency (proxy)"; Fig-1 obs line labeled "Labbé+23 z~7-9".
DEFERRED analyses unchanged (TNG server 504s / approval-gate).

## Cycle 4 (prose polish, no new analysis) — applied
- Defined "effective deterministic fixed-n conversion proxy, ε_proxy" on first use; consistent term.
- Labbé extreme candidate: removed "impossible/overestimated" → "lies above ε_proxy=1 reference; may reflect rank/mass-bias/scatter/selection/duty-cycle; cannot distinguish."
- Conclusion: "0.5 dex short at fixed number density" → "relative to the adopted fixed-n TNG benchmark, face-value JWST candidates extend ~0.5 dex higher"; "ordinary efficiencies"→"conditional proxy values below one".
- Sec6: removed "significance jointly limited" → "we do not estimate a formal discrepancy significance."
- Grammar: semicolon→comma (L67).

## Cycle 5 (global proxy-only consistency pass) — applied
Propagated the corrected proxy-only framing to abstract/intro/results/Sec4:
- Abstract: removed "at fixed abundance"/"detection density"/"hence overestimated"/"ordinary efficiencies" → "relative to adopted fixed-n TNG benchmark, JWST candidates extend ~0.5 dex higher (not a fixed-abundance measurement)"; ε→ε_proxy; baryon budget "conditional proxy values below one".
- Intro: 2nd prong no longer "permits/separates cosmology from astrophysics" → "illustrate conversion factors of an adopted fixed-n mapping; NOT the survey-volume baryon-ceiling analysis needed to distinguish".
- Results: "JWST detection density"→"adopted n=1e-5 TNG benchmark"; removed "too massive too early signature" → "individual objects are not an abundance-matched quantile".
- Sec4: "ordinary values"→"conditional proxy values below ε_proxy=1 reference".
- L61: "where TNG succeeds"→"in the face-value z<4 comparison".
- Ferrara entry completed (title + volume 8 + DOI).

## Cycle 6 (SCIENCE PASSED; final notation patch) — applied
DR: "science, caveats, and deferred-analysis boundaries now PASS." Final notation fixes:
- Sec4 opening: "ΛCDM could in principle host" → "conditional illustration asks what conversion proxy follows when each object is assigned the adopted fixed n."
- ε_proxy now defined at first use (Sec4); Sec5 references it (no redefinition); Sec4 "21% → ε_proxy>0.2", "extreme → ε_proxy>1".
- Abstract + conclusion "reproduces the abundance at z=4" → "matches the face-value abundance at z=4" (consistent with L61).

## Cycle 7 — DR REVIEW PASS ✅ (2026-07-17 ~13:36 KST)
Verified against fresh massive_draft_v7.txt (defeated read-dedup false-cache). All 3 cycle-6 residuals RESOLVED (Sec4 conditional-illustration opening; ε_proxy defined+propagated; reproduces→matches face-value). Global consistency passes: no fixed-abundance claim, no impossible/forbidden/overestimated language, deferred-analysis boundaries explicit, FFB unproven. "No remaining prose or scientific-framing issues found." SCIENCE passed at cycle 6.
LOOP CONVERGED after 6 substantive review→revise cycles (~55 fixes). Deferred ANALYSES (real next work, data-blocked by TNG server 504s / approval gate): native centrals+M200c efficiency, completeness-corrected observed GSMF inversion + forward model, HMF mdef/calibration bracket, TNG100/TNG300 resolution+volume convergence.

## Post-PASS upgrade — native centrals+M200c efficiency added (2026-07-17, TNG server recovered)
Resolved the DR-deferred native-efficiency item: downloaded TNG100 Group_M_Crit200 + GroupFirstSub (z=4,5,6); computed native central ε=M*/(f_b·M200c). Result CONFIRMS the proxy's non-rise on a proper basis: at fixed halo mass ε≈flat with z (~0.04 @ logM200c=11.5; ~0.09-0.11 @ 12), peak ε≈0.12-0.13 (LOWER than proxy 0.18-0.20 → proxy modestly over-stated TNG). z=6 box reaches only logM200c≈11.7 (massive end still needs TNG300). New Fig (fig_native) + subsection; deferred-list updated (native now in hand). Scripts: topic5/native_m200c.py.
## Native DR-verify: does NOT overturn cycle-7 pass; applied scope-'confirms'-to-sampled-range + estimand-difference (not 'over-stated') refinements.
