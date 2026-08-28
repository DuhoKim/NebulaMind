# BS-2a CODE GATE — GPT56, round 4

Verdict: **NOT CLEAR**. The pinned subject digest matches exactly. `--self-test` genuinely
passes (31 controls, 0 failures, 24/24 codes covered) and `--acquire` genuinely reproduces
49,211 of 65,060 with MATCH, both re-run for real in this session. All five frozen constants
were independently recomputed **without importing the module** and every one matched. I could
not make the verifier **accept** a receipt it should reject — every single-code and every
pairwise (all 276 combinations) deletion probe was caught, and every prior round's forgery
(forged parent key, foreign all-pass partition, χ nested in thresholds, float/bool counts,
lying `__eq__`, `OverflowError`) is refused as the round-3 repair claims. However, I **did**
succeed at the other half of the brief's challenge — **making it raise instead of refuse** —
via a defect the round-3 repair did not touch, in a different location from the one round 3
fixed. That is a live defect in the shipped file, not a hypothetical.

## Identity and executed comparison

- Subject: `../ref/bs2a_quality_gate.py`.
- Brief-pinned sha256: `e9d2ce3be96e481bf6433ac4736a13b0f8b870da3f40f0cb988d1bf559a1c3c8`.
- Independently computed sha256 before testing (`shasum -a 256`):
  `e9d2ce3be96e481bf6433ac4736a13b0f8b870da3f40f0cb988d1bf559a1c3c8`.
- Independently recomputed sha256 after all probes/attacks: same
  `e9d2ce3be96e481bf6433ac4736a13b0f8b870da3f40f0cb988d1bf559a1c3c8`.
- **Comparison: MATCH** — the reviewed bytes are exactly the brief-pinned subject, unchanged by
  this review (no probe ever wrote to the subject file; every mutation ran on in-memory copies
  under `_tmp_gpt56_r4/`, one real-file exception noted below and deleted after use).
- `python3 ref/bs2a_quality_gate.py --self-test` exited 0, printed `self-test: 31 controls, 0
  failure(s)` and `every one of 24 checks is exercised by a control`. Matches the brief's
  expectation exactly.
- `python3 ref/bs2a_quality_gate.py --acquire acquire` exited 0, printed `n_parent=65060,
  n_joined=65060, n_retained=49211, n_excluded=15849`, `evidence_sha256 =
  0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca`, and `retained 49,211 of
  65,060 (expected 49,211) — MATCH`. No `REFUSED` lines; exit 0.
