# The F1–F3 repair — what changed, what closed, what is still open

2026-08-26, Hwao. Written against `CLOSURE_RECEIPT_GPT56.md` and `CLOSURE_RECEIPT_CODEX.md`,
both `NOT CLEAR`. This is the lane record of the repair, not a verdict on it. The repaired code
has not been refereed.

## Round 9 is superseded, and it has to come off the record as such

Blanc relayed my round-9 result to Duho as a strength: that a parent missing rows was refused by
a completeness proof which could not be satisfied without also shortening the oracle, whose
total is pinned to the release. **That conclusion is refuted.** The referees showed the oracle
was not independent of the caller — probe C01 keeps the total at exactly 832,393 while a parent
row is gone, by moving one count into a filler row. The proof held only against an opponent who
declined to edit the file it was reading.

My own adversarial round did not find this; the gate did. The finding stands, the earlier claim
does not, and anything downstream that cites "the round-9 attack now fails" should cite this
instead. `CLOSURE_PROBE_FINDINGS_20260825.md` carries the same correction at its head.

## What the three blockers were

One defect in three places: **the artifact that judges the manifest was handed in by whoever
presented the manifest.** `close_manifest(parent_csv, selection_npz, oracle_npz, manifest)`
computed a digest for each of those three paths, reported them in its result, and compared them
to nothing.

## What changed in `ref/successor_ref_v5.py`

`close_manifest(manifest_bricknames)` — one argument, the thing being judged. Everything else is
loaded from a pinned path with a pinned digest:

| binding | pinned path | digest | second witness |
|---|---|---|---|
| geometry | `PINNED_SIDECAR_REL` | `PINNED_UNIVERSE_SHA256` | cardinality 366,912 |
| planner | frozen lane module | `PINNED_PLANNER_DIGEST` | live callables (below) |
| count table | `PINNED_COUNTS_REL` | `PINNED_COUNTS_SHA256` | 270,577 rows, total 832,393 |
| selection | `PINNED_SELECTION_REL` | `PINNED_SELECTION_SHA256` | 6,445 bricks — **code pin only** |
| parent | `PINNED_PARENT_REL` | `PINNED_PARENT_SHA256` | `positions_receipts.json:output_sha256` |

Four further changes, each traceable to a numbered finding:

1. **The count table is the CSV, not a re-serialised NPZ** (CODEX F1). `PINNED_COUNTS_SHA256`
   was already in the file, unused; it is the digest of `combined_per_brick_counts.csv`, so
   that is what closure reads. Schema violations refuse at load: duplicate brickid, negative
   count, wrong column names, wrong row count, wrong total.
2. **The parent has two independent bindings** (GPT56 F3, CODEX F3). The fetch wrote
   `output_sha256` into `positions_receipts.json` against TAP job URLs before any closure code
   existed. Both it and the code constant must agree, and the receipt's own `total_rows` must
   equal the sum over its 13 chunk receipts.
3. **The planner digest binds the code that runs** (GPT56 F4). That seat rebound the live
   `adapter.plan_object` in memory; file digests were untouched, the pinned digest still
   matched, and the replacement produced the answer. The digest now includes a recursive
   fingerprint of the live callables' bytecode, names, constants and defaults.
   Writing this the obvious way — `repr(code.co_consts)` — was wrong: a nested code object
   reprs with its memory address, so the digest moved on every module load. Nested code is
   recursed into instead, and the value is stable across processes.
   `PINNED_PLANNER_DIGEST` therefore changed from `82971b80…` to `10cea7a6…`. **That is not a
   changed planner; it is a digest that binds more than it did.**
4. **Two validators the seats named as gaps** (CODEX F7): every selected brick must resolve in
   the pinned geometry universe, and every parent row's coordinates must fall inside the brick
   that row declares. The second closes the C04 family: row counts prove cardinality, never
   that a row sits where it says it does.

## The first end-to-end production closure

Never run before this repair; both referees flagged that. On the pinned artifacts:

```
objects            65,060
selected bricks     6,445
required bricks    12,117
plan_digest        aaeaa9f37aabf1da6000a6ad07890cfe010677e301583530ba1a108833e3b3f1
runtime               185 s   (47 s sidecar verify + 77 s planning 65,060 objects + parse)
```

**The download is about twice the size the queued plan assumes.**
`DOWNLOAD_QUEUE_PLAN_20260825.md` estimates "order 77 GB (≈6,445 bricks at the predecessor's
measured 12.2 MB/brick, plus edge…)". The closure requires **12,117** bricks, not 6,445 — the
neighbour-brick effect is 1.88×, not a small margin. At the same 12.2 MB/brick that is
**≈148 GB**. The plan's byte ceiling was written against the smaller number and needs Duho's
decision before anything fires. Nothing has been fetched.

## What is still open

- **The selection's binding is weaker than the rest.** A code pin, no producer receipt. A
  sealed BS-2s receipt carrying that digest is the obvious next step, and until it exists the
  suite says so rather than implying parity with the parent.
- **The repaired code has not been refereed.** Neither seat has seen v5.
- **Verification-to-use window.** Every loader hashes a file and then re-opens it. Both seats
  named this; it is untested and unaddressed.
- **U02's dispute is unresolved on the record.** I implemented the coherence check rather than
  wait for a ruling, so the probe now refuses. A referee may still hold the check belongs
  upstream; if so it should say which producer enforces it.

## Files

- `ref/successor_ref_v5.py` — the repaired subject. v4 is untouched: both referee reports pin
  its digest and that record stays readable.
- `ref/FIXTURES_V5_20260826.out` — 42 checks, all pass.
- `gates/closure_probe_suite_v5.py` — 23 probes. The V4 probes that edited caller-supplied
  inputs cannot be written any more; they are replaced by redirection probes that point a
  pinned path constant at a copy and check the digest gate refuses it.
- `gates/CLOSURE_PROBE_V5_RECEIPT_20260826.json` — its run.
