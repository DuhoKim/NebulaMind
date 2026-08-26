# CLOSURE V7 REFEREE — KIMI

## Verdict

**CLEAR** — with conditions named below. All five claimed repairs hold under dynamic test, my
full production-uncached suite run reproduces the shipped receipt's `stable_sha256` exactly
(v6's F2 is dead, not lucky), the required set re-derives independently at 12,117 with the
pinned plan digest, and none of my findings gives a presenter who does not own the machine a
path to a false acceptance through the production path. Two findings are new this round (the
worker's verify-then-import double read of its own subject, and the isolated-check running
after the subject import); one is a bookkeeping failure the brief explicitly warns about (my
v6 F7 vanished from the repair record's accounting while persisting in the suite). All fail
in the safe direction or sit inside the conceded machine-ownership class. Open by the
authors' own statement and outside this mechanism's scope: the fingerprint blind spots
(KIMI-V6 F4), the unfrozen refusal schema and unused `require_environment()` (KIMI-V6 F8),
and the selection's missing producer receipt (CODEX-V5 F6).

## Scope and custody

I ruled only on the v7 closure mechanism and the artifacts the brief names. I did not read
`/Users/duhokim/NebulaMindData/`. I did not inspect or mutate any live downloader. Apart from
this report and `_tmp_KIMI_*` / `CLOSURE_PROBE_V7_*_KIMI*` artifacts in this gate directory I
wrote nothing; the pinned suite, subject, worker and fixtures were never modified (hashes
below re-verified after all runs).

Independently computed SHA-256 (all matching the brief's pins):

- `../ref/successor_ref_v7.py`: `6be341bd443d45c42eecd6b47e806f652882c971827300d51ff6fcb568069f33`
- `../ref/closure_worker_v7.py`: `3468b90d981c07459cc1fc040b2a9e2828d76d1d1c128bea70cdf963cd4255b5`
- `../ref/FIXTURES_V7_20260826.out`: `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`
- `closure_probe_suite_v7.py`: `a0e8fcf5c167bfa490cf1f5e42e91b9c2b3f144d76ef9b839eca0f377cbdb718`
- `CLOSURE_PROBE_V7_RECEIPT_20260826.json`: `258307e2c7e671551e793e267a245ee9db78eeed49486a9ee075b24fa28aa2f3`
- `CLOSURE_REPAIR_V7_20260826.md`: `8a97d1a0964c6bdc045218e4c8eb7cacf416447712f79990313af74204d0d489`
- `../ref/successor_ref_v6.py`: `d921d7445ddfee37eb3f91340730bd53989d53ad480287e3e1f987dff0784805`
  (unchanged since my v6 report; that report stays legible against its pins)
- `../ref/successor_ref_v4.py` / `../ref/successor_ref_v5.py` present and unread this round
  beyond digest spot-checks against the v4/v5 reports.

Interpreter: `/usr/bin/python3`, Python 3.9.6 (CLT), macOS arm64.

## Reproduction (question 1)

**Yes — exactly, for the same mode, and the v6 diagnosis is confirmed rather than merely
out-voted.**

- My full `production-uncached` run (`CLOSURE_PROBE_V7_RUN_KIMI.out`, receipt
  `CLOSURE_PROBE_V7_RECEIPT_KIMI.json`, 1,963.7 s): 31/31 conforming, no non-conforming
  probe, no error-typed probe, verdict SUITE-CONFORMING, hooks 9 declared / 9 ran / all_ran.
- My `stable_sha256`: `009e5bce1ac5b52487e474b7ceb3196f442d5ae3fff9ff10ff760d9b9b3b74a9` —
  **identical to the shipped receipt's**. The two `stable` objects are dictionary-equal
  (verified element-wise, not hash-only), every probe row identical, and my canonical rehash
  of my own stable block matches my stored hash, as does the shipped receipt's
  (recomputed == stored for both).
- The F2 mechanism specifically: two separate processes ran
  `--only B04,B05,B06,B07,F03,F04,F05` with different per-process run dirs
  (`_tmp_KIMI_v7_sub1`, `_tmp_KIMI_v7_sub2`). Both printed
  `b0b7eb8f210ac4fca0c1e5a31ec625a0f44fa8b5b7adbdae5b2d4181ca4b1103` and their stable objects
  are dictionary-equal. The exact strings that broke v6 — F03/F04's refusal payloads carrying
  the per-process run dir — now read `$RUN/counts_link.csv`, `$RUN/counts_fifo.csv`,
  `$RUN/counts_nofollow.csv` in the hashed structure: `normalise_deep()` rewrites the run dir
  out of every string in the hashed rows (`closure_probe_suite_v7.py:672-686`, applied to
  `result` at `:776`, `message` at `:775`, `verify_note` at `:774`). The v6 diagnosis was two
  payload strings; those strings are now normalised, and the hash reproduces. That is the
  confirmation the brief asked for rather than agreement by luck.
- One scoping remark for the next seat: the hash is a **per-installation** witness, not a
  cross-machine constant. B04's payload records the worker's real `sys.path` and G01 the
  worker's absolute path by design ("recorded, not summarised"), so a different home
  directory legitimately yields a different stable hash. On this machine, same mode, it
  reproduces exactly.

## Numbered findings

### F1 — MINOR (I5, demonstrated dynamically) — the worker verifies the subject's bytes and then imports the path: two reads, so verified code ≠ consumed code under a swap

**Symbol/line.** `subject_bytes = SUBJECT.read_bytes()` (`closure_worker_v7.py:77`, hashed at
`:78`, compared to the pin at `:89-91`) versus
`spec = importlib.util.spec_from_file_location("closure_subject", SUBJECT)` +
`spec.loader.exec_module(mod)` (`:110-113`), which opens and reads `SUBJECT` again from the
filesystem at execution time.

**Why it fails.** I5: "the verified bytes and code must be the bytes and code actually
consumed." For the artifacts the mechanism holds this by construction (one open, hash as
read, parse the snapshot — `verified_bytes()`); for the subject — the code that does all the
judging — verification and consumption are two separate opens of the same path with a window
between. Demonstrated, not argued: a Python audit hook around the worker's exact sequence
captured two distinct `open` events naming `successor_ref_v7.py` (one from `read_bytes`, one
from the import machinery, plus a `.pyc` cache probe). A caller who can write to `../ref/`
between the two reads passes the pin check with the pinned bytes and then has different code
executed. The window is small and the write access it needs is inside the conceded
"modification of a pinned artifact in place" class — but the suite's `not_covered` names that
class for *artifacts probed by redirection* and the race entry speaks of "replacing a file
between the worker's verified read and its parse … closed by construction" for artifacts;
neither entry names the subject import, which is not closed by construction. B05 covers a
mismatch present at verification time, not a swap between verification and import.

**Smallest sufficient repair.** Execute the verified bytes instead of the path: build the
module by hand, set `mod.__file__ = str(SUBJECT)` (the subject resolves its pinned artifacts
via `Path(__file__).resolve().parents[2]`, so `__file__` must stay the real subject path),
then `exec(compile(subject_bytes, str(SUBJECT), "exec"), mod.__dict__)`. Alternatively write
`subject_bytes` to the worker's private work dir and import that — the same pattern
`load_pinned_geometry()` already uses for the sidecar.

### F2 — MINOR (boundary hygiene, demonstrated dynamically) — the worker checks `-I` after importing the subject, so a non-isolated environment executes code before the refusal

**Symbol/line.** The subject import at `closure_worker_v7.py:110-113` precedes the isolation
refusal at `:124-128` (`if not provenance["isolated"]: fail(...)`).

**Why it fails.** The refusal's premise is that an un-isolated interpreter is untrustworthy;
as ordered, that untrustworthy environment runs first. Demonstrated: a fake `numpy/` on
`PYTHONPATH` whose module-level code writes a sentinel; the worker started **without** `-I`
imported the subject, the sentinel appeared, and the worker then died with an *uncaught*
`AttributeError` traceback (no structured `WORKER-ERROR` JSON), because the fake numpy lacks
`array` (`_tmp_KIMI_poison/`, `_tmp_KIMI_poison_FIRED.txt`). B04 passes only because a clean
non-isolated environment imports the subject successfully and reaches the guard. Through
`closure_receipt()` this stays fail-closed — `-I` is hard-coded in the call
(`successor_ref_v7.py:806`), `PYTHONPATH` is ignored under `-I`, and an empty stdout becomes
"closure worker produced no receipt," never an acceptance — so no false acceptance is
reachable. But the guard as placed protects nothing it claims to protect, and the crash
shape means the boundary's own error contract (one JSON receipt) depends on the environment
being benign enough to survive the import.

**Smallest sufficient repair.** Move the `sys.flags.isolated` check to the top of `main()`,
before the subject is read or imported (the flag is fixed at interpreter startup, before any
import). Related nit, same file: the F6 manifest-type refusal exits as `WORKER-ERROR` (code
1) rather than the REFUSE channel (code 2); through `closure_receipt()` both become one
`ManifestClosureError` carrying the payload, so this is cosmetic — but the boundary's exit
taxonomy would be cleaner if a malformed candidate were "refused" (2) rather than "could not
run" (1).

### F3 — MINOR (repair-record bookkeeping) — my v6 F7 persists in the suite and appears in neither the repair record's "fixed" list nor its "not fixed" list

**Symbol/line.** S01–S05 and U01's `varies` strings (`closure_probe_suite_v7.py:537, 549,
561, 574, 588, 601`) each declare "a copy …, AND the pinned digest set to the copy's", while
`Ctx.redirect()` (`:151-155`) reassigns the `PINNED_*_REL` path constant *and* the digest
together. The path reassignment is still not named in any of the six. `CLOSURE_REPAIR_V7_
20260826.md` lists fixed findings F3/F1/F2/F5/F6 and not-fixed F4/F8/CODEX-V5-F6; KIMI-V6 F7
is in neither list, and the v7 brief repeats those two lists.

**Why it fails.** Not the mechanism — the accounting. The brief's own words: "a repair round
that quietly drops a finding is worse than one that leaves it open." F7 was a numbered
finding in the round being repaired; it is still true of the suite text; and the record of
this round neither claims it fixed nor states it open. The redirect is uniform and the digest
override is the declared part, so no hidden change decides any outcome — the severity stays
minor — but a reader of the repair record cannot tell the finding was seen.

**Smallest sufficient repair.** Add "and `PINNED_*_REL` points at that copy" to the six
`varies` strings (one line each), and add F7 to the repair record's not-fixed list — or fix
the strings and list it as fixed.

### F4 — MINOR (probe fidelity) — B06's verify hook is vacuous, and F05's basis claims a property the probe cannot evidence

**Symbol/line.** B06: `verify=lambda o, r: (True, "TypeError from the signature, not a forged
receipt")` (`closure_probe_suite_v7.py:314`). F05: basis "the refusal is now O_NOFOLLOW on
the open itself rather than an lstat before it, so there is no window between the check and
the read" (`:349-351`).

**Why it fails.** B06's hook returns `True` unconditionally; it asserts nothing. The probe
body is the real assertion (acceptance of the kwarg raises `AssertionError` → ERROR row →
non-conforming; a silently ignored kwarg yields PASS → non-conforming), so conformance is
sound — but the hook's note ("TypeError from the signature") is asserted by nothing in the
hook; the row already carries `{"typeerror": ...}` and the hook could check it. F05 is now
mechanically identical to F03 (both point a symlink at the genuine table and require REFUSE +
"symlink"), and no static-symlink probe can distinguish O_NOFOLLOW-on-open from
lstat-then-open — both refuse identically. The "no window" property is actually evidenced by
the fixture's source assertion (`CLOSURE-SINGLE-OPEN`: `"O_NOFOLLOW" in _vb and "is_symlink"
not in _vb`, re-executed by me, byte-identical output), not by the probe. The basis
overclaims what the probe establishes.

**Smallest sufficient repair.** B06 hook: `(isinstance(r, dict) and "typeerror" in r, ...)`.
F05 basis: narrow to "a symlink to the genuine table is refused" and cite the fixture's
source assertion as the evidence for O_NOFOLLOW — or drop F05 as a duplicate of F03.

### F5 — MINOR (carried from v6, still not in `not_covered`) — no timeout on the worker subprocess; extra keys in the worker's stdin JSON ignored

**Symbol/line.** `_sp.run([sys.executable, "-I", str(worker), "--work-dir", td], input=...,
capture_output=True, text=True)` (`successor_ref_v7.py:806`) — no `timeout`. Worker:
`request = json.loads(...)`; `if not isinstance(request, dict) or "manifest" not in request`
(`closure_worker_v7.py:97-98`) — additional keys are accepted silently.

**Why it fails.** Availability only: a hung worker (a FIFO standing where an artifact should
be is refused, but a genuinely stuck planner call is not) hangs `closure_receipt` forever —
fail-safe direction, never a false acceptance. Extra stdin keys (e.g. a future
`"expected_result"` field smuggled alongside the manifest) are ignored today; naming the
accepted schema closed is cheaper than reasoning about it later.

**Smallest sufficient repair.** Add `timeout=` to the subprocess call and map expiry to a
closure refusal; reject any stdin key other than `manifest`.

### F6 — MINOR (stated open, re-verified this round) — fingerprint blind spots, unused environment guard, thin R06 payload, no selection producer receipt

All four are declared open by the brief/repair record; I re-verified each rather than taking
the statement:

- `math.radians` rebound to `lambda x: 0.0` in my process: `frozen_planner_digest()` unmoved,
  still `1617af00eb7398abd93cc2726dbfb1ecfb24d07bede4b84c128ef2442bf40cb4` == pin.
- `adapter.tangent_plane_offsets` rebound to `lambda *a, **k: (0.0, 0.0)`: digest unmoved,
  still pinned.
- `require_environment()` is referenced nowhere on the closure path (`close_manifest`,
  `closure_receipt`, the worker); the worker records the python version in provenance but
  enforces nothing.
- R06's structured result is still `{"error": "TypeError"}` (my run's receipt row agrees),
  after objects, selected-brick count and every digest are known.
- The selection binding remains a code pin (`PINNED_SELECTION_SHA256`) with no producer
  receipt — CODEX-V5 F6, upstream of this mechanism.

## Answers to the referee questions

1. **Reproduction.** Yes, exactly: my full-run stable object is dictionary-equal to the
   shipped receipt's and `stable_sha256` `009e5bce…` matches; two-process subset runs
   reproduce at `b0b7eb8f…`; both receipts self-hash consistently. The v6 cause (run-dir
   strings in F03/F04 payloads) is confirmed repaired by `normalise_deep()`; see
   Reproduction above for the per-installation scoping of the hash.
2. **Does the process boundary establish I1?** For the demonstrated attack class, yes: B01
   and B02 poison every count/parent/receipt pin in the presenter's own process and the
   worker's receipt still reports the true digests (`4e4ec45d…`, `425a42c3…`) and the true
   12,117. It is a real custody boundary, with the terminal trust still outside both
   processes: the receipt self-reports its digests, and the worker's own docstring concedes
   the external comparison "is the part no code inside either process can perform for
   itself" — here that comparison is these referee rounds re-running the suite, which is the
   right shape. The stated site-packages residual is **not** the only residual: it is real
   and measured as stated (under `-I` + the one add-back, the CLT system site-packages
   precedes the add-back and numpy **and astropy** resolve from the unpinned user site — the
   sidecar's bytes are pinned, its parser is not; re-verified live this round), and F1, F2
   and F5 above are residuals of the same machine-ownership family that the round does not
   name.
3. **The reachable fingerprint (I2, I5).** It binds the three planner files' bytes, the
   adapter pin, the prefilter, both entry callables' bytecode/defaults/kwdefaults/closures
   and walkable pure-Python globals by value, and re-checks after the plan (N05: my run
   reproduces `1617af00… → 83f9abd7…` on a timed mid-plan mutation). It still cannot see:
   module objects' contents (`math.radians` — re-demonstrated), helpers reachable only
   through class methods (`tangent_plane_offsets` — re-demonstrated), C callables (type name
   only), the retained objmanifest instance the plan actually runs on (stated in
   `not_covered`), and a mutation reverted before the post-plan digest (uncovered;
   in-process only). Its cross-process stability still comes partly from `_stable_repr`
   reducing all of these to type-name strings — stability and blindness share a root cause,
   now stated in the suite's own `not_covered` in my v6 words. In the worker these blind
   spots bite only at import time, which is the stated site-packages residual.
4. **Verified-bytes custody (I5).** Real for the artifacts: one open
   (`O_RDONLY|O_NOFOLLOW|O_NONBLOCK`), `fstat` regular, hashed as read, parsed from that
   snapshot; the FITS sidecar is re-parsed from a private byte-identical snapshot in the
   worker's own temp dir; F03/F04/F05 refuse the symlink and the FIFO (tested directly as
   well as through the suite). One remaining path, demonstrated: the worker's subject import
   verifies one read and consumes another (F1). No path reachable to a presenter without
   write access to the pinned tree (conceded class) — but the subject import is not inside
   the "closed by construction" argument the `not_covered` race entry makes for artifacts.
5. **The single adjudication (I3, I4).** Correct on every shape exercised: R08 names both
   the duplicate (`0001m252`) and the omission (`0001m250`); R01/R02/R05/R07 omissions named
   with full counts; R03 extra-only; R04 duplicate-only; R06 one refusal (thin payload —
   F6/F8); B07 one refusal at the boundary with `manifest_type` recorded. Beyond the shipped
   shapes I ran one more at the production boundary: the required set plus a *duplicated
   extra* brick (`0001p000` twice) — one refusal naming duplicate 1 AND extra 1 with missing
   0 (`_tmp_KIMI_v7_dupextra.out`). Duplicates, omissions and extras are computed from the
   finished required set and reported together; I found no shape where one condition masks
   another.
6. **Do the five fixes hold, and did any break something?** All five hold; no regression
   found, treating v7 as a fresh subject:
   - **F3 (interpreter nomination).** Signature is exactly `['manifest_bricknames']`;
     calling with `python_executable=` raises `TypeError` before anything runs (tested); the
     call is hard-coded `[sys.executable, "-I", worker]`; the new fixture asserts the live
     signature and the call text. The old forge shape dies at the signature.
   - **F1 (verify hooks).** Shipped receipt: 9 declared / 9 ran / all_ran true; my full run
     agrees. Dynamically proven, mirroring my v6 sentinel test: a copied suite with a
     sentinel-writing hook on R05 produced the sentinel file and the row records
     `verify_ran: true` with its note (`_tmp_KIMI_v7_hookcheck_suite.py`,
     `_tmp_KIMI_v7_hook_sentinel.txt`). The pinned suite was never modified.
   - **F2 (`stable_sha256`).** Exact reproduction, full and subset scale (above).
   - **F5 (symlink on the open).** `O_NOFOLLOW` on the open, lstat and the false docstring
     claim gone; my direct symlink test refused with the `{"symlink": ...}` payload; the
     fixture asserts `O_NOFOLLOW` present and `is_symlink` absent.
   - **F6 (manifest type).** The worker refuses a JSON object with
     `'manifest' must be a JSON array or null, got dict` and records `manifest_type`
     (tested directly: exit 1, WORKER-ERROR; B07 conforms through the suite).
   Regression check: the fixture battery **re-executed by me** this round —
   `python3 ../ref/successor_ref_v7.py --fixtures` — produces byte-identical output to the
   shipped `FIXTURES_V7_20260826.out` (`fab32ba2…` both ways; `ALL FIXTURES PASS`), and my
   full 31-probe run conforms. The only new defects I found are pre-existing structural
   items this round names (F1, F2), not regressions.
7. **Probe fidelity.** The nine hooks assert what their `basis` claims, and each claim is
   true on the receipt's own rows: P01 (planner digest identical before/after), R02 (100
   missing names carried in the structured result — the hook runs on the live, untruncated
   result; the receipt's `jsonable()` still truncates lists at 8 with counts preserved),
   R04, R08, B01, B02, U02 (`incoherent_rows` == 5), N05 (both digests, differing), and B06
   (vacuous hook, sound body — F4). Metadata: S01–S05/U01 still under-declare the
   `PINNED_*_REL` reassignment (F3 — and it fell out of the repair record's accounting).
   F05's basis overclaims what a static symlink can show (F4). Everything else is faithful;
   B05's comment recording the v6→v7 wrong-reason episode is the right kind of honesty.
8. **Coverage.** Conditions bearing on I1–I5 that neither the 31 probes nor `not_covered`
   reach: the worker's subject verify-then-import double read (F1); the isolated-check
   ordered after the subject import, including the unstructured-crash shape (F2); no
   subprocess timeout and ignored extra stdin keys (F5); mutation-then-revert during the
   plan defeating the post-plan re-check (in-process only, carried from v6); the vacuous B06
   hook and F05's basis (F4). Stated and confirmed open rather than missed: the three
   fingerprint blind spots, the retained-instance gap, `require_environment()` unused, R06's
   thin payload, the selection's producer receipt, concurrency, in-place artifact
   modification, the download itself.
8. **The 12,117 figure (against v6).** Confirmed independently. I imported the frozen
   planner and parsed the pinned parent directly — never calling `close_manifest` —
   planning all 65,060 rows (`_tmp_KIMI_enumerate_v7.py`, `_tmp_KIMI_enumeration_v7.json`,
   156.9 s): **12,117 distinct required bricks**, plan digest
   `aaeaa9f37aabf1da6000a6ad07890cfe010677e301583530ba1a108833e3b3f1`, histogram
   `{1: 55566, 2: 8801, 3: 591, 4: 102}` — digest and histogram identical to the shipped v7
   receipt, to my v6 measurement, and to the v5 measurement the ceiling order cites. The
   planner pin is unchanged v6→v7 (`1617af00…`), so the plan the ceiling pays for is
   unchanged; parent and sidecar hashes match their pins. Ceiling arithmetic:
   12,117 × 12.2 MB = 147,827.4 MB ≈ the approved ≈148 GB; 12,117 / 6,445 = 1.88006. The
   two historical probe objects are not rows of the pinned parent, as before.

## Failed attacks / positive evidence

- All pinned subject/worker/suite/fixture hashes reproduce; the shipped receipt self-hashes
  consistently; my full run is dictionary-equal to it.
- B01/B02: presenter-process poisoning of every artifact pin changes nothing in the worker's
  receipt. B04: un-isolated worker refuses. B05: subject/pin mismatch refuses with both
  digests. B06: the v6 forge channel is closed at the signature. B07: dict manifest refused
  with its type recorded.
- N01–N04: pre-verification live mutations all move the digest and refuse; N05's timed
  mid-plan mutation is caught by the post-plan re-check with both digests reported.
- F03/F04/F05: symlink and FIFO refused; the refusal is on the open itself.
- S01–S05, U01, U02: schema, sum, field, universe and coherence faults all refused, U02 with
  the true total (5), not a cap.
- Duplicated-extra manifest: one refusal naming duplicate and extra together.
- The v6 blind-spot demonstrations still move nothing (F6) — confirming the stated open
  items rather than discovering divergence.
- Fixture battery re-executed byte-identical; 12,117 and the plan digest re-derived without
  the closure code path.

## Evidence ledger

Content-read: the v7 brief; `CLOSURE_REPAIR_V7_20260826.md`; the required prior rounds
(`CLOSURE_RECEIPT_GPT56.md`, `CLOSURE_RECEIPT_CODEX.md`, `CLOSURE_V5_CODEX.md`,
`CLOSURE_V6_KIMI.md`); `closure_probe_suite_v7.py` (whole); `../ref/successor_ref_v7.py`
(closure region 1-825 and fixture region in full); `../ref/closure_worker_v7.py` (whole);
`../ref/FIXTURES_V7_20260826.out`; `CLOSURE_PROBE_V7_RECEIPT_20260826.json` (whole);
`../acquire/DOWNLOAD_QUEUE_PLAN_20260825.md`; v6→v7 diffs of subject and worker (62 and 13
diff lines — surgical).

Commands/probes (artifacts as `_tmp_KIMI_*` or named receipts in this directory):

- `shasum -a 256` over every artifact listed in Scope and custody.
- `python3 closure_probe_suite_v7.py --list`.
- Full production-uncached suite run → `CLOSURE_PROBE_V7_RECEIPT_KIMI.json`,
  `CLOSURE_PROBE_V7_RUN_KIMI.out` (sha256 `0341e681…`, `ad6675ad…`); recursive stable-object
  comparison against the shipped receipt; canonical rehash of both.
- Two-process subset reproduction (`_tmp_KIMI_v7_subset_run1.json`, `_run2.json`).
- Direct B06/B07/F05 behaviour tests (signature TypeError; dict-manifest refusal; symlink
  refusal with payload).
- Audit-hook demonstration of the subject's two opens at verify+import (F1).
- PYTHONPATH-poisoned non-isolated worker run (F2): `_tmp_KIMI_poison/`,
  `_tmp_KIMI_poison_FIRED.txt`.
- Blind-spot re-demonstrations: `math.radians`, `tangent_plane_offsets` (F6).
- Sentinel verify-hook suite copy + run (F1-fix proof): `_tmp_KIMI_v7_hookcheck_suite.py`,
  `_tmp_KIMI_v7_hookcheck.json`, `_tmp_KIMI_v7_hook_sentinel.txt`.
- Independent 65,060-object enumeration without `close_manifest` (question 8b):
  `_tmp_KIMI_enumerate_v7.py`, `_tmp_KIMI_enumeration_v7.json`.
- Fixture battery re-execution: `_tmp_KIMI_v7_fixtures.out` (byte-identical after the
  trailing exit line is removed).
- Duplicated-extra adjudication shape: `_tmp_KIMI_v7_dupextra.out`.
- `python3 -I` sys.path inspection; numpy/astropy resolution under `-I` + the pinned
  add-back.

## Constraints and uncertainties

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not launch, authorize, inspect or mutate any downloader or transfer process; no image
  bytes were read. This report clears the closure mechanism; it does not itself fire
  anything, and the 148 GB ceiling stays tied to the confirmed 12,117.
- The executor reported my full-suite process dead at ~500 s; it kept running and completed
  normally (same behaviour as my v6 runs). No result above depends on the executor's process
  accounting; the receipt and run log are the evidence.
- Extra jobs ran concurrently with the first half of my full suite run; per-probe timings
  match the shipped receipt's (N05 138.1 s vs 141.3 s), so no timing-sensitive probe was
  affected.
- The stable hash is a per-installation witness (absolute paths in B04/G01 payloads);
  cross-machine equality is neither expected nor claimed.

## Testimony

- `DOWNLOAD_QUEUE_PLAN_20260825.md` records the ≈148 GB ceiling tied to the 12,117
  measurement, states the ceiling raise is not authorization to fetch, and states no image
  byte has been fetched. I read that record; I did not inspect live transfer state.
- The parent receipts' 13 chunk records carry TAP job URLs and per-chunk digests. I verified
  the envelope's pin, schema fields, chunk sequence and sums against the loader's checks; I
  did not re-query the remote jobs or reconstruct the parent from archived payloads.
- The brief's "~200 s per closure / ~45 min" estimate held (1,963.7 s full run under
  concurrent referee load; 156.9 s direct enumeration).
- Lane remnants: `runner_v7_kimi.log` was created empty by the dispatch script; this report
  is the seat's product. No other seat's v7 report is present in this directory as of
  writing.

**CLEAR**
