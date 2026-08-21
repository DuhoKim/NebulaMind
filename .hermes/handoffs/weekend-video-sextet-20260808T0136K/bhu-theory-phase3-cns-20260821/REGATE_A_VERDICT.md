PASS_P3A_AUDIT

# Re-gate A — verification that the HOLD_P3A_LOADBEARING repairs actually landed

**Verdict: PASS.** All four required fixes landed as substance, not as relabeling. The gate's
upheld spine (H1, H2, H4, H5, the receipt, the open Track C) survived untouched — I diffed it
line-for-line, nothing was dulled to buy the fix. The receipt still reproduces, the JSON regenerates
byte-identically from the extractor, and the overclaim sweep is clean. One minor, non-blocking
residual is noted at the end; it does not rise to a HOLD and pre-dates this repair.

I was adversarial: I treated every fix as a suspected rename until the source or the diff proved it
was real. Below is what I checked and what I found.

---

## Check 1 — DIFF THE REPAIR (each of the four fixes landed as substance)

I diffed `TRACK_A_AUDIT.md.pre-gate-repair → TRACK_A_AUDIT.md` and `verdicts.json.pre-gate-repair →
verdicts.json`. The prose diff is surgical: **only** H3, the B-9/B-12/B-18 evidence cells, and a new
§5 gate-record changed. Nothing else in the audit moved.

- **B-18 out of any failing count — YES.** Pre: `load_bearing:true`, counted in
  `n_load_bearing_failing:7`, evidence "**Load-bearing**". Post: `load_bearing:false`,
  `unverified:true`, `unverified_why:"quoted from sources not yet read; neither a pass nor a
  failure"`, evidence "**Unverified, which is not a failure** — an unread citation." The failing
  count that contained it no longer exists. Not renamed — removed.

