# GPT56 REFEREE REPORT — PREREGISTRATION TEXT V14, ROUND 4

## Verdict

**NOT CLEAR.** The promise can fail in the statistical sense: §5 and the pinned `_decide_from()` both define mutually exclusive REPRODUCED, REJECTED-AT-LONGO-AMPLITUDE, and INCONCLUSIVE regions, and §1 correctly limits what rejection/null would mean. The current text nevertheless cannot be frozen because the Stage-P definition remains openly dual-valued, the new BS-L chronology is self-dependent and placed on the wrong side of freeze, the canonical receipt producer cannot produce the fields its consumer authenticates, and the new blinding exceptions contradict the universal void rule and omit a necessary calibration path. The binding-slot ledger, threshold authority, and even the document's V13/V14 identity are also not single-valued.

## Numbered findings

### 1. BLOCKER — Stage P remains dual-valued, and the openness propagates into the selection promise

**Section / sentence.** §0: “Where prose and code could be read to disagree, the code is the definition.” §2.6: “This text promises the EXACT per-trial test,” while immediately acknowledging that pinned `successor_ref_v9.py` implements the shared-null route and that BS-5p cannot be filled. §4 still describes the shared-reference-null mechanism as the operative Stage-P contract.

**Why it fails as a promise.** This is the acknowledged open blocker, not a repaired one. Stage P determines `L_min_plan`, `L_plan`, the selected footprint and the final re-pass, so the ambiguity is not confined to a power-report footnote: it leaves the experiment's parent geometry dual-defined. The exact receipt is outcome-consistent on the measured reduced set (995/1000), but that cannot choose the rule for a future prefix or branch. Leaving this open does not invalidate §5's decision regions, but it prevents BS-5p, BS-2s and every dependent freeze claim from becoming binding.

**Smallest sufficient repair.** Implement the exact per-trial null route in the normative reference code, pin its trial/permutation counts, addressing, plus-one rule and serialization, add boundary fixtures, rerun the full planning chronology, then repin and freshly gate every artifact whose closure verdict binds the old code digest. Alternatively amend §0 to make one prose specification normative, but do not retain two precedence routes.

### 2. BLOCKER — BS-L is self-dependent and cannot be a freeze prerequisite

**Section / sentence.** §6.1(1): BS-L is “the moment at which every class-P slot holds a receipt” and is itself “sealed by its own signed receipt, BS-L”; §7 places BS-L inside “Class P — freeze prerequisites” and says it is blocked by execution-gate BS-5f. The opening says the document becomes a preregistration only when every class-P slot holds. §7's BS-V row still says “verdict + primary lock,” and §10 still calls BS-V the primary lock.

**Why it fails as a promise.** “Every class-P slot” includes BS-L itself, so BS-L requires its own receipt before its receipt can establish the condition. More importantly, BS-L is blocked by BS-5f, which follows image inference, while all class-P receipts are required before this draft becomes the preregistration governing that execution. An operator must relax either the freeze rule or the lock rule to start. The stale BS-V row supplies a second, contradictory candidate lock after §6.1 says BS-V is not the lock. The V13 repair changed the label but did not make the chronology executable.

**Smallest sufficient repair.** Move BS-L to Class E; define it as attesting all *other* required pre-lock receipts plus BS-5f; make the signed-envelope schema and signer verification normative; and strike “primary lock” from both the BS-V row and §10. State one sequence only: preregistration freeze after all genuine Class-P prerequisites → BS-6/images/inference → BS-2f/BS-8f/BS-5f → BS-L → unblinding → BS-7f/BS-V.

### 3. BLOCKER — the lock/verdict sequence is not receiptable through the pinned canonical producer

**Section / sentence.** §0 makes all digest serializations code-defined. §5 requires a canonical BS-5f receipt bound to the exact mask. §6.1(4) requires the access-log digest to be receipted at BS-2f and BS-L. §7 gives BS-L no code symbol.

**Verified code conflict.** In pinned `successor_ref_v9.py`:

- `SLOT_SCHEMA` has no BS-L or BS-2a entry. `receipt('BS-L', {'anything': b'goes'})` therefore succeeds instead of enforcing the promised lock fields.
- BS-2f's exact schema is only `(brickid, objid, c, accept_flag, bin, boundaries, mask_digest)`; it omits `access_log_digest`, and `receipt()` rejects extra fields for a known slot.
- A canonical BS-5f `receipt()` returns only `slot`, `schema`, `environment`, `body_sha256`, and `envelope_sha256`. It does not return top-level `passed` or `mask_digest`. `run_production_verdict()` requires exactly those top-level values. Appending them after receipt creation leaves `envelope_sha256` unchanged, so the control fields the consumer trusts are outside the authenticated envelope.

**Why it fails as a promise.** There is no conforming end-to-end receipt path. The honest canonical object lacks the fields the consumer reads; a wriggler can append those fields without changing the envelope; BS-L can carry arbitrary fields; and the required BS-2f log digest is schema-forbidden. Thus neither successful execution nor custody is determined by the promise.

