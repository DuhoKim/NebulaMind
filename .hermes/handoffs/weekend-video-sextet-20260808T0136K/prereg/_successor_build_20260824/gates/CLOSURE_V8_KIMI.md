# CLOSURE V8 REFEREE — KIMI

## Verdict

**CLEAR** — with conditions named below. Both claimed repairs hold under dynamic test: the
worker executes the subject bytes it verified (W02's counts are equal in the shipped receipt
and in mine, and I established the event anatomy independently), and the isolation check now
runs before anything is read or imported (my own poisoned-numpy run against the v8 worker
produced a structured refusal with the sentinel never written). My full production-uncached
suite run reproduces the shipped receipt's `stable_sha256` exactly — dictionary-equal stable
objects, not hash-agreement by luck. The required set re-derives independently at 12,117 with
the plan result digest the ceiling order cites. None of my findings gives a presenter who does
not own the machine a path to a false acceptance through the production path; all fail in the
safe direction or sit inside the conceded machine-ownership class. New this round: the change
record the brief names does not exist, the brief carries v7 hashes and cites a probe removed
in v7, and the F2 fix silently removed the receipt's only sys.path record while two written
claims still say it is there. Carried and re-verified rather than taken on trust: the six
`varies` strings, the vacuous B06 hook, F05's basis, the timeout/stdin/channel items, R06's
thin payload, the unused environment guard, the three fingerprint blind spots, and the
selection's missing producer receipt (CODEX-V5 F6, upstream of this mechanism).

## Scope and custody

I ruled only on the v8 closure mechanism and the artifacts the brief names. I did not read
`/Users/duhokim/NebulaMindData/`. I did not inspect or mutate any live downloader. Apart from
this report and `_tmp_KIMI_*` / `CLOSURE_PROBE_V8_*_KIMI*` artifacts in this gate directory I
wrote nothing; the pinned suite, subject, worker and fixtures were never modified (hashes
re-verified after all runs).

Independently computed SHA-256, each matching the receipt (per the brief's instruction, hashes
are taken from `CLOSURE_PROBE_V8_RECEIPT_20260826.json`, not from the brief text — see F2):

- `../ref/successor_ref_v8.py`: `1bec5c2831464e023f2fee472a30480761b9a9f40cc034ba092cbfc28ad7758a`
  == receipt `stable.subject.sha256`.
- `../ref/closure_worker_v8.py`: `245057259830c60e65b179bc01053d531964a7005b560e264bdefa0745c0092d`
  == the `worker_sha256` recorded through the boundary in G01's `self_check`.
- `../ref/FIXTURES_V8_20260826.out`: `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`
  == receipt.
- `closure_probe_suite_v8.py`: `382a078ff108cf0aea1f7c89f448dc650d8f86a0a7fdb6e988a711cf12309926`
  == receipt.
