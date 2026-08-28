# BS-2a CODE GATE — CODEX, round 5

Verdict: **NOT CLEAR**. The pinned subject digest matches exactly. `--self-test` genuinely
passes (34 controls, 0 failures, 26/26 codes covered — matching the brief's claim to the digit)
and `--acquire` genuinely reproduces 49,211 of 65,060 with MATCH, both re-run independently in
this session. Round 4's finding — malformed top-level `receipt`/`evidence` containers crashing
instead of refusing — is confirmed repaired: `E25`/`E26` catch every container-shape attack I
constructed, including the brief's own disclosed near-miss (`evidence={"a":1}`), and the
short-circuit does not launder a second, lower-priority fault (tested both directions, and one
level lower at `E09`'s own early return too). All 26 single-code and all 325 pairwise (`C(26,2)`)
code-deletion combinations over the current 34-control battery are caught. **I could not make the
verifier ACCEPT a receipt it should reject** — an extended false-accept battery (dict/list
subclasses, a full `Mapping`-protocol non-dict, `str` subclasses on join keys and `join_keys`
itself, `MappingProxyType` rows, `IntEnum` for `quality_pass`, `complex` thresholds, identity-
aliased duplicate rows, a colliding-`__eq__` extra receipt key) all refused correctly. **But I did
make it RAISE instead of refuse**, on fully JSON-native input that clears the E25/E26 container
gate — and independently reproduced a second seat's (GPT56's) two round-5 findings of the exact
same shape rather than taking them on trust. Both are the identical "raise instead of refuse"
class this module has now surfaced at four consecutive levels (per-row shape → per-row values →
top-level containers → individual field values used downstream), each round's own repair
introducing the next level rather than closing the class.

## Identity and executed comparison

- Subject: `../ref/bs2a_quality_gate.py`.
- Brief-pinned sha256: `aa03d1f96f47742b1cd4863b4f0e5ebbeeac66dba787b83175d9b95f702c509f`.
- Independently computed sha256 before testing (`shasum -a 256`):
  `aa03d1f96f47742b1cd4863b4f0e5ebbeeac66dba787b83175d9b95f702c509f`.
- Independently recomputed sha256 after all probes (this review never edited the reviewed
  subject): `aa03d1f96f47742b1cd4863b4f0e5ebbeeac66dba787b83175d9b95f702c509f`.
- **Comparison: MATCH** — the reviewed bytes are exactly the brief-pinned subject at the sha256
  identity level, before and after this review.
- Cross-checked against the git history of this working tree (`git log --oneline -- .../ref/bs2a_quality_gate.py`):
  the tip commit `a03bdd5d3` ("fix(bs2a): guard the containers, and key their early return off the
  structure not the refusal list") is the round-5 repair the brief describes, and `git show a03bdd5d3`
  shows exactly the diff the brief's dispatch note claims: `E25`/`E26` codes added, the
  container-type guard added before the receipt-field checks, the structural (not `bad`-keyed)
  early return, and the three new controls (`receipt is not an object`, `evidence is not a list`,
  `evidence is a dict`). This is corroborating evidence for the diff's shape, not a substitute for
  the independent digest/behavior checks above.
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
  FROZEN and this file does not touch it"). Not imported, not opened, not executed anywhere in the
  file. No `git status` change against `successor_ref_v9.py` for the duration of this review.

## Recomputed frozen constants (without importing the module)

All five recomputed via `gates/_tmp_r5_recompute_constants.py`, written fresh this round. It does
**not** `import bs2a_quality_gate`; it re-implements the join/predicate/digest logic directly from
the module's own docstring prose (read as text, transcribed by hand) and reads
`acquire/positions_selected.csv` / `acquire/quality_selected.csv` directly, then string-matches the
recomputed literals against the subject file's own source *text* (grep-equivalent, not import), so
nothing here trusts the module's own arithmetic or its own import machinery:

| constant | literal in file | independently recomputed | match |
|---|---|---|---|
| `PARENT_SHA256` (source pin) | `425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831` | same, via direct file hash | MATCH |
| `QUALITY_SHA256` (source pin) | `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3` | same, via direct file hash | MATCH |
| `PARENT_ROWS` / `EXPECTED_RETAINED` | `65_060` rows, `49_211` retained | independent join (0 duplicate parent keys, 0 duplicate quality keys, 0 parent objects missing a quality row, 0 orphaned quality rows) + predicate applied per-row = `65060` / `49211` | MATCH |
| `PARENT_KEYSET_SHA256` | `550e50a8c6fbea2a72ac93597b8c0fbc6798fc78172a5056f10329d7dde93bd6` | independently recomputed = same | MATCH |
| `EVIDENCE_SHA256` | `0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca` | independently recomputed = same | MATCH |

Script output: `ALL FIVE MATCH SOURCE TEXT: True`. The trust root holds: `PARENT_SHA256`/
`QUALITY_SHA256` are exactly the sha256 of the real `acquire/` CSVs, the join is genuinely total
and one-to-one (0 duplicates, 0 missing, 0 orphaned on either side, computed independently of
`build_evidence()`), and both derived commitments match exactly what the sources produce. None of
the five is theatre.

## Numbered findings

### 1. HIGH — `E18`'s `n_retained + n_excluded` arithmetic crashes instead of refusing, on fully JSON-native input that the `E21` type gate already flagged but did not structurally return on

- File/line: `../ref/bs2a_quality_gate.py:435`
  (`if receipt["n_retained"] + receipt["n_excluded"] != receipt["n_joined"]:`).
- `E21` (lines 360-364) checks every `COUNT_FIELDS` member (`n_parent`, `n_joined`, `n_retained`,
  `n_excluded`) for `type(x) is not int or x < 0` and appends a refusal to `bad` — but it does
  **not** return. Line 435 is 71 lines later and does raw `+` arithmetic on two of those same four
  fields without re-checking their type. The module's own comments state the governing principle
  three times ("a verifier that raises has not refused", lines 259, ~314-318, ~377-381) and this
  round's own repair applied it at the container level — but not here, one level further in, at a
  single field's downstream arithmetic use.
- Executed attacks, against the real authenticated fixture with only the named field(s)
  substituted, all reachable by a `json.loads(...)["receipt"]["n_retained"] = None` edit to an
  otherwise well-formed JSON document — squarely inside the module's own stated threat model (a
  hand-made receipt/evidence pair):
  ```
  n_retained = None   (JSON null)    → RAISED TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
  n_excluded = None   (JSON null)    → RAISED TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
  n_retained = "49211" (JSON string) → RAISED TypeError: can only concatenate str (not "int") to str
  ```
  Full traceback for the first, captured directly from this session:
  ```
  File ".../bs2a_quality_gate.py", line 435, in verify_receipt
      if receipt["n_retained"] + receipt["n_excluded"] != receipt["n_joined"]:
  TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
  ```
- Contrast, executed in this session, to confirm the crash is field-specific and not general to
  every `E21`-flagged field: `n_joined = None` and `n_parent = None` both refuse cleanly
  (`{E14, E17, E18, E21}` and `{E13, E14, E21}` respectively) — neither is ever used in `+`
  arithmetic below the `E21` check, only in `!=`/`<`/`len()` comparisons, none of which raise on
  `None` against an `int`. Only `n_retained` and `n_excluded` are ever added together.
- The 34-control battery does not exercise this: its two existing count-type controls (`float
  count fields`, `boolean count field`) both substitute types Python's `+` handles without raising
  (`float + int` and `bool + int` are legal, since `bool` subclasses `int`) — so this specific
  arithmetic-crash shape was never constructed by the current battery.
- Smallest sufficient repair: make `E21` return immediately when `mistyped` is non-empty (mirroring
  the structural-return pattern this round's own repair already applied at `E25`/`E26` and the
  pre-existing `E01`/`E02` pattern), before line 366 ever runs. This requires updating the
  `boolean count field` control's expected set from `{E18, E21}` to `{E21}` alone (an early return
  on `E21` prevents `E18` from ever firing for that specific mutation), so the fix and the control
  table must land together.

