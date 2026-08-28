# BS-2a CODE GATE — CODEX, round 6

Verdict: **CLEAR for FREEZING the quality-predicate component; this is not a fill authorization.**
The reviewed bytes match the brief's pinned digest exactly, before and after every probe. Both
round-5 findings (`E18` arithmetic reached past `E21`'s flag; `E15` hashing reached past `E24`'s
flag) are repaired by structural-condition returns, confirmed by direct execution and by literal
source-level deletion of the repair, not by trusting the diff. `--self-test` genuinely passes
(36 controls, 0 failures, 26/26 codes covered) and `--acquire acquire` genuinely reproduces 49,211
of 65,060 with MATCH, both re-run independently in this session against the live `acquire/`
directory. A strict deletion probe — crash scored as NOT detected, only a named control counts —
catches all 26 single codes and all 325 pairwise combinations by name, with zero crash-only
credits; six of those pairs were additionally verified by literal AST-level deletion of the real
`refuse()` call sites and a real re-run of `self_test()` against each mutant, not merely by
filtering already-captured output. I could not make the verifier ACCEPT a receipt it should
reject. I could make it raise, but only with a hostile Python object the module's own docstring
already excludes by name and that the builder provably cannot produce — that result confirms the
docstring's disclaimer rather than contradicting it. The docstring's honesty claim under attack:
the "no crash path reachable from the builder" sub-claim is true by direct census of all 65,060
built rows, and a crash cannot produce a false PASS because the string `PASS` never appears as an
emittable token anywhere in the module's control flow, and every crash path I could construct or
locate in five prior rounds' reports exits the process non-zero before either the receipt JSON or
the `MATCH`/`REFUSED` summary line prints (one narrow exception is disclosed below and does not
change this). No remaining defect blocks FREEZING the quality-predicate component. Filling BS-2a
remains blocked on `verify_cutout_integrity` (Row C2), the confidence threshold, retry/failure
semantics, the ledger schema, and §6.3(9)'s adversarial producer fixtures under transformed
cutouts — none of that is built, and it needs cutouts BS-2a does not yet have.

## Identity and executed comparison

- Subject: `../ref/bs2a_quality_gate.py`.
- Brief-pinned sha256: `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`.
- Independently computed before testing (`shasum -a 256`):
  `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`.
- Independently recomputed after all probes (this review never edited the reviewed subject):
  `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`.
- **Comparison: MATCH** — the reviewed bytes are exactly the brief-pinned subject, before and
  after this review.
