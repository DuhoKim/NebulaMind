# R3C2 — batch reading for the limb-B corpus problem: PREPARATION, UNADOPTED (2026-09-06 20:01 KST)

**Status.** An execution question, kept out of the clause candidate so Duho can rule on it separately. Nothing adopted, frozen,
dispatched or run. The finding it answers: `R3C2_LIMB_B_DEATH_FINDING_20260906.md` (one seat cannot hold 89 texts / 106,676 non-blank
lines in one session; the void seat B died after 3 h 45 min improvising subagent chunks). Option A of that finding, specified here
well enough to judge, with staged tooling and controls.

## 1. What a batch is — concrete, computed from the real manifest

The 89 enumerable texts of `R3C2_CORPUS_MANIFEST.md` (sha256 `300d4da144d96ae9f1390c9018e919ae1ba6cf00be9f45ad36fdccfdcfbf9b24`), in manifest row order, partitioned into 12
batches whose sizes differ by at most one (five of 8, seven of 7). Computed by the staged tool, printed, pinned
(`r3c2_staged_d1d7/partition_12_of_89.json`, sha256 `e8ca431c9066aea5ab9c5accd05bb691f72ff5847dea24747991fd8e9bc9510a`):

```
batch 1: rows 1-8 (8 texts)
batch 2: rows 9-16 (8 texts)
batch 3: rows 17-24 (8 texts)
batch 4: rows 25-32 (8 texts)
batch 5: rows 33-40 (8 texts)
batch 6: rows 41-47 (7 texts)
batch 7: rows 48-54 (7 texts)
batch 8: rows 55-61 (7 texts)
batch 9: rows 62-68 (7 texts)
batch 10: rows 69-75 (7 texts)
batch 11: rows 76-82 (7 texts)
batch 12: rows 83-89 (7 texts)
```

Twelve, not eight: the seat that died was handling sets of eleven; seven or eight texts (roughly 8–10 thousand non-blank lines) is
what one session can read completely and still do the arithmetic. The partition is a function of the manifest and the number 12
alone; anyone can recompute it and must get the same bytes.

## 2. What a session is

For each batch k, each seat is a fresh process of the same engine under the same kernel profile, in a working directory holding the
packet, the brief, the pinned scripts, the manifest and ONLY batch k's texts. It prints its own `ACCESS_SHA` (= the packet digest), runs
the brief's steps over its texts, and writes `candidates_b<k>.json`, `exclusions_b<k>.json`, `ledger_b<k>.json`, `SEAT_REPORT_b<k>.md`.
A seat's sessions run in batch order; the two seats' sessions never share a directory. The seat itself never joins anything.

## 3. What the seal between batches preserves

After a session exits, the custodian runs `seal` for batch k, which records the digests of its four artefacts in `seals.json` BEFORE
batch k+1 is dispatched, and refuses to re-seal a batch. The seal preserves: the batch's text list (fixed by the partition), the bytes
of its four artefacts, its `ACCESS_SHA`, and the dispatch order. A later session cannot alter an earlier batch's files because they are
not in its directory; the lane never edits them; `join` refuses any artefact whose digest differs from its seal. The seal does not
preserve, and does not claim to, the reader's memory across sessions.

## 4. The join, as a pure function

