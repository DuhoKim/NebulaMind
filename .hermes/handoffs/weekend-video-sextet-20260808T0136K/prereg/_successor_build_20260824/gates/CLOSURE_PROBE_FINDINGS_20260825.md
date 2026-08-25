# What the probe run shows — Hwao's reading, 2026-08-25

**This is not a gate verdict.** It is the lane record of what `closure_probe_suite.py` returned
and what I think it means. The ruling belongs to the referee seats under
`BRIEF_CLOSURE_RECEIPT_V4.md`, and they are free to reject every line of this.

## Result

Receipt `CLOSURE_PROBE_RECEIPT_20260825.json`, production path (no memoised geometry), 16 min
29 s, `stable_sha256 f1cd1004de806c6bb6f1261e4177680bc7fdc9f28de056ca5ca1dc5a26281961`. The
same 22 outcomes came back under two earlier `--fast-geometry` runs, which agreed with each
other byte-for-byte (`3abf01ae…`), and they reproduce what an independent probe script written
in the previous round returned before it could be reviewed.

22 probes, 18 conforming. Four inputs that the suite expected to be refused were accepted:

| id  | input | outcome |
|-----|-------|---------|
| C01 | parent with one row omitted + an oracle file edited so the omitted brick's eligible count is 0 and that 1 sits in a filler row | **accepted** |
| C02 | parent with one row omitted + a selection and oracle both reduced to match it | **accepted** |
| C03 | the C01 inputs reached through symlinks | **accepted** |
| C04 | parent whose per-brick counts balance but whose second row carries an unused ls_id and the first object's coordinates | **accepted** |

All twelve refusal controls (R01–R11), the honest baseline (P01) and all five malformed-input
probes (E01–E05) behaved as the check's docstring says they should. The refusals are real and
they name the brick: R01 and R02 reproduce the historical `3471m885` / `2857m870` omissions and
refuse them by name.

## Root cause, as I read it

`close_manifest` has four bindings. Two of them are anchored outside the caller:

- geometry — read from `PINNED_SIDECAR_REL`, digest checked against `PINNED_UNIVERSE_SHA256`;
- planner — full transitive digest checked against `PINNED_PLANNER_DIGEST`.

The other two are not. The selection, the parent and the count oracle arrive as **paths chosen
by the caller**. Their digests are computed (`sha256_file`) and reported in the result dict, but
compared to nothing. The only pinned quantity on that side is the scalar
`PINNED_COUNT_TOTAL = 832,393`, and a scalar total is preserved by moving counts between rows —
which is exactly what C01 and C02 do.

So the round-9 finding has not been removed; it has moved. The witnesses are now *computed*
rather than *accepted*, but two of them are computed **from files the caller nominates**, and a
digest of a file the caller chose is not an external witness.

`successor_ref_v4.py:105` already declares

    PINNED_COUNTS_SHA256 = "4e4ec45d83f156e8daa738d81cd71a1e140d4ccbadd5343dc0bb8ed9f2479aa0"

under a comment calling it an external witness a caller cannot regenerate. **That constant is
never read anywhere in the module.** I verified what it is a digest of:

    shasum -a 256 _tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/combined_per_brick_counts.csv
    4e4ec45d83f156e8daa738d81cd71a1e140d4ccbadd5343dc0bb8ed9f2479aa0

The count table therefore has a pinnable path and a pinned digest already sitting in the file,
unused. C01–C03 walk through the gap between the constant and its non-use.

C04 is a different gap: nothing binds the parent's row *contents*. The count proof compares row
counts per brick, so a row whose ls_id does not exist and whose coordinates belong to another
object still balances, and the required brick set the planner derives from it is understated —
the same shape of error as the 60,308/60,310 failure, arrived at from the other end.

## Candidate repairs, none implemented, none chosen

1. **Oracle (C01–C03).** Mirror `load_pinned_geometry`: a `load_pinned_counts()` that reads the
   count table from its pinned relative path and verifies `PINNED_COUNTS_SHA256`, and drop the
   `oracle_npz` parameter. Then the completeness proof rests on an artifact the caller cannot
   nominate. This is the smallest repair and it uses machinery that already exists.
2. **Selection (C02).** The selection is the study's own output, so it cannot be pinned as a
   constant before it exists. It needs a digest recorded outside the calling process — the
   committed selection receipt — with `close_manifest` reading that receipt from a pinned path.
   Symlinked paths (C03) stop mattering once both artifacts are pinned rather than passed.
3. **Parent rows (C04).** Cheapest defensible check: for every row, the brick it declares must
   be the brick whose bounds contain its (ra, dec) per the pinned geometry. On the C04 input
   that fails, because the fake row's coordinates sit in the first object's brick while the row
   declares the second. A stronger version binds the parent to the catalog fetch receipts.
   The referee may instead rule C04 outside this function's contract; if so, the requirement
   moves upstream rather than disappearing, and something must be named that carries it.

## Consequence for the download

Unchanged and unchanged deliberately: **nothing may be fetched.** Duho's condition was that the
download waits for the closure check to clear. It has not cleared, and this run is evidence
against it clearing in its present form, not for it.

## What this run does not show

The suite's own `not_covered` list is in the receipt and is part of what the referees are asked
to extend. The largest item: every probe here runs on a two-object parent table. The real
closure — 65,060 objects, 6,445 selected bricks — has never been run end to end, so nothing
here is evidence about its runtime, its memory, or its behaviour at scale.
