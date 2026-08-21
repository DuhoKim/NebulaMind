# FINDING (Revision 2) — BS-1's footprint-variance PASS was measured on a different population than the one being measured

Hwao, 2026-08-21 17:01 KST. Revision 2 repairs three defects ruled by `GATE_FOOTPRINT_GEOMETRY_20260821.md`
(HOLD). Revision 1 survives byte-for-byte as
`HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV1_SUPERSEDED.md`. Replaced wording is quoted
verbatim in the changelog at the end. No aggregate over chi was computed; geometry from positions
only.

## The two populations

| | population BS-1 gated | sample actually being measured |
|---|---|---|
| definition | **dered Cut-6**, BRICKID keyspace `1…662174` | **dered Cut-5** R1 study parent, BRICKID `1..121000` |
| objects | **832,393** | **208,407** |
| keyspace coverage | 662,174/662,174 | 121,000/662,174 = 18.273143% |
| declination | full DR10-south | `[-89.593, -39.375]`, median `-56.457` |
| mean(cos theta) | `-0.109116` (brick centres) | `-0.646430` |
| mean(cos^2 theta) | `0.457108` (brick centres) | `0.475857` |
| var(cos theta) | **`0.445201`** — PASS vs 0.15 | **`0.057985`** — FAIL vs 0.15 |
| range of cos theta | full | `[-0.991828, +0.318140]` |

They differ in **count, keyspace, and cut level**. Independently reproduced by the gate over all
208,407 rows with `math.fsum`, matching to six decimals, on a CSV it hashed itself to the pinned
`90fa6c96…`.

**The receipt disclaims the use BS-1 made of it.** `TORI_FOOTPRINT_VARIANCE_RECEIPT.md` line 90:

> `- accepted-sample variance claimed: NO — this receipt is for the frozen dered Cut-6 population;`

The frozen preregistration's BS-1 row nevertheless cites it as *"footprint variance PASS …
var(cos theta) = 0.445201 >= 0.15"*. Neither document is wrong. They were never compared.

Under the receipt's own binding rule, the measured sample fails: `0.057985 + 0.0124 = 0.070385 < 0.15`.

## Consequence 1 — F-1's normalisation does not transfer to this footprint

F-1 freezes `A_hat = 3 * D_hat`. The factor 3 is exact only when `E[cos^2 theta] = 1/3`, i.e. a
uniform full sphere. Here `E[cos^2 theta] = 0.475857`, so `E[A_hat] = 1.427571 * A` when `M = 0`
— the estimator responds **42.76% high**. An amplitude of `A = 0.028580` would produce
`A_hat = 0.0408`.

**Scope of that example (Rev 2 repair).** It establishes only that such a sky **centres the
amplitude predicate** of REPRODUCED-LONGO. F-6 independently requires permutation `p < 0.001`,
Longo's sign per F-5, and the attenuation correction; the example does not establish those and
therefore does not establish a REPRODUCED-LONGO verdict.

Not caused by the cap: the gated population's own moment gives `3 * 0.457108 = 1.371323`, so the
factor-three issue would have applied there too.

Two primary sources close the escape routes, both located by the gate:

- `spike/sim_power.py` — the source behind F-1's *"unbiasedness receipt: spike, injected 0.0400 ->
  recovered 0.0402"* — draws `costheta = np.random.uniform(-1, 1, N)` under the comment
  `# On a sphere, mean(cos^2) = 1/3`. It is a full-sky simulation and validates nothing about a
  restricted footprint.
- Longo 2011 (arXiv:1104.2815) fits *"the 15158 points … to an a cos gamma dependence"*, obtaining
  `a = -0.0408` with `sigma_a = 0.011`. A through-origin fit coefficient is `sum(s*c)/sum(c^2)`
  — the second moment is in the **denominator**. Longo's number therefore already absorbs his own
  footprint geometry, which is precisely why `3 * D_hat` does not transfer to ours.

## Consequence 2 — monopole leakage, six times worse than on the gated footprint

`E[A_hat] = 3*M*E[cos theta] + 3*A*E[cos^2 theta]`. The monopole coefficient here is
`3 * -0.646430 = -1.939291`; on the gated population it was `-0.327348`, a ratio of `5.924`.
A monopole of `M = 0.01` — from the sky **or from sample selection** — produces
`A_hat = -0.019393` with no dipole present. F-2 requires the monopole be reported first, which is
the right instinct, but reporting is not subtracting or orthogonalising.

## Consequence 3 — the positive pole is never observed

