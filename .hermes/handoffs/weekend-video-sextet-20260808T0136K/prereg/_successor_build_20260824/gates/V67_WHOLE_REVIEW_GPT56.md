# V67 whole-document adversarial review — GPT56

**VERDICT: NOT CLEAR.** The pinned subject digest matches and the mechanical inventories reproduce, but the central V67 repairs are not executable as written. Resolve–append–release still cannot truthfully bind a write's terminal commit result without an atomic staging/commit contract; the off-log request identifier does not make recovery idempotent; the newly named enumeration verifier has neither an authenticated enumeration schema nor a code-side implementation requirement; recurrence remains defeatable by relabelling; the BS-3g verifier does not enforce the manifest rules or the new grid resolution; and Row F admits a χ-bearing input that no authorised producer creates. Two stale “freeze-time enumeration” statements also directly contradict the new run-time gate.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — resolve–append–release has no atomic write construction that makes the logged outcome true

Section §6.1 lines 619–622 says Row B stages a write, thereby knows its true outcome, appends the sole event, and only then commits the write to the store. But staging success is not commit success. The event schema at lines 586–590 and Row B at line 654 carry success/refusal for the touch, while the actual store touch occurs at the later commit.

Counterexample 1: staging is outside the destination store. Row B validates and stages successfully, appends `success`, then the destination commit fails. The event's claimed outcome is false, and line 626 has no second event in which to record the promised `FAILED` availability code. Counterexample 2: staging writes into a non-transactional destination store. A prefix becomes durable before the append; a crash then leaves committed bytes with no event, worse than the admitted over-report residue. A rename/transaction does not cure this merely by being called staging: its final commit can still fail after the append unless the access-log append and store commit share a specified atomic transaction or recovery protocol.

The text therefore has not established its three universal claims simultaneously: true outcome, no delivered/committed byte unlogged, and exactly one event. It needs a concrete atomicity and recovery contract, not an ordering sentence.

### F2 — HIGH / REPAIR-REQUIRED — an internal request ID outside the event does not make append recovery idempotent

Lines 623–624 add an internal request identifier in Row B's recovery state but expressly omit it from the access log. The document does not define an atomic binding between that identifier and the event append. Line 625 simultaneously says there is no durable pre-verdict state.

Counterexample: request R is assigned an internal ID; its event append becomes durable; Row B crashes before its separate recovery state records that this exact ID owns that event. On restart, repeated touches and legal retries make `(actor,row,operation,object)` non-unique. Reprocessing R produces two events for one request; treating a matching tuple as R can suppress a later legal request. A single serialized writer and lease-loss rule prevent concurrent appenders but do not identify an already-appended request after this crash boundary.

The identifier must be carried in the authenticated event or atomically committed in a durable idempotency index bound to the event digest/chain position. Merely naming an off-log identifier does not make “one request never produces two events” testable after recovery.

### F3 — HIGH / REPAIR-REQUIRED — the enumeration verifier is named but has no authenticated object to verify and no implementation obligation

Lines 599 and 604 require “one entry per emission” and say every catch-all event “carries an enumeration entry.” But the closed access-log event schema at lines 586–590 contains only timestamp, actor, row, operation, object identity, success/refusal, refusal reason and chain digest; it contains no enumeration entry or entry reference. No separate enumeration-entry schema, identity, producer, signature, canonical serialization, join key, or chain-entry type is defined. A whole-document search finds `enumeration verifier` only in lines 603–605, and §11 contains no code-side item requiring its symbol, digest, schema, fixtures or gate wiring.

A nominal verifier can therefore accept an unauthenticated side table, an empty “explained” value, or a summary generated after the fact; there is no canonical byte object against which an independent implementation can reject. `tools/refusal_vocabulary_check.py` does not close this: R08 at lines 155–161 only regex-matches the phrases “enumeration verifier” and “consulted twice.” Its self-test passes those words without any schema or executable dependency.

This is the same named-but-unspecified receipting defect the brief asks the seats to attack. Until the entry format, custody, join, producer, verifier and both gate invocations are specified and required in §11, the P6/P7 block is prose.

### F4 — HIGH / REPAIR-REQUIRED — “same class recurs” has no frozen equivalence rule and is defeated by relabelling

Line 600 stops explanation from discharging “the same class” when it recurs, but nowhere defines class identity or who computes it. Enumeration entries are human “named or explained” (line 599), and F3 shows they have no schema.

Conforming counterexample: the same verifier timeout happens on every run, but each explanation names a formally distinct class — `timeout-row-D-request-17`, `timeout-row-D-request-18`, or “timeout before stage check” versus “stage-check timeout.” Every emitted event is individually enumerated; no byte-defined class repeats; the vocabulary is never re-derived; both consultations pass. The catch-all has become the routine timeout code by relabelling rather than repeated identical prose.

