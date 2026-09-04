ACCESS_SHA=cf51fdc7081a8f04bb7939905a9852907dbbf5c8157cf20544591ff7a1e6af7c
GATE=PREREG_SOUND_WITH_REPAIRS

1. 
Quote: mass relation `M = (4/3)π χ*³ ρ₀` at entry 56 `gaztanaga_mass_mnras_clean.txt` **L143**
Defect: Strict numeral tracing failure; the exact text at the cited line contains OCR artifacts (`43` and `3`) rather than the stated numerals.
Exact replacement wording: mass relation `M = 43π χ 3 ρ0` [sic] at entry 56 `gaztanaga_mass_mnras_clean.txt` **L143**

2. 
Quote: - **C6 — non-circularity.** No CMB statistic may enter the derivation; the seat asserts the prediction is complete and printed **before** the estimator is called. Exact assertion: `C6_PREDICTION_BEFORE_DATA=PASS`.
Defect: The control is merely an unfalsifiable promise ("the seat asserts") that does not structurally prevent a seat from peeking at the CMB data during derivation.
Exact replacement wording: - **C6 — non-circularity.** No CMB statistic may enter the derivation; the prediction script must execute to completion and save its output before a separate script loads the Planck map or calls the estimator. Exact assertion: `C6_PREDICTION_BEFORE_DATA=PASS`.

3. 
Quote: 1. **K4_BOUNDARY_INERT** — the perturbed junction yields an F1/F2-type condition; no low-`ℓ` modification; the freedom map's residual closes. Report which of F1/F2 and the derivation.
Defect: Declares a standing outcome (closing the residual) inside an outcome class.
Exact replacement wording: 1. **K4_BOUNDARY_INERT** — the perturbed junction yields an F1/F2-type condition; no low-`ℓ` modification. Report which of F1/F2 and the derivation.

Justification: The pre-registration's falsifier design, outcome classes, and executable discipline are strong and unsoftenable. However, it fails the strict numeral tracing criterion due to OCR drift in the source text, relies on an unenforceable seat promise for its non-circularity control instead of structural separation, and violates scope rules by declaring a standing outcome inside class 1.

Given the freedom map already established that even an optimal explicit cutoff cannot raise the phase (b) percentile above ~3%, spending 10 to 14 seat-days deriving a boundary condition that can at best replicate this insufficient suppression is not worth doing.

K4_PREREG_GATE_COMPLETE
