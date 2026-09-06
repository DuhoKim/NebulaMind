# R3C2 — batch reading for the limb-B corpus problem: PREPARATION, UNADOPTED (revision 4 after three rounds of independent review, 2026-09-06 20:38 KST)

**Status.** An execution question, kept out of the clause candidate so Duho can rule on it separately. Nothing adopted, frozen,
dispatched or run. Revision 1 was judged BATCH_PREP=UNSOUND by both reviewers for one decisive reason, accepted and repaired here:
**§2's IMPORTED rule reads a named source's value line in ANOTHER paper, which may sit in another batch; a session holding only its own
batch's texts cannot file that record** (both reviewers executed it: the same D1 record validates with both texts present and fails
with one batch's texts only — reproduced in the kit). The finding it answers: `R3C2_LIMB_B_DEATH_FINDING_20260906.md`.

## 1. The principle: a batch partitions OWNERSHIP of candidate passages, not ACCESS to evidence

Every session's working directory holds ALL 89 pinned texts (they are the pinned corpus; nothing is withheld) and an ownership list.
The seat ENUMERATES only its owned texts — reads them completely, applies §1, attempts the arithmetic — which is what bounds the reading
load; for §2/D1 it may look up the named source's line in ANY manifest text, and every such lookup is logged with manifest digest,
file and line. Reference-only access creates no ownership and no denominator entry. No input is classified BLOCKED because a text was
withheld, because none is. The same rule applies to both census seats and, under D7, to the auditor's enumeration and re-derivations.

## 2. What a batch is — concrete, computed from the real manifest

The 89 texts of `R3C2_CORPUS_MANIFEST.md` (sha256 `300d4da144d96ae9f1390c9018e919ae1ba6cf00be9f45ad36fdccfdcfbf9b24`), in manifest row order, partitioned into 12 ownership
batches whose sizes differ by at most one. Computed by the staged tool and pinned (`r3c2_staged_d1d7/partition_12_of_89.json`, its
printed form `partition_12_of_89.txt`, both in the pin sheet):

```
batch 1: rows 1-8 (8 texts, 278483 bytes, 4030 non-blank lines)
batch 2: rows 9-16 (8 texts, 1244397 bytes, 17938 non-blank lines)
batch 3: rows 17-24 (8 texts, 1573014 bytes, 16038 non-blank lines)
batch 4: rows 25-32 (8 texts, 745198 bytes, 8148 non-blank lines)
batch 5: rows 33-40 (8 texts, 1266439 bytes, 11819 non-blank lines)
batch 6: rows 41-47 (7 texts, 577720 bytes, 4319 non-blank lines)
batch 7: rows 48-54 (7 texts, 693384 bytes, 7628 non-blank lines)
batch 8: rows 55-61 (7 texts, 438168 bytes, 8692 non-blank lines)
batch 9: rows 62-68 (7 texts, 198317 bytes, 3799 non-blank lines)
batch 10: rows 69-75 (7 texts, 363253 bytes, 5130 non-blank lines)
batch 11: rows 76-82 (7 texts, 197654 bytes, 3321 non-blank lines)
batch 12: rows 83-89 (7 texts, 338821 bytes, 15814 non-blank lines)
```

**Twelve is a workload hypothesis, not a demonstrated capacity** (both reviewers): the seat that died was handling sets of eleven; seven
or eight texts per batch is below the observed failure and itself untested. The per-batch bytes and non-blank lines above are the
workload measure; batch 1's report confirms the size before batch 2 is dispatched, so a failure at eight is cheap, not fatal. **Equal text counts do not bound lines:** by manifest row order the batches range from 3321 to 17938 non-blank lines, so the row-order partition is
the simplest, not the most even; a line-balanced partition (a different pure function of the same manifest) is the obvious alternative and is
listed in the line for Duho. Batch 1 is light but not the lightest (batches 9 and 11 are smaller on both measures); a light first batch confirms less about
capacity than a heavy one would — a heavier first batch is the stronger pilot, at a higher risk of the failure it is testing for. The
pinned partition implementation deterministically computes these bytes from this manifest and 12; identical serialization and
implementation are required for byte equality (kimi recomputed it byte-identical with the pinned code).

