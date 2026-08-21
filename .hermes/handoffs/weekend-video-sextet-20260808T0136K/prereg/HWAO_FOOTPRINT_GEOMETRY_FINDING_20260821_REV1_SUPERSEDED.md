# FINDING — BS-1's footprint-variance PASS was measured on a different population than the one being measured

Hwao, 2026-08-21 16:02 KST. Found while implementing F-1 for the verdict estimator. **Not gated. Must be
adversarially gated before it is treated as settled.** No aggregate over chi was computed;
everything below is geometry from positions only.

## The two populations

| | population BS-1 gated | sample actually being measured |
|---|---|---|
| definition | dered Cut-6, BRICKID keyspace `1…662174` | parent, BRICKID `1..121000` |
| objects | **832,393** | **208,407** |
| declination | full DR10-south | `[-89.593, -39.375]`, median `-56.457` |
| mean(cos theta) | `-0.109116` | **`-0.646430`** |
| mean(cos^2 theta) | `0.457108` | `0.475857` |
| var(cos theta) | **`0.445201`** — PASS vs 0.15 | **`0.057985`** — FAIL vs 0.15 |
| range of cos theta | full | `[-0.9918, +0.3181]` |

Gated column: `TORI_FOOTPRINT_VARIANCE_RECEIPT.md` (`9f6955e3…`), cited in the frozen
preregistration's BS-1 row as *"footprint variance PASS … var(cos theta) = 0.445201 >= 0.15"*.
Measured column: computed today from `_positions_20260820/positions_parent_20260820.csv`
(`90fa6c96…`, 208,407 rows) about the frozen axis `(216.984434295527, +32.060611193471)`.

The parent stopped at BRICKID 121000 under the authorized stopping rule in
`TORI_PARENT_ROW_COUNT_20260812.md` — *"contiguous completed BRICKID range 1..121000 of
documented key range 1..662174"*, *"not yet covered: 121001..662174"* — once the contiguous Cut-5
lower bound reached 200,000. The variance receipt swept the whole keyspace. **Neither document is
wrong; they were simply never compared.**

Under the receipt's own binding rule (`FAIL if V + 0.0124 < 0.15`), the measured sample fails:
`0.0580 + 0.0124 = 0.0704 < 0.15`.

## Three consequences, in order of severity

**(1) The estimator normalisation is wrong for this footprint — and for the gated one too.**
F-1 freezes `A_hat = 3 * D_hat`. That factor 3 is exact only when `E[cos^2 theta] = 1/3`, i.e.
full sky. Here `E[cos^2 theta] = 0.475857`, so `E[A_hat] = 3 * 0.475857 * A = 1.4276 * A`.
**A_hat overstates the true amplitude by 43%.** A sky carrying `A = 0.0286` — 70% of Longo's
value — would be reported as `A_hat = 0.0408`, landing dead centre in REPRODUCED-LONGO.
Note this is **not** caused by the cap: the gated population has `E[cos^2 theta] = 0.457108`, so
the same inflation (x1.371) would have applied there. The F-1 unbiasedness receipt
(*"injected 0.0400 -> recovered 0.0402"*) can only have been run on a full-sky simulation.

**(2) Monopole leakage is severe, and the cap makes it six times worse.**
With `E[s] = M + A cos theta`, `A_hat = 3*M*E[cos theta] + 3*A*E[cos^2 theta]`. On this sample
the monopole coefficient is `3 * -0.646430 = -1.939`. A monopole of only `M = 0.01` — from the
sky *or from sample selection* — produces `A_hat = -0.0194` with no dipole present at all. On the
gated population the coefficient was `-0.327`. F-2 requires the monopole be reported first, which
is the right instinct, but reporting it is not subtracting it.

**(3) We never observe the positive pole.** `cos theta` reaches only `+0.3181`. A dipole is a
two-ended object; the sample covers one end and the equatorial band, never the other end.

## What is NOT affected

The permutation null (F-3). Label permutation preserves the multiset of signs, hence the monopole,
hence its leakage — so the null distribution carries the same offset and the **p-value remains
valid**. The damage is confined to F-6's amplitude comparisons, which test `A_hat_c` against
absolute thresholds.

## What I did not do

Change anything. F-9 binds absolutely. I did not adjust the estimator, re-derive the
normalisation, or touch a frozen file. **The remedy is Duho's and it needs a gate.**

## What a gate should try to refute

1. That a receipt exists which re-derived F-1's normalisation for a non-full-sky footprint, and I
   failed to find it.
2. That Longo's published `A` carries a normalisation convention that already absorbs `E[cos^2 theta]`,
   making `3 * D_hat` correct by construction against *his* number rather than against the sky.
3. That the parent is not final — that BRICKID `121001..662174` was always intended to land.
4. My arithmetic, directly: 208,407 rows, one pass, no sampling.

## My own error, corrected

In `HANDOVER_20260820_NIGHT.md` I wrote that whether one cap can constrain a dipole *"was answered
on 12 Aug"* by this receipt, and I repeated it verbally today. **That was wrong.** The receipt
answered the question for the full-keyspace population, not for the cap. I read a PASS and did not
check which population it passed for — the exact failure the campaign's own rule about verifying
anchor claims from the source exists to prevent.