- **B-9 and B-12 demoted from load_bearing — YES.** Pre: both `load_bearing:true`
  ("the paper's justification for maximizing black holes at all" / "the claim that M_max cannot be
  lower, which fixes 1.5 as an optimum"). Post: both `load_bearing:false` with `secondary_why`
  ("motivating gloss, not on the falsifier's critical path (Gate A)" / "bounds M_max from below; the
  fired falsifier does not test that (Gate A)"). Table cells changed "**Load-bearing**" →
  "**Secondary** (Gate A)". The demotion is backed by the source (§II disclaimer line 52; §III
  "≈" title line 54; B-12's lower-bound direction), not asserted.

- **H3 softened to what the source supports — YES.** Pre-headline "Section III's argument … is not
  CNS's argument" ending "The entropy argument is a substitute, and it does not do the work the chain
  needs." Post-headline "Section III's entropy argument is a loose sentence, not a load-bearing
  step," which keeps the non-sequitur criticism, cites the "≈" title and §II disclaimer, points the
  CNS link at B-17/B-18, and explicitly withdraws the "does not do the work" overstatement. (Detail
  in Check 4.)

- **`n_load_bearing_failing` retired, not renamed-but-equivalent — YES.** Pre fields:
  `n_load_bearing:7`, `n_load_bearing_failing:7`. Post fields: `n_load_bearing:4`,
  `n_load_bearing_imported:4`, `n_unverified:1`. This is **not** a rename: the failing-7 set was
  {B-2,4,5,17} ∪ {B-9,B-12 UNSUPPORTED} ∪ {B-18 unverified}; the imported-4 set is {B-2,4,5,17}
  only. Different cardinality (7≠4) *and* different semantics — "imported" states the epistemic fact
  (cited, not derived here) with no pejorative, where "failing" was the rhetorical number the gate
  objected to. A new contract line was added: *"There is no failing count. An imported citation is
  not a defect in a 4-page note, and an UNVERIFIED row is an unread source, not a failure. Do not
  derive one."* The problem was retired, not relabeled.

## Check 2 — NO COLLATERAL SOFTENING (upheld findings intact)

Line-diff confirms **H1, H2, H4, H5, §2 (Track C), and every row other than B-9/B-12/B-18 are
character-for-character unchanged.** Specifically:
- **H1** (falsifiable content and derived content are disjoint) — untouched, still "the *falsifiable*
  content and the *derived* content of this paper are disjoint sets."
- **H2** — untouched, including the sharpest clause: "**this paper never cites Smolin 1992, CQG 9,
  173**" (I confirmed against the 24-entry reference list in `blr_clean.txt` lines 209–291: refs (5)
  Smo97 book and (6) Physica A 340 (2004) 705 are present; **Smolin 1992 CQG is nowhere**). Not
  softened.
- **H4/H5** — untouched.
- **Track C** (§2 lines 90–93) — untouched; "still an open question after this audit, not a settled
  one. That is Track C's job." remains.

The only load-bearing-row wording nudge is B-2's `load_bearing_why` "asserted by citation" →
"imported by citation"; both mean not-derived-here and the row stays load_bearing:true. No finding
was dulled to purchase the repair.

## Check 3 — THE COUNT IS NOW HONEST

`verdicts.json` reports exactly **4 load-bearing (B-2, B-4, B-5, B-17), all imported-not-derived,
plus 1 unverified (B-18)** — matching the prose in §5 and H1/§2.

I reran `extract_verdicts.py` in a lane-local temp dir (copied inputs; did **not** overwrite the
deliverable) and the regenerated `verdicts.json` is **identical** to the committed file
(`diff` on canonicalized JSON: no differences). Script self-report: `22 rows | load-bearing 4, of
which imported-not-derived: 4 | unverified: 1`, `declared load-bearing not found in table: none`.
The `source_sha256` in the JSON (`ea9804c2…891442`) equals `shasum -a 256 TRACK_A_AUDIT.md`, so the
tally is pinned to the post-repair prose, not a stale draft. (The pre-repair pair is likewise
internally consistent: `af2a2b97…40d4b`.)

No pre-computed pass-rate or failure-rate exists anywhere in the file, and the contract explicitly
forbids deriving one. **Non-blocking residual:** per-row `passing` booleans remain (12 true / 10
false across 22 rows), so a determined consumer could still hand-compute a raw "12/22" — but this is
intrinsic to any per-row verdict file, was present pre-repair and un-flagged by the gate (whose
objection was the *aggregated pejorative headline* n_load_bearing_failing, now gone), and is guarded
by the contract line "Do not render a pass percentage from this file." I note it for the record; it
does not warrant a HOLD.

## Check 4 — H3 STILL TRUE (re-read against blr_clean.txt lines 52, 54, 69)

The post-repair H3 is accurate — neither overstated nor over-retracted:
- Line 54 title "Maximization of Black Holes **≈** Maximization of the Entropy" — H3 quotes the "≈"
  correctly and reads it as signalling analogy.
- Line 52 "We are not in a position, nor is it our objective, to address the basic questions
  associated with the scenario…" — H3 quotes it faithfully; the authors do disclaim the mechanism.
- Line 69 "…Therefore, the maximum number of black holes does the best, so far, in moving towards
  equilibrium." — H3 truncates at "does the best," dropping only the trailing adverbial; no change of
  meaning (the gate validated this same truncation).

Crucially, **the valid criticism was NOT given away.** H3 still asserts the non-sequitur — "Read as
parameter selection that inference is a non-sequitur: the second law governs how a system evolves,
not which Standard Model parameters obtain," and "The non-sequitur stands as a criticism of one
sentence." What was withdrawn is only the load-bearing-failure framing ("substitute … does not do
the work the chain needs"), which the source refutes: BLR disclaim the mechanism (line 52), flag §III
with "≈" (line 54), and the CNS requirement "upper mass limit … be as low as possible" is sourced to
Smo04 (line 50), i.e. the link runs through B-17/B-18, not §III. The withdrawal is warranted and the
surviving criticism is exactly the defensible one. No over-correction.

## Check 5 — RECEIPT

`python3 receipts/r1_entropy.py` → `Eq.(2) coefficient : 1.0494e+77 k_B (dev 0.05%)`,
`BH / Fe-core ratio : 1.049e+20`, `R1 PASS` (exit 0). Unchanged and still passing.

## Check 6 — OVERCLAIM SWEEP

`grep -i "BHU is falsified"` over `TRACK_A_AUDIT.md` and `verdicts.json`: **absent.** No sentence
claims CNS is falsified or generalises to black-hole-universe cosmology. Every "falsif…" hit is
either about the *falsifier set* / *the chain as the source states it* (H1, §2, B-1, B-21, B-22) or
a direct source quotation — none asserts CNS itself is dead. The residual "7/7" and "failing" strings
appear **only** inside the new §5 gate-record, where they narrate what was *removed* ("removed from
the failing count," "`n_load_bearing_failing` retired," "No '7 of 7'"), and inside the contract line
that forbids the count. That is disclosure of the repair, not a surviving overclaim.

---

## Bottom line

The HOLD is cleared. The four fixes are substantive reclassifications grounded in the source, not
cosmetic renames; the upheld spine is intact; the count is honest and reproduces; H3 is now correctly
balanced with its valid criticism preserved; receipt and overclaim sweep are clean. **PASS_P3A_AUDIT.**

## Boundaries receipt
Reads only, within the lane, except: (i) the one file written — this verdict; (ii) a lane-local
`_tmp_regate/` scratch dir used to reproduce the extractor without overwriting the deliverable,
created and removed within the lane. No network. `portal.nersc.gov` untouched. Nothing committed,
published, or uploaded. "BHU is falsified" is false and is not said here.

— Re-gate A reviewer, fresh one-shot, 2026-08-21 17:54 KST. Cross-engine to Track A's author (Tori)
and to the first Gate A reviewer. Signed. Findings only; nothing fixed.