- Frozen planner files (byte-identical to my v6 record, which is what the planner digest binds):
  `../_objmanifest_20260820/build_object_manifest.py` `c63030e2…`, `../adapter/nm_brick_cutout_adapter.py`
  `267b2a93…` (== the objmanifest's own `PINNED_ADAPTER_SHA256`), `../_cutout_runner_20260820/cutout_runner.py`
  `ccb9b8fe…`.
- `../ref/successor_ref_v7.py`: `6be341bd…` and `../ref/closure_worker_v7.py`: `3468b90d…` —
  unchanged; the v7 report stays legible against its pins.

Interpreter: `/usr/bin/python3`, Python 3.9.6 (CLT), macOS arm64.

## Reproduction (question 1)

**Yes — exactly, for the same mode.**

- My full `production-uncached` run (`CLOSURE_PROBE_V8_RUN_KIMI.out`, receipt
  `CLOSURE_PROBE_V8_RECEIPT_KIMI.json`, 2,072.1 s): 33/33 conforming, no non-conforming probe,
  no error-typed probe, verdict SUITE-CONFORMING, hooks 12 declared / 12 ran / all_ran true.
- My `stable_sha256`: `509071e1138c867567e8059fccaa6abea82446fa7b09d699e044ecede4b94939` —
  **identical to the shipped receipt's**. The two `stable` objects are dictionary-equal
  (verified element-wise: 0 differences across all 33 probe rows, pins, digests and summaries),
  and each receipt self-hashes consistently (canonical rehash of each stable block == its
  stored hash, both ways).
- The v6 F2 mechanism specifically: the strings that broke v6 reproduction (F03/F04's
  run-dir-bearing refusal payloads) read `$RUN/counts_link.csv`, `$RUN/counts_fifo.csv`,
  `$RUN/counts_nofollow.csv` in my hashed structure — `normalise_deep()` rewrites the run dir
  out of `result`, `message` and `verify_note` (`closure_probe_suite_v8.py:759-773`, applied at
  `:861-863`). The v6 diagnosis stays confirmed: the cause is repaired, not out-voted.
- Scoping remark carried from v7, still true: the hash is a **per-installation** witness. G01's
  `self_check.worker` carries the worker's absolute path by design ("recorded, not
  summarised"), so a different home directory legitimately yields a different stable hash. On
  this machine, same mode, it reproduces exactly.

## Numbered findings

### F1 — MINOR (bookkeeping) — the change record the brief names does not exist

**Symbol/line.** Brief line 64: "`CLOSURE_REPAIR_V8_20260826.md` is the change record. Read it
as a claim to be checked." A `find` over the whole handoff tree returns no such file; the
`gates/` directory holds repair records for the base round, V6 and V7 only.

**Why it fails.** The brief points the referee at an artifact that was never written. The
brief's own "What changed, and what is claimed" section is the de facto record, and the v7→v8
diffs verify its two fixed claims exactly (subject: one line, the worker filename; worker: the
isolation-first move and the exec-verified-bytes change, matching the repairs my v7 report
specified). But a reader following the evidence list hits a dead pointer — and a round whose
own topic list includes "a finding going unlisted" (my v6 F7, twice named) should hold its own
record-keeping to the standard it cites.

**Smallest sufficient repair.** Write `CLOSURE_REPAIR_V8_20260826.md` (the brief's change
section plus the not-fixed list is already the content), or amend the brief to name the section
as the record.

### F2 — MINOR (stale brief content) — two Evidence hashes are the v7 files', and question 2 cites probe B03, removed in v7

**Symbol/line.** Brief line 68 pins the subject at `6be341bd443d…` — that is
`successor_ref_v7.py`'s digest (measured); the v8 subject is `1bec5c28…`. Brief line 69 pins
the worker at `3468b90d…` — `closure_worker_v7.py`'s digest; the v8 worker is `24505725…`.
The receipt carries the correct values and the brief says to take hashes from it, which
contains the error. Separately, brief question 2 (line 100) reasons from "B03 does the same
thing without the boundary and expects the opposite" — but B03 exists in neither the v7 nor
the v8 suite. It lived in v6 (`closure_probe_suite_v6.py:298`, the in-process control whose
verify hook asserted the core read the caller's table); the v7 suite dropped it (29 probes +3
new −1 = 31) without the v7 brief or the v7 repair record saying so, and the v7 brief already
cited it the same way. My own v7 report answered question 2 without noticing the removal — I
record that miss here rather than inherit it silently.

**Why it fails.** Stale pins in an evidence list are the exact shape a seat that skips the
receipt would gate against; the instruction to prefer the receipt is what saves this round.
B03's absence is smaller but real: it was the only dynamic evidence that the disclaimed
in-process core still reads caller-nominated pins — the control that shows the boundary, not
the core, does the custody work. B01/B02 evidence the boundary side; the core side now rests on
a docstring sentence alone.

**Smallest sufficient repair.** Update the two hashes. Either restore B03 (one probe, ~140 s)
or strike it from the brief and record the removal in the change record.

### F3 — MINOR (transparency regression introduced by the F2 fix) — no receipt records the worker's sys.path any more, while two written claims say it does

**Symbol/line.** Worker docstring (`closure_worker_v8.py:27-29`): "The full sys.path the worker
ran with is recorded in the receipt so the gate can see it rather than take my word for it."
Suite `not_covered` entry 1 (`closure_probe_suite_v8.py:62-66`): "Every receipt records the
full sys.path so this is visible." Measured: `sys_path` occurs **zero** times in the shipped
v8 receipt and in mine.

**Why it fails.** In v7 the claim was true exactly once: B04's refusal carried the full
provenance because the isolation check ran after provenance was built (v7 receipt's B04
payload has the 7-entry `sys_path`). The v8 fix — correctly — refuses before provenance exists
(`closure_worker_v8.py:79-82`), and `closure_receipt()` returns only `out["result"]`, dropping
provenance for PASS and REFUSE alike (`successor_ref_v8.py:825`). So the correct repair of my
v7 F2 silently deleted the only record the stated visibility rested on, and both claims stayed.
The direction is fail-safe (less information, never more trust), and the residual itself is
unchanged — but a repair round is where claims and mechanism drift apart, and question 6 asks
exactly that. I verified the underlying fact independently instead: under true `-I` plus the
one add-back, `sys.path` is the four standard CLT entries followed by the user site dir, and
numpy, astropy, erfa, astropy_iers_data, packaging, yaml, scipy and dateutil **all** resolve
from the unpinned user directory. (The `__editable__.astro_agent` finder in v7's B04 record was
an artifact of that probe's *non-isolated* interpreter; it does not appear under true `-I`.
The `.pth` channel in the CLT site-packages exists but currently injects nothing.)

**Smallest sufficient repair.** Include the interpreter-state provenance that needs no file
reads (python version, the three flags, `sys_path`, `pinned_site_dir`) in the early
isolation-refusal payload, and/or have `closure_receipt()` retain the worker's provenance in
the result it returns. Failing that, narrow the two claims to match the mechanism.

### F4 — MINOR (carried, restated precisely) — the frozen planner's files are verified and consumed by distinct reads on every use

**Symbol/line.** `_frozen_planner()` re-executes `build_object_manifest.py` from disk on every
call (`successor_ref_v8.py:266-277`); `frozen_planner_digest()` execs it (via `:384`) and then
reads the file bytes (`:387-389`); `close_manifest()` digests (`:652`), then execs a fresh
instance for the plan (`:655-656`), then re-digests after the plan (`:737`).

**Why it fails — precisely, and precisely why it does not block.** For the four pinned
artifacts and (now) the subject, verified bytes and consumed bytes are one read — closed by
construction. For the three planner files they are distinct reads by design: the digest's reads
and the execs that precede and follow them are separate opens of the same paths, so a
swap-and-revert between pre-plan digest and plan, or between plan and post-plan digest, moves
no number. That needs write access to the pinned lane tree — inside the conceded
machine-ownership class, and unreachable to a presenter who executes nothing in the worker —
but the `not_covered` race entry's "closed by construction" language covers only the
`verified_bytes` artifacts, and the retained-instance entry covers a different gap. Stating the
shape so the residual is not misread as covering it.

**Smallest sufficient repair.** Snapshot the three planner files into the worker's private work
dir at digest time and exec from there — the pattern `load_pinned_geometry()` already uses for
the sidecar — or name the re-execution windows in the `not_covered` race entry.

### F5 — MINOR (carried from v7, re-verified this round, all admitted) — the named-not-fixed list is accurate

Each re-verified rather than taken on trust:

- The six S01–S05/U01 `varies` strings (`closure_probe_suite_v8.py:624-689`) still omit the
  `PINNED_*_REL` reassignment `Ctx.redirect()` performs (`:159-163`). KIMI-V6 F7, twice named,
  twice unfixed, now in `not_covered` — the minimum I asked for.
- B06's verify hook is still `(True, "TypeError from the signature, not a forged receipt")`
  (`:322`); the probe body is the real assertion (acceptance → `AssertionError` → ERROR row →
  non-conforming), so conformance is sound and the hook asserts nothing.
- F05's basis still claims the no-window property; F05 is mechanically identical to F03 (both
  symlink the genuine table and require REFUSE + "symlink"), and the property's real evidence
  is the `CLOSURE-SINGLE-OPEN` fixture source assertion — re-executed by me this round,
  byte-identical output.
