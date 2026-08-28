# BS-2a CODE GATE — GPT56 referee report

Subject: `../ref/bs2a_quality_gate.py`
Digest check: `shasum -a 256` computed by me = `4e205c67d7efc72a0432b8ac4d7ddeb0f6514d01c21f791011eb6427ab2d2c62` — **byte-identical to the digest pinned in the brief**. The file reviewed is the file named.
Standing constraints honored: `successor_ref_v9.py` was not modified (post-hoc `git status` clean on it; its sha unchanged across my work, `6a9abbbd…e148`). `/Users/duhokim/NebulaMindData/` was never read. All fixtures were built in `tempfile` dirs or as `_tmp_*` scripts inside the gates dir. No image byte fetched.

## Executed claims (reproduced by me, not taken from the brief)

- `python3 ref/bs2a_quality_gate.py --self-test` → 7 controls, 0 failures, baseline clean. Confirmed.
- `python3 ref/bs2a_quality_gate.py --acquire acquire` → receipt with `n_parent 65060, n_joined 65060, n_retained 49211, n_excluded 15849`, printed `retained 49,211 of 65,060 (expected 49,211) — MATCH`, exit 0. Confirmed.
- Constants in the file (`T_FLUX_IVAR_R_GT = 8.4000532`, `T_PSFSIZE_R_LT = 1.5699703`, `T_NOBS_R_GE = 3.0`, `QUALITY_SHA256 61214b59…`, `PARENT_SHA256 425a42c3…`, `PARENT_ROWS 65_060`, `EXPECTED_RETAINED 49_211`) were checked against **the V29 document** (PREREG_SUCCESSOR_DRAFT_V29_20260827.md §2.7(7) lines 372–376, Row E line 539, §3 line 464, §6.1): all match. No constant was taken from the brief.

## Findings (numbered, severity, file:line, why it fails, smallest sufficient repair)

**1. MAJOR — `quality_pass` content is never verified, so a receipt passes with χ (or any payload) onboard.**
File: `ref/bs2a_quality_gate.py:250-259` (recompute uses only the three float columns; nothing compares `e["quality_pass"]` to the recomputed value or requires it to be a bool), and `:203` (`evidence_digest` reduces the field to `"1" if e["quality_pass"] else "0"` — truthiness, not content).
Demonstrated: I replaced a passing row's `quality_pass` with a custom truthy object carrying a χ payload (`class Chi: __bool__ → True`). `evidence_digest` over the poisoned evidence is **byte-identical** to the clean digest, and `verify_receipt(untouched receipt, poisoned evidence)` returned `[]` — **ACCEPTED**. Same result with `quality_pass = 1` and with `quality_pass = {"chi": 0.7}` plus an honestly recomputed digest. This is exactly the brief's attack 1: a field that leaks χ and still passes. The `_c_evidence_shape` control only tests χ as an **extra key**; χ smuggled *inside* an existing field is invisible to the whole battery.
Repair: in `verify_receipt`, require `e["quality_pass"] is True or is False` and assert `e["quality_pass"] == quality_pass(e["flux_ivar_r"], e["psfsize_r"], e["nobs_r"])` per row; add a control mutating `quality_pass` content with key-set unchanged.

**2. MAJOR — `verify_receipt` never checks `receipt["n_parent"]` against `PARENT_ROWS`.**
File: `ref/bs2a_quality_gate.py:211-261` (the field is in `RECEIPT_FIELDS` at line 75 but no line of the verifier reads it).
Demonstrated: receipt with `n_parent = 999` (contract parent is 65,060) returned `[]` — **ACCEPTED**. A receipt can assert any parent cardinality it likes; the 65,060 identity is enforced only in `build_evidence` (line 143), not at verification time, so a foreign/short partition's receipt is conforming. The partition the evidence does support is checked (`n_joined`, `n_retained`, sum, digest) — the partition's *parent identity* is not.
Repair: `if receipt["n_parent"] != PARENT_ROWS: bad.append(...)`; add a negative control.

**3. MINOR — malformed evidence rows (missing/renamed column) crash the verifier with `KeyError` instead of producing a refusal.**
File: `ref/bs2a_quality_gate.py:245-251`. The shape loop (245-248) appends a reason but does not `return`; the recompute at 250 then indexes `e["nobs_r"]` and raises. Demonstrated both with a 5-key row and a renamed 6-key row: unhandled `KeyError: 'nobs_r'` regardless of row position. A verifier whose stated contract is "refusals name what failed" (line 82) dies nameless on the most obvious malformed-input class. Not exploitable into an accept (crash ≠ pass), so MINOR not MAJOR.
Repair: `bad.append(...); continue` is not enough — restructure so the recompute only runs on rows that passed the shape check, or `return bad` immediately when any row is malformed.

