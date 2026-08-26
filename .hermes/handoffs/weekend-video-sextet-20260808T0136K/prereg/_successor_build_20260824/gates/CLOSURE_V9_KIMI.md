# CLOSURE V9 REFEREE — KIMI

## Verdict

**CLEAR** — with conditions named below. The single v9 repair (my v8 F3) holds under dynamic
test on every path it claims: the isolation refusal now carries the full interpreter state
(measured in my own non-isolated run, not only in the suite's B04), `closure_receipt()` returns
the worker's provenance beside the result for PASS and REFUSE alike (every boundary REFUSE row
in both receipts carries `worker_provenance`; my own extra-keys closure agrees), and the two
rewritten claims now describe what the code does, with W03 and B04 asserting exactly that in
both receipts. My full production-uncached run reproduces the shipped receipt's
`stable_sha256` exactly — dictionary-equal stable objects, not hash-agreement by luck. The
required set re-derives independently at 12,117 with the plan result digest the ceiling order
cites, and the planner pin is measured unchanged since v6. Treating v9 as a fresh subject
found no regression: the fixture battery re-executes byte-identical, the subject diff is six
lines plus the worker filename, the worker diff is the F3 repair plus the residual paragraph
and a dead check's removal, and the only consumer of `closure_receipt()` in the lane is the
suite itself. New this round: the change record the brief names does not exist (second
consecutive round), the brief's question block is carried from v8 and still cites a probe
removed in v7, the repaired claims' "even a refusal" overstates coverage for the five
non-isolation early refusals, and the suite's own text still names stale versions. Carried and
re-verified rather than taken on trust: the six `varies` strings, the vacuous B06 hook, F05's
basis, the timeout/stdin/channel items, R06's thin payload, the unused environment guard, the
three fingerprint blind spots, the planner files' distinct reads, and the selection's missing
producer receipt (CODEX-V5 F6, upstream of this mechanism). None of my findings gives a
presenter who does not own the machine a path to a false acceptance through the production
path; all fail in the safe direction or sit inside the conceded machine-ownership class.

## Scope and custody

I ruled only on the v9 closure mechanism and the artifacts the brief names. I did not read
`/Users/duhokim/NebulaMindData/`. I did not inspect or mutate any live downloader. Apart from
this report and `_tmp_KIMI_*` / `CLOSURE_PROBE_V9_*_KIMI*` artifacts in this gate directory I
wrote nothing; the pinned suite, subject, worker and fixtures were never modified (hashes
re-verified after all runs, below).

Independently computed SHA-256, each matching the receipt (per the brief's instruction, hashes
are taken from `CLOSURE_PROBE_V9_RECEIPT_20260826.json`, not from the brief text — the brief's
own values are also correct this round):

