# BS-2a is fillable. An upstream quality cut exists with 32% headroom.

**Authorised catalogue metadata query, 2026-08-28 13:29–13:39 KST. No image bytes.**

## Provenance

`acquire/fetch_quality.py` — the frozen record's own TAP client, with its receipts, backoff, chunking
and byte caps. `acquire/quality_query.adql` differs from the selection query `positions_query.adql`
by **exactly one line**, the SELECT list; the WHERE clause is byte-identical, so the row set is the
same population.

    endpoint   https://datalab.noirlab.edu/tap/async
    13 chunks, 6,445 bricks, 65,060 rows          ← exactly the frozen sample size
    quality_selected.csv sha256 61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3
    join on ls_id: 65,060 of 65,060 — no losses, no extras

Columns: `flux_ivar_r`, `psfsize_r`, `nobs_r`. All three confirmed present in the DR10 tractor
schema; `fracflux_r`, `fracmasked_r`, `fracin_r` are **absent** and cannot be used.

## The concern was real. The magnitude is not.

Survey quality genuinely varies with position along the tested axis:

    corr(flux_ivar_r, cos θ) = −0.2532
    corr(psfsize_r,   cos θ) = +0.3659
    corr(nobs_r,      cos θ) = −0.3012

So a quality cut **is** correlated with the axis — the objection was well founded. It does not
matter, because Var(cos θ) sits far above its threshold.

## The gate is N_eq = 3·N·Var(c) against NEQ_MIN = 100,000

`ref/successor_ref_v9.py` line 85.

    cut                          kept    attrition   Var(cosθ)      N_eq    floor 100,000
    (no cut) baseline          65,060       0.0%      0.7561     147,578    PASS
    flux_ivar_r > p10          58,554      10.0%      0.7700     135,257    PASS
    psfsize_r  < p90           58,553      10.0%      0.7609     133,657    PASS
    nobs_r    >= 3             56,696      12.9%      0.7542     128,287    PASS
    combined p10+p90+n3        49,211      24.4%      0.7517     110,983    PASS
    flux_ivar_r > p25          48,795      25.0%      0.7458     109,179    PASS
    nobs_r    >= 5             34,278      47.3%      0.5243      53,916    FAIL

**The sample can lose 32.2% at unchanged Var before N_eq reaches the floor.**

## Findings

1. **An admissible upstream quality cut exists.** The combined cut — `flux_ivar_r` above its 10th
   percentile, `psfsize_r` below its 90th, `nobs_r ≥ 3` — removes 24.4% of the sample and leaves
   **N_eq = 110,983 against a floor of 100,000.** Every quantity is a catalogue column evaluated
   before any cutout exists, so its independence from handedness is **temporal, not argued**.
2. **`BS2A_DESIGN_V2.md`'s refusal is overturned.** It concluded *"no admissible upstream quantity
   protects power without destroying the frozen sample"* on the ground that there was *"no
   guarantee"* the geometry survives. There is now a number. The guarantee was computable and the
   refusal was an assertion.
3. **Var barely moves because it is a shape property, not a size property.** Three of the seven cuts
   *increase* it. What kills N_eq is losing N, not losing spread — `nobs_r ≥ 5` fails on attrition
   (47.3%), not on geometry (Var 0.5243 is still 3.5× threshold).
4. **BS-2a's original cause was already resolved** by deleting §2.7 reason (d) and refusing reason
   (c): acceptance is integrity-only and excludes nothing on the measured quantity. The refusal has
   been carried as a status since 19:02 on 2026-08-27, after its premise was removed.

## The cost, stated

Any cut changes N and **invalidates the closure, geometry and Stage-P receipts computed on 65,060**,
including `plan_digest aaeaa9f3…` and the 12,117-brick manifest. That is a recomputation cost, not an
impossibility, and it must be paid before BS-6 if a cut is adopted. The manifest would also shrink,
reducing the 148 GB ceiling.

## What is NOT established here

Whether the study *needs* a quality cut at all. That depends on how far accuracy `a` degrades when
unmeasurable cutouts enter the estimator, which cannot be known without measuring `a` on real
cutouts — and no image has been fetched. **This receipt establishes only that a cut is available and
affordable if wanted.** Adopting one is a decision, not a consequence.
