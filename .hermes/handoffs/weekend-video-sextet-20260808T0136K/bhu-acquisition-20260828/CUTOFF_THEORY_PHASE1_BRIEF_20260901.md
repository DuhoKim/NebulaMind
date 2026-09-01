# Cutoff theory — Phase 1: derive the window from the causal condition (Tori, 2026-09-01)

**To:** codex + agy, INDEPENDENT blind derivations. **Authority:** Duho RELAY "pursue the cutoff theory
(clamp overridden)." **This is original theory aimed at a publishable bar** — derive a number
non-circularly, or bound the irreducible ambiguity precisely. Strict, adversarial, equation-by-equation +
numerics. A tier-upgrade candidate returns to Duho; do NOT change tiers yourself.

## Where we are (from the calibration lane, `GAZTANAGA_CALIBRATION_RECONCILIATION_20260901.md`)

The Gaztañaga cutoff's *location* is fixed a priori (θ_cut≈60°, χ_§≈3.15 c/H₀, from H₀/Ω_Λ + r_S). But the
papers' *descriptions* of the cutoff are mutually inconsistent (sharp-k vs sharp-θ vs ℓ<5), the amplitude is
called a "mystery," so S₁/₂ was UNDETERMINED — it slid from 0 to ~35,000 μK⁴ by choice of the unsupplied shape.

**Phase-1 job: stop using the papers' ambiguous descriptions and instead DERIVE the cutoff from the model's
actual physical postulate — the causal boundary condition — then see whether S₁/₂ becomes a definite,
non-circular prediction.**

## The physical postulate to derive FROM (not the ambiguous "sharp cutoff" wording)

The model's real content is the **causal boundary condition**: the gravitational potential has no correlations
beyond the causal scale — `Φ(χ > χ_§) = 0`, an infrared cutoff in super-horizon inhomogeneities
(`2003.11544_clean.txt:241-265`; the smoothness/IR-cutoff language `:251-253`). Treat this as the axiom and
derive its consequences rigorously. Two readings are possible — DERIVE BOTH and say which the physics supports:
- **(R1) compact-support correlation:** the primordial potential two-point function ξ_Φ(r)=0 for r>χ_§. Then
  P_Φ(k) is the Fourier transform of a *truncated* correlation function — NOT a sharp k-step. Derive P_Φ(k)
  (or equivalently the induced C_ℓ window) from a scale-invariant ξ_Φ truncated at χ_§.
- **(R2) field boundary condition:** Φ itself vanishes outside a causal patch (a finite-box / spherical-domain
  eigenmode problem) → a discrete/should-suppressed set of low-k modes. Derive the induced low-ℓ suppression.

## The calibration (steps)

1. **Derive the window** W(k) or the modified C_ℓ^prim from (R1) and (R2). Show the math. Note that a real-space
   truncation and a k-step are NOT equivalent (the calibration lane proved this) — so this derivation is the
   point: which does the causal condition actually give?
2. **Normalize non-circularly:** fix the small-scale amplitude A_s to its Planck-measured value **at ℓ≈200–2500**
   (far above ℓ_cut≈3). Argue explicitly why using small-scale A_s to predict the LARGE-angle S₁/₂ is NOT circular
   with respect to the low-ℓ/S₁/₂ deficit it aims to predict.
3. **Propagate to the observed sky** via the standard transfer INCLUDING late-time ISW (use CAMB): observed
   C_ℓ = (truncated primordial) + ISW. The papers themselves warn ISW/lensing add large-angle power
   (`2003.11544_clean.txt:432-437`) — so the observed S₁/₂ has an ISW floor even if the primordial part is cut.
   Compute S₁/₂, C₂, C₃ for R1 and R2.
4. **Compare** to Planck measured (S₁/₂≈1150 μK⁴, `1906.02552_clean.txt:2416-2431`; >99.9% ΛCDM tail) and to
   ΛCDM (~34,900). State each number.

## Verdict (first line, one token)

- `CALIBRATED` — the causal condition (R1 or R2) UNIQUELY fixes the large-angle window, so with small-scale A_s
  the observed S₁/₂ (incl. ISW) is a definite number + threshold that Planck tests. State the number, the σ/p vs
  Planck and vs ΛCDM, and what would refute it. (This would be the original result — the papers never derived it.)
- `IRREDUCIBLE_AMBIGUITY_<name it>` — even deriving from the causal condition, a specific physical input remains
  genuinely free (name it precisely — e.g. the epoch defining χ_§, or the Φ↔ζ relation, or R1-vs-R2
  undecidability). This is a REFINEMENT of the calibration lane's "amplitude free": say exactly what survives.
- `PARTIAL_<...>` — a bounded prediction (e.g. an S₁/₂ range or an upper bound) that still constrains.

## Deliverable (`CUTOFF_THEORY_PHASE1_<seat>_RESULT.md`)

The derivation of W(k)/C_ℓ from R1 and R2 (full math); the non-circularity argument; the CAMB numerics with code;
the three-way S₁/₂ comparison; the verdict + threshold. Sources in `bhu-reading-20260823/sources/`:
`2003.11544_clean.txt` (the causal-condition paper — primary), `2104.00521`, `sym14091849`, `sym14101984`,
`2204.11608`, `2011.00910v4_fosalba_gaztanaga_clean.txt`, Planck `1906.02552v2_planck2018_isotropy_clean.txt`.

## Discipline

Non-circular is the whole game: derive the window from the causal axiom, not by fitting Planck's deficit. Every
number greppable in a source or reproducible from shown code. Absence claims: pattern + one missed class + what
you did. Do NOT change tiers. Blind — do not read the other seat's result.
- codex WRITE to `CUTOFF_THEORY_PHASE1_codex_RESULT.md`; agy OUTPUT to stdout.
