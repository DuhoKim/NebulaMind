# ADVERSARIAL GATE BRIEF — successor preregistration V8 (round 7)

You are an adversarial gate. REFUSE if you can. Rounds 1–6 refused V2–V7; V8 claims to
repair the union of both V5 refusals and adds three directed changes. A repair that responds
without repairing is a REFUSAL. New holes count as much as old ones.

**Context you are entitled to know:** the predecessor study was DECLINED BY SIGNATURE on
2026-08-25 and its sample archived; V6 is a fresh preregistration DRAFT whose drafting Duho
authorized the same day. Drafting only — no run, no fetch is authorized, and this text must
not assume any. If V6 anywhere assumes an authorization it does not have, that is a finding.

## Pin first (custody)

Compute and print sha256 of ALL THREE and verify before reviewing:
- `../PREREG_SUCCESSOR_DRAFT_V8_20260825.md` =
  `faea9047682e9de6dc7721bdf1f094f8c8947f0d35d9c455b46abdef292bcb39`
- `../ref/successor_ref_v4.py` =
  `979819048f59baef2773b448706e246edbb1f5de5a8180ac8ad3de2c15279d50`
- `../ref/FIXTURES_V4_20260825.out` =
  `70268cf5b325834ca8486101d69e2dc77b51f50aeb2ac018faa118248d5599eb`
Any mismatch: STOP, report, review nothing.

## Context (read-only)

`GATE_GPT56_SUCCESSOR_V7.md`, `GATE_CODEX_SUCCESSOR_V7.md` (this directory — V8 §10 traces
every finding); `../../SUCCESSOR_SCOPE_20260821.md` incl. Amendment 1;
`../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`;
`../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md`;
`../../VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md` (the lapsed spec whose battery and run
guards V6 claims to carry); anything under `../../` a claim cites. Do not read
`/Users/duhokim/NebulaMindData/`.

## Attack surfaces (minimum; add your own)

1. **Run the code.** `python3 ../ref/successor_ref_v4.py --fixtures` and compare to the pinned
   output (record your environment). Then attack the code as the definition: nondeterminism
   the fixtures miss; input regimes where a frozen function is wrong or fails OPEN; docstring
   claims contradicted by bodies (the no-BLAS claim, the banned-spawn claim, the
   two-random-calls-per-object claim); and any place the constitution claims more than the
   code enforces.
2. **The three directed additions.** (a) §2.4/BS-2m manifest closure — does the property plus
   check actually prevent the named 60,308-vs-60,310 defect, including at the footprint edge
   where the planner's neighbour rule matters, and can a lazy implementation satisfy it while
   still shipping a short manifest? (b) §2.1 bound release choice-point — can the Sep-5
   resolution genuinely slot in without reopening frozen text, and is branch-invariance
   checkable? (c) §1 citation/sign anchors — verify the bibcode/DOI/amplitude/axis against a
   source, and check that the published-minus-sign to our-plus-sign mapping is stated
   consistently everywhere it appears (this is a directional claim that has inverted lanes
   before).
3. **The power equality contract.** The Stage-P analytic null replaces an infeasible nested
   kernel. Attack it: is the exact-variance claim right; is normality adequate AT the 0.001
   decision quantile for realistic N and sign imbalance; is the PWR-EQ fixture's 5% tolerance
   defensible or does it hide a power misestimate; does anything let the analytic null leak
   into a production decision?
4. **Slot machine.** Walk every class-P and class-E slot: named producer, inputs available at
   that time, schema/digest, code symbol, what it blocks. Nothing pre-freeze may need
   post-freeze data. Every §-obligation needs a slot and vice versa (incl. BS-9's R1–R5 rerun
   and the runner prohibition, and BS-V's verdict/lock).
5. **Quotation fidelity** against V3-pred, BS6-pred, the lapsed spec and the scope amendment,
   byte-level where executable strings are claimed.
6. **Loopholes.** Laziest compliant reading of every MUST — especially BS-2c closure proofs,
   BS-2m's "frozen cutout planner" (named but not reimplemented — is that a hole?), Stage-C
   mask admissibility, the calibration halt, the blind-double reimplementation scoping, and
   the void rule's exemption clause.
7. **Inherited-defects section (§8).** For each of the eight, does the cited fix actually
   close it, and is any known predecessor defect MISSING from the list?

## Report (write ONLY your report in this directory)

`GATE_<YOURSEAT>_SUCCESSOR_V8.md`: pinned shas as computed; your environment; numbered
findings (severity, quote/symbol, why, minimal repair); verdict **PASS** (freeze-candidate
grade) or **REFUSED** (blockers named). Unbacked author statements under Testimony.


## Round-7 specific instructions

1. **Re-run every attack that succeeded in your round-6 report.** In particular: the
   self-consistent shortened parent, the shortened/unpinned brick universe, the zero
   half-size, the FixtureMask reaching Stage C or the production record, the monkeypatched
   guards, the `_perm`/`n_perm` bypass, the reduced-N verdict, the calibration-after-statistic
   ordering, the no-power `build_plan` path, the feasible allocation the allocator rejected,
   and the wrap rectangle. Any still succeeding is a REFUSAL and worth more than a new finding.
2. **NEW ARTIFACT IN SCOPE — the real-geometry receipt** `../real/REAL_GEOMETRY_RESULT_20260825.md`
   and the scripts in `../real/`. This is the first time this preregistration has touched real
   catalog data (authorized by Duho as catalog-only; no images, no chi). Attack it:
   - are the pinned digests actually those of the named files;
   - does the count oracle's left-join/zero-materialization claim hold on the real table;
   - is Var(cos theta) = 0.445201 reproducible, and does it agree with the frozen 0.4452;
   - is `real/greedy_fast.py` genuinely order-identical to the pinned `greedy_ledger`, and is
     40 random cases adequate evidence for a 270,577-brick production run;
   - does the reported selection (6,446 bricks, N_eq 120,006) actually satisfy the frozen
     requirement under the frozen rules, or does it depend on the fast path's shortcuts;
   - is 997/1000 with 77/77 boundary confirmations a sound Stage-P PASS, or can the
     confirmation band (10x the threshold) miss unsafe trials outside it?
3. **§10 discloses four things as NOT closed** (clean-room spec, BS-9 schema, BS-V lock, the
   pinned greedy not scaling). Do not count those as new findings; check instead whether
   anything ELSE is claimed closed that is not.
