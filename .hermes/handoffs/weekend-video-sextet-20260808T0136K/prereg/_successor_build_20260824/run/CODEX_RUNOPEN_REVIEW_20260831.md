# CODEX run-open review — 2026-08-31

## 1. Blind-double operation-set derivation

I derived this set from the frozen §6.1 table only, before comparing any staged operation-set result.

Extraction rule: take every primitive store effect expressly permitted in the `may touch (read → write)` cell of Rows A, B, C, C2, D, D2, E, F, G, H, I, J, L, and Q; retain only effects that a requesting row performs through Row B; discard workflow verbs that do not themselves touch a mediated store (`creates`, `computes`, `signs`, `opens`, `halts`, `verifies`), Row B's own event-accounting verbs, and reads of external release/source bytes. Normalize ordinary byte effects to `READ` or `WRITE`, qualify them by the store because the frozen text requires one log across distinct stores and `(row, operation)` must remain unambiguous, and keep human display conveyance as its own primitive because Row G says cutouts are “rendered through the sealed interface,” while the frozen text separately requires every render to be its own committed touch. Provisioning-time metadata recording in Row A precedes Row B's active interval and therefore is not a Row-B chain request; Row Q's later archive metadata read is.

The resulting closed token set is:

```
MAIN-READ
MAIN-WRITE
COMMITTEE-READ
COMMITTEE-WRITE
ARCHIVE-METADATA-READ
MAIN-RENDER-TO-SEALED-INTERFACE
```

These are tokens, not prose labels. `MAIN-RENDER-TO-SEALED-INTERFACE` is not merged into `MAIN-READ`: the store effect is conveyance into a human display session, and Row G's “any unlogged view” condition makes that distinction operational.

## 2. BS-1 date gate

The coordinator's reading is sound. The disclosed ruling supersedes the draft's trigger enumeration and closes the substantive choice now: “the choice-point is **CLOSED on Branch B by this ruling**.” It does not amend frozen v9. The ruling expressly preserves the executable obligation: “the **branch-invariance requirement is NOT superseded** and stands: BS-1's receipt must still show every §7 downstream artifact produced by the same code path.”

Frozen v9 accepts only two supplied facts. Its docstring says: “`photoz_available` is the receipted result of the pinned availability probe; `resolution_date` is the immutable stamp.” Its guard is literal:

```python
if not photoz_available and d < BRANCH_FALLBACK_DATE:
    raise RuntimeError(
        f"the choice-point cannot close for Branch B before {BRANCH_FALLBACK_DATE}: "
        f"DR11 photo-z may still appear (resolution_date {d})")
```

Accordingly, on 2026-08-31 the truthful pair `(False, "2026-08-31")` refuses. `(False, "2026-09-05")` is the first truthful accepted Branch-B pair if the receipt is emitted on that date. Supplying `True` would falsify the probe; supplying a future date now would falsify the immutable stamp. A principal ruling is neither parameter: nothing in the frozen function accepts a ruling, override, or third input, and the ruling says nothing that changes either receipted fact. Bypassing `resolve_branch` would also abandon the preserved v9/branch-invariance path rather than constitute a third path within it. Thus the substance may govern preparatory intent now, while the literal BS-1 receipt waits until 2026-09-05.

## 3. Run-plan and staging findings

F1. **The staged mediator does not cover the frozen three-store custody surface and does not enforce exclusivity.** Frozen §6.1 says the three sealed stores are “the *main sealed store*,” “the *committee sealed store*,” and “the predecessor archive,” and Row A must “bring[] the predecessor archive under the mediator.” `mediator.json` instead lists `main_sealed`, `receipt`, and `label_sealed`; it contains no predecessor-archive path or identity. Moreover it is a policy JSON beside directly reachable directories, not an installed exclusive access boundary. Clause 4 is decisive: “no holder or run host may possess a raw-store read path outside the pinned mediator; the gate must identify and test that boundary, and inability to enforce it makes BS-2k unfillable.” The current filesystem layout supplies raw paths and no boundary test.

F2. **Key provisioning is incomplete and its trust roots are not bound.** Row A requires “generates, splits and escrows the keys” and the enumeration machinery requires provisioned machine public keys. The script generates two unencrypted, single-file private keys, does not split them, and writes neither public key nor signer identity into `constants.json`, `rosters.json`, `mediator.json`, or `STAGED_seal_state.json`. Listing filenames to stdout is not a receipted binding. The claim “no share leaves it” does not repair the missing split or authenticated public-half binding.

