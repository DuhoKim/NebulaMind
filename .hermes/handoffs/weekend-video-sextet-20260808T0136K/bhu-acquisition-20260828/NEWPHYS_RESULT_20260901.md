# New-physics program — result (Tori, 2026-09-01)

Duho RELAY "start the new-physics program (clamp overridden)." Goal: supply, from a **principled** argument,
the stochastic completion the theory lane proved is missing, and see if it calibrates the Gaztañaga cutoff.
Two independent principled routes + adversarial verification.

## Verdict — STILL_AMBIGUOUS. The cutoff cannot be calibrated even with a principled completion. Tier UNCHANGED.

| seat / route | verdict |
|---|---|
| codex — maximum-entropy | `STILL_AMBIGUOUS_IR_NORMALIZATION` (with a non-existence proof) |
| kimi — adversarial verifier | `STILL_AMBIGUOUS` (confirms codex; agy's uniqueness undischarged) |
| agy — causal/retarded-Green | `CALIBRATED_CANDIDATE` — **REFUTED (over-reach)** |

## The proof (codex, verified by kimi) — the IR normalization is irreducibly free

- **Maximum entropy has no maximizer.** Given any feasible compact-support covariance ξ₀ (ξ=0 for r>χ_§)
  matching the measured small-scale P(k), add λ·q where q is the autocorrelation of a smooth compactly-
  supported function: q keeps support ≤ χ_§, Q(k)=|g̃(k)|²≥0 decays super-algebraically (small-scale band
  untouched), and log det Σ_λ → +∞ as λ→∞. So no determinant-maximizing completion exists; entropy cannot
  select the window.
- **Paley–Wiener:** exact small-scale power-law equality is incompatible with compact support (compact support
  ⇒ entire FT; a scale-invariant power law is not). The constraint set is "fat, not a point."
- The causal condition bounds the support *scale* (χ_§→60°) but says nothing about the *profile* within → the
  large-scale amplitude / IR variance is a free input. **Not calibratable without adding new information.**

## agy's CALIBRATED refuted (its third over-reach this session)

agy imposed ONE completion — white noise on a top-hat causal patch — and called it "unique **given the
standard choice** of initial state" (a conditional that concedes the ansatz is chosen, not derived). kimi:
top-hat vs any smooth compact window of the same support gives a different |W̃|² and a different S₁/₂; agy's
S₁/₂≈9,913 (ensemble mean 16,919) is **one point inside codex's 6,230–22,327 family**, not a forced output.
Its Planck ~2σ-vs-ΛCDM ~3σ tail comparison evaluates one arbitrary member, irrelevant to uniqueness.
(Pattern: theory lane — agy misread Φ as a field BC; here — agy calls one ansatz "unique." codex+kimi reliable.)

## The semi-quantitative finding worth keeping

Across every principled/natural completion (codex R1/R2: 6,230–22,327; agy causal-Green: 9,913, ensemble
16,919), the causal cutoff **suppresses** large-angle power relative to ΛCDM (S₁/₂≈34,900) — the right
direction — but lands at **S₁/₂ ~ 6,000–22,000 μK⁴, still ~5–20× ABOVE Planck's anomalous ~1,150**. So the
cutoff moves toward the S₁/₂ deficit but does not reach it, and the exact value is completion-dependent. Even
agy's most favourable completion leaves the observed value at ~2σ, not a fit. Non-circular throughout
(A_s, n_s fixed at ℓ≈200–2500; ISW included).

## Conclusion — the program is pursued to its honest end

Calibrating the Gaztañaga cutoff into a falsifier would require a **forced IR normalization / initial-condition
principle** that neither the causal condition nor maximum entropy provides. That is genuinely new physics that
does not exist in — and is not derivable from — the published model. **The cutoff is robustly SCALE-FIXED but
AMPLITUDE-FREE**: a real a-priori 60° prediction (its directional content), not a calibrated falsifier, and it
cannot be made one from this model. **Tier UNCHANGED — 23/24/25/26/27 stay QUALITATIVE-DIRECTIONAL.** No
bibliography tier edit.

Seat files: `NEWPHYS_PHASE1_{codex,agy,kimi}_RESULT.md`; brief `NEWPHYS_PHASE1_BRIEF_20260901.md`.
Method note: the reliable finding required codex's proof + kimi's independent check; agy's confident CALIBRATED
was the third instance where verifying against math/source, not a seat's token, was decisive.
