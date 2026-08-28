# REFEREE BRIEF — V33 and gain-control v2. Two of your findings were answered by withdrawal.

Subjects, both in scope:

- **`../PREREG_SUCCESSOR_DRAFT_V33_20260828.md`**, sha256
  `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`
- **`GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`** — **rewritten**, sha256
  `4cee2723bf8ce35d59f1f670bc9af11a57e25cc00a76192f04ae412dd97d6630`

**Verify both and state the comparisons.** Predecessor: V32,
`02a922167bcb77082a72ef0b3da0642975c39c7fef4ebd75ca28fd8d8a708e95` — NOT CLEAR from both of you.

`diff` V32 → V33: **the retitle, §2.7 line 390, and one §10 row.** Nothing else. All five
gain-control findings were repaired in the sidecar, which is not part of the draft's bytes.

## The document change — your only non-sidecar finding

GPT56-V32-6 / CODEX-V32-5: §2.7's closing sentences claimed the conditional-independence assumption
"no longer rests on nothing" immediately after correctly saying no evidence about it was measured.
**You were both right and the sentence is gone.** It now says the coupling **does not test**
conditional independence because handedness is unread, and that what it shows is a violation would
project through a stronger coupling in the retained mask — **raising the consequence of a violation,
not its likelihood**. Check that it no longer overreaches, and that it still does not read as grounds
to revisit a frozen cut.

## The sidecar — what changed, and two claims withdrawn outright

**1. The incompatible observables (GPT56-1, CODEX-2).** `γ̂ = β̂ᵀK` is now the **sole** acceptance
statistic; the two-hemisphere contrast and the 8-bin profile are **diagnostic displays that enter no
threshold**.

This costs the "ungameable binning" property, deliberately, and I want that decision attacked. The
reasoning is GPT56's: *"'Frozen and non-tunable' bin labels do not freeze those freedoms."* The
answer-determining freedoms were never in the bin labels — they were in allocation, weights,
covariance and support. **A hemisphere contrast with unfrozen sampling is more gameable than a
continuous slope with all of it frozen.** So the sampling contract is now frozen in full: background
manifest and allocation, injection grid, WLS design matrix with the intercept fitted and discarded,
inverse-variance weights, **background as the clustering unit with a CR2 covariance** (injections
sharing a background are not independent), support-refusal, and the exact receipt fields.
**Is that actually less gameable, or have I traded a visible freedom for several invisible ones?**

**2. WITHDRAWN — the no-flip claim (GPT56-2, CODEX-3).** "A systematic below 0.011 cannot flip the
verdict" was false. Replaced by a rule needing no such claim: the verdict must be **identical at both
endpoints** of the signed systematic interval `Γ = |μ_ceiling|·(|γ̂| + 1.96σ_γ)`, else
`INCONCLUSIVE-BY-SENSITIVITY-GRADIENT`, no retry. Consequence, not magnitude. Propagation now uses
absolute values throughout since `K` can be negative. **Attack the invariance rule itself.**

**3. The univariate slope (GPT56-3).** `K` is now a vector over all three quality variables —
`flux_ivar_r −0.270181`, `psfsize_r +0.483014`, `nobs_r −0.317419` — because they are correlated
(`flux_ivar_r`–`nobs_r` at **+0.7176**), so a univariate slope cannot stand in. The claim is narrowed
to the **first-order linear** part; nonlinearity, interactions and other position-coupled properties
are named as unbounded. **Recompute all three via `ref/gain_gradient_kernel.py` and `--self-test`.**

**4. `|μ|max` (GPT56-4, CODEX-3).** No longer called generous. Both point comparisons reproduce
(`0.070624`, `0.094962 ± 0.024`) but `0.10` exceeds the latter by only 5.3% and both are human-label
GZ1 statistics. `μ` is now defined operationally on the accepted-sign population; the ceiling is
`max(0.10, |μ_obs|)`, produced automatically and receipted **before any operator sees a result**.
**Is `max(0.10, |μ_obs|)` sufficient, or does the ceiling still do work it cannot bear?**

**5. WITHDRAWN — the blindness claim (GPT56-5, CODEX-4).** "The real sky is simply absent" was false;
the inputs are real DR10 backgrounds. Blindness is now **earned** by the paired construction
`χ(b ⊕ i) − χ(b)`, which cancels background chirality, rather than asserted. **And the provenance bug
you found is fixed**: "non-sample" now means outside the **full 65,060 parent** and the footprint,
not outside the 49,211 retained mask — which had permitted all 15,849 quality-excluded objects.
**Check the paired construction really does cancel background chirality**, and that the manifest
being frozen before any recovery exists is stated tightly enough.

## Attack it

1. **Is the sidecar now a freezeable control, or still not?** It remains DESIGN, defined, **UNFILLED**
   — `β` is unmeasured and nothing is filled against it. Say plainly whether the remaining defects
   block *freezing* or only *filling*.
2. **Does V33 credit the control with anything it has not produced?** That is the shape you caught at
   line 120 and again at §2.7.
3. Run `prereg_lint.py`, its `--self-test`, `prereg_trace.py --check` and its `--self-test`.
4. §1 scope and §2.7 line 384 must remain byte- and position-identical to V30. Verify.

## Standing state

**BS-2a DESIGN/UNFILLED**, code gate at round 5 NOT CLEAR ×2 — both findings since repaired, with
the robustness limit now recorded in the module docstring. **One of fifteen class-P slots filled.**
BS-2v UNRESOLVED; rows C2 and E cannot run; Stage P `SUPERSEDED`; **BS-6 and the first image byte
remain blocked.** Non-sample DR10 cutouts are authorised for instrument characterisation only.

Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

`V33_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`. **Judge independently; do not converge.**
