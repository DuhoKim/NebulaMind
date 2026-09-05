# DRAFT — NOT ORDERED — R3-G pre-registration: does the Smoller–Temple shock-wave cosmology fix the present shock position, or does its free start epoch span every value?

**Status:** DRAFT, written under Duho's 2026-09-05 18:56 KST grant ("take the unstarted round-3 preregs — drafting is not
starting"). Round-3 ranked packet cluster **#10** (agy and codex proposed independently; CONT 3, TRACT 4, score 12, 1 seat-day
as costed by agy, 2 by codex). Not blocked. Nothing runs on this document. No tier, warrant token, standing or stamp moves.
Paper HOLD. Nothing outward. Published peer-reviewed sources only. Nothing from Hwao's lane, pipeline or data.

**Version:** DRAFT 1. A freeze produces `R3G_SMOLLER_TEMPLE_SHOCK_MAGNITUDE_PREREG_2026MMDD.md` with §8 filled, C0 by two seats
and a two-seat design gate before any derivation.

## 1. Question

Entries 36–38 and 57 (Smoller & Temple; warrant `W_MIXED`: derived background, asserted link to cosmology) are theorem-grade GR
constructions with no stated falsifier. Entry 36 (the 2000 shock-wave paper) is the one that prints a **number**: it states that
the position of the shock at present time is "a new length scale that is derived from the model, and this length scale is not
determined by any adjustable parameters in the problem other than the experimentally determined values of the Hubble constant
and the background radiation temperature" (SOURCE lines 96–104), and prints (SOURCE lines 155–214, eq. 7.31 and the worked
example):

- (S1) `(2.62×10⁻⁷) T0⁴/(h0² H0²) · ln²(1/R*) ≤ r² − r*² ≤ (2.65×10⁻⁷) T0⁴/(h0² H0²) · ln²(1/R*)` — the squared distance the
  shock travels beyond free fall, as a function of the **start epoch `R*`**, with `r` in Hubble lengths;
- (S2) the worked value `r² − r*² ≈ 0.019² H0⁻²` for `T0 = 2.7 K, h0 = 0.55, R* = 2.7/4000`;
- (S3) upper and lower bounds on the present shock position `r` as functions of `T0, H0, R*` (eqs. 7.37–7.38, SOURCE lines
  225–233, 3563–3591), plotted for `T0 = 2.7 K, h0 = 0.55`;
- (S4) the pure-radiation comparison `36h0/H0 ≤ r ≤ 36h0 √(1 + 2.5R*)/H0` (eq. 8.7, SOURCE lines 285–299), "significantly beyond
  the Hubble length".

The same page calls `R*` "the earliest time at which the shock-wave solution has settled down to the point where our model
applies" — a free datum the warrant audit already records (SOURCE lines 160–167). The corpus pattern from K3s3/K5/K6 and
R3A/R3D is: the construction fixes a *shape* and leaves free the *magnitude* a measurement would test. The question:

> **Once `R*` ranges over its admissible interval, does the present shock position in Hubble lengths stay inside a range the
> construction fixes (a magnitude), or does `R*` span every value (a shape)? And do `H0` and `T0` enter as inputs whose
> restatement is being called a prediction?**

Plainly: the paper says its shock sits a fixed distance away, given today's expansion rate and microwave temperature. Is that
distance fixed, or does a knob the paper admits it cannot set move it anywhere?

## 2. Sources and pins

| role | file | sha256 | lines |
|---|---|---|---|
| entry 36, version of record text | `../bhu-reading-20260823/sources/smoller_temple_2000_clean.txt` | `13d07d24a6d4877a15f288c0e5c622e53fb7eb9e0290a9bab43b4a6709b33d03` | 3797 |
| entry 37/38 foundation (1997 Oppenheimer–Snyder shock) | `../bhu-reading-20260823/sources/smoller_temple_1997_clean.txt` | `37d2869df53ec3b372f679bc5cb47257d015fcfef94b0bdacae271a05df2a848` | 4305 |

Inputs the seat may use: the 2000 paper's printed equations (7.31, 7.35–7.38, 8.7 and the relations feeding them), its printed
constants (`σ̄ ≈ 0.1231`, the `T0⁴` coefficients), STANDARD constants, and the paper's own stated admissible interval for `R*`
(`2.7/4000 ≤ R* < 1` as printed; the seat records the exact printed statement). No value the paper does not print.

## 3. Procedure (1 seat-day; every symbolic operation through the committed 120 s wrapper)

