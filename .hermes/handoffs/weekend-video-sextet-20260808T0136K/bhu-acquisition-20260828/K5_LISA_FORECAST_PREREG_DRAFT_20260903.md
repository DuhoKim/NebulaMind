# DRAFT — NOT ORDERED — K5 pre-registration: a calibrated ringdown forecast for de Sitter-core "cosmological black holes" (entries 21, 16) (Tori, 2026-09-03 22:18 KST)

**Status:** drafted on Duho's word "k5 draft prereg too" (pane, 2026-09-03 22:18 KST), completing the set begun on Blanc's 20:03 continuation note
(K3 step 2, K4). No derivation, no seats beyond the referee gate. Becomes live only on Duho's order; re-gated at that time.

## 0. Why this would exist
Entry 21 (Roupas 2022) is the corpus's only `W_ROUTE_CONNECTED` prospect: it computes quasi-normal-mode frequencies for regular
black holes with a de Sitter core and maps them onto a detector band — "for black hole masses M ∈ [10, 10⁹] M☉, the fundamental
frequency lies in the range 10⁻⁶ Hz ≲ ω_R,0 ≲ 50 Hz" (`2203.13295_clean.txt` L395) and "for M ≳ 10⁴ M☉ the fundamental mode …
lies within the frequency detectability range" of a space interferometer (L399). What it does NOT supply is an amplitude: the
excitation factors are named as the missing step in the paper's own words (L400), so the route is connected but not calibrated
(`WARRANT_TABLE_20260903.md` row 21). Entry 16 (Pourhassan 2025) names gravitational-wave echoes and primordial-black-hole
surveys without a model likelihood (row 16, `W_ROUTE_NAMED_ONLY`; source L75–76, L610–618, L622–630). K5 asks whether the named
route survives being calibrated: does any admissible model point produce a ringdown a LISA-class detector could both SEE and
DISTINGUISH from an ordinary black hole?

## 1. Objects, every symbol bound
- **The source model:** entry 21's static equilibrium (its Eqs. 4–7, L245) with core parameter α (the paper's Compton-wavelength
  scale, L247) and mass M ∈ [10⁴, 10⁹] M☉ (the band it names as detectable, L399); the axial perturbation equation and scattering
  potential it derives (L250, L269) and its tabulated fundamental modes (Table 1, L365; Figures 4–5, L271, L367).
- **The discriminant:** the axial–polar splitting. Entry 21 imports isospectrality for ultracompact de Sitter-core objects from its
  ref. [28] (row 21's borrowed-inputs field, SOURCE L245). Whether the splitting is nonzero at all for this model is therefore the
  first thing the study must establish, not assume; if isospectrality holds exactly, the discriminant is the mode SPECTRUM
  (frequency–damping pairs versus the Kerr/Schwarzschild ringdown), not the splitting.
- **The detector:** the official LISA sensitivity curve and Galactic-confusion foreground model, fetched and pinned at step 1
  (not currently in the lane's sources tree); the source-frame-to-detector-frame redshift factor with a pinned cosmology.
- **The amplitude chain:** excitation factors → ringdown strain amplitude at the source → luminosity distance → detector response →
  signal-to-noise ratio, each step's formula pinned at step 1 with a receipt.

## 2. The question, exactly
Over the admissible (M, α, distance) volume that entry 21's own construction allows, is there a nonempty region where (i) the
ringdown signal-to-noise ratio in a LISA-class detector exceeds a declared detection threshold AND (ii) the mode content is
distinguishable from a Kerr ringdown of the same mass and spin at a declared statistical level, with ordinary source parameters
marginalised?

## 3. Outcome classes — declared now
- **K5_DETECTABLE_AND_DISTINGUISHABLE:** a nonempty admissible region satisfies both; entry 21's route becomes a calibrated
  falsifier with a stated strain target (a real prediction, and the corpus's first).
- **K5_DETECTABLE_NOT_DISTINGUISHABLE:** loud enough, but degenerate with an ordinary black-hole ringdown once mass and spin are
  marginalised — the "mode camouflage" the paper itself names (L401); the route stays connected, never calibratable.
- **K5_UNDETECTABLE:** no admissible point clears the detection threshold; the named route is closed.
- **K5_AMPLITUDE_FREE:** the excitation factors are not fixed by the construction (an arbitrary normalisation survives), so no
  strain can be predicted → INCONCLUSIVE, and the same "amplitude irreducibly free" pattern the freedom map found for the cutoff
  (`PROGRAM_A_FREEDOM_MAP_20260902.md`) would be recorded a second time, which is itself a finding for the record.
- **K5_MODEL_UNDERDETERMINED:** the admissible (M, α) region is not fixed by the pinned construction → INCONCLUSIVE; name the freedom.

## 4. What counts as a verdict either way
A computed signal-to-noise map over the admissible volume against the pinned sensitivity curve, plus a distinguishability statistic
(declared: e.g. a Bayes-factor or mismatch criterion with its threshold fixed before computing) against a Kerr template bank; one
class filed. Reproducing entry 21's Table 1 frequencies is a control, not a result.

## 5. Controls (must pass before any class is filed)
- **C1 reproduction:** the seat's mode solver must reproduce entry 21's tabulated fundamental frequencies (Table 1, L365) and the
  10⁻⁶–50 Hz band statement (L395) within a declared tolerance. Failure = the solver is wrong; stop; no class.
- **C2 Schwarzschild limit:** as α → 0 the solver must return the textbook Schwarzschild quasi-normal frequencies (pinned at step 1
  by a receipted reference value). Failure = stop; no class.
- **C3 detector control:** the pipeline must reproduce a published signal-to-noise ratio for one standard LISA source (pinned at
  step 1) within a declared tolerance. Failure = stop; no class.
- **C4 deletion probe:** removing the distinguishability test must change the class of at least one region (declared before running:
  K5_DETECTABLE_NOT_DISTINGUISHABLE → K5_DETECTABLE_AND_DISTINGUISHABLE). Failure = stop; no class.

## 6. Seat plan, blind double, cost
Two blind seats (codex, Claude seat: mode solver plus detector pipeline, each its own script), third seat via
`nm_referee_dispatch.sh` on a class split, an independent second route for the "both" standard (e.g. a time-domain ringdown
injection against a frequency-domain SNR calculation), Kimi on the check-sheet arithmetic. About fifteen seat-days (round-2 seat
estimate, `TOPIC_SEARCH_ROUND2_RECONCILIATION_20260903.md`); data: public LISA sensitivity products only, fetched at step 1; laptop
compute.

## 7. What would make it INCONCLUSIVE
K5_AMPLITUDE_FREE or K5_MODEL_UNDERDETERMINED; or C1–C3 failing in both seats after two attempts; or the LISA sensitivity products
being unavailable through open routes (then the study waits, and the acquisition line goes to Duho as with the 1980s papers).

## 8. Non-circularity
No observed gravitational-wave event enters. The detector curve and the Kerr template bank are instruments of comparison, not
inputs to the source model; entry 21's own tabulated frequencies are a CONTROL on the solver, not the result. Entry 16 is touched
only if its named echo/PBH channels can be given a likelihood; if not, its `W_ROUTE_NAMED_ONLY` stands unchanged.

## 9. Relationship to the rest of the lane
K5 is independent of K2 (junction theorem, done), K3 (spin closure, step 1 done) and K4 (draft; causal-boundary transfer physics).
It is the only remaining cluster whose success would give the corpus a NEW calibrated falsifier rather than closing an old one.
