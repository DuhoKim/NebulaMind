CSEAT_AMEND_REPAIR_COMPLETE 161547400e47ed66df616ba14756d9ab066c547f54b39bc161e6b4eaa26478c0

# ACQ science seat (claude-seat) — pre-K-8 amendment, Revision 2 (repairs applied)

**2026-08-20 20:32 KST.** `AMENDMENT_PREK8_20260820.md` · SHA-256
`161547400e47ed66df616ba14756d9ab066c547f54b39bc161e6b4eaa26478c0` (860 lines; Revision 1 was
`e832a341…`, 562 lines). Edited in place. Frozen prereg re-verified `b06901c8…`, mode 444,
unmodified.

**Status: DRAFT FOR KUN'S RE-GATE. Nothing frozen, accepted, published, committed, or pushed.**

Gate answered: `KUN_GATE_A_AMENDMENT_20260820.md` (`HOLD_PREK8_AMENDMENT`, four blocking repairs).
The gate is detailed and fair; its Check 3c and 4c findings are correct and are the two that
mattered.

## The four repairs

- **R1 — origin claim qualified everywhere.** §1.1 now separates by name the **scientific sign
  convention** (frozen 2026-08-14 by BS-5 §3; restated at AM-A.1, not added) from the **operational
  polarity** of the frozen weights (frozen **nowhere** before 2026-08-20; AM-A.2 is new). The chain
  conclusion, AM-A.1's and AM-A.2's headers, and Link 4 are rewritten; Link 4 now states that it
  could have come out inverted, in which case BS-5 §5 required a synthetic-side correction before
  the crossing. The document now says explicitly: **no sentence may be read as claiming the
  operational polarity was frozen on 2026-08-14.**

- **R2 — verification re-pointed.** Now pinned to
  `_rehearsal_20260820/attempt3_hold/hc1h_neyman_priors.json` · `4b6b7130…`, with a boxed citation
  warning that the **root** path was overwritten by the later N=20,000 rerun (now `e9f47597…`), holds
  entirely different strings, and does **not** contain the quoted values.

- **R3 — pool-source contradiction resolved in one direction.** **The full-pool freeze stands**, and
  for a stronger reason than Revision 1 gave: **option (i) is not executable in production at all.**
  In the rehearsal the campaign could serve as prior source only because every object was synthetic
  and carried a `truth_sign`; in production the campaign *is* the real population, no real object has
  truth, so `c_s` is undefined over real rows. Freezing the campaign would freeze a rule that cannot
  run — and the defect would surface after the crossing, where F-9 forbids repair. The byte-for-byte
  claim is downgraded to what it proves (the **formula and its Decimal serialization**, on real
  integer inputs, through the pinned code path) and Revision 1's "demonstrated to be exactly
  executable by the existing pinned code path" is **withdrawn**. New **AM-B.3** requires an
  end-to-end full-pool demonstration through the unmodified allocator, hash-pinned and gated, before
  the crossing — with its own residual stated: it must use synthetic cutpoints, since real cutpoints
  cannot exist pre-crossing.

- **R4 — line-pin corrected, merge surface restated.** §3.4 item 4 now names all five nine-stratum
  invariants (`hc1h_statistics`, `hc1h_verdict`, `allocate_neyman` key-match, balanced injection
  allocator, sealed-commitment recording) in a table giving line numbers **in both revisions**, and
  states that a conforming merge is a **NEW hash-pinned harness revision with its own fixtures and
  its own gate**, not a patch — with **AM-C.2 governing until one exists**.

## One correction back to the gate (§3.7 of the amendment), with evidence

Ruling (ii)'s line-pin attribution is **inverted**, and I record it rather than silently adopting a
false correction. From the git object store, not from a working file:

```
git show 199c3168:…/prereg/handcheck/nm_handcheck.py | shasum -a 256
  -> cc88fa5e…  (the rehearsal-pinned SHA)   line 45 HC1H_STATES, line 46 HC1H_STRATA
current working copy
  -> 65c04377…                                line 42 import HC1H_STATES, line 49 HC1H_STRATA
```

