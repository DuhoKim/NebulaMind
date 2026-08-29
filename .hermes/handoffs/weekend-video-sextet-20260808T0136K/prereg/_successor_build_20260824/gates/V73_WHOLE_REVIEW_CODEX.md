# CODEX — V73 whole-document adversarial review

VERDICT: NOT CLEAR.

The dispatched draft matched the required SHA-256 before I read it. The official lint, lifecycle, refusal-vocabulary, count, and registry-generator runs are green on the present bytes, but the new controls do not establish what V73 says they establish. The string registry omits the actual pinned slot schema; the lifecycle checker accepts materially truncated and non-visible quotations; the production-equal replay pin authenticates a source file while mutable live callables remain substitutable; and three negative/absence controls can be bypassed while still exiting zero. These are contract defects, not objections to the parked draw discipline.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — the registry omits every field in the actual pinned `SLOT_SCHEMA`

V73 §6.1 lines 586–588 class existing slot receipts as non-χ-bearing by their authenticated schemas, and §11 lines 1405–1411 says `receipt_strict()` and every slot verifier validate value domains against `ref/STRING_FIELD_REGISTRY.md`. But the generator at `ref/gen_string_field_registry.py:72–86` reads only five prose patterns from the draft; it never reads the operative `SLOT_SCHEMA` at `ref/successor_ref_v9.py:185–205`.

Independent AST extraction found 18 v9 slots and 76 unique schema fields; all 76 are absent from the 37-row generated registry. Concrete omitted fields include string-bearing or arbitrary-byte-capable fields such as `branch`, `input_fn`, `input_adapter`, `query_sha256`, `schema`, `environment`, and `verdict`. Frozen v9's `field()` accepts arbitrary bytes, so field names alone do not bound their values. The V72 defect therefore survives at the actual schema boundary: either successor validation accepts unregistered payloads, defeating the non-χ claim, or forbidden-by-default rejects every existing slot, making the listed class-P/class-E receipt surface unfillable. A registry generated from selected prose blocks is not a registry of the operative schemas.

Required repair: mechanically enumerate the pinned v9 `SLOT_SCHEMA` plus every successor-layer schema and every declared non-slot non-χ schema, classify every resulting field, and make both omissions and stale classifications blocking.

### F2 — HIGH / REPAIR-REQUIRED — the lifecycle checker accepts truncated and non-visible invariant “quotes”

`tools/lifecycle_derivation_check.py:42–45,55–73` searches raw Markdown. It uses the first matching pin anywhere, including comments/history; it extracts labelled fragments without excluding HTML comments; and line 69 accepts `nb in spec_rows[tag]` rather than equality with the complete row body.

An in-memory attack against the exact V73 bytes replaced the complete G2 quotation at draft line 625 with only:

`**G2 — No false event**`

The mutation removed the refusal-event truth rule, the undecided-permission restriction, and the requirement that a specific reason actually be established. The checker still returned `[]`. Equivalent attacks hiding the complete quote or the correct pin in an HTML comment also returned clean. L04 only proves that a tag-shaped fragment exists; it does not prove that the visible complete invariant survives.

This directly falsifies the draft's line-622 claim that quoted invariant-body divergence and deletion are now a blocking predicate. Require one visible, live, full-row quotation per tag; compare normalized bodies by equality; reject duplicates, comments/history, and multiple pins; and add truncation/comment controls.

### F3 — HIGH / REPAIR-REQUIRED — production-equal replay authenticates source bytes, not the live executed callables

V73 lines 1303–1314 requires an in-process assertion that the imported `successor_ref_v9` hashes to `6a9abbbd…`. The wrapper imports an ordinary mutable module object at `ref/gain_counterfactual_path.py:49–50`, then dynamically resolves `v9.perm_record` and `v9._decide_from` at lines 137–143.

I rebound `g.v9.perm_record` in memory to a fake callable. Before and after rebinding, hashing `Path(g.v9.__file__).read_bytes()` returned the required `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`, while the live callable returned the forged result. Thus every file pin can pass while replay executes substituted code. The new in-process file-hash assertion closes import-path drift but not mutable-module drift.

Required repair: execute replay in a fresh isolated process that imports only after verifying immutable bytes, prohibit import hooks/monkeypatch state, and bind or attest the actual live callable code objects before every replay path. A source-file digest is not a digest of Python runtime state.

### F4 — MEDIUM / REPAIR-REQUIRED — schema-format omission is advisory even though the draft says it is blocking

The generator's event-schema extractor at `ref/gen_string_field_registry.py:77–79` depends on the exact phrase `access log under its BS-2k event schema (...)`. A one-word format drift makes all eight event fields disappear. Because those fields still exist in the hand-written `CONSTRAINTS`, they become `stale` at lines 99–112; the return code at lines 116–118 depends only on newly found-but-unclassified fields, not stale rows.

The exact in-memory mutation produced:

- lost fields: `actor`, `object identity`, `operation`, `refusal reason`, `running chain digest`, `success/refusal`, `table row`, `timestamp`
- `unclassified []`
- `stale_count 8`
- exit formula `0`

That defeats draft lines 668–671 and the brief's claim that the generator is nonzero on omission. Make every stale registry row blocking unless explicitly retired by a separately authenticated schema change, and parse structural schema objects rather than sentence spellings.

### F5 — MEDIUM / REPAIR-REQUIRED — `prereg_lint` silently skips the lifecycle predicate when its companion is absent, and its battery does not canary that predicate

`tools/prereg_lint.py:540–549` invokes the lifecycle check only under `if spec.exists():`; there is no `else` finding. Removing or mislocating the companion therefore converts a required blocking dependency into no check and leaves the draft's internal pin uninterpreted. Separately, `CHECKS_RUN` at lines 455–456 and the self-test path at lines 464–518 omit the lifecycle check entirely. The observed `--self-test` output reported eight controls and zero failures without testing lifecycle wiring.

