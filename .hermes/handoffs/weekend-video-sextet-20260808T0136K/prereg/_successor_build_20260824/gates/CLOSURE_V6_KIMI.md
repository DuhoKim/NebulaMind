# CLOSURE V6 REFEREE — KIMI

## Verdict

**CLEAR** — with conditions named below. The four v5 blockers are closed to the standard the
rounds have enforced: the process boundary reports true digests regardless of what the
presenter's process rebinds (B01/B02 versus B03), the required set is derived inside the check
from byte-pinned artifacts read once and parsed from the verified snapshot, the planner is
bound by file bytes plus a reachable-state fingerprint that is re-checked after the plan, one
adjudication names duplicates, omissions and extras together, and malformed input leaves as
one closure refusal. I independently reproduced the 12,117-brick closure and its plan digest
without calling `close_manifest`. None of my findings gives a presenter who does not own the
machine a path to a false acceptance through the production path; they are numbered below with
severities, and none is blocking. Two items remain open by the authors' own statement and are
outside this mechanism's scope: the selection has no producer receipt (CODEX-V5 F6, upstream),
and the site-packages/interpreter residual (machine-ownership threat).

## Scope and custody

I ruled only on the v6 closure mechanism and the artifacts the brief names. I did not read
`/Users/duhokim/NebulaMindData/`. I did not inspect or mutate any live downloader. Apart from
this report and `_tmp_KIMI_*` artifacts in this gate directory I wrote nothing.

Independently computed SHA-256 (all matching the pins/brief where a pin exists):

- `../ref/successor_ref_v6.py`: `d921d7445ddfee37eb3f91340730bd53989d53ad480287e3e1f987dff0784805`
- `../ref/closure_worker.py`: `88f66f63eee6d023fa899014ca61f56dfa2895391618e31c4f1fe383a9c838e9`
- `../ref/FIXTURES_V6_20260826.out`: `9ff7c82df4a25a380747ac90e1d61c39690b2eb65cffc61b4b5c5beab3f00b1c`
- `closure_probe_suite_v6.py`: `08714ec1584bcffc59551c74e7403cab042ddefd6cfd7aeae3f56c01b1b65708`
- `CLOSURE_PROBE_V6_RECEIPT_20260826.json`: `cf6b96df60aa56fa922173c9af6f60b4907e2ab8426c9320d508c52185f6e8c9`
- `../ref/successor_ref_v4.py`: `8191c42be1e8153e80480c0d110eb03c8f9c92f91895692e333af3fcbef50a21` (unchanged; the v4 reports stay legible against it)
- `../ref/successor_ref_v5.py`: `02237163b27be3a531676275e10dfd08c2ae6198bf383b2ffd0f63e9437c1171` (unchanged; CLOSURE_V5_CODEX stays legible)
- `../../_objmanifest_20260820/build_object_manifest.py`: `c63030e2878bbea126ef32de1e3687bdf550457aa0cbf31c02fc1743e5e369ed`
- `../../adapter/nm_brick_cutout_adapter.py`: `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f` — equals `PINNED_ADAPTER_SHA256` in the objmanifest
- `../../_cutout_runner_20260820/cutout_runner.py`: `ccb9b8fed457333669e54fa9f0a3dac645dc866a56c6cd8dc665ffd4d93b1bcc`

Pinned-artifact checks on disk:

- sidecar `863e5ded…` == `PINNED_UNIVERSE_SHA256` == `OFFICIAL_SIDECAR_SHA256` (objmanifest).
- count table `4e4ec45d…` == pin; columns `(brickid, n_cut6_dered)`; 270,577 rows; total 832,393.
- selection `b913939d…` == pin; shape `(6445,)`, dtype int64, 6,445 unique.
- parent `425a42c3…` == pin; 65,060 rows.
- parent receipts `41716d47…` == pin; 13 chunks; chunk rows sum 65,060; chunk bricks sum 6,445;
  `output_sha256` equals the parent file's digest.

## Reproduction (question 1)

Three production-uncached runs of the pinned suite exist now: the shipped receipt
(`_tmp_closure_probe_run_45235`) and two of mine (`…_53872`, `…_56374`). All three: 29/29
conforming, no non-conforming probe, no error-typed probe, verdict SUITE-CONFORMING.