Limb A — **reproduce the printed numbers.** From the printed relations, reproduce (S2) exactly and (S4)'s two bounds at
`T0 = 2.7 K, h0 = 0.55`; print residuals. This is the `PRINTED`-input reproduction the R3C2 census would perform on this entry,
done here because the elimination in limb B rests on it.

Limb B — **eliminate `R*`.** Treat `T0, H0` as fixed to their printed values. Sweep `R*` over the printed admissible interval and
record the interval of present shock positions `r/H0⁻¹` that (S3) admits; report its extremes, the ratio max/min, and whether the
`ln²(1/R*)` factor is bounded on the interval (it is not as `R* → 0`; the question is what the *printed* lower limit on `R*`
does). Report separately whether any **dimensionless combination** of `r, H0, T0` is independent of `R*` — the codex framing.

Limb C — **input or output.** For each of `H0, T0`: quote the sentence where it enters and classify it `MEASURED`-input or
derived output under the R3C2 origin taxonomy (the seat classifies; the lane records). Count equations and unknowns for the
present-time relation; state whether the "derived length scale" is a function *of* the two observables or a prediction *for*
either of them.

## 4. Outcome classes (precedence top to bottom; exactly one is filed)

1. `R3G_NO_CLASS` — a pre-audit control fails in every seat, or the packet fails redaction.
2. `INCONCLUSIVE_BRANCH` — the printed solution family does not say which branch or which interval of `R*` represents the claimed
   universe, and the answer to limb B differs between admissible readings; state both.
3. `SHOCK_UNREPRODUCED` — (S2) or (S4) is **unreproduced from the stated inputs** after two attempts; print the residual (this
   outranks the magnitude classes because limb B rests on the printed relations).
4. `MAGNITUDE_TUNABLE` — over the printed admissible `R*` interval, the present shock position spans a range whose max/min
   ratio exceeds 10, or is unbounded; the construction fixes the shape (a log dependence) but not the magnitude.
5. `MAGNITUDE_BOUNDED` — the range is bounded with max/min ratio at most 10, and no dimensionless invariant exists: the
   construction fixes the magnitude to within an order of magnitude but predicts nothing beyond the inputs.
6. `INVARIANT_FIXED` — a dimensionless relation among `r, H0, T0` independent of `R*` exists and is stated with its printed
   derivation; this would be the corpus's first construction-fixed observable magnitude on this branch.

The threshold of 10 is chosen now, before any number is computed, as the line between "an order of magnitude" and "decades".

**Stated before ordering:** (S1) shows the distance scales with `ln²(1/R*)`, so a bounded range depends entirely on the paper's
printed floor for `R*`. If the paper prints no floor, class 4 is the likely outcome and the study's value is one line in the
record: entry 36's "derived length scale" depends on an epoch the paper says it cannot set.

## 5. Controls

- **C1 SOURCE_IDENTITY** — byte-exact anchors for lines 96–104, 155–167, 186–214, 225–233, 285–299 and eqs. 7.31, 7.37, 7.38, 8.7
  (the text is PDF-extracted with broken fraction layout; anchors are `repr()`-normalised as R3A's C1 did).
- **C2 POSITIVE** — the worked value (S2) reproduced to the printed two significant figures before limb B runs.
- **C3 DELETION_PROBE** — delete the printed `R*` floor from the input set and require limb B to fail with the exact code set
  `{R3G_C3_NO_START_FLOOR}` rather than silently sweeping to `R* → 0`.
- **C4 HARNESS** — live `sympy` version print through the wrapper.
- **Negative control** — plant `ln(1/R*)` in place of `ln²(1/R*)` and require (S2) to fail reproduction.

## 6. Seats

Blind double, two engines (codex via the dispatcher; kimi via `--provider moonshot -m kimi-k3`), packet only, ACCESS_SHA verified
by the lane after exit, nothing read before a seat exits, no edit under a running seat. Lane's own second route for limb A and
the `R*` sweep sealed before dispatch.

## 7. Closed-check against prior studies

K2 classified shell-free boundary motion; K4 tested the top-hat comoving boundary; both are junction questions. This study
accepts the shock junction as the theorem gives it and asks only whether the printed present-day number is fixed. No ledger
entry is re-run. Entries 37, 38, 57 are pinned as foundation only; no claim in them is tested here.

## 8. Versions

| version | date (KST) | change |
|---|---|---|
| DRAFT 1 | 2026-09-05 (this file) | written; not ordered, not frozen, not gated |

R3G_PREREG_DRAFT_COMPLETE