- `../ref/successor_ref_v9.py`: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`
  == receipt `stable.subject.sha256` and == the worker's `SUBJECT_SHA256` pin.
- `../ref/closure_worker_v9.py`: `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`
  == the `worker_sha256` recorded through the boundary in G01's `self_check`.
- `../ref/FIXTURES_V9_20260826.out`: `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`
  == receipt.
- `closure_probe_suite_v9.py`: `b218aa998ac8ef97a0c4c933d73068d18ff45ce3553cb7bc80f1fe59be8c91d7`
  == receipt.
- Frozen v8 (freeze record `FREEZE_CLOSURE_V8_20260826.md`, all matching, read-only preserved):
  subject `1bec5c28…`, worker `24505725…`, suite `382a078f…`, fixtures `fab32ba2…`,
  my v8 report `47d24f32…`. v4 `8191c42b…` and v5 `02237163…` subjects unchanged, so those
  reports stay legible against their pins.
- Frozen planner files (byte-identical to my v6 record, which is what the planner digest binds):
  `../_objmanifest_20260820/build_object_manifest.py` `c63030e2…`, `../adapter/nm_brick_cutout_adapter.py`
  `267b2a93…` (== the objmanifest's own `PINNED_ADAPTER_SHA256`), `../_cutout_runner_20260820/cutout_runner.py`
  `ccb9b8fe…`.

Pinned-artifact checks on disk: count table 270,577 rows totaling 832,393 == pins; selection
`(6445,)` int64, 6,445 unique == pin; parent receipts 13 chunks, rows sum 65,060, bricks sum
6,445, `output_sha256` == the parent pin.

Interpreter: `/usr/bin/python3`, Python 3.9.6 (CLT), macOS arm64.

## Reproduction (question 1)

**Yes — exactly, for the same mode.**

- My full `production-uncached` run (`CLOSURE_PROBE_V9_RUN_KIMI.out`, receipt
  `CLOSURE_PROBE_V9_RECEIPT_KIMI.json`, 2,253.9 s): 34/34 conforming, no non-conforming probe,
  no error-typed probe, verdict SUITE-CONFORMING, hooks 13 declared / 13 ran / all_ran true.
- My `stable_sha256`: `687a4543d14b48120a84d6e4fbefb41826ec2f7a9a9cc9a34e0a63c6e29e9131` —
  **identical to the shipped receipt's**. The two `stable` objects are dictionary-equal
  (recursive element-wise diff: 0 differences across all 34 probe rows, pins, digests and
  summaries), and each receipt self-hashes consistently (canonical rehash of each stable block
  == its stored hash, both ways).
- The v6 F2 mechanism stays dead: F03/F04/F05's refusal payloads read `$RUN/counts_link.csv`,
  `$RUN/counts_fifo.csv`, `$RUN/counts_nofollow.csv` in the hashed structure; `normalise_deep()`
  rewrites the run dir out of `result`, `message` and `verify_note`
  (`closure_probe_suite_v9.py:780-794`, applied at `:882-884`). This is the third consecutive
  round the hash reproduces; the repair is confirmed, not out-voted.
- Scoping remark carried from v7/v8, still true: the hash is a **per-installation** witness.
  G01's `self_check.worker` carries the worker's absolute path and B04's payload the real
  non-isolated `sys.path` by design ("recorded, not summarised"), so a different home directory
  legitimately yields a different stable hash. On this machine, same mode, it reproduces
  exactly.

## Numbered findings

### F1 — MINOR (bookkeeping, second consecutive round) — the change record the brief names does not exist

**Symbol/line.** Brief line 70: "`CLOSURE_REPAIR_V9_20260826.md` is the change record. Read it
as a claim to be checked." Brief line 57: "this brief is regenerated, and
`CLOSURE_REPAIR_V9_20260826.md` exists." A `find` over the whole `NebulaMind` tree returns no
such file; `gates/` holds repair records for the base round, V6 and V7 only.

**Why it fails.** The brief points the referee at an artifact that was never written — the
exact shape of my v8 F1, in a round whose own preamble says "you have twice found a finding
that went unlisted." The brief's "What changed, and what is claimed" section is the de facto
record, and I checked it as the claim: every sentence verifies against the v8→v9 diffs (the
interpreter-state capture moved before the isolation gate, `closure_receipt()` attaching
provenance on both paths, W03/B04 as the asserting probes, the residual paragraph's new
contents). But a reader following the evidence list hits a dead pointer, and the sentence
"naming it because you have twice found a finding that went unlisted" now sits beside a third.

**Smallest sufficient repair.** Write `CLOSURE_REPAIR_V9_20260826.md` (the brief's change
section plus the not-fixed list is already the content), or amend the brief to name the section
as the record.

### F2 — MINOR (stale brief content, carried from v8 F2) — the question block is v8's verbatim and still cites probe B03, removed in v7

**Symbol/line.** A diff of the v8 and v9 briefs' "Questions to answer" blocks shows exactly two
changes: "33 probes" → "34 probes" and the report filename. Question 2 (line 107) still reasons
from "B03 does the same thing without the boundary and expects the opposite" — but B03 exists
in no suite since v6 (`closure_probe_suite_v6.py:298`; dropped in v7; absent from the v7, v8
and v9 suites alike). This is the third consecutive brief that cites it after removal; my v8
report (F2) named the same citation, and my v7 report answered the question without noticing
the removal. Question 6 (line 117) says "Do the five fixes hold … B06, B07 and F05 are new
probes for F3, F6 and F5 … treat v7 as a fresh subject rather than a diff" — v9 has ONE fix
(my v8 F3) and its new probe is W03, with B04's strengthened hook; "v7" should read "v9".

**Why it fails.** The evidence-list half of my v8 F2 is fixed (all four brief hashes are
correct this round — measured). The question half is not: a seat answering question 2 against
the suite finds no B03, and the in-process core's non-custody still has no dynamic control
anywhere — the point my v8 F2 made stands unaddressed (B01/B02 evidence the boundary side;
the core side rests on the subject's own docstring). The stale "five fixes"/"v7" wording is
smaller: it misdescribes the round's content to anyone who reads the brief before the record.

**Smallest sufficient repair.** Either restore B03 (one probe, ~140 s, asserting the in-process
core reads the caller-nominated table) or strike the citation from question 2 and record the
removal; update question 6 to the round's actual fix list.

### F3 — MINOR (wording precision, the class this round exists to fix) — "even a refusal carries it" is true of the isolation refusal and every closure refusal, but not of the five other early WORKER-ERROR refusals

**Symbol/line.** Worker docstring (`closure_worker_v9.py:20-24`): "the interpreter state --
the flags and the full sys.path -- captured before the isolation gate so that even a refusal
carries it." Suite `not_covered` entry 1 (`closure_probe_suite_v9.py:66-69`): "and so does a
refusal, since the interpreter state is captured before the isolation gate."

**Why it fails — precisely.** The claim is now true where v8 needed it true: my own
non-isolated worker run produced `WORKER-ERROR` carrying `python`, the three flags,
`pinned_site_dir` and a 7-entry `sys_path` (`_tmp_KIMI_v9_noI.json`), and every closure REFUSE
through the boundary carries `worker_provenance` (shipped and my receipt rows R01/R02/R06/R08;
my own extra-keys worker closure refused with full provenance). But the five OTHER early
`fail()` sites carry no interpreter state: `subject missing` (`closure_worker_v9.py:104`),
`SUBJECT DIGEST MISMATCH` (`:117-119` — B05's receipt row has only `subject_pin` and
`subject_sha256`), `stdin is not JSON` (`:124`), `stdin must be … 'manifest'` (`:126`), and
`'manifest' must be a JSON array or null` (`:131-133` — B07's row has only `manifest_type`).
Read strictly, "even a refusal carries it" covers those receipts too, and it does not. The
direction is fail-safe — the refusal that v8 silently stripped is the one now carrying the
state, and nothing here hides trust — but a round whose purpose is making two sentences true
should not leave the same sentence shape half-true on the same file.

**Smallest sufficient repair.** Pass `**interpreter` into the remaining five `fail()` calls
(one argument each — the state is already built before all of them), or narrow the two
sentences to "the isolation refusal and every closure refusal carry it."

### F4 — MINOR (record text staleness) — the suite's pinned text still names v6/v7/v8 where it means v9

**Symbol/line.** `not_covered` entry 2 (`closure_probe_suite_v9.py:76-77`): "and v7 does not
close this." Entry 8 (`:87-88`): "KIMI-V7 F3, F4 and F5, which are NOT fixed in v8" — v9 now,
and the brief's own not-fixed list confirms they remain unfixed. The suite docstring
(`:2-35`) still titles itself "CLOSURE PROBE SUITE V6", describes "WHAT CHANGED SINCE V5", and
shows usage `python3 closure_probe_suite_v6.py` — carried from the v8 file, where it was
already stale.

**Why it fails.** Cosmetic, but the receipt pins these strings verbatim: the record a gate
reads says the wrong version in three places, in a lane whose recurring defect is exactly
records drifting from the mechanism.

**Smallest sufficient repair.** Update the three strings (and the docstring header/usage) to
the file's own version.

### F5 — MINOR (carried from v8, re-verified this round, all admitted) — the named-not-fixed list is accurate

Each re-verified against v9 rather than taken on trust:

- The six S01–S05/U01 `varies` strings (`closure_probe_suite_v9.py:646, 658, 670, 683, 697,
  710`) still omit the `PINNED_*_REL` reassignment `Ctx.redirect()` performs (`:162-166`).
  KIMI-V6 F7, three times named, never fixed, in `not_covered` — the minimum I asked for.
- B06's verify hook is still `(True, "TypeError from the signature, not a forged receipt")`
  (`:325`); the probe body is the real assertion (acceptance → `AssertionError` → ERROR row →
  non-conforming), so conformance is sound and the hook asserts nothing.
- F05's basis still claims the no-window property; F05 is mechanically identical to F03 (both
  symlink the genuine table and require REFUSE + "symlink"), and the property's real evidence
  is the fixture's source assertion (`CLOSURE-SINGLE-OPEN`), re-executed by me this round,
  byte-identical output.
- No `timeout` on the worker subprocess (`successor_ref_v9.py:806`). Extra stdin keys ignored:
  re-tested this round — `{"manifest": [], "expected_outcome": "PASS", "comment": …}` produced
  the computed REFUSE with all 12,117 missing names and full provenance, exit 2
  (`_tmp_KIMI_v9_extrakeys.json`); the smuggled keys changed nothing, because the adjudication
  is computed, never caller-supplied.
- The dict-manifest refusal exits on the WORKER-ERROR channel (`closure_worker_v9.py:131-133`,
  code 1) rather than REFUSE (2); through `closure_receipt()` both become one
  `ManifestClosureError`, fail-closed.
- R06's structured result now carries `worker_provenance` (both receipts) but still lacks the
  closure numbers — objects, selected bricks and every digest are known by the time the None
  manifest is iterated (`successor_ref_v9.py:746`).
- `require_environment()` is defined (`successor_ref_v9.py:60`) and called at `:1596`, but by
  nothing on the closure path (`close_manifest`/`closure_receipt`/worker, `:632-833`).
- The three fingerprint blind spots stand — re-demonstrated live against v9: `math.radians`
  rebound to `lambda x: 0.0` and `adapter.tangent_plane_offsets` rebound to a stub each left
  `frozen_planner_digest()` at the pinned `1617af00…`; the `INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2`
  control moved the digest as designed; restore returns the pin.
- The planner's three files are verified and consumed by distinct reads on every use (my v8
  F4): `_frozen_planner()` re-executes from disk per call (`:266-277`), `frozen_planner_digest()`
  execs then reads bytes (`:384-389`), `close_manifest()` digests, plans on a fresh instance,
  re-digests (`:652, 655, 737`). In `not_covered` via the in-place-modification and
  retained-instance entries; the distinct-reads shape itself is still not named.
- The selection's binding remains a code pin with no producer receipt (CODEX-V5 F6, upstream).

## Answers to the referee questions

1. **Reproduction.** Yes, exactly — see Reproduction above: identical `stable_sha256`,
   dictionary-equal stable objects, both receipts canonically self-consistent, the v6 cause
   confirmed repaired for the third consecutive round, with the per-installation scoping
   stated.
2. **Does the process boundary establish I1?** For the demonstrated attack class, yes: B01/B02
   poison every artifact pin in the presenter's own process and the worker's receipt still
   reports the true digests (`4e4ec45d…`, `425a42c3…`) and the true 12,117, with hooks
   asserting exactly those values. It is a real custody boundary, not a longer path to the
   same trust — with the terminal trust outside both processes: the receipt self-reports its
   digests, and the comparison "no code inside either process can perform for itself" (the
   worker's own words) is these referee rounds re-running the suite, which is the right shape.
   The stated site-packages residual is **not** the only residual, measured this round: (a)
   the stated residual itself — under true `-I` plus the one pinned add-back, the CLT system
   site-packages precedes the add-back and numpy, astropy, erfa, scipy, yaml (and packaging,
   dateutil, astropy_iers_data) all resolve from the unpinned user site dir; the sidecar's
   bytes are pinned, its parser is not — the worker docstring's enumeration is accurate; (b)
   the `.pth` injection channel in the CLT site-packages remains open under `-I` (currently
   inert: `distutils-precedence.pth` only; the user site's `__editable__.astro_agent` .pth is
   NOT processed under `-I`, and the worker's manual `sys.path.append` processes no `.pth`
   either — measured; this channel is unnamed in `not_covered`); (c) the planner's three
   files load from unpinned lane paths with re-execution windows (F5/carried F4); (d) the
   worker's own code is loaded by the interpreter before it can hash itself — self-reported,
   externally witnessed only (my on-disk hash equals G01's record); (e) the in-process core's
   non-custody has had no dynamic control since B03's removal in v7 (F2). B03, which the
   brief's question cites, does not exist.
3. **The reachable fingerprint (I2, I5).** Unchanged by v9 and re-verified: it binds the three
   planner files' bytes, the adapter pin, the prefilter, both entry callables'
   bytecode/defaults/kwdefaults/closures and walkable pure-Python globals by value, and
   re-checks after the plan (my run reproduces N05's `1617af00… → 83f9abd7…` on the timed
   mid-plan mutation, and the probe proves the mutation fired). It still cannot see — each
   re-demonstrated live this round, not argued: module objects' contents (`math.radians`
   rebound: digest unmoved), helpers reachable only through class methods
   (`tangent_plane_offsets` rebound: unmoved), C callables (type name only), the retained
   objmanifest instance (`not_covered`'s last entry), and anything reverted before the
   post-plan digest. Its cross-process stability **does** still come partly from ignoring
   these: `_stable_repr` (`:286-298`) reduces every non-primitive to its type name precisely
   so that no memory address enters the digest — stability and blindness share a root cause,
   as `not_covered` states (with a stale version reference, F4). In the worker these blind
   spots bite only at import time, which is the stated site-packages residual.
4. **Verified-bytes custody (I5).** Real for the artifacts: one open
   (`O_RDONLY|O_NOFOLLOW|O_NONBLOCK`), `fstat` regular, hashed as read, parsed from that
   snapshot; the FITS sidecar re-parsed from a private byte-identical copy; F03/F04/F05 refuse
   the symlink and the FIFO. Real for the subject: one `read_bytes`, hash, pin-compare, then
   `exec(compile(subject_bytes, …))` (`closure_worker_v9.py:102-152`) — W02's equality holds
   in both receipts (2 events hashing, 2 through a whole closure). Remaining paths by which
   consumed bytes could differ from verified bytes: the planner files (F5/carried F4), the
   worker's own code (terminal trust, external comparison only), and the unpinned import-time
   parser stack (the stated residual). None is reachable to a presenter without write access
   to the pinned tree or the import-path directories.
5. **The single adjudication (I3, I4).** Correct on every shape exercised: R08 names both the
   duplicate (`0001m252`) and the omission (`0001m250`) with the hook asserting both counts and
   names; R01/R02/R05/R07 omissions with full counts (R02's hook asserts 100 names on the live,
   untruncated result — confirmed in my run; the receipt's `jsonable()` truncates lists at 8
   with counts preserved, a recording choice, while the worker's own JSON and the live result
   carry everything); R03 extra-only; R04 duplicate-only with missing 0; B07 one refusal at the
   boundary with `manifest_type` recorded (WORKER-ERROR channel — F5). The adjudication
   computes duplicates, missing and extra independently from the finished required set and
   reports them in one result (`successor_ref_v9.py:746-773`). Against v9's byte-identical
   adjudication I re-ran my v7 duplicated-extra shape (required set plus `0001p000` twice):
   one refusal naming duplicate 1 AND extra 1 with missing 0 (`_tmp_KIMI_v9_dupextra.out`). I
   found no candidate shape where one condition masks another. The residual is R06's thin
   closure-numbers payload (F5) — one refusal, provenance now attached, the numbers still not.
6. **Do the fixes hold, and did any of them break something?** The question's "five" is stale
   (F2); v9 has ONE fix and it holds, with no regression found, treating v9 as a fresh
   subject: (i) the interpreter-state capture sits before the isolation gate and needs no file
   reads (`closure_worker_v9.py:92-100`); my own non-isolated run carries the full state —
   independently of the suite's B04, which conforms with its hook asserting `isolated is
   False` and a non-empty `sys_path` in both receipts; (ii) `closure_receipt()` attaches the
   provenance to the result for PASS and REFUSE alike (`successor_ref_v9.py:823-833`) — W03's
   hook asserts `sys_path` non-empty, `isolated is True` and the add-back named, in both
   receipts; every boundary REFUSE row carries `worker_provenance`; (iii) the two rewritten
   claims now describe the code, and both say the probes establish it; (iv) the v8 dead
   second isolation check is removed, not half-kept; (v) R06's refusal gained provenance as a
   side benefit. Regression surface checked: the only in-lane consumer of `closure_receipt()`
   is the suite (grep); `close_manifest()`'s own result shape is unchanged (the worker adds
   provenance at the boundary); no BS-2m receipt is built from `closure_receipt()`'s result,
   so the new key cannot trip the exact-field schema; the fixture battery **re-executed by me**
   this round produces byte-identical output to the shipped `FIXTURES_V9_20260826.out`
   (`fab32ba2…` both ways, ALL FIXTURES PASS); the subject diff is six lines plus the worker
   filename; the worker diff is the F3 repair, the residual paragraph and the dead-check
   removal; my full 34-probe run conforms; the shipped receipt self-hashes consistently.
7. **Probe fidelity.** 13 hooks declared, 13 ran, `verify_hooks_all_ran` true — the meta-check
   is computed, not asserted, in both receipts. The hooks assert what their `basis` claims on
   the receipt's own rows: P01 (planner digest identical before/after), R02 (100 names on the
   live result), R04, R08 (both conditions named), B01/B02 (the true digests), B04
   (`isolated is False` and `sys_path` present — the F3 property), W01 (sentinel never
   written), W02 (event-count equality), W03 (provenance present and isolated — the F3
   property), N05 (both digests, differing), U02 (`incoherent_rows` == 5, the true total, not
   a cap). B06's hook is vacuous (F5); S01–S05/U01 under-declare the path reassignment (F5);
   F05's basis overclaims what a static symlink evidences (F5). Every probe that bypasses
   `closure_receipt()` declares so in its `direct` field (22 declared). B04/B05's comments
   recording the wording-change and wrong-reason episodes remain the right kind of honesty.
   Nothing else under-declares what it changes.
8. **Coverage.** Conditions bearing on I1–I5 that neither the 34 probes nor `not_covered`
   reach: (i) the five non-isolation early WORKER-ERROR refusals carry no interpreter state
   (F3) — the transparency claim's remaining gap, and no probe asserts their payload shape;
   (ii) the `.pth` injection channel in the CLT system site-packages under `-I` (channel open,
   currently inert, unnamed in `not_covered`); (iii) the in-process core's non-custody has no
   dynamic evidence anywhere — B03 removed in v7 and still cited by the brief (F2); (iv) the
   worker's self-hash terminal trust (stated in its own docstring; no probe can close it);
   (v) swap-and-revert of the planner files between digest and exec — the distinct-reads shape
   is carried near `not_covered`'s in-place and retained-instance entries but not named (F5);
   (vi) a mutation reverted before the post-plan digest (in-process only, carried from v6);
   (vii) the WORKER-ERROR→`ManifestClosureError` path through `closure_receipt()` carries the
   interpreter state at top level of the payload, not under `worker_provenance` — a shape
   difference no probe asserts (W03 covers the PASS path; the R probes cover REFUSE outcomes).
   Stated and confirmed open rather than missed: the three blind spots, the retained-instance
   gap, in-place artifact modification, the genuine race (structural evidence only), the
   selection's producer receipt, concurrency, the download itself, the timeout/stdin/channel
   items, R06's thin closure-numbers payload, `require_environment()`.
8. **The 12,117 figure.** Confirmed independently against v9. I imported the frozen planner and
   parsed the pinned parent directly — never calling `close_manifest`
   (`_tmp_KIMI_enumerate_v9.py`, `_tmp_KIMI_enumeration_v9.json`, 150.6 s): **12,117 distinct
   required bricks** from 65,060 objects; plan result digest
   `aaeaa9f37aabf1da6000a6ad07890cfe010677e301583530ba1a108833e3b3f1`; histogram
   `{1: 55566, 2: 8801, 3: 591, 4: 102}` — digest and histogram identical to the v5 measurement
   the ceiling order cites, to v6, to v7 and to v8; parent and sidecar hashes match their pins;
   the two historical probe objects are not rows of the pinned parent, as before. On the
   brief's "since the planner digest changed": measured this round — the planner **pin** is
   `1617af00…` in v6, v7, v8 and v9 alike (my v9 baseline == the pin == v8's value); it last
   changed at v5→v6 (`10cea7a6…` → `1617af00…`, because the digest binds more, per the
   subject's own comment at `successor_ref_v9.py:150-153`), and the plan **result** digest the
   ceiling cites (`aaeaa9f3…`) has been unchanged since v5. So the plan the ceiling pays for
   is unchanged. Ceiling arithmetic: 12,117 × 12.2 MB = 147,827.4 MB = 147.83 decimal GB ≈ the
   approved ≈148 GB; 12,117 / 6,445 = 1.880062.

## Failed attacks / positive evidence

- All pinned subject/worker/suite/fixture hashes reproduce against the receipt; the shipped
  receipt self-hashes consistently; my full run is dictionary-equal to it.
- B01/B02: presenter-process poisoning of every artifact pin changes nothing in the worker's
  receipt. B04: un-isolated worker refuses with interpreter state attached (in-suite and in my
  own run). B05: subject/pin mismatch refuses with both digests. B06: the v6 forge channel dies
  at the signature. B07: dict manifest refused with its type recorded.
- W01: poisoned environment + no `-I` → refusal and no sentinel, in-suite. W02: hash-only and
  full-closure event counts equal, in both receipts. W03: provenance present and isolated, in
  both receipts.
- N01–N04: pre-verification live mutations all move the digest and refuse; N05's timed
  mid-plan mutation is caught by the post-plan re-check with both digests reported, in both
  receipts, and the probe proves the mutation fired.
- F03/F04/F05: symlink and FIFO refused on the open itself.
- S01–S05, U01, U02: schema, sum, field, universe and coherence faults all refused, U02 with
  the true total (5).
- Extra stdin keys smuggled alongside the manifest change nothing; the adjudication is
  computed, and the refusal carries full provenance.
- Duplicated-extra manifest: one refusal naming duplicate and extra together, against v9's
  adjudication directly.
- The v6 blind-spot demonstrations still move nothing (F5) — confirming the stated open items.
- Fixture battery re-executed byte-identical; 12,117 and the plan digest re-derived without the
  closure code path; frozen planner files byte-identical to my v6 record.

## Evidence ledger

Content-read: the v9 brief; the required prior rounds (`CLOSURE_RECEIPT_GPT56.md`,
`CLOSURE_RECEIPT_CODEX.md`, `CLOSURE_V5_CODEX.md`, `CLOSURE_V6_KIMI.md`, `CLOSURE_V7_KIMI.md`,
`CLOSURE_V8_KIMI.md`); `FREEZE_CLOSURE_V8_20260826.md`; `closure_probe_suite_v9.py` (whole);
`../ref/successor_ref_v9.py` (pins, planner/fingerprint, loaders, closure core and receipt
regions: 100-260, 260-467, 470-833, `__main__`); `../ref/closure_worker_v9.py` (whole);
`../ref/FIXTURES_V9_20260826.out`; `CLOSURE_PROBE_V9_RECEIPT_20260826.json` (whole);
`CLOSURE_PROBE_V9_RUN_20260826.out`; `../acquire/DOWNLOAD_QUEUE_PLAN_20260825.md`; v8→v9 diffs
of subject (6 lines) and worker (the repair); v8→v9 brief-question diff. The change record the
brief names, `CLOSURE_REPAIR_V9_20260826.md`, does not exist — F1.

Commands/probes (artifacts as `_tmp_KIMI_*` or named receipts in this directory):

- `shasum -a 256` over every artifact listed in Scope and custody, before and after all runs.
- `python3 closure_probe_suite_v9.py --list` (34 probes; `not_covered` text inspected).
- Full production-uncached suite run → `CLOSURE_PROBE_V9_RECEIPT_KIMI.json`,
  `CLOSURE_PROBE_V9_RUN_KIMI.out` (2,253.9 s); recursive stable-object comparison against the
  shipped receipt (0 diffs); canonical rehash of both stable blocks; systematic row audit
  (mentions guards, hook declared/ran consistency, ERROR rows — none).
- Independent 65,060-object enumeration without `close_manifest` (question 8b):
  `_tmp_KIMI_enumerate_v9.py`, `_tmp_KIMI_enumeration_v9.json`, `_tmp_KIMI_enumerate_v9.out`.
- Fixture battery re-execution: `_tmp_KIMI_v9_fixtures.out` (byte-identical, hash equality).
- Direct non-isolated worker run (F3-fix proof on the refusal path): `_tmp_KIMI_v9_noI.json`.
- Extra-stdin-keys worker test with smuggled `expected_outcome` (computed REFUSE, provenance
  attached): `_tmp_KIMI_v9_extrakeys.json`.
- Blind-spot re-demonstrations against v9: `math.radians`, `tangent_plane_offsets`, plus the
  `INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2` control (output in session; F5).
- Duplicated-extra adjudication shape against v9's `close_manifest`:
  `_tmp_KIMI_v9_dupextra.out`.
- `python3 -I` sys.path inspection and module resolution for numpy/astropy/erfa/scipy/yaml/
  packaging/dateutil/astropy_iers_data; `.pth` inventory of both site-packages directories;
  user-site `.pth` non-processing under `-I` confirmed.
- Count table, selection and parent-receipt recounts against pins (270,577 rows / 832,393;
  6,445 unique int64; 13 chunks summing 65,060/6,445, `output_sha256` == parent pin).
- Receipt text searches and probe-id inventories across the v6–v9 suites (B03 timeline — F2);
  v7/v8/v9 brief question diff (F2); v8/v9 not_covered and docstring version strings (F4).

## Constraints and uncertainties

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not launch, authorize, inspect or mutate any downloader or transfer process; no image
  bytes were read. This report clears the closure mechanism; it does not itself fire anything,
  and the 148 GB ceiling stays tied to the confirmed 12,117.
- My suite run overlapped with my own enumeration, extra-keys and direct worker checks during
  its first half; per-probe timings agree with the shipped receipt's (N05 140.5 s vs 139.1 s;
  W03 142.2 s vs 139.6 s), and the timing-sensitive N05 ran after all my side jobs had
  completed. No timing-sensitive probe was affected.
- The stable hash is a per-installation witness (absolute paths in G01/B04 payloads);
  cross-machine equality is neither expected nor claimed.
- The duplicated-extra check ran in-process against `close_manifest` (the adjudication itself,
  not the boundary); the boundary path for that shape is covered by the R-family rows.

## Testimony

- `DOWNLOAD_QUEUE_PLAN_20260825.md` records the ≈148 GB ceiling tied to the 12,117 measurement,
  states the ceiling raise is not authorization to fetch, and states no image byte has been
  fetched. I read that record; I did not inspect live transfer state.
- The parent receipts' 13 chunk records carry TAP job URLs and per-chunk digests. I verified
  the envelope's pin, schema fields, chunk sequence and sums against the loader's checks (13
  chunks, rows sum 65,060, bricks sum 6,445, `output_sha256` == the parent pin); I did not
  re-query the remote jobs or reconstruct the parent from archived payloads.
- The brief's "~200 s per closure / ~45 min" estimate held (2,253.9 s full run under concurrent
  referee load; 150.6 s direct enumeration).
- Lane remnants: `runner_v9_kimi.log` was created empty by the dispatch script; this report is
  the seat's product. No other seat's v9 report is present in this directory as of writing.

**CLEAR**
