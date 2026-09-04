# K3 step 3 — one-page check sheet

**Tori, 2026-09-04 15:28 KST.** For a human checking this without redoing it. Run any script below with `python3` from
this directory.

## The question
K3 step 2 computed the spin closure in the **free** Dirac gas. The equation that defines the problem has a four-fermion
interaction. **Is that interaction small where the bounce happens?**

## The answer in one line
**No — it is a two-thirds correction exactly there**, so no controlled calculation of the closure exists at the bounce.

## The number, and where it comes from

`R(T) = |ε̃|/ε = α h_n² T² / h_*` with `α = (9/16)κ` (entry 10 Eq. (10), **L116–118**) and the ultrarelativistic
`ε(T)`, `n(T)` (**L152–L168**).

| where | `R` | receipt |
|---|---|---|
| at the bounce `T_cr` | **2/3** | `K3S3_route2_agy.out`; `K3S3_tori_verify.out` `VERIFY_R_BOUNCE_TWO_THIRDS=PASS` |
| at `T_cr/100` | `1/15000 ≈ 6.7e-5` | `K3S3_limbA_codex.out` `R_AWAY_EXACT=1/15000` |
| at matter–radiation equality | `~1e-56` | `K3S3_route2_agy.out` §5 |

Threshold declared in the prereg **before** computing: limb A fires if `|R| ≥ 0.1`. `2/3 ≥ 0.1`, so it fires.

## Where the bounce value actually comes from — the part worth checking
`T_cr` is **not** "where the energy density cancels". It is the **minimum of the scale factor**, `da/dT = 0`
(entry 10 **L179**) applied to `a(T)` of Eq. (15) (**L169–L176**). Route 2 integrated Eq. (14) itself and confirmed the
integration reproduces the printed Eq. (15), then imposed the minimum: `T_cr² = 2h_*/(3α h_n²)`, giving `R = 2/3`.

**So 2/3 is a computed consequence of the paper's own equations, not a tautology.** Had the bounce been defined by
`ε + ε̃ = 0`, `R` would be 1 by fiat — and that is precisely the error described next.

## Two things the lane got wrong, and who caught them
1. **Tori's own seat** asserted `R = 1`, assuming the wrong bounce condition. codex caught it blind; route 2 caught it
   blind by a different method; Tori re-derived it rather than accepting either (`K3S3_tori_verify.out`,
   `TORI_SEAT_INTERMEDIATE_WRONG=True`). The class is unaffected — both 1 and 2/3 clear the threshold.
2. **The prereg's own gate** predicted the ratio would be "exactly 1" and "by construction". It is 2/3, and it is
   derived. The gate was right that limb A would fire and wrong about the value and the reason — which is the case for
   computing the cheap limb instead of trusting the argument that it must fire.

## What was NOT done
- **Limb B (Hartree–Fock) was never written.** The study cost the cheap limb alone.
- **Six of the seven controls are NOT RUN**, by name: `C1_FREE_LIMIT_MATCHES_K3S2`, `C2_INTERACTION_DELETED`,
  `C3_FOUR_TERMS_SEPARATE`, `C5_MAP_DERIVED`, `C6_BOTH_OBJECTS_REPORTED`, `C7_NO_PRINTED_COEFF_INPUT`. They belong to
  limb B. They are **not** claimed as passes. Only `C4_EXPANSION_PARAMETER_COMPUTED=PASS` is claimed, in all three seats.
- **No tier, warrant token, standing or stamp moved.**

## What it means for K3 step 2
Step 2's `−(3/8) n²/N_f` to `−(3/16) n²/N_f` **stands wherever the theory is perturbative** — everywhere below about
`0.32 T_cr`. It is **not** established at the bounce. Taken together: the printed closures are refuted where the
calculation is controlled, and at the bounce nobody has a controlled calculation at all.

## Arithmetic re-check
Kimi, Moonshot route, no-fallback control: all nine steps CORRECT, including that `1 ≠ 2/3`
(`K3S3_KIMI_ARITHMETIC_20260904.md`).

## Receipts (sha256)
```
K3S3_SELFCONSISTENCY_PREREG_20260904.md  5c7dcc06809cd0af7b2f86a1719c4927e1ed41f5a7d4cf04af9d5343dbfc894f
K3S3_limbA_claude.py / .out              9bc48c12…d612e / 5ff0cdd3…6aae0
K3S3_limbA_codex.py / .out               72a828f0…d7f00 / b49a8fe1…7f664f
K3S3_route2_agy.py / .out                8ea8ce20…b32b6f / 25762c8f…8544c0
K3S3_tori_verify.py / .out               ec854a7e…a9881f / c90fcc64…f72824
```
Full hashes in `K3S3_RESULT_20260904.md` §6. Gate: `K3S3_PREREG_GATE_20260904_agy.md`.

K3S3_CHECK_SHEET_COMPLETE
