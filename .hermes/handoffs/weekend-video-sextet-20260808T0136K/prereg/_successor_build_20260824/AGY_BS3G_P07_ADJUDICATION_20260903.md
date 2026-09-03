ACCESS_SHA=915bc8c683cea5a42588a28d7fbb670ccf768fd7914a0469eb688374ab1ce21e
READING: i

**Adjudication of P07**
The text mandates **Reading (i)**: an `INCONCLUSIVE-BY-CALIBRATION` cell IS a recordable outcome of the sweep. The matrix cell must record that token, the sweep must continue, and the reduction treats it per the ruled failure consequence (resulting in a `FAILED` receipt).

**Evidence from the Frozen Bytes:**
1. **It is a run outcome, not a refusal:** V136 §5 (line 559) explicitly states: "A pre-unblinding numerical failure does not void the run — it terminates it through the pre-statistic inconclusive codes above". Furthermore, line 479 confirms: "If any bin's a_LB_b < 0.85, it emits an immediate pre-unblinding INCONCLUSIVE-BY-CALIBRATION and the run halts." Thus, it is a valid verdict token.
2. **The "real gate" includes it:** `OPEN_QUESTION_T_COMPLETENESS.md` (lines 48-49) ruled option (b) real gate: "each allowed perturbation is mapped through accepted signs, calibration and the production permutation record".
3. **No restriction to numeric tokens:** V136 §11 (line 1526) states that the `draw_verdict_digest` takes "one token per cell, \n-separated, no trailing separator, UTF-8". V136 §5 (line 507) defines the three numeric verdicts (which include `INCONCLUSIVE`), but §11 never restricts the matrix cells to *only* these three. Codex hallucinated this restriction in `gates/bs3g_producer.py` (line 35), causing the script to improperly refuse the outcome.
4. **The matrix evaluates to FAILED:** V136 §11 (line 1530) states: "There is no ordering: invariance_outcome is HELD if and only if every cell (i, j) equals its own draw's (i, j₀) cell, and FAILED otherwise". Because `INCONCLUSIVE-BY-CALIBRATION` differs from the baseline cell, the reduction yields `FAILED`.
5. **The consequence is a true record:** V136 §7 (line 939) states: "a verifier-valid FAILED receipt is a TRUE RECORD THAT BLOCKS — it is the pre-stated evidence-about-the-design outcome and goes to the principal". It is not a missing receipt; it is a valid failure receipt.

**Logical Constraints:**
- A "three numeric tokens" cell set can represent `INCONCLUSIVE` (as it is one of the three defined at line 507), but it **cannot** represent `INCONCLUSIVE-BY-CALIBRATION` or `INCONCLUSIVE-BY-POWER`. Codex's enforcement of `TOKENS` forced a script crash where the protocol required a token.
- The record's gamma-extreme accuracy **predictably breaches 0.85 for ANY realistic fixture**. The ruled `OPEN_QUESTION_GAIN_SIGN_MAPPING.md` option A uses `a(c) = a₀ + γ·(c − c̄)`. At the extremes of the ratified range (`γ = ±0.25`), with `c` spanning a range of ~1.0, the term `γ·(c − c̄)` shifts accuracy by roughly `±0.125`. For an instrument with an `a_hat` of ~0.88, `0.88 - 0.125 = 0.755`. Since `a_lb_b` is strictly lower than `a_hat`, it inevitably breaches the `0.85` floor. The ruled range of `±0.25` was never mathematically compatible with the real gate's `0.85` floor.

**What Hwao should do next:**
Hwao must update `gates/bs3g_producer.py` to remove the hallucinated restriction that cells may only contain the three numeric tokens, and update `ref/gain_counterfactual_path.py` so that it returns `INCONCLUSIVE-BY-CALIBRATION` as the cell's verdict rather than raising it as `PathRefusal [P07]`. The sweep must be allowed to complete and emit the `FAILED` receipt. This receipt will rightfully block BS-3g and correctly route the parameter contradiction (the ±0.25 sweep range vs. the 0.85 calibration floor) to the principal as evidence about the design.

SEAT: AGY
VERSION: BS3G-P07-ADJUDICATION-V1
READING: i
OPEN_FOR_PRINCIPAL: yes