- `successor_ref_v9.py`: grepped the subject for the string `successor_ref_v9` — one match, the
  docstring at line 6 (`` `successor_ref_v9.py` is FROZEN and this file does not touch it ``).
  No `import`, `open()`, or `Path(...)` construction referencing it anywhere. sha256 before and
  after this review: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`
  — unchanged.

## Recomputed frozen constants (no import of the subject)

A standalone script (`_tmp_gpt56_r4/recompute_constants.py`) re-implements the join, predicate,
and canonical digest encoding directly from the module's docstring (predicate thresholds,
lines 12-15) and reads `acquire/positions_selected.csv` / `acquire/quality_selected.csv`
directly with the stdlib `csv` module — it never `import`s or execs `bs2a_quality_gate.py`.

| constant | literal in file | independently recomputed | match |
|---|---|---|---|
| `PARENT_SHA256` | `425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831` | `shasum -a 256 acquire/positions_selected.csv` = same | MATCH |
| `QUALITY_SHA256` | `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3` | `shasum -a 256 acquire/quality_selected.csv` = same | MATCH |
| `EXPECTED_RETAINED` | `49_211` | independent join + predicate + count = `49211` | MATCH |
| `PARENT_KEYSET_SHA256` | `550e50a8c6fbea2a72ac93597b8c0fbc6798fc78172a5056f10329d7dde93bd6` | independently recomputed (own `_enc`/sorted-join reimplementation) = same | MATCH |
| `EVIDENCE_SHA256` | `0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca` | independently recomputed = same | MATCH |

All five are exactly what the sources produce. None is theatre; the trust root holds.

## Numbered findings

### 1. HIGH — an unhashable-but-JSON-legal join-key value crashes the verifier at the E15 uniqueness check instead of being refused

- File/lines: `../ref/bs2a_quality_gate.py:403-404`:
  ```python
  keys = [(e.get("brickid"), e.get("objid")) for e in evidence]
  if len(set(keys)) != len(keys):
  ```
- Executed attack: starting from the real authenticated fixture (`authenticated_fixture()`
  output — a genuine JSON-round-trippable receipt/evidence pair, not a Python-only
  construction), set a single evidence row's `brickid` to a JSON array, e.g.
  `ev[3]["brickid"] = ["x"]`, and call `verify_receipt(rec, ev)` with everything else
  untouched. Confirmed the mutated evidence is JSON round-trippable
  (`json.loads(json.dumps(ev))` succeeds — a hand-edited receipt JSON containing an array or
  object where a string key belongs is a realistic attacker input, not a synthetic
  Python-only edge case).
- Observed output:
  ```
  Traceback (most recent call last):
    File ".../bs2a_quality_gate.py", line 404, in verify_receipt
      if len(set(keys)) != len(keys):
  TypeError: unhashable type: 'list'
  ```
  Reproduced identically for `objid` (with `TypeError: unhashable type: 'dict'` when the value
  is a JSON object instead), for both fields independently, for multiple rows simultaneously,
  and for the degenerate case `brickid = []`.
- Why it fails: `E24`'s own check at lines 397-401 (`mistyped_keys = [... if type(e.get(k)) is
  not str ...]`) DOES correctly flag this row — `type(["x"]) is not str` is `True` — and
  `refuse("E24", ...)` fires. But `E24`'s check does not `return`; execution falls straight
  through to line 403, which builds a **raw, uncoerced** tuple `(e.get("brickid"),
  e.get("objid"))` for every row and immediately calls `set(keys)` on the whole list at line
  404. `set()` requires every element to be hashable; a JSON array (Python `list`) or JSON
  object (Python `dict`) as a field value is unhashable, so the interpreter raises `TypeError`
  before the function can return `bad`. This is exactly the same defect class the module's own
  docstring and round-3 comments warn about — `"a verifier that raises has not refused"` — but
  in a **different location** from the one round 3 actually closed. Round 3 closed the
  raise-on-missing-key/non-dict-row path at `evidence_digest()` (guarded by the `off_schema`
  early return at line 361) and the type-coercion path inside `_enc()`/`evidence_digest()`'s
  `num()` (which safely uses `.get()` plus a caught-exception sentinel, confirmed still true
  below). Neither guard reaches line 403-404: `off_schema` only catches **extra/missing
  fields** or a non-dict row (`set(e) != set(EVIDENCE_FIELDS)`), not a **wrong-typed value on a
  present field** — a row with exactly the six required keys, one of which holds a list, passes
  `off_schema` cleanly (`set(e) == set(EVIDENCE_FIELDS)` is still `True`) and is never returned
  on. `evidence_digest()`/`keyset_digest()` are separately safe here (confirmed: both compute
  a digest without raising on the same mutated row, because `_enc()` coerces every value through
  `str()` before use) — the crash is specific to line 403's construction of raw, uncoerced
  tuples for the `E15` uniqueness check, which has no equivalent coercion.
- Contrast case confirming the defect is about **hashability**, not non-string-ness in general:
  a hashable non-string key (Python `tuple`, e.g. `ev[3]["brickid"] = (1, 2)`) does **not**
  crash — it is cleanly refused `{'E19', 'E20', 'E23', 'E24'}`. The module's own existing
  `non-string join key` control (`_c_nonstring_key`) uses `12345` (an `int`), which is hashable
  and therefore never exercises this code path — the control's own choice of attack value is
  why round 3's battery, which passes 31/31, never caught this. It is a gap in control
  coverage, not merely a code gap: the existing `E24` control tests type-wrongness but not
  hashability-wrongness, and those are different failure classes at line 403-404.
- Smallest sufficient repair: replace the raw tuple construction at line 403 with the same
  coercion pattern the module already applies elsewhere (`_enc()`'s `map(str, parts)`, or
  `mistyped_keys`'s own `type(...) is not str` result): either (a) skip the `E15` check
  entirely when `mistyped_keys` is non-empty (mirroring the `off_schema`/`missing or extra`
  early-return pattern — a row already known to carry the wrong type for its join key cannot
  be trusted to build a well-formed key tuple), or (b) build `keys` from
  `str(e.get("brickid"))`/`str(e.get("objid"))` the same way `keyset_digest()` already does at
  line 284 (`_enc(str(e.get("brickid")), str(e.get("objid"))) for e in evidence`), which is
  string-safe and therefore always hashable. Add an isolated control: `brickid` (or `objid`)
  set to a JSON array/object, on an otherwise-authenticated evidence set, asserting the exact
  code set `{E24}` (or whatever the repair settles on) rather than a crash.

### 2. Everything round 3 claimed to fix, verified fixed

- **`del ev[0]["flux_ivar_r"]` no longer raises.** `verify_receipt()` returns `{E09}` cleanly —
  reproduced for all six evidence-row schema fields individually, and for four non-dict row
  types (`None`, a string, a list, an int).
- **`isinstance(e, dict)` short-circuits before `set(e)`.** `ev[0] = None`, `ev[0] = "string"`,
  `ev[0] = 42` all refuse `{E09}` cleanly, no crash.
- **The encoder is guarded.** `evidence_digest()`'s `enc()`/`num()` uses `.get()` plus a
  `try/except (TypeError, ValueError, OverflowError)` sentinel — confirmed directly:
  `evidence_digest()` and `keyset_digest()` do NOT raise on the same unhashable-list-brickid
  row that crashes `E15` (see finding 1) — proving the encoder's guard is real and specific to
  that function, not a blanket fix. `EVIDENCE_SHA256` and `PARENT_KEYSET_SHA256` both still
  reproduce exactly against the unmodified fixture (see constants table above); no digest of
  well-formed evidence changed.
- **`OverflowError` is caught.** `ev[0]["flux_ivar_r"] = 10**400` refuses `{E10, E19, E23}`, no
  crash — reproduced.
- **Lying `__eq__` no longer buys an ACCEPT.** `_LiarEq()` in `schema_version` refuses `{E03}`;
  in `thresholds["psfsize_r_lt"]` refuses `{E07}`; in `evidence_sha256` refuses `{E19}` —
  reproduced for all three, via both the module's own controls and independent direct
  construction.
- **31 controls, 0 failures, 24/24 codes covered** — reproduced exactly via `--self-test`.

### 3. Short-circuit laundering check: the `off_schema` early return does not hide an accept, and does not suppress checks ABOVE E09

- Constructed a receipt whose only defects are (a) an off-schema row (`E09`-triggering) and
  (b) a second, independent defect that lives structurally BELOW E09 in the function body
  (duplicate evidence key, `E15`-class; wrong `evidence_sha256`, `E19`-class; wrong
  `n_retained`, `E16`/`E22`-class). In every combination tried, the result was exactly `{E09}`
  — never an accept, never a code from below E09 leaking through, and never a raise. This
  confirms the early return at line 361 does exactly what its comment claims: it returns
  `bad` (non-empty, since `E09` was just appended) before reaching any check that assumes
  well-formed rows — it does not launder an ACCEPT.
- Constructed a receipt combining an off-schema row (E09, below-the-line check) WITH an
  independently forged `parent_source_sha256` (E05, a check that runs BEFORE `off_schema` at
  line 318, well above the `missing or extra` early return's target and above the off_schema
  check itself). Result: `{'E05', 'E09'}` — both codes present, confirming the E09 early
  return does not retroactively suppress checks that already ran and populated `bad` before
  it — only checks below the return point are skipped, exactly as designed.
- `row missing a key` and `row is not a dict` isolation (brief's question 4): both re-verified
  to expect **exactly** `{E09}` — no other code creeps in, none is missing. Confirmed by direct
  construction matching the module's own `_c_missing_row_key`/`_c_nondict_row` mutators.

### 4. Deletion-probe results (exhaustive, this session, independently re-derived methodology)

Method: build the real authenticated fixture once, run each of the 31 controls exactly once
against the unmodified subject to record its true output (all 31 matched their declared
expected code set with 0 unexpected raises — a direct cross-check against `--self-test`'s own
31/0 result). Then, for every candidate set of codes to "delete" (all 24 singles, all 276
pairs), simulate the deletion by removing those codes from each control's *already-observed*
result and comparing against the control's fixed declared expected set — this is the same
check `self_test()` itself performs (`got == expect`), so a deletion is CAUGHT iff at least one
control's simulated post-deletion result differs from its declared expected set.

**Method validated against a REAL deletion**, not just simulated: physically deleted the `E13`
`refuse()` call from a scratch copy of the subject (`n_parent` identity check) and re-ran
`--self-test` for real. Output: `self-test: 31 controls, 1 failure(s)`, with `FAIL parent
identity wrong: expected ['E13', 'E14'], got ['E14'] — missing ['E13'], spurious []` — exactly
matching what my simulation predicts for dropping `{E13}`. The scratch copy was deleted
immediately after this one validation run; the reviewed subject file was never touched (its
sha256 is confirmed unchanged in the Identity section above).

- **Single-code deletion, all 24 codes**: **all 24 caught.** No silent code.
- **Pairwise deletion, all 276 combinations of 2 codes out of 24**: **all 276 caught.** No
  silent pair. (Completed in under a second using the observed-once-then-simulate method,
  cross-validated against one real deletion as above; this reproduces round 3's 683-second
  exhaustive result via a faster but methodologically equivalent approach.)

This directly answers the brief's question 2/4: I found no control passing for the wrong
reason, and no pairwise combination that survives silently.

## Other failed attacks (accept-a-bad-receipt angle, all refused correctly)

- Threshold round-tripped through `struct.pack`/`struct.unpack('d', ...)` (bit-identical float,
  testing IEEE754 edge tolerance): value remains bit-identical, so this is expected to be
  accepted on that axis alone — not a finding, confirms no false-positive rejection either.
- `schema_version`/`n_parent`/`thresholds`/`join_keys` as **subclasses** (`str`, `int`, `dict`,
  `list` subclasses respectively) carrying the otherwise-correct value: all refused with their
  normal codes (`E03`, `E21`, `E06`, `E08`) — confirms every `type(x) is not T` check is
  genuinely exact-type, not `isinstance`-style, and a subclass cannot sneak past by duck-typing.
- `evidence_sha256` as `bytes` (not `str`) with the correct hex value encoded: refused `E19` —
  `type(...) is not str` correctly rejects it.
- Threshold value as `decimal.Decimal`: refused `E07` — `type(t[name]) not in (int, float)`
  correctly rejects it.
- Two rows' `(brickid, objid)` swapped (key set unchanged, but quality-value binding to the
  wrong key): refused `E23` — the frozen full-evidence digest catches value-binding forgeries
  that a membership-only check would miss.
- Embedded `\n` (the digest's row-join separator) inside a `brickid` value: refused
  `{E20, E23}` — the `\n`.join(sorted(...)) construction is not confused by a value containing
  the separator, because `_enc()`'s length-prefix scheme still round-trips the value uniquely
  and the resulting row differs from every genuine row.
- Case/suffix perturbation of a genuine `brickid`, empty-string `brickid`: both refused
  `{E20, E23}`.
- Exact duplicate row appended (counts and digest honestly recomputed): refused
  `{E14, E15, E20, E23}` — no silent dedup in the digest construction.
- Unicode combining-character variant of a genuine `brickid`: refused `{E20, E23}`.
- `n_parent = NaN` (float), `n_parent` with a raising custom `__lt__`, `n_parent = True`: all
  refused via `E21`'s `type(receipt[f]) is not int` gate, which short-circuits before any
  comparison that could raise — confirmed no crash on any of these.
- `quality_pass = None` (JSON null): refused `{'E11', 'E16', 'E19', 'E23'}` cleanly — contrast
  case showing `None` (falsy, not raising) does not hit the same class of bug as an unhashable
  value; this is the correct, intended refusal path.

## Other failed raise attempts (angles tried beyond finding 1)

- Circular self-referential dict as a field value, complex numbers, deeply nested dict
  (recursion-depth bait) as `flux_ivar_r`: all refused cleanly `{'E10', 'E19', 'E23'}` — the
  per-row `float(e[...])` cast's `except (KeyError, TypeError, ValueError, OverflowError)`
  tuple, and `evidence_digest()`'s equivalent `num()` guard, both handle these without raising.
- A self-referential extra key inside `thresholds` (`thresholds["self"] = thresholds`):
  refused `E06` cleanly (extra key detected by the exact-set check, no infinite recursion since
  the check is a `set()` comparison, not a deep walk).
- A `join_keys` list containing a nested list element: refused `E08` cleanly.
- Custom classes with raising `__str__`, `__bool__`, `__iter__`, or a hostile `dict` subclass
  overriding `__iter__`: these DO raise (as expected — such objects cannot appear in
  JSON-round-tripped input at all, so they are outside the realistic-attacker-input threat
  model the brief and the module's own docstring implicitly use; recorded for completeness,
  not counted as a finding, since a hand-edited JSON receipt can never produce a Python object
  with a raising dunder method — only finding 1's list/dict values are both realistic JSON
  input AND crash a genuinely reachable code path).

## Claim-boundary review

Re-read the module docstring's claims (lines 21-44) against the code. The module states the
predicate is outcome-blind with respect to this study's unobserved χ, explicitly disclaims
statistical independence from handedness, states the handedness-conditional-on-position
question is "not established," and says `E23` matching is "custody, not science." Grepped the
whole file for `chi`, `handedness`, `independent`, `custody`, `science` — every occurrence
outside the docstring is either a control name/comment referencing the round-2 `chi_net` attack
or the `order-independent by construction` comment about the digest's row-order invariance
(an unrelated, accurate claim about hash construction, not about the science). I found no
executable path, comment, or variable name anywhere in the file that asserts or implies
anything stronger than the docstring's disclaimers.

## Testimony and constraints

The following is asserted from direct code reading rather than an executed reproduction,
disclosed per the brief's instruction:

- `main()`'s `if bad: return 1` producing a nonzero exit on a genuine `MISMATCH` — read from
  the source at lines 764-770, not exercised end-to-end against a real mismatching dataset,
  since doing so would require corrupting the frozen `acquire/` CSVs (outside scope; the brief
  forbids reading `/Users/duhokim/NebulaMindData/` and instructs not to modify reviewed
  sources). The underlying mechanism (`E22` firing whenever `n_retained != EXPECTED_RETAINED`,
  and `bad`'s truthiness gating `main()`'s return) was verified directly via `verify_receipt()`
  calls on forged receipts with mismatching `n_retained` (e.g. the "foreign all-pass partition"
  control), which is the same code path `main()` exercises.

Everything else in this report was executed in this session: the digest verification (before
and after all probes), the self-test run, the `--acquire` run, the independent constant
recomputation via a script that does not import the subject, the exhaustive single- and
pairwise-code deletion sweep (300 total combinations, cross-validated against one real physical
deletion in a disposable scratch copy), the short-circuit laundering checks, the isolation
checks for the two named controls, the raise-vs-refuse attack that succeeded (finding 1,
reproduced for both `brickid` and `objid`, multiple rows, and the degenerate empty-array case),
roughly twenty other raise attempts that failed to reproduce a crash, roughly fifteen other
accept-bad-receipt attempts that were all correctly refused, the claim-boundary grep, and the
`successor_ref_v9.py` untouched check. I did not read `/Users/duhokim/NebulaMindData/`, did not
fetch an image byte, did not emit an acquisition artifact via `--emit`, and did not modify the
reviewed subject (its sha256 is confirmed identical before and after this entire session). One
disposable scratch file (`_tmp_gpt56_r4/real_deletion_test.py`, a temporary copy of the subject
with `E13`'s `refuse()` call physically deleted) was created solely to validate the deletion-probe
simulation methodology against ground truth, and was deleted immediately after that one
validation run — it never touched the reviewed subject at `../ref/bs2a_quality_gate.py`. This
review does not fill BS-2a, authorise a fetch, or resolve conditional independence. BS-2a
remains UNFILLED; one of fifteen class-P slots is filled; BS-6 and the first image byte remain
blocked.

## Addendum: a concurrent process changed the subject file during this session, and the report below now covers a superseded prior round's bytes

While preparing this report, `ps aux` revealed multiple concurrently-running `hermes -z` seat
processes in this same directory: a duplicate GPT56 round-4 process (started 19:53:29, same
brief file `BRIEF_BS2A_CODE_GATE_R4.md`, same pinned digest `e9d2ce3b...`), plus a **CODEX
round-5** and a second **GPT56 round-5** process (both started 20:17:xx, targeting
`BRIEF_BS2A_CODE_GATE_R5.md` against a NEW pinned digest `aa03d1f9...`). `git log` on the
subject path shows a commit `a03bdd5d3` landed at **20:17:39 KST**, titled *"guard the
containers, and key their early return off the structure not the refusal list"* — this fixes a
**different** raise-vs-refuse defect (CODEX's own round-4 finding: `type(receipt) is dict` /
`type(evidence) is list` were never checked, so a JSON-null receipt or a JSON-object evidence
slot crashed `set(receipt)`/`enumerate(evidence)` before any refusal could fire; the commit
adds `E25`/`E26` and a structural early return). The commit message explicitly acknowledges the
same-filename overwrite race this round's own brief opens with ("You made it raise. That path
is closed.") and states report filenames are moving to a `_R<N>` suffix specifically because
"GPT56's round-4 seat was still running when round 5 was dispatched."

**This means**: the file at `../ref/bs2a_quality_gate.py` I hashed, self-tested, and attacked
throughout this entire session — verified sha256 `e9d2ce3be96e481bf6433ac4736a13b0f8b870da3f40f0cb988d1bf559a1c3c8`
at both the start and immediately after all probes, matching the digest this round's brief
pins — **is no longer the current bytes on disk**. The file now hashes to
`aa03d1f96f47742b1cd4863b4f0e5ebbeeac66dba787b83175d9b95f702c509f` (the round-5-pinned digest),
because a separate process committed a fix for an unrelated defect while I was writing this
report. My review is complete and correct **for the round-4-pinned digest this brief names**,
and every execution and probe result reported above is real and was captured against exactly
that pinned digest — I did not silently re-target a moving file.

**Critically, I re-ran the specific attack from finding 1 against the CURRENT (post-fix,
round-5-pinned) bytes before closing this report**, to check whether the unrelated fix
incidentally also closed my defect:

```
ev[3]["brickid"] = ["x"]  (unhashable JSON array, same attack as finding 1)
  -> TypeError: unhashable type: 'list'
     File "ref/bs2a_quality_gate.py", line 425, in verify_receipt
         if len(set(keys)) != len(keys):
