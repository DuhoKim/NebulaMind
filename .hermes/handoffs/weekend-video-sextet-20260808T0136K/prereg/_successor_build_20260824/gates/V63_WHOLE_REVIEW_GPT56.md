# V63 whole-document review — GPT56

## Verdict

**NOT CLEAR.** The dispatched draft matched the required SHA-256 before its first read. The V63 `VOID`/numerical repair does not form a partition: several study artifacts are both computed by the run and verified before the later failure, directly falsifying the claimed exclusivity. One of the three planning sites moved to `CALLER` is an internal iteration-cap failure after feasibility has already been established, not a supplied-argument defect. BS-3g is additionally impossible in lifecycle order, still absent from the pinned schema while §6.1 classifies it as conforming to that schema, and its new stochastic receipt does not define the draw-by-perturbation reduction it asks an independent verifier to reproduce. The suspended refusal vocabulary also remains operative in the normative event-schema sentence and in the referenced checker.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — §5 lines 495–501; §6.1 Rows I/J and Clause 3(c), lines 613–614 and 631–636

The new `VOID`/numerical question is not exclusive. V63 says to ask whether the failing quantity “was PINNED, SEALED OR VERIFIED before this point, or did the run COMPUTE it,” then asserts that a run-computed quantity “was not verified before unblinding.” The lifecycle expressly creates the opposite case.

BS-8f is computed by Row I at P4 (line 613), BS-5f is computed by Row J at P5 (line 614), and Clause 3(c) requires `verify_lock()` to verify the BS-8f calibration and BS-5f PASS before unblinding (line 633). If either authenticated object is later non-finite, degenerate, or digest-altered at P8, it is simultaneously (a) a quantity the run computed and (b) an already-verified object that is no longer what verification certified. BS-2f has the same shape: produced by the run at P3 and later bound into BS-L.

This is not the “derivative of a pinned object” case V63 discusses. The object itself is both computed and subsequently verified. The one-question test therefore returns **both**, so the two clauses still overlap and a precedence/causal inquiry is needed to decide whether the failure is corrupted verified state (`VOID`) or a fresh failed computation (`INCONCLUSIVE-BY-NUMERICAL-FAILURE`). V63’s own falsification test says that means the repair has not landed. The partition must be causal (verification contradiction/protocol deviation versus a fresh operation on intact admissible inputs), not based on mutually false provenance categories.

### F2 — HIGH / REPAIR-REQUIRED — §5 lines 503–504; `ref/RAISE_SITE_CLASSIFICATION.md` lines 79–81; pinned `successor_ref_v9.py` lines 951–1004

L986 is not a caller error under the draft’s own boundary. `local_pass()` reaches L986 only after the caller’s target has already been met: lines 967–973 build an ordered prefix and refuse at L973 if it never reaches `l_plan`; only the complementary `reached=True` branch enters the reduction loop. L986 then raises solely because the algorithm’s internal `moves` counter exceeds frozen `MOVE_CAP = 10_000`.

Thus, if L986 fires, there demonstrably **is** a feasible subset—the prefix already found by the same call—and the failure tests neither the supplied type, shape, field set, nor admissibility of `l_plan`. It tests an internal value computed by the algorithm. A concrete admissible family is an order containing more than 10,000 near-zero-leverage bricks followed by a high-leverage brick: the final brick first makes the prefix feasible, after which more than 10,000 removable low-leverage members can exhaust the cap while feasible subsets continue to exist. Classifying this as “a setup error against a target the caller supplied” is therefore false.

I did not find a path from `run_production_verdict()` to L986, and I do not turn a pre-run planning failure into a run outcome contrary to the principal’s ruling. But “not a run outcome” does not imply “caller violated the contract.” The ledger needs a pre-run internal-planning failure disposition distinct from CALLER, or the planning API must make the cap an explicit caller contract. Moving all three line numbers together hid a materially different third site.

### F3 — HIGH / REPAIR-REQUIRED — §7 lines 754, 769, 779–783; §6.1 phase line 598 and Rows E/I/J lines 609–614; §11 lines 1039–1047, 1073–1089

BS-3g’s new input binding creates an impossible lifecycle cycle. The Class-P BS-3g row says all seven gate components bind **before BS-6** and that BS-3g blocks BS-6. BS-6 is the Class-E approval for the first image byte. But the proposed verifier refuses unless:

- `mask_sha256` equals the `mask_digest` **pinned by BS-2f**; and
- `calibration_sha256` is recomputed from the calibration actually bound (`a_b`, `a_lb_b`, `cov_a`).

BS-2f is a P3 Class-E artifact, produced by Row E only after image production/integrity and complete inference; BS-8f calibration is produced at P4 by Row I after the hand-check path. The phase line is explicit: P1 is BS-6/first image byte, then P2 inference, P3 BS-2f, P4 BS-8f. Consequently a pre-BS-6 verifier cannot read a BS-2f digest or the real BS-8f calibration, while BS-6 cannot open until that verifier accepts BS-3g.

