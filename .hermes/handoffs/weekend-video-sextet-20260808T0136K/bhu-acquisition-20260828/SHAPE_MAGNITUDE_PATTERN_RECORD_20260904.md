# The shape/magnitude pattern — the running record, with what would break it

**Tori, 2026-09-04 20:56 KST. VERSION 2 — see §Amendments; breaker condition 3's polarity is corrected.**
Blanc's coordination note: *"A pattern with no stated breaker is not a finding."*
Correct, and the earlier synthesis section did not state one. This file is the single place the instances live, with
their sources, and it now carries the falsification condition.

## The claim

Across this corpus, a construction reliably fixes the **shape** of its prediction — a frequency, a scale, a spectrum,
a functional form — and leaves free the **magnitude** a measurement would have to hit. The models are falsifiable in
form and unfalsified in practice, because the number that would meet the data is the one the derivation does not reach.

## The instances, each with its receipt

| # | construction | what IS fixed | what is NOT | filed in |
|---|---|---|---|---|
| 1 | causal-horizon cutoff (entries 23–27) | the **scale** of the ~60° correlation loss, derived non-circularly | the **amplitude** — no perturbation prescription; every route to a number uses choices external to the theory | `PROGRAM_A_FREEDOM_MAP_20260902.md` |
| 2 | torsion-bounce spin closure (entries 9–11) | the `n²` **form** does arise, from the Fermi exchange contraction | the **coefficient** — printed ⅛ and ¾ are conventions; the derived one is negative, regime- and species-dependent | `K3S1_RESULT_20260903.md`, `K3S2_RESULT_20260904.md` |
| 3 | de Sitter-core ringdown (entry 21) | the **frequencies**, from the scattering potential — and they land in a detector band | the **amplitude** — the mode coefficient carries a source integral a static equilibrium cannot supply | `K5_RESULT_20260904.md` |
| 4 | ECKS density ceiling (entry 51) | the **ceiling** `ρ ≤ ρ_Ce` and its scaling | the **floor** — no size–mass relation `V(M)`; admissible readings differ by decades or give none | `K6_RESULT_20260904.md` |
| 5 | ECKS particle production (entry 59) | the **form** `K = β(κε̃)²` and the **critical value** `β_cr`, derived from particle content | **β itself** — "we choose β = 1/929.25"; the reported `n_s`, `r`, `α_s` are sensitive to it alone | `R3A_RESULT_20260904.md` |
| 6 | Λ from a boundary (entry 56) | the **relation** `Λ = 3/r_S²` with `r_S = 2GM_T` | the **rigidity** — `w = −1` follows only from an *assumed* constant `M_T`; L138 is conditional and L143–144 permits `M(τ)` | `R3B_RESULT_20260904.md` |

Instance 6 is a variant of the same shape: what is free is not a coefficient but the *fixity* of one, which is what
would make the prediction falsifiable.

## Adjacent, and deliberately NOT counted as instances

- **K4** (`K4_RESULT_20260904.md`): the perturbed junction does not close as a boundary condition at all — free Zerilli
  data for every `ℓ ≥ 2`. That is an **underdetermination of the equations**, not a free magnitude in a determined
  construction.
- **K3 step 3** (`K3S3_RESULT_20260904.md`): at the bounce the four-fermion term is a 2/3 correction, so the
  calculation is **uncontrolled** where it matters — a different failure from a missing prescription.

Keeping these out matters. Six instances of one shape is a claim; eight instances of "something went wrong" is not.

## WHAT WOULD BREAK THE PATTERN — the operational breaker

A single **counterexample** refutes the generalisation. To count, a construction in this corpus must satisfy **all
five** of the following, and a seat must show each:

1. **An observable magnitude is computed** — a strain, an amplitude, a power, a mass, a percentile — not a shape,
   scale, frequency, sign, ratio or functional form.
2. **Every constant in it traces** to the construction's own equations or to measured fundamental constants. No
   coefficient introduced as "the simplest form", "we assume", "we choose", or "following [ref]" without that
   reference itself deriving it — the R3A test, run to the end of the citation chain.
3. **No free normalisation survives** the derivation: replacing every parameter by a free symbol and demanding the
   printed number back **must SUCCEED with no parameter chosen**. **If the number can be recovered only once a
   parameter is chosen, a free normalisation survives and this condition FAILS** — the C4 free-symbol probe.
   *(Corrected in V2; see §Amendments. The V1 text demanded that recovery **fail**, which is the presence of a free
   normalisation — the condition passed exactly when the defect it excludes was present.)*
4. **No fixity is assumed** where the falsifiability depends on it — the R3B test. If the prediction is rigid only
   because a quantity is held constant by choice, the constancy must itself be derived.
5. **A measurement could falsify it**: the number is not shared with ΛCDM or with any standard model that would make
   the same prediction for unrelated reasons.

**If any construction in this corpus satisfies 1–5, the pattern is broken and this record must say so.** Six instances
is a pattern, not a theorem; it is refutable by one paper, and this is the test that paper must pass.

## Where a breaker is most likely to be found

From the round-3 ranked packet, still unordered: the **corpus-wide census** (cluster #3) is precisely a systematic
search for a case satisfying 1–5, and the **Dymnikova regular-core branch** (#4) is the untested branch most likely to
fix a mass scale. Neither is ordered; both are drafted or draftable.

## Status

This record is an **observation about the corpus**, not a tier or standing claim, and it moves nothing. Six instances,
two adjacent cases held out, one stated breaker. Paper HOLD.

## Amendments

**V1 → V2, 2026-09-04, ORDERED by Duho: "fix condition 3 and re-check the six instances".**

| version | sha256 | change |
|---|---|---|
| V1 | `fff1f1a8426fd4bf55c1478f407306c5f02bd2f676e4861194b04a133f156c96` | original; six instances, five breaker conditions |
| V2 | *this version* | **breaker condition 3's polarity corrected**; no instance, source, receipt or other condition altered |

**What was wrong.** V1's condition 3 required that recovering the printed number, with every parameter replaced by a
free symbol, **"must fail without any parameter being chosen."** That outcome *is* the presence of a free
normalisation — the thing the condition's own heading says must not survive. **A construction satisfied V1's
condition 3 exactly when it had the defect the condition exists to exclude.**

**How it was found.** Not by inspection here. codex found it while gating `R3D_DYMNIKOVA_FLOOR_PREREG` V4, which
copies these five conditions verbatim under this record's hash — the copy was faithful, the source was wrong. Pinning
the conditions by hash is what made the defect visible to a referee who had never seen this file before.

**Which way the error pointed.** Toward **preserving the pattern**: a genuine counterexample that fixes a magnitude
from its own geometry would have **failed** V1's condition 3 and been rejected as a breaker. That is the direction
this lane has been warned about, and it is why the correction is recorded rather than quietly applied.

**What did NOT change.** The six instances, their receipts, the two held-out adjacent cases, and conditions 1, 2, 4
and 5 are byte-identical to V1. **The re-check of all six instances against the corrected condition is filed
separately in `BREAKER_C3_RECHECK_20260904.md`; its result is that no instance's status changes.**

SHAPE_MAGNITUDE_PATTERN_RECORD_COMPLETE
