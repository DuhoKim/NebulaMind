# CODEX — V71 whole-document adversarial review

**VERDICT: NOT CLEAR.** The required subject SHA-256 matched before the draft was read. The V70 gamma-range and production-permutation repairs are present, and the mechanical checks are green, but the lifecycle repair was not propagated into the draft's own duplicated guarantee block. The new view-session boundary can keep one commit alive across later redisplays. Post-BS-L continuation records have signatures but no authenticated signer/trust root, while explanation artifacts are unrestricted prose protected only by an unenforceable semantic sentence. The BS-3g within-draw repair is contradicted by two surviving scalar-baseline verifier clauses and does not require common random numbers across gamma, so it still cannot separate draw noise from gradient sensitivity.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — The draft still states the V70-broken G2/G3 immediately after claiming derivation from the spec

`LIFECYCLE_GUARANTEE_SPEC.md` lines 31–32 repairs refusal truth and event exhaustiveness: a refusal event truthfully records refusal with no store effect, and every event is exactly one touch's or one refusal's. Draft §6.1 line 621 says the draft is derived from that spec and that a conflict is a defect. But the draft's own guarantee block at lines 622–625 retains the old wording: G2 is true only “of the store effect it records,” and G3 says only “one event per touch.”

Concrete counterexample: Row B commits a false `REFUSED-SCHEMA-NONCONFORMING` event for a conforming write and performs no store effect. The live spec forbids it; the draft's duplicated G2 has no store effect against which to test truth, and its G3 does not require the event to belong to either a touch or refusal. The repair exists in one home and is contradicted in the derived text. Delete the duplicate guarantee block or byte-align it with spec G1–G5/N1–N3.

### F2 — HIGH — REPAIR-REQUIRED — The view-session end condition permits later redisplays under the original commit

The spec defines a VIEW as one render-commit session that ends only when the traversal position advances or the interface clears (`LIFECYCLE_GUARANTEE_SPEC.md` lines 89–96; draft §6.1 line 649). Dwell and magnification remain the same view. That boundary is gameable without violating either named end condition.

Counterexample: render object X under event E1; leave X selected; occlude/minimize the interface or let the display sleep; later restore/wake it. The traversal never advanced and the interface state was never cleared, so the text keeps E1's session alive. Yet X is displayed to the human again after a period in which it was not displayed, with no new render commit. Repeating this yields what any reader calls multiple views while the lifecycle records one. G5's “every render is its own touch” and Row G's “any unlogged view” protection therefore depend on an interface-state convention that does not cover visibility loss/restoration. The session must end on loss of display/visibility (or every restoration must force a fresh committed render), not only on position advance or explicit clear.

### F3 — HIGH — REPAIR-REQUIRED — Continuation signatures have no signer identity or trust anchor

Draft §6.1 line 608 says post-`BS-L` entries and explanations authenticate independently by the enumerator's signature. Line 610's exact entry schema ends with “the enumerator's signature” but carries no signer identity, key identifier, certificate/roster binding, canonical signed body, or trust-root digest. The only keypair provisioning named in Row A is Duho's signing key (§6.1 line 669), not an enumeration signer. The §11 verifier item (lines 1352–1362) recomputes joins and resolves references but does not authenticate a permitted enumerator against a pinned key.

Forge: append a continuation entry joined to a real `(chain_position,event_digest)`, generate an attacker keypair, self-sign the entry and matching explanation, and present that public key as the verification key. The join proves which real event is being discussed; it does not prove who was authorised to disposition it. All stated fields can be satisfied while the attacker discharges the emission. Post-BS-L continuation needs a provisioned signer identity/key, a canonical signed-body definition, and verifier binding to that trust root before “independently authenticated” is true.

### F4 — HIGH — REPAIR-REQUIRED — The non-χ explanation surface is unrestricted prose guarded only by a sentence

