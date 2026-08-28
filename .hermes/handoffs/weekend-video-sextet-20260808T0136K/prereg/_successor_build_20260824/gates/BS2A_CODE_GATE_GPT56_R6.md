# BS-2a CODE GATE — GPT56, round 6

Verdict: **CLEAR for FREEZING the quality-predicate component; not a fill authorization.** The reviewed bytes match the brief pin exactly. Both round-5 defects are repaired by returns keyed to the structural conditions, the real self-test passes 36/36, the real acquisition produces 49,211 of 65,060 and MATCH, and a strict source-deletion run catches all 26 checks through named control failures with zero crash-only credits. I found another raise only outside the recorded boundary, using a hostile Python object the builder cannot produce; that executed result supports, rather than contradicts, the docstring's explicit statement that arbitrary-hostile-input hardening is not established. No remaining defect blocks freezing this component. Filling remains blocked on the separately named cutout-integrity implementation, threshold/semantics/schema work, and transformed-cutout producer fixtures.

## Identity and executed comparison

- Subject: `../ref/bs2a_quality_gate.py`.
- Brief-pinned sha256: `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`.
- Independently computed before testing: `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`.
- Independently recomputed after the probes: `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`.
- **Comparison: MATCH.** The reviewed bytes are exactly the bytes pinned by the round-6 brief.
- `successor_ref_v9.py` sha256 before and after: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; size 110,996 bytes and mtime `1787747367` also stayed unchanged. `git status --short` reported no change for either reviewed path. The only occurrence of `successor_ref_v9.py` in the subject is the docstring statement at line 6; there is no import, open, or path use. Nothing in this review touched it.

## Required executions

