# GPT56 — V73 whole-document adversarial review

## Verdict

**NOT CLEAR.** The dispatched draft matched the required SHA-256 before I read it. V73 repairs the literal G/N quotation block on its present bytes, but the repair does not survive the attacks the brief requires. The draft still contradicts the companion lifecycle spec in unlabelled normative prose; the new string registry omits the pre-existing non-χ slot schemas it claims to govern; the lifecycle gate accepts materially truncated invariants and silently disappears when the companion is absent; and the refusal-vocabulary checker still admits an active twelfth code on a line containing an unrelated retirement statement.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — unlabelled retry prose re-authorizes an unlogged render

The companion spec makes the recovery split explicit. `LIFECYCLE_GUARANTEE_SPEC.md:66` permits **conveyance** to re-deliver from its committed buffer without a new event, but says **render: NO re-render without a NEW touch commit (G5)**. Its Row-G analysis repeats the same distinction at lines 116–120: render buffers are not reused; each render re-conveys under its own commit.

V73's unlabelled lifecycle prose broadens that rule again. At draft line 637, the crash-window conclusion is unqualified: **“Delivery retries from the committed buffer without a new event (G3).”** That statement covers the render delivery described by the same paragraph just as naturally as conveyance. Line 641 then collapses the post-commit state to “(reads: delivery from the committed buffer)” rather than preserving the spec's render/conveyance split. This is not cured by line 633's narrower conveyance sentence: the later universal retry sentence reopens the forbidden branch.

Concrete counterexample: a Row-G frame is committed, display delivery is interrupted, and recovery displays the committed buffer again. V73 line 637 calls that a no-new-event delivery retry; spec line 66 and G5 call the redisplay a new render requiring a new touch commit. The two normative objects assign different event counts to the same recovery. This is exactly the material unlabelled lifecycle divergence the checker declares out of scope.

Smallest sufficient repair: qualify every no-new-event retry sentence to **conveyance only**, and state in the crash-window block itself that a render recovery may not redisplay the buffer without a fresh render touch commit.

### F2 — HIGH — REPAIR-REQUIRED — the string registry omits the existing non-χ slot-receipt schemas

V73 lines 586–588 classify the listed `SLOT_SCHEMA` receipts as non-χ-bearing. Lines 663–676 then claim that `ref/STRING_FIELD_REGISTRY.md` enumerates **every string-bearing field** from the schema blocks, and lines 1405–1411 require `receipt_strict()` and every slot verifier to enforce value domains against that registry, with an unclassified field blocking the battery.

The generator does not inspect `SLOT_SCHEMA` at all. `ref/gen_string_field_registry.py:72–86` recognizes only five hand-written prose shapes: the BS-3g “exactly these” block, the access-log parenthesis, the enumeration-entry sentence, `cause`, and three acceptance-projection bits. Frozen `ref/successor_ref_v9.py:185–205` contains 18 slot schemas and 76 unique field names; an independent set comparison found **all 76 absent from the generator's extracted set**. Concrete omitted string-bearing fields include:

- `BS-1.branch`;
- `BS-1b.photoz_product` and `BS-1b.provenance`;
- `BS-4.sign_convention` and `BS-4.verdict`;
- `BS-7p.environment`;
- `BS-V.path` and `BS-V.verdict` (post-unblinding, but still proof that the claimed schema extraction is not what the tool performs).

The failure is exploitable on an in-scope non-χ receipt. I called frozen `v9.receipt()` with the exact BS-1b field set and `provenance = b'objid=12345 outcome=+1 arbitrary prose'`; it accepted and returned a canonical envelope. That is the value-domain hole V73 says the successor layer will close, but `provenance` has no registry row for `receipt_strict()` to enforce. Running the generator on the unmodified V73 bytes reports `fields found 37`, `FORBIDDEN-BY-DEFAULT 0`, `stale 0`, and returns 0.

