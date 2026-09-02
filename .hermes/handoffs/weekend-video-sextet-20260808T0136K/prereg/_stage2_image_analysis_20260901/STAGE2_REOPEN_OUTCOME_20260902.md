# STAGE TWO — RE-OPENED, AND WHAT THE RE-OPEN FOUND

**Ruled by the principal, 2026-09-02 (direction #53), verbatim:**

> re-open stage two now that the data is here

Stage two was closed on 2026-09-01 at a calibration wall. It re-opened this
morning on the completion of the bulk acquisition — 12,117 DR10-south bricks,
143.37 GiB, every one SHA-256 verified
(`../_successor_build_20260824/acquire/ACQUISITION_COMPLETE_20260902.md`).

The re-open was run with a deliberate prior: **the wall was human-labelling
capacity, not data access, so possession of the pixels should change nothing.**
Both seats were instructed to default to that and make the evidence overturn it.

## Outcome, stated first

**The frozen run does not re-open.** codex `DOES-NOT-REOPEN` (20 verified frozen
quotes); agy `CONFIRMED` on independent recomputation. The calibration gate is
stated three separate times in the frozen text, not once, and no branch escapes
it.

**But the closure contained two factual errors of its own, and both are
corrected below.** One of the four dead ends was closed on a premise that is
false.

## CORRECTION 1 — "Galaxy Zoo lacks coverage of DR10.1-south" is FALSE

`STAGE2_CLOSED_20260901.md` states, in the external-labels row of its dead-end
table, that GZ1 "lacks coverage of DR10.1-south". That assertion was argued, not
measured. With the retained mask in hand it became measurable, and it does not
survive measurement.

Measured against `positions_selected_cut.csv` (49,211 rows, sha256
`a20682c1…cdd372`) versus GZ1 Tables 2+3 (667,944 + 225,268 rows), nearest
neighbour, 1.0″ acceptance:

| quantity | count |
|---|---:|
| retained-mask rows matched within 1.0″ | **16,604** |
| unique GZ1 objects among those matches | 16,600 |
| from GZ1 Table 2 / Table 3 | 14,574 / 2,030 |
| matched rows with any CW/ACW vote | 13,347 |
| matched rows with `P_CW + P_ACW > 0.5` | 1,040 |
| matched rows with `P_CW ≥ 0.8` or `P_ACW ≥ 0.8` | **363** |

Threshold sensitivity (mask rows): 16,488 @0.5″ · 16,637 @1.5″ · 16,658 @2.0″.
The 1.0″ rule travels with the number; a positional crossmatch has no
threshold-free count.

**Blind-doubled.** agy wrote its own sexagesimal parser and its own
`astropy.match_coordinates_sky` crossmatch rather than re-running codex's, and
reproduced all ten quantities exactly. agy's astronomical sanity check: a ~34%
overlap is plausible because SDSS DR7 and DR10-south both cross the celestial
equator (Stripe 82), so a dense equatorial band of overlap is expected.

The defensible narrower claim — that GZ1 lacks *population-representative*
coverage — was neither what the closure said nor tested. It remains open.

## CORRECTION 2 — the "no published sign anchor" objection was ours, not the text's

The closure held GZ1's screen-relative sign to have "no publishable anchor to our
East-of-North convention," implying the frozen design requires a *published*
anchor. It does not. The frozen text freezes a different empirical anchor —
the mandatory synthetic absolute-sign anchor BS-4, re-established "empirically
before any real image" (V134 lines 124–129). An empirical anchor is therefore
conceptually admissible in kind; the closure added a requirement the text never
imposed.

This correction does **not** rescue the route — see below — but the reason it
fails is the actor table, not the anchor.

## Why the frozen run still does not re-open

The calibration floor is not one gate but three, independently stated:

* **Estimator (line 417)** — the branch predicate "first checks the calibration
  floor: any `a_LB_b < 0.85` emits an immediate pre-unblinding
  `INCONCLUSIVE-BY-CALIBRATION` and halts."
* **Stage-C boundary (lines 477–482)** — "Only if all bins satisfy
  `a_LB_b >= 0.85` may Stage C run."
* **The lock Duho signs (lines 1243–1244)** — `verify_lock()` "independently
  recompute[s] `all(a_LB_b >= 0.85)`", with a required negative fixture proving
  a low-bound aggregate cannot produce a passing lock.

There is no raw-null, calibrated-statistic, or existence-only escape branch. The
algebraic intuition that a null test needs only `â > 1/2` is correct as
statistics and **irrelevant as procedure**: the floor is evaluated before any
real statistic exists, so nothing is emitted to test. Where the text and the
algebra disagree, the text governs.

And the 363 labels are inadmissible here regardless of their number. Row G admits
only the hand-check committee, "of the allocated sample only"; row H's ingestion
writer receives labels only from row G; and the conduct table (lines 721–723)
makes the list exclusive — "Any pre-unblinding touch of a χ-bearing object by any
person or process not in this table, or outside a row's stated surface, is
forbidden by default." Substituting an external catalogue would add an actor,
a data source, a label schema and a match rule after P0. **Pixels changed
feasibility, not admissibility.**

## What a successor would face (the honest costing of the 363)

For a *new* preregistration with its own freeze, the 363 are a real starting
asset. They are also, on present evidence, probably not enough — and the reason
is structural, not arithmetic:

1. **The floors are per-stratum, not global.** ≥30 real labels per live HC
   stratum across 9 strata, AND ≥10 per non-empty joint cell across the 3×9
   allocation. 363 spread over 27 joint cells averages ~13 per cell, and real
   sky distributions are not uniform. The global count clearing 270 says little.
2. **The strata are χ-derived, so the distribution is unknowable until the
   instrument runs.** Row D2 computes "machine-committee state × χ tertile per
   object." Which stratum each of the 363 falls in cannot be determined without
   measuring χ — which is behind BS-6. So whether the 363 satisfy the floors is
   *not answerable from catalogue data at all*.
3. **The sign anchor would need its own precommitted design** — render matched
   GZ1 objects through the ratified geometry, fix the mapping by consistency,
   precommit the disagreement rule — before any of it is used.
4. **Shamir (2022, MNRAS 516, 2281)** annotated 1,287,094 DR8 Legacy objects
   with winding directions, but the catalogue is "available upon reasonable
   request", not a public download, and it is machine annotation, not human
   truth. NOT VERIFIED for overlap. The 8.67M-row GZ DESI catalogue is model
   prediction and remains forbidden inside `a`.

## Status

**STAGE TWO RE-OPENED AND RE-CLOSED THE SAME DAY, with its record corrected.**
Stage one remains the deliverable. The image half still awaits human calibration
capacity. What changed is that the reason it waits is now stated accurately: not
"there are no external labels" — there are 363 confirmed ones — but that the
frozen text admits no actor to carry them, and that whether they would satisfy
the per-stratum floors cannot be known until an instrument run that is itself
gated.

Sources: `CODEX_REOPEN_ANALYSIS_20260902.md`, `AGY_REOPEN_VERIFY_20260902.md`.