### 2. HIGH — `E15`'s `set(keys)` crashes on an unhashable join-key value, past the `E24` field-type gate that flagged it but did not structurally return

- File/lines: `../ref/bs2a_quality_gate.py:424-425`
  (`keys = [(e.get("brickid"), e.get("objid")) for e in evidence]` /
  `if len(set(keys)) != len(keys):`).
- `E24` (lines 418-422) checks `type(e.get("brickid")) is not str or type(e.get("objid")) is not
  str` per row and refuses if any join key is non-string — but does not return. Two lines later,
  `E15` builds a list of `(brickid, objid)` tuples and calls `set(keys)` to check uniqueness; a
  tuple containing an unhashable element (a JSON array or JSON object, both legal values for a
  `brickid`/`objid` field in a hand-made receipt) makes the tuple itself unhashable, and `set()`
  raises before `E15` can record anything.
- Executed attacks, against the real authenticated fixture with only one row's join key field
  substituted, all directly JSON-native:
  ```
  brickid = [1, 2, 3]   (JSON array)   → RAISED TypeError: unhashable type: 'list'
  brickid = {"a": 1}    (JSON object)  → RAISED TypeError: unhashable type: 'dict'
  objid   = [1, 2]      (JSON array)   → RAISED TypeError: unhashable type: 'list'
  ```
  Full traceback for the first, captured directly from this session:
  ```
  File ".../bs2a_quality_gate.py", line 425, in verify_receipt
      if len(set(keys)) != len(keys):
  TypeError: unhashable type: 'list'
  ```
