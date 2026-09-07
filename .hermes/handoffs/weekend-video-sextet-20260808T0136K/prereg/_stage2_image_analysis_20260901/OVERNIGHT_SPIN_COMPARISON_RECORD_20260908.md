# Overnight machine–human spin comparison — completed, exploratory (2026-09-08 04:06 KST)
Stamped from `date`. HWAO. Duho's authorization: **"run it until i check back"**. The work lives at
`/Users/duhokim/work/Trio/OVERNIGHT_SPIN_COMPARISON_20260908/`, outside git; every file there is pinned
by digest in `OVERNIGHT_SPIN_EVIDENCE_MANIFEST_20260908.txt`, filed alongside this record.

## The result
On **1,657 scored, field-of-view-eligible, DR9-north CzSL-expert-labelled spirals, machine and human
agree on 1,276 = 77.0%** (Wilson 95% 74.9–79.0%). That set is **6.9% of the 24,824 expert-labelled
parent sample as eligible, 6.7% as actually scored** — the fraction that stops any universal reading.
Both sides are near-balanced (human 850/807, machine 845/812), so the rate is not a lopsided predictor
meeting a lopsided label set. Terminal accounting for all 2,000 selected identities: 286 oversized and
13 size-unknown excluded from rendering by this run, 1,701 eligible, 1,657 scored, 44 render refusals,
0 unavailable, 0 unscored. The reused 400-object GZ baseline (311/388) is kept separate and never pooled.

## What made it trustworthy, in one place
* **Sign mapping documented, not fitted:** CzSL Table 3 class percentages (30.1/30.6/39.3, matched to
  0.03%) fix +1 = right-handed; CzSL §4.1 ties R/L to GZ1 Clockwise/Anti-clockwise; Lintott et al. 2008
  equates GZ1 "Clockwise" with Z-wise **rotation**; the estimator's +1 was fixed by synthetic
  mirror-verified spirals as **outward winding**. Naming and geometry are joined only by the
  trailing-arm assumption, which the sources state and this run did not measure per object.
* **Selection pre-committed:** the plan's salt `trio-human-spin-20260908-v1|` on a pool corrected to
  remove an inherited GZ confidence cut and a DR10-absence cut. Two superseded selections retained.
* **Eligibility frozen before scoring:** petroR90_r ≤ 14.7″, finite and strictly positive — SDSS's
  −9999 sentinel had briefly passed as "a small galaxy" and was caught before any scoring.
* **Every claim recomputed** independently of the scorer's own summary; all execution pins re-hashed.

## What it is not
Not a validated instrument, not an unseen-data result, not a physically calibrated handedness claim,
and **no reopening of the closed option A validation**, which remains closed on its own record. Sources
that produced no scores say so: Iye 2024 had **0 of 185** in-footprint galaxies fit the fixed field, and
Iye & Sugai 1991 is distributed by magnetic tape on request and could not be obtained — its overlap is
**not measured, which is unknown rather than zero**.

## Exposure
On this machine, from checked metadata: 2,568 brick directories (31.5 GB) downloaded by this run, plus
the pre-existing Tier-C and Option-A caches; every attempted download is digested in `exposure-log.jsonl`.
**The other Mac was never inventoried, so its coverage is UNKNOWN — absent inventory is never "fresh".**
Acquisition is whole-brick, so a brick on disk carries every object inside it, not only the selected one.

Independent review: Blanc recomputed the result from saved predictions and filed a scoped verdict
(REVIEW.md §D) — faithful to specification, reproduces independently, no material finding blocking
closure; both recommended report-only corrections were applied without touching `predictions.jsonl`.