So **45–46 is correct for the pinned `cc88fa5e…`; line 49 belongs to the current `65c04377…`.**
Corroborated systematically: every pin in the gate (`:597 :710 :807 :1018 :1417 :1457 :1468 :3187
:3205`) resolves in `65c04377…`; every pin in Revision 1 (`:45–46 :691–693 :701–702 :1000 :3169–3170
:3179–3180 :3186–3187`) resolves in `cc88fa5e…`. The two documents read different revisions. The
cause is identifiable: `HC1H_STATES` moved into `committee_state_vocabulary.py` at the prereg root —
the plumbing lane's repair of rehearsal finding 8.

**This does not diminish the repair; it sharpens it, and the material finding is Kun's.** A bare line
number is revision-ambiguous whichever reader was on which revision — that is a real defect in my
citation practice, now fixed (every code citation carries its SHA). The merge-surface finding is
correct in full and is why §3.4 item 4 was rewritten. And it surfaces a **new open item**: the
rehearsal's entire evidence base was produced against `cc88fa5e…` while the tree now holds
`65c04377…`, so **nothing establishes that the current revision preserves the rehearsal's
behaviour**. AM-B.3 and AM-C.3 must both be evaluated against the revision hash-pinned **at the
crossing** (§5 item 6).

## Rulings incorporated (§4, recorded as decided, not re-argued)

- **(i) P7 wording — APPROVED** as a shape change, conditional on (ii): *"`|S|` strata (3 ≤ |S| ≤ 9)
  plus the pre-merge populations and the full merge record."* The gate's correction is recorded:
  declining the wording change does **not** force AM-C.2 unconditionally — what governs is the
  implementation precondition. My old escalation on this point is withdrawn as answered.
- **(ii) Merge gateable in principle, not on the evidence presented** — new gated revision required;
  **AM-C.2 governs until it exists**; the crossing is **not** to be held hostage to it.
- **(iii) AM-A.4's FAIL_CLOSED consequence — NOT ENTAILED.** Accepted and **frozen as a new
  addition, AM-A.6** (§1.7): a delivered raster whose PC-3 parity log does not match the anchored
  North-up/East-left `REVERSING` orientation is **FAIL_CLOSED and excluded**, never reoriented,
  evaluated at ingest on WCS metadata alone, before and independent of χ, counted as its own line in
  the P6 funnel. Revision 1's "already entailed" framing is **withdrawn**. Scope flagged: this is a
  §6 custody exclusion, not an I-5/BS-6 science cut — Kun's note wanted if he reads it otherwise.

## Recorded, not changed

Gate's non-blocking note: pilot mode allocates 10 per stratum without calling `allocate_neyman`
(`cc88fa5e…`:691–693 / `65c04377…`:710), so a stratum under 10 under-fills silently and surfaces
only as a count mismatch. **Flagged for the plumbing lane's separate gate (§3.6); no amendment
change on account of it.**

## Still open for Kun

`AM-A.5` (`sign(0) = 0`) — offered as a reading of F-1, not an amendment; the gate did not rule. If
it is a parameter, it needs freezing before the crossing.

## Boundary

Real chirality labels computed: 0 · real χ read: 0 · real cutouts/tensors/positions/rows read: 0 ·
sky statistics: 0 · frozen files modified: 0 · network calls: 0 ·
publication/acceptance/freeze/commit/push: 0. Computation performed: SHA-256 recomputation;
read-only extraction of one historical blob from the local git object store (no checkout, no branch
or index change); decimal arithmetic on numbers already in rehearsal receipts. Files written:
`AMENDMENT_PREK8_20260820.md` (edited in place), this receipt.

Back to Kun to re-gate; Duho owns acceptance and the freeze.

— ACQ science seat (claude-seat), 2026-08-20.