- shipped `stable_sha256`: `28e6f23571b09f9e284f9ffa15543a034c4caffa21d387afe17917cb734b6f51`
- my run 1: `e690e0a0c78d19c05c0063ecf265f0c0c5e5fa2f21885e50286fa6116cefe254` (2,161.5 s)
- my run 2: `0faecd18303fc6820b19ee497406b206a459799660e6d48afe7b6184532a17dd` (2,154.5 s)

**My `stable_sha256` does not match the receipt's, and the cause is fully diagnosed, not
suspected:** an exact recursive diff of the stable objects shows the ONLY differences between
any pair of the three runs are the `result` payloads of probes F03 and F04, which embed the
absolute path of the per-process run directory (`_tmp_closure_probe_run_<pid>/counts_link.csv`,
`…/counts_fifo.csv`). `normalise()` rewrites the run dir to `$RUN` in the `message` field but
the `result` dict passes through `jsonable()`, which keeps strings verbatim. Every other byte
of the stable block — all 29 outcomes, messages, digests, counts, the plan digest, the summary —
is identical across three processes. The suite's outcomes reproduce exactly; its stable hash
cannot, by construction. That is finding F2 below.

Both my receipts are preserved: `CLOSURE_PROBE_V6_RECEIPT_KIMI_run1.json`,
`CLOSURE_PROBE_V6_RECEIPT_KIMI_run2.json` (the second overwrote the first at
`CLOSURE_PROBE_V6_RECEIPT_KIMI.json`; `CLOSURE_PROBE_V6_RUN_KIMI.out` is interleaved by both
runs and is not clean evidence).

## Numbered findings

### F1 — MAJOR (suite fidelity, non-blocking) — the `verify` hooks are registered and never invoked

**Symbol/line.** `probe(..., verify=None)` stores the hook in the probe record
(`closure_probe_suite_v6.py:101-115`); the conformance computation in `main()` is
`out["actual"] == p["expect"]` plus the `mentions` substring (`:688-691`) and never references
`p["verify"]`; receipt rows carry no verify outcome (`:692-698`).

**Why it fails.** The brief's answer to CODEX-V5 F7 is that "several probes now carry a
`verify` hook that asserts on the structured result." They carry it; nothing runs it. The
SUITE-CONFORMING verdict is exactly as narrow as v5's: PASS/REFUSE plus a message substring.
I demonstrated this dynamically, not by inspection alone: I copied the suite (pinned original
untouched, digest above) and gave R05 a verify hook that writes a sentinel file if called.
`--only R05` completed SUITE-CONFORMING and the sentinel does not exist
(`_tmp_KIMI_hookcheck_suite.py`, `_tmp_KIMI_hookcheck.out`).

