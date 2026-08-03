# Cycle 4 — Kun: FINAL PORTFOLIO GATE (adversarial)

**GATE 1 (Goru selection forward-model): PASSES AS A BOUNDING/ENVELOPE EXERCISE, NOT AS A POINT ESTIMATE.** Script reproduces the writeup to the digit; the #6 direction is correct and robust (de-biasing obs DOWN widens the TNG gap in all 9 grid configs — sign confirmed); #3's z<6 SFR-evolution claim is not merely "reframe" but must be DROPPED (lower envelope reaches ~0 = pure artifact not excluded); z>6 residual + MZR survive.

**GATE 2 (#4 written passages vs E1–E7): SATISFIED for E1–E5, HONESTLY DEFERRED for E6–E7.** z7–9 demotion is unambiguous ("outside the realistic budget and marginal, not consistent"); the ε=0.20 TNG-calibration-not-ΛCDM reframe is carried into BOTH abstract and conclusion; every shipped number traces to Kun-cycle2 corrected values (no unexplained drift). Remaining real blocker: E6 TNG mass-aperture basis is still unmatched.

---

## GATE 1 — did I trust it? No. What I re-ran / re-derived.

**Numbers match the writeup exactly.** Ran `python3 c3_goru_selection.py` (live SDSS pull, N=120k, SF-ridge σ=0.44/0.42/0.38/0.38/0.39, median 0.39 — confirms paper's σ). SENSITIVITY ENVELOPE printed:
- z≈3.5: inflation +0.63 [+0.23,+1.17]; residual +0.14 [−0.40,+0.54]
- z≈4.7: inflation +0.51 [+0.05,+1.15]; residual +0.38 [−0.26,+0.84]
- z≈5.4: inflation +0.44 [−0.02,+1.20]; residual +0.52 [−0.24,+0.98]
- z≈6.7: inflation +0.46 [+0.10,+1.20]; residual +1.48 [+0.74,+1.84]

Every cell equals the writeup table. ✓

**Is the Hβ-flux-floor truncation model defensible?** Yes, in principle — an emission-line flux floor is an SFR floor at fixed z (F(Hβ)>F_lim → L(Hα)→SFR via Kennicutt), and truncating the low-SFR tail of a scattered SFMS lifts the detected median. That is textbook Malmquist/Eddington selection on SFR, and the model behaves sensibly under stress (deeper F_lim → lower floor → less truncation → higher recovered E_true: z6.7 goes 0.72→0.24 inflation from shallow→deep; correct direction). The analytic truncated-normal cross-check (median shift = σ·q(a)) agrees bin-by-bin and shows the bias is mass-dependent (logM*≈8 shift +0.5→+0.7, logM*≈9 shift +0.1→+0.3), as claimed.

**But it OVERSTATES its own precision and the "~half is selection" central is not a measurement.** The "≈0.4–0.6 dex (≈40–60%) of the z≈3.5–5.4 elevation is selection" central is the MEDIAN OF 9 ARBITRARY GRID POINTS (σ∈{.30,.45,.60}×F_lim∈{1e-19,3e-19,1e-18}), not a posterior — it has no physical privilege. As a FRACTION, z=3.5's envelope-median inflation is 0.63/0.77 = **82%**, not "40–60%." The script's own SAMPLE-MATCHED CENTRAL swings **6%→87%** across bins (z4.7=6%, z3.5=87%) — i.e. the point estimate is unstable, exactly as the writeup concedes. **Corrected framing: quote the ENVELOPE, not the central "~half."** The writeup mostly does this and flags the degeneracy honestly, so this is a wording discipline note, not a defect.

**The envelope is if anything TOO NARROW (conservative for the disposition).** It varies only σ and F_lim. It does NOT grid the MF slope (β=0.9 fixed — a steeper faint end puts more low-mass galaxies at the floor → MORE inflation), dust (would raise the required SFR → more inflation), the selection LINE ([OIII], not Hβ, is often the real high-z selector, and [OIII]/Hβ rises at low Z), or mass-dependent E_true (assumed flat). So the TRUE uncertainty is wider than [+0.23,+1.17] etc. — which makes "pure selection not excluded below z≈6" MORE true, not less. Good: the conclusion is conservative w.r.t. the un-gridded axes.

**Direction check for #6 (load-bearing) — SIGN CONFIRMED, robust across ALL configs.** Gap = TNG_internal − obs. Selection inflates obs UP; de-biasing pulls obs DOWN; TNG internal growth (+1.30/+1.45/+1.61) is the intrinsic mass-matched value with no line floor → gap = TNG − obs GROWS. The script widens the gap in every configuration (never negative):
- central-config: z4.7 +0.41→+1.14 (widen +0.73); z5.4 +0.49→+1.19 (widen +0.70)
- sample-matched: z4.7 +0.41→+0.46 (widen +0.05); z5.4 +0.49→+0.83 (widen +0.34)

So #6 "survives and STRENGTHENS" is correct — the SFR-over-evolution discrepancy is a **lower bound w.r.t. selection**, not an artifact. **One mislabel to fix:** the writeup's "z≈4.7 gap +0.41→~+0.46 (up to +0.73 in the aggressive-selection corner)" — **+0.73 is the WIDENING amount, not the aggressive-corner gap**; the aggressive-corner GAP is **+1.14**. Cosmetic; does not touch the sign or the conclusion.

**Is #3's disposition ("reframe, keep z>6 + MZR deficit") honest, or shelve the SFR claim outright?** The z<6 SFR-evolution sub-claim specifically CANNOT be defended — residual lower envelopes are +0.14 [−0.40,…], +0.38 [−0.26,…], +0.52 [−0.24,…], all ≤0, i.e. pure selection is not excluded at any of z=3.5/4.7/5.4. So the honest call is stronger than "reframe": **DROP the z<6 SFR-evolution / "rapid early enrichment toward evolving equilibrium" claim entirely** (not soften it), keep only the z>6 residual (+1.48 [+0.74,+1.84] — survives even the max selection shift at its LOWER bound) and the independent MZR −0.4 dex deficit. And per Kun-cycle1 + project memory ("z≈0 SDSS relations are anchors, not standalone papers"), the surviving pieces feed #6/#1 — **#3 does not ship standalone.** Goru's writeup effectively does this ("not earned from the SFR sector; demote the equilibrium language") but uses the softer word "reframe"; sharpen to "drop the z<6 SFR claim."

---

## GATE 2 — #4 passages vs Kun's own E1–E7 (cycle2_kun_gate)

Independently re-verified the crux arithmetic: ε_unshifted = 10^10.5/(0.157·1.0e12) = **0.201** ✓; ε_shifted = 10^10.22/1.57e11 = **0.106** ✓; +0.70 dex to ε=1: 0.20·10^0.70 = **1.00** ✓; z5–6 shift 0.436/1.58 = **0.276≈0.28** ✓; z7–9 1.134/1.58 = **0.718≈0.72** ✓; factor 2.7 = 10^0.436 ✓.

| E | requirement | shipped in cycle3_tori JOB1 | verdict |
|---|---|---|---|
| E1 | budget as range 0.46–0.55, 1.30 = upper bound, note correlation | abstract+§3.1 adopt "0.46–0.55 dex" range, 1.30 labeled worst-case upper bound | **MET (with a resolved tension — see below)** |
| E2 | z7–9: recompute 0.72 at s=−1.58, move OUTSIDE budget, or cite s≈−2.6; label photometric | chose 0.72, "exceeds the committed 0.55 budget", "outside the realistic budget and marginal, not consistent"; §3.1 note explicitly corrects the old 0.44 | **MET, clean** |
| E3 | two falsification thresholds (<0.28; slope-dependent 0.72), Table 1 footnote | 1C states both; "clears the first with factor ~2 margin but falls short of the second" | **MET** |
| E4 | ε=0.20/0.105, +0.70 dex, HMF ≤~0.06 in ε / ≤~0.11 dex threshold, DELETE "≲0.05" | all present incl. Tinker log M_halo=11.90, ε≈0.26, threshold→+0.59; "do not claim ≲0.05" | **MET** |
| E5 | reframe z5–6 as TNG-calibration-not-ΛCDM, in abstract AND conclusion | both: abstract "not a ΛCDM stress test at all but a mismatch against TNG's specific… calibration"; conclusion opens on it | **MET** |
| E6 | name TNG stellar-mass aperture, match to SED-mass or add as budget line | 1E FLAGS as NOT satisfiable from materials — needs TNG catalog metadata | **NOT MET — honestly deferred; REAL BLOCKER** |
| E7 | in-box object count, TNG n at z=5 AND z=6 | partial: ~15–40 count folded in; exact N and z=6 value flagged as not in materials | **PARTIAL — honestly deferred** |

**GATE 2 specific answers:**
- **z7–9 demotion unambiguous?** YES. "outside the realistic budget and marginal, **not consistent**" (abstract) and "a weaker case… exceeds the committed budget… outside the realistic budget and marginal" (conclusion). Not hedged back to "consistent." ✓
- **ε=0.20 reframe in abstract AND conclusion?** YES, both. ✓
- **Any number that drifted from Goru's writeup?** Two drifts, BOTH are corrections Kun made in cycle2 and both shipped correctly:
  1. z7–9 shift: Goru-cycle2 said **0.44 dex, "within budget but marginal"**; shipped text says **0.72 dex, "outside budget."** The 0.72 is right (0.44 only follows from an unstated s≈−2.6). ✓ corrected.
  2. HMF/Tinker: **Goru-cycle2 line 66 STILL reads "Tinker shifts M_halo ≲0.05 dex (ε ≲0.03) — immaterial"** — this is the stale WRONG claim; colossus Tinker08(200m) gives log M_halo=11.90 = 0.12 dex, ε≈0.26. Shipped text uses the corrected 0.12/0.06. ✓ shipped right, but **flag Goru-cycle2 line 66 as stale** so nobody re-imports it.
- **E1 tension (surfaced, not a blocker):** Kun-cycle2's E1 said "0.55 is a lower bound and 1.30 the fully-correlated upper bound" (positive correlation raises combined uncertainty), while Kun-cycle2 hit #3 argued the opposite (treating the same SED degeneracy as 3 independent terms INFLATES the quadrature → realistic ≤0.55). Tori resolved this by adopting the **double-count reading** ("0.46–0.55 dex… strictly independent mildly inflates the quadrature") and dropping the "0.55 is a lower bound" clause. That is the HARDER-on-the-paper choice (smaller budget), and 0.28 < 0.46 still holds, so z5–6 survives it. Acceptable resolution; note it was a genuine internal contradiction in my own cycle2 gate.

---

## FINAL PORTFOLIO DISPOSITION TABLE

| # | Paper | Bar-status | Single remaining blocker | Human now, or more machine work? |
|---|-------|-----------|--------------------------|----------------------------------|
| **#1** | z9–10 unlensed MZR deficit | **SHIP-REFRAME** | Data ceiling: N=5 (6 w/ GN-z11), magnitude floored by 0.1–0.2 dex Te zero-point → systematic-limited non-detection, NOT a writing gap | **HUMAN NOW.** Reframe + N reconciliation are ship-ready (cycle2 GATE B + cycle3 JOB2). No machine hour moves the ceiling. Closest to bar. |
| **#2** | f_esc / ξion landscape | **HOLD** | No new discriminating datum — maps the ξion–SFRD envelope, doesn't narrow it | Machine/data first. Needs a genuine new high-z ξion anchor before human review adds value. Do not spend polish cycles. |
| **#3** | scaling relations z0→JWST | **REFRAME (not standalone; fold into #6/#1)** | z<6 SFR-elevation is selection-degenerate to ~0 (must be DROPPED, not softened); collapsing the envelope needs the actual per-catalog (Nakajima/Lisiecki) lowest-detected SFR per bin | Machine first (real detection floors), then a human should ratify the fold/drop decision. Keep z>6 residual (~1.3–1.5 dex, survives) + MZR −0.4 dex. |
| **#4** | TNG massive-galaxy abundance | **CLEARS-WITH-EDITS** | E6 — TNG100-1 stellar-mass APERTURE (total-subhalo vs 2R½) is unmatched to the SED-mass basis; the entire downward budget currently rides on an unmatched mass definition | One machine step first (read TNG catalog aperture; E7's in-box N + z=6 n), THEN human. Prose (E1–E5) is ship-ready and gate-clean. |
| **#5** | MZR aperture/calibration framework | **SHELVE** | No original result — structurally cannot clear the non-circular-*result* axis | Neither. Keep only as a methods/review companion; never resubmit as a frontier paper. |
| **#6** | TNG calibration ≠ validation | **REFRAME (upgraded — result HARDENED)** | Mass-aperture matching (same TNG 2R½ vs SED-mass issue as #4/E6), orthogonal to selection; and its obs anchor must adopt #3's selection-de-biased (downward) SFMS | Machine first (aperture match + fold in de-biased obs). GATE 1 promotes this: the SFR-over-evolution gap SURVIVES and WIDENS under de-biasing — retain it as a **lower bound**, not an artifact. |

### Honest gate closing
- **Two papers a human should read now:** #1 (ship the reframe) and #4 (prose clears — but do not stamp "done" until E6's mass-aperture is matched; that is the one thing standing between CLEARS-WITH-EDITS and a real overclaim).
- **The single highest-value machine step remaining** is the same one that resolves BOTH #4 and #6: pin the TNG stellar-mass aperture and match it to the SED-mass basis (E6 / #6 mass-definition caveat). It is orthogonal to selection and currently un-done in every draft.
- **GATE 1's real service** is asymmetric: it does NOT rescue #3's z<6 story (drop it) and it HARDENS #6 (SFR gap is a selection lower bound). Anyone reading Goru's "reframe #3" as "keep the elevation with caveats" is reading it too softly — the z<6 SFR-evolution claim is not defensible and should be removed.
- **Nothing here is validated.** #1 and #4 are the honest ship/near-ship; #6 is a hardened-but-unwritten result; #3 folds; #2 holds; #5 shelves. Truth over polish: the portfolio is one aperture-lookup away from #4 being genuinely clean and #6 being writeable.
