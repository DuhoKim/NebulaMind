# Cutoff theory — lane result (Tori, 2026-09-01)

Duho RELAY "pursue the cutoff theory (clamp overridden)." Original-theory attempt to derive the cutoff's
large-angle CMB amplitude from the model's causal boundary condition and thereby calibrate it. Blind
derivations: codex (`CUTOFF_THEORY_PHASE1_codex_RESULT.md`, 144 lines, CAMB) + agy (`..._agy_RESULT.md`,
107 lines, CAMB). **They split; the source settles it in codex's favour.**

## Verdict — IRREDUCIBLE_AMBIGUITY (the causal condition does NOT calibrate the cutoff). Tier UNCHANGED.

| seat | verdict |
|---|---|
| codex | `IRREDUCIBLE_AMBIGUITY_STOCHASTIC_COMPLETION` |
| agy | `CALIBRATED` (S₁/₂=43,786 μK⁴, "rigidly falsified") — **REFUTED, see below** |

## Why codex is right — verified against the primary source

The split turned on ONE physical question: what is Φ in the causal condition Φ(χ>χ_§)=0?
- **agy** read it as a Dirichlet boundary condition on the scalar potential *field*, discretising primordial
  perturbations into spherical-Bessel eigenmodes on a ball of radius χ_§ → a "unique" S₁/₂=43,786.
- **codex** read it as an *integrated gravitational flux* term.
- **The source (`2003.11544_clean.txt`, verified directly):** Eq. 16 (`:235`) is **Φ = −∫_M √−g d⁴x R⁰₀** — a
  4-volume integral of R⁰₀, i.e. a flux, NOT the fluctuation field. Line `:257-260`: "Φ(χ>χ_§)=0 in Eq.16, so
  that there is no flux (i.e. no effects of gravity) beyond the causal scale," and this **implies Eq. 17**
  (Λ/8πG = ⟨ρ+3p⟩_§/2) — it is used to fix the causal SCALE, not to discretise a perturbation field.

**agy's CALIBRATED is refuted on a source misreading:** Φ is a flux integral; there is no Dirichlet
field-boundary problem, so the spherical-Bessel mode discretisation (and its 43,786) does not follow.

## And even granting a mode picture, the completion is free (independent confirmation)

codex proved, and the two seats' own numbers demonstrate, that the boundary condition does not fix the
perturbation covariance:
- **R1** (compact-support correlation ξ_Φ(r)=0 for r>χ_§) fixes only the *support*, not the interior taper;
  scale-invariance makes ξ IR-divergent (only a renormalised difference is defined). codex's literal
  log-truncation gives S₁/₂ ≈ 22,327 μK⁴ — one convention, not a unique prediction.
- **R2** (eigenmodes) fixes the mode *functions* but not their *occupations* ⟨a a*⟩. Different occupation/
  boundary choices give wildly different S₁/₂: **codex 6,230 & 14,002; agy 43,786** — same condition, 3–7×
  apart. That spread IS the free stochastic completion.
- The source itself concedes patch differences "could be matched" but gives no matching law / initial-condition
  model (`2003.11544:248-253,463-466`).

## Numbers (non-circular: A_s fixed at ℓ≈200–2500, full CAMB incl. ISW+lensing)

- ΛCDM S₁/₂ ≈ 34,900 μK⁴ (both seats); Planck measured ≈ 1,142–1,209 μK⁴ (`1906.02552:2416-2434`; >99.9% ΛCDM tail).
- Representative model completions span **≈6,230 → 22,327 μK⁴** (R2-4.493 → R1-log) — all still **far above** the
  Planck ≈1,150 anomaly, and not unique. No single number, no threshold, no σ (codex correctly refused a σ:
  it needs the specified ensemble = the missing completion).

## What this means (the honest, precise negative)

Pursued rigorously, the Gaztañaga causal boundary condition **fixes the cutoff SCALE (60°, via Eq. 17) but
imposes NO constraint on the perturbation covariance** — so the large-angle amplitude / S₁/₂ is genuinely free.
Calibration is impossible not for lack of effort but because the theory contains no initial-condition /
perturbation model. A real calibration would require *new physics beyond the published papers*: a specified
primordial covariance (edge taper for R1, or mode occupations + patch geometry + observer position for R2), i.e.
a full stochastic completion. **Tier UNCHANGED — 23/24/25/26/27 stay QUALITATIVE-DIRECTIONAL.** The cutoff
remains a genuine a-priori *scale* prediction; it is not, and cannot from this model be made, a calibrated
falsifier. No bibliography tier edit.

## Method note
agy's error is instructive and worth keeping: reading a flux/boundary term as a field Dirichlet condition
manufactures a spurious "unique" prediction. The guard is the one that settled it — verify the disputed object
against the primary source, don't take a seat's confident token. codex + source, not a seat vote, decided this.
