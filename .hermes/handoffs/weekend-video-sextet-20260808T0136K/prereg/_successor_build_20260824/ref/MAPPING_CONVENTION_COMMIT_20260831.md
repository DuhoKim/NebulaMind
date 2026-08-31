**STATUS: COMMITTED BLIND — the mapping-A free conventions, fixed BEFORE any sweep runs
or any verdict is seen (no invariance receipt exists; γ̂ is unmeasured), under the same
instrument as `DRAW_MECHANICS_COMMIT_20260830.md`. FILED to the principal for
confirmation as an extension of his option-A ruling of 2026-08-29 — the ruling fixed the
model's SHAPE; CODEX's convention pass (gates/CODEX_MAPPING_CONVENTION_20260831.md,
MAPCONV-V1, DIVERGENT ×3) correctly found these four parameters LEFT OPEN by it, not
ruled; they are fixed here with rationales-why-not-shopped, and `mapping_id` transitions
only on the principal's confirmation.**

# The mapping-A conventions — chosen by rule, not by search

| convention | committed value | rationale — why this value could not have been shopped |
|---|---|---|
| the intercept `a₀` | **`cal["a_hat"]`** — the measured global accuracy | the ONLY preregistered accuracy scalar in the calibration object; any other intercept is a new number with a search space; the ruling wrote a single `a₀`, so the piecewise per-bin alternative would change the ruled shape |
| the centering `c̄` | **the unweighted mean of `mask.c` over the analysis population** | the ruling's expression centres on the tested population's `c̄`; the mask IS the tested set; the unweighted mean carries no tunable weight |
| out-of-domain accuracy | **clamp into `[0.5 + 1e-9, 1.0]`, per-call clip fraction REPORTED** | an accuracy has physical support (0.5, 1]; production's `inject_signs` REFUSES outside it, so out-of-domain linear values have no production meaning; a crash would turn a ratified grid point into a non-verdict and defeat the sweep's every-cell contract — the clamp restricts the field to the model's support and the diagnostic makes heavy clamping visible per γ |
| the `cal′` transform | **per-bin means of the SAME field the signs saw; per-bin lower-bound margins preserved; `sigma_a`/`cov_a` unchanged; an empty bin keeps its measured value** | the joint ruling requires amplitude and significance to MOVE TOGETHER: the significance path consumes per-bin calibration, so the minimal faithful transform applies the identical accuracy field bin-aggregated in the calibration's own per-bin shape; margins are the measurement's uncertainty and a hypothesized field shift does not change measurement error; an empty bin has no perturbed objects, so nothing moves |

**Binding:** `ref/gain_mapping_a.py`'s `identity_record()` gains this file's sha256, so a
change to any convention is an identity change. **Every value above is frozen by this
commitment: a later change is a post-hoc edit and says so.**