**What rescues the evidence this round.** I evaluated every hook's assertion myself against
the shipped receipt's retained results and my own worker-level runs, and all of them hold:
P01 (`planner_digest == planner_digest_after_plan`, `1617af00…` both), R02 (`missing_count`
100; I re-ran the shape at the worker and the runtime `missing_from_manifest` really is 100
entries, exactly the expected names — `_tmp_KIMI_r02_runtime.json`; the worker's receipt does
not truncate, only the suite's `jsonable()` does, at 8 entries), R04 (missing 0, duplicate 1),
R08 (duplicate 1 AND missing 1, both named: `0001m252` duplicated, `0001m250` missing),
B01 (counts digest `4e4ec45d…`, the true table), B02 (parent digest `425a42c3…`, the true
file), B03 (counts digest `e9064985…`, the caller's table — I recomputed that exact digest
from the suite's mutation and line-ending convention), N05 (`planner_before` `1617af00…` !=
`planner_after` `83f9abd7…`), U02 (`incoherent_rows` == 5, the cap bug from CODEX-V5 F5 is
gone). So the hooks assert what their `basis` claims, and the claims are true — but the suite
does not establish that; I did.

**Smallest sufficient repair.** In the runner loop, when `p["verify"]` is present, call it on
`(out["actual"], out["result"])`, fold its boolean into `conforms`, and record its note in the
row. Stop truncating structured refusal lists in the receipt (or record the untruncated length
alongside — the counts already survive).

### F2 — MAJOR (receipt reproducibility, fail-safe direction) — `stable_sha256` is per-process by construction

**Symbol/line.** `jsonable()` (`closure_probe_suite_v6.py:625-637`) keeps strings verbatim;
F03/F04's `ManifestClosureError.result` carries the absolute run-dir path
(`{"symlink": str(path)}`, `{"not_regular": str(path)}` — `successor_ref_v6.py:434,446`), and
`DEFAULT_RUNDIR` includes the pid (`closure_probe_suite_v6.py:59`).

**Why it fails.** The brief asks a referee to reproduce `stable_sha256` "for the same mode."
Three same-mode runs produce three hashes (above) with byte-identical evidence content. A gate
that compares hashes across seats will report a mismatch on honest runs — a false alarm, never
a false acceptance, so the direction is fail-safe; but v5 achieved dictionary-equal stable
objects across seats (CLOSURE_V5_CODEX), so this is a v6 regression in the receipt, not in the
mechanism.

**Smallest sufficient repair.** run `normalise()` over `out["result"]` as well as
`out["message"]` (or have `verified_bytes()` return the pinned relative path in its refusal
payloads instead of the resolved absolute path).

### F3 — MAJOR (I1, mitigated by default and by the gate model) — `python_executable` lets the caller nominate the judging interpreter

**Symbol/line.** `def closure_receipt(manifest_bricknames, python_executable=None)` and
`_sp.run([python_executable or sys.executable, "-I", str(worker), …])`
(`successor_ref_v6.py:778,797`).

**Why it fails.** I1: no artifact that judges the manifest may be nominated by whoever
presents it. The parameter nominates the interpreter that runs the worker. I reproduced the
forge (`_tmp_KIMI_experiments.py`): a 3-line fake executable that ignores `-I` and the worker
and prints `{"outcome":"PASS","result":{…}}` was handed a nonsense manifest through
`closure_receipt(["not-a-real-brick"], python_executable=fake)` and the forged result was
returned to the caller; no closure ran. GPT56's leftover `_tmp_GPT56_fake_python` is the same
attack prepared. A sophisticated forge copies the public digest values from the brief, so the
receipt's self-provenance does not catch it; only the gate's external comparison or re-run
does — which the worker's own docstring concedes is "the part no code inside either process
can perform for itself."

**Why it does not block.** The default is the real `sys.executable`; the suite never overrides
it; the download gate is these referee rounds, which run the check themselves rather than
accepting presenter-produced receipts. The finding is that the production signature keeps a
nomination channel the invariants say should not exist, and neither the brief, the repair
record, nor the suite's `not_covered` list names it.

**Smallest sufficient repair.** Remove the parameter (hard-code `sys.executable`), or pin the
interpreter path in the receipt and state in the brief that a receipt is only as trustworthy
as its invoker — the gate must invoke `closure_receipt()` itself.

### F4 — MODERATE (I2/I5, bounded by the worker) — the reachable fingerprint still cannot see three classes of answer-determining state, and its stability partly comes from not seeing them

**Symbol/line.** `_reachable_fingerprint()` (`successor_ref_v6.py:320-370`); `_stable_repr()`
(`:286-298`).

**What it cannot see, demonstrated:**

1. **Modules-as-values.** A global resolving to a module is folded as the literal string
   `<module>`. The adapter's spherical math runs on `math` (e.g.
   `adapter/nm_brick_cutout_adapter.py:589-593`). I rebound `math.radians` to
   `lambda x: 0.0` and recomputed `frozen_planner_digest()`: unchanged at
   `1617af00eb7398abd93cc2726dbfb1ecfb24d07bede4b84c128ef2442bf40cb4`, still matching the pin
   (`_tmp_KIMI_experiments.py`). GPT56's leftover attack script probes the same seam.
2. **Pure-Python helpers resolved only from class methods.** A class contributes its methods'
   code objects; the walk does not recurse into what those methods resolve.
   `TanWcs.sky_to_pixel` calls the module-level `tangent_plane_offsets()`
   (`nm_brick_cutout_adapter.py:567-568`), on the plan path via
   `output_overlap_area_in_source_pixels`. I rebound `adapter.tangent_plane_offsets` to
   `lambda *a: (0.0, 0.0)`: digest unchanged, still matching the pin. N04 covers a helper
   resolved directly (`angular_separation_deg`); this shape is not covered by any probe and is
   not in `not_covered`.
