# VERDICT MEMO — z>7 MZR v2 detection run (finalization)

**Prepared:** 2026-07-20 16:23 KST · **Run:** overnight-z7-mzr-v2-detection-20260720 (Pick #1)
**Authoritative inputs:** DETECTION_VERDICT.md (Goru ruling), PHASE_B_RESULTS.md + detection_results.json (numbers),
CALIBRATION_AND_RULE.md, DATA_ACQUISITION.md, DETECTION_PREREG.md. Base manuscript evolved from
`../overnight-z7-mzr-20260720/draft.tex`.

## Status — the final honest label (per Goru §2; used verbatim in title/abstract)
> **Selection-robust, multi-calibration z>7 MZR deficit — a mass-controlled 12+log(O/H) shortfall of ~0.45–0.55 dex
> (Nakajima+23, N=16) that survives two independent local calibrations (KE08 and the Te-anchored Curti+2020) and
> does NOT collapse but GROWS to ~0.68–0.78 dex in an orthogonally-selected lensed subsample — breaking the
> selection↔evolution degeneracy and giving strong evidence for genuine early chemical evolution; but the
> second-survey and orthogonal axes both rest on the SAME 4 lensed galaxies (Heintz's CEERS objects duplicate
> Nakajima's; Curti+24 unreachable per-object), so this is confirmation on a single small (N=4) orthogonal anchor,
> NOT a fully independent detection — pending a larger, independent orthogonally-selected sample.**

The words "detection" / "validated" / "measurement of evolution" are **barred** until the N=4 / S≡O collapse is retired.
The prereg boolean fired truth-table cell #1 mechanically (PASS_S=2, PASS_C=2, PASS_O=TRUE), but only because one N=4
lensed anchor was counted on both the 2nd-survey axis (S) and the orthogonal axis (O); it is **not claimed**.

## What advanced vs the prior run
| Axis | Prior run (overnight-z7-mzr-20260720) | This run (v2) |
|---|---|---|
| Surveys | Single-survey (Nakajima+23, N=16) | Nakajima+23 **plus** a 2nd reduction (Heintz+23); same-sign offset — but only the 4 lensed objects are Nakajima-independent |
| Calibration | Single transfer (KE08); signal "leaned on strong-line transfer" | **Two independent transfers** — KE08 **and** the fully Te-anchored Curti+2020 (C2≥C1 on every cell) → calibration-lean broken |
| Selection | Forward-modelled bound only (Δ_sel≈0.10 dex); selection-**bounded** | **Empirically orthogonal**: lensed/continuum subsample where the deficit **grows** (0.68/0.78 dex) → selection↔evolution degeneracy **broken** |
| Label | Selection-**bounded**, descriptive | Selection-**robust**, multi-calibration, orthogonal-**confirmed** (on N=4) |

Net: a genuine, publishable step beyond a selection-bounded upper limit — and short of a validated detection by exactly
one thing.

## Key numbers (all trace to detection_results.json / PHASE_B_RESULTS.md; every one carries its in-sentence caveat)
- Nakajima+23 × KE08: Δ=+0.452, boot95 [+0.270,+0.641], LOO [+0.431,+0.484], N=16.
- Nakajima+23 × Curti+2020: Δ=+0.551, [+0.378,+0.724], LOO [+0.528,+0.582], N=16.
- Orthogonal lensed × KE08: Δ=+0.679, [+0.335,+1.002], LOO floor +0.595, N=4 (metal-poor lensed dwarfs; = the 2nd survey).
- Orthogonal lensed × Curti+2020: Δ=+0.784, [+0.477,+1.075], LOO floor +0.715, N=4 (same 4 galaxies).
- Pooled indep (N=20): +0.497 [+0.333,+0.667] (KE08) / +0.598 [+0.443,+0.752] (Curti+2020).
- Direct-Te corroboration (N=4): Δ=+0.336 [+0.031,+0.644] — barely excludes 0, more selection-biased channel → corroboration only.
- Non-independent sensitivity (full Heintz N=13, CEERS-only N=9): Δ≈+0.68/+0.78, same direction — NOT confirmation.

## Referee verdict: **MINOR revision**
Data are sound; the central novel claim (selection-robust deficit confirmed on an orthogonal subsample) is already
supported by the on-disk numbers. Only the label was overclaimed. Three non-negotiable conditions, all now met in draft.tex:
- **C1** — "validated detection" / "Upper Bound" struck; retitled to the §2 label; cell #1 demoted to the honest refinement.
- **C2** — every headline number carries the N=4 / S≡O caveat in the **same sentence** (abstract, results, figure, table, conclusion, caveats).
- **C3** — N=4 fragility reported honestly (bootstrap + LOO floors, intrinsically metal-poor lensed dwarfs, Curti+24
  unreachable per-object → emission-line side effectively single-survey; full/CEERS Heintz kept as non-independent sensitivity).

## The ONE decisive next step
Pull a **second, larger (N≳15), independently-selected orthogonal sample** — lensed-cluster or deep continuum/dropout
z>7 galaxies with O-based O/H in [8.0,9.5] from fields **not** in Nakajima+23 (e.g. additional Heintz cluster fields,
UNCOVER/Abell-2744, GLASS/A2744 continuum, or a JADES deep-continuum cut with per-object O/H). If its orthogonal-deficit
CI still excludes 0, axes S and O separate, the double-count dissolves, and cell #1 ("validated detection") fires honestly.
This single addition is make-or-break; nothing else is.

## Deliverables
- `draft.tex` → `draft.pdf` compiled with tectonic: **5 pages, figure `fig_detection.png` embedded** (forest plot of per-cell Δ + CIs).
- Title: *"A Selection-Robust Mass–Metallicity Deficit at z>7: Confirmation on an Orthogonally-Selected Lensed Subsample."*

## Honest one-liner
A mass-controlled z>7 O/H deficit of ~0.45–0.55 dex (Nakajima+23) that survives a fully Te-independent calibration and
**grows to ~0.68–0.78 dex under orthogonal, lens-based selection** — strong evidence for genuine early chemical evolution
that emission-line selection cannot explain away; but its independent-survey and orthogonal axes are the **same 4 lensed
galaxies**, so it is confirmation on one small anchor, not yet a fully independent detection.