## 3. What a session is

For batch k, each seat is a fresh process; each seat's twelve sessions run one engine and one kernel profile; the two seats are as V23
specifies (two engines), and the auditor is on a third. The working directory holds the packet, the brief, the pinned scripts, the
manifest, all 89 texts and the ownership list for k. The session prints its own `ACCESS_SHA` (= the packet digest) and writes
`candidates_b<k>.json`, `exclusions_b<k>.json`, `ledger_b<k>.json`, `SEAT_REPORT_b<k>.md`. **Identifiers are global and source-based:**
every candidate id, claim id and input id begins with `<owned file>#`, so nothing is renumbered at join and a cross-batch
`derived_from` reference resolves by its own name. Sessions of one seat run in batch order; the two seats never share a directory;
independence between seats is asserted per dispatch (same custody, same confinement, no other seat's output in the inventory), not
inherited from the first.

## 4. What the seal between batches preserves — and what it does not

After a session exits, the custodian runs `seal` for batch k. The seal binds: the partition digest; the owned texts' digests, verified
against the manifest at sealing; the four artefacts' digests; and the digest of the predecessor seal (k−1). It refuses to seal batch k
before k−1, and refuses to re-seal. It preserves the bytes of what was committed and the order of commitment. **It does not prove that
all owned texts were read, that the nominated reader produced the work, or that a later session could not reach an earlier batch's
files** — a later session is not FURNISHED them; an out-of-directory alteration is DETECTED at join, which refuses any artefact whose
digest differs from its seal: detection, not prevention, the same floor C4 states for the seats. The seals file itself lives outside
any session's write authority, with the custodian.

## 5. The join, as a pure function of fixed inputs

`join <partition> <seat_dir> <seals> <manifest> <prefix>` verifies the partition and manifest binding, each seal's owned-file and digest
lists against the partition, every artefact digest, the complete ordered predecessor chain, and the absence of missing or extra batch
seals; verifies that every candidate and every ledger claim is OWNED by its batch (a candidate citing another batch's text as its own
passage fails), that every ledger claim names an INCLUDED candidate of its batch and every input id begins with that claim's file and
`#`; verifies that every evidence `source_file` is a manifest row (any text, any batch); checks id uniqueness across batches and that
every `derived_from` resolves and the graph is acyclic;
concatenates in batch order without renaming; recomputes the declared counts; writes one candidate file, one exclusion file and one
ledger per seat with sorted keys. For fixed inputs and fixed code it is deterministic (a control checks identical bytes twice); it
performs no scholarly classification, and it does implement two policies — ownership and global identifiers — which are the ones stated
here. The pinned `census` then runs over the joined files and must PASS; the lane's `validate` runs over the joined ledger against the
FULL corpus and must PASS (that is where a cross-batch import machine-matches).

## 6. Why it is ONE census with ONE denominator read by TWO independent readers — what is checkable, what is not

- **One denominator, mechanically.** §1's inclusion rule is per passage; enumeration ownership is disjoint and exhaustive by
  `C1B_BATCH_COVERAGE` (every manifest text owned exactly once, owned bytes verified, every batch report access-proven), and the joined
  count is what `census` prints. Whole-text ownership preserves a claim's local context; cross-batch imports are not blocked by withheld
  evidence if each dispatch supplies and verifies all manifest texts as required — a dispatch check recording the availability and byte
  verification of all 89 texts per session is part of the run plan, since final ownership coverage alone does not verify earlier
  reference access, and neither coverage nor join verifies the lookup logs. What the mechanism establishes is one joined denominator; calling it one independently completed
  census additionally needs the reading, source-access and reconciliation evidence of the run record.
- **Two independent readers.** Each seat's joined files come from one engine under one packet across twelve sessions that never see the
  other seat's directories; the two joined files are reconciled claim by claim as V23 §2/§4 prescribe. Independence BETWEEN seats is
  retained per dispatch on the conditions in §3; what is new is that a seat's reading is not one memory.
- **What is lost, stated plainly.** Cross-batch consistency of one reader's judgement. The run log reports between-seat disagreement by
  batch, descriptively, with counts and denominators; **that rate does not identify within-reader drift** (both seats can drift together;
  batches differ in content). Reconciliation and C6 address the disagreements and failures their procedures detect; neither
  establishes cross-batch consistency.
- **The audit under the same partition (D7).** The auditor's enumeration is owned and sealed batch for batch under the same partition;
  its re-derivation stage reads cross-batch import sources under §1 of this file; `audit compare` then runs over the auditor's joined
  files against the sealed joined files. The comparison code is unchanged; sections 1 and 3 require equivalent evidence access and
  global identifiers; dispatch checks and the repaired join must verify their implementation.

## 7. Staged tooling and controls — STAGED, NOT INSTALLED

`r3c2_staged_d1d7/r3c2_batch_tools_STAGED.py` (lane-side, never given to a seat): `partition`, `seal`, `join`, `coverage`; pins in
`r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256` (this document prints no hash of its own). Controls in `r3c2_staged_tests.py`, run 2026-09-06 20:38 KST:
partition in manifest order with bytes and lines; seal order enforced (batch 2 before 1 refused), predecessor bound, re-seal refused;
join allows a batch-1 claim whose IMPORT evidence is a batch-2 line and the joined ledger validates against the full corpus, while the
same record CANNOT validate in a directory holding only batch 1's texts (the reviewers' finding, reproduced); join deterministic;
`census` PASSES over the joined files; coverage positive. Negatives, each asserting exactly one failure, each with a deletion probe: a
batch-2 candidate claiming ownership of a batch-1 text; a non-global id; a candidate-id collision; a ledger record naming a claim that is
not an included candidate; an input id not of the claim-file form; a broken predecessor chain; a root seal claiming a predecessor; sealed ownership differing from the
partition; a seal for a batch not in the partition; a cross-batch `derived_from` that resolves to nothing; evidence
cited from a non-manifest text; an artefact changed after its seal; a text owned by two batches; a manifest text owned by none; an owned
text whose bytes differ from the manifest; a batch report without the packet's `ACCESS_SHA`. Whole kit: `controls=111 passed=111 failed=0`,
`STAGED_TESTS=PASS`.

