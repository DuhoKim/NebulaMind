# BS-2a CODE GATE — CODEX, round 3

Verdict: **NOT CLEAR**. The pinned subject digest matches. `--self-test` genuinely passes (25
controls, 0 failures, 24/24 codes covered) and `--acquire` genuinely reproduces 49,211 of 65,060
with MATCH, both re-run independently in this session. I could not make the verifier accept a
receipt it should reject — every single-code and every pairwise (all 276 combinations) deletion
probe was caught by the rebuilt exact-set control battery, and every round-2 forgery (forged
parent key, foreign all-pass partition, χ nested in thresholds, float/bool counts) is refused as
claimed. `PARENT_KEYSET_SHA256`, `EVIDENCE_SHA256`, and `EXPECTED_RETAINED` all independently
recompute to exactly the frozen literals. However, I *did* succeed at the other half of the
brief's challenge — **making it raise instead of refuse** — via a class of malformed evidence
rows that the round-3 repair did not close. That is a live defect in the shipped file, not a
hypothetical.

## Identity and executed comparison

- Subject: `../ref/bs2a_quality_gate.py`.
- Brief-pinned sha256: `c6fe6930c0ae451555e278ec2617c7ae647bba61d6f6af729030c6af3899d59e`.
- Independently computed sha256 before testing: `c6fe6930c0ae451555e278ec2617c7ae647bba61d6f6af729030c6af3899d59e` (via `shasum -a 256`).
- Independently recomputed sha256 after all probes: `c6fe6930c0ae451555e278ec2617c7ae647bba61d6f6af729030c6af3899d59e`.
- Comparison: **MATCH** — the reviewed bytes are exactly the brief-pinned subject at the sha256 identity level, unchanged by this review.
- `python3 ref/bs2a_quality_gate.py --self-test` exited 0 and printed `self-test: 25 controls, 0 failure(s)`, and `every one of 24 checks is exercised by a control`.
- `python3 ref/bs2a_quality_gate.py --acquire ../acquire` exited 0 and independently printed `n_parent=65060`, `n_joined=65060`, `n_retained=49211`, `n_excluded=15849`, `evidence_sha256=0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca`, and `retained 49,211 of 65,060 (expected 49,211) — MATCH`.
- `successor_ref_v9.py` sha256, before and after this review: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` — unchanged. It is referenced only in a docstring comment at line 6; not imported, not opened, not executed by the subject at any point I found.

## Recomputed frozen constants

All three recomputed independently — via a standalone script that does **not** import
`bs2a_quality_gate.py`, re-implementing the join/predicate/digest logic directly from the
module's docstrings and reading `positions_selected.csv` / `quality_selected.csv` directly —
so as not to trust the module's own arithmetic when checking its own literals:

| constant | literal in file | independently recomputed | match |
|---|---|---|---|
| `PARENT_SHA256` (source pin) | `425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831` | `shasum -a 256 acquire/positions_selected.csv` = same | MATCH |
| `QUALITY_SHA256` (source pin) | `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3` | `shasum -a 256 acquire/quality_selected.csv` = same | MATCH |
| `EXPECTED_RETAINED` | `49_211` | independently joined + predicate-applied count = `49211` | MATCH |
| `PARENT_KEYSET_SHA256` | `550e50a8c6fbea2a72ac93597b8c0fbc6798fc78172a5056f10329d7dde93bd6` | independently recomputed = same | MATCH |
| `EVIDENCE_SHA256` | `0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca` | independently recomputed = same | MATCH |

The trust root holds: `PARENT_SHA256`/`QUALITY_SHA256` are exactly the sha256 of the real
`acquire/` CSVs, the join is total (0 duplicate keys, 0 missing, 0 orphaned on either side), and
all three derived commitments the brief asked me to distrust are exactly what the sources
produce. None of the five is theatre.

## Numbered findings

### 1. HIGH — a malformed (but schema-detectable) evidence row crashes the verifier instead of being refused

- File/lines: `../ref/bs2a_quality_gate.py:401` (`ed = evidence_digest(evidence)`), which calls
  `evidence_digest()` at `262-268`, whose inner `enc()` closure does bare `e["brickid"]`,
  `e["objid"]`, `e["flux_ivar_r"]`, `e["psfsize_r"]`, `e["nobs_r"]`, `e["quality_pass"]` with no
  `.get()` and no try/except.
- Executed attack: starting from the authenticated fixture (`build_evidence()` output, so this
  is a genuine JSON-round-trippable receipt/evidence pair, not a Python-only construction), delete
  a single required key from a single evidence row — e.g. `del ev[0]["flux_ivar_r"]` — and call
  `verify_receipt(rec, ev)` with the receipt otherwise untouched.
- Observed output: **`TypeError: 'flux_ivar_r'` raised as a `KeyError` propagating out of
  `evidence_digest()`**, not returned as a refusal list. Confirmed with a full traceback:
  ```
  File ".../bs2a_quality_gate.py", line 401, in verify_receipt
      ed = evidence_digest(evidence)
  File ".../bs2a_quality_gate.py", line 268, in evidence_digest
  File ".../bs2a_quality_gate.py", line 266, in enc
      repr(float(e["flux_ivar_r"])), ...
  KeyError: 'flux_ivar_r'
  ```
- Why it fails: `verify_receipt()` already computes `off_schema` correctly at line 342
  (`set(e) != set(EVIDENCE_FIELDS)`) — this row *would* be flagged `E09` — and the module's own
  per-row float-cast loop at 350-359 already wraps the same `float(e["flux_ivar_r"])` pattern in
  `try/except (KeyError, TypeError, ValueError)` specifically so a missing/bad value becomes
  `E10` rather than a crash. But `evidence_digest()` is called unconditionally at line 401,
  *after* those two guarded checks have already run and populated `bad`, with no equivalent
  guard, and nothing short-circuits the function before reaching it. So a row that the verifier
  itself would flag as `E09` (and would cleanly catch as `E10` via the guarded loop) instead
  crashes the whole call at the digest step before `bad` is ever returned. This reproduces
  exactly the round-2/round-3 pattern the module's own docstring warns about ("a verifier that
  raises has not refused") — it is the same defect class the module fixed for `E24`
  (non-string join keys) via `_enc()`'s `map(str, parts)` coercion, but that coercion only
  protects against a *wrong-typed* value; it does not protect against an *absent* key, which
  `evidence_digest()`'s bare indexing still crashes on.
- Reproduced for every one of the six evidence-row schema fields individually
  (`brickid`, `objid`, `flux_ivar_r`, `psfsize_r`, `nobs_r`, `quality_pass` all raise `KeyError`
  when deleted from a row and the receipt is verified), and for a row replaced wholesale with a
  non-dict (`None`, a bare string, a list, a tuple — all raise `AttributeError`/`TypeError` at
  line 342's `set(e)` or line 383's `e.get(...)` before even reaching 401, depending which
  field is probed first). All of these are realistic attacker inputs: a truncated/corrupted JSON
  evidence array, or a hand-edited receipt, easily produces a dict missing a key or a row that
  isn't a dict at all, and none of them is rejected — they crash the process.
- Smallest sufficient repair: guard `evidence_digest()`'s `enc()` (and `keyset_digest()`'s
  analogous key encoder) the same way `_enc()` already guards types — with `.get(field)` plus a
  sentinel, or by having `verify_receipt()` short-circuit and return `bad` immediately once
  `off_schema` or a non-dict row is detected (mirroring the existing `missing or extra` early
  return for the receipt-level schema at lines 306-307), rather than falling through into
  digest/key computations that assume every row is well-formed. Add an isolated
  malformed-row control (missing key, non-dict row) asserting the resulting code set does not
  include an uncaught exception.

### 2. Everything round 3 claimed to fix, verified fixed

- **Closed nested `thresholds`** (round-2 finding 1): `type(t) is not dict or set(t) !=
  set(THRESHOLD_FIELDS)` at line 319 catches both an extra key (`chi_net` or any other name) and
  a missing key, refusing `E06` in both directions — reproduced.
- **Membership, not just cardinality** (round-2 finding 2): the forged-parent-key attack
  (`ev[2]["brickid"] = "FORGED_PARENT_MEMBER_NOT_IN_SOURCE"`, evidence digest honestly
  recomputed) is refused `{E20, E23}` — reproduced. The foreign all-pass partition (GPT56's
  round-2 forgery: every row set `quality_pass=True`, counts and digest kept internally
  consistent) is refused `{E12, E22, E23}` — reproduced; `main()` no longer merely prints
  `MISMATCH`, it returns nonzero via the `if bad: return 1` branch, since `E22` fires whenever
  `n_retained != EXPECTED_RETAINED`.
- **Control-isolation defect** (round-2 finding 3, the "silent surviving guard" problem): the
  control declarations now assert the *exact set* of codes, not a substring, and I confirmed
  this holds under exhaustive attack — see the Deletion-probe section below.
- **Float/bool counts** (round-2 finding 4): `type(receipt[f]) is not int` at line 333 rejects
  both `65060.0` and `True` (since `type(True) is bool`, not `int`, so it isn't fooled by
  `bool`'s `int` subclassing) — reproduced `E21` for both.
- **The raise-vs-refuse fixes the brief specifically named** (int `brickid` via `E24`; the
  `missing or extra` structural early return replacing the `bad`-keyed one) both hold under
  direct attack: an int `brickid` is caught by `E24` before any digest call, and deleting a
  required top-level receipt field is caught by `E01` with a clean early return, not a
  `KeyError`.

### 3. E23 does not catch an extra evidence field; E09 does — the brief's claim is correct and E09 is sufficient

- Executed check: added `chi_net` to *every* evidence row (not just one), left
  `evidence_sha256` untouched, and confirmed `evidence_digest(ev) == rec["evidence_sha256"]`
  still holds (`True`) because `evidence_digest()`'s `enc()` reads exactly six named fields and
  ignores anything else present on the dict. `verify_receipt()` on this input returns exactly
  `{E09}` — `E23` is absent, `E09` fires because the per-row loop at line 342 checks
  `set(e) != set(EVIDENCE_FIELDS)` for *every* row (not just the first, per the round-1/round-2
  fix noted in the module's own comment at line 338-341), so an extra field on any row, or all
  rows, is caught. E09 alone is sufficient for this attack class; E23 is not expected to catch
  it and correctly does not.

## Deletion-probe results (exhaustive, this session)

All mutations were performed only on in-memory copies constructed from the fixture returned by
`authenticated_fixture()`/`build_evidence()`; the pinned subject file was never edited on disk
(confirmed unchanged sha256 above).

- **Single-code deletion, all 24 codes**: for each code, filtered `verify_receipt()`'s output to
  drop refusals carrying that code (equivalent to deleting the corresponding `refuse()` call,
  since nothing in the function branches on the *contents* of `bad` besides the structural
  `missing or extra` early return, which none of these deletions touches) and re-ran all 25
  controls. **Every single deletion was caught** — the corresponding control's exact-set
  assertion failed and named the missing code. No orphans.
- **Pairwise deletion, all 276 combinations of 2 codes out of 24**: same method, exhaustively
  over every unordered pair. **All 276 were caught** — none left the control battery green.
  (Run took ~683s; full sweep completed, not sampled.)
- **Targeted high-overlap pairs re-verified by direct construction** (not just filtering):
  `{E20,E23}`, `{E22,E23}`, `{E16,E22}`, `{E13,E14}`, `{E14,E17}`, `{E18,E21}`, `{E12,E22}`,
  `{E12,E23}`, `{E15,E20}`, `{E15,E23}`, `{E11,E16}`, `{E20,E24}`, `{E23,E24}`, `{E10,E23}` — all
  caught, consistent with the exhaustive sweep.
- This directly answers the brief's question 3 ("is any control passing for the wrong reason, or
  expecting a set it does not deserve?"): I found no such control. Every one of the eleven
  multi-code controls (`parent identity wrong`, `retained count inflated`, `joined count wrong`,
  `boolean count field`, `row contradicts predicate`, `non-boolean quality_pass`,
  `non-finite quality value`, `duplicate evidence key`, `forged parent member`,
  `non-string join key`, `foreign all-pass partition`) reproduces its declared exact set when run
  directly against the unmodified subject, and none of them survives either member of its own
  code-pair being independently deleted without failing.

## Other failed attacks

- Threshold-value forgery with correct keys, correct partition sum, and an honestly-recomputed
  `evidence_sha256` (so `E19` passes): refused `{E22, E23}` — the frozen `EVIDENCE_SHA256`
  literal catches a value forgery that a self-consistency check alone would miss.
- `thresholds` with an unrelated extra field name (not `chi_net`): refused `E06`, same as the
  round-2/round-3 `chi_net` case — the closure is genuinely by exact key-set, not a
  name-specific blocklist.
- `thresholds` missing a required field (not just extra): refused `E06`.
- Int `3` supplied for `nobs_r_ge` where the frozen threshold is float `3.0`: **accepted**
  (`3 == 3.0` in Python) — this is expected and consistent with the module's design; threshold
  values are never claimed to be type-checked the way count fields are (`THRESHOLD_FIELDS`
  values are compared with `!=`, and `COUNT_FIELDS` are the only fields with an explicit
  `type(...) is not int` gate at `E21`). Not a finding — flagging only to record it was tried.
- `receipt["thresholds"]` = `None`: refused `E06` (`type(t) is not dict` branch), not a crash.
- `receipt["join_keys"]` = `None`: refused `E08`, not a crash.
- Empty evidence list `[]` with the real receipt: refused `{E06, E16, E17, E19, E20, E23}` (a
  pile of failures, none of them a crash) — `type([]) is dict` is false is irrelevant here since
  `[]` is a valid `list[dict]` of length 0; the receipt's non-zero counts simply mismatch it on
  every axis. Confirms the empty-evidence path does not crash either.
- `main()`'s `MATCH`/`MISMATCH` control flow: read directly (not simulated, since simulating a
  real MISMATCH would require corrupting the frozen source CSVs, which the brief instructs not
  to touch and which are not present under `/Users/duhokim/NebulaMindData/`). The code at
  line 700 (`if bad: return 1`) is unconditional on `bad`'s contents, and `E22` fires whenever
  `n_retained != EXPECTED_RETAINED`, so a genuine MISMATCH in a future contract *would* produce
  `bad` non-empty and `main()` would exit 1 — this is a direct code read, not an executed
  reproduction, and is flagged as such under Testimony below.
- `successor_ref_v9.py`: grepped the subject for the string `successor_ref_v9` — one match, the
  docstring line 6. No `import`, no `open()`, no `Path(...successor_ref_v9...)` construction
  anywhere in the file. sha256 unchanged across the whole session (see Identity section).

## Claim-boundary review

Re-read the module docstring's claims (lines 21-44) against the code. The module states it is
outcome-blind with respect to unobserved χ, explicitly disclaims statistical independence from
handedness, states the handedness-conditional-on-position question is "not established," and
says `E23` matching is "custody, not science." I found no executable path, comment, or variable
name anywhere in the file that asserts or implies anything stronger than these disclaimers — the
claims are consistently scoped throughout.

## Delta vs round 2 (this seat's own prior report)

Round 2 found four defects (nested-thresholds bypass, membership-vs-cardinality, silent
overlapping controls, float/bool counts) — all four are independently reproduced as fixed in
this round, per the numbered items in section 2 above. Round 2 did not find the raise-not-refuse
defect in finding 1 above; that is new in this round, surfaced by trying the specific attack the
brief asked me to try ("try to make it raise rather than refuse").

## A note on execution environment

While running this review I found a separate, already-running background process (shell
dispatcher `gates/_tmp_bs2acode_r3.sh`, launched 2026-08-28 19:11 KST, still running at the time
I wrote this report) independently executing this identical round-3 CODEX brief and targeting
the same output path, `gates/BS2A_CODE_GATE_CODEX.md`. I did not stop it, since killing another
in-flight process's work was outside what this brief authorized. This report was written to the
exact path the current instruction specified; if that other process also writes to the same
path, whichever write lands last wins on disk. The findings above were independently derived and
executed in this session regardless of that process's outcome — flagging the collision so it can
be reconciled deliberately rather than silently overwritten.

## Testimony and constraints

The following two items are asserted from direct code reading rather than an executed
reproduction, disclosed per the brief's instruction:

- `main()`'s `if bad: return 1` producing a nonzero exit on a genuine `MISMATCH` — read from the
  source at lines 697-703, not exercised end-to-end against a real mismatching dataset, since
  doing so would require corrupting the frozen `acquire/` CSVs (outside scope; the brief forbids
  reading `/Users/duhokim/NebulaMindData/` and the review must not modify reviewed sources). The
  underlying mechanism (`E22` firing whenever `n_retained != EXPECTED_RETAINED`, and `bad`'s
  truthiness gating `main()`'s return) was verified directly via `verify_receipt()` calls on
  forged receipts with mismatching `n_retained`, which is the same code path `main()` exercises.
- `successor_ref_v9.py` not being touched — verified by grep and by unchanged sha256 across the
  session; not verified by exhaustively tracing every code path for a dynamic import (none exists
  in the source, and Python has no other implicit-import mechanism that would reach this file).

Everything else in this report was executed in this session: the self-test run, the `--acquire`
run, the independent constant recomputation (via a script that does not import the subject), the
exhaustive single- and pairwise-code deletion sweep (300 total combinations), the direct-forgery
reproductions of all four round-2 defects and their fixes, the raise-not-refuse attack in
finding 1 (reproduced for all six evidence fields and four non-dict row types), the E23/E09
extra-field distinction, and the claim-boundary grep. I did not read
`/Users/duhokim/NebulaMindData/`, did not fetch an image byte, did not emit an acquisition
artifact via `--emit`, and did not modify the reviewed subject or `successor_ref_v9.py`. This
review does not fill BS-2a, authorise a fetch, or resolve conditional independence. BS-2a remains
UNFILLED; one of fifteen class-P slots is filled; BS-6 and the first image byte remain blocked.

**NOT CLEAR**
