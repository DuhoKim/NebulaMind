# New-physics program — Phase 1: a principled stochastic completion (Tori, 2026-09-01)

**Authority:** Duho RELAY "start the new-physics program (clamp overridden)." **Goal:** SUPPLY the piece the
theory lane proved is missing — a primordial-perturbation covariance consistent with the causal condition —
from a **principled physical argument, NOT a fit to Planck**, and determine whether it yields a definite,
calibrated large-angle CMB prediction (S₁/₂, C₂). This is original theory aimed at a publishable bar:
non-circular, defensible, or an honest bounded/negative result.

**Two seats, two DIFFERENT principled routes (this is a robustness test, not a blind-double-for-agreement):**
- **codex → maximum-entropy completion.**
- **agy → causal / retarded-Green-function completion.**
Do not read each other's result.

## Where the theory lane left it (`CUTOFF_THEORY_RESULT_20260901.md`)

The causal condition Φ(χ>χ_§)=0 is a FLUX condition (source Eq. 16, Φ=−∫√−g R⁰₀) that fixes the cutoff SCALE
(χ_§≈3.15 c/H₀ → θ_cut≈60°, via Eq. 17) but imposes NO constraint on the perturbation covariance. So the
large-angle amplitude is free: representative completions span S₁/₂≈6,200–22,300 μK⁴ (Planck ≈1,150; ΛCDM
≈34,900). Phase 1 asks: does a PRINCIPLED completion pin it?

## Non-circularity — the whole game (read twice)

- Fix the small-scale amplitude/tilt (A_s, n_s) to Planck's values measured at **ℓ≈200–2500** only. These modes
  sit at r≪χ_§, deep inside the causal patch, unaffected by the boundary → using them is non-circular w.r.t.
  the ℓ≲5 / S₁/₂ prediction.
- The completion's PRINCIPLE must be fixed a priori (max-entropy; or causal-Green from a standard initial state).
  **Nothing may be tuned to Planck's low-ℓ / S₁/₂ deficit.** If the only way to get a number is to fit the
  deficit, the verdict is `CIRCULAR_ONLY` — say so; do not fabricate a "prediction."

## codex — Route A: maximum-entropy completion

The least-biased Gaussian primordial field consistent with the constraints. For a Gaussian field the entropy is
∝ log det Σ, so the max-entropy completion is the covariance that **maximizes log det Σ** subject to:
(i) Σ reproduces the measured P(k) for k ≫ k_cut (small scales), and
(ii) the causal constraint at large scales — state precisely which you adopt and why (e.g. compact-support
ξ_Φ(r)=0 for r>χ_§, i.e. a band-limited/support-limited covariance completion; or the flux/boundary form).
This is a determinant-maximizing covariance-completion problem; it has a unique solution given the constraints
(max-ent adds no information). Derive Σ / the induced P(k) window, then C_ℓ, S₁/₂, C₂ via CAMB
(full transfer incl. ISW+lensing; A_s fixed at small scales). Show the math + code. If the causal constraint
admits no unique max-ent completion (e.g. the constraint set is not closed / determinant unbounded), say so.

## agy — Route B: causal / retarded-Green-function completion

The source itself points here: retarded Green functions φ(χ,t)=φ(χ−ct) solving the wave equation with the
causal boundary (`2003.11544_clean.txt:248`). Derive the induced primordial curvature/potential correlation
from **causal (retarded) propagation of fluctuations within the causal patch**, starting from a standard
initial state (e.g. adiabatic vacuum / white-noise source) on the finite causal domain bounded at χ_§. Obtain
the large-scale covariance / P(k) window, then C_ℓ, S₁/₂, C₂ via CAMB (same non-circular normalization).
Show the math + code. State every choice (initial state, boundary type) and whether the result is unique given
those standard choices.

## The Phase-1 question (both seats answer for their route)

Does your principled route yield a DEFINITE S₁/₂ (and C₂) prediction — a number that Planck tests — or does a
residual free choice remain even within your principled framework? Give the number(s), the three-way comparison
(your model / Planck ≈1,150 / ΛCDM ≈34,900), and a threshold (what measured S₁/₂ would refute it, at what σ if
you can define an ensemble).

## Verdict (first line, one token)

- `CALIBRATED_CANDIDATE` — your route gives a definite non-circular S₁/₂ + threshold. State it.
- `BOUNDED_<range>` — a principled range, not a point (e.g. an upper bound or an interval). State it.
- `STILL_AMBIGUOUS_<what>` — even your principled route leaves a specific free input; name it.
- `CIRCULAR_ONLY` — a number only obtainable by fitting Planck; the route does not predict.

## Deliverable (`NEWPHYS_PHASE1_<seat>_RESULT.md`; agy → stdout)

The derivation (full math), the non-circularity argument, the CAMB numerics + code, the three-way S₁/₂
comparison, the verdict + threshold. Every number greppable in a source or reproducible from shown code.
Absence/uniqueness claims stated with their limits. Do NOT change any tier — a calibrated candidate returns to
Duho after adversarial verification.

Sources: `2003.11544_clean.txt` (causal condition — Eq. 16 flux, :248 retarded-Green), `2104.00521`, `sym14091849`,
`sym14101984`, `2204.11608`, Planck `1906.02552v2_planck2018_isotropy_clean.txt` (S₁/₂ Table 11, `:2416-2431`).
