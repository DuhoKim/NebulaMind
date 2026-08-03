# DETECTION_PREREG — the z>7 MZR detection gate (anti-overclaim contract)

**Run:** overnight-z7-mzr-v2-detection-20260720 (Pick #1) · **Author:** Goru (skeptic/gate) · **Locked:** 2026-07-20 15:58 KST
**Status of prior run:** DESCRIPTIVE — bounded, selection-robust deficit Δ = 0.45 dex (selection-corrected 0.25–0.41, central ~0.35),
bootstrap 95% CI [0.28, 0.62] excludes 0, single-survey (Nakajima+23, N=16), 7/7 systematics PASS-in-the-bounded-sense.
**Purpose:** Fix the exact label the result MUST carry for every combination of the three upgrade axes, BEFORE any new number
exists, so the pipeline cannot narrate its way from "descriptive" to "detection". Declared here → cannot be reverse-fit.

This gate SITS ON TOP OF the prior 7-test systematics scorecard (PREREGISTRATION.md). Those tests decide whether a survey/
subsample *counts at all*; this truth table decides what the assembled evidence may be *called*.

---

## The three axes (all evaluated on the mass-matched, calibration-reconciled deficit)

- **S — independent surveys** in which the mass-controlled deficit's sign + bootstrap 95% CI-excludes-0 SURVIVES, computed per-survey:
  - `S1` = 1 survey (Nakajima+23 only) · `S2` = ≥2 independent surveys (e.g. + Curti+24 / Heintz+23).
- **C — independent calibration transfers** the deficit SURVIVES under:
  - `C1` = 1 surviving transfer · `C2` = ≥2 independent surviving transfers (KE08 T04→PP04-O3N2 AND a 2nd Te-independent path).
  - The deficit is reported as the INTERSECTION of transfers. Te-direct is NOT an independent transfer here: it is itself
    the more selection-biased channel (RECONCILIATION.md) and, corrected, its CI can include 0 — it corroborates, it does not confirm.
- **O — orthogonally-selected subsample** (lensed / deep-continuum, i.e. NOT emission-line- or UV-line-selected):
  - `O0` = absent (none pulled, or pulled but deficit does not survive) · `O1` = present AND deficit survives in it (CI excludes 0).

A level is only reached if the prior-run 7 systematics (below) PASS for the samples that earn it. Failing those = not counted.

---

## THE GATE — explicit truth table (8 cells, one mandatory label each)

Read as (S, C, O). Only the all-pass cell may say "detection". Every other cell names a specific bounded/descriptive flavor.

| # | S | C | O | MANDATORY LABEL (title / abstract / verdict must use this, no synonym-upgrade) |
|---|---|---|---|---|
| 1 | ≥2 | ≥2 | present+survives | **VALIDATED DETECTION of z>7 MZR evolution below the extrapolated local relation.** *(the ONLY detection cell)* |
| 2 | ≥2 | ≥2 | absent | **Multi-survey, multi-calibration SELECTION-BOUNDED result.** Robust to survey & calibration, but the selection↔evolution degeneracy is NOT broken. NOT a detection. *(the ceiling if no orthogonal sample is pulled)* |
| 3 | ≥2 | 1 | present+survives | **Multi-survey, selection-broken, CALIBRATION-LIMITED deficit.** Residual leans on a single surviving transfer. Descriptive. |
| 4 | 1 | ≥2 | present+survives | **Single-survey, multi-calibration, selection-broken deficit.** Could still be a Nakajima+23-specific artifact. Descriptive. |
| 5 | ≥2 | 1 | absent | **Multi-survey, CALIBRATION- and SELECTION-BOUNDED descriptive deficit.** Descriptive. |
| 6 | 1 | ≥2 | absent | **Single-survey, SELECTION-BOUNDED, calibration-robust descriptive deficit.** Descriptive. |
| 7 | 1 | 1 | present+survives | **Single-survey, calibration-limited, selection-broken descriptive deficit.** Descriptive. |
| 8 | 1 | 1 | absent | **Single-survey, single-calibration, SELECTION-BOUNDED descriptive deficit.** = the PRIOR-RUN result (baseline; no upgrade). |

**Collapse rule (overrides the table):** if on the matched scale the deficit VANISHES into the residual calibration band
(|Δ| − σ_cal,resid ≤ 0) or its bootstrap CI includes 0 in the survey/cell being assessed, that cell is not "descriptive deficit"
but **NULL — consistent with no z>7 MZR evolution within systematics**, and that null IS the honest reported result.

---

## Still-required systematics (carried over from the 7-test scorecard — a new survey/subsample must PASS all to count)

Each NEW survey or orthogonal subsample, before it may advance an axis (S1→S2, C1→C2, O0→O1), MUST independently pass:
1. **Mass-match** — deficit evaluated ONLY inside the SDSS↔sample stellar-mass overlap **[8.0, 9.5]**; report N in that interval. No extrapolation of the SDSS MZR as evidence.
2. **Small-N robustness** — bootstrap ≥10^4 resamples, **95% CI excludes 0**, AND leave-one-out (LOO) keeps the CI excluding 0 (not one-object-driven).
3. **O-based diagnostics only** — primary O/H from O-based (Te-direct / R23 / O3) diagnostics; N-based (N2/O3N2) discarded in any plausibly N/O-enhanced object. No N-based diagnostic may carry a cell.
4. **Per-survey calibration reconciliation** — the survey put on the SAME matched scale as the SDSS anchor (mass-DEPENDENT reconciliation) BEFORE differencing. Cross-scale subtraction without an explicit conversion term is forbidden.

A survey/subsample that FAILS any of the four **does not count** toward "≥2 surveys", "≥2 calibrations", or "present-and-surviving".
It may be reported as an unconfirmed addition, never as an axis upgrade.

---

## Honesty guardrail (governs the write-up)

- **Same-sentence systematic.** Wherever the deficit is stated, the *limiting* systematic for that cell is quantified in the SAME sentence
  (e.g. "…0.25–0.41 dex; selection accounts for ~10–45%, ≥55% residual" / "…leaning on the single KE08 transfer"). No headline number floats free of its dominant caveat.
- **"Detection" is a locked word.** It may appear only if the bootstrap CI excludes 0 in **EVERY required cell** — i.e. only cell #1
  (≥2 surveys × ≥2 calibrations × orthogonal-present-and-surviving), with all four systematics passed by every contributing sample. In all other cells the words "detection", "measurement of evolution", and "validated" are forbidden in title, abstract, and verdict.
- **Ceiling without an orthogonal sample.** If the orthogonal (lensed / deep-continuum) subsample is absent — including the concrete
  case where no lensed data can be pulled — the MAXIMUM admissible claim is **"multi-survey, multi-calibration selection-bounded result"** (cell #2). It is NOT a detection no matter how many surveys or calibrations pass, because the selection↔evolution degeneracy remains unbroken.
- **The single make-or-break condition.** The one thing that, if it fails, keeps the result descriptive regardless of everything else is the
  **orthogonally-selected (lensed / deep-continuum) subsample surviving with its CI excluding 0 (axis O0→O1).** Emission-line/UV selection is common-mode across Nakajima+23, Curti+24, and Heintz+23; adding more of the same selection cannot break the degeneracy. Only an orthogonally-selected sample can, so O1 is the load-bearing axis for the word "detection".
- **No-fabrication clause.** If a sample cannot be pulled, SAY SO; the rule holds and the label falls to whatever cell the real data occupy. Every reported number carries a bootstrap CI. Both a surviving deficit and a vanishing null are admissible outcomes.