A recurrence rule needs a preregistered, machine-computed equivalence key (at minimum stable failure-site/cause identity independent of object/request/run) and a verifier-enforced recurrence test over prior/current chains. Human naming cannot police human relabelling.

### F5 — HIGH / REPAIR-REQUIRED — BS-3g's verifier accepts manifests that violate the stated grid and never enforces Δγ

The normative prose at lines 1136–1143 requires both endpoints, at least three distinct values, and a maximum grid spacing `Δγ`. The stated verifier at lines 1138–1139 checks only `max|γ| >= gamma_bound` and rejects the singleton `{0}`. Those checks do not imply either endpoint or distinctness: `[0, +gamma_bound, +gamma_bound]` has length three, reaches the bound and is not `{0}`, yet lacks `−gamma_bound` and has only two distinct values. The independent-verifier checklist at lines 1210–1226 recomputes the manifest digest and length but never adds the missing endpoint/distinctness checks.

The V67 repair makes `Δγ` a class-P blocker at line 1143, but `Δγ` is absent from the exact seventeen-field schema at lines 1100–1104 and from every verifier clause. Even after a value is written in prose, a manifest can contain a gap larger than it and still pass every specified machine check. Thus the gate can emit `HELD` with a grid that does not have the claimed resolution.

Add a bounded `delta_gamma` binding (or an unambiguous freeze-body binding), require exact equality to the frozen value, and have the verifier sort/validate finite unique points, require both exact endpoints, require at least three distinct values, and reject every adjacent gap above `Δγ`.

### F6 — HIGH / REPAIR-REQUIRED — Row F's newly admitted χ-bearing stratum index has no authorised producer

Row F now reads the per-object HC stratum index for allocation (line 659), and lines 725–735 define it as machine-committee state × |χ| tertile. But no row produces that index. Row D produces only the primary instrument's χ/sign/amplitude/confidence receipts (line 657); no authorised row runs the “two additional architectures” needed for machine-committee state or writes a stratum-assignment artifact. The frozen reference confirms the gap: `allocate_handcheck(cell_counts, budget)` accepts a caller-supplied 3×9 matrix, while no production function assigns strata; `FINDING_ROW_F_STRATA.md` lines 34–37 records the same source-level fact.

Because the table is exhaustive, an unnamed secondary-classifier/stratum producer is forbidden by Row R. BS-8p cannot silently create it: §7 says BS-8p carries rules, plan and allocation, not a χ-bearing producer/store/schema, and Row F's authorization names only BS-8p and the realised partition. Widening the consumer's surface therefore moved the defect but did not create a legal data path to its input.

Separately, the promised allocation/bin separation is unenforced: `calibration_bins(c)` accepts an untyped numeric array, and Row F now possesses both `c` and a χ-bearing numeric stratum index. No capability split or verifier proves which array reached the call. A producer plus typed/capability-separated interfaces and a recomputation check are required; otherwise the allocation is impossible legally and the “may never reach calibration_bins()” exclusion is only an assertion.

### F7 — LOW / REPAIR-REQUIRED — two operative sentences still require impossible freeze-time enumeration

Lines 597–605 correctly state that freeze-time enumeration is impossible and replace it with checks at BS-L and opening. But line 612 still says the catch-all “freeze-time enumeration surfaces it,” and line 626 says “the freeze-time enumeration required above” keeps undecided permission visible. No such requirement exists above; the document explicitly rejected it nine and twenty-nine lines earlier.

This is not merely history-labelled prose: both sentences describe the live maintenance and terminal-treatment mechanisms. Replace them with the run-time continuous enumeration/verifier language. R06 in `tools/refusal_vocabulary_check.py` misses the contradiction because its regex requires `REFUSED-UNCLASSIFIED` and “enumerated at freeze” within a narrow span; the stale claims use “freeze-time enumeration” farther from the token.

## Failed attacks / checks that held