- No `timeout` on the worker subprocess (`successor_ref_v8.py:806`). Extra stdin keys ignored:
  tested this round — `{"manifest": [], "expected_outcome": "PASS", "comment": …}` still
  produced the computed REFUSE with all 12,117 missing names; the smuggled keys changed
  nothing, because the adjudication is computed, never caller-supplied.
- The dict-manifest refusal exits on the WORKER-ERROR channel (`closure_worker_v8.py:114`,
  code 1) rather than REFUSE (2); through `closure_receipt()` both become one
  `ManifestClosureError`, fail-closed.
- R06's structured result is still `{"error": "TypeError"}` (my run's row agrees) — one closure
  refusal, but thin against I4's "numbers a receipt needs": objects, selected bricks and every
  digest are known by the time the None manifest is iterated.
- `require_environment()` is referenced nowhere on the closure path.
- The three fingerprint blind spots stand — re-demonstrated live against v8: `math.radians`
  rebound to `lambda x: 0.0` and `adapter.tangent_plane_offsets` rebound to a stub each left
  `frozen_planner_digest()` at the pinned `1617af00…`; restore returns the same value.
- The selection's binding remains a code pin with no producer receipt (CODEX-V5 F6, upstream).

## Answers to the referee questions

1. **Reproduction.** Yes, exactly — see Reproduction above: identical `stable_sha256`,
   dictionary-equal stable objects, both receipts canonically self-consistent, and the v6 cause
   confirmed repaired (`normalise_deep`), with the per-installation scoping stated.
