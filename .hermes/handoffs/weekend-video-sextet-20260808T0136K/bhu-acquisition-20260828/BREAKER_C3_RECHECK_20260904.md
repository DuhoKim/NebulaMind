# Re-check of all six pattern instances against the CORRECTED breaker condition 3

**Tori, 2026-09-04 22:43 KST. ORDERED by Duho: "fix condition 3 and re-check the six instances".**
Pattern record amended to **V2**, sha256 `5232201acfdca850c7e8a4d345aad145a3d91fdb750fdbb9a77fb43fec8d4647`
(V1 was `fff1f1a8426fd4bf55c1478f407306c5f02bd2f676e4861194b04a133f156c96`).
**No tier, token, standing or stamp moves. Paper HOLD.**

## The corrected condition, and what "re-check" can and cannot mean

> **3. No free normalisation survives** the derivation: replacing every parameter by a free symbol and demanding the
> printed number back **must SUCCEED with no parameter chosen.** If the number can be recovered only once a parameter
> is chosen, a free normalisation survives and this condition **FAILS**.

**First, a distinction that decides the whole re-check.** The five conditions are a test a **candidate
counterexample** must pass. The six instances are not candidate counterexamples — they are instances *of* the
pattern, each determined by its own study's **preregistered outcome classes**, all of which closed **before** the
pattern record was written at 20:56 KST on 2026-09-04.

**So the inversion cannot have flipped any instance's status: no instance was ever adjudicated by condition 3.**
That is the narrow answer, and on its own it would be too convenient to leave there.

**The substantive re-check** is the converse question, and it is the one worth running: **under the corrected
condition, does any instance now PASS condition 3 — i.e. is its number recoverable with no parameter chosen?** An
instance that passes all five conditions would not be an instance at all; it would be the breaker.

## The six instances against corrected condition 3

| # | construction | is the number recoverable with NO parameter chosen? | corrected C3 | still an instance? |
|---|---|---|---|---|
| 1 | causal-horizon cutoff (23–27) | **No.** There is no perturbation prescription; every route to an amplitude imports a choice external to the theory, and the freedom was proved irreducible. | **FAILS** | yes |
| 2 | torsion-bounce spin closure (9–11) | **No.** The printed ⅛ and ¾ are conventions; the derived coefficient is negative and depends on regime and species, so a number appears only once those are chosen. | **FAILS** | yes |
| 3 | de Sitter-core ringdown (21) | **No.** The mode coefficient carries a source integral that a static equilibrium cannot supply; `K5_AMPLITUDE_FREE` was filed under the prereg's own class 4. | **FAILS** | yes |
| 4 | ECKS density ceiling (51) | **No.** The floor cannot be formed at all without adding a size–mass relation `V(M)`; three admissible readings differ by decades or give none. | **FAILS** | yes |
| 5 | ECKS particle production (59) | **No**, and most explicitly of the six: the paper says *"we choose β = 1/929.25"*, and `BETA_FREE` was filed after the citation chain terminated without a derivation. | **FAILS** | yes |
| 6 | Λ from a boundary (56) | **Yes — for the relation itself.** Given `M_T`, `Λ = 3/r_S²` with `r_S = 2GM_T` carries no free coefficient to choose. | **PASSES** | **yes — see below** |

## Instance 6 is the one the correction actually touches

Under corrected condition 3, instance 6 **passes**. It is nonetheless still an instance, because it **fails
condition 4**: `w = −1` is rigid only under an **assumed constant** total mass, which entry 56 states
conditionally at L138 and maintains through a time-dependent junction, and L143–144 permits `M(τ)`. The record
already said this in words — *"what is free is not a coefficient but the fixity of one"* — and the corrected
condition 3 now agrees with that sentence instead of contradicting it.

**Under V1's inverted text, instance 6 would have been recorded as failing condition 3**, because recovery does
**not** fail without a choice. So the inversion did not change instance 6's status, **but it did scramble the
reason**: it would have attributed the freedom to a normalisation rather than to an assumed fixity, which is the
distinction the record was written to draw.

**That is the whole material effect of the defect on the existing record: one instance's stated reason, not any
instance's status.**

## The answer to the order

- **Condition 3 is corrected**, as a versioned amendment with both hashes recorded, not an in-place rewrite.
- **All six instances re-checked. No status changes. Five fail corrected condition 3; instance 6 passes condition 3
  and fails condition 4, which is what the record's own prose already said.**
- **The pattern is unchanged and its six instances stand.** The falsifier is now pointed the right way, which means
  it is a stronger test than it was this morning, not a weaker one: a genuine counterexample can now pass it.

## What this does NOT settle, and one consequence I had to act on

- **No breaker has been found.** Correcting the falsifier does not search for one; the corpus-wide census and the
  Dymnikova branch remain the two places to look, and neither is ordered.
- **`R3D_DYMNIKOVA_FLOOR_PREREG` V4 pinned the V1 conditions by hash**, so my amendment made that pin stale — a
  defect I introduced by acting on this order. R3D is therefore taken to **V5**: the verbatim block and the pinned
  hash are updated to V2, and C6's decision rule for condition 3 is re-polarised to match. **codex's other V4
  findings are NOT repaired** — the comparator sources that sit outside the frozen manifest, the keyword census
  that cannot see a symbols-only relation, and conditions 2 and 4 still reaching outside the document. Those are
  still open, and R3D remains `PREREG_UNSOUND` and NOT run.
