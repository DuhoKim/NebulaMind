# BS-2a CODE GATE — CODEX, round 4

Verdict: **NOT CLEAR**. The pinned subject digest matches. `--self-test` genuinely passes (31
controls, 0 failures, 24/24 codes covered) and `--acquire` genuinely reproduces 49,211 of 65,060
with MATCH, both re-run independently in this session. Round 3's per-row raise-instead-of-refuse
defect (`del ev[0]["flux_ivar_r"]`) is confirmed repaired: the structural early-return now fires
before `evidence_digest()` is ever reached for an off-schema row, and I could not reopen that
specific hole by any variant. I could **not** make the verifier accept a receipt it should
reject — every single-code and every pairwise (all 276 combinations) deletion probe was caught,
every round-2/round-3 forgery is refused as claimed, and an extensive battery of new false-accept
attempts (lying-`__eq__` subclasses of the *correct* type, `int`-subclass counts, NaN thresholds,
bool thresholds, duplicated/tripled evidence lists, empty-string join keys) all refused correctly.
However, I *did* find new **raise-instead-of-refuse** defects, this time one level up from where
round 3 looked — at the top-level `receipt`/`evidence` parameters themselves rather than inside
an individual evidence row — and they are reachable with fully JSON-native inputs, not exotic
Python objects. That is a live defect in the shipped file, in the same class of bug that has kept
this gate at NOT CLEAR for three straight rounds.

## Identity and executed comparison