**Smallest sufficient repair.** Make canonical receipts carry and authenticate their decoded fields (or make consumers decode and verify the canonical body); recompute the envelope in every consumer; reject post-envelope control fields; add exact schemas for BS-2a and BS-L, including signer identity/signature and access-log digest; add `access_log_digest` to BS-2f; and execute one fixture from BS-2f + BS-8f → BS-5f → BS-L → unblinding → BS-7f → BS-V, with tamper tests at every edge.

### 4. BLOCKER — the universal pre-lock ban and void rule invalidate every newly declared exception

**Section / sentence.** §6.1(2): “No person and no process may decrypt, query, render, summarise or inspect any χ-bearing object or derivative” before BS-5f, BS-L and unblinding. §6.1(3) then permits four blind processes and the hand-check committee to touch/view χ-bearing material before the lock. §6.1(5): “Any pre-lock access voids the run — authorised or not.”

**Why it fails as a promise.** There is no exception clause in (2) or (5). Strict compliance makes the instrument/committee route impossible: the committee's explicitly authorised view is still an authorised pre-lock access, and (5) says that event voids the run. Conversely, an operator who treats (3) as an implicit override has chosen which equally absolute sentence wins. That is outcome-adjacent discretion in the blinding covenant itself.

**Smallest sufficient repair.** Rewrite (2) and (5) to say “except the exact operations enumerated in (3), under their pinned identities, sealed-output restrictions and logged inputs/outputs.” Define any operation outside that closed list, or any listed process emitting outside its sealed schema, as voiding. Add a fixture/receipt proving both one permitted committee read and one permitted automation run do not void, while a one-byte or one-symbol enlargement does.

### 5. BLOCKER — the exception list is neither symbol-pinned nor complete, and committee isolation conflicts with BS-8f production

**Section / sentence.** §6.1(3) says the only four processes are the instrument, cutout producer, Stage-C runner, and acceptance-ledger recompute, and says “each is identified by the pinned code symbol implementing it.” It then says committee members “take no part in filling, adjudicating or locking.” §7 nevertheless names “Hwao + hand-check committee” as BS-8f's producer.

**Verified code/text conflict.** The text gives no exact module/function symbol for any of the four. The pinned reference defines `stage_power()` and `accuracy_from_handcheck()`, but no functions named or bound as the instrument, cutout producer, or acceptance-ledger recompute. More decisively, BS-8f cannot be computed without consuming the committee's χ-derived human labels and instrument-agreement data. `accuracy_from_handcheck()` is the obvious blind aggregation step, but it is not in the four-process exception list. The committee is simultaneously required as a BS-8f producer and forbidden to take part in filling.

**Why it fails as a promise.** The promised “complete set” omits a necessary χ-derived aggregation path and replaces pinned identity with role descriptions. A conforming operator cannot produce BS-8f; a permissive operator can nominate an arbitrary implementation for a listed role. Committee isolation is therefore not real as written: either its members violate the no-filling clause, or Hwao receives/reads material the universal ban withholds from him.

**Smallest sufficient repair.** Publish a closed process-flow table with exact path, function/entry-point, digest, input schema, output schema, principal and access-log event for every pre-lock operation. Add the blind BS-8f aggregation process explicitly. Make the committee label only inside its sealed interface and co-sign an input receipt, not “fill” BS-8f; let a pinned blind aggregator emit only the calibration summary Hwao may receipt. Prove that no raw label, sign, cutout or per-object agreement escapes.

### 6. BLOCKER — the outcome-adjacent confidence threshold has two binding homes

**Section / sentence.** §2.7(2) says exclusion reason (d) uses “the threshold pinned in BS-3”; §2.7(6) says “The numeric confidence threshold” is part of DESIGN slot BS-2a; §2.7(7) again says the thresholds in (d) are pinned in BS-3. The §7 BS-2a row again assigns it the numeric confidence threshold, while BS-3 separately carries instrument identity and τ.

**Why it fails as a promise.** Acceptance changes both signs and geometry. Nothing states that BS-2a's value and BS-3's τ are identical, which receipt wins, or that either blocks the other. A later operator can satisfy both slots with different values and choose the one favourable to the realised accepted mask. This is precisely the researcher degree of freedom §2.7 was added to remove.

**Smallest sufficient repair.** Give the threshold one authority and one slot. If BS-3 owns τ, make BS-2a bind its exclusion predicate to BS-3's exact digest and add an equality check/dependency; if BS-2a owns it, remove every BS-3 threshold reference and make the instrument receipt consume the BS-2a digest. Add a mismatch-refusal fixture.

### 7. BLOCKER — the slot ledger understates incompleteness and contradicts its own DESIGN/VALUE classes

**Section / sentence.** §7 says “One of twelve class-P slots is filled” and calls “BS-2f, BS-5p, BS-8p and BS-9” DESIGN slots. The actual Class-P table has 14 rows, only BS-2m filled, so 13 are unfilled. The same section marks BS-2a as DESIGN/Class P, while §2.7 and the Class-E table call BS-2f a value-only realised partition.