- Contrast, executed in this session, to isolate the defect: `brickid = 12345` (a plain `int`,
  hashable, non-string) does **not** crash — it refuses cleanly `{E19, E20, E23, E24}`. Only
  *unhashable* non-string values reach the crash; the existing `non-string join key` control
  (`_c_nonstring_key`, which uses `int`) is hashable and cannot see this class.
- Interaction with finding 1, executed: when a row carries both an unhashable `brickid` AND a
  `None` `n_retained` simultaneously, the verifier crashes at line 425 (`E15`'s site, which runs
  first in source order) rather than reaching line 435 — confirmed by direct execution and
  traceback inspection. This is not laundering (nothing is accepted), but it means the two findings
  are not independent in one specific joint-attack ordering; each is independently reachable alone.
- Why it matters: identical shape to finding 1 — a field-level type gate (`E24`) that flags but
  does not structurally return, followed by code that assumes the flagged value is safe to use
  (here, *hashable*) rather than merely *present*. `E19`/`E20`/`E23` (the digest/keyset checks,
  which run later) would independently catch a forged unhashable key via `_enc()`'s `str()`
  coercion — the module's own docstring at lines 254-261 explicitly says this coercion exists "so
  that a non-string join key digests instead of raising" — but `E15` at line 425 runs *before*
  those and has no equivalent defense.
- Smallest sufficient repair: build `keys` using the same `str()`-coercion `_enc()` already applies
  for exactly this reason — `keys = [(str(e.get("brickid")), str(e.get("objid"))) for e in
  evidence]` — which makes `E15`'s uniqueness check well-defined for any JSON-native value without
  requiring `E24` to gate it first, and requires no control-table renumbering since E15's expected
  set is unaffected for non-string-but-stringifiable keys.

**Independence note on findings 1 and 2:** both were first surfaced in a parallel round-5 seat's
(GPT56's) report, which I read after completing my own independent attack battery (Section:
"E25/E26 second-fault-laundering test" and "NEW false-accept battery" below) and before writing
this report. Per this review's own discipline (verify, never trust another seat's claim), I did not
take either finding on the other report's word — I independently re-derived both directly against
the real shipped subject file's source (confirming the exact line numbers, the exact traceback
text, and the contrast cases) via a fresh script (`gates/_tmp_r5_verify_gpt56.py`) that imports
only the subject module, not the other report. Both reproduced exactly as described. This is
disclosed per the brief's Testimony requirement, and is a corroboration, not a substitute for
independent execution — every command that produced the traceback text above was run in this
session against this file.

### 3. Everything round 4 claimed to fix, verified fixed — including this round's own disclosed near-miss and the requested "look for the same shape elsewhere" check

- **Round 4's container-type defect is closed.** `receipt=None`, `receipt=42`, `evidence=None`,
  `evidence=42`, `evidence=True` — all refuse cleanly (`{E25}` or `{E26}`), no exception,
  reproduced directly this round.
- **This round's own disclosed near-miss (`evidence={"a":1}`) is genuinely fixed.** `off_schema`
  no longer runs at all for a non-list `evidence`: `E26` catches the type before
  `enumerate(evidence)` is ever reached (confirmed by reading the code at line 313-314 and by
  direct execution — `evidence={"a":1}` refuses `{E26}` cleanly).
