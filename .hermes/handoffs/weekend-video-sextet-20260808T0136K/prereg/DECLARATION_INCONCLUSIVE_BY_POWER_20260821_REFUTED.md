# DECLARATION — INCONCLUSIVE-BY-POWER, before unblinding

Hwao, 2026-08-21 18:19 KST. **Draft for adversarial gating. Not effective until gated and accepted by Duho.**
Authorised in direction by Duho: *"go ahead with inconclusive-by-power and scope the successor."*

## The declaration

Under **F-6**, the outcome of the Longo-amplitude test on the frozen DR10.1-South parent
(BRICKID 1..121000, 208,407 dered Cut-5 rows) is declared

> **INCONCLUSIVE-BY-POWER — declared before unblinding. No run.**

No dipole is estimated. No aggregate over chi is computed. The four decision regions are not
entered, and no statement is made about Longo's claim in either direction.

## Grounds

F-6 defines this outcome as *"declared before unblinding if the section 5 power gate fails; no
run."* Section 5 requires **power >= 0.95** at `A_eff = (2a-1)*0.0408`.

That bar is unreachable on this footprint, at any acceptance and at any label accuracy:

| quantity | value |
|---|---|
| noncentrality required for 0.95, one-sided at alpha = 0.001 | `4.7351` |
| full-parent geometric noncentrality bound | `4.4888` |
| one-sided power at the most favourable `a = 1` | `0.9187` |
| one-sided power at the frozen floor `a = 0.85` | `~0.52` |

Because `SSE(S) <= SSE(P)` for every subset S of the parent, the bound holds for **every possible
accepted sample**, not merely for a particular acceptance rate. There is no version of this run
that clears the gate.

Evidence: `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md` (Revision 3), gated twice —
`GATE_FOOTPRINT_GEOMETRY_20260821.md` (HOLD) and `GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md`
(HOLD, not refuted; independent all-row recomputation, first-principles permutation algebra, and
Longo's own footprint reconstructed from his published supplement).

## Why this declaration does not violate F-9

F-9 voids the run if any parameter changes after a real-sky statistic exists. **Every number
grounding this declaration is computed from positions alone.** No chi value, sign, or aggregate
was read; both gates certified this in their boundary statements, and neither opened
`/Users/duhokim/NebulaMindData/chi_dr10_south/`.

The geometry was therefore knowable before the first galaxy was measured. A decision that cannot
depend on the outcome cannot be an outcome-driven decision, which is the only thing F-9 exists to
prevent. Declaring the study underpowered is also the conservative direction: it forecloses
REPRODUCED-LONGO, the result a biased actor would want.

## The reading of section 5 being used, stated openly

The re-gate identified two readings of HC-6 and we are deliberately refusing one.

- **Literal-algorithm reading.** HC-6 says re-evaluate *by the same method* the pinned harness
  used, substituting realized `N` and the lower-bound `a`. The pinned harness
  (`spike/sim_power.py`) draws `costheta` uniformly on `[-1,1]` and assumes
  `mean(cos^2) = 1/3`. Re-run literally at realized `N`, that calculation **could still report
  PASS** — because it never reads the footprint at all.
- **Scientific reading.** "Power" means the power of frozen F-3 on the accepted fixed positions.
  On this reading the gate fails and cannot be made to pass.

**We refuse the literal reading**, and the reason is not convenience: a formal PASS produced by a
uniform-sphere calculation would certify a property it never measured, on a footprint whose actual
leverage is `5.7486` times worse than the sphere it assumed. Passing a power gate by not looking
at the footprint is not passing a power gate.

This is disclosed rather than buried because it is the one place where the frozen text admits an
outcome we are declining to take, and a future reader must be able to see that we knew.

## What is NOT claimed

- **No statement about Longo.** This is not REJECTED-AT-LONGO-AMPLITUDE. An underpowered
  instrument cannot reject an amplitude it was never able to detect.
- **No statement about the sky.** The canonical boundary sentence still applies: nothing here
  establishes that the sky is isotropic.
- **No statement about black-hole-universe cosmology**, in either direction. Kun's boundary
  stands: a spin result would be a spin-anisotropy/statistical-isotropy result only. The lane's
  confirmed scope inside the BHU programme (Duho, 2026-08-21) is a matter of portfolio and
  motivation and does not license an inference from this outcome to any BHU model.
- **No fault of the instrument.** The estimator, its frozen weights, tau, the identity receipts,
  the committee, the hand-check harness and the custody chain are all unimpeached. What failed is
  the footprint.

## What continues, and why

Acquisition **runs to completion** — transfer, cutouts and chi. It is unattended, receipt-driven,
already paid for, and a completed verified sample is the asset that lets a successor proceed
without re-fetching 0.7 TB. The verdict estimator is still built and hash-frozen per
`VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md`, because analysis code provably predating its data is
worth having and is the successor's starting point.

Successor design: `SUCCESSOR_SCOPE_20260821.md`.

## The cause, recorded so it is not repeated

The parent was fixed by a stopping rule that took **contiguous BRICKIDs until 200,000 galaxies had
accumulated**. Legacy brick IDs run south-to-north, so a contiguous prefix **is** a polar cap by
construction — and a cap is the worst available geometry for a dipole, because only one end of it
is ever observed.

The figure of merit for a fixed-axis dipole test is `N * Var(cos theta)`, not `N`. The rule
maximised the first factor while structurally minimising the second. `Var(cos theta)` came out
`0.057985` against a full-sky `1/3`. **The failure was designed in the moment the stopping rule
was written, and no amount of data collection could have escaped it.**