The repaired non-χ list admits signed explanation artifacts and says they may describe request/authorisation state but never the object (§6.1 line 656). The entry schema merely makes `explanation_ref` resolve to a signed artifact naming its emission (line 610). `tools/refusal_vocabulary_check.py` R03 checks only that the **draft text** contains the principle and no affirmative contradiction (lines 148–157); it never reads an explanation artifact. The §11 enumeration verifier likewise resolves explanations but specifies no closed explanation schema or executable content predicate (lines 1352–1362).

A conforming leak is therefore easy: an explanation can say, “Authorisation branch BLUE was selected; request denied,” with `BLUE/RED` chosen from a measured sign, or can place an object-derived value in prose, whitespace, or an otherwise unconstrained signed field. It names the joined emission and is signed, so every mechanical clause passes; whether it “describes the object” is left to human interpretation after the leak exists. Calling such content “a violation to be refused” is not a refusal mechanism. Either explanations must remain χ-bearing/inaccessible pre-unblinding, or their exported content must be a closed mechanically checked vocabulary whose legal values cannot encode outcome data.

### F5 — HIGH — REPAIR-REQUIRED — The within-draw repair is contradicted by the surviving scalar-baseline verifier rules

The new rule is explicit: `HELD` iff `verdict(i,j) = verdict(i,0)` for every draw and perturbation; when the gamma-zero column varies, `baseline_verdict` is the literal `PER-DRAW` (§11 lines 1243–1250). But two later normative clauses retain the old rule: lines 1298–1300 say every cell must equal `baseline_verdict`, and verifier clauses (e)/(g) at lines 1321–1322 and 1327–1330 enforce the same scalar comparison.

Counterexample: draw 1 has `INCONCLUSIVE` for every gamma; draw 2 has `REJECTED-AT-LONGO-AMPLITUDE` for every gamma. The new within-draw rule requires `HELD` and stores `baseline_verdict = PER-DRAW`. The later verifier requires every verdict cell to equal the literal `PER-DRAW`, which none does, and therefore requires `FAILED`. Conversely, an implementer following the later clauses cannot implement the repaired rule. `baseline_verdict` is also described at lines 1236–1237 as drawn from the run-outcome token set, which does not include `PER-DRAW`. All scalar-baseline clauses and the field's token domain must be re-derived together.

### F6 — HIGH — REPAIR-REQUIRED — “Within draw” does not bind the random variates across gamma

The draft defines a draw-by-perturbation matrix and a reproducible generator/seed (§11 lines 1225–1232, 1291–1295), but nowhere requires draw `i` to reuse the same underlying uniforms/sign innovations for every gamma `j`. A conforming generator may address independent randomness by `(master_seed,i,j)`. `ref/gain_counterfactual_path.py` does not close this: its mapping API receives `gamma, mask, cal` but no normative draw/coupling object (lines 120–152), and the future mapping/generator remains external.

With independent cell draws, `verdict(i,j)` and `verdict(i,0)` differ from both gradient response and Monte Carlo redraw noise. Then the claimed rationale at lines 1243–1247 is false: the comparison is called “within-draw,” but the two cells are not the same draw in the only sense that cancels draw noise. A null gamma effect can produce `FAILED` solely from independent redraws; a real weak shift can be hidden by the same noise. The preregistration must freeze common-random-number coupling: for each draw index, derive one object-level uniform vector from `(master_seed,i)` and transform that same vector under every gamma, with the verifier replaying that coupling. Reproducibility of independent cells is not noise control.

## Failed attacks / checks that held

