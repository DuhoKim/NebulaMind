# K5 — FROZEN PRE-REGISTRATION: a calibrated ringdown forecast for de Sitter-core "cosmological black holes" (entries 21, 16)

**Tori, 2026-09-04 15:51 KST. Version 1. FROZEN pending the fresh referee gate. ORDERED by Duho ("K3 step 3, K5, K6 in
order", relayed by Blanc 2026-09-04 14:56 KST — second of three, sequential; K3 step 3 filed at 15:28.)**

Predecessor: `K5_LISA_FORECAST_PREREG_DRAFT_20260903.md`, gated `PREREG_SOUND_WITH_REPAIRS` 2026-09-03 22:27 KST
(`K5_DRAFT_GATE_agy.md`); its **nine** repairs are applied and were re-verified clause by clause on 2026-09-04 09:58
KST. This version is the draft plus the requirements of Duho's standing order, above all that a cheap disqualifying
limb runs first.

**No derivation has been run, and no LISA product has been fetched, under this document.**

---

## 0. Why this exists

Entry 21 (Roupas 2022, `2203.13295_clean.txt`) is the corpus's only `W_ROUTE_CONNECTED` prospect. It computes
quasi-normal-mode frequencies for regular black holes with a de Sitter core and maps them onto a detector band:
`10⁻⁶ Hz ≲ ω_R,0 ≲ 50 Hz` for `M ∈ [10, 10⁹] M☉` (**L395**), and for `M ≳ 10⁴ M☉` the fundamental mode "lies within
the frequency detectability range" of a space interferometer (**L399**).

What it does not supply is an amplitude, **in its own words at L400**:

> "Still, in order to estimate the minimum possible amplitude sensitivity of an interferometer so as to detect a
> cosmological black hole ringdown, the excitation factors of its quasi-normal modes, following a binary merger, have
> to be calculated. This is an involved task, that this work urges the community to perform."

So the route is connected but not calibrated. **K5 asks whether it survives being calibrated.**

Entry 16 (Pourhassan 2025) names gravitational-wave echoes and primordial-black-hole surveys without a model
likelihood (`W_ROUTE_NAMED_ONLY`). It is touched only if its named channels can be given a likelihood; if not, its
token stands unchanged and this study says so.

## 1. THE LIMB STRUCTURE — cheapest first, per Duho's standing order

This study is the lane's most expensive at about fifteen seat-days, and it needs a detector product that is **not in
the lane's source tree**. It is therefore split into three limbs, run strictly in order, each able to end the study.

**Limb A — the amplitude question (cheapest, ~1 seat-day, no acquisition, no solver, no compute).**
Does entry 21's construction **fix** the ringdown amplitude, or does a free normalisation survive?

The excitation factors of a ringdown are set by the perturbation that rings the object — for the case entry 21 names,
a binary merger. Entry 21's model is a **static equilibrium** (its Eqs. 4–7, **L245**). To pass limb A, the seat must
write down the exact mathematical derivation fixing the amplitude strictly from the model's pinned parameters without
introducing new free variables; if it cannot, it must conclude the amplitude is:
  - **fixed** by the construction (then limb B follows), or
  - **free** — no strain is predictable without an input the construction does not contain, in which case
    **file `K5_AMPLITUDE_FREE` and stop**: no LISA product is fetched, no mode solver is written, no compute is run.

The seat must state explicitly whether "the paper does not compute it" (which L400 says outright) is the same as "the
construction does not fix it" (which does not follow from L400 alone and must be argued). **Conflating those two is
the specific error this limb must not make.**

**Limb B — acquisition (only if limb A passes).** The official LISA sensitivity curve and Galactic-confusion
foreground, by a **legitimate open route only**: no paywall bypass, no purchase, no credentialed access. Every route
tried is logged with its response class, as `NURGALIEV_PONOMARIEV_OPEN_ROUTE_RETRY_20260904.md` did. If no validated
open product exists, the study **waits** and the acquisition line goes to Duho; it does not proceed on a
reconstructed-from-memory curve.

**Limb C — the expensive half (only if A and B pass).** Mode solver, amplitude chain, detector response, SNR map, and
the distinguishability statistic of §3.

## 2. Objects, every symbol bound

- **Source model:** entry 21's static equilibrium (Eqs. 4–7, **L245**) with core parameter `α` (**L247**) and mass
  `M ∈ [10⁴, 10⁹] M☉` (the band it names as detectable, **L395 and L399**); its axial perturbation equation and
  scattering potential (**L250, L269**); its tabulated fundamental modes (Table 1, **L365**; Figures 4–5,
  **L271, L367**).
- **Discriminant:** the axial–polar splitting. Entry 21 **imports** isospectrality for ultracompact de Sitter-core
  objects from its ref. [28] (**L245**). Whether the splitting is nonzero at all for this model is therefore the first
  thing limb C must establish, **not assume**; if isospectrality holds exactly, the discriminant becomes the mode
  spectrum (frequency–damping pairs against the Kerr/Schwarzschild ringdown), not the splitting.
- **Detector:** the official LISA sensitivity curve and confusion foreground, pinned in limb B; the
  source-frame-to-detector-frame redshift factor with a pinned cosmology.
- **Amplitude chain:** excitation factors → ringdown strain at the source → luminosity distance → detector response →
  signal-to-noise ratio, each step's formula pinned with a receipt at the step that uses it.

## 3. The question, exactly

Over the admissible `(M, α, distance)` volume entry 21's construction allows, is there a nonempty region where **(i)**
the ringdown signal-to-noise ratio in a LISA-class detector exceeds a detection threshold pinned at limb C **and
(ii)** the mode content is distinguishable from a Kerr ringdown of the same mass and spin at a statistical level
pinned at limb C, with ordinary source parameters marginalised?

## 4. Outcome classes — declared now

1. **K5_DETECTABLE_AND_DISTINGUISHABLE** — a nonempty admissible region satisfies both; the route yields a stated
   strain target.
2. **K5_DETECTABLE_NOT_DISTINGUISHABLE** — a nonempty region clears the detection threshold, but NO region is
   distinguishable from an ordinary black-hole ringdown once mass and spin are marginalised — the "mode camouflage"
   the paper itself names (**L401**).
3. **K5_UNDETECTABLE** — no admissible point clears the detection threshold.
4. **K5_AMPLITUDE_FREE** — the excitation factors are not fixed by the construction, so no strain can be predicted.
   **INCONCLUSIVE.** This is **limb A's exit** and requires no acquisition and no compute. If it fires, the record
   gains a second instance of the "amplitude irreducibly free" pattern the freedom map found for the cutoff
   (`PROGRAM_A_FREEDOM_MAP_20260902.md`), which is itself a finding.
5. **K5_MODEL_UNDERDETERMINED** — the admissible `(M, α)` region is not fixed by the pinned construction.
   **INCONCLUSIVE**; name the freedom exactly.
6. **K5_ACQUISITION_BLOCKED** — limb B finds no validated open LISA product. The study **waits**; not a scientific
   class, and it must not be reported as one.
7. **K5_NO_CLASS** — a control fails in both seats after two attempts.

Class 4 takes precedence over 1, 2 and 3: if no amplitude is predictable, no detectability statement may be filed.

## 5. What counts as a verdict

A computed signal-to-noise map over the admissible volume against the pinned sensitivity curve, plus a
distinguishability statistic and threshold pinned at limb C against a Kerr template bank; one class filed.
**Reproducing entry 21's Table 1 frequencies is a control, not a result.**

## 6. Controls, each with an exact named code

- **C1 — reproduction.** The seat's mode solver must reproduce entry 21's tabulated fundamental frequencies
  (Table 1, **L365**) and the `10⁻⁶–50 Hz` band statement (**L395**) within a tolerance pinned at limb C. Exact
  assertion: `C1_TABLE1_REPRODUCED=PASS`.
- **C2 — Schwarzschild limit.** As `α → 0` the solver must return the textbook Schwarzschild quasi-normal
  frequencies, pinned at limb C by a receipted reference value. Exact assertion: `C2_SCHWARZSCHILD_LIMIT=PASS`.
- **C3 — detector control.** The pipeline must reproduce a published signal-to-noise ratio for one standard LISA
  source, pinned at limb C, within a tolerance pinned at limb C. Exact assertion: `C3_DETECTOR_CONTROL=PASS`.
- **C4 — deletion probe.** Removing the distinguishability test must change the class of at least one region; the seat
  states the expected change (`K5_DETECTABLE_NOT_DISTINGUISHABLE → K5_DETECTABLE_AND_DISTINGUISHABLE`) **before**
  running. Exact assertion: `C4_DISTINGUISHABILITY_DELETION=PASS`.
- **C5 — amplitude provenance.** The amplitude pipeline must physically halt if any variable outside the pinned set
  `(M, α, distance)` is requested. The seat asserts `C5_AMPLITUDE_PROVENANCE=PASS` only if the executed code contains
  no external amplitude injections. Exact assertion: `C5_AMPLITUDE_PROVENANCE=PASS`. **This
  is the control limb A turns on, and it is the one that must not be finessed.**

**All controls that belong to a limb not reached are recorded `NOT RUN`, never as passes** — the discipline K4 and
K3 step 3 established. The check sheet names the exact set `{C1_TABLE1_REPRODUCED, C2_SCHWARZSCHILD_LIMIT,
C3_DETECTOR_CONTROL, C4_DISTINGUISHABILITY_DELETION, C5_AMPLITUDE_PROVENANCE}` and states each one's status.

## 7. Executable discipline

`K4_BOUNDARY_TRANSFER_PREREG_20260904.md` §7, adopted unchanged: every cited script exists, runs under `python3`, is
re-executed by Tori and not only by its author, has its output preserved as a file and hashed in the check sheet, and
no sentence calls a script executable support unless all of that holds. **Four instances of this defect have now been
caught in this lane** (`K2_route2_agy.py` a stub; `cutoff_phase1_camb.py` absent; K4's and K3 step 3's seat outputs
unpreserved by their authors).

## 8. Seats — Duho's "both" standard

Blind double (codex and the Claude seat); third seat through `nm_referee_dispatch.sh` (ACCESS_SHA proof or no verdict)
on any split; an independent second route by a different method, blind to route 1 (for limb C: a time-domain ringdown
injection against a frequency-domain SNR calculation); Kimi via the Moonshot route on the check-sheet arithmetic with a
no-fallback control; a one-page human check sheet; Tori re-runs every script. A "what a critic gets" note is filed
after the result and before any ruling.

## 9. What makes this INCONCLUSIVE

Class 4 (limb A's exit) or class 5; or C1/C2/C3 failing in both seats after two attempts (class 7); or route 1 and
route 2 disagreeing after a third seat. Class 6 is a wait, not a verdict. In every case the residual freedom is stated
exactly and **no amplitude, threshold or sensitivity curve is manufactured**.

## 10. Non-circularity and scope

No observed gravitational-wave event enters. The detector curve and the Kerr template bank are instruments of
comparison, never inputs to the source model; entry 21's own tabulated frequencies are a **control on the solver, not
the result**. Entry 16 is touched only if its named channels can be given a likelihood; otherwise its
`W_ROUTE_NAMED_ONLY` stands and this study says so explicitly.

No tier, warrant token, standing or stamp moves on Tori's authority. **NOT ordered and untouched:** the downstream
bounce study from K3 step 2, and the K4 follow-up under a declared assumption. K6 follows *after* this study is filed.
Row 23 of the K4 annotation stays as applied. Paper HOLD; nothing outward.

## 11. Cost and stopping rule

Limb A about one seat-day; limb B a few hours of open-route acquisition; limb C the remainder of the ~15 seat-day
estimate. **Stop and file at the first limb that exits.** If limb C is reached and has not converged after the second
route plus one third seat, stop and file whatever class is reached.

---

## 12. Gate record (V1 → V2)

`K5_PREREG_GATE_20260904_agy.md` (fresh seat via `nm_referee_dispatch.sh`, ACCESS PROVEN,
`ACCESS_SHA=2b36b505f2535e98baabae7372f3f89c852f991f6817b47a0395c3d7365fb01a`) returned
`GATE=PREREG_SOUND_WITH_REPAIRS` with three repairs, **all applied verbatim**. Every one replaced a promise with a
mechanical test, which is the right criticism to make of this lane:

1. **Limb A's exit rested on a seat's judgement.** Warning a seat not to conflate "the paper does not compute it" with
   "the construction does not fix it" is an admonition, and the gate's word for what a seat can do with an admonition
   is "finesse". Limb A now demands the **exact derivation** fixing the amplitude from the pinned parameters without
   new free variables; failure to produce it *is* the finding.
2. **Classes 1 and 2 were not mutually exclusive** — a model distinguishable in some regions and degenerate in others
   could have fired both. Class 2 now requires that **no** region be distinguishable.
3. **C5 was a promise to print documentation.** It now requires the pipeline to **halt** if any variable outside the
   pinned set `(M, α, distance)` is requested, and passes only if the executed code contains no external amplitude
   injection.

The gate also verified the numeral tracing and found the circularity defence robust, noting entry 21's Table 1 control
sits at a mass disjoint from the result volume.

On whether the study is worth its ~15 seat-days, the gate's answer: given L400's own words that calculating the
excitation factors is an "involved task" left to the community, **limb A is highly likely to end the study
immediately, and the design is right to spend the cheap limb before committing.**

K5_PREREG_V2_FROZEN