Pre-existing catalogue files may predict the eventual 49,211-row mask, but the written equality is to the authenticated digest **BS-2f pinned**, not to a separately named pre-freeze forecast artifact; likewise “the calibration actually used” cannot exist before the committee measurement. The edge is therefore not merely unfilled—it is unfillable in the stated order. Split a pre-BS-6 design/forecast control from a post-BS-8f realised control, or relocate the dependency without allowing first-image acquisition before the intended gate.

### F4 — HIGH / REPAIR-REQUIRED — §6.1 lines 578–580; §11 lines 1007–1011 and 1018–1104; pinned `successor_ref_v9.py` lines 185–224

V41’s BS-3g addition still only appears receiptable. Section 6.1 currently classifies BS-3g as non-χ-bearing because it is a slot receipt “under the pinned `SLOT_SCHEMA` as conformed by this revision’s code items.” The pinned v9 bytes contain 18 schema entries and no `BS-3g`. Section 11 itself admits “BS-3g (until its entry lands)” is absent and calls the 16-field entry work for the next atomic revision.

I reproduced the consequence against the pinned bytes: `receipt('BS-3g', {'per_object_chi': b'+1'})` returned a canonical-looking envelope with body and envelope digests instead of refusing. No pinned `receipt_strict`, BS-3g producer, or independent BS-3g verifier exists. The field-list prose may specify future work and honestly leaves the slot UNFILLED, but it does not make §6.1’s present-tense **pinned authenticated schema** classification true. Until the entry, strict constructor binding, decoded-field authentication, producer, and verifier are pinned, BS-3g cannot be included in the closed non-χ receipt list and cannot discharge its BS-6 edge.

### F5 — HIGH / REPAIR-REQUIRED — §7 line 769; §11 lines 1024–1032, 1058–1069 and 1073–1087; `ref/gain_counterfactual_path.py` lines 148–169

The four draw fields make a draw set replayable but do not define the answer-changing reduction over it. There are two dimensions: an ordered perturbation manifest of γ values and `n_draws` stochastic sign draws. Yet `draw_verdict_digest` is defined only as a one-dimensional “ordered per-draw verdict sequence,” and clause (e) says the verifier must accept the “worst” reported outcome without defining:

1. whether one draw is reused across all γ values or a separate draw is generated for every `(draw, γ)` cell;
2. the canonical serialization/order of the required draw-by-perturbation verdict matrix;
3. how each draw’s multiple γ verdicts reduce to the single per-draw verdict placed in the digest; or
4. a total order or baseline-relative rule under which categorical `REPRODUCED-LONGO`, `REJECTED-AT-LONGO-AMPLITUDE`, and `INCONCLUSIVE` have a unique “worst.”

The referenced implementation confirms the missing contract. `evaluate_path()` evaluates one mapping realization over a γ list, while `invariance()` asks only whether all resulting categorical verdicts are identical; it has no stochastic draw loop, draw×γ addressing, baseline binding, or worst-case ordering. The claim that the maximum of D draws targets the `D/(D+1)` quantile also presupposes an ordered scalar variate; an unordered/tied verdict category does not acquire that meaning without a defined severity statistic.

Two independent implementers can regenerate the same draws and still produce different digest sequences and opposite `HELD`/`FAILED` reductions while each literally reports its chosen “worst.” Pin the draw×perturbation addressing, full matrix serialization, baseline, and exact fail predicate (for example, any draw at any allowed γ crossing the baseline verdict boundary ⇒ FAILED). A digest authenticates bytes; it cannot supply semantics absent from the contract.

### F6 — HIGH / REPAIR-REQUIRED — §6.1 lines 581–589 and Row B line 605; `tools/refusal_vocabulary_check.py` lines 2–24, 46–65 and 95–118; `PROPOSAL_ACCESS_LOG_REFUSAL_VOCABULARY.md` lines 1–7

The suspension still does not suspend. The normative event-schema sentence says the refusal reason “carries exactly one code from the closed set below and nothing else,” followed by the exact eight codes and the no-catch-all consequence. Later paragraphs say the derivation is withdrawn, the set is suspended/not in force, and no-catch-all must not be carried forward—but line 588 then again says “Every refusal is therefore one of” the old categories. Row B continues to require every refusal to be logged. The draft therefore gives opposite executable instructions and no replacement enum.

The referenced checker remains harder-coded than the prose: `CODES` is the old exact eight, including `REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET`, which V63 says does not survive; R01 rejects any replacement membership; and the docstring says option A has “no escape hatch.” Executed on V63, it exits 1 only with R05 because the obsolete eight strings remain present. Its seven-control self-test passes, proving that it reliably enforces the superseded contract rather than that suspension landed. The superseded proposal itself now states that the old set remains operative in the draft/checker and calls that a live finding.

Demote the old set and no-catch-all text unambiguously to historical quotation, make BS-2k/event-schema filling explicitly blocked, and retire or suspend the membership-enforcing checker until a newly ruled derivation replaces it.

## Failed attacks / repairs that held