**Why it fails as a promise.** Slot class controls whether a new text and fresh text gate are required or whether a value can be inserted mechanically. A future operator can quote the summary to treat BS-2f as a DESIGN revision, quote §2.7 to treat it as value-only, and omit BS-2a from the declared design count. The false 1/12 status makes the document read materially more complete than its own operative table. Moving BS-L as Finding 2 requires another recount, not preserving either number.

**Smallest sufficient repair.** Generate the status sentence from the authoritative table after correcting BS-L. List every DESIGN slot (including BS-2a and excluding value-only BS-2f unless its status is intentionally changed), give filled/unfilled counts, and make each row carry exactly one class and one revision policy.

### 8. BLOCKER — the artifact called V14 identifies itself as V13 and leaves V14 in the future

**Section / sentence.** The filename is `PREREG_SUCCESSOR_DRAFT_V14_20260827.md`, but line 1 says “PREREGISTRATION DRAFT V13”; the opening says “V13 repairs…” and that anything from KIMI “folds into V14.” Later it contains a “V14 CORRECTION.” §10's repair trace stops at V10 and still calls BS-V the primary lock.

**Why it fails as a promise.** A preregistration's value depends on an unambiguous immutable subject. A signer, gate or later auditor cannot tell whether a signature on “V14” binds the bytes self-declared as V13, or whether a still-future V14 was contemplated. This is not cosmetic version prose when any post-read amendment voids the run.

**Smallest sufficient repair.** Give these exact bytes one version everywhere: title, opening status, supersession sentence, repair trace, freeze record and signature payload. State the prior digest and this candidate digest in the gate/freeze record; remove future-tense “folds into V14” language from V14 itself.

## Researcher-degrees-of-freedom audit

- **Closed in the promise:** the claim axis/amplitude/sign; parent accounting identity; closed exclusion-reason vocabulary; the final p/band/floor decision regions; permutation count and tie direction for the production verdict; and the four named output categories.
- **Still open but declared as prerequisites:** release branch; photo-z provenance; confidence/retry semantics; clean-room specification; BS-9 input path; hand-check plan; authorization; and all Class-E measured values. These are acceptable only if their DESIGN/VALUE classes and authorities are repaired before freeze.
- **Improperly open:** Stage-P algorithm/precedence (Finding 1), BS-L/BS-V chronology (Finding 2), unauthenticated receipt control fields (Finding 3), exception precedence and process identity (Findings 4–5), and confidence-threshold authority (Finding 6).
- **Circularity:** I found no additional data-judges-itself cycle in the §4 Clopper–Pearson boundary or §5 decision bands once the calibration inputs are genuinely pre-unblinding and frozen. The present BS-L self-dependency is an executable cycle, not a statistical one.

## Verified artifact and number checks

- Recomputed sha256: `successor_ref_v9.py = 6a9abbbd900d…`, `closure_worker_v9.py = 28f8e1f9a8c7…`, `FIXTURES_V9_20260826.out = fab32ba24ced…`, and `CLOSURE_V9_KIMI.md = f2ee062bb7f1…`; these match §0/the freeze record.
- Parsed `STAGEP_EXACT_RECEIPT_20260826.json`: 1,000 trial p-values; 995 are `< 0.001`; 951 equal the `1/20001` floor; geometry is 6,445 bricks, n=53,005, Var(c)=0.7546638985, N_eq=120002.8798. These match §2.6 to stated rounding.
- The corrected geometry receipt contains 366,912 = 270,577 + 96,335, total 832,393, selected 6,445, raw 65,060, retained 53,005, and the appended exact Stage-P result 995/1000. The earlier 6,446/997 entries remain historical but are explicitly corrected/retracted later in that same receipt.
- `12,117 × 12.2 MB = 147.8274 GB` in decimal units, supporting “≈147.8 GB.”
- The fixture transcript ends `ALL FIXTURES PASS`; I did not rerun the expensive environment-pinned battery.
- `_decide_from()` matches §5's strict inequalities: reproduced at p<0.001; rejected only at p>0.05 with the Longo-amplitude exclusion band; every other numeric result is inconclusive.

## Testimony / not independently verified

The Longo source quotation and bibliographic anchors were not re-fetched in this pass. I did not rerun the 431-second exact Stage-P harness, the 34-probe closure suite, real parent/closure enumeration, provider-refusal history, claimed three-way independent reproduction, predecessor transport, or the clean-room equivalence batteries; those remain testimony here except for their on-disk hashes and receipt contents. I did not inspect any image, χ value, sealed store, credential, key or authorization file. The finding that process identities are unbound is about what this text and pinned code fail to name; it is not testimony that no external implementation exists.

Blocking findings: 1 (open Stage P), 2 (BS-L cycle/class), 3 (receipt incompatibility), 4 (exception/void contradiction), 5 (incomplete unpinned exception path), 6 (dual threshold authority), 7 (binding-slot class/count conflict), and 8 (version identity).

**NOT CLEAR**