This is not merely the already-disclosed fact that frozen v9 checks names rather than values. V73's proposed repair source is itself incomplete, so implementing §11 literally would preserve the leak while reporting full registry coverage.

Smallest sufficient repair: derive the slot-field inventory from the actual pinned/successor `SLOT_SCHEMA` objects (or a single canonical schema manifest), union it with the non-slot schemas, classify every resulting field, and add a canary proving that an existing field such as `BS-1b.provenance` cannot disappear from extraction.

### F3 — HIGH — REPAIR-REQUIRED — the “blocking” lifecycle derivation gate has two independent fail-open paths

First, `tools/lifecycle_derivation_check.py:69` accepts a quote when the normalized draft body is merely a **substring** of its labelled spec row (`if nb not in spec_rows[tag]`). That is not the documented verbatim/equality contract. In a read-only in-memory mutation I replaced the complete G2 quotation with only **“G2 — No false event”**, deleting the refusal truth condition and the rule that an undecided permission verdict may carry only `REFUSED-UNCLASSIFIED`. `check()` returned `[]`. G2 remained present, so L04 did not fire. The checker therefore accepts the exact meaning-changing truncation the brief asked to construct.

Second, the lint wiring is optional. `tools/prereg_lint.py:540–549` invokes lifecycle checking only under `if spec.exists():` and has no blocking `else`. The integrated lint self-test returns before this wiring at lines 531–533, and lifecycle checking is absent from `CONTROLS`/`CHECKS_RUN` at lines 439–456. Piping the exact V73 bytes to `prereg_lint.py /dev/stdin` (so the companion was not adjacent) produced the ordinary 97 advisory / 0 blocking result and exited 0; no lifecycle message appeared.

Thus “wired as blocking” is path-dependent: deletion of a load-bearing suffix passes even with the companion present, and absence/mislocation of the companion silently removes the block altogether. The current full quotations do byte-match the current spec, but the claimed predicate is not durable.

Smallest sufficient repair: require normalized equality, not containment; fail closed when the companion cannot be resolved; make the companion an explicit CLI argument or pinned manifest input; and add lint-level canaries for a truncated labelled invariant and a missing companion.

### F4 — MEDIUM — REPAIR-REQUIRED — an unrelated retirement phrase exempts an active twelfth refusal code

`tools/refusal_vocabulary_check.py:121–129` scans each entire line for any retirement word and exempts **every** non-member `REFUSED-*` token on that line when one is present. The parser does not bind the retirement phrase to the token it supposedly retires.

Read-only reproduction against the exact V73 text:

`REFUSED-ZOMBIE remains in force; REFUSED-LOCK-NOT-OPEN is retired.`

After appending that one line in memory, `check()` returned `[]`. `REFUSED-ZOMBIE` is explicitly active, but the unrelated retirement of the known old token causes it to be skipped. The baseline checker and its 21-control self-test both return clean because no control puts an active and a retired token on the same line.

The current V73 bytes do state the intended eleven members; this finding is against the checker V73 cites as protecting that claim. A later edit can activate a twelfth code while preserving a green check.

Smallest sufficient repair: parse retirement assertions per token (or require a canonical retired-token block), reject any non-member occurrence not syntactically bound to its own affirmative retirement statement, and add the mixed-line counterexample as a negative control.

## Failed attacks / held checks

