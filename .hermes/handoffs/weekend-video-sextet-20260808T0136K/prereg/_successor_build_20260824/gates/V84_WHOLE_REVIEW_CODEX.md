# V84 whole-document referee — CODEX

## Verdict

**NOT CLEAR.** The exact V84 subject bytes matched the dispatch digest, but the current on-disk artifacts that V84 makes normative do not match the bytes V84 pins: the lifecycle companion has moved and now contradicts V84 and itself, and the refusal checker has moved while regressing a stated control. Independent attacks also broke the “checked declarations,” found a wrong closed vocabulary in the generated string registry, and defeated cross-run recurrence by omission from the successor-authored predecessor list.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — §6.1 lines 621–633; `LIFECYCLE_GUARANTEE_SPEC.md` lines 34–36, 53–70, 80, 176

**The named lifecycle companion no longer matches V84’s pin, and the live companion is internally half-migrated.** V84 pins `5f4bd2859ba0edd5558410793beb702a42ae34aeae7f9dbdd470c5970a7840e1`; the current file hashes to `6984d62f548f1d37ff1f70f3f80e475c25988c15beec0abb76ec72170b1fcd69`. The lifecycle checker therefore emits blocking L02 and two L03 findings: live G3 says “One TOUCH event per touch” while V84 quotes “One event per touch,” and live N2 is a retired-by-ruling arrival-receipt statement while V84 quotes the former “request ... invisible” non-guarantee.

The current companion is not merely newer; its migration is incomplete on its own bytes. Lines 53–63 introduce a write-ahead ARRIVAL event and say no request can vanish, line 70 retires N2, but line 80 still says W1 is invisible/no binding and safe to re-process, and line 176 still says N2 stands referred and needs the second event class that lines 53–63 just introduced. Because the brief explicitly puts this companion in scope and V84 declares a conflict with it to be a draft defect, the current dependency state cannot support V84.

### F2 — HIGH / REPAIR-REQUIRED — §6.1 line 618; `tools/refusal_vocabulary_check.py` lines 182–190, 299–301

**The refusal checker’s quoted digest is stale, and the live checker now misses the direct contradiction its R03 branch says it guards.** V84 says the checker’s sha256 begins `c448646b955bd220`; the current file hashes to `5ee5967580443f57fffc0f08d32ff62d8ce73abe798cf0cb121fe62a1346325a`, so `prereg_lint.py` emits blocking `checker-digest-stale`.

The byte change is substantive. The former contradiction control for “A refusal reason may describe the OBJECT” was replaced with a narrower `content-derived` regex. In-memory execution of the live `check()` on its clean fixture plus `A refusal reason may describe the OBJECT.` returned no finding; `may encode the OBJECT` also returned no finding. The live self-test still reports 32 controls and zero failures because its own mutation was changed to the narrower phrase. Thus the checker both diverges from V84’s pin and can green-light the exact negation of V84’s governing principle.

### F3 — HIGH / REPAIR-REQUIRED — §6.1 lines 664–678; `ref/gen_string_field_registry.py` lines 21–25, 323–331

**The registry generator is not bound to the draft being reviewed.** It accepts no subject path; it globs every `PREREG_SUCCESSOR_DRAFT_V*.md` and assigns `DRAFT = DRAFTS[-1]`. With V84 still under review and V85 now present in the same directory, importing the current generator selects `PREREG_SUCCESSOR_DRAFT_V85_20260830.md`, not V84. Therefore the only executable that can regenerate V84’s claimed registry can no longer regenerate or check V84 once a successor filename exists. A rerun would write a V85 registry over the shared path, while V84’s lint merely checks the registry header and never executes this generator. This is mutable-path custody at the checker’s subject boundary.

### F4 — HIGH / REPAIR-REQUIRED — §6.1 clause 3(b) line 726; clause 6 line 735; `ref/gen_string_field_registry.py` lines 276–305

**The “checked declarations” do not detect added normative fields.** `crosscheck_declared()` does not extract either clause’s member set and compare it with `OPENAUTH` or `LOCKBODY`; it searches for a hard-coded list of expected phrase fragments. It detects deletion or rewording of an expected fragment, but any additional normative member is invisible.

Two in-memory attacks against the exact V84 text both returned an empty problem list: adding `the audit-session identifier` to Clause 6’s “binds exactly” opening body, and adding `the audit-session digest` to clause 3(b)’s “names exactly, in canonical order” lock body. Neither field exists in the declared sets. This breaks the brief’s claim that the generator fails on a missing or stranger member and leaves the opening/lock body declarations vulnerable to precisely the clause-growth drift the check is meant to prevent.

### F5 — HIGH / REPAIR-REQUIRED — §11 lines 1288–1289, 1308–1322; `ref/STRING_FIELD_REGISTRY.md` line 168; `ref/gen_string_field_registry.py` line 206

**`baseline_verdict` is assigned the wrong closed vocabulary.** The draft defines it as the unperturbed production run verdict and says the field carries the constant γ=0 verdict token when the column is constant, or `PER-DRAW` otherwise. Production verdict tokens are `REPRODUCED-LONGO`, `REJECTED-AT-LONGO-AMPLITUDE`, the named inconclusive outcomes, etc. The generated registry instead constrains `baseline_verdict` to `HELD | FAILED | PER-DRAW`; `HELD` and `FAILED` are the separate `invariance_outcome` vocabulary.

A constant γ=0 production column therefore cannot be encoded in a registry-conforming BS-3g receipt: its real run-verdict token is forbidden, while the two allowed constant tokens describe a different field. This is a wrong classification, not an absent schema, and it defeats the claim that value-domain enforcement makes the twenty-field receipt receiptable.

