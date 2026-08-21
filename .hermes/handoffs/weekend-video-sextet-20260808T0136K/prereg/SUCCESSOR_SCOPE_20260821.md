# SUCCESSOR SCOPE — a Longo-amplitude test on a footprint chosen for leverage

Hwao, 2026-08-21 18:19 KST. **Scoping note, not a preregistration.** Authorised in direction by Duho:
*"go ahead with inconclusive-by-power and scope the successor."* Nothing here is frozen; the
successor needs its own preregistration, its own binding slots and its own gates.

## The one-line diagnosis it must design against

The figure of merit for a fixed-axis dipole test is `N * Var(cos theta)`, not `N`. The dead run
maximised count and structurally destroyed geometry. Every design choice below follows from that.

## The prize, in numbers

| population | N | Var(cos t) | leverage | full-sphere-equivalent |
|---|---:|---:|---:|---:|
| dead parent, BRICKID 1..121000 | 208,407 | 0.0580 | 12,084 | **36,253** |
| full-keyspace dered Cut-6 | 832,393 | 0.4452 | 370,582 | **1,111,747** |
| full keyspace @ 45% acceptance | 374,576 | 0.4452 | 166,762 | 500,285 |
| full keyspace @ 25% acceptance | 208,098 | 0.4452 | 92,646 | 277,937 |
| Longo 2011, his 15,158 at our axis | 15,158 | 0.2245 | 3,403 | 10,208 |

Frozen requirement: **100,000** full-sphere-equivalent.

Two readings worth keeping:

- The full footprint clears the requirement at **8.99% acceptance**. Headroom is not the problem.
- **Same N, 7.7x the leverage.** 208,098 galaxies drawn from the full footprint are worth 277,937
  full-sphere-equivalent; 208,407 drawn as a contiguous prefix are worth 36,253. The count was
  never the issue.

(`Var` for the full keyspace is the count-weighted brick-centre value from
`TORI_FOOTPRINT_VARIANCE_RECEIPT.md` with its `0.0124` bracket — adequate for scoping, and to be
recomputed on actual accepted positions before any freeze.)

## Seven design requirements

1. **Selection must never be a contiguous BRICKID range.** That is what built the cap. Take the
   whole footprint, or if a subset is required, choose it to maximise `N * Var(cos theta)` about
   the target axis — which favours both polar regions and de-weights the equatorial band.
2. **Any stopping rule must be written on leverage, not count.** "Stop at 200,000 galaxies" is the
   defect. "Stop when accepted `N * Var(cos theta)` reaches X" is the repair, and it is
   computable from positions alone at any moment, with no chi involved.
3. **Footprint-aware normalisation.** Freeze `A_hat = D_hat / E[cos^2 theta]` as a *procedure*
   evaluated on the accepted sample, never the constant `3 * D_hat`. The constant is a full-sky
   special case that silently inflated by 42.76% here.
4. **Project the monopole out, do not merely report it.** Use the centred estimator
   `A_hat = sum (s - s_bar)(c - c_bar) / sum (c - c_bar)^2`, which is what the permutation null
   already implies and which removes the `-1.939` leakage coefficient by construction. F-2's
   report-monopole-first rule stays, but reporting was never subtraction.
5. **Derive sigma from the actual footprint.** `sigma_D = sqrt(1/(3N))` embeds the same `1/3`.
   Use the exact permutation variance `Var(s) * Var(c) / (N-1)`.
6. **The power gate must name accepted-sample `Var(cos theta)` as an explicit input**, closing
   the literal-reading loophole that let a uniform-sphere calculation formally certify power on a
   footprint it never inspected.
7. **Fix the sidedness seam.** `sim_power.py` is two-sided; F-3 is one-sided at Longo's sign.
   Whichever is chosen, one document must state it and the harness must match.

## Release: DR11, once photo-z lands

DR10.1 full-footprint is viable today and is the fallback. **DR11 is better and the wait is short.**

- +48% area (15,342 -> 22,731 deg^2), so more leverage still.
- Carries the DR10.1 sub-blob fix — confirmed by Dustin Lang, 2026-08-19, from the source.
- `ls_dr11.photo_z` is in production by Rongpu Zhou, *"ready in 2 weeks, optimistically by the end
  of this week"* as of 2026-08-19. Our selection cuts on `z_phot_median`, so this is the gate.
- Dustin has **offered to produce a list of every r-band image with its checksum** and we accepted
  (task 26). Producer-supplied digests are a stronger custody claim than digests fetched from the
  same tree as the data.

Decision point: if DR11 photo-z has not appeared by roughly **2026-09-05**, freeze the successor on
DR10.1 full-footprint instead of waiting further.

## What carries over untouched

The instrument and its frozen weights (`83008c1c…`), `tau = 4.4006456017494235`, the bit-exact
antisymmetry identity and its receipts, the machine committee, the HC-1H hand-check harness and
sealed-key protocol, the transport with its per-brick digest custody, the cutout and inference
runners with their authorisation gating, and the whole receipts discipline. **None of it is
impeached.** The dead run also proved the entire chain end-to-end on real data, which is precisely
what a successor needs and would otherwise have to establish from scratch.

## What must be rebuilt

The parent selection, the footprint receipt, F-1 through F-7, the power gate, and the
preregistration itself. The verdict estimator built under
`VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md` becomes the starting point rather than the endpoint —
its gating pattern and validation battery survive; its normalisation and sigma do not.

## Open questions for Duho

1. **DR11 or DR10.1-full?** My recommendation is DR11 with the 2026-09-05 fallback date.
2. **Does the successor keep Longo's axis fixed, or add a second preregistered axis?** Fixed-axis
   is what makes it a test of a published claim; a free-axis scan is a different study and would
   need its own justification.
3. **Is the dead run written up?** A preregistered study that stopped itself on geometry it could
   have checked earlier is publishable as a methods note, and the diagnosis — that a
   count-based stopping rule on south-to-north brick IDs guarantees a cap — is transferable to
   anyone doing fixed-axis work on Legacy Surveys.