`cos theta` spans `[-0.991828, +0.318140]`. The sample reaches very near the negative pole and
never approaches the positive one. A dipole is a two-ended object; we observe one end and the
middle.

## Consequence 4 (Rev 2, NEW and NOT YET GATED) — power, not only amplitude

Revision 1 said the permutation null was unaffected. That was too broad. Using the gate's exact
permutation moments for fixed signs and positions:

    E_perm[D_perm]   = mean(s) * mean(c)
    Var_perm(D_perm) = Var(s) * Var(c) / (N-1)
    E[D_obs] - E_perm[D_perm] = A * Var(c)

**Calibration survives** under exchangeability: the null is centred on the same monopole-leakage
offset, so the conditional randomisation p-value remains valid. **Power does not.** With
`Var(s) <= 1`, sensitivity scales as `A * sqrt(N * Var(c))`, so relative to a uniform full sphere:

| quantity | value |
|---|---|
| `Var(c)` this parent | `0.057985` |
| `Var(c)` uniform full sky | `0.333333` |
| leverage ratio | `0.173954` |
| sensitivity ratio `sqrt` | `0.417078` |
| N multiplier for equal power | `5.7486` |
| N for 100,000 full-sky-equivalent | `574,865` |
| full-sky-equivalent at **100%** acceptance of 208,407 | **`36,253`** |
| full-sky-equivalent at 50% acceptance | `18,127` |

**Even if every parent galaxy were accepted, this footprint delivers the statistical leverage of
about 36,253 full-sky galaxies against a frozen requirement of 100,000.** The frozen power gate
was computed on `sim_power.py`'s uniform sphere and does not establish that power here.

This consequence therefore reaches beyond F-6 into **F-4** (`sigma_D = sqrt(1/(3N))` uses the same
`1/3`), **F-7** (the floor is `3.09*sigma_ours`), and **INCONCLUSIVE-BY-POWER**, which F-6
declares *before* unblinding. Exchangeability itself is also assailable: a spatially varying
selection effect would violate it and is not rescued by preserving the global sign count.

**This whole section is new material and has not been gated. It must be attacked before it is
relied on.**

## Scope limit that binds every coefficient above (Rev 2 repair)

F-1 is defined over **accepted** galaxies. The 208,407 rows are the **pre-classifier Cut-5 study
parent**. `LANA_VARIANCE_APPROACH_AUDIT.md` (lines 85-88) warns that no tier licenses
accepted-sample variance because abstention can re-tilt the weights. So `1.427571`, `-1.939291`
and every number in Consequence 4 are **exact for the current parent and not yet proven for the
eventual accepted subset**. They cannot be proven until acceptance exists — which is after the
sample completes. This is a limit on precision, not a refutation of the mismatch.

## What I did not do

Change anything. F-9 binds absolutely. No estimator adjustment, no re-derived normalisation, no
frozen file touched. The remedy is Duho's.

## My own error, corrected

In `HANDOVER_20260820_NIGHT.md` I wrote that whether one cap can constrain a dipole *"was answered
on 12 Aug"* by this receipt, and repeated it verbally on 21 Aug. **That was wrong.** The receipt
answered it for the full-keyspace Cut-6 population and explicitly disclaimed accepted-sample
variance on its own face. I read a PASS and did not check what it passed for.

## Changelog — Revision 1 to Revision 2, replaced wording verbatim

1. **Consequence 1 overreach.** Was: *"A sky carrying `A = 0.0286` — 70% of Longo's value — would
   be reported as `A_hat = 0.0408`, landing dead centre in REPRODUCED-LONGO."* Replaced with the
   amplitude-predicate-only statement above. Gate ruling: the p and sign predicates bind
   independently.
2. **F-3 claim too broad.** Was: *"The permutation null (F-3). Label permutation preserves the
   multiset of signs, hence the monopole, hence its leakage — so the null distribution carries the
   same offset and the p-value remains valid. The damage is confined to F-6's amplitude
   comparisons."* Replaced by Consequence 4: calibration survives, power does not, and F-4/F-7/
   INCONCLUSIVE-BY-POWER are reached.
3. **Missing scope limit.** Revision 1 asserted the coefficients without noting that F-1 is over
   accepted galaxies while the file is the pre-classifier parent. Added as its own section.
4. **Additions from the gate's own work, not present in Revision 1:** the receipt's line-90
   self-disclaimer; the cut-level difference (Cut-6 vs Cut-5); `sim_power.py`'s uniform-sphere
   draw; Longo's fit-coefficient definition from the primary source.