- The subject digest held exactly at `7a8e7151e4063e5e77f0910835686ba6fba0aececa6e645429bcd1afda8ea238`, verified before reading.
- The frozen reference held its §0 pin: `ref/successor_ref_v9.py` recomputed to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- `tools/refusal_vocabulary_check.py` recomputed to the draft's cited `a3f64aef6e7b9d2e2e9f70449e320b1430579529f928a13ac67446724d24a422`; V71 returned 0 problems and its self-test returned 20 controls, 0 failures.
- `prereg_lint.py` returned the briefed 97 legacy-citation advisories and 0 blocking findings; none is reported as unresolved.
- `prereg_counts.py` independently returned 16 class-P / 8 class-E with prose agreement.
- `prereg_trace.py --check` returned 70 transitions, 0 problems.
- `void_registry.py --self-test` returned 6 controls, 0 failures.
- `ref/RAISE_SITE_CLASSIFICATION.md` closes arithmetically to 112 raise nodes (25 CALLER + 60 INTEGRITY + 20 NUMERICAL + 3 PLANNING-INTERNAL + 1 TYPED-OUTCOME + 3 WRAPPER). I did not re-find the parked per-raise-versus-call-site defect.
- V70's gamma-range attack is repaired: §11 lines 1182–1188 now reject every manifest point with `|gamma| > gamma_bound` as well as requiring both endpoints, zero, distinctness, and spacing.
- V70's operation-key attack is repaired at text-contract level: §6.1 line 601 requires `operation` to come from a closed BS-2k set fixed at provisioning.
- V70's missing later enumeration hooks are present in both prose and §11: BS-L, opening, BS-7f, BS-V, and disclosure are all named.
- The production permutation address itself held in frozen v9: `run_production_verdict()` calls `perm_record(m, STAGE_REAL, 0, 0, N_PERM)` (`successor_ref_v9.py` lines 1591–1624). The findings above concern the contradictory reduction and coupling of stochastic counterfactual draws, not a re-finding of the V70 2,000-permutation default.
- The continuation `(chain_position,event_digest)` join defeats an orphan/position-only forgery. F3 is specifically the missing authority behind the independent signature.
- I did not count the parked availability-code/object-identity leak, durable pre-verdict state, VOID partition, strata/producer question, BS-3g lifecycle cycle, Row-L signature phase, `require_authorization`, or the known `REFUSED-INTEGRITY-MISMATCH` collision as new findings.

## Evidence and write scope

Content read: `gates/BRIEF_V71_REVIEW.md` first; exact V71 draft after digest verification; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/successor_ref_v9.py` at the randomness and production-verdict paths; `ref/gain_counterfactual_path.py`; `tools/refusal_vocabulary_check.py`; and the prior V70 CODEX report solely to distinguish repairs from re-findings. Commands were read-only. Only this CODEX report was written; the draft and referenced artifacts were not modified.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V71
VERDICT: NOT CLEAR
COUNT: 6
F1 | HIGH | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md §1 lines 31–32; draft §6.1 lines 621–625 | The draft's duplicated G2/G3 still omit refusal truth and event exhaustiveness, contradicting the spec it claims to derive from.
F2 | HIGH | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md §5 lines 89–96; draft §6.1 line 649 | Visibility loss and restoration can create later redisplays while neither named session-ending event fires, keeping one commit alive across multiple views.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 608, 610, 669; §11 lines 1352–1362 | Continuation entries and explanations are signed but bind no signer identity, key, canonical signed body, or provisioned trust root.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 610, 656; tools/refusal_vocabulary_check.py lines 148–157; §11 lines 1352–1362 | Signed free-form explanations can encode object-derived data because the never-the-object principle has no executable content check.
F5 | HIGH | REPAIR-REQUIRED | §11 lines 1236–1250, 1296–1300, 1318–1330 | The repaired within-draw rule and PER-DRAW token are contradicted by two surviving verifier clauses that compare every cell to one scalar baseline.
F6 | HIGH | REPAIR-REQUIRED | §11 lines 1225–1235, 1243–1249, 1291–1295; ref/gain_counterfactual_path.py lines 120–152 | The draw contract does not require common random variates across gamma, so within-draw comparisons remain contaminated by independent redraw noise.
<!-- END FINDINGS-BLOCK -->