- Subject custody held: SHA-256 was exactly `8b224c684ea4cdf067883b4d478e3cdef083118ebf7bc9c205c6ae44979ae376` before the first draft read. The frozen reference and worker pins recomputed exactly to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` and `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.
- Independent AST enumeration found 112 `Raise` nodes. The generated classification table has 112 unique rows with `CALLER 26 / INTEGRITY 60 / NUMERICAL 20 / TYPED-OUTCOME 3 / WRAPPER 3`; `NUMERICAL-PLANNING` and `UNREACHABLE-BY-CONSTRUCTION` are absent. F2 attacks one moved site’s semantics, not the arithmetic closure.
- I found no `run_production_verdict()` path to L963/L973/L986 in the supplied lower-bound callsite graph. The graph reports three planning/fixture paths per site as claimed.
- The measurement-only promotion basis is genuinely dropped. A structural, site-specific subsumption proof is now required, and no site is currently promoted. The falsification route still terminates a wrongly promoted guard in `INCONCLUSIVE-BY-NUMERICAL-FAILURE` and corrects the record.
- Forbidden-act, protocol-deviation, and digest-deviation antecedents remain `Any` phase in §7.1. The V63 narrowing changes only the post-unblinding non-finite/degenerate width. I found no prose return of measurement-only promotion and no reintroduced same-run rerun procedure.
- The Row-L exemption is body-bound for the freeze signature; the opening authorization has a canonical body; and the BS-L detached signature is over the canonical lock digest. I found no new third mandated signature caught by the exemption wording. The separately parked P0/P6/P7 policy question was not re-derived.
- Counts and mechanical checks held at their stated scopes: `prereg_counts.py` returned 16 Class P / 8 Class E; correctly invoked `prereg_trace.py <dir> --check <V63>` returned 62 transitions / 0 problems; `void_registry.py` returned 54 antecedents and 20 §6.1 rows; lint exited 0 with 97 advisory and 0 blocking findings. The permanent legacy-citation advisories were not reported as unresolved.
- The KIMI citation correction is now honest: the draft says F7 does not support the Stage-P claim and identifies F13 as the opposite reading. The defect-register entry accurately records the failed prior substitution.
- `gain_counterfactual_path.py --self-test` passed all nine existing refusal controls and correctly refused to claim its deterministic `_TEST_ONLY_` mapping is the ruled stochastic mapping. F5 concerns the missing new stochastic reduction contract, not those existing path/refusal controls.

## Evidence ledger and scope

Read in content: `gates/BRIEF_V63_REVIEW.md` first; the complete V63 draft only after its hash matched; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; the relevant `successor_ref_v9.py` schema/receipt, planning, calibration, and production regions; `ref/gain_counterfactual_path.py`; `gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`; `OPEN_QUESTION_GAIN_SIGN_MAPPING.md`; `tools/refusal_vocabulary_check.py`; both refusal-vocabulary proposals; and the V59 GPT56/CODEX reports for repair-state control. Executed: SHA-256 checks; AST/table recounts; unknown-slot receipt reproduction; gain-path self-test; refusal checker and self-test; counts, trace, VOID and lint checkers; and targeted byte searches/diffs. I did not read real χ values or `/Users/duhokim/NebulaMindData/`. No draft, reference, checker, proposal, source, or gate file other than this report was modified by this seat.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V63
VERDICT: NOT CLEAR
COUNT: 6
F1 | HIGH | REPAIR-REQUIRED | §5 lines 495–501; §6.1 Rows I/J and Clause 3(c) | Run-produced BS-2f/BS-8f/BS-5f are also verified before unblinding, so the new VOID/numerical question returns both and is not an exclusive partition.
F2 | HIGH | REPAIR-REQUIRED | §5 lines 503–504; raise ledger L986; pinned reference lines 951–1004 | L986 is an internal MOVE_CAP failure after local_pass has already found a feasible prefix, so moving it to CALLER violates the draft’s own supplied-argument boundary.
F3 | HIGH | REPAIR-REQUIRED | §7 BS-3g/BS-6/BS-2f/BS-8f rows; §6.1 phase line; §11 lines 1039–1089 | Pre-BS-6 BS-3g verification requires the later P3 BS-2f mask and P4 BS-8f calibration, creating an unfillable lifecycle cycle.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 578–580; §11 lines 1007–1011 and 1018–1104 | BS-3g remains absent from pinned SLOT_SCHEMA and accepts arbitrary fields through v9.receipt(), contradicting its present classification as a pinned authenticated non-χ receipt.
F5 | HIGH | REPAIR-REQUIRED | §7 BS-3g row; §11 lines 1024–1087 | The draw fields omit the draw×perturbation addressing, matrix serialization, baseline, and categorical worst-case rule, so replayable draws still do not determine one checkable worst outcome.
F6 | HIGH | REPAIR-REQUIRED | §6.1 lines 581–589; Row B; refusal checker lines 2–24, 46–65, 95–118 | The old exact-eight/no-catch-all refusal vocabulary is called suspended but remains normative in the event schema and hard-enforced by the referenced checker.
<!-- END FINDINGS-BLOCK -->