2. **Does the process boundary establish I1?** For the demonstrated attack class, yes: B01/B02
   poison every artifact pin in the presenter's own process and the worker's receipt still
   reports the true digests (`4e4ec45d…`, `425a42c3…`) and the true 12,117, with hooks
   asserting exactly those values. It is a real custody boundary, not a longer path to the same
   trust — with the terminal trust outside both processes: the receipt self-reports its
   digests, and the comparison "no code inside either process can perform for itself" (the
   worker's own words) is these referee rounds re-running the suite, which is the right shape.
   The stated site-packages residual is **not** the only residual: (a) measured this round —
   under true `-I` the CLT system site-packages precedes the one pinned add-back, and the whole
   scientific stack including the sidecar's parser (astropy) and the selection's parser
   (numpy) resolves from the unpinned user site dir; (b) the `.pth` injection channel in the
   CLT site-packages exists under `-I` (currently inert; unnamed in `not_covered`); (c) the
   planner's three files load from unpinned lane paths with re-execution windows (F4); (d) the
   worker's own code is loaded by the interpreter before it can hash itself — self-reported,
   externally witnessed only (my on-disk hash equals G01's record); (e) and since v8 the
   receipt no longer records the sys.path that (a)'s "so this is visible" rests on (F3).
3. **The reachable fingerprint (I2, I5).** It binds the three planner files' bytes, the adapter
   pin, the prefilter, both entry callables' bytecode/defaults/kwdefaults/closures and walkable
   pure-Python globals by value, and re-checks after the plan (my run reproduces N05's
   `1617af00… → 83f9abd7…` on the timed mid-plan mutation, and the probe proves the mutation
   fired). It still cannot see — each re-demonstrated live this round, not argued: module
   objects' contents (`math.radians` rebound: digest unmoved), helpers reachable only through
   class methods (`tangent_plane_offsets` rebound: unmoved), C callables (type name only),
   instance-attribute shadowing of class methods, the retained objmanifest instance
   (`not_covered`'s last entry), and anything reverted before the post-plan digest. Its
   cross-process stability **does** still come partly from ignoring these: `_stable_repr`
   reduces every non-primitive to its type name precisely so that no memory address enters the
   digest — stability and blindness share a root cause, as `not_covered` now states in my v6
   words. In the worker these blind spots bite only at import time, which is the stated
   site-packages residual.
4. **Verified-bytes custody (I5).** Real for the artifacts: one open
   (`O_RDONLY|O_NOFOLLOW|O_NONBLOCK`), `fstat` regular, hashed as read, parsed from that
   snapshot; the FITS sidecar re-parsed from a private byte-identical copy; F03/F04/F05 refuse
   the symlink and the FIFO. And now real for the subject: one `read_bytes`, hash, pin-compare,
   then `exec(compile(subject_bytes, …))` (`closure_worker_v8.py:84-99, 130-134`) — W02's
   equality holds in both receipts (2 events hashing, 2 through a whole closure). Anatomy,
   established independently this round: both events come from the single `read_bytes` (the
   audit pipeline counts it twice; `is_file`/`stat` add none) and the exec adds none — so the
   "2" is not magic and the equality is the assertion, as the brief says. Remaining paths by
   which consumed bytes could differ from verified bytes: the planner files (F4), the worker's
   own code (terminal trust, external comparison only), and the unpinned import-time parser
   stack (the stated residual). None is reachable to a presenter without write access to the
   pinned tree or the import-path directories.
5. **The single adjudication (I3, I4).** Correct on every shape exercised: R08 names both the
   duplicate (`0001m252`) and the omission (`0001m250`) with the hook asserting both counts and
   names; R01/R02/R05/R07 omissions with full counts (R02's hook asserts 100 names on the live,
   untruncated result); R03 extra-only; R04 duplicate-only with missing 0; B07 one refusal at
   the boundary with `manifest_type` recorded (WORKER-ERROR channel — F5). The adjudication
   computes duplicates, missing and extra independently from the finished required set and
   reports them in one result (`successor_ref_v8.py:746-773`); my v7 duplicated-extra shape
   (required set plus `0001p000` twice: one refusal naming duplicate 1 AND extra 1) still holds
   against v8's identical code. I found no candidate shape where one condition masks another.
   The residual is R06's thin error-typed payload (F5) — one refusal, but not the numbers.
6. **Do the fixes hold, and did any break something?** Both hold; one side effect found (F3),
   no mechanism regression. F1: the exec-verified-bytes change is exactly my v7 repair; the
   subject's only `__name__` use is the `__main__` guard (`successor_ref_v8.py:2112`) and it
   touches no `__spec__`/`__loader__`, so the exec context is behavior-neutral; W02's equality
   is in both receipts. F2: my independent poison reproduction (fake numpy on PYTHONPATH,
   worker started without `-I`) produced a structured WORKER-ERROR, exit 1, sentinel never
   written; W01 conforms with its hook asserting `sentinel_written is False`. Treating v8 as a
   fresh subject: the fixture battery re-executed by me produces byte-identical output to the
   shipped `FIXTURES_V8_20260826.out` (`fab32ba2…` both ways; all fixtures pass); the subject
   v7→v8 diff is one line; the worker diff is the two fixes and nothing else; my full 33-probe
   run conforms; the shipped receipt self-hashes consistently. The B04 mentions-guard repair
   (asserting the payload key instead of wording) is the right kind of probe maintenance,
   recorded in the suite's own comment.
7. **Probe fidelity.** 12 hooks declared, 12 ran, `verify_hooks_all_ran` true — the meta-check
   I asked for is computed, not asserted. The hooks assert what their `basis` claims on the
   receipt's own rows: P01 (planner digest identical before/after), R02 (100 names on the live
   result), R04, R08 (both conditions named), B01/B02 (the true digests), B04 (`isolated is
   False` as a payload key, wording-proof), W01 (sentinel never written), W02 (equality), N05
   (both digests, differing), U02 (`incoherent_rows` == 5, the true total, not a cap). B06's
   hook is vacuous (F5); S01–S05/U01 under-declare the path reassignment (F5); F05's basis
   overclaims what a static symlink evidences (F5). Everything else is faithful; B04/B05's
   comments recording the wording-change and wrong-reason episodes are the right kind of
   honesty.
8. **Coverage.** Conditions bearing on I1–I5 that neither the 33 probes nor `not_covered`
   reach: (i) swap-and-revert of the planner files between digest and exec (F4); (ii) a
   mutation reverted before the post-plan digest (in-process only, carried from v6); (iii) the
   in-process core's non-custody has no dynamic evidence anywhere — B03 removed in v7 and still
   cited by the brief (F2); (iv) the worker's self-hash terminal trust (stated in its own
   docstring; no probe can close it); (v) `.pth` injection in the CLT system site-packages
   under `-I` (channel open, currently inert, unnamed); (vi) the sys.path-recording gap itself
   (F3) — `not_covered` entry 1 currently claims the opposite of the fact. Stated and confirmed
   open rather than missed: the three blind spots, the retained-instance gap, in-place artifact
   modification, the genuine race (structural evidence only), the selection's producer receipt,
   concurrency, the download itself, the timeout/stdin/channel items, R06's thin payload,
   `require_environment()`.
8. **The 12,117 figure.** Confirmed independently against v8. I imported the frozen planner and
   parsed the pinned parent directly — never calling `close_manifest`
   (`_tmp_KIMI_enumerate_v8.py`, `_tmp_KIMI_enumeration_v8.json`, 145.6 s): **12,117 distinct
   required bricks** from 65,060 objects; plan result digest
   `aaeaa9f37aabf1da6000a6ad07890cfe010677e301583530ba1a108833e3b3f1`; histogram
   `{1: 55566, 2: 8801, 3: 591, 4: 102}` — digest and histogram identical to the v5 measurement
   the ceiling order cites, to v6, and to v7; parent and sidecar hashes match their pins; the
   two historical probe objects are not rows of the pinned parent, as before. On the brief's
   "since the planner digest changed": the planner **pin** is `1617af00…` in v6, v7 and v8
   alike — it last changed at v5→v6 (`10cea7a6…` → `1617af00…`, because the digest binds more,
   per the subject's own comment at `successor_ref_v8.py:150-153`), and the plan **result**
   digest the ceiling cites (`aaeaa9f3…`) has been unchanged since v5. So the plan the ceiling
   pays for is unchanged. Ceiling arithmetic: 12,117 × 12.2 MB = 147,827.4 MB = 147.83 decimal
   GB ≈ the approved ≈148 GB; 12,117 / 6,445 = 1.880062.

## Failed attacks / positive evidence

- All pinned subject/worker/suite/fixture hashes reproduce against the receipt; the shipped
  receipt self-hashes consistently; my full run is dictionary-equal to it.
- B01/B02: presenter-process poisoning of every artifact pin changes nothing in the worker's
  receipt. B04: un-isolated worker refuses with the flag-named payload. B05: subject/pin
  mismatch refuses with both digests. B06: the v6 forge channel dies at the signature. B07:
  dict manifest refused with its type recorded.
- W01: poisoned environment + no `-I` → refusal and no sentinel, in-suite and in my own
  reproduction. W02: hash-only and full-closure event counts equal, in both receipts.
- N01–N04: pre-verification live mutations all move the digest and refuse; N05's timed
  mid-plan mutation is caught by the post-plan re-check with both digests reported, and the
  probe proves the mutation fired.
- F03/F04/F05: symlink and FIFO refused on the open itself.
- S01–S05, U01, U02: schema, sum, field, universe and coherence faults all refused, U02 with
  the true total (5).
- Extra stdin keys smuggled alongside the manifest change nothing; the adjudication is computed.
- The v6 blind-spot demonstrations still move nothing (F5) — confirming the stated open items.
- Fixture battery re-executed byte-identical; 12,117 and the plan digest re-derived without the
  closure code path; frozen planner files byte-identical to my v6 record.

## Evidence ledger

Content-read: the v8 brief; the required prior rounds (`CLOSURE_RECEIPT_GPT56.md`,
`CLOSURE_RECEIPT_CODEX.md`, `CLOSURE_V5_CODEX.md`, `CLOSURE_V6_KIMI.md`, `CLOSURE_V7_KIMI.md`);
`CLOSURE_REPAIR_V7_20260826.md` (the v8 record named by the brief does not exist — F1);
`closure_probe_suite_v8.py` (whole); `../ref/successor_ref_v8.py` (closure region 53-825 and
fixture region references); `../ref/closure_worker_v8.py` (whole);
`../ref/FIXTURES_V8_20260826.out`; `CLOSURE_PROBE_V8_RECEIPT_20260826.json` (whole);
`CLOSURE_PROBE_V8_RUN_20260826.out`; `../acquire/DOWNLOAD_QUEUE_PLAN_20260825.md`; v7→v8 diffs
of subject (1 diff line) and worker (the two repairs).

Commands/probes (artifacts as `_tmp_KIMI_*` or named receipts in this directory):

- `shasum -a 256` over every artifact listed in Scope and custody, before and after all runs.
- Full production-uncached suite run → `CLOSURE_PROBE_V8_RECEIPT_KIMI.json`,
  `CLOSURE_PROBE_V8_RUN_KIMI.out`; recursive stable-object comparison against the shipped
  receipt (0 diffs); canonical rehash of both stable blocks.
- Independent 65,060-object enumeration without `close_manifest` (question 8b):
  `_tmp_KIMI_enumerate_v8.py`, `_tmp_KIMI_enumeration_v8.json`, `_tmp_KIMI_enumerate_v8.out`.
- Fixture battery re-execution: `_tmp_KIMI_v8_fixtures.out` (byte-identical, hash equality).
- PYTHONPATH-poisoned non-isolated worker run against v8 (F2-fix proof): `_tmp_KIMI_v8_poison/`;
  no sentinel file exists after the run.
- Audit-hook anatomy of the W02 counts (self-check side; `is_file`/`stat`/`read_bytes`
  attribution): both events from the single `read_bytes`.
- Blind-spot re-demonstrations against v8: `math.radians`, `tangent_plane_offsets` (output in
  this report's F5).
- Extra-stdin-keys worker test (dict with smuggled outcome keys → computed REFUSE).
- `python3 -I` sys.path inspection and dependency resolution for numpy/astropy/erfa/
  astropy_iers_data/packaging/yaml/scipy/dateutil.
- Receipt text searches: `sys_path` occurrences in the v8 and v7 receipts (0 vs 1 — F3);
  probe-id inventories of the v6/v7/v8 suites (B03 timeline — F2).

## Constraints and uncertainties

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not launch, authorize, inspect or mutate any downloader or transfer process; no image
  bytes were read. This report clears the closure mechanism; it does not itself fire anything,
  and the 148 GB ceiling stays tied to the confirmed 12,117.
- The harness reported my full-suite process "exited" at ~516 s; the process kept running and
  completed normally (receipt and run log are the evidence) — the same behavior as my v6 and
  v7 runs; no result above depends on the executor's process accounting.
- My suite run overlapped with my own enumeration and inspection commands; per-probe timings
  match the shipped receipt's (N05 138.2 s shipped; my run's rows agree in outcome everywhere),
  so no timing-sensitive probe was affected.
- The stable hash is a per-installation witness (absolute worker path in G01's payload);
  cross-machine equality is neither expected nor claimed.

## Testimony

- `DOWNLOAD_QUEUE_PLAN_20260825.md` records the ≈148 GB ceiling tied to the 12,117 measurement,
  states the ceiling raise is not authorization to fetch, and states no image byte has been
  fetched. I read that record; I did not inspect live transfer state.
- The parent receipts' 13 chunk records carry TAP job URLs and per-chunk digests. I verified
  the envelope's pin, schema fields, chunk sequence and sums against the loader's checks (13
  chunks, rows sum 65,060, bricks sum 6,445, `output_sha256` == the parent pin); I did not
  re-query the remote jobs or reconstruct the parent from archived payloads.
- The brief's "~200 s per closure / ~45 min" estimate held (2,072.1 s full run; 145.6 s direct
  enumeration).
- Lane remnants: `runner_v8_kimi.log` was created empty by the dispatch script; this report is
  the seat's product. No other seat's v8 report is present in this directory as of writing.

**CLEAR**