`join <partition> <seat_dir> <seals> <prefix>` verifies every seal, verifies that every candidate in batch k cites a text OF batch k
(a candidate citing another batch's text fails `JOIN`), prefixes every candidate id, claim id, input id and `derived_from` entry with
`b<k>_`, concatenates in batch order, recomputes the declared counts, and writes one candidate file, one exclusion file and one input
ledger per seat, with sorted keys — the same inputs give the same bytes (a control checks it). It has no parameters and no judgement.
The pinned `census` then runs over the joined files and must PASS: that is the seat's denominator.

## 5. Why it is still ONE census with ONE denominator read by TWO independent readers — checkable, not asserted

- **One census, one denominator.** §1's inclusion rule is per passage and §2's arithmetic is per claim; neither consults any other
  text. Therefore the enumeration of the whole corpus equals the union of the enumerations of any partition of it, PROVIDED every text
  is in exactly one batch and no batch cites outside itself. Both provisos are controls, not assumptions: `C1B_BATCH_COVERAGE=PASS` iff
  the union of the batch text lists equals the manifest with no duplicate and every batch report prints the packet's `ACCESS_SHA`;
  `JOIN=PASS` iff every seal matches and every candidate cites its own batch's text. The denominator is the count `census` prints over
  the joined file; every §4 class, the 10% dispute rule and C6's selection are computed over the joined files exactly as V23 states.
- **Two independent readers.** Each seat's joined files are produced by one engine under one packet across its 12 sessions; seat A's
  sessions and seat B's never see each other's directories; the two joined files are then reconciled claim by claim as V23 §2/§4
  already prescribe. Independence BETWEEN seats is unchanged; what is new is that a seat's reading is not one memory.
- **What is lost, stated.** Cross-batch consistency of one reader's judgement. It is measured, not assumed: the run log reports the
  seat-A/seat-B disagreement rate per batch, so drift shows as a rising rate in later batches; the existing dispute stops apply over
  the union. The two-seat reconciliation and the C6 audit are already the design's answer to inconsistency.
- **The audit (D7) under the same partition.** If the stronger D7 is accepted, the auditor's own enumeration is read under the same
  12-batch partition and the same seals; `audit compare` then runs over the auditor's joined files against the sealed joined files.
  The partition changes nothing about what the audit compares.

## 6. Staged tooling and controls — STAGED, NOT INSTALLED

`r3c2_staged_d1d7/r3c2_batch_tools_STAGED.py` (sha256 `bf3a3524884c44b6a41fb9bc62f59b39b0df5042b5b26cf1048f1f7b542f1581`), lane-side, never given to a seat: `partition`, `seal`, `join`,
`coverage`. Controls in `r3c2_staged_tests.py` (sha256 `89c0202fc9283233ad349025a67959dad7b532234825ac7db343a69bdfbb165a`), run 2026-09-06 20:01 KST: partition 5→2 in manifest order; seal; re-seal
refused; join verifies seals and scope, renumbers, recomputes; join deterministic (identical bytes twice); the pinned-form `census`
(staged copy, sha256 `60a191f36a757c6c15e01f3e778518c8e20935bde464deab3e0d9e65fac082ff`) PASSES over the joined files; `C1B_BATCH_COVERAGE` positive. Negatives, each asserting EXACTLY one
failure: a batch-2 candidate citing a batch-1 text; an artefact changed after its seal; a text in two batches; a manifest text in no
batch; a batch report without the packet's `ACCESS_SHA`. Deletion probes: removing the scope, seal, duplicate, missing-text or
ACCESS_SHA check turns the matching negative into PASS. `STAGED_TESTS=PASS` (37/37 over the whole staged kit).

## 7. What accepting it changes about what the census can conclude

Nothing about the claims. The report gains one caveat ("enumeration was performed per preregistered batch; per-batch seat
disagreement rates: …") and two controls (`C1B_BATCH_COVERAGE`, `JOIN`). It is the difference between a census that can run and one
that cannot. Cost: 12 sessions × 2 seats (+12 for the auditor under D7), sequential per seat, parallel across seats.

## 8. What adopting would take (not done)

A version amending C1's single-file schema, the dispatch record (one `ACCESS_SHA` per session), §9's split rule and C6's frame with
"a seat is a sequence of sessions under one packet; the join is mechanical and pinned"; the batch tool pinned lane-side; packet
rebuild; C0; two-seat gate; the 11:11 approval procedure.

**Line for Duho:** accept / change (batch size; number of batches; whether disagreement per batch is reported) / defer.
(Blocks a first run: without it, no seat completes.)

R3C2_BATCH_PREPARATION — UNADOPTED
