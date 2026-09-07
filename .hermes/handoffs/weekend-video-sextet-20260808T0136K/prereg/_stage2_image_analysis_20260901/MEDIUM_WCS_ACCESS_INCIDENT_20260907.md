# ACCESS INCIDENT — fresh-validation and holdout pixels were fetched and cached by the developing account
2026-09-07 22:52 KST / 13:52Z. HWAO, lane owner. Filed under A1's attempt/abort registration and push
rule (line 108). This is a record of what happened and the consequence the run's own rules attach to
it. **It is not a request for a decision, and it does not propose a restart, an amendment, or anything
that would restore a closed attempt.**

## 1. The finding, verified with my own controller
Found by Codex, then verified independently by me from the pinned drawn lists and the tuning inventory,
using JSON reads and `os.stat` only — **no FITS bytes, pixel arrays, labels or outcomes were opened**
to produce this record, and none were needed.

The tuning stage fetched **whole DR9 bricks**, not per-object cutouts. The three drawn lists are
disjoint by identity (tuning ∩ holdout = 0), but bricks are shared:

* **2 holdout objects in 2 bricks** — 587735662085537895 (`1485p365`), 587736781457916109 (`2379p345`)
* **24 validation objects in 23 bricks** — 587725470136205340 `1398p567`, 587725551735996593 `1280p527`,
  587729232516547021 `2511p442`, 587731499725488147 `1656p557`, 587731679044501710 `1334p402`,
  587731870168318054 `1694p547`, 587731870706565310 `1749p557`, 587732135380975762 `1652p507`,
  587732154177683565 `1395p410`, 587732482744975392 `1685p482`, 587734621638164597 `1461p397`,
  587735667451101380 `2044p570`, 587738953105408190 `2065p365`, 587739848603337094 `2446p532`,
  587739848604975456 `2479p502`, 587739849138045209 `2399p575`, 587739863099310335 `2460p580`,
  588013382744670361 `1871p522`, 588013383821033593 `1969p525`, 588013384351023291 `1707p525`,
  588017111836327967 `1960p475`, 588017604158488738 `2181p392`, 588298664110391415 `1843p482`,
  588298664113864794 `1960p475`

25 distinct bricks. All **75 plane files exist on disk, 307.8 MB**, owned by uid 501 (`duhokim`, the
developing account), written between **2026-09-07T12:32:32Z and 12:45:58Z**. Per-file digests, sizes,
owner and timestamps: `/Users/duhokim/work/Trio/hwao-shared-brick-exposure-audit-20260907.json`.
The first tuning brick `1461p347` is not shared; that changes nothing about the other 25.

## 2. The operative clause, quoted
Signed V15 E5(d), line 23 (`fdd9eedd…`), verbatim:

> before both freeze receipts exist, no person or agent who participates in candidate or pipeline
> selection may view, possess, query, cache, copy, fetch, or cause any other person, seat or service
> (including public cutout services or another machine) to inspect any fresh-validation-set pixel.
> Any such access voids attempt 2 and closes option (A).

No freeze receipt exists — there is no W, no winner, and the holdout was never opened. The pixels of 24
fresh-validation-set objects were **fetched, copied and are cached** on the developing account. That is
four of the six listed verbs, in the plain sense of the words. **The clause has no exemption for whole
bricks, for compressed files, for pixels that were never cut out, or for a stage that produced no
score, and I will not invent one.** A1 line 121 expressly retains V15's "custody and fetch-after-freeze
restrictions"; A1 line 125 states a later amendment "cannot ... cure prior exposure, reopen holdout or
restore an expended attempt" and that "Existing CLOSED/no-further-attempt obligations remain
controlling". Custody under E5(d) was never in place for these files: they are in the lane, owned by the
developing account, not in `/Users/nmcustody/fresh_validation_bricks/` under `chmod 700`, and no lift
was given because no freeze receipts exist to lift against.

Independently, A1 line 92 requires W published and the opening record anchored "before the first
participant, process or service accesses any holdout pixel", and line 94 states that "early access ...
invalidates and stops the run". Two holdout objects' pixels were fetched with no W in existence.

## 3. The consequence, under those rules
**Attempt 2 is void and option (A) is closed for this run.** The holdout early access independently
invalidates and stops it. This is what the signed text does; it is not a disposition I chose, and it is
not something an amendment can lift. The begun run therefore ends here, on its own terms, with the
tuning abort and this incident as its final record.

## 4. Two of my own earlier statements were wrong
* `BEGUN_RUN_EXPOSURE_INVENTORY_20260907.md` concluded "catalogue IDs only" for holdout and validation.
  I inferred that from the **absence of label and outcome files** — a check over a set that never
  established what the set contained, which is the exact defect class I have spent this week removing
  from other people's gates. Absent labels say nothing about fetched pixels. That record stands as
  written, with this correction attached; see `EXPOSURE_INVENTORY_CORRECTION_20260907.md`.
* `MEDIUM_WCS_REPAIR_CANDIDATE_AND_CONSEQUENCE_20260907.md` §3 item 5 said the attempt count was "the
  owner's alone" and that I made no claim. That was wrong in both directions: the rules already decide
  it, and presenting a determined closure as an open choice would have invited an amendment that the
  signed text forbids.

## 5. Cause, for whoever designs the successor
The fetch granularity is the whole brick, while the draw partitions **objects**. Any draw over a
catalogue that shares bricks across the three sets puts other sets' pixels on disk the moment the first
set is fetched. Nothing in the run path checks that. A successor design has to either fetch per-object
cutouts, or partition the draw by brick so the three sets never share one — a check that belongs at
draw time, before any fetch. Recorded as preparation, not proposed as an amendment to this run.

**Preserved:** the abort journal, all downloaded evidence, every existing binding, the exposed 400
tuning labels, both failed journals, and the adopted bytes (run path `1c4f96fb…`, producer `ea46478e…`).
No file was deleted, and no protected data was read to write this.