**4. MINOR — the "exact" join silently canonicalizes keys (`str.strip()`), so byte-distinct keys are equated.**
File: `ref/bs2a_quality_gate.py:128-129` (`tuple(str(row[k]).strip() ...)`).
Demonstrated: parent key `"1"` joined to quality key `" 1 "` and the evidence emitted key `"1"` — the join succeeded where a byte-exact join must refuse or flag. The digest binds the *canonicalized* key, not the source key, so key whitespace mutations in the source CSV are laundered through custody. Low blast radius here because both source files are sha-pinned (a whitespace-mutated source fails `verified_bytes` first), but the join's claimed exactness ("exact set equality", line 136) is not what the code does, and any future un-pinned source inherits the looseness.
Repair: drop `.strip()` (or refuse on `str(row[k]) != str(row[k]).strip()`); add a control with a whitespace-carrying key.

**5. MINOR — negative-control battery covers 7 of the 13 verifier branches; five checks have no proof they can fail.**
File: `ref/bs2a_quality_gate.py:326-334` (`CONTROLS`). Demonstrated by direct mutation: `schema_version`, `parent_source_sha256`, `join_keys`, `n_joined`, and `n_excluded`-only mutations are all rejected by the verifier (they work today), but **no control exercises them** — exactly the vacuity pattern the module's own docstring (lines 34-40) says this file exists to prevent. If any of those branches is ever deleted or no-oped, `self_test()` stays green. The `quality_pass`-content hole (finding 1) survived precisely because no control mutates content at a fixed key-set.
Repair: add the five controls (one line each); add the missing-field crash case from finding 3 as a control asserting a *named refusal* rather than an exception.

## Failed attacks (what I tried that held)

- Real invocation reproduces the contract numbers exactly: 65,060 joined / 49,211 retained / 15,849 excluded, digest-pinned sources, MATCH (see above).
- Join refuses all four constructed violations: duplicate quality row, duplicate parent row (via the parent-count refusal), orphan quality row, orphan parent row — each a named `QualityGateError`, none a silent drop.
- `verified_bytes()` is a real custody boundary: single `os.open` with `O_NOFOLLOW`, `fstat` regular-file check, hash-as-read of the same bytes it returns. Symlink target refused (`OSError` from O_NOFOLLOW), directory refused ("not a regular file"). The read-once pattern matches the v9 custody rule; there is no verify-then-reopen.
- `evidence_digest()` moves on a 1-ulp float mutation, is invariant under row reorder (sorted lines), and binds key whitespace in the evidence. (It does not bind `quality_pass` content — that is finding 1, not a digest defect per se.)
- `n_retained` inflation, evidence-digest forgery, threshold mutation, source-digest swap, extra receipt field, partition non-sum: all rejected, each with a working control.
- The file does not touch `successor_ref_v9.py`: one docstring mention, no import, no open.
- Docstring honesty check (brief attack 6): the docstring claims outcome-blindness w.r.t. unobserved χ and **explicitly disclaims** statistical independence from handedness, including the conditional-on-position question. I found no code path or comment implying the stronger claim. The stronger-claim hunt failed — good.

## Testimony (asserted but not executed)

None. Every claim above was executed; transcripts are from `gates/_tmp_bs2a_battery_gpt56.py`, `_tmp_bs2a_battery2_gpt56.py`, `_tmp_bs2a_battery3_gpt56.py`, and inline probes, all run under the successor-build tree with the pinned-digest file.

## Uncertainties / not inspected

- `evidence_digest()`'s `"|".join(...)` admits a theoretical separator-injection collision on crafted keys (demonstrated: `("1|2","1")` vs `("1","2|1")` digests equal); with the sources sha-pinned this is not reachable from the real inputs, so I record it as an observation, not a finding.
- The `nobs_r >= 3.0` comparison on a `NaN` evidence value fails the predicate (NaN comparisons are False) and the verifier stays consistent; I did not count this as a finding because a NaN row can only bias toward exclusion, but a real schema would refuse non-finite floats explicitly.
- I did not review the acquire CSVs' provenance beyond their pinned digests (out of scope; the digests matched the document).

## Verdict rationale

Findings 1 and 2 are each independently disqualifying for a gate whose entire purpose is "a verifier that can reject a non-conforming receipt": 1 lets χ cross the boundary the receipt schema exists to seal, and 2 lets a receipt assert a parent identity the evidence does not support. Both are demonstrated accepts, not arguments. Repairs are small (each is a few lines plus a control). BS-2a stays UNFILLED; the first image byte stays blocked.

**NOT CLEAR**