```

**It does not.** The line number shifted from 404 to 425 (the new `E25`/`E26` container guard
added ~21 lines above it), but the E15 uniqueness-check crash in finding 1 is untouched by the
round-4/5 fix and still reproduces identically on the current bytes. This is independent
confirmation that finding 1 is a real, distinct defect from the one round 5 was dispatched to
address — it survived a fix cycle aimed at a different bug in the same neighborhood of the
function, which is exactly the failure mode the brief's own framing warns about ("Round 4:
You made it raise. That path is closed" — evidently not fully, one level further out).

I am reporting this honestly rather than silently treating my review as covering current bytes,
per the brief's own standard that a refusal you can demonstrate beats a pass you can argue, and
per the same transparency CODEX's round-3 report modeled when it disclosed an identical
same-filename race. **This round's verdict below is for the round-4-pinned digest
(`e9d2ce3b...`), which is what this brief (`BRIEF_BS2A_CODE_GATE_R4.md`) asked me to review and
which I verified matched before, during, and immediately after every probe in this session.**
Whoever dispatches round 6 should know finding 1's underlying bug class (a check that flags a
row without returning, followed by unguarded container construction from the flagged value)
is still present in the round-5-pinned bytes at the new line 425, one level removed from where
round 5's fix looked.

## Verdict rationale

Round 3 closed the specific raise-vs-refuse defect the brief named (`del ev[0]["flux_ivar_r"]`)
by adding a structural early return keyed off the `off_schema` condition. That fix is real and
holds under attack — confirmed above. But the same underlying failure mode — a check whose
`refuse()` call does not `return`, followed downstream by code that assumes the offending value
is well-formed enough to be hashed — was never eliminated as a *class*; it was patched at one
location and left live at another. `E24`'s check (line 397-401) flags a wrong-typed join key
but does not `return`, and the very next lines (403-404) build a raw tuple from that same
untrusted value and hash it. A JSON array or JSON object in a `brickid`/`objid` field —
completely realistic hand-edited-receipt input — reaches that line and crashes the process
instead of being refused. Per the brief's own standard: **"A verifier that raises has not
refused."** This is a live, reproducible defect in the exact bytes pinned by this round's
brief.

**NOT CLEAR**
