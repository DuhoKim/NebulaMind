# Overnight publishable-quality run — LEDGER

## Phase P1 · Paper A (z>7 MZR) · gate audit (astrosage-70b referee)
- G2 non-circularity: FAIL — evidence set == hypothesis set (~N=4 lensed galaxies); no disjoint/orthogonal confirmation.
- G3 calibration: FAIL — common O/H scale + survival-past-0.24dex not established.
- Decision: REVISE. DROP detection framing. Cap at explicitly selection-bounded / consistency claim.
- Next for A: (1) reconcile all z>7 O/H onto one Te/O3N2 scale + record per-object provenance; (2) leave-one-out over N=4; (3) reframe abstract+conclusion to upper-limit/consistency; (4) re-referee.
- Status: A → REVISE (bounded-descriptive path; NOT a detection). Consistent with pre-registration.

## Next phases (scheduled)
- P1 continued: A calibration reconciliation; begin Paper B (TNG SMF, non-circular by construction — like-for-like M*, cumulative n(>M*,z) vs systematic budget).
- Corpus grounding (qwen3-embedding over 120k ADS) substitutes for DR autonomously; DR queries filed in DR_QUEUE.md for a browser session.

## DR — delegated to Tori (kanban t_3fbb9efe, RUNNING as of 23:44 KST)
- Could not drive DR from the background job (TCC -1743 denies Apple Events; :19223 CDP is Goru's live browser — not hijacked). Asked Tori via the shared kanban board (the sanctioned crew channel).
- Tori runs the 3 queries in Gemini Deep Research (authenticated lane), files reports to dr_results/ (dr1/dr2/dr3.md), reference-only (no .tex/DB writes).
- LOOP: on each wakeup, check dr_results/ — if present, cite as lit-grounding in the relevant paper's motivation/discussion (supersedes the corpus-only substitute). Do NOT block on it.

## Phase P2 (00:26 KST) · Paper A REVISED → re-refereed
- Calibration-clean recompute: restricted to direct-Te subset (N=6) vs Curti+2020 local MZR (Te-consistent). No mixed strong-line calibs in the claim.
- Deficit = -0.47 +/- 0.10 dex; leave-one-out range -0.41..-0.59 (no single galaxy drives it). Mixed-calib N=40 gives -0.61 (EXCLUDED as scale-contaminated — the G3-fail path).
- astrosage re-referee: G3 PASS (Te-consistent scale) · G2 PASS-as-bounded-descriptive (no external confirmation → not a detection) · G6 PASS (honest label).
- **VERDICT: A → ACCEPT-as-human-review-ready (bounded-descriptive), caveat N=6 small sample.** NOT a detection. Queued for human sign-off (still 0 validated).
- Remaining polish: state the N=6 direct-Te restriction + Curti-scale explicitly in abstract/method; note DR#1 (independent z>7 anchors) may add external context when Tori's report lands.

## Phase P2 · Paper B (TNG SMF) · gate setup
- G1 motivation: contested frontier (sim "too massive too early" vs JWST) — grounded. PASS (pending citation via DR#2/corpus).
- G2 non-circularity: PASS by construction (TNG prediction vs independent JWST obs; disjoint by design).
- G3 calibration: N/A (axis is stellar mass, not O/H) — but M* systematics (IMF/aperture/SED prior) are the analogue and are the open work.
- OPEN (blocks ACCEPT): like-for-like M* (aperture+IMF+SED-prior matched) + cumulative n(>M*,z) vs the systematic budget; needs JWST high-z SMF numbers (DR#2 pending / data pull). Have TNG100 n(>10^10.5)=1.49e-3 Mpc^-3 from prior run.
- **STATUS: B → in-progress (G1/G2 pass; systematic-budget test outstanding). Not yet ACCEPT.**

## Running tally
- A: ACCEPT-as-human-review-ready (bounded-descriptive, NOT a detection).
- B: in-progress (needs like-for-like M* + systematic budget).
- C (MZR/FMR aperture): not yet started.
- DR (t_3fbb9efe): running at Tori; results pending → fold into A external context + B systematics when they land.

## Phase P3 (01:21 KST) · Paper B (TNG SMF) · RESOLVED
- Real cited data: TNG100 n(>10^10.5)=1.11e-5 (z5), 7.4e-7 (z6); obs Weibel+2024 z~5-6=3e-5, Labbe+2023 z~7-9 candidates=1e-5.
- Like-for-like systematic-budget test: Weibel z~5-6 excess (2.7x) ERASED by 0.28 dex M* shift (within ~0.3 budget) -> consistent within systematics. Labbe z~7-9 (13.6x) borderline (0.44 dex) AND rests on unconfirmed photometric candidate masses.
- Conclusion: the "too massive too early" tension is NOT robust to the M* systematic budget.
- astrosage gate audit: G1 PASS · G2 PASS (non-circular by construction) · Defensibility PASS · G6 PASS.
- **VERDICT: B → ACCEPT-as-human-review-ready.** A defensible sim-vs-obs confrontation (deflates a claimed tension). Queued for human sign-off.

## Running tally (updated)
- A: ACCEPT-as-human-review-ready (z>7 bounded-descriptive deficit -0.47±0.10 dex, Te-clean, LOO-robust; NOT a detection).
- B: ACCEPT-as-human-review-ready (TNG "too-massive-too-early" tension NOT robust to M* systematics).
- C (MZR/FMR aperture): next.
- DR t_3fbb9efe: still in Gemini final-synthesis (no throttle); folds into A external-context/B systematics if it lands.

## Phase P4 (02:15 KST) · DR folded in (Tori dr1.md, dr2.md landed) — verdicts updated
### DR1 → Paper A: DOWNGRADE ACCEPT → REVISE (DR surfaced a real systematic)
- DR1 (independent z>7 anchors): genuinely independent UNLENSED field anchors now exist — Pollock+2026 (N=11, direct-Te, z~9.3-10, arXiv:2506.15779), Cullen+2025 (EXCELS-63107 z=8.27, direct-Te), Isobe+2026 (JADES stacks). Lensed samples must be QUARANTINED (differential magnification distorts M*/sSFR).
- MATERIAL ISSUE: my "clean" direct-Te subset (ERO=SMACS0723, GLASS=Abell2744) is LENS-CONTAMINATED; only CEERS is field. So the -0.47 dex deficit carries a differential-magnification systematic I did not account for.
- HONEST FIX (blocks ACCEPT): re-derive the deficit on unlensed field anchors (Pollock/Cullen/Isobe — needs a data pull), and/or add explicit lensing caveat + cite independent anchors. Not fabricating a re-derivation tonight.
- **VERDICT: A → REVISE.** Still NOT a detection; the bounded-descriptive result stands *with a lensing-systematic caveat*, but a clean unlensed re-derivation is required for human-review-ready. DR strengthened rigor by catching this.

### DR2 → Paper B: ACCEPT CONFIRMED + strengthened
- DR2 (M* systematic budget): literature finds M* systematics FAR larger than my conservative 0.3 dex — SED-code spread ~1 dex on identical photometry (indistinguishable chi^2); top-heavy IMF alone -1.0 dex; AGN/LRD contamination drops host M* by orders of magnitude; Eddington-bias correction -> epsilon 0.2-0.4 (LCDM-consistent). 68 citations, 55 sources.
- => Paper B's "tension not robust to M* systematics" conclusion is well-supported (my 0.28 dex erasure threshold is comfortably within the real budget). Add residual caveat: spectroscopic QUIESCENT galaxies (RUBIES-UDS-QG-z7, ~2 dex excess) are a distinct, harder case not dismissed by these systematics.
- **VERDICT: B → ACCEPT-as-human-review-ready (CONFIRMED, DR-strengthened).**

### Paper C (MZR/FMR aperture): waiting on DR3
- No local aperture-vs-integrated / IFU cross-calibration data. DR3 (aperture/covering-fraction across calibrations; resolved-vs-integrated MZR offsets) is exactly what C needs and is still cooling down at Tori. C = BLOCKED-ON-DR3 (do not fabricate). Gate-audit framing only.

## Running tally (updated after DR)
- A: REVISE (z>7 bounded-descriptive deficit stands with lensing caveat; needs unlensed-field re-derivation. NOT a detection.)
- B: ACCEPT-as-human-review-ready (tension not robust to M* systematics; DR-confirmed).
- C: blocked on DR3 (aperture data).
- DR t_3fbb9efe: dr1+dr2 done; dr3 pending.

## Phase P5 (03:08 KST)
- DR3 still stuck at Gemini "Starting research…" (16+ min, no quota/block error). Paper C REMAINS blocked-on-DR3 (no fabrication). Framing only.
- Paper A: no local unlensed-field data (Pollock/Cullen/Isobe) — cannot re-derive tonight. A stays REVISE; wrote A_revise_note.md (lensing caveat + re-derivation plan + independent-anchor cites).
- Paper B: wrote human-review-ready abstract (B_abstract.md) stating like-for-like M*, the 0.28 dex erasure threshold, the DR2 ~1 dex budget, and the quiescent-galaxy residual caveat. B remains ACCEPT.

## Phase P6 (04:01 KST) · DR3 landed → Paper C adjudicated
- DR3 (dr3.md, 53KB, 94 cites): calibration-SCALE offset up to 0.7 dex (theoretical vs Te); APERTURE bias >0.15 dex below 20% covering fraction (SDSS 3" fiber; masks high-mass MZR turnover); DIG 30-60% of Halpha flattens/inverts gradients; resolved IFS (MaNGA/CALIFA/SAMI/MUSE rMZR) as independent ground truth. Framework separates ΔO/H(aperture) from the scale offset.
- astrosage gate audit: G1 PASS · G2 PASS · G3 PASS · **G4 novelty FAIL (synthesis of known systematics; no new original measurement).**
- Pre-registration: G4 FAIL -> SHELVE (astrosage's overall "ACCEPT-with-review-framing" is advisory, not a gate pass). C cannot be REVISEd into novelty without an original measurement (no local IFU/aperture data pull tonight).
- **VERDICT: C → SHELVE as a research paper.** SALVAGE PATH (human decision): reframe as an explicit methods/review contribution (the correction-framework compilation IS the contribution) — legitimate but a different genre; not auto-taken.
- Note: Tori is re-running a corrected dr2 (exact TNG/number-density plan) — will strengthen B's citations when it lands; B's numbers already came from local smf_results.json so verdict unaffected.

## SUBSTANTIVE VERDICTS SET (pending 08:00 freeze report)
- A → REVISE: z>7 bounded-descriptive deficit (-0.47±0.10 dex, direct-Te, LOO-robust) WITH lensing caveat (ERO/GLASS lensed); needs unlensed-field re-derivation (Pollock/Cullen/Isobe). NOT a detection. [A_revise_note.md]
- B → ACCEPT-as-human-review-ready: TNG "too-massive-too-early" tension NOT robust to M* systematics (0.28 dex erasure vs ~1 dex budget); quiescent-galaxy residual noted. [B_abstract.md]
- C → SHELVE (research paper); salvageable as methods/review. [C_referee.txt, dr3.md]

## Phase P7 (04:54 KST) · light polish
- Corrected dr2: not landed yet. Unlensed field-anchor data: still not local. (1)&(2) no-op.
- (3) astrosage residual-overclaim QA on B_abstract.md: OVERCLAIM CHECK PASS · LABEL CHECK PASS (descriptive/not-validated intact, no sentence exceeds evidence+budget). B ACCEPT confirmed clean. [B_overclaim_check.txt]
- No further substantive work available before freeze; verdicts locked: A REVISE, B ACCEPT, C SHELVE.

## ═══ EXTENSION (+4h) · started ~08:15 KST 2026-07-21 · freeze ~12:15 KST ═══
Same pre-registered gates + bright lines carry over. Goals:
- E1: Paper A unlensed re-derivation — pull field-anchor data (Pollock+2026 arXiv:2506.15779 z~9.3-10 direct-Te; Cullen+2025 EXCELS-63107; Isobe+2026), re-derive deficit on the UNLENSED direct-Te sample, astrosage re-referee. If data unpullable, queue a data trip to Tori + keep A REVISE.
- E2: Paper B full AASTeX draft from B_abstract.md + analysis; compile PDF (tectonic) as a reviewable deliverable.
- E3 (time permitting): gate-audit ONE new contested frontier (e.g. LyC escape f_esc / cosmic SFRD) — pre-register, do not fabricate.

## Extension E1 (08:15 KST) · Paper A UPGRADED via unlensed data pull
- Pulled Pollock+2026 (arXiv:2506.15779) Table 2 via ar5iv: N=7 direct-Te; kept N=5 strictly unlensed FIELD (CAPERS-EGS/UDS + JADES-GN/GS, z=9.27-9.94, logM=8.19-8.59). Excluded RXJ2129 (lensed cluster) + JADES-GN-55757 (OH upper limit). [data/pollock2026_unlensed_directTe.csv]
- RE-DERIVED deficit vs Curti+2020 local MZR: -0.69 +/- 0.03 dex; leave-one-out spread only 0.04 dex (very robust). INDEPENDENT of the original Nakajima+23 ERO/GLASS/CEERS (-0.47). So the deficit is now confirmed on TWO independent samples, and lensing systematic REMOVED.
- HONEST framing: the tiny formal sigma (~22) OVERSTATES confidence; dominant uncertainty is SYSTEMATIC (Curti+2020 extrapolated below its SDSS mass range to logM~8.3; absolute Te scale). => a robust, independent, UNLENSED metallicity deficit vs the local-MZR extrapolation — NOT a formal statistical detection; magnitude is scale/extrapolation-dependent.
- astrosage re-referee: G2 PASS (independent unlensed), G3 PASS, G6 PASS, overclaim managed (22sigma not used as detection). [A_upgraded_referee.txt]
- **VERDICT: A → ACCEPT-as-human-review-ready** (bounded, independent, unlensed, systematic-limited; NOT a detection). Upgraded from REVISE.

## Running tally (extension)
- A: ACCEPT-as-human-review-ready (UPGRADED — independent unlensed deficit -0.69 dex, systematic-limited, not a detection).
- B: ACCEPT-as-human-review-ready.
- C: SHELVE (research paper); salvageable as review.

## Extension E2 (09:32 KST) · Paper B full manuscript + PDF
- Wrote full AASTeX (aastex631) Letter from B_abstract.md + the analysis + DR2 systematic-budget consensus; self-contained bibliography (Curti+2020, Labbé+2023, Nelson/TNG, Weibel+2024).
- Compiled with tectonic → paperB/paperB.pdf (2 pp, 54 KB). Reviewable deliverable for the ACCEPT paper.
- Honest label retained throughout ("descriptive, machine-generated draft — not a validated measurement").

## Extension next (E3)
- Build Paper A manuscript + PDF (UPGRADED unlensed version: independent Pollock+2026 deficit -0.69 dex, systematic-limited, NOT a detection). A is now the strongest result — worth a compiled draft.
- Time permitting: gate-audit ONE new contested frontier (LyC escape f_esc / cosmic SFRD) with full pre-registration; do not fabricate.

## Extension E3 (10:24 KST) · Paper A manuscript+PDF + robustness
- Wrote + compiled Paper A upgraded (unlensed) AASTeX Letter → paperA/paperA.pdf (56 KB). Frames: Nakajima -0.47 (lens-caveated) + Pollock unlensed -0.69±0.03 (LOO-robust); explicitly NOT a formal detection (systematic-limited). Both ACCEPT papers now have compiled PDFs.
- Robustness (3rd independent anchor): Cullen+2025 EXCELS-63107 (unlensed field, direct-Te, z=8.27) deficit = -1.50 dex. HONEST NOTE: this is a single EXTREME metal-poor EMPG — it CONFIRMS the sign on a third independent object but its magnitude is an outlier; NOT folded into the population estimate (Pollock -0.69 remains representative). Sign now confirmed across 3 independent samples; magnitude stays scale/extrapolation-limited.
- New-frontier paper (f_esc / SFRD): DEFERRED. A publishable one needs a real measurement on real data; a rushed corpus-only version would SHELVE on novelty (cf. Paper C). Not fabricating one to pad the count.

## Extension tally (substantive work complete)
- A: ACCEPT-as-human-review-ready + PDF (independent unlensed deficit -0.69 dex, sign confirmed 3x, systematic-limited, NOT a detection). [paperA/paperA.pdf]
- B: ACCEPT-as-human-review-ready + PDF (TNG tension not robust to M* systematics). [paperB/paperB.pdf]
- C: SHELVE (research paper); salvageable as review.
- 0 validated (human sign-off pending).

## ═══ EXTENSION-2 (+2h) · started ~12:17 KST · freeze ~14:15 KST ═══
Goal: HARDEN Paper A's #1 caveat — re-anchor the z>7 deficit on a local direct-Te MZR MEASURED at low
mass (Andrews & Martini 2013) instead of the Curti+2020 extrapolation. Quantify the anchor systematic.
Same gates/bright lines. (E5 optional: C review-reframe compile, time permitting.)

## Extension-2 E4 (12:20 KST) · Paper A HARDENED — anchor-robustness
- Re-anchored the Pollock unlensed deficit on Andrews&Martini2013 (direct-Te local MZR MEASURED down to logM~7.4, NOT extrapolated): -0.645 dex, vs -0.687 against Curti+2020 extrapolation. ANCHOR SYSTEMATIC = 0.042 dex.
- => A's #1 caveat (local-MZR extrapolation below SDSS mass range) is RESOLVED: the deficit is robust to the local-anchor choice. Two of three leading systematics (lensing, extrapolation) now controlled; dominant remaining = absolute Te scale (~0.1-0.2 dex) + small N.
- Updated + recompiled paperA/paperA.pdf with the AM13 re-anchoring. astrosage ACCEPT stands (this only strengthens; still explicitly NOT a detection).
- A remains ACCEPT-as-human-review-ready, now hardened.

## Extension-2 E5 (12:41 KST) · Paper C SALVAGED as a review
- Reframed C as an explicit methods/REVIEW (calibration-scale + aperture + DIG framework, grounded in DR3's 94 citations), compiled → paperC/paperC.pdf (56 KB). Explicitly labels itself a synthesis, not a new result.
- astrosage under review-framing: REVIEW-CLEARS YES · HONEST-LABEL PASS. [C_review_referee.txt]
- => C upgraded from SHELVE(research paper) to review-cleared methods contribution (human decides whether to run the review genre).

## Extension-2 tally (substantive work complete)
- A: ACCEPT + PDF, HARDENED (unlensed -0.69 dex; anchor-robust, extrapolation caveat resolved 0.04 dex; Te-scale + N the only remaining limit; NOT a detection). [paperA/paperA.pdf]
- B: ACCEPT + PDF (TNG tension not robust to M* systematics). [paperB/paperB.pdf]
- C: REVIEW-CLEARED + PDF (methods/review; was SHELVE-as-research). [paperC/paperC.pdf]
- 0 validated (human sign-off pending). Three compiled manuscripts.

## Extension-2 E6 (12:50 KST) · Paper A FURTHER hardened — cross-method + large-N confirmation
- Grew unlensed direct-Te sample from local data: only +1 (CEERS_01027; direct-Te at z>7 is intrinsically rare). N=6 individual → deficit -0.67 (Curti)/-0.63 (AM13), LOO spread 0.049.
- Pulled Isobe+2026 (arXiv:2606.11345): STACKED-Te MZR from ~1500 unlensed JADES spectra, z=4-10, Z8=7.62±0.10 at logM=8, slope 0.34 (~unchanged from z~0). Deficit = -0.61 (Curti) / -0.50 (AM13).
- => deficit now confirmed by TWO methodologies (individual direct-Te + stacked-Te) and N=5 → ~1500; the small-N caveat is largely RESOLVED. It is a NORMALIZATION deficit (~0.5-0.6 dex) at unchanged slope.
- Updated + recompiled paperA/paperA.pdf. Remaining caveat narrowed to the absolute Te scale (~0.1-0.2 dex). Still explicitly NOT a formal detection. A remains ACCEPT, substantially hardened.
- saved data/unlensed_combined_directTe.csv

## Extension-2 E6b (12:52 KST) · overclaim QA + fix on hardened A
- astrosage flagged one over-reach: asserting a z~9-10 "normalization deficit" from Isobe+2026 (whose stack spans z=4-10). Detection-discipline PASS (no detection claim).
- FIXED: softened to attribute the slope-vs-normalization finding to Isobe's z=4-10 stack ("consistent with", not established at z~9-10); explicitly caution the z>7 MZR slope remains weakly constrained. Recompiled paperA/paperA.pdf. [A_hardened_qa.txt]
- A remains ACCEPT-as-human-review-ready; claims now match the evidence tier.

## Extension-2 E6c (12:55 KST) · Isobe claim made bare-factual (referee over-conservative, stopped the loop)
- After 2 fixes, astrosage kept flagging an already-bounded statement (over-conservative repetition). Per bright line "astrosage advisory, not a gate", I did NOT delete the real result; reduced Isobe to a bare factual statement (reports 12+log(O/H)=7.62 at logM=8 over z=4-10 = -0.5 to -0.6 dex deficit; z~9-10-specific value rests on Pollock). No inference beyond the data. Recompiled. Human review is the arbiter. [A_hardened_qa2.txt]
- Detection-discipline held throughout (PASS). A remains ACCEPT, honestly bounded.

## Extension-2 E7 (12:56 KST) · figures added
- Paper A: MZR-deficit figure (paperA_fig.pdf) — local MZR curves + Pollock unlensed points + Isobe stack + deficit band. Embedded, recompiled.
- Paper B: number-density figure (paperB_fig.pdf) — TNG vs Weibel/Labbé + the 0.28 dex erasure arrow. Embedded, recompiled.
- Both manuscripts now have their key result visualized.

## Extension-2 E8 (13:40 KST) · Paper A Te-scale sensitivity (honest significance)
- Monte Carlo (N=20000): shift all O/H by a common N(0,0.15 dex) Te-scale systematic. Central deficit -0.687 dex.
- Result: sign persists ~100%; P(>0.3 dex)=99.6%; P(>0.5 dex)=89.3%. Effective significance = |base|/sqrt(0.032^2+0.15^2) = ~4.5 sigma (NOT the formal ~22).
- => quantifies the honest confidence: a robust ~4.5-sigma metallicity deficit whose SIGN is secure and whose MAGNITUDE (0.3-0.5+ dex) is Te-scale-limited. Added to paperA.tex Discussion; recompiled. A remains ACCEPT, now with a properly-quantified significance floor (replaces the hand-wavy "systematic-limited").

## CONTINUATION (2026-07-22, migrated) · see continuation-20260722/
9 DR-independent rigor cycles (00:15-04:34 KST 2026-07-22), done in scratch during the Kun-report
reconciliation, now migrated here. Highlights:
- Paper A: formal error budget (-0.68+/-0.16 dex, Te-scale dominant); N=5->6 via GN-z11 (sign confirmed z=10.6);
  inverse-variance-weighted -0.684+/-0.032, no mass/z trend (normalization-offset claim validated);
  dominant caveat = irreducible absolute-Te zero-point (grounded vs Kewley&Ellison 2008).
- Paper B: COMPLETE — erasure-sensitivity grid (no robust number-count tension across excess x slope);
  quiescent-galaxy residual bounded as statistics-of-one (n~3e-6 Mpc^-3, Poisson+CV ~0.5-0.7 dex).
- Paper C: headline 0.7 dex calibration offset verified (Kewley&Ellison 2008).
- Drop-in LaTeX tables ready (continuation-20260722/*.tex); manuscripts NOT yet edited/recompiled.
See continuation-20260722/SCRATCH_LEDGER.md (full log) and RUN_CONTINUATION_REPORT.md (summary).

## INTEGRATION (2026-07-22) · tables inserted into manuscripts + recompiled
- Paper A: inserted Table 1 (systematic error budget) + a paragraph (inverse-variance-weighted -0.68+/-0.03,
  no mass/z trend -> normalization offset, GN-z11 z=10.6 sign confirmation, effective ~4sigma, total +/-0.16 dex);
  added Curti+2023 (arXiv:2304.08516) bibitem for GN-z11. Recompiled -> paperA.pdf (3 pp). Table ref + citation resolved.
- Paper B: inserted Table 1 (erasure-sensitivity grid: excess 2-20x vs SMF slope -1.4..-2.0; all <=1 dex budget;
  only a ~2 dex excess exceeds). Recompiled -> paperB.pdf (2 pp). Table ref resolved.
- Honest framing preserved (both still "descriptive, not validated"). Source backups: paper[AB].tex.bak-pre-tables.
- NOT re-refereed (additive consolidation of already-accepted results); astrosage re-review optional.
- Live-site PDFs NOT changed (they are separate copies in frontend/public); run-dir PDFs updated only.

## REFEREE (2026-07-22) · astrosage-70b on changed sections
- Paper A error-budget section: REVISE -> (removed detection-adjacent "~4sigma effective significance" sentence) -> ACCEPT-as-human-review-ready.
- Paper B erasure-grid section: ACCEPT-as-human-review-ready (first pass).
Both recompiled; framing still descriptive/not-validated. [continuation-20260722/INTEGRATION_REFEREE.txt]
