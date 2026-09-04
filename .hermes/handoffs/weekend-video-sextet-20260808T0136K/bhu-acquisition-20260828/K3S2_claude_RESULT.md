K3S2_EXCHANGE_N2_RESTORED

# K3 step 2 — route-1 seat "claude" result

Governing document: `K3S2_EXCHANGE_PREREG_20260904.md` (frozen V2). Script: `K3S2_claude_exchange.py`,
sha256 `9c9592cec6dbb7ea6a5faec96e52d9a28683b6bbbc1f23fb93abaef1afd5f18e`; executed output
`K3S2_claude_exchange.out`, sha256 `a3e614973336e6a0745316d5f915cb77322c8a0f796c03cd7527df92e78ebb1a`.
Written blind: no `K3S2_codex*`, `K3S2_ROUTE2*`, `K3S2_RESULT*`, `K3S2_CHECK*` or `K3S2_RECONCIL*` file was opened
before this file was frozen.

## Class

**K3S2_EXCHANGE_N2_RESTORED**, with a coefficient that is **negative** and **not universal**.

## The finding

An `n²` term **does** return, and it comes from exactly the place the critic note named: the Fock (exchange)
contraction of the coincident-point quadratic operator. It is not the term either printed closure asserts.

With the medium one-body density matrix written, after angular averaging, as `ρ_med = A·1 + B·β`:

| quantity | value |
|---|---|
| direct (Hartree) contraction | `0` (unpolarized) |
| exchange (Fock) contraction | `−3(A² + B²)` |
| `A` | `n/4` (fixed by `Tr ρ_med = n`) |
| `B` | `∫ d³p/(2π)³ (m/2E)(f₋ + f₊)`; `→ n/4` non-relativistically, `→ 0` ultrarelativistically |
| exchange, non-relativistic | `−(3/8) n²` |
| exchange, ultrarelativistic | `−(3/16) n²` |
| contact (self) term | `(3/4) n`, i.e. `(3/4) n/V` coarse-grained over the cell — K3 step 1's term |

So the density power is `n²`, but the coefficient runs with `m/p_F` between `−3/8` and `−3/16` and is negative in
both limits. The bounce chain's own regime is extreme density, hence ultrarelativistic, hence `−3/16`.

## Against the two printed relations

C6 re-derived, independently of step 1, that `½ s_ij s^ij = |s⃗|²` exactly (ratio printed by the script, and the
same under the opposite Levi-Civita sign convention), so both printed relations are values of one quantity and are
compared to the same number.

- printed spin-fluid `⅛ n²` (entry 10 L121; Gasperini 1986 `σ² = ℏ²⟨n²⟩/8`): **not reproduced.** Opposite sign; the
  ultrarelativistic magnitude `3/16` is one and a half times `1/8`.
- printed Dirac `¾ n²` (entry 10 L113): **not reproduced.** Opposite sign; the non-relativistic magnitude `3/8` is
  exactly half of `3/4`.

Neither numeral entered the computation (C8: recomputing with both replaced by free symbols is byte-identical).

## Controls — all eight, by name

`C1_DIRECT_ZERO=PASS`, `C2_POLARIZED_N2_QUARTER=PASS`, `C3_CLASSICAL_LINEAR_IN_N=PASS`, `C4_EXCHANGE_DELETED=PASS`,
`C5_UNITS_RESTORED=PASS`, `C6_MAP_DERIVED=PASS`, `C7_ANTIPARTICLE_SECTOR_LIVE=PASS`,
`C8_NO_PRINTED_COEFF_INPUT=PASS`. `MISSING_CODES=none`, `ALL_CONTROLS=PASS`.

C4's prediction was written into the script header before running: deleting antisymmetrisation must leave only the
direct product, which is zero for the unpolarized state. Observed: `0`.

## Residual freedom, stated exactly

1. **The coefficient is not a number.** It depends on `m/p_F` through `B`; only the two limits are universal. No
   single constant multiplies `n²` for the audited object across the regimes the bounce papers span.
2. **Two distinct objects share the name `⟨s²⟩`.** The local coincident-point operator expectation (what enters
   `U^ik` and therefore Einstein–Cartan) carries the `n²` exchange term reported here. The cell-averaged square
   `⟨S_a S_a⟩/V²` — K3 step 1's object — has both its contact and its exchange contributions falling as `1/V`,
   because the exchange hole has finite range. The sources do not say which they mean. This is a real freedom in the
   record, not in the calculation.
3. **The subtraction is a choice.** Medium normal ordering is declared and used throughout; a different
   renormalisation of the coincident-point product would shift the state-independent part, though not the `n²`
   coefficient reported here, which is built from `ρ_med` alone.

## What this does and does not do to K3 step 1

It does **not** overturn `CLOSURE_SCALING_FAILS` for the object step 1 audited. It answers the objection the critic
note raised: the coincident-point exchange contraction of the correct local operator does produce an `n²` term, so
the surviving objection was well founded — but the term it produces has the **wrong sign** for the bounce chain and
a magnitude that matches neither printed coefficient, and it is regime-dependent rather than universal.

No tier, warrant token, standing or stamp is moved here; that is Duho's.

K3S2_CLAUDE_SEAT_RESULT_COMPLETE
