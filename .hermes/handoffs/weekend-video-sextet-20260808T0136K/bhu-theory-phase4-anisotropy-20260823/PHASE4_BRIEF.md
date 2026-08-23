# Phase 4 brief — the anti-Copernican discriminant (2026-08-23 23:12 KST, Tori)

## 0. Why this study exists

Reading batches 1–9 (2026-08-23) established that the interior-geometry branch of the BHU family
is anti-Copernican **in print**: Smoller & Temple 2000 states the model "would place our solar
system in a special position relative to the center of the explosion", and Blau–Guendelman–Guth
1987 is the exact-solution anchor for the exterior-black-hole / interior-universe geometry. No
paper in the 51-entry base layer computes the observational consequence. The branch is
consistency-only precisely because nobody calibrated it. This phase manufactures the branch's
first calibrated confrontation — or shows honestly why one cannot be built.

**The claim under test (stated before any derivation):** if the observable universe is the
interior of a horizon-bounded region entered off-center, the geometry generically implies
radially structured observables — an anisotropy in the locally inferred expansion rate, an
excess (non-kinematic) dipole, and/or a suppression of power near the horizon scale. Either
existing data bounds the off-center parameter (a calibrated consistency statement, the branch's
first), or the observable-scale version of the branch is excluded (a falsification). Both
outcomes are publishable-grade; neither is circular.

## 1. Tracks

**Track A — the strict interior model.** From the pinned exact solutions ONLY (no literature
shortcuts): the Smoller–Temple FRW/TOV shock-matched metric (entries 36, 57 — both held in full)
and the entry-37 inside-the-horizon construction (PNAS 2003 — to acquire, task 0). Derive the
null geodesics seen by an observer displaced x_off from the center, and the resulting
sky-dependence of (a) the redshift–distance relation (an H₀ dipole/quadrupole amplitude as a
function of x_off and shock distance R_shock), and (b) the CMB dipole beyond the kinematic term.
Deliverable: closed-form or numerically tabulated D(x_off, R_shock) — the prediction functions.
Every equation traced to the pinned source or derived in-lane; derivation receipts as in Phase 3.

**Track B — the data confrontation.** Freeze the observational bounds FIRST, from primary
sources quoted at freeze time (rule: no directional claim from memory —
[[feedback_anchor_block_verify_from_source]]):
- B1: H₀/expansion anisotropy — the cluster-scaling anisotropy literature and SN-compilation
  dipole fits. Candidate anchors (all [VERIFY-AT-FREEZE], not asserted): Migkas et al. 2021
  (A&A, cluster X-ray scaling anisotropy), Pantheon+ dipole analyses, quasar dipole work.
- B2: CMB dipole consistency — Planck's measured dipole vs the kinematic expectation, and the
  published bounds on an intrinsic component ([VERIFY-AT-FREEZE] against Planck papers).
- B3: large-scale power suppression — the low-ℓ anomaly numbers and the published significance
  range ([VERIFY-AT-FREEZE]; treat as weak evidence either way — the significance is contested,
  and the record must say so).
Deliverable: a frozen bounds table with per-number primary-source quotes and shas.

**Track C — the confrontation and verdict.** Push the frozen bounds through the Track A
prediction functions to bound x_off/R_shock (or exclude). State the verdict in the established
classes: a new CALIBRATED-FALSIFIER for the branch if the machinery closes; CANNOT-CALIBRATE
with the specific obstruction named if it does not. Kill criteria, stated now:
- K1: if Track A shows the observables are degenerate with initial conditions (i.e., the metric
  can absorb any x_off into unobservable gauge), the branch is UNTESTABLE-AS-STATED — say so.
- K2: if the predicted signal at all allowed x_off is below current *and* forecast sensitivity,
  the study closes as PROSPECT with the required sensitivity computed.
- K3: no parameter added beyond (x_off, R_shock) without a gate; a growing dial-count is the
  Phase-3 βH⁴ lesson.

## 2. Sources

Held and pinned (bhu-reading-20260823/sources/): smoller_temple_2000 (sha ef904904…),
smoller_temple_1997 (sha 6e709a9c…), blau_guendelman_guth_1987 (sha 1d195f5f…).
Task 0 acquisitions: entry 37 (Smoller & Temple, PNAS 100, 11216 (2003) — PNAS open archive,
free), and the entry-54 PRD pin cross-referenced from the campaign records. Data-side primary
papers acquired at Track B freeze, campus IP where entitled.

## 3. Discipline (inherited from Phase 3, restated)

- No claim classed or frozen from memory or triage; every anchor quoted from pinned source text.
- Cross-engine gates: each track gated on Codex and kimi (hermes_moonshot.sh wrapper; key never
  printed) before its verdict stands; same-family Claude gate is the weakest and never sole.
- Receipts for every numeric: scripts in-lane, one shasum per line, timestamps from `date`.
- Writes confined to this lane dir; temp files as `_tmp_*` here, never TMPDIR.
- The verdicts file sha-pins the prose AFTER final edit (the stale-pin lesson, twice).
- This is BHU-lane work under the standing hold directive (BHU lanes continue).
- "BHU is falsified" is not a sayable sentence from this study; at most the OBSERVABLE-SCALE
  INTERIOR BRANCH can be excluded, and the record must keep that scope.

## 4. What this phase is NOT

Not a paper draft (no .tex); not a DESI-lane task (no survey data reduction — published bounds
only); not a rebuild of the spin-parity study (that test is frozen and blocked on its three
human checkers, untouched by this phase); not a Gaztañaga-branch audit (entry 54's window has
its own watch).

## 5. Sequence and triggers

1. Duho reads this brief → "go ahead" freezes it (sha-pinned) and starts Track A.
2. Track A verdict → gate → Duho pinged.
3. Track B freeze (primary-source quotes) → gate → Duho pinged.
4. Track C confrontation → cross-engine gates → final verdict deck.
No wall-clock promises; Track A is the long pole (real derivation work, order weeks of lane
time, resumable across sessions).