3. **Callables without `__code__`** (C builtins, partials): folded as their type name only.

**On the second half of question 3.** Yes — the digest's cross-process stability comes partly
from ignoring these. `_stable_repr` reduces anything non-primitive to its type name precisely
so that memory addresses never enter the digest (the repair record's own lesson from
`repr(co_consts)`); stability and blindness have the same root cause. The docstring's "a
function is recursed into… what the digest cannot see, it names" overclaims: it names
unresolvable NAMES (`absent:<name>`) but does not name the class-method-reachable functions it
declines to recurse into, and a module's content is folded as `<module>`.

**Why it does not block.** In the worker these bindings are established once from
byte-hashed files (`frozen_planner_digest()` includes the objmanifest, runner and adapter file
bytes) in a fresh isolated interpreter that no presenter executes in; exploiting a blind spot
requires in-process mutation (excluded by the boundary; the in-process core is disclaimed by
its own docstring and evidenced by B03) or a poisoned dependency at import time — which is the
stated site-packages residual. Note the residual is wider than "numpy": under `-I` the
recorded `sys.path` still carries the CommandLineTools `python3.9/site-packages` ahead of the
one pinned add-back, and numpy AND astropy both resolve from the user directory
(`~/Library/Python/3.9/lib/python/site-packages`). The sidecar's file bytes are pinned, but
its PARSER (astropy) is answer-relevant and unpinned beyond the cardinality check; that is the
same stated residual, stated slightly too narrowly.

**Smallest sufficient repair.** Recurse into class methods' resolved globals the same way as
plain functions; fold pure-Python modules by a content hash of their source file; or narrow
the digest's documented claim to "the three planner files plus walkable pure-Python globals"
and fold C-extension/stdlib trust explicitly into the site-packages residual. Add a probe for
the class-method-reachable helper (N04's shape, one level down).

### F5 — MINOR — the symlink refusal is on the path, not the descriptor

**Symbol/line.** `verified_bytes()` checks `path.is_symlink()` (lstat on the path) and only
then `os.open()` (`successor_ref_v6.py:433-439`); the docstring says "both are checked on the
open descriptor."

**Why it fails.** `fstat` on the descriptor can confirm `S_ISREG` of whatever the open
resolved to; it cannot detect that the path was a symlink swapped in between the lstat and the
open. The window is microseconds and requires write access to the pinned tree — the in-place
modification class `not_covered` already concedes — but the docstring overstates the guarantee
that F03 evidences.

**Smallest sufficient repair.** open with `O_NOFOLLOW` so the descriptor itself refuses a
symlink, and drop the separate lstat.

### F6 — MINOR — the worker never validates that the manifest is a list

**Symbol/line.** `manifest = request["manifest"]` (`closure_worker.py:99`), then
`[str(b) for b in manifest_bricknames]` (`successor_ref_v6.py:742`).

**Why it fails.** Iterating a JSON object yields its keys. I passed the worker
`{"manifest": {name: 1 for each of the 12,117 required names}}`: exit 0, outcome PASS,
`manifest_entries` 12,117 (`_tmp_KIMI_dict_manifest.json`). A dict cannot under-cover or
duplicate, so this leniency cannot shrink a closure; and `closure_receipt()` normalizes
caller-side containers with `list(...)` before the boundary (`:794`), so the production entry
point is not affected — only direct worker callers. It is still an unvalidated type at the
trust boundary, and R06/R07 exist precisely because malformed shapes must fail closed.

**Smallest sufficient repair.** `if not isinstance(manifest, list): fail(...)` in the worker.

### F7 — MINOR (probe metadata) — S01–S05 and U01 `varies` still do not name the path-pin reassignment

**Symbol/line.** e.g. S01's `varies` ("a copy …, AND the pinned digest set to the copy's",
`closure_probe_suite_v6.py:490-498`) versus what `Ctx.redirect()` sets
(`PINNED_*_REL` and the digest together, `:142-146`).

