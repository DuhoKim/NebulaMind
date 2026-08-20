# Handover — night of 2026-08-20 (written 23:31 KST)

**The headline: K-8 is crossed. This program measured the chirality of real galaxies tonight for
the first time**, at 22:30 KST, under a frozen amendment and a frozen authorization.

## Running unattended right now (all guarded, all resumable)

| machine | state at handover |
|---|---|
| transfer | 9,141 / 60,308 bricks, RUNNING, 0 quarantined, 2 transient retries |
| cutter | 2,771 tensors |
| χ inference | 2,771 measured |

Pauses itself at 24:00 KST, resumes 12:00, weekend windows unrestricted. Projected transfer
completion ~Tuesday; cutter and χ trail by minutes. Receipts are the only state everywhere —
reboots and pauses cost nothing.

## What was decided and frozen today (all before the crossing, deliberately)

- `AMENDMENT_PREK8_20260820.md` — `161547400e47ed66df616ba14756d9ab066c547f54b39bc161e6b4eaa26478c0`,
  mode 444. Sign convention (BS-5's scientific freeze + a newly-stated operational polarity),
  Jeffreys allocation priors with the estimate firewall verified in code, sparse-cell rule
  defaulting to HOLD → INCONCLUSIVE-BY-POWER until a gated merge revision exists.
  Gates: `KUN_GATE_A_AMENDMENT_20260820.md` (HOLD, 4 repairs, 3 rulings) →
  `KUN_GATE_A2_REGATE_20260820.md` (PASS, integrity sweep PASS).
- `K8_CROSSING_AUTHORIZATION_20260820.md` — `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`,
  mode 444, Duho verbatim "freeze it and authorize the crossing". Six binding conditions; the
  load-bearing one is **no tertile, no aggregate, no summary over χ until the sample is complete**.

## Gate record today (nine gates, all resolved)

PASS: cutout pipeline, positions export, object manifest (+repairs re-gate), inference build,
plumbing fixes, authorization pin, amendment re-gate. HOLD-then-repaired: object manifest
(staging-path + fail-closed), amendment (4 repairs — including that it had cited a harness line
from a **different revision** than its evidence came from, and a byte-for-byte verification
pointing at a file the N=20,000 rerun had overwritten).

## The rehearsal was the day's best investment

Synthetic end-to-end run found eight interface faults **and two parameters about to be chosen on
the wrong side of K-8** (prior smoothing; sparse-cell rule). Either chosen after the first real χ
would have voided the run under F-9. It also confirmed χ recovers synthetic chirality at 94.8%
with the direct sign convention, and that the full 208,407 will cost ~12.5 h of compute.

## Sky-map finding, worth knowing before someone panics at the picture

All 208,407 parent galaxies lie at **dec < −39.4** (median −56.5). The empty northern sky in
Blanc's map is **not missing data** — the frozen chain restricts to BRICKID 1..121000 and Legacy
brick IDs run south-to-north, so the parent is a deliberate ~18%-of-sky southern cap. Whether one
cap can constrain a dipole was answered on 12 Aug: `TORI_FOOTPRINT_VARIANCE_RECEIPT.md`,
count-weighted var(cos θ) = 0.445201 against a required 0.15.

## What waits on Duho (nothing urgent)

1. **The 150-label pilot** — only after the sample is complete and strata compute once. Days away.
2. Standing items unchanged: set `qlcxQbkIYlI` private on the personal YouTube channel; a
   thank-you to Dustin Lang; NERSC/Iris and Globus are optional now (route B is doing the job).

## Fault log additions (2026-08-20)

Gate sessions degrade past ~a day / ~150K context — one gate per fresh session, and **one
deliverable per gate** (the combined amendment+plumbing gate ran 67 min without a verdict; split
in two, both finished). Spoken decimals do not normalize into slide numbers ("zero point eight
three four" never becomes 0.834336) — say numbers a normalizer can convert, and say a progress
bar's total out loud or the graphic is correctly dropped. Quiet hours (22:30–08:00 KST) render
but do not play; republish with `--force-live` when Duho is up.

## Boundary state

K-8's chirality-label clause is **spent**, by authorization, on the record. Everything else
holds: no sky estimand, no unblinding, no aggregate over χ, no hand-check, nothing published.
F-9 now binds absolutely — no parameter may change, or the run is void.
