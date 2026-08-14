# LANA — BS-9 evaluated constants table (filled)

**Lana (science / claim-boundary seat), 2026-08-14.** Fills BS-9 of the preregistration register.
Aggregate/documentation work only: no sky data, no object rows, no positions, no images, no labels,
no sky statistic. Every number below carries its source file. **Verdict at the end is judged, not
tuned: both validity thresholds PASS, and they pass across the entire permitted range of `a`, so no
tuning was possible even in principle.**

## 1. Inputs, with sources and one input correction

- **Bound N = 130,076** — `TORI_BS1_CLOSURE_PACKET.md` (§ counted chain): displayed arithmetic
  `832,393 × 0.1823 × 0.8572 = 130,076.02307108`, rounded to 130,076. Quoted caveat honoured
  throughout: *"a counted preregistration feasibility LOWER bound, not 130,076 observed
  classifier-accepted real objects."* Direction note: every quantity in this table improves
  monotonically as true N exceeds the bound, so evaluating at the lower bound is conservative.
- **Measured a — input corrected to the authoritative receipt.** The brief pointed to
  `YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md` (100% sign accuracy, four S/N bins). Tori's BS-1
  packet marks that receipt **SUPERSEDED** (its population was inclination 0–60° only). The
  authoritative measurement is `YUI_INCLINATION_RETENTION_REMEASURE_20260812.md` (full
  Cut-6-admitted inclination range, uniform in cos i), which reports (its lines 11–14, 34):
  retention 10,349/12,000 = 86.24%; **accepted-sign accuracy 10,349/10,349 = 100.00%**; its printed
  one-sided lower 95% bound **99.974%**. Using the authoritative file removes a population mismatch
  (0–60° accuracy applied to a 0–69.3° population) that would otherwise have been embedded in this
  slot. Same headline number, correct population.
- **Conservative lower bound on a, method stated:** a measured 100% on finite n is treated as an
  upper edge; the one-sided 95% Clopper–Pearson lower bound for zero errors in n trials is
  a_low = 0.05^(1/n). With n = 10,349 accepted: **a_low = 0.05^(1/10349) = 0.999711**. (The
  receipt prints 99.974%; my exact CP recomputation gives 99.9711% — a 0.003-percentage-point
  discrepancy, immaterial to every output below at the printed precision; I evaluate at the more
  conservative 0.999711.)
- **Frozen formulas, quoted from `PREREG_LONGO_AMPLITUDE_TEST_20260812.md`:**
  - F-4: *"σ_D ≡ √(1/(3·N_accepted)); σ_ours ≡ 3·σ_D/(2a−1); σ_comb ≡ √(σ_pub² + σ_ours²) with
    σ_pub = 0.011."*
  - F-6: *"REPRODUCED-LONGO: permutation p < 0.001 AND sign per F-5 AND |Â_c − 0.0408| ≤ 3·σ_comb."*
  - F-7: *"the p < 0.001 requirement implies a one-sided detection floor of 3.09·σ_ours on Â_c …
    The REPRODUCED band's low edge is therefore inoperative below the floor — no Â_c below the
    evaluated floor can be called REPRODUCED regardless of the band, and the evaluated floor is
    printed in the results table."*

## 2. Arithmetic, shown for recomputation

At N = 130,076, a = 0.999711:

- σ_D = √(1/(3 × 130,076)) = √(1/390,228) = √(2.56260×10⁻⁶) = **1.60081×10⁻³**
- 2a − 1 = 0.999421
- σ_ours = 3 × 1.60081×10⁻³ / 0.999421 = 4.80244×10⁻³ / 0.999421 = **4.8052×10⁻³**
- detection floor (F-7) = 3.09 × 4.8052×10⁻³ = **1.4848×10⁻²**
- σ_comb = √(0.011² + 0.0048052²) = √(1.21000×10⁻⁴ + 2.30900×10⁻⁵) = √(1.44090×10⁻⁴)
  = **1.20037×10⁻²**
- 3·σ_comb = 0.036011 → REPRODUCED band = 0.0408 ± 0.036011 = **[0.004789, 0.076811]**
- expected true-null 3σ upper limit = 3·σ_ours = **0.014416**

## 3. The table (primary evaluation, plus the worst-permitted-a robustness row)

| Quantity | at bound N = 130,076, a_low = 0.999711 | robustness: a = 0.85 (HC-5 floor) |
|---|---:|---:|
| σ_D | 0.0016008 | 0.0016008 |
| σ_ours | **0.004805** | 0.006861 |
| σ_comb | 0.012004 | 0.012964 |
| Detection floor (F-7, 3.09·σ_ours) | **0.014848** | 0.021199 |
| REPRODUCED band (0.0408 ± 3σ_comb) | [0.004789, 0.076811] | [0.001908, 0.079692] |
| Effective REPRODUCED region (band ∩ ≥ floor, per F-7) | **[0.014848, 0.076811]** | [0.021199, 0.079692] |
| Expected null 3σ UL (3·σ_ours) | 0.014416 | 0.020582 |

Two consequences worth printing with the table: the F-7 rule bites exactly as designed — the band's
low edge (0.0048) is inoperative and the effective REPRODUCED region starts at the floor (0.0148);
and the expected null UL (0.0144, worst case 0.0206) sits far below 0.0408, so
REJECTED-AT-LONGO-AMPLITUDE remains comfortably decidable at this N.

## 4. Verdict against the validity ranges

| Validity condition | Value (primary) | Value (a = 0.85 floor) | Verdict |
|---|---:|---:|---|
| σ_ours ≤ 0.008 | 0.004805 | 0.006861 | **PASS — at both** |
| Detection floor ≤ 0.025 | 0.014848 | 0.021199 | **PASS — at both** |

**BS-9: PASS.** The pass is robust across the entire permitted attenuation range: even at the
prereg's own worst-permitted a = 0.85 (HC-5 floor), both conditions clear with margin (0.0069 vs
0.008; 0.0212 vs 0.025). No constant was, or could have been, tuned to produce this: the margins
exist at the most pessimistic admissible inputs.

## 5. Caveats that must travel with this slot

1. **a is synthetic-measured.** The authoritative re-measure itself warns (its line 20): high
   inclination costs retention, not accepted-sign accuracy, *on these synthetics*, and "does not
   establish realistic projected-arm blending." The operative a at run time comes from HC-1..5's
   hand-check on real images; if the hand-checked a lands anywhere ≥ 0.85, this table's PASS
   verdict is unchanged (robustness column). Below 0.85, HC-5 already declares
   INCONCLUSIVE-BY-POWER independently of this slot.
2. **N is a feasibility lower bound** (Tori's caveat quoted in §1); all entries move favourably if
   true accepted N exceeds it.
3. This slot evaluates constants; it asserts nothing about the sky, and no real galaxy was touched
   in filling it.

— Lana, 2026-08-14. BS-9 filled; Kun gates; Duho owns acceptance.