- **The E25/E26 short-circuit does not launder a second, lower-priority fault** (the brief's
  question 2), tested in both directions:
  - `receipt=None` + evidence independently carrying a forged parent key (would be `{E20,E23}` if
    reached) → refused `{E25}` only.
  - `evidence=None` + receipt independently carrying a wrong `schema_version` (would be `{E03}` if
    reached) → refused `{E26}` only.
  - Both bad simultaneously → refused `{E25, E26}` — both codes named, neither swallows the other.
- **The same launder check applied one level lower, at `E09`'s own pre-existing early return**
  (per the brief's "look for the same shape elsewhere"): an off-schema row (would fire `E09`)
  combined *simultaneously* with an inflated `n_retained`/`n_excluded` pair (would fire
  `E16`/`E22` if reached), a forged parent key on another row (would fire `E20`/`E23` if reached),
  and a deliberately wrong `evidence_sha256` (would fire `E19` if reached) all at once → refused
  `{E09}` only. `E09`'s early return has the identical non-laundering property as `E25`/`E26`'s.
- **The self-repair the brief disclosed (structural return keyed on the condition, not on `bad`)
  is present and correct at all three sites**: line 319 (`if not (receipt_ok and evidence_ok):
  return bad`), line 332 (`if missing or extra: return bad`), and line 382 (`if off_schema: ...
  return bad`) — all three key off independently-computed structural booleans, not off whether
  `bad` is non-empty, confirmed by direct source read of every early-return statement in the
  function (there are exactly these three, plus the final `return bad` at the end).
- **Reconstructed and confirmed the disclosed pre-dispatch defect really would have existed** in
  the shape the brief describes: I rebuilt the "first version" of the container guard by reverting
  its early return from the structural condition (`if not (receipt_ok and evidence_ok)`) to a
  `bad`-keyed one (`if bad: return bad`) *and* deleting the `E25` `refuse()` call, in a throwaway
  copy of the source (never touching the reviewed subject). Calling `verify_receipt(None, ev)`
  against that reconstruction **crashed** with `TypeError: 'NoneType' object is not iterable` at
  the `set(receipt)` line — confirming the disclosed pre-dispatch bug shape is real. Calling the
  *actual shipped* subject with the same input returns cleanly: `['[E25] receipt is not an
  object: NoneType']`. The repair is genuine, not merely claimed.
- **34 controls, 0 failures, 26/26 codes covered** — confirmed by direct execution, not asserted.

## Deletion-probe results (exhaustive, this session, against the current 34-control, 26-code battery)

Methodology: for every control, compared its real executed refusal-code set against its declared
`expect` set (0 mismatches — the battery's own claims about itself hold). Then for every candidate
deletion set (every single code, and every pairwise combination), computed whether *any* control's
`(real_codes − deleted) != expect` — equivalent to deleting the corresponding `refuse()` call(s),
valid because nothing in `verify_receipt()` branches on the *contents* of `bad`, only on the three
independently-computed structural booleans identified in finding-3's bullet above (re-verified by
direct source read, not assumed).

- **Single-code deletion, all 26 codes**: **all 26 caught.** No orphans.
- **Pairwise deletion, all 325 combinations of 2 codes out of 26** (`C(26,2) = 325`; note the
  brief's own recap text cites round 4's "276 pairwise" figure, which was `C(24,2)` before this
  round's `E25`/`E26` grew the code set to 26 — the correct exhaustive count for the *current*
  battery is 325, and I ran all 325, not 276): **all 325 caught.** No orphans.
- **Real-execution confirmation for the highest-overlap pairs** (not filter-simulated for these —
  independently re-derived by calling the actual `verify_receipt()` per control and only then
  post-filtering its true output, which is behaviorally identical to a real deletion per the
  structural-condition argument above, but was cross-checked against a hand-reconstructed literal
  source deletion for six of the newest/highest-risk codes — see next paragraph):
  `{E25,E26}`, `{E01,E02}`, `{E13,E14}`, `{E14,E17}`, `{E16,E22}`, `{E18,E21}`, `{E20,E23}`,
  `{E15,E20}`, `{E12,E22}`, `{E12,E23}`, `{E11,E16}`, `{E20,E24}`, `{E23,E24}`, `{E10,E23}`,
  `{E09,E25}`, `{E09,E26}` — every one caught, consistent with the exhaustive sweep.
- **Real source-level mutation (not filter-simulated) for six codes**, to go beyond output-
  filtering: literally deleted the `refuse("E25", ...)`, `refuse("E26", ...)`, `refuse("E09", ...)`,
  `refuse("E19", ...)`, `refuse("E23", ...)`, and `refuse("E20", ...)` call sites from six separate
  copies of the real source file (never the reviewed subject) and ran the real `--self-test
  --acquire acquire` against each mutant. All six were caught by name: e.g. mutant `E25` produced
  `FAIL receipt is not an object: expected ['E25'], got [] ... self-test: 34 controls, 1
  failure(s)`; mutant `E23` produced 7 named failures (every control whose expected set includes
  `E23`); mutant `E20` produced 3 named failures. This is a stronger check than filtering a live
  run's output, and it agrees with the filter-based sweep exactly.
- This directly answers the brief's question 5 ("is any control passing for the wrong reason, or
  expecting a set it does not deserve?"): no. Every one of the 34 controls reproduces its declared
  exact set against the unmodified subject, and none survives either its own or a paired code's
  deletion — verified both by output-filtering (325 pairs) and by real source mutation (6 spot
  checks including the newest codes).

## Failed attacks — could not make the verifier ACCEPT a receipt it should reject

All of the following were tried against the real, unmodified subject and all **refused** (none
accepted, none silently laundered):

- **Container subclass attacks**: receipt as a `dict` subclass (`DictSub`, exact-type check `type(x)
  is dict` correctly rejects it) — refused `{E25}`. Evidence as a `list` subclass (`ListSub`) —
  refused `{E26}`. Receipt implementing the full `collections.abc.Mapping` protocol but not a real
  `dict` (`FakeMapping`) — refused `{E25}`. Evidence as a duck-typed `__iter__`/`__len__` object
  that is not a real list (`FakeList`) — refused `{E26}`.
- **`str`-subclass attacks on the exact-type gates**: `join_keys` supplied as a list of `str`
  subclass instances (`StrSub("brickid")`, `StrSub("objid")`, value-equal to the real strings) —
  refused `{E08}` (the exact-type check `type(k) is not str` correctly rejects a subclass despite
  value equality). Evidence row `brickid` as a `str` subclass, value otherwise unchanged — refused
  `{E24}`, same reasoning.
- **`Decimal`/`complex`/`IntEnum` type-confusion attempts**: threshold `psfsize_r_lt` as
  `complex(1.5699703, 0)` (numerically real-part-equal) — refused `{E07}` (`type(t[name]) not in
  (int, float)` excludes `complex`). `quality_pass` as an `IntEnum` member (`QP.TRUE`, value `1`,
  not `bool`) — refused `{E11, E16}` (`type(x) is not bool` correctly excludes the enum despite its
  int-like value).
- **Immutable/aliased-row attacks**: an evidence row wrapped in `types.MappingProxyType` (fully
  read-only, otherwise a valid row) — refused `{E09}` (`isinstance(e, dict)` correctly rejects a
  proxy, since a `MappingProxyType` is not a `dict` instance). Two evidence rows sharing the exact
  same dict *object* by identity (aliasing) with a duplicate key by construction — refused `{E15,
  E16, E20, E23}`, no crash, no silent double-count.
- **Non-JSON-reachable Python-only attack** (recorded per prior-round precedent, narrower threat
  model, not folded into either HIGH finding's severity): an extra receipt key constructed with a
  colliding `__eq__`/`__hash__` designed to make `set(receipt) - set(RECEIPT_FIELDS)` miss it —
  refused `{E08}` (the collision affects a different check, not the one it targeted; the smuggled
  key still surfaces via `E02`'s underlying set difference in practice, and separately the
  `join_keys` field this attack happened to collide with fired independently).
- Threshold-value forgery, extra receipt fields, missing receipt fields, late-row-carries-χ,
  row-missing-a-key, row-is-not-a-dict, lying `__eq__` on schema/threshold/digest, `OverflowError`
  values, foreign all-pass partitions, forged parent members, duplicate evidence keys, non-string
  (hashable) join keys — all reconfirmed refused exactly as rounds 3/4 established, re-executed
  fresh in this session rather than assumed from prior reports.

## `main()` / `--emit` surface probes (the brief's question 1: "consider `--emit` and `main()`, not only `verify_receipt()`")

Executed via real subprocess invocations of `ref/bs2a_quality_gate.py`, not simulated:

- No arguments: prints `--acquire <dir> required (or --self-test)`, exits 1. Clean.
- `--acquire <nonexistent dir>`: raises `FileNotFoundError` inside `verified_bytes()`'s `os.open()`
  call, uncaught, traceback to stderr, process exit 1. This is a **raise, not a refuse**, but it is
  outside `verify_receipt()`'s scope — it is the acquisition/build stage refusing to even construct
  a receipt from missing or absent source files, which is a different threat model (a missing
  filesystem path, not a malformed receipt) from what `CODES`/`CONTROLS` are built to cover. Not
  scored as a new finding against `verify_receipt()`'s contract, but noted since the brief asked to
  look at `main()` specifically: `main()` provides no refusal-style handling for this class of
  input at all, only bare tracebacks, for every one of: parent-source digest mismatch (confirmed:
  corrupting a byte of `quality_selected.csv` in a throwaway copy produces
  `QualityGateError: ... digest mismatch`, an intentional named refusal raised as an exception, not
  caught by `main()`, printed as an uncaught traceback), a source path that is a directory instead
  of a regular file (confirmed: `QualityGateError: ... is not a regular file`, same uncaught-raise
  behavior), and a missing/partial acquire directory (confirmed: bare `FileNotFoundError`).
- `--self-test --acquire <nonexistent dir>`: this path is explicitly guarded — prints `FAIL sources
  not found under <dir>; the fixture is the authenticated evidence and cannot be synthesised`,
  exits 1, no traceback. Confirmed the asymmetry: `--self-test` guards against a missing acquire
  directory; the real `--acquire` (production) path does not, and neither guards against a
  digest-mismatched or non-regular-file source — both surface as uncaught `QualityGateError` /
  `FileNotFoundError` tracebacks rather than a clean nonzero exit with an informative refusal
  message. This is consistent with the module's own explicit design principle applying to
  `verify_receipt()`'s contract, not to `build_evidence()`'s acquisition-stage error handling,
  which the module's docstring does not claim covers this class — recorded as an observation for
  completeness per the brief's specific ask, not folded into either numbered HIGH finding (which
  are both scoped to `verify_receipt()`, matching every prior round's scope).
- `--emit <valid tmp path>`: writes the full receipt+evidence JSON (9.8MB), prints `wrote
  <path>`, exits 0. Confirmed by inspecting the written file's size and structure.
- `--emit <path in a nonexistent directory>`: raises bare `FileNotFoundError` from
  `Path(...).write_text(...)`, uncaught, after already having printed the receipt JSON and the
  MATCH line to stdout. A cosmetic/operational gap (an operator-facing usage error, not a receipt
  a caller controls), not a security-relevant refusal-vs-raise defect since `--emit`'s destination
  is a trusted operator argument, not adversary-controlled input — not scored as a finding.
- `--self-test --acquire acquire` (self-test flag combined with a valid acquire path): self-test
  wins, runs the full 34-control battery as normal, exits 0. Consistent flag-precedence, no
  surprise.

## Claim-boundary review (the brief's question 6: "does the module claim more than it establishes?")

Re-read the module docstring's claims (lines 21-44) against the code, and re-read the three
instances of the "a verifier that raises has not refused" design principle (lines 259, ~314-318,
~377-381) against findings 1 and 2 above. The docstring's substantive scientific claims
(outcome-blindness with respect to unobserved χ, explicit disclaimer of statistical independence
from handedness, "not established" for conditional-on-position independence, `E23` matching being
"custody, not science") are unchanged from prior rounds and remain consistently scoped — no
executable path or comment asserts anything stronger. However, the module's own *design-principle*
claim ("nothing below may assume its container's shape without this", "a verifier that raises has
not refused") is stated as an absolute but is not fully established by the code: findings 1 and 2
are exactly a violation of that stated principle, one level further in than this round's own
repair reached. This is a real gap between what the module's comments assert about itself and what
the code delivers — worth naming explicitly as the answer to question 6, distinct from the
science-claim boundary which holds.

## Delta vs round 4 (this seat's own prior report)

Round 4 found one HIGH defect (top-level `receipt`/`evidence` container raise-instead-of-refuse)
and confirmed all round-3 repairs held. That defect is independently reproduced as fixed in this
round (finding 3 above), including the pre-dispatch near-miss the brief disclosed and a
reconstruction proving the disclosed defect shape was real. Round 4 did not test individual field
values used in downstream arithmetic/hashing after passing their own type gate without a
structural return — that gap is what findings 1 and 2 above close, surfaced by trying the exact
angle the round-5 brief asked for ("find another raise... where is the next level?") and
cross-checked against a parallel seat's independent findings of the same shape rather than taken
on trust.

## A note on execution environment

While running this review I observed a parallel GPT56 round-5 process still active in the process
table (`gates/_tmp_bs2acode_r5.sh`, dispatched contemporaneously, targeting
`gates/BS2A_CODE_GATE_GPT56_R5.md` — a different output path than this report's) and its report
already written to disk by the time I reached the claim-boundary section of my own review. I read
that report only after completing my own independent attack battery (deletion sweep, container
laundering tests, and the new false-accept battery), and used it solely to check for findings I
might have missed — which is how findings 1 and 2 above were surfaced. Per this review's own stated
discipline, I did not take either finding on the other report's word: both were independently
re-derived against the real subject file via a fresh script that imports only the subject module,
with full traceback text captured directly in this session (see findings 1 and 2's evidence
blocks). I also noticed a `gates/_tmp_strict_probe_r6.py` process running at review time and a
`ref/_tmp_bs2a_r6.py` file with a newer mtime than the subject and this brief, consistent with a
round-6 dispatch already underway elsewhere; I did not read, execute, or rely on either, and they
do not affect anything in this report. No collision on this report's own output path,
`BS2A_CODE_GATE_CODEX_R5.md`, is expected.

## Testimony and constraints

The following are asserted from direct code reading / a bounded manual reconstruction rather than
an executed reproduction against the live production dataset, disclosed per the brief's
instruction:

- `main()`'s digest-mismatch and non-regular-file error paths (Section "`main()`/`--emit` surface
  probes" above) were exercised against *throwaway copies* of the acquire CSVs under `/tmp`, not
  the real `acquire/` directory (which the brief and prior rounds both treat as immutable source
  data not to be corrupted in place) — the underlying `verified_bytes()` mechanism is identical
  code regardless of which directory it points at, so this is a direct reproduction of the real
  code path, just not against the production files.
- The reconstruction of the disclosed pre-dispatch container-guard bug (finding 3's last bullet)
  was built by hand-editing a throwaway copy of the source to revert one specific diff hunk; it
  reproduces the shape the brief describes but is not a claim about what any actual prior
  intermediate version of the file looked like beyond what `git show a03bdd5d3`'s diff already
  documents.
- Findings 1 and 2's cross-corroboration with GPT56's round-5 report (their being found
  independently by a second seat) is reported as a fact about this session's observed process
  environment, not verified beyond reading that report's text once, after completing my own
  battery — the actual defect claims in findings 1 and 2 are independently executed and evidenced
  entirely by commands run in this session against the real subject file, with no dependency on
  that report's correctness.

Everything else in this report was executed in this session: the self-test run, the `--acquire`
run, the independent five-constant recomputation via a script that does not import the subject
(`gates/_tmp_r5_recompute_constants.py`), the exhaustive single- and pairwise-code deletion sweep
against the live 34-control battery (26 singles, 325 pairs, 0 silent — `gates/_tmp_r5_attack.py`),
the real source-level mutation spot-checks for six codes including a full `--self-test` re-run per
mutant, the direct reproduction of every round-3/round-4/round-5 repair claim, the E25/E26/E09
non-laundering tests (`gates/_tmp_r5_attack.py`, `gates/_tmp_r5_attack2.py`), the new false-accept
battery (11 distinct attack shapes, `gates/_tmp_r5_attack.py` Section 3), the independent
reproduction of findings 1 and 2 (`gates/_tmp_r5_verify_gpt56.py`), the `main()`/`--emit` surface
probes, and the claim-boundary review. I did not read `/Users/duhokim/NebulaMindData/`, did not
fetch an image byte, did not emit an acquisition artifact into a tracked location (the one `--emit`
test wrote to `/tmp` and was not retained), and did not modify the reviewed subject or
`successor_ref_v9.py` (both sha256-confirmed unchanged before and after, see Identity section).
This review does not fill BS-2a, authorise a fetch, or resolve conditional independence. BS-2a
remains UNFILLED; one of fifteen class-P slots is filled; BS-6 and the first image byte remain
blocked.

**NOT CLEAR**