The current companion exists and its digest matches; that is a failed attack on today's custody, not a defense of the absence path. The lint must fail when a draft carries a lifecycle pin but the companion cannot be opened, and the lint's own negative-control battery must mutate the lifecycle pin/body and assert a blocking result through `prereg_lint`, not only through the helper's standalone self-test.

### F6 — MEDIUM / REPAIR-REQUIRED — an unrelated retirement word exempts an active illegal refusal code

`tools/refusal_vocabulary_check.py:121–131` exempts every nonmember `REFUSED-*` token on a line if any non-negated retirement word appears anywhere on that line. The retirement grammar is not bound to the token being exempted.

Appending this active twelfth member to the exact V73 text returned no problems:

`Active member REFUSED-EVADE; the old rule is retired.`

The existing negation guard does not address cross-clause scope. This defeats R01 while the checker and its self-test remain green. Permit nonmember tokens only in a token-specific affirmative retirement construction, preferably only for names already in the `RETIRED` map, and add the exact cross-clause attack as a positive control.

### F7 — MEDIUM / REPAIR-REQUIRED — current unlabelled lifecycle prose reopens render-buffer reuse

The spec distinguishes the paths exactly: `LIFECYCLE_GUARANTEE_SPEC.md:66` permits re-delivery from the committed buffer for conveyance but requires a new touch commit for every render; lines 116–120 say renders have no buffer reuse. V73's labelled G5/G6 quotations are correct, and line 653 later repeats the no-reuse rule. But unlabelled derived prose at draft lines 633 and 637 says delivery retries from the committed buffer produce no second event, and line 641 broadens the terminal step to “reads: delivery from the committed buffer.” “Reads” includes Row G render reads under the document's own touch definition. Those sentences admit a cached redisplay under the old commit, exactly what G5 forbids.

The derivation checker cannot see this contradiction because it has no `G… —`/`N… —` label. The same paragraph at line 621 also inventories the spec as G1–G5 although the spec now contains G6. Scope every retry/buffer sentence explicitly to machine conveyance and state that render delivery cannot use that path.

## Failed attacks / repairs that held

- Subject SHA-256 matched exactly before reading: `d48c3000aa50d804841f3c170cd660791dc5f3355d7aa682ed33147f6aa3a8ae`.
- Companion spec digest matched the draft pin: `ca24b6dd994a70b8396f58d8370fa4389a05500b2266402b9de8e3bd44ca8fe3`.
- Frozen v9 digest matched: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- `tools/refusal_vocabulary_check.py` digest matched the draft's quoted `29e85d4a38d89c61…`; its real-text run and 21-control self-test were green.
- Official `prereg_lint` exited 0 with 16 class-P / 8 class-E rows and 97 legacy advisories, zero blocking; I did not treat the option-D legacy advisories as unresolved.
- Standalone lifecycle derivation and its seven controls were green on current bytes; deletion of G6, a G6 paraphrase, swapped labels, and an undefined tag were detected. The finding is the still-accepted truncation/comment/absence paths, not a claim that every path is dead.
- AST recount found 112 raises and exactly reconciled the classification table: 25 CALLER, 60 INTEGRITY, 20 NUMERICAL, 3 PLANNING-INTERNAL, 1 TYPED-OUTCOME, 3 WRAPPER. I did not re-find the parked per-call-site-unit defect or the parked L963/L973/L986 question.
- The eleven-code vocabulary itself is present, and the current draft contains no active twelfth code outside the adversarial mutation.
- Entry↔emission requirements state a two-way bijection and continuation entries join by `(chain_position,event_digest)`; I did not find a current-byte orphan that survives those stated checks.
- I did not attack the frozen draw discipline or report the parked availability-code, durable-pre-verdict, strata/producer, VOID partition, integrity-mismatch, BS-3g lifecycle-cycle, or other principal-referred findings.

## Evidence ledger and scope

Read as content: `gates/BRIEF_V73_REVIEW.md`; the exact V73 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `ref/successor_ref_v9.py`; `ref/gain_counterfactual_path.py`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `tools/lifecycle_derivation_check.py`; `tools/prereg_lint.py`; `tools/refusal_vocabulary_check.py`; prior V72 seat reports where needed to avoid re-finding parked material.

Executed: SHA-256 checks; official lint and lint self-test; lifecycle checker and self-test; refusal-vocabulary checker and self-test; AST schema/raise recounts; in-memory mutations for truncation, format drift, retirement scoping, missing companion behavior, and live-module rebinding. No draft bytes or code bytes were changed. The registry generator was invoked once and reproduced the existing registry byte-for-byte; post-run git diff for that path was empty. The only intended content write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V73
VERDICT: NOT CLEAR
COUNT: 7
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 586–588; §11 lines 1405–1411 | Registry omits all 76 fields in the operative v9 SLOT_SCHEMA.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 622–632; lifecycle checker lines 42–73 | Checker accepts materially truncated or hidden invariant quotes and pins.
F3 | HIGH | REPAIR-REQUIRED | §11 lines 1303–1314 | Source hash stays pinned while live production callables are rebound.
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 668–671 | Schema-format omission becomes nonblocking stale rows and exits zero.
F5 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 622–632; prereg lint lines 540–549 | Lint silently skips a missing companion and its battery omits lifecycle wiring.
F6 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 591–618 | Unrelated retirement prose exempts an active illegal refusal code.
F7 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 621, 633–641 | Unlabelled retry prose permits render-buffer reuse contrary to G5.
<!-- END FINDINGS-BLOCK -->