- Subject: `../ref/bs2a_quality_gate.py`.
- Brief-pinned sha256: `e9d2ce3be96e481bf6433ac4736a13b0f8b870da3f40f0cb988d1bf559a1c3c8`.
- Independently computed sha256 before testing (`shasum -a 256`): `e9d2ce3be96e481bf6433ac4736a13b0f8b870da3f40f0cb988d1bf559a1c3c8`.
- Independently recomputed sha256 after all probes: `e9d2ce3be96e481bf6433ac4736a13b0f8b870da3f40f0cb988d1bf559a1c3c8`.
- Comparison: **MATCH** — the reviewed bytes are exactly the brief-pinned subject at the sha256 identity level, unchanged by this review.
- `python3 ref/bs2a_quality_gate.py --self-test --acquire acquire` exited 0 and printed `self-test: 31 controls, 0 failure(s)` and `every one of 24 checks is exercised by a control`.
- `python3 ref/bs2a_quality_gate.py --acquire acquire` exited 0 and printed `n_parent=65060`, `n_joined=65060`, `n_retained=49211`, `n_excluded=15849`, `evidence_sha256=0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca`, and `retained 49,211 of 65,060 (expected 49,211) — MATCH`.
- `successor_ref_v9.py` sha256, before and after this review: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` — unchanged. Grepped the subject for `successor_ref_v9`: one match, the docstring line 6. Not imported, not opened, not executed anywhere in the file.

## Recomputed frozen constants

All five recomputed independently via `gates/_tmp_r4_recompute_constants.py`, which does **not**
import `bs2a_quality_gate.py` — it re-implements the join/predicate/digest logic directly from
the module's own docstring prose and reads `acquire/positions_selected.csv` /
`acquire/quality_selected.csv` directly, then string-matches the recomputed literals against the
subject file's source *text* (grep-equivalent, not import) so nothing here trusts the module's
own arithmetic:

| constant | literal in file | independently recomputed | match |
|---|---|---|---|
| `PARENT_SHA256` (source pin) | `425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831` | same, via direct file hash | MATCH |
| `QUALITY_SHA256` (source pin) | `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3` | same, via direct file hash | MATCH |
| `PARENT_ROWS` / `EXPECTED_RETAINED` cardinality basis | `65_060` rows, `49_211` retained | independently joined (0 duplicate keys, 0 missing, 0 orphaned either side) + predicate-applied count = `65060` / `49211` | MATCH |
| `PARENT_KEYSET_SHA256` | `550e50a8c6fbea2a72ac93597b8c0fbc6798fc78172a5056f10329d7dde93bd6` | independently recomputed = same | MATCH |
| `EVIDENCE_SHA256` | `0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca` | independently recomputed = same | MATCH |

Script output: `ALL FIVE MATCH SOURCE TEXT: True`. The trust root holds — none of the five is
theatre.

## Numbered findings

### 1. HIGH — malformed top-level `receipt`/`evidence` arguments crash the verifier instead of being refused, via fully JSON-native inputs

- File/lines: `../ref/bs2a_quality_gate.py:301-302` (`extra = set(receipt) - set(RECEIPT_FIELDS)`,
  `missing = set(RECEIPT_FIELDS) - set(receipt)`) and `:349-350`
  (`off_schema = [i for i, e in enumerate(evidence) if not isinstance(e, dict) or set(e) != set(EVIDENCE_FIELDS)]`),
  plus the off-schema reporting line `:353` (`shape = (... set(evidence[i]) ... else ...)`).
- Round 4's repair (verified fixed under finding 2 below) guards every check *inside* an
  individual evidence row's shape, and guards `off_schema`'s own computation against a row that
  is `None`/a string/an int via `isinstance(e, dict)` short-circuiting before `set(e)`. It did
  not add an equivalent guard on the *container* arguments themselves: `verify_receipt()` calls
  `set(receipt)` at line 301 assuming `receipt` supports iteration into a key-set, and
  `enumerate(evidence)` at line 349 assuming `evidence` supports iteration into a row-sequence —
  neither is type-checked before use, and this is the same defect *class* the module's own
  comments call out repeatedly ("a verifier that raises has not refused"), one level higher than
  where round 3 looked.
- Executed attacks, all against the real authenticated fixture with only the named substitution
  applied, all fully reachable by an attacker who controls a JSON document
  `{"receipt": ..., "evidence": ...}` handed to a caller that does
  `json.loads(...)["receipt"]` / `["evidence"]` with no further validation before calling
  `verify_receipt()` — precisely the module's own stated threat model (a hand-made receipt/
  evidence pair):
  ```
  receipt = None    (JSON null)                  → RAISED TypeError: 'NoneType' object is not iterable
  receipt = 42       (JSON number)                → RAISED TypeError: 'int' object is not iterable
  evidence = None    (JSON null)                  → RAISED TypeError: 'NoneType' object is not iterable
  evidence = 42      (JSON number)                → RAISED TypeError: 'int' object is not iterable
  evidence = true    (JSON bool)                  → RAISED TypeError: 'bool' object is not iterable
  evidence = {"a":1} (JSON object, non-empty)      → RAISED KeyError: 0
  ```
  Full tracebacks captured; representative two:
  ```
  File ".../bs2a_quality_gate.py", line 301, in verify_receipt
      extra = set(receipt) - set(RECEIPT_FIELDS)
  TypeError: 'NoneType' object is not iterable

  File ".../bs2a_quality_gate.py", line 353, in verify_receipt
      shape = (sorted(set(evidence[i]) ^ set(EVIDENCE_FIELDS)) if isinstance(evidence[i], dict)
  KeyError: 0
  ```
- The `evidence={"a":1}` case is the most interesting because it is *almost* caught: iterating a
  dict yields its string keys (`"a"`), so `off_schema` correctly flags index `0` as off-schema
  (`isinstance("a", dict)` is `False`). But the very code written to *report* that refusal at
  line 353 does `evidence[i]` with the integer index `i=0` — which is valid on a list but raises
  `KeyError: 0` on a dict, since a dict indexed by an int looks for the key `0`, not the 0th
  item. The detector fires; the reporter crashes before the refusal can be returned.
- Two inputs in this family did **not** crash, and are recorded for completeness (not findings):
  `evidence="notalist"` (a JSON string) iterates into individual characters, each of which fails
  `isinstance(e, dict)` cleanly → refused `{E09}`; `evidence={}` (an empty JSON object) iterates
  into zero rows → falls through as an empty evidence list, refused
  `{E16, E17, E19, E20, E23}` on the resulting count/digest mismatches. Both are accidental
  survivals of the same missing-type-guard problem, not evidence the problem is generally safe.
- Why it matters: this is exactly the class of bug that produced round 3's HIGH finding and this
  round's repair — "keyed off the structural condition, not off `bad`" — but the structural
  condition itself (`set(receipt)`, `enumerate(evidence)`) is unguarded at the point of first use.
  A verifier whose own stated design principle is "refuse malformed input, don't crash" has not
  applied that principle to its own two parameters.
- Smallest sufficient repair: at the top of `verify_receipt()`, before line 301, add
  `if not isinstance(receipt, dict): refuse("E01", ...); return bad` and, immediately after the
  receipt-schema early return (currently line 311-312), add
  `if not isinstance(evidence, list): refuse("E09", ...); return bad` before line 349 ever runs.
  This reuses existing codes (E01 for a non-dict receipt is the natural fit — an object that
  isn't a dict is trivially "missing required fields"; E09 for non-list evidence is the natural
  fit — a non-list is trivially "off-schema" at the collection level) and costs two isolated
  controls (`receipt is not a dict`, `evidence is not a list`) asserting the resulting code set
  contains no uncaught exception.

### 2. Everything round 3/round 4 claimed to fix, verified fixed

- **The specific round-3 defect is closed.** `del ev[0]["flux_ivar_r"]` on the authenticated
  fixture, receipt otherwise untouched: `verify_receipt()` now refuses `{E09}` cleanly, no
  exception. Reproduced for all six evidence-row fields individually (`brickid`, `objid`,
  `flux_ivar_r`, `psfsize_r`, `nobs_r`, `quality_pass`) — every one refused `{E09}`, none raised.
- **`off_schema` no longer raises while computing itself.** `ev[0] = None`, `ev[0] = "string"`,
  `ev[0] = 42` (a row replaced wholesale, not just missing a key) — all refused `{E09}` cleanly.
  `isinstance(e, dict)` short-circuits before `set(e)` as documented.
- **The encoder is guarded anyway.** Re-verified `evidence_digest()`'s `enc()` reaches
  `.get(k)` with the `\x00missing` sentinel for a well-formed-dict-but-missing-key case that
  somehow reaches the digest step (it can't currently, given the structural return at line
  360-361, but the guard is there as defense-in-depth) — confirmed the guard exists and does not
  interfere with well-formed evidence: `EVIDENCE_SHA256` and `PARENT_KEYSET_SHA256` both
  independently reproduce exactly (see constants table above), so no digest of well-formed
  evidence changed.
- **`OverflowError` is caught.** `float(10**400)` on `flux_ivar_r`: refused `{E10, E19, E23}`,
  not raised — reproduced directly.
- **A lying `__eq__` no longer buys an ACCEPT.** `_LiarEq()` (always compares equal, always
  unequal-false) substituted for `schema_version`, a threshold value, and `evidence_sha256`:
  refused `{E03}`, `{E07}`, `{E19}` respectively — the `type(x) is not T` guard catches it before
  the lying `__eq__` is ever consulted, reproduced. I additionally tried subclass variants the
  brief didn't name — `LyingFloat(float)` with `__eq__` always `True` as a threshold value, and
  `LyingStr(str)` with `__eq__` always `True` as `schema_version` — both still refused (`E07`,
  `E03`) because `type(x) is not T` checks the *exact* type, and `type(LyingFloat(2.0)) is float`
  is `False` (it's `LyingFloat`), so the type gate catches the subclass regardless of its `__eq__`.
- **Six isolated controls present and passing**: `row missing a key`, `row is not a dict`,
  `lying __eq__ schema`, `lying __eq__ threshold`, `lying __eq__ digest`, `value overflows
  float` — all five verified in the self-test output above (31 controls total, up from 25 in
  round 3), each producing exactly its declared code set.
- **31 controls, 0 failures, 24/24 codes covered** — confirmed by direct execution, not asserted.

## Deletion-probe results (exhaustive, this session, against the current 31-control battery)

Methodology: filtered `verify_receipt()`'s real output per control, dropping any refusal
carrying a to-be-deleted code (equivalent to deleting the corresponding `refuse()` call — valid
because nothing in the function branches on the *contents* of `bad`, only on the structural
`missing or extra` / `off_schema` conditions, and neither deletion touches those), then compared
against each control's declared exact-set expectation. Sanity check first: all 31 controls'
*real, undeleted* code sets matched their declared `expect` sets exactly (0 mismatches) — i.e.
the current `CONTROLS` table's own expectations are internally correct before any deletion is
simulated.

- **Single-code deletion, all 24 codes**: **all 24 caught.** No orphans — every deletion changed
  at least one control's observable behavior.
- **Pairwise deletion, all 276 combinations of 2 codes out of 24**: **all 276 caught.**
  (`gates/_tmp_r4_deletion_sweep.py`, exhaustive, not sampled — full C(24,2) sweep, completed in
  under a second since it operates on precomputed real code-sets rather than re-running
  `verify_receipt()` per combination.)
- This directly answers the brief's question 2 ("does the new early return hide anything? ...
  construct a receipt whose only other defect is below E09 and which also carries an off-schema
  row, and check the short-circuit is not laundering the second fault"): constructed exactly that
  — an off-schema row (extra `chi_net` field on row 1) *combined with* a corrupted `n_retained`/
  `n_excluded` pair (an E16/E22-class defect) in the same receipt. Result: refused `{E09}` only —
  the short-circuit does mean the second (below-E09) fault is never independently reported in
  *this* call, but that is not laundering: `E09` alone is a true and sufficient refusal (the
  receipt IS rejected), and the second defect can never reach ACCEPT because E09 already blocks
  it. I also tried the inverse — corrupt `evidence_sha256` to `"f"*64` alongside the same
  off-schema row — same result, refused `{E09}` only, never accepted.

## Failed attacks (new to this round, beyond the deletion sweep)

- Lying-`__eq__` **subclasses of the correct type** (`LyingFloat(float)`, `LyingStr(str)`) —
  refused, not accepted (see finding 2).
- `int`-subclass count field (`class IntSub(int): pass`) with the *correct* value — refused
  `{E21}` because `type(x) is not int` checks the exact type, and `type(IntSub(...))` is
  `IntSub`, not `int`. This means the count-field type gate is actually *stricter* than
  necessary (it would reject a legitimately-typed `int` subclass too) — not a security problem,
  flagged only as a minor behavioral note, not a finding.
- `bool` substituted for a threshold value (`nobs_r_ge = True`) — refused `{E07}` (thresholds
  are compared with `!=` against the exact frozen float, and `True != 3.0`, so this is caught by
  value regardless of the type gate that protects count fields specifically).
- NaN as a threshold value (`flux_ivar_r_gt = nan`) — refused `{E07}` (`nan != 8.4000532` is
  `True` in IEEE 754, so the `!=` comparison alone catches it without needing a finite check).
- NaN-shaped join key content (`join_keys = ["brickid", nan]`) — refused `{E08}` (`nan != "objid"`
  under the exact-list-equality check).
- String literal `"nan"` as a `brickid` value on a real row — refused `{E19, E20, E23}` (changes
  the row's identity, breaks the frozen key-set and digest commitments, exactly as any other
  single-character mutation would).
- Evidence list tripled via `ev * 3` (65,060 → 195,180 rows, mostly duplicate dict references) —
  refused `{E15, E16, E17, E19, E20, E23}`, no crash, no hang, no accept — the duplicate-key
  check (`E15`) and the count/digest checks all fire together as expected for a grossly malformed
  evidence list.
- Empty-string `objid` on a row — refused `{E19, E20, E23}`, not accepted, not raised.
- `n_parent = True` (bool where a row-count int belongs) — refused `{E13, E14, E21}` (the count
  type gate at `E21` catches it, and since `type(True) is bool` fails the `is not int` check
  regardless of `True == 1`, the round-2 float/bool defect class remains closed for this field
  too, consistent with the module's own comment at lines 337-338).
- A row carrying a Python-level circular self-reference as an extra field (not JSON-producible,
  included for completeness) — refused `{E09}` cleanly; the off-schema set-size check fires on
  field *count* before anything would need to traverse into the cycle, so no infinite loop.
- Exotic non-JSON-reachable objects (`__str__`/`__float__` that raise `ValueError` /
  `ZeroDivisionError` / infinite-recurse) *do* still crash the verifier (`ValueError`,
  `ZeroDivisionError`, `RecursionError` respectively) when substituted for `brickid` or
  `flux_ivar_r` on an otherwise-well-formed row. These are **not** reachable through a JSON
  receipt/evidence document (JSON has no mechanism to embed a Python object with a hostile
  `__str__`/`__float__`), so they are recorded here as a narrower-threat-model observation, not
  folded into finding 1's severity — finding 1 is scored on its JSON-reachable subset only. If
  `verify_receipt()` is ever called with receipt/evidence data that is not a plain JSON
  round-trip (e.g. directly from `build_evidence()`'s own Python objects, which are always
  well-formed floats/strings from `csv.DictReader`+`float()`, so this path does not arise in the
  module's own callers), this class would need the same treatment as finding 1's repair.

## Claim-boundary review

Re-read the module docstring's claims (lines 21-44) against the code. The module states it is
outcome-blind with respect to unobserved χ, explicitly disclaims statistical independence from
handedness, states the handedness-conditional-on-position question is "not established," and
says `E23` matching is "custody, not science." I found no executable path, comment, or variable
name anywhere in the file that asserts or implies anything stronger than these disclaimers — the
claims are consistently scoped throughout, unchanged from round 3's review.

## Delta vs round 3 (this seat's own prior report)

Round 3 found one HIGH defect (a well-formed-schema row missing one required key crashed
`evidence_digest()` via a bare `KeyError`) and confirmed all four round-2 defects fixed. That
round-3 defect is independently reproduced as fixed in this round (finding 2 above). Round 3 did
not test the top-level `receipt`/`evidence` *container* types themselves — it tested rows within
evidence, not evidence's own type, and not receipt's own type. That gap is what finding 1 above
closes: the same "raise instead of refuse" defect class, surfaced one abstraction level higher by
trying the exact angle the round-4 brief asked for ("try the angles it [round 3] did not").

## A note on execution environment

While running this review I found other background processes from a parallel GPT56 round-4
dispatch active in the process table (`gates/_tmp_bs2acode_r4.sh`, `gates/_tmp_deletion_probe_r4b.py`,
launched ~19:53 KST, contemporaneous with this session) independently executing the same round-4
brief and targeting `gates/BS2A_CODE_GATE_GPT56.md` — a different output path than this report's,
so no collision on this file is expected. I did not stop that process, since it targets a
different seat's output file and killing another in-flight process's work is outside what this
brief authorized. All findings above were independently derived and executed in this session's
own working files (`gates/_tmp_r4_*.py`), none of which were shared with or read from that other
process's temp files.

## Testimony and constraints

The following is asserted from direct code reading rather than an executed reproduction,
disclosed per the brief's instruction:

- `main()`'s `if bad: return 1` producing a nonzero exit on a genuine `MISMATCH` — read from the
  source (`if bad: ... return 1` branch after the `--acquire` path's `verify_receipt()` call),
  not exercised end-to-end against a real mismatching dataset, since doing so would require
  corrupting the frozen `acquire/` CSVs (outside scope; the brief forbids reading
  `/Users/duhokim/NebulaMindData/` and the review must not modify reviewed sources). The
  underlying mechanism was verified directly via `verify_receipt()` calls on forged receipts with
  mismatching `n_retained`/`n_parent`/etc., which is the same code path `main()` exercises.

Everything else in this report was executed in this session: the self-test run, the `--acquire`
run, the independent five-constant recomputation via a script that does not import the subject
(`gates/_tmp_r4_recompute_constants.py`), the exhaustive single- and pairwise-code deletion sweep
against the live 31-control battery (`gates/_tmp_r4_deletion_sweep.py`, 300 total combinations,
0 silent), the direct reproduction of every round-3/round-4 repair claim, the new top-level
raise-instead-of-refuse attacks in finding 1 (`gates/_tmp_r4_attack.py`,
`gates/_tmp_r4_attack2.py`, with full tracebacks captured), and the claim-boundary grep. I did
not read `/Users/duhokim/NebulaMindData/`, did not fetch an image byte, did not emit an
acquisition artifact via `--emit`, and did not modify the reviewed subject or
`successor_ref_v9.py` (both sha256-confirmed unchanged before and after, see Identity section).
This review does not fill BS-2a, authorise a fetch, or resolve conditional independence. BS-2a
remains UNFILLED; one of fifteen class-P slots is filled; BS-6 and the first image byte remain
blocked.

**NOT CLEAR**