1. `python3 ref/bs2a_quality_gate.py --self-test` (using the module's default authenticated `acquire/` fixture) exited 0. It printed:
   - authenticated receipt verifies clean;
   - every one of 26 checks is exercised by a control;
   - `self-test: 36 controls, 0 failure(s)`.
2. `python3 ref/bs2a_quality_gate.py --acquire acquire` from the successor-build root exited 0. It printed `n_parent=65060`, `n_joined=65060`, `n_retained=49211`, `n_excluded=15849`, evidence digest `0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca`, and `retained 49,211 of 65,060 (expected 49,211) — MATCH`.
3. I independently reran the existing no-module-import recomputation script. It found zero duplicate parent keys, zero duplicate quality keys, zero missing parent members, zero extra quality members, and reproduced the two source digests, 65,060 rows, 49,211 retained, the evidence digest, and the parent-keyset digest. Its terminal result was `ALL FIVE CONSTANTS MATCH SOURCE TEXT: True`.

## Numbered findings

### 1. INFORMATIONAL — both round-5 structural-use defects are closed, at the structural conditions

- File/lines: `../ref/bs2a_quality_gate.py:386-393` (E21/mistyped counts) and `:447-454` (E24/mistyped join keys).
- Executed repair checks:
  - `n_retained = "49211"` returns `{E21}` without reaching E18 arithmetic.
  - the shipped string-count control now expects and receives `{E21}`.
  - `brickid = []` returns `{E24}` without reaching E15 hashing.
  - the shipped unhashable-key control now expects and receives `{E24}`.
  - the real full self-test confirms the adjusted expectations while retaining coverage of E18 through `partition does not sum` and E15 through `duplicate evidence key`.
- Why it holds: each return is keyed to the independently computed structural condition (`if mistyped:` / `if mistyped_keys:`), not to the mutable `bad` list. Deleting the refusal call therefore does not turn the control into crash-only detection; the strict probe below confirmed this at source level.
- Smallest sufficient repair: none. The round-5 requested repair is present and behaviorally verified.

### 2. INFORMATIONAL — strict source-deletion probe: 26/26 named, 0 crash-only, 0 undetected

- File/lines under attack: all 26 unique `refuse("E01"...)` through `refuse("E26"...)` call sites in `verify_receipt`; probe: `gates/_tmp_gpt56_strict_probe_r6.py`.
- Method: for each code, a throwaway copy under `gates/_tmp_gpt56_strict_mutants_<pid>/` had that one real `refuse()` call replaced by a no-op; the mutant's real `self_test(acquire)` was executed. A deletion counted as detected only if a control whose declared expected set contains that code printed its own `FAIL <control-name>:` line. An exception was recorded as **CRASH-ONLY / NOT DETECTED**, never as success. Throwaway mutants were removed after the run; the reviewed source was never edited.
- Result: `SUMMARY total=26 named=26 crash_only=0 undetected=0`, exit 0. Every code had at least one named failing control. In particular, deleting E21 was named by the float, boolean, and string count controls; deleting E24 was named by the non-string and unhashable-key controls.
- Why it holds: the two new early returns are structural-condition keyed. Neither repair relies on the deleted refusal having populated `bad`.
- Smallest sufficient repair: none.

### 3. INFORMATIONAL — the robustness limit is honest; an arbitrary hostile Python object can still raise, exactly as disclaimed

- File/lines: module docstring `:45-69`; conversion boundary `verify_receipt()` at `:417-421`.
- Executed hostile-object attack: replaced one otherwise authentic evidence row's `flux_ivar_r` with a Python object whose `__float__` raises `RuntimeError("hostile __float__ reached")`. `verify_receipt()` raised that RuntimeError because its conversion handler intentionally catches ordinary conversion failures (`KeyError`, `TypeError`, `ValueError`, `OverflowError`), not arbitrary code execution from hostile Python objects.
- Why this does **not** fail the claimed contract: lines 57-69 explicitly say arbitrary-hostile-input hardening is **NOT established**, describe the boundary as receding, restrict in-study use to builder output, and require downstream fillers to repeat the limit rather than inherit the bare word “verified.” The demonstrated raise is therefore a confirmation that the disclaimer is substantive, not hidden overclaim.
- The word “verified” is sufficiently bounded: the positive property is separately headed `Sound against forgery — established`; the negative property is separately headed `Hardened against arbitrary hostile input — NOT established, and deliberately not claimed`; and the final sentence makes carrying that limit into any fill mandatory. A reasonable reader is not licensed by this text to inherit arbitrary-input hardening.
- Smallest sufficient repair: none for freezing. For a future untrusted-library use, add the validating wrapper the docstring already requires, with exact built-in container/field types and a top-level exception-to-refusal boundary.

### 4. INFORMATIONAL — “unreachable from the builder” is true for the verifier crash boundary

- File/lines: builder `:214-277`; builder-output claim in docstring `:63-69`.
- Executed over the actual authenticated build output, not sampled:
  - 65,060 evidence rows;
  - 0 off-schema rows;
  - 0 rows whose exact type is not `dict`;
  - 0 non-string `brickid`/`objid` values;
  - 0 non-float quality values;
  - 0 non-bool `quality_pass` flags;
  - `verify_receipt()` returned no refusal codes and did not raise.
- Source reasoning corroborates the execution: `_rows()` produces dict rows; `_key()` string-coerces and strips both join keys; `float(q[c])` constructs quality values; `quality_pass()` returns bool; receipt counts come from `len`/`sum`; and the fixed receipt fields are built from literals. Any different source bytes are rejected by the pinned digest before building.
- I also fuzzed 208 JSON-native substitutions across every receipt field and every field of one authentic evidence row (`null`, booleans, integers, float, strings, arrays, and objects): 0 crashes and 0 false accepts after excluding the one exact-value no-op. This is not a proof over all hostile Python values, but it supports the narrower builder/JSON-native claim.
- Smallest sufficient repair: none.

### 5. LOW advisory — an emit-destination failure can print MATCH before exiting non-zero; it still does not emit PASS or falsely accept a receipt

- File/lines: `main()` `:847-860`, especially MATCH printing at `:849-852` before the optional write at `:857-859`.
- Executed: `--acquire acquire --emit gates/_tmp_missing_dir_xyz/out.json` completed building and verifying the authentic receipt, printed the true `MATCH`, then raised `FileNotFoundError` while writing to a nonexistent directory and exited 1. Stdout contained no `PASS` token.
- Why it does not defeat this gate: the verified receipt was genuinely conforming; the later failure was output-destination I/O, not a verifier crash or false acceptance. The process exit is non-zero, so the operation fails closed for callers that honor process status. This does show why an integrator must never treat the informational word `MATCH` alone as the component's success signal.
- Smallest sufficient repair: optional hardening only—write the requested emission before printing the final summary, or catch emission errors and print an explicit `EMIT FAILED`; downstream callers must gate on exit status. This does not block freezing the predicate/verifier component.

## Can a verifier crash produce a false PASS?

No, for the attacked path. I monkeypatched `build_evidence()` in a throwaway driver to return the authentic receipt/evidence except for the hostile `FloatBomb` value, then invoked the real `main()`. The subprocess exited 1 with `RuntimeError: hostile __float__ reached from main`; stdout was empty and contained neither `PASS` nor `MATCH`. `main()` calls `verify_receipt()` before printing the receipt or summary, so an exception in verification prevents either from being emitted. The source has no successful uppercase `PASS` emission at all; its success indicators are exit 0 plus the informational `MATCH`. The separate post-verification emit-I/O case in finding 5 exits non-zero and prints only a factually correct MATCH for already-authenticated evidence.

## Failed attacks

The following attacks held (refused cleanly or failed closed; none accepted a forged receipt):

- All 36 shipped negative controls, including string count and unhashable join key.
- All 26 literal single-check source deletions under the strict named-control-only rule.
- 208 JSON-native field substitutions: 0 crashes and 0 false accepts.
- The round-5 crash shapes (`n_retained` string/null; `brickid`/`objid` array/object) now refuse at E21/E24 rather than raising.
- A foreign all-pass partition, forged parent member, duplicate evidence key, nested χ, non-finite values, non-bool pass flag, wrong source/parent digest, and malformed top-level containers were all re-exercised by the shipped control battery and produced their exact expected refusal-code sets.
- I did find the arbitrary-Python `__float__` raise, but it produced no acceptance and is inside the module's explicit NOT-established robustness limit.

## Freeze versus fill

**No remaining defect found here blocks FREEZING the quality-predicate component.** The predicate, authenticated evidence commitments, verifier, exact controls, builder boundary, and recorded robustness limitation are sufficiently pinned for the DESIGN slot.

This is **not** permission to FILL BS-2a. As the brief states, `verify_cutout_integrity` (Row C2), the confidence threshold, retry/failure semantics, the ledger schema, and §6.3(9)'s transformed-cutout adversarial producer fixtures are not built; those fixtures require cutouts. BS-2a remains DESIGN, UNFILLED. BS-6 and the first image byte remain blocked.

## Testimony and constraints

Executed in this session: subject and frozen-successor hashes; full source read; both round-5 reports read as prior findings to re-attack; real 36-control self-test; real acquire run; independent constant/source recomputation; strict 26-mutant source-deletion probe; complete builder-output type/schema census; 208-case JSON-native field fuzz; hostile-object raise; hostile-object-through-`main()` subprocess; emit-I/O crash subprocess; post-probe hashes, stat, source-reference search, and path-scoped git status.

Asserted from source reasoning rather than exhaustive execution: that no conceivable Python object can bypass or alter process semantics; arbitrary Python objects are explicitly outside the established boundary, and I demonstrated one raise rather than claiming universal hardening. I did not run all 325 pairwise deletions in round 6 because the brief specifically required the strict 26 single deletions and the source-level strict result closes the crash-credit defect; the prior pairwise result is not used as new testimony here. I did not read `/Users/duhokim/NebulaMindData/`, fetch any image byte, modify the reviewed subject, modify `acquire/`, or modify `successor_ref_v9.py`. Review artifacts and throwaway probes were confined to `gates/`; the required report is this file.

**CLEAR**