- `successor_ref_v9.py` sha256, before and after this review:
  `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` — unchanged. `git status
  --short` against both reviewed paths reported nothing (clean). Grepped the subject for
  `successor_ref_v9`: exactly one match, the docstring line 6 ("`successor_ref_v9.py` is FROZEN
  and this file does not touch it"). Not imported, not opened, not executed anywhere in the file.
- Cross-checked against git history (`git log --oneline -- ref/bs2a_quality_gate.py`): the tip
  commit `8cb1a03e5` ("a type gate must return, and the robustness limit is now stated in the
  module") is exactly the round-5 repair the brief describes — `git show 8cb1a03e5` shows the two
  `return bad` statements added after the `E21` and `E24` refusals, the two controls' expected sets
  shrinking (`{E18,E21}→{E21}`, `{E20,E23,E24}→{E24}`), a new `string count field` control, a new
  `unhashable join key` control, and the new "THE ROBUSTNESS LIMIT" docstring section. This
  corroborates the diff's shape; it is not a substitute for the independent behavior checks below.

## Required executions — run myself, not taken from the brief

- `python3 ref/bs2a_quality_gate.py --self-test --acquire acquire` (from the successor-build root,
  against the live `acquire/` directory): exited 0, printed `self-test: 36 controls, 0 failure(s)`
  and `OK every one of 26 checks is exercised by a control`, with every one of the 36 individual
  control lines printing `OK` and its declared exact code set — matches the brief's "36 controls,
  0 failures" claim to the digit.
- `python3 ref/bs2a_quality_gate.py --acquire acquire`: exited 0, printed `n_parent: 65060,
  n_joined: 65060, n_retained: 49211, n_excluded: 15849, evidence_sha256:
  0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca` and `retained 49,211 of 65,060
  (expected 49,211) — MATCH` — matches the brief's "49,211 of 65,060, MATCH" claim exactly.

## Recomputed frozen constants, without importing the module

Independent script (`gates/_tmp_CODEX_bs2a_r6_recompute.py`, this round's own fresh script, not
inherited from round 5) that never imports `bs2a_quality_gate` — it re-derives the join, predicate,
and both digests directly from `acquire/positions_selected.csv` / `acquire/quality_selected.csv`,
and only reads the subject's source *text* via regex to pull the five pinned literals for
comparison:

| constant | pinned literal | independently recomputed | match |
|---|---|---|---|
| `PARENT_SHA256` | `425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831` | direct file hash | MATCH |
| `QUALITY_SHA256` | `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3` | direct file hash | MATCH |
| `PARENT_ROWS` / `EXPECTED_RETAINED` | `65_060` / `49_211` | independent join: 0 duplicate parent keys, 0 duplicate quality keys, 0 missing, 0 orphaned + predicate applied per-row = `65060` / `49211` | MATCH |
| `PARENT_KEYSET_SHA256` | `550e50a8c6fbea2a72ac93597b8c0fbc6798fc78172a5056f10329d7dde93bd6` | independently recomputed | MATCH |
| `EVIDENCE_SHA256` | `0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca` | independently recomputed | MATCH |

Script output: `ALL_MATCH True`. The trust root holds: the two source digests are exactly the
sha256 of the real `acquire/` CSVs; the join is genuinely total and one-to-one; both derived
commitments match exactly what the sources produce.

## Numbered findings

### 1. Both round-5 findings are repaired, verified two ways (not one)

- File/lines: `../ref/bs2a_quality_gate.py:388-393` (`E21`'s `return bad` after the `mistyped`
  check) and `:449-454` (`E24`'s `return bad` after `mistyped_keys`).
- **Behavioral re-derivation** (`gates/_tmp_CODEX_bs2a_r6_probe.py`), against the real module
  imported fresh this round:
  ```
  n_retained = "49211" (JSON string)  -> returns {E21}, no TypeError
  n_retained = None    (JSON null)    -> returns {E21}, no TypeError
  n_excluded = None    (JSON null)    -> returns {E21}, no TypeError
  brickid = []          (JSON array)  -> returns {E24}, no unhashable-type crash
  brickid = {}          (JSON object) -> returns {E24}, no unhashable-type crash
  objid   = [1, 2]       (JSON array) -> returns {E24}, no unhashable-type crash
  ```
  All six of round 5's exact crash inputs now refuse cleanly with exactly the declared repaired
  code set, no exception, no traceback.
- **Literal source-level confirmation, not just import-and-call**: I re-parsed the live source
  with the `ast` module, confirmed via source read that both returns are keyed to the
  independently-computed structural booleans (`if mistyped:` / `if mistyped_keys:`), not to
  whether `bad` is non-empty — matching the pattern already established at the three earlier
  early-return sites (`E25`/`E26`, `E01`/`E02`, `E09`). This means deleting the underlying
  `refuse()` call still leaves the structural early return intact, so a deleted check cannot
  regress into crash-only detection — verified directly for `E18`/`E21` and `E15`/`E24` in the
  pairwise spot-check below (`gates/_tmp_CODEX_bs2a_r6_pairspot.py`), which literally removes the
  `refuse("E21", ...)` and `refuse("E24", ...)` statements via AST transform and re-runs the real
  `self_test()`: both mutants failed cleanly by name (`FAIL float count fields`, `FAIL string
  count field`, `FAIL non-string join key`, `FAIL unhashable join key`, etc.), zero exceptions.
- The brief's own recap ("36 controls, 0 failures, 26/26 codes covered ... Digests unchanged,
  `--acquire` still 49,211 MATCH") is confirmed to the exact figure by this round's own execution,
  not accepted from the brief text.

### 2. Strict deletion probe — 26/26 single codes, 325/325 pairs, 0 crash-only, 0 undetected

Method (`gates/_tmp_CODEX_bs2a_r6_probe.py`): for every one of the 26 codes, an AST transform
deletes exactly one `refuse(code, ...)` call site inside `verify_receipt()` from a fresh in-memory
copy of the real source (never the reviewed file on disk), compiles and executes the mutant, and
re-runs every control whose declared `expect` set includes that code against it. A deletion counts
as **NAMED_CONTROL_FAILURE** only if a control's `codes_of(...)` output differs from its declared
`expect` (which the strict rule requires be a genuine miss, not a raised exception); a raised
exception during that re-run is scored **CRASH_ONLY**, never credited as detection; if neither
happens, the code is **UNDETECTED**.

- **Single-code deletion, all 26 codes**: **26/26 NAMED_CONTROL_FAILURE, 0 crash-only, 0
  undetected.** (Full per-code detail captured in this session's tool output — e.g. deleting
  `E21` is caught by name by all three of `float count fields`, `boolean count field`, `string
  count field`; deleting `E24` is caught by name by both `non-string join key` and `unhashable
  join key`.)
- **Pairwise deletion, all 325 combinations of 2 codes out of 26** (`C(26,2) = 325`, the correct
  count for the current 26-code battery): computed from each control's real executed refusal set
  minus the two deleted codes, compared against its declared expected set — **325/325
  NAMED_CONTROL_FAILURE, 0 crash-only, 0 undetected.** This filter-based method is valid because
  `verify_receipt()`'s only branches on `bad`'s *contents* are the three pre-existing structural
  early returns plus the two round-5 ones, none of which are keyed to specific refusal codes
  being present or absent (confirmed by direct AST walk of every `Name(id='bad', ctx=Load)`
  reference in the function — the only such uses are the five `return bad` statements and the
  final `return bad`, none of them conditioned on `bad`'s contents).
- **Literal source mutation, not filter-simulated, for 6 spot-checked pairs**
  (`gates/_tmp_CODEX_bs2a_r6_pairspot.py`): `{E18,E21}` (this round's own repaired pair),
  `{E15,E24}` (this round's other repaired pair), `{E25,E26}` (round-4 repair), `{E09,E25}`,
  `{E20,E24}`, `{E01,E25}`. Each pair had both real `refuse()` call sites literally removed via
  AST transform from a fresh copy, and the mutant's actual `self_test()` was executed end to end
  (not output-filtered). All six produced a genuine `self-test: 36 controls, N failure(s)` with
  every affected control printing `FAIL <name>: ... missing [...], spurious []` — never a
  traceback, never a false `OK`. This directly answers the brief's ask to reproduce the probe
  strictly and not credit a crash: none of the 26+325 deletions I ran were crash-credited, and the
  6 I mutated at the literal source level confirm the filter-based sweep agrees with real
  execution.

### 3. Failed attacks — could not make the verifier ACCEPT a receipt it should reject

All of the following were tried against the real, unmodified subject this round; all refused
cleanly, none accepted, none silently laundered (`gates/_tmp_CODEX_bs2a_r6_probe.py`):

- Honestly re-digested forgeries on the real authenticated fixture: forged `brickid`/`objid`
  string values (refused `{E20,E23}`), forged quality values `flux_ivar_r`/`psfsize_r`/`nobs_r`
  (refused `{E23}` or `{E12,E23}` depending on whether the predicate outcome also flipped),
  flipped `quality_pass` (refused `{E12,E16,E23}`), non-string `brickid` as `int` or `list`
  (refused `{E24}` cleanly, not a crash — this is exactly last round's repaired shape, re-verified
  fresh), `quality_pass` as `int` `1` instead of `bool` (refused `{E11,E23}`), a `None`
  `flux_ivar_r` (refused `{E10,E23}`), a `NaN` `psfsize_r` (refused `{E10,E23}`) — every one of
  these mutations re-digested the evidence honestly (as a real forger with write access to both
  fields would), and every one was still caught by the membership/value checks (`E10`–`E12`,
  `E20`, `E23`, `E24`), not merely by a stale digest mismatch.
- A dict key type outside JSON's representable key space (`thresholds[0] = 1`, i.e. a Python `int`
  dict key mixed with string keys) did raise — `TypeError: '<' not supported between instances of
  'int' and 'str'` — but this is not reachable from JSON at all (JSON object keys are always
  strings; this requires hand-constructing a Python dict directly, bypassing `json.loads`
  entirely) and is explicitly the class the docstring's "Python library caller, not a JSON
  receipt" caveat already excludes. Recorded for completeness, not scored as a finding against the
  JSON-native threat model every control in `CONTROLS` and every prior round's findings are scoped
  to.
- A non-string, non-JSON-key integer key mixed into an **evidence row** dict (`ev[0][0] = 1`) did
  **not** crash — refused cleanly `{E09}` (the row now has an extra key beyond `EVIDENCE_FIELDS`,
  caught by the schema-closure check with no crash, since dict iteration/comparison here never
  needs total ordering).

### 4. Attacking the docstring's robustness-limit claim directly (the brief's five sub-questions)

**(1) Is the recorded limit honest and sufficient, or does a reader inherit "verified" for an
unestablished property?** The docstring separates the two properties under distinct headers
("Sound against forgery — established" vs. "Hardened against arbitrary hostile input — NOT
established, and deliberately not claimed") and closes with an explicit imperative: "Anything that
fills a slot against this module must state that limit rather than inherit the word 'verified'."
I re-read every other docstring section for leakage — the "WHAT IS AND IS NOT CLAIMED" section
(outcome-blindness, non-independence-from-handedness disclaimer) and the "WHAT THE VERIFIER BINDS"
section (custody, not science) are both consistently scoped, using "established"/"not established"
language nowhere else contradicted by an unqualified "verified". This is honest disclosure, not
a hedge that quietly reclaims the word elsewhere.

**(2) Is "unreachable from the builder" true?** Direct census over the actual live build output,
this session, not sampled: **0 of 65,060** built evidence rows are off-schema; **0** have a
non-`dict` row type; **0** have a non-string `brickid`/`objid`; **0** have a non-float quality
value; **0** have a non-`bool` `quality_pass`. `verify_receipt()` on this real receipt/evidence
pair returns `[]` (clean pass) with no exception. Source reasoning corroborates: `_rows()` returns
`csv.DictReader` output (always well-formed dicts of strings); `_key()` unconditionally
`str()`-coerces and strips both join fields; `float(q[c])` either succeeds (producing a real
`float`) or raises inside `build_evidence()` itself — before any evidence row is ever constructed,
so a build that reaches `verify_receipt()` at all has already passed that gate; `quality_pass()`
returns a Python `bool` by construction (`and`-chained comparisons). The claim is **true** for
this study's actual sources, confirmed by execution, not merely by reading the code.

**(3) Can a crash produce a false PASS?** No crash I found or that any of the five prior rounds'
reports (both seats, all rounds) found ever causes `main()` to exit 0 or print a success token
after a crash. I checked this three independent ways this round:
  - Grepped the entire module source for the literal string `PASS`: it appears exactly once, in
    the docstring's own claim ("can never emit a PASS") — there is no `print`, `return`, or
    `f-string` anywhere in the module that emits the uppercase token `PASS` as output. The
    module's only success signals are exit code 0 plus the printed word `MATCH` — this matches
    what round 5 (both seats) and this round's parallel GPT56 R6 report also found, independently
    re-verified here by direct grep rather than taken on trust.
  - Reproduced a hostile hand-crafted `__float__`-raising object (`RuntimeError` from
    `float(hostile_obj)`) against `verify_receipt()` directly: it raises, uncaught, before any
    refusal list is returned — `RuntimeError`, not a refusal, not an accept. This input is outside
    every threat model this module's `CONTROLS`/`CODES` battery is built for (it requires
    constructing a Python object with a poisoned `__float__`, impossible via JSON, and impossible
    for the real CSV-reading builder, confirmed by finding 2's builder census) — consistent with
    the docstring's own explicit disclaimer, not a violation of it.
  - Ran `main()` itself end-to-end via real subprocess invocations, checking stdout content
    against the process exit code, for every crash class found across all six rounds that remains
    reachable through `main()`'s actual argument surface: a digest-mismatched `positions_selected
    .csv` (appended garbage bytes) exits 1 with **empty stdout** (the crash is inside
    `verified_bytes()`, before any JSON is printed) — `QualityGateError` raised and uncaught by
    `main()`, correctly non-zero, no MATCH, no PASS. Same for a digest-mismatched
    `quality_selected.csv`. A missing/empty acquire directory exits 1 with empty stdout
    (`FileNotFoundError`, uncaught, before any print). None of these produce output containing
    `PASS`; none exit 0.
  - **One disclosed asymmetry, not a false PASS**: `--emit <valid receipt> --emit-destination
    <directory that does not exist>` (reproduced fresh, on a throwaway acquire copy under `/tmp`,
    never the real `acquire/`) prints the true receipt JSON and the correct `MATCH` line — because
    `verify_receipt()` already succeeded honestly on real, unforged evidence — and *then* raises
    `FileNotFoundError` while attempting the file write, exiting 1. This is not a false PASS: the
    printed `MATCH` is honestly earned by a receipt that really does conform, the failure is
    strictly I/O on an operator-supplied output path (never adversary-controlled input to
    `verify_receipt()`), and the process still exits non-zero, so any caller gating on exit status
    (the only documented success signal, since `PASS` is never printed) correctly sees failure. I
    verified this is the same shape GPT56's parallel R6 report also found independently this
    round — reproduced here directly via subprocess rather than accepted from that report. It is
    an advisory (a caller that reads stdout for `MATCH` alone, ignoring exit status, would be
    misled), not a defect that overturns "cannot emit a PASS": no `PASS` token is printed on any
    path I found, in this round or any prior round's cumulative findings.

**(4) Find another raise.** The one new raise this round — the hostile `__float__` object — sits
squarely inside the module's own stated exclusion (arbitrary hostile Python objects, not JSON-
native input, not builder output) and is disclosed above rather than scored as a finding, since
scoring it as a defect would misstate what the docstring actually claims. I did not find a sixth
JSON-native/builder-reachable raise beyond the two the brief already confirmed repaired.

**(5) Can the verifier accept a receipt it should reject?** No — see finding 3's failed-attack
list; consistent with rounds 3-5's cumulative finding of zero false accepts.

### 5. `successor_ref_v9.py`: untouched

Confirmed by sha256 (identical before/after), `git status --short` (clean), file size and the
grep census in the Identity section above — the only reference is the docstring's own disclaimer
sentence.

## Testimony

The following are disclosed rather than exhaustively executed against production:

- The dict-with-non-string-key (`thresholds[0]=1`) and the row-with-integer-key
  (`ev[0][0]=1`) probes in finding 3 construct Python objects directly rather than via
  `json.loads(...)` — genuinely impossible to reach through the module's documented JSON-receipt
  threat model (JSON object keys are always strings), disclosed for completeness per the brief's
  "attack the framing" instruction, not scored as findings against that model.
- The pairwise deletion sweep for all 325 combinations is filter-derived from each control's real
  executed output (justified in finding 2 by a direct AST walk proving no code-content-dependent
  branch exists), with 6 of the highest-relevance pairs additionally confirmed by literal AST-level
  source deletion and a real `self_test()` re-run per mutant — not all 325 were literally
  source-mutated, matching the scope round 5 (both seats) used for the same reason.
- I did not read `/Users/duhokim/NebulaMindData/`.

Everything else in this report was executed in this session: the sha256 re-checks before and after
every probe, `git log`/`git show`/`git status` on the reviewed paths, `--self-test --acquire
acquire` and `--acquire acquire` against the live `acquire/` directory, the independent five-
constant recomputation via a script that does not import the subject
(`gates/_tmp_CODEX_bs2a_r6_recompute.py`), the AST-based single- and pairwise-code deletion sweep
(`gates/_tmp_CODEX_bs2a_r6_probe.py`), the six literal source-mutation pairwise spot-checks
(`gates/_tmp_CODEX_bs2a_r6_pairspot.py`), the round-5 repair re-derivation (both behavioral and
literal-deletion), the full 65,060-row builder-output type census, the hostile-`__float__` probe
and the `main()`/`--emit` subprocess probes including the digest-mismatch and missing-acquire-
directory cases (`gates/_tmp_CODEX_bs2a_r6_probe2.py`), and the literal-`PASS`-token source grep.
All temp scripts and outputs stayed under `gates/`, none touched `acquire/` or the reviewed
subject, and none used the real `acquire/` directory for the deliberately-corrupted-digest cases
(byte-identical throwaway copies under `/tmp` instead). This review does not fill BS-2a, authorize
a fetch, or resolve conditional independence.

## Freezing versus filling

**No remaining defect blocks FREEZING the quality-predicate component.** The predicate, the
authenticated evidence commitments, the verifier, the exact-set control battery, the builder
boundary census, and the recorded robustness limit are all independently reproduced this round and
hold. BS-2a stays **DESIGN, UNFILLED**: `verify_cutout_integrity` (Row C2), the confidence
threshold, retry and failure semantics, the ledger schema, and §6.3(9)'s adversarial producer
fixtures under transformed cutouts are not built, and those fixtures need cutouts that do not yet
exist. BS-6 and the first image byte remain blocked.

**CLEAR**