### F6 — MEDIUM / REPAIR-REQUIRED — §6.1 line 601; `LIFECYCLE_GUARANTEE_SPEC.md` lines 177–179

**Cross-run recurrence is defeatable by omitting the immediately prior preregistration from the successor-authored list.** V84 says the successor’s freeze review reads the listed predecessors and treats a class explained in any listed prior run as recurring. It then identifies honesty of the domain with the statement that each preregistration lists its known predecessors. No artifact, canonical chain, verifier, or freeze rule obligates the next document to list this one.

A successor can list V3-pred, omit V84/this run, and truthfully execute the rule over its declared list; the recurring class is then first-occurrence again and may be `EXPLAINED`. The spec itself leaves cross-run recurrence as a successor duty, but a duty whose subject chooses its own history is customary rather than checkable. The recurrence guard therefore closes only within-run recurrence.

### F7 — MEDIUM / REPAIR-REQUIRED — §6.1 line 610; §11 lines 1224–1225, 1455–1458; `ref/STRING_FIELD_REGISTRY.md` line 170

**`calibration_sha256` has no reproducible preimage encoding.** The field is defined as the digest of `a_b`, `a_lb_b`, and `cov_a` “in canonical order,” and the verifier is told to recompute it, but no dtype, endianness, array shape framing, element ordering, or decimal representation is specified. The unique-JSON rule does not close this: it forbids floats in structured JSON and says real values live in dedicated decimal-ASCII fields, while these real arrays are nested inside the calibration digest preimage and are not dedicated receipt fields.

Two independent implementations can encode the same calibration with different lawful decimal strings or raw array bytes and obtain different digests. “Canonical order” orders objects; it does not canonicalize their bytes. This is a digest-ref to an encoding nobody wrote.

## Failed attacks / checks that held

- The subject sha256 independently matched exactly: `6ec2bc2bdabcd12c4d292d33fce867dcc482a29e4bf874c16545f7105a1c95f6`.
- §7 recount held at 16 class-P / 8 class-E rows; `tools/prereg_counts.py` returned 0.
- The frozen v9 pin held at `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- Independent AST closure held: 112 `Raise` nodes and 112 unique classification rows, exactly 26 CALLER / 59 INTEGRITY / 20 NUMERICAL / 3 PLANNING-INTERNAL / 1 TYPED-OUTCOME / 3 WRAPPER; no site is marked `UNREACHABLE-BY-CONSTRUCTION`. I did not re-derive the parked per-call-site-unit defect.
- `tools/void_registry.py` returned 0 with 54 antecedents and 20 §6.1 rows.
- The unmutated refusal vocabulary check returned 0 and its current self-test returned 0. The finding is the adversarial mutation it does not cover, not a claim that its ordinary run fails.
- The absent `gates/replay_harness.py` is honestly named as REQUIRED/DOES NOT EXIST with an UNSET expected pin and a BS-3g blocker. I did not count that declared blocker as a new finding.
- The three/four BS-3g draw-set and harness blockers remain explicit; I did not attack the draw discipline barred by the brief.

## Evidence and scope

Read in content: `gates/BRIEF_V84_REVIEW.md` first; the exact V84 subject only after its digest matched; the full V84 draft; the live `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `ref/successor_ref_v9.py`; `ref/gain_counterfactual_path.py`; `tools/refusal_vocabulary_check.py`; `tools/lifecycle_derivation_check.py`; and the relevant lint source.

Executed read-only hashes, lint/count/VOID/refusal/lifecycle checks, AST/table closure, and in-memory adversarial mutations. The final full lint run reports 102 findings: 5 blocking and 97 legacy-citation advisories. The five blockers are `checker-digest-stale`, `string-registry-stale`, lifecycle L02, and two lifecycle L03 divergences. The trace command was invoked with a single draft and returned “no consecutive draft pairs found”; I do not use that invocation as evidence about trace closure. No draft, spec, reference, checker, registry, or sibling gate report was modified by this seat; the only intended write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V84
VERDICT: NOT CLEAR
COUNT: 7
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 621–633; lifecycle spec lines 34–36, 53–70, 80, 176 | The live lifecycle companion mismatches V84's pin and is internally half-migrated between N2 and an arrival-event design.
F2 | HIGH | REPAIR-REQUIRED | §6.1 line 618; refusal checker lines 182–190, 299–301 | The checker digest is stale and its live R03 control now accepts an explicit permission to describe the object.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 664–678; registry generator lines 21–25, 323–331 | The generator selects the newest filename, so with V85 present it cannot regenerate or check V84.
F4 | HIGH | REPAIR-REQUIRED | §6.1 clause 3(b) line 726; clause 6 line 735; registry generator lines 276–305 | Added normative opening/lock fields are invisible to the claimed checked-declaration cross-check.
F5 | HIGH | REPAIR-REQUIRED | §11 lines 1288–1289, 1308–1322; string registry line 168 | baseline_verdict is wrongly closed to invariance tokens instead of production verdict tokens.
F6 | MEDIUM | REPAIR-REQUIRED | §6.1 line 601; lifecycle spec lines 177–179 | A successor can omit this run from its self-authored predecessor list and evade cross-run recurrence.
F7 | MEDIUM | REPAIR-REQUIRED | §6.1 line 610; §11 lines 1224–1225, 1455–1458 | calibration_sha256 names canonical order but no canonical byte encoding for its real-valued arrays.
<!-- END FINDINGS-BLOCK -->