**Why it fails.** CODEX-V5 F7 named this exact under-declaration for v5; B01/B02/F03/F04/U02
now name the `PINNED_*_REL` constants explicitly, but S01–S05 and U01 still describe only the
copy and the digest override. The redirect is uniform and the digest override is the declared
part, so no hidden change decides any outcome — but the metadata contract is that `varies`
records what changes.

**Smallest sufficient repair.** Add "and `PINNED_*_REL` points at that copy" to the six
`varies` strings.

### F8 — MINOR (stated open, confirmed) — thin generic-refusal payloads; environment guard unused on the closure path

R06's structured result is still `{"error": "TypeError"}` even though objects, selected-brick
count and every digest are known by the time the None manifest is iterated
(`successor_ref_v6.py:742`, after planning). The phase-aware refusal schema from GPT56-V5 F5 /
CODEX-V5 F5 remains unfrozen and unasserted — the repair record says so itself. Through the
worker the receipt still carries provenance, so the boundary receipt is not thin. Separately,
`require_environment()` (FROZEN_ENV: python 3.9, numpy 1.26.4, little-endian) is never called
by `close_manifest()` or the worker; the worker records the python version in provenance but
enforces nothing. Neither is blocking; both are recorded so the next round cannot say they
were invisible.

## Answers to the eight referee questions

1. **Reproduction.** No — and the mismatch is diagnosed to two strings, not suspected: the
   hashed stable block embeds the per-process run directory in F03/F04's `result` payloads
   (F2). Three same-mode runs (shipped + my two) are otherwise byte-identical: 29/29
   conforming, no error types, same plan digest. My stable hashes:
   run 1 `e690e0a0…`, run 2 `0faecd18…`, shipped `28e6f235…`.
2. **The process boundary and I1.** It is a real custody boundary for the demonstrated attack
   class: B01/B02 poison every pin in the presenter's process and the worker still reports the
   true digests and the true 12,117; B03 records that the in-process core reads the caller's
   table (its digest `e9064985…` recomputed by me). It is also still a longer path to the same
   trust at two points: the caller-nominated `python_executable` (F3, demonstrated forge), and
   the gate's external digest comparison, which no code inside either process can perform.
   The stated site-packages residual is not the only one — F3 is unstated, and the residual
   itself is wider than named: the CLT system `site-packages` precedes the pinned add-back on
   the recorded `sys.path`, and astropy (the sidecar parser) sits in the same unpinned
   directory as numpy.
3. **The reachable fingerprint (I2, I5).** It binds the three planner files byte-for-byte, the
   adapter pin, the prefilter, both entry callables' bytecode/defaults/kwdefaults/closures,
   and the walkable pure-Python globals by value — and the post-plan re-check catches mutation
   during the 65,060-object loop (N05). It still cannot see: module objects' contents
   (`math.radians` rebound, digest unmoved — demonstrated), pure-Python helpers reachable only
   through class methods (`tangent_plane_offsets` rebound, digest unmoved — demonstrated),
   C callables (type name only), the retained objmanifest instance `close_manifest` actually
   plans on (stated in `not_covered`), and a mutation that is reverted before the post-plan
   digest (uncovered shape; in-process only). Its cross-process stability comes partly from
   reducing all of these to type-name strings — stability and blindness share a root cause.
   In the worker these matter only at import time, which is the stated site-packages residual.
4. **Verified-bytes custody (I5).** Real, with one sliver. Every artifact is opened once with
   `O_RDONLY|O_NONBLOCK`, `fstat`-checked regular, hashed as read, and parsed from that
   snapshot; the FITS sidecar is re-parsed by the frozen loader from a private byte-identical
   snapshot whose basename the loader requires; F03/F04 refuse the symlink and the FIFO.
   Remaining path: the symlink check is an lstat on the path, not a flag on the open
   (F5, TOCTOU sliver), and the snapshot file is re-read from disk by the planner's loader —
   from a private worker temp dir in production, so the consumer of that path is the worker
   itself. No path by which consumed bytes differ from verified bytes is reachable to a
   presenter without write access to the pinned tree (already conceded) or the worker's own
   temp dir.
