# BS-2a CODE GATE — GPT56, round 5

Verdict: **NOT CLEAR**. The pinned subject digest matches exactly. `--self-test` genuinely
passes (34 controls, 0 failures, 26/26 codes covered — matching the brief's claim to the digit)
and `--acquire` genuinely reproduces 49,211 of 65,060 with MATCH, both re-run independently in
this session. Round 4's finding — malformed top-level `receipt`/`evidence` containers crashing
instead of refusing — is confirmed repaired: `E25`/`E26` now catch every container-shape attack I
could construct, including the round-5 brief's own disclosed near-miss (`evidence={"a":1}`), and
the short-circuit does not launder a second, lower-priority fault (tested both directions). All
276 single-pair and all 325 pairwise deletion combinations over the current 26-code, 34-control
battery are caught — the battery's own internal claims about itself hold. **But I did make the
verifier raise instead of refuse, twice, on fully JSON-native input that clears the E25/E26
container gate and is exactly the shape `verify_receipt`'s own design principle exists to
handle.** Both are new to this round; neither is the E25/E26 class the brief already knows about
— they are one level *further in*: past the container gate, inside individual field values that
the E21/E24 field-shape checks flag but do not structurally return on, the same coupling this
module has fixed twice already for different fields.

## Identity and executed comparison

- Subject: `../ref/bs2a_quality_gate.py`.
- Brief-pinned sha256: `aa03d1f96f47742b1cd4863b4f0e5ebbeeac66dba787b83175d9b95f702c509f`.
- Independently computed sha256 before testing (`sha256sum`):
  `aa03d1f96f47742b1cd4863b4f0e5ebbeeac66dba787b83175d9b95f702c509f`.
- Independently recomputed sha256 after all probes (this review never edits the reviewed
  subject): `aa03d1f96f47742b1cd4863b4f0e5ebbeeac66dba787b83175d9b95f702c509f`.
- **Comparison: MATCH** — the reviewed bytes are exactly the brief-pinned subject at the sha256
  identity level, before and after this review.
- `python3 ref/bs2a_quality_gate.py --self-test --acquire acquire` exited 0 and printed
  `self-test: 34 controls, 0 failure(s)` and `every one of 26 checks is exercised by a control`
  (full per-control OK listing captured in this session's tool output).
- `python3 ref/bs2a_quality_gate.py --acquire acquire` exited 0, printed `n_parent=65060`,
  `n_joined=65060`, `n_retained=49211`, `n_excluded=15849`,
  `evidence_sha256=0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca`, and
  `retained 49,211 of 65,060 (expected 49,211) — MATCH`.
- `successor_ref_v9.py` sha256, before and after this review:
  `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` — unchanged. Grepped the
  subject for `successor_ref_v9`: one match, the docstring line 6 ("`successor_ref_v9.py` is
  FROZEN and this file does not touch it"). Not imported, not opened, not executed anywhere in
  the file — confirmed by reading every line, not just grepping the name.

## Recomputed frozen constants (without importing the module)

All five recomputed via `gates/_tmp_bs2a_r5_recompute_constants.py`, written fresh this round. It
does **not** `import bs2a_quality_gate`; it re-implements the join/predicate/digest logic
directly from the module's own docstring prose (read and hand-verified against the source, not
copy-pasted from it) and reads `acquire/positions_selected.csv` / `acquire/quality_selected.csv`
directly, then string-matches the recomputed literals against the subject file's own source
*text* (a grep, not an import) so nothing here trusts the module's own arithmetic:

| constant | literal in file | independently recomputed | match |
|---|---|---|---|
| `PARENT_SHA256` (source pin) | `425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831` | same, via direct file hash | MATCH |
| `QUALITY_SHA256` (source pin) | `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3` | same, via direct file hash | MATCH |
| `PARENT_ROWS` / `EXPECTED_RETAINED` | `65_060` rows, `49_211` retained | independent join (0 duplicate parent keys, 0 duplicate quality keys, 0 parent objects missing a quality row, 0 orphaned quality rows) + predicate applied per-row = `65060` / `49211` | MATCH |
| `PARENT_KEYSET_SHA256` | `550e50a8c6fbea2a72ac93597b8c0fbc6798fc78172a5056f10329d7dde93bd6` | independently recomputed = same | MATCH |
| `EVIDENCE_SHA256` | `0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca` | independently recomputed = same | MATCH |

Script output: `ALL FIVE CONSTANTS MATCH SOURCE TEXT: True`. The trust root holds — none of the
five is theatre, and the join is genuinely one-to-one and total over the parent (independently
verified, not assumed from the module's own `build_evidence` behavior).

## Numbered findings

### 1. HIGH — `n_retained + n_excluded` (E18) does raw arithmetic on values E21 has already flagged as mistyped, crashing instead of refusing, via fully JSON-native input

- File/line: `../ref/bs2a_quality_gate.py:435`
  (`if receipt["n_retained"] + receipt["n_excluded"] != receipt["n_joined"]:`).
- `E21` (line 360-364) checks every `COUNT_FIELDS` member (`n_parent`, `n_joined`, `n_retained`,
  `n_excluded`) for `type(x) is not int or x < 0` and appends a refusal — but it does **not**
  return, and nothing below it re-checks the type before using the value arithmetically. Line 435
  is 75 lines later, well past the point where the module's own established pattern says a
  structural condition should gate further use ("A verifier that raises has not refused" appears
  three times in this file's own comments, at lines 259, 314-318, and 377-381 — this is the same
  defect class, one level further into the field values than the container-level fix this round's
  brief describes).
- Executed attacks, all against the real authenticated fixture with only the named field
  substituted, all reachable by a `json.loads(...)["receipt"]["n_retained"] = None` edit to an
  otherwise-well-formed JSON document — i.e. inside the module's own stated threat model (a
  hand-made receipt):
  ```
  n_retained = None   (JSON null)   → RAISED TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
  n_excluded = None   (JSON null)   → RAISED TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
  n_retained = "49211" (JSON string) → RAISED TypeError: can only concatenate str (not "int") to str
  ```
  Full traceback for the first:
  ```
  File ".../bs2a_quality_gate.py", line 435, in verify_receipt
      if receipt["n_retained"] + receipt["n_excluded"] != receipt["n_joined"]:
  TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
  ```
- Contrast, to show the crash is genuinely field-specific and not a general property of `E21`
  catching something: `n_joined = None` and `n_parent = None` do **not** crash — they refuse
  cleanly (`{E14, E17, E18, E21}` and `{E13, E14, E21}` respectively), because neither
  `n_joined` nor `n_parent` is ever used in arithmetic below the `E21` check — only compared with
  `!=`, `<`, or used as a `len()` operand elsewhere, none of which raise on `None`/`str` against
  an `int`. `n_retained` and `n_excluded` are the only two `COUNT_FIELDS` that are ever added
  together, and that is exactly where the type gate's non-return matters.
- The 34-control battery does not exercise this: the two existing count-field-type controls
  (`float count fields`, `boolean count field`) both substitute types that Python's `+` operator
  handles without raising (`float + int` and `bool + int` are both legal arithmetic, since `bool`
  is an `int` subclass) — so this specific arithmetic-crash shape was never constructed, only
  types that happen to survive `+`.
- Why it matters: this is not a new class of defect — it is the same "type-check without
  structural return" shape the module has already fixed twice, once for evidence-row containers
  and once (this round) for receipt/evidence top-level containers — surfacing again one level
  deeper, inside a single field's arithmetic use, in a way the current fix pattern did not
  anticipate because `E21` accumulates into `bad` rather than returning.
- Smallest sufficient repair: either (a) make `E21` return immediately when `mistyped` is
  non-empty (before line 366), mirroring the structural-return pattern already used for `E25/E26`
  and `E01/E02`; or (b) guard line 435 specifically with a type check before the `+`
  (`if type(receipt["n_retained"]) is int and type(receipt["n_excluded"]) is int and
  receipt["n_retained"] + receipt["n_excluded"] != receipt["n_joined"]: refuse("E18", ...)`).
  Option (a) is smaller and closes the same hole for any future arithmetic added on count fields;
  it costs re-verifying that no currently-passing control (e.g. `boolean count field`, which
  expects `{E18, E21}` together) still gets its full expected set — `E21` returning early would
  turn that control's expectation into `{E21}` alone, so the control table needs a one-line
  update alongside the fix, not just the fix.

### 2. HIGH — a non-hashable join-key value (JSON array or object as `brickid`/`objid`) crashes the duplicate-key check (E15) via `set(keys)`, past the E24 field-type gate

- File/line: `../ref/bs2a_quality_gate.py:424-425`
  (`keys = [(e.get("brickid"), e.get("objid")) for e in evidence]` /
  `if len(set(keys)) != len(keys):`).
- `E24` (line 418-422) checks `type(e.get("brickid")) is not str or type(e.get("objid")) is not
  str` per row and refuses if any join key is non-string — but again does not return. Two lines
  later, `E15`'s `set(keys)` call attempts to hash every `(brickid, objid)` tuple, and a tuple
  containing an unhashable element (a `list` or `dict`, both directly JSON-representable as a
  `brickid` value) makes the *tuple itself* unhashable, raising before `E15` can record its
  refusal.
- Executed attacks, all against the real authenticated fixture with only row 0's `brickid`
  substituted, all directly JSON-native (`"brickid": [1,2,3]` and `"brickid": {"a":1}` are both
  legal JSON):
  ```
  brickid = [1, 2, 3]   (JSON array)   → RAISED TypeError: unhashable type: 'list'
  brickid = {"a": 1}    (JSON object)  → RAISED TypeError: unhashable type: 'dict'
  objid   = [1, 2]      (JSON array)   → RAISED TypeError: unhashable type: 'list'
  ```
  Full traceback for the first:
  ```
  File ".../bs2a_quality_gate.py", line 425, in verify_receipt
      if len(set(keys)) != len(keys):
  TypeError: unhashable type: 'list'
  ```
- Contrast, to isolate the defect: `brickid = 12345` (a plain `int`, hashable, non-string) does
  **not** crash — it refuses cleanly `{E19, E20, E23, E24}`, because `E24`'s own check
  (`type(...) is not str`) fires and every downstream digest/keyset check independently
  disagrees. Only *unhashable* non-string types reach the crash; the existing
  `non-string join key` control (`_c_nonstring_key`, using `int`) tests a hashable non-string and
  cannot see this.
- Why it matters: identical shape to finding 1 — a field-level type gate (`E24`) that flags but
  does not structurally return, followed by code that assumes the flagged value is safe to use
  (here, hashable) rather than merely present. `E19`/`E20`/`E23` (the digest/keyset checks) also
  run over `evidence` and would independently catch a forged unhashable key via `_enc`'s
  `str(parts)` coercion (which the docstring at line 258-261 explicitly says exists so a
  non-string join key "digests instead of raising") — but `E15` at line 425 runs *before* those
  and is not similarly defended, so it crashes first.
- Smallest sufficient repair: either (a) make `E24` return immediately when `mistyped_keys` is
  non-empty (before the `keys = [...]` / `set(keys)` block at 424-425), matching the same
  structural-return pattern; or (b) build `keys` using the same `str()`-coercion `_enc` already
  uses for exactly this reason (e.g. `keys = [(str(e.get("brickid")), str(e.get("objid"))) for e
  in evidence]`), which makes `E15`'s uniqueness check well-defined for any JSON-native value
  without needing E24 to gate it. Option (b) is smaller, requires no control-table renumbering
  (E15's expected set is unaffected by non-string-but-stringifiable keys), and mirrors the
  digest functions' own existing defense.

### 3. Everything round 4 claimed to fix, verified fixed — including this round's own disclosed near-miss and one launder check the brief specifically asked for

- **Round 4's container-type defect is closed.** `receipt=None`, `receipt=42`, `evidence=None`,
  `evidence=42`, `evidence=True` — all refuse cleanly (`{E25}` or `{E26}`), no exception,
  reproduced directly this round.
- **This round's own disclosed near-miss (`evidence={"a":1}`) is genuinely fixed, not merely
  claimed.** `off_schema` no longer runs at all for a non-list `evidence` — `E26` catches the
  type before `enumerate(evidence)` is ever reached, confirmed by reading the code (line
  313-314) and by direct execution: `evidence={"a":1}` refuses `{E26}` cleanly.
- **The E25/E26 short-circuit does not launder a second, lower-priority fault** — this round's
  brief's question 2, tested in both directions this round:
  - `receipt=None` + evidence independently carrying a forged parent key (would be `{E20,E23}` if
    reached) → refused `{E25}` only.
  - `evidence=42` + receipt independently carrying a bad threshold (would be `{E07}` if reached)
    → refused `{E26}` only.
  - `evidence={"a":1}` (the sharp near-miss case) + receipt independently carrying a bad
    `schema_version` (would be `{E03}` if reached) → refused `{E26}` only.
  In every case the container gate alone is a true and sufficient refusal — the receipt IS
  rejected — and the second, unreported defect can never reach ACCEPT because the container
  check already blocks it. Not laundering.
- **The self-repair the brief disclosed (structural return keyed on the condition, not on
  `bad`) is present and correct at both sites**: line 319 (`if not (receipt_ok and
  evidence_ok): return bad`) and line 332 (`if missing or extra: return bad`) — both key off the
  boolean structural flags, not off whether `bad` is non-empty, so deleting `E25`/`E26`/`E01`/
  `E02` cannot reintroduce the fall-through-to-traceback shape the brief's own dispatch note
  describes finding and fixing pre-round.
- **34 controls, 0 failures, 26/26 codes covered** — confirmed by direct execution, not asserted
  (full listing captured this session).

## Deletion-probe results (exhaustive, this session, against the current 34-control, 26-code battery)

Methodology: for every control, compared its real executed refusal-code set against its declared
`expect` set — 0 mismatches (the battery's own claims about itself hold). Then, for every
candidate deletion set (single code, and every pairwise combination), computed whether *any*
control's `(real_codes − deleted) != expect` — i.e. whether any control's observable behavior
changes when the named code(s) are removed from what `verify_receipt` would produce. This is
equivalent to actually deleting the corresponding `refuse()` call(s), since nothing in the
function branches on the *contents* of `bad`, only on the structural conditions (verified by
reading the source: the only early returns are keyed on `receipt_ok`/`evidence_ok` and
`missing`/`extra`/`off_schema`, none of which depend on which codes have been appended).

- **Single-code deletion, all 26 codes**: **all 26 caught.** No silent deletions.
- **Pairwise deletion, all 325 combinations of 2 codes out of 26** (C(26,2) = 325 — the brief's
  own text says "276 pairwise" from round 4's 24-code battery; round 5's battery has grown to 26
  codes since round 4 added `E25`/`E26`, so the correct exhaustive count this round is 325, and
  I ran all 325, not 276): **all 325 caught.** No orphans.
- Sanity check first: all 34 controls' real, undeleted code sets matched their declared `expect`
  sets exactly (0 mismatches) before any deletion was simulated — the `CONTROLS` table's own
  expectations are internally correct.

This directly answers the brief's question 2 in a different guise from finding 3's launder check:
"does the new early return hide anything." No control in the current battery, real or deleted,
ever depends on the container guard hiding a second fault — the deletion sweep and the launder
check are consistent with each other and with an internally sound battery.

## Failed attacks (false-accept battery, this round's untried angles)

All of the following were tried and refused (not accepted, not silently laundered):

- `n_retained = IntEnum(49211)` (numerically equal, correct value, wrong exact type) — refused
  `{E21}` (`type(x) is not int` catches any subclass, including `IntEnum`, regardless of value).
- `n_retained = HonestIntSub(49211)` (a plain `int` subclass, correct value, supports `+` and
  comparison normally) — refused `{E21}` for the same reason. Noted as a minor behavioral
  observation, not a security gap: the type gate is *stricter* than strictly necessary (it would
  reject a legitimately-typed `int` subclass too), consistent with what round 4 already noted for
  a different `int`-subclass case.
- `psfsize_r_lt = Decimal("1.5699703")` (numerically equal to the frozen threshold, wrong exact
  type) — refused `{E07}` (`type(t[name]) not in (int, float)` excludes `Decimal`).
- `n_retained += 2, n_joined += 2` (inflate both together, attempting to keep `E14`/`E17`/`E18`
  internally consistent while still claiming a wrong retained count) — refused
  `{E14, E16, E17, E22}`: `n_joined` no longer matches `n_parent` (`E14`), no longer matches
  `len(evidence)` (`E17`), the recount from evidence disagrees with the inflated claim (`E16`),
  and the frozen `EXPECTED_RETAINED` pin catches the inflated value regardless (`E22`). Inflating
  `n_joined` cannot make the evidence list itself longer, so this attack cannot ever succeed
  against a receipt bound to real evidence.
- A wholly empty evidence list with a wholly zeroed, internally self-consistent receipt
  (`n_parent=n_joined=n_retained=n_excluded=0`, digest recomputed over the empty set) — refused
  `{E13, E20, E22, E23}`: the frozen parent cardinality (`E13`), frozen key-set (`E20`), frozen
  retained count (`E22`), and frozen evidence identity (`E23`) pins all independently refuse an
  empty world regardless of internal self-consistency. Confirms the module's own claimed
  `evidence=[]` behavior (`{E16,E17,E19,E20,E23}`) exactly matches a direct re-run of that case.
- Two exploratory paths turned out to be non-attacks and are disclosed rather than silently
  dropped: (a) attempting to swap join keys between two evidence rows that share an identical
  `(flux_ivar_r, psfsize_r, nobs_r, quality_pass)` signature — checked the real 65,060-row
  evidence for any such duplicate signature and found **zero** groups, so this attack is not
  instantiable against the actual dataset (not a property of the verifier); (b) attempting to
  forge `evidence_sha256` back to the correct frozen `EVIDENCE_SHA256` on a "regenerated"
  evidence set — the regeneration logic was accidentally a no-op (produced byte-identical
  evidence to the authentic fixture), so this was retesting the pristine receipt, not an attack.
  Both are recorded here so the two apparent "ACCEPTED" results in my raw session log are not
  mistaken for exploits — investigated and confirmed non-findings before writing this report.

## `main()` / `--emit` verification

- `--emit`: ran a genuine `--acquire acquire --emit <tmp>.json` invocation. Wrote a valid JSON
  file (9.8MB) containing `{"receipt": ..., "evidence": [...]}`; re-parsed it and confirmed
  `receipt.n_retained == 49211` and `len(evidence) == 65060`, matching the printed summary
  exactly. Temp file removed after inspection; the reviewed subject and `acquire/` were not
  modified.
- `main()`'s digest-mismatch path, executed for real (not asserted): built a tiny fake
  `positions_selected.csv`/`quality_selected.csv` pair under `/tmp` (2 rows, not derived from or
  touching `acquire/` or `/Users/duhokim/NebulaMindData/`) and ran
  `--acquire /tmp/_bs2a_r5_fake_acquire`. Result: `QualityGateError: positions_selected.csv
  digest mismatch: expected ..., read ...` raised inside `build_evidence`/`verified_bytes` (by
  design — this is `verified_bytes`'s own documented refusal for wrong-source input, not
  `verify_receipt`), caught by the module's own `if __name__ == "__main__": sys.exit(main())`
  wrapper only insofar as Python's default traceback-and-nonzero-exit applies — `main()` itself
  does not wrap `build_evidence()` in a try/except, so a wrong-source `--acquire` argument
  produces a traceback and exit code 1, not a clean printed refusal message. This is consistent
  with the module's design (`verified_bytes` refuses by raising `QualityGateError`, a named
  exception type, before any receipt is built — not the same code path `verify_receipt` protects,
  and the exit code is still correctly non-zero) but is worth naming: a caller parsing stdout for
  a clean refusal message rather than checking the exit code would see a traceback here, not a
  `REFUSED:` line. Not scored as a finding against `verify_receipt` (out of that function's
  scope) but disclosed since the brief asked me to look at `main()` specifically.
- The genuine `MISMATCH`-but-clean-refusal path inside `verify_receipt` (via a hand-built
  in-memory `receipt`/`evidence` pair with the frozen digests removed from the mismatch) was
  exercised directly and repeatedly throughout this report's findings and failed-attack sections
  — e.g. the empty-evidence and inflated-count cases above both print `REFUSED:` lines via
  `main()`'s own `if bad: ... return 1` branch logic, verified by reading lines 806-809 against
  the `verify_receipt` outputs already captured.

## Claim-boundary review

Re-read the module docstring's claims (lines 21-44) against the code, independently of round 4's
review. The module states it is outcome-blind with respect to unobserved χ, explicitly disclaims
statistical independence from handedness, states the handedness-conditional-on-position question
is "not established," and says `E23` matching is "custody, not science." Found no executable
path, comment, or variable name anywhere in the file that asserts or implies anything stronger
than these disclaimers. Unchanged from round 3 and round 4's review — the docstring text itself
is byte-identical to what round 4 quoted (confirmed by direct read, not diffed against round 4's
report).

## Is any control passing for the wrong reason, or expecting a set it does not deserve?

Checked each control's mutator against its declared `expect` set for internal coherence (not just
that the real output matches — that reconciliation is 0 mismatches, above — but whether the
*mechanism* claimed in each control's docstring comment is the actual mechanism firing):

- `row contradicts predicate` (`_c_row_disagrees`) expects `{E12, E22, E23}`, **not** `E19` —
  the control's own comment explains why (`evidence_sha256` is re-digested honestly after the
  mutation, so `E19` cannot fire; only the frozen-identity pins `E22`/`E23` catch it because the
  *content*, not just the accompanying digest, no longer matches the authenticated evidence).
  Verified this reasoning directly: re-digesting after mutation does make `E19` pass while
  `E22`/`E23` still fire, confirming the control expects exactly what the mechanism produces.
- `non-boolean quality_pass` (`_c_nonbool`) expects `{E11, E16}`, explicitly **not** `E23` — the
  control's comment states the digest encodes `quality_pass` by truthiness so `int 1` and `True`
  produce identical digest bytes. Verified directly: `evidence_digest` uses
  `"1" if e.get("quality_pass") else "0"`, and Python's `1` is truthy, so this claim is
  mechanically correct, not merely asserted.
- No control's declared `expect` set was found to be broader or narrower than what a careful
  reading of the verifier's actual branch structure would predict for its mutation — none is
  "passing for the wrong reason" in the sense of expecting a code that fires by coincidence
  rather than by the mechanism the control's comment claims.

## Does the module claim more than it establishes?

No new instance beyond what round 4 already confirmed absent. The two new findings above are
about the verifier's own robustness (raise vs. refuse), not about a claim the docstring makes
that the code does not support — `verify_receipt`'s crashing on a malformed field is a
correctness defect in the refuse-vs-raise contract, not a misrepresentation of what the predicate
or the custody chain establishes.

## Testimony and constraints

The following is asserted from direct code reading rather than an executed reproduction,
disclosed per the brief's instruction:

- The exact interaction between an `E21`-flagged count field and every other place `COUNT_FIELDS`
  values are used besides the `E18` arithmetic (e.g. the f-string formatting at lines 363-364,
  which uses `repr()` and would not crash on `None`) — read from source, not independently
  fuzzed field-by-field beyond the specific attacks in findings 1 and 2, since the two concrete
  raises found are sufficient to establish the defect class without an exhaustive re-derivation
  of every non-crashing path.
- `main()`'s exit code on a real end-to-end `verify_receipt` MISMATCH via `--acquire` against the
  genuine frozen sources (as opposed to a hand-built in-memory receipt, which was exercised
  directly) was not separately re-run, since doing so would require corrupting the frozen
  `acquire/` CSVs or the module itself — outside scope, and forbidden by the brief's silence on
  destructive testing of frozen sources. The underlying mechanism (`if bad: ... return 1`) was
  verified by direct source read against many real `verify_receipt(rec, ev)` calls in this
  session that did produce non-empty `bad`, which is the same code path `main()` exercises.

Everything else in this report was executed in this session: the self-test run, the `--acquire`
run, the independent five-constant recomputation via a script that does not import the subject
(`gates/_tmp_bs2a_r5_recompute_constants.py`), the exhaustive single- and pairwise-code deletion
sweep against the live 34-control, 26-code battery (325 pairs, all caught, 0 silent), direct
reproduction of every round-4 repair claim plus this round's own disclosed near-miss and its
launder check in both directions, the two new raise-instead-of-refuse attacks in findings 1 and 2
with full tracebacks captured, the false-accept battery (including investigating and disclosing
two apparent-but-non-genuine "accepts" in my own raw log before writing this report), the
`--emit` round-trip, a genuine wrong-source `main()` invocation, and the claim-boundary and
control-mechanism reviews. I did not read `/Users/duhokim/NebulaMindData/`, did not fetch an
image byte, did not modify the reviewed subject, `acquire/`, or `successor_ref_v9.py` (all
sha256-confirmed unchanged before and after — see Identity section), and removed all temp files
created under `/tmp` after use. This review does not fill BS-2a, authorise a fetch, or resolve
conditional independence. BS-2a remains UNFILLED; one of fifteen class-P slots is filled; BS-6 and
the first image byte remain blocked.

**NOT CLEAR**
