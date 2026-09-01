# Gaztañaga causal-horizon cutoff — CALIBRATION derivation brief (Tori, 2026-09-01)

**To:** codex + agy, INDEPENDENT blind derivations. Do NOT read each other's result. **Authority:** Duho
RELAY "calibrate the Gaztañaga cutoff (clamp overridden)." **This is ORIGINAL THEORY, not an audit** —
derive a number, or prove the number is not derivable. **Strict model (per Duho): adversarial,
equation-by-equation; derive, do not order-of-magnitude scope.** Any tier outcome returns to Duho.

## The state we are trying to change

The Gaztañaga causal-horizon CMB cutoff (entries 23/24/25/26/27) is tiered **QUALITATIVE-DIRECTIONAL**:
the cutoff **scale** is predicted a priori (ℓ_cut ≈ 3, θ_cut ≈ 60°, fixed from the background H₀/Ω_Λ via the
causal/Schwarzschild horizon r_S = 2GM, published before the CMB check), but the papers supply **no
amplitude / C_ℓ threshold**, so it is scale-level, not calibrated. **Your task: derive the amplitude —
turn "there is a cutoff at 60°" into a quantitative, falsifiable prediction — or show it cannot be derived
from the model.**

## Sources (all pinned; read them adversarially)

`bhu-reading-20260823/sources/` :
- **23** `2003.11544_clean.txt` (Gaztañaga 2020, "The size of our causal Universe")
- **24** `2104.00521_clean.txt` (Gaztañaga 2022, "A peek outside our Universe")
- **25** `sym14091849_clean.txt` (Gaztañaga 2022, "The Black Hole Universe, Part I")
- **26** `sym14101984_clean.txt` (Gaztañaga 2022, "The Black Hole Universe, Part II")
- **27** `2204.11608_clean.txt` (Gaztañaga 2022, "How the Big Bang Ends Up Inside a Black Hole")
- context: `2011.00910v4_fosalba_gaztanaga_clean.txt` (Fosalba–Gaztañaga 2021)
- **Planck data for comparison:** `1906.02552v2_planck2018_isotropy_clean.txt` (Planck 2018 VII isotropy &
  statistics — carries the measured S₁/₂, the low quadrupole C₂, and the large-angle deficit significance).

## Step 1 — pin the EXACT cutoff prescription (adversarial read)

From the sources, extract precisely what the model predicts about large-angle power. Do NOT assume; quote:
- Is the cutoff a **sharp** truncation or a smooth suppression? In comoving **k** (P(k)=0 for k<k_cut) or in
  **angle/multipole** (C(θ)=0 for θ>θ_cut; C_ℓ=0 or suppressed for ℓ<ℓ_cut)?
- What FIXES k_cut / θ_cut / ℓ_cut, exactly, from H₀/Ω_Λ/r_S? Reproduce that derivation.
- Does the model say anything about the **amplitude/normalization** of the surviving power, or only the
  location of the cutoff? (This is the crux: if only the location, the amplitude may be un-fixed.)

## Step 2 — derive the calibratable observable

The cleanest calibration target is the **large-angle two-point angular correlation C(θ)** and the **S₁/₂
statistic**, S₁/₂ = ∫_{-1}^{1/2} [C(θ)]² d(cosθ), which Planck measures and which ΛCDM finds anomalously low.
- **IF** the model implies C(θ) ≈ 0 for θ > θ_cut ≈ 60° (a hard causal cutoff), then S₁/₂ is directly
  predictable and small. Compute the model's predicted S₁/₂ (and the quadrupole C₂) from a standard ΛCDM
  primordial+transfer spectrum truncated by the model's prescription. You MAY write and run code (numerical
  C(θ) from C_ℓ, or C_ℓ from a truncated P(k)). Show the calculation.
- Compare THREE numbers: (a) the model's predicted S₁/₂ (and C₂); (b) Planck's MEASURED S₁/₂ and C₂ (from
  1906.02552); (c) ΛCDM's expected S₁/₂ and the fraction of ΛCDM realizations below the observed value
  (the anomaly significance Planck reports). State each with its source line.

## Step 3 — the threshold and the verdict

- **The calibration:** state the predicted value + a **threshold** — what measured S₁/₂ (or C₂) would
  REFUTE the model, and at what significance the current Planck value confirms/contradicts it. A calibrated
  falsifier needs: a number the model predicts, a threshold, and a measurement that could cross it.
- **VERDICT (first line, one token):**
  - `CALIBRATED` — you derived a definite predicted S₁/₂ (or C₂ / low-ℓ) amplitude + threshold that Planck
    tests. State the number, the threshold, the σ/p, and what would refute it.
  - `UNDETERMINED_NEEDS_<x>` — the model fixes the cutoff LOCATION but NOT the amplitude/shape (the
    surviving-power normalization or the sharp-vs-smooth choice is free), so S₁/₂ is not derivable without
    an extra assumption the model does not supply. Name the missing piece. (This is the RQ-B-style honest
    negative — do NOT fabricate a number.)
  - `PARTIAL_<...>` — a bounded/conditional result; state exactly what is and isn't fixed.

## Deliverable (`GAZTANAGA_CALIBRATION_<seat>_RESULT.md`)

1. The exact cutoff prescription, quoted with `file:line` receipts.
2. The derivation of S₁/₂ (and C₂) — every step, with the code if you ran it, and the three numbers (model /
   Planck-measured / ΛCDM-expected).
3. The verdict token + the threshold + what would refute the model.
4. Every number greppable in a source or reproducible from your shown calculation. Absence claims: pattern +
   one missed class + what you did about it. Do NOT change any tier — a calibrated outcome returns to Duho.

## Method notes

- Non-circular is essential: the cutoff SCALE was fixed a priori (good). The amplitude must be derived from
  the model + standard cosmology, NOT tuned to match Planck's deficit. If the only way to get the amplitude
  is to fit Planck, that is UNDETERMINED, not CALIBRATED — say so.
- codex WRITE to `GAZTANAGA_CALIBRATION_codex_RESULT.md`; agy OUTPUT to stdout. Blind — do not read the other.