## 8. What accepting it changes about what the census can conclude

Per-claim outcomes and classes use the operative rules explicitly accepted for this run, including any accepted D1/D2 changes, over
the validated joined files. The report gains: the caveat that enumeration
was performed per preregistered ownership batch with all texts furnished; the between-seat disagreement by batch, descriptively; two
structural controls (`C1B_BATCH_COVERAGE`, `JOIN`); and the honest statement that within-reader consistency across batches is not
measured. Cost: 12 sessions × 2 seats (+12 for the auditor under D7), sequential per seat, parallel across seats; runtime unmeasured.
It is the difference between a census that could not run (one observed failure) and one that might — whether it can run is what
batch 1 is designed to test.

## 9. What adopting would take (not done)

A version amending C1's single-file schema, the dispatch record (one `ACCESS_SHA` per session, all texts furnished, ownership list
stated), §9's split rule and C6's frame with "a seat is a sequence of sessions under one packet; ownership is partitioned, access is
not; identifiers are global; the join is mechanical and pinned"; the batch tool pinned lane-side; packet rebuild; C0; two-seat gate;
the 11:11 approval procedure.

**Line for Duho:** accept / change (number of batches; row-order vs line-balanced partition; whether disagreement per batch is reported;
whether batch 1 must confirm size before batch 2) / defer. (Blocks a first run on the evidence of the limb-B death finding: the unbatched seat died; whether this batching is the remedy is what
batch 1 tests; the principal may choose another workable execution design.)

R3C2_BATCH_PREPARATION — UNADOPTED — revision 4