F3. **The proposed Duho seal-state signature would itself trigger Row L's frozen wrong-signature condition.** The script tells Duho to “Sign STAGED_seal_state.json's sha256 under nmpr-p0 (one command, same form as P0).” Row L permits signing the canonical lock digest and exempts exactly two other objects: “the freeze signature (P0) and the canonical opening authorization (P7)”; “No other signature is exempt.” A new P0-key signature over the seal-state JSON is neither exempt object. The seal state needs its schema's authentication path, not an invented third Duho signature.

F4. **The staged seal-state body is schema-incomplete.** Frozen clause 7 says the canonical authenticated seal-state schema binds “archive identity, seal identifier/version, holder-roster digest, checkpoint predecessor digest, and monotonic event/epoch data.” `STAGED_seal_state.json` has no monotonic event or epoch data. Adding `constants_digest` and `mediator_digest` does not supply the missing canonical fields. It also names the archive only as the vague compound string “spin-parity predecessor archive + successor stores,” rather than a uniquely bound predecessor-archive identity.

F5. **The epoch-1 predecessor value is substantively correct, but the staged opening is not schema-conformant.** Frozen item (ii-c) reserves epoch 0 “as the first opening's predecessor,” so epoch 1 with predecessor 0 is the correct opening relation. The exact OPENING schema, however, is `(boot_epoch, monotonic_reading, predecessor_epoch, gap_declaration)`, “nothing else.” The staged object uses `k`, `epoch`, `reading`, `predecessor`, `gap_declared`, and `gap_epochs`. Wrong field names plus two extra fields mean the staged bytes cannot be the canonical opening record. The string encoding of predecessor (`"0"`) is also inconsistent with the schema's bounded decimal integer unless canonical serialization converts it before emission.

F6. **The staged rosters do not implement the ruled roster schema.** The commitment requires the reviewer roster under `(kind, roster_entries)`, count-prefixed and identity-sorted. `rosters.json` instead contains `_rule`, `reviewer_roster`, and `custody_holder_roster`, with no `kind`, no `roster_entries`, and no count-prefixed canonical body. The seal state's `holder_roster_digest` is a hash of ad hoc default-spaced JSON, not the frozen canonical count-prefixed roster encoding. The identities and public key agree with Option A, but their artifact form does not.

F7. **X2 is absent from the object the script proposes to seal.** The commitment requires the closed operation set to be “extracted ... digested, and committed” at provisioning. Neither `constants.json` nor any other staged artifact contains the operation tokens, extraction-tool digest, table-byte digest, or resulting set digest. Yet the script says signing `STAGED_seal_state.json` makes provisioning “DONE.” The run-state checklist itself still marks X2 pending. Signing the current body would therefore close BS-2k before a mandatory committed component exists.

F8. **The plan starts work before BS-1 despite the frozen dependency.** The slot table says BS-1 “blocks everything.” Run-plan step 1 performs BS-2k and starts Row B, while step 2 defers the BS-1 receipt. The statement “Nothing in provisioning consumes the receipt before then” is not the frozen condition; the condition is a dependency edge, not data consumption. The early ruling fixes the branch's substance but, under the coordinator's own sound date-gate reading, does not yet produce the required BS-1 receipt. Therefore run execution cannot begin with BS-2k/Row B before the 2026-09-05 receipt unless a new disclosed ruling expressly supersedes that dependency too.

F9. **The later run sequence reverses the frozen phases and dependencies.** The frozen phase line is “P1 BS-6, first image byte → P2 cutout production ... and instrument inference → P3 BS-2f.” The plan instead puts BS-2f at step 5, BS-3g at step 6, and only then BS-6 imagery and Rows C/C2/D/D2/Row F at step 7. BS-2f depends on the realised partition after complete inference, Row D2 precedes BS-2f, and Row F acts “P3, at BS-2f”; BS-3g is class P and blocks BS-6. A conforming order is: finish all class-P/design blockers including BS-3g; issue BS-6; run C → C2 → D → D2 and E; construct the realised partition; run Row F atomically at BS-2f (including the allocation only once BS-SI/BS-8p prerequisites are satisfied); then G/H/I → BS-8f → J/BS-5f → BS-L and the frozen post-lock sequence.

SEAT: CODEX
VERSION: RUNOPEN-V1
VERDICT: DEFECTIVE
COUNT: 9
F-lines: 1,2,3,4,5,6,7,8,9