- Subject identity held: sha256 recomputed before reading as `3dbf4af7fab34e1f58477fffb92fcc4af40a4ceb9ed21d61f8063469f9e7c0e8`.
- The §0 reference pin held: `ref/successor_ref_v9.py` recomputed to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- The checker digest quoted in V67 held exactly: `tools/refusal_vocabulary_check.py` recomputed to `f74040dc8c98b7c3a70c3970006772fd20961c65472d9a782338fc81acf6dcf3`.
- The refusal checker exited 0 on V67 and its self-test reported 15 controls, 0 failures, every code controlled. F3/F4/F7 are attacks on what its phrase-based controls do not establish.
- The eleven formatted refusal codes matched the checker's exact set; I found no twelfth formatted code or revival of a retired code.
- The frozen BS-3g emission blockers remain honestly stated: `n_draws`, `draw_master_seed` and `Δγ` are UNSET and the admissible generator set is empty. I found no present emission path through all blockers. F5 concerns what the eventual verifier would accept after those values are filled.
- V67 correctly narrows `HELD` to “no flip found on the evaluated grid”; I do not re-find V66's universal-invariance overclaim. F5 is the distinct enforcement gap between the stated grid and the verifier.
- The planning classification repair matches `ref/RAISE_SITE_CLASSIFICATION.md`: L963/L973 are CALLER and L986 is PLANNING-INTERNAL; the ledger totals are 25/60/20/1/3/3 = 112.
- Mechanical checks held: `prereg_counts.py` reported 16 class P / 8 class E and prose match; `prereg_trace.py --check` reported 66 transitions and 0 problems; `prereg_lint.py` exited 0 with 97 advisory and 0 blocking findings; `void_registry.py` found 54 antecedents and its self-test reported 6 controls, 0 failures.
- `UNREACHABLE-BY-CONSTRUCTION` remains assigned to no site in `ref/RAISE_SITE_CLASSIFICATION.md`; V67's uses describe the empty category and its falsification rule.
- The V43 in-run rerun allowance remains deleted. I found no retry route after the terminal numerical outcome.
- The numerical VOID antecedents remain Post-unblinding, while forbidden-act, protocol-deviation and digest-deviation remain `Any`.
- KIMI-V11 F7 was checked against `gates/PREREG_TEXT_V11_KIMI.md`: it concerns the exact Stage-P receipt's v7 subject, not the Stage-P implementation claim. V67 correctly records that the V42 substitution was wrong rather than relying on it.

## Evidence ledger and scope

Content read:

- `gates/BRIEF_V67_REVIEW.md`
- `PREREG_SUCCESSOR_DRAFT_V67_20260829.md` (all 1,244 lines)
- `gates/V66_WHOLE_REVIEW_GPT56.md`
- `gates/V66_WHOLE_REVIEW_CODEX.md`
- `ref/RAISE_SITE_CLASSIFICATION.md`
- targeted regions of `ref/successor_ref_v9.py`
- `FINDING_ROW_F_STRATA.md`
- `gates/PREREG_TEXT_V11_KIMI.md` targeted F7/F13 regions
- `/Users/duhokim/NebulaMind/NebulaMind/tools/refusal_vocabulary_check.py`

Commands/checks executed:

- `shasum -a 256` on the subject, pinned reference, raise-site classification and refusal checker.
- `git diff --no-index` for V66→V67.
- refusal-vocabulary live check and self-test.
- prereg counts, lint, trace check, VOID-registry live check and self-test.
- targeted searches for lifecycle identity/commit boundaries, enumeration schema/verifier wiring, recurrence, freeze-time residue, BS-3g grid enforcement, Row-F strata production and calibration function signatures.

I did not modify the draft, reference code, tools, or any file other than this report. Parked findings named by the brief were not re-derived.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V67
VERDICT: NOT CLEAR
COUNT: 7
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 586–590, 619–622, 626, 654 | Staging success cannot establish a write's later commit outcome without an atomic log/store contract, so the sole event may be false or bytes may precede it.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 623–625 | An internal request ID omitted from the event has no atomic event binding, so recovery can duplicate one request or suppress a legal retry.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 599, 603–605; §11; checker lines 155–161 | The enumeration verifier has no authenticated entry schema, producer, join, implementation item or real gate wiring; the checker verifies only phrases.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 599–600 | “Same class recurs” has no frozen equivalence key, so routine catch-all failures can be relabelled into formally distinct classes forever.
F5 | HIGH | REPAIR-REQUIRED | §11 lines 1100–1104, 1136–1143, 1210–1226 | BS-3g's verifier does not enforce both endpoints, distinct points or maximum spacing Δγ, and Δγ is absent from the receipt binding.
F6 | HIGH | REPAIR-REQUIRED | §6.1 line 659; §6.3 lines 725–741; §7 BS-8p; successor_ref_v9.py lines 1359–1378 | Row F admits a χ-bearing stratum index that no authorised producer creates, and no typed boundary keeps it out of calibration_bins().
F7 | LOW | REPAIR-REQUIRED | §6.1 lines 597–605, 612, 626 | Two live clauses still invoke impossible freeze-time enumeration after the mechanism expressly moved to run-time gates.
<!-- END FINDINGS-BLOCK -->