- **Subject identity held.** Before reading the draft, I recomputed `d48c3000aa50d804841f3c170cd660791dc5f3355d7aa682ed33147f6aa3a8ae`, exactly matching the brief.
- **Current literal lifecycle pin and quotes held.** The companion digest is `ca24b6dd994a70b8396f58d8370fa4389a05500b2266402b9de8e3bd44ca8fe3`, matching draft line 623. Independent extraction showed all nine current G1–G6/N1–N3 quote bodies equal their own spec rows. F1 is outside those labels; F3 attacks the predicate rather than claiming current quote drift.
- **Baseline tools held on their stated narrow surfaces.** `prereg_lint.py` exited 0 with 97 advisory and 0 blocking findings; lint self-test reported 8/8 controls firing. Lifecycle check reported 0 problems and 7 controls/0 failures. Refusal check reported 0 problems and 21 controls/0 failures. I did not re-report the 97 ruled legacy citations.
- **Counts and trace held.** `prereg_counts.py` reproduced 16 class P / 8 class E and prose match. `prereg_trace.py` reproduced 72 transitions / 0 problems; all three scope controls passed.
- **VOID name-coverage held at its disclosed strength.** `void_registry.py` reproduced 54 antecedents and its six-control self-test passed. I did not treat name-coverage as semantic coverage and did not re-derive the parked VOID/numerical partition.
- **Frozen reference identity and raise inventory held.** `successor_ref_v9.py` hashes to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` hashes to `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`. Independent AST recount reproduced 112 raises: 68 `RuntimeError`, 39 `ManifestClosureError`, 2 `InconclusiveByPower`, 1 `ValueError`, 1 `InconclusiveByCalibration`, and 1 bare re-raise. The call-site ledger openly remains a lower bound with many `UNJUDGED` paths; I did not re-find the parked per-raise/per-call-site unit defect.
- **BS-3g posture held as unfinished rather than executable.** V73 honestly says the successor schema, strict constructor, producer and verifier are not yet pinned/implemented and blocks receipt emission while required values remain unset. I found no current path that legitimately discharges BS-6 through BS-3g. I did not attack the frozen draw discipline.
- **V42/KIMI correction record held.** `PREREG_TEXT_V11_KIMI.md:224–226` shows F7 is the exact-Stage-P receipt's v7-subject disclosure, while lines 332–347 show F13 says the promise is single-valued exact-per-trial. V73 correctly records that substituting KIMI F7 did not support the dual-valued claim.
- **No new eleven-code object leak was claimed.** I did not re-report the parked membership leak or the parked integrity-mismatch collision. F4 is a distinct parser bypass.

## Evidence ledger and scope

Read in content: `gates/BRIEF_V73_REVIEW.md` first; all 1,433 lines of the exact-hash V73 draft; all of `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; the pinned `SLOT_SCHEMA`/`receipt()` region of `ref/successor_ref_v9.py`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `tools/refusal_vocabulary_check.py`; `tools/lifecycle_derivation_check.py`; `tools/prereg_lint.py`; `tools/prereg_counts.py`; `tools/prereg_trace.py`; `tools/void_registry.py`; and the cited KIMI V11 report region.

Executed read-only: SHA-256 checks; baseline and self-test invocations for lint, lifecycle, refusal, counts, trace and VOID registry; independent AST raise recount; in-memory lifecycle truncation; `/dev/stdin` missing-companion lint; in-memory string extractor/schema set comparison; frozen BS-1b arbitrary-provenance receipt construction; and in-memory mixed active/retired refusal-token mutation. I did not modify the draft, spec, reference code, tools, registry, or any file outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V73
VERDICT: NOT CLEAR
COUNT: 4
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 633–641; lifecycle spec lines 66, 116–120 | Unlabelled delivery-retry prose re-authorizes a no-new-event render contrary to G5.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 586–588, 663–676; §11 lines 1405–1411 | The 37-field registry omits the existing non-χ SLOT_SCHEMA fields, including unconstrained provenance.
F3 | HIGH | REPAIR-REQUIRED | tools/lifecycle_derivation_check.py:69; tools/prereg_lint.py:531–549 | The blocking derivation gate accepts truncated invariant bodies and silently skips when the companion is absent.
F4 | MEDIUM | REPAIR-REQUIRED | tools/refusal_vocabulary_check.py:121–129 | A retirement word for one token exempts an unrelated active twelfth REFUSED-* code on the same line.
<!-- END FINDINGS-BLOCK -->