5. **The single adjudication (I3, I4).** Correct on every shape I exercised or inspected. R08
   refuses and names BOTH the duplicate (`0001m252`) and the omission (`0001m250`) in the
   structured result — v5's exact failure. Duplicates, omissions and extras are computed from
   the finished required set and reported together with full counts; the message truncates to
   four examples but the structured result carries everything and the worker's receipt does
   not truncate (R02 runtime: 100/100 names). Other shapes checked: extra-only (R03),
   duplicate-only (R04), empty (R05), None (R06 — one refusal, thin payload, F8), wrong-type
   entries str()-converted and reported as missing+extra with correct counts (R07), and a JSON
   object as the manifest (accepted as its keys — F6; cannot under-cover). I found no shape
   where one condition still masks another.
6. **Probe fidelity.** The hooks assert what their `basis` claims — but the runner never calls
   them (F1, demonstrated with a sentinel); I verified each assertion by hand and all hold.
   Metadata: S01–S05/U01 still under-declare the `PINNED_*_REL` reassignment (F7). Nothing else
   under-declares: B01–B05, N01–N05, F03/F04, R01–R08, U01/U02, G01 are faithful, and N05's
   vacuous-guard AssertionError would surface as an ERROR row, which is the right design.
7. **Coverage.** Beyond the 29 probes and the `not_covered` list: F3 (caller-nominated
   interpreter); F1 (no meta-check that hooks run); F4.2 (class-method-reachable helper
   mutation); mutation-then-revert during the plan defeating the post-plan re-check; F5
   (symlink TOCTOU); F6 (non-list manifest at the worker's stdin); `require_environment()`
   unused on the closure path; no timeout on the worker subprocess (a hung worker hangs the
   gate — availability); extra keys in the worker's stdin JSON ignored; astropy unpinned as
   the sidecar parser (folded into the stated site-packages residual).
8. **The 12,117 figure.** Confirmed independently against v6. I imported the frozen planner
   and parsed the pinned parent directly — never calling `close_manifest` — and planned all
   65,060 rows (`_tmp_KIMI_enumerate.py`, `_tmp_KIMI_enumeration.json`, 153.3 s): **12,117
   distinct required bricks**, plan digest
   `aaeaa9f37aabf1da6000a6ad07890cfe010677e301583530ba1a108833e3b3f1`, per-object histogram
   `{1: 55566, 2: 8801, 3: 591, 4: 102}` — the digest identical to the shipped v6 receipt and
   to the v5 measurement the ceiling order cites, and the histogram identical to CODEX-V5's
   independent enumeration. The v5→v6 planner-digest change (`10cea7a6…` → `1617af00…`) binds
   more state without changing the plan, as the repair record claims. Ceiling arithmetic:
   12,117 × 12.2 MB = 147,827.4 MB = 147.83 decimal GB ≈ the approved ≈148 GB;
   12,117 / 6,445 = 1.88006. The two historical probe objects (ls_id 10997315463551936,
   10995116744378804) are not rows of the pinned parent, so they are not part of this
   enumeration; in v6 the omission-refusal property they anchor is exercised by R01/R02
   against the derived required set (v6 names the sorted head of that set, e.g. `0001m250`,
   not the v4-era fixture bricknames).

## Failed attacks / positive evidence

- All named subject/suite/worker/fixture hashes reproduce; all artifact pins verify on disk.
- B01/B02: poisoning `PINNED_COUNTS_*`, `PINNED_PARENT_*` and the receipt pins in the
  presenter's process changes nothing in the worker's receipt (true digests throughout).
- B03: the in-process core demonstrably reads the caller's table (receipt digest
  `e9064985…` = my independently recomputed digest of the suite's moved table).
- B04: an un-isolated worker refuses to run; B05: a subject/digest mismatch refuses.
- N01–N04: pre-verification live mutations (plan_object, prefilter, intersection threshold,
  a directly-resolved helper) all move the digest and refuse. N05: a valid-valued mutation
  timed to land mid-plan is caught by the post-plan re-check and reports both digests.
- F03/F04: symlink and FIFO refused. S01–S05: count-table duplicate/negative/total and
  receipt schema/sum faults refused. U01: selection brick outside the geometry universe
  refused. U02: five coordinate-incoherent parent rows refused with the true total (5), not a
  capped example count.
- The full 29-probe suite conforms on two independent runs of my own (2161.5 s, 2154.5 s).
- The required set, plan digest and per-object histogram reproduce without the closure code
  path at all (question 8).
- `plan_object_bricks()` (the retired reimplementation) raises rather than planning.

## Evidence ledger

Content-read: the v6 brief; `CLOSURE_REPAIR_V6_20260826.md`; the three required prior rounds
(`CLOSURE_RECEIPT_GPT56.md`, `CLOSURE_RECEIPT_CODEX.md`, `CLOSURE_V5_CODEX.md`);
`closure_probe_suite_v6.py` (whole); `../ref/successor_ref_v6.py` (closure region 53-816 in
full); `../ref/closure_worker.py` (whole); `../ref/FIXTURES_V6_20260826.out`;
`CLOSURE_PROBE_V6_RECEIPT_20260826.json` (whole); `../acquire/DOWNLOAD_QUEUE_PLAN_20260825.md`;
`../../_objmanifest_20260820/build_object_manifest.py` (1-280);
`../../adapter/nm_brick_cutout_adapter.py` (planner and WCS regions);
`CLOSURE_PROBE_FINDINGS_20260825.md`; lane remnants (`_tmp_GPT56_fake_python`,
`_tmp_CODEX_fake_python`, `_tmp_GPT56_v6_attacks.py`, `runner_v6_*.log`, `_tmp_v6_smoke.out`).

Commands/probes (all outputs under this directory as `_tmp_KIMI_*` or named receipts):

- `shasum -a 256` over every artifact listed in Scope and custody.
- `python3 closure_probe_suite_v6.py --list`.
- Two full production-uncached suite runs (`--json CLOSURE_PROBE_V6_RECEIPT_KIMI.json`;
  preserved as `_run1.json`, `_run2.json`), plus recursive stable-object diffs against the
  shipped receipt and each other.
- `_tmp_KIMI_experiments.py` — python_executable forge; `math.radians` digest probe.
- `tangent_plane_offsets` digest probe (one-liner, output in session).
- `_tmp_KIMI_enumerate.py` — direct 65,060-object enumeration without `close_manifest`.
- `_tmp_KIMI_dict_manifest.py` — worker-level list/object manifest shapes.
- `_tmp_KIMI_r02_runtime.py` — 100-omission refusal at the worker boundary, untruncated.
- `_tmp_KIMI_hookcheck_suite.py` (`--only R05`) — verify-hook sentinel; suite's pinned
  original untouched.
- Recomputation of the B03 moved-table digest from the suite's own mutation.
- `python3 -I` sys.path inspection; numpy/astropy resolution under `-I` + the pinned add-back.

## Constraints and uncertainties

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not launch, authorize, inspect or mutate any downloader or transfer process; no image
  bytes were read. This report clears the closure mechanism; it does not itself fire anything.
- This pass is limited to the closure mechanism. The selection's producer authorization
  (CODEX-V5 F6) is upstream of it and remains open by the authors' own statement.
- Both my full-suite runs wrote the same receipt path and run log; run 1's receipt was
  preserved before run 2 overwrote it. The interleaved run log was not used as evidence.
- The first suite process I launched was reported dead by my executor but kept running; both
  completed. No result above depends on the executor's process accounting.

## Testimony

- `FIXTURES_V6_20260826.out` states all fixtures pass, including the CLOSURE-* battery. I
  verified the file's digest and read its content; I did not re-execute `run_fixtures()`.
- The parent receipts' 13 chunk records carry TAP job URLs and per-chunk digests. I verified
  the envelope's pin, schema fields, chunk sequence and sums; I did not re-query the remote
  jobs or reconstruct the parent from archived payloads.
- `DOWNLOAD_QUEUE_PLAN_20260825.md` records the raised ≈148 GB ceiling tied to 12,117 and
  states no image byte has been fetched. I read that record; I did not inspect live transfer
  state.
- `runner_v6_gpt56.log` and `runner_v6_codex.log` each contain only a provider safety-filter
  refusal; the GPT56/CODEX v6 attack remnants on disk show preparation (fake interpreters,
  the math.radians probe) but no completed seat report. As far as this directory shows, v6 has
  been refereed to completion by no other seat.
- The brief's "~200 s per closure / ~45 min" estimate held on this machine under load
  (2,154-2,162 s per full run; 153 s for the direct enumeration).

**CLEAR**
