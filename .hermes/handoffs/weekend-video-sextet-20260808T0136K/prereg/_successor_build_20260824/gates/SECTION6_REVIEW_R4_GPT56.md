# §6 FOURTH-PASS REFEREE REPORT — GPT56

## Verdict

The universal access ban remains closed at the normative level, the hand-check committee can complete G → H → I without voiding the run, and the BS-5f → BS-L → unblinding order is no longer self-dependent. The proposed acceptance projection is not, however, outcome-blind by construction. It carries cutout checksums that the same scope calls χ-bearing verification oracles, and it carries an undefined confidence quantity written by the outcome-bearing instrument process. A field-name prohibition does not stop either field from carrying outcome information. The draft also claims a lawful cutout-completion read for row E that row E does not contain, leaves the final unblinding checkpoint without the chain fields and verifier needed to establish finality, omits the automated archive checker from the pinned-symbol inventory, and carries two cross-section classification/inventory contradictions into Part 2. The replacement is not yet a closed executable promise.

## Numbered findings

### 1. BLOCKER — the acceptance-evidence projection is declared outcome-free, not made outcome-free

**Clause / table row at issue.** Scope lines 40–56; rows D and E (lines 92–93); clause 2 (lines 125–131); Part 2 items 5 and 7 (lines 186 and 188); Part 5 item 3 (line 214); current §2.7(3)–(5), especially current lines 311–336.

**Why it fails as a promise.** The split keeps the serialized measurement receipt away from row E, but it does not establish the stronger property the current §2.7 requires. First, the projection contains expected and actual cutout checksums. The scope separately defines every cutout as χ-bearing and defines an opaque digest of χ-bearing bytes as χ-bearing because it is a verification oracle for a guessed outcome (lines 52–55). The cutout is the checksum preimage and is not a non-bearing schema. Calling the projection non-χ-bearing in item (v) therefore directly contradicts the scope's own digest rule. Second, the projection carries “the frozen confidence quantity,” but no exact confidence field/function, sign symmetry, producer boundary, canonical projection schema, authenticator, or verifier is defined. Row D sees the outcome and writes the projection. A schema that forbids fields named `sign` and `amplitude` does not prevent a signed confidence, a confidence whose definition depends on class, or deliberate encoding in any permitted scalar. The only proposed gate language is that BS-2a “proves” the boundary; no mechanism states what it proves or how. Thus the projection is capable of carrying an outcome and the acceptance process is lawfully allowed to receive it at the outcome-adjacent partition step.

**Smallest sufficient repair.** Do not expose cutout digests to row E. Have a pinned in-store integrity verifier compare expected/actual bytes and export only the enumerated pass/fail predicates needed by §2.7. Define and pin the exact confidence-producing function and canonical projection schema; require a sign-symmetry/invariance contract and fixtures that demonstrate the confidence and every exported field are unchanged under the instrument's handedness-reversing transformation. Name the projection authenticator and verifier, make row E accept only that verified schema through a field-restricting interface, and make BS-2a unfillable if any outcome/sign/amplitude field or χ-bearing digest is reachable. If no such confidence construction exists, refuse confidence-based exclusion rather than calling it blind.

### 2. BLOCKER — row E still has no lawful path to consume its χ-bearing cutout-completion authorization

**Clause / table row at issue.** Scope lines 52–56; rows C–E (lines 91–93); Part 3 C4 (line 198); Part 5 item 5 (line 216).

**Why it fails as a promise.** The cutout-completion receipt is expressly χ-bearing and remains in the main store. Row D's read surface now expressly includes it. Row E's read surface, by contrast, says it reads **only** the acceptance-evidence projections and fixed parent lists; nevertheless its authorization column requires the cutout-completion receipt. Part 5 then claims that its authenticated read was added to both D and E. That claim is false of the normative table. An external scheduler or envelope verifier cannot lawfully lift the receipt out because it is χ-bearing, while row E cannot read it under its exact surface. The row can neither verify its stated prerequisite nor legally begin.

**Smallest sufficient repair.** Either add a pinned in-store verifier for the completion receipt to row E's exact surface and state exactly what non-outcome predicate it returns, or remove that receipt from E's authorization and make completeness derivable from the independently fixed parent list plus exactly one authenticated projection per parent. Do not give E raw cutout digests; finding 1 requires the verifier to retain those inside the store.

### 3. BLOCKER — the unblinding receipt names a final checkpoint but does not make finality verifiable

**Clause / table row at issue.** Rows B and O (lines 90 and 103); row P (line 104); clauses 3(c), 4, and 6 (lines 142–157); Part 2 items 3–5 (lines 184–186); Part 5 item 2 (line 213).

**Why it fails as a promise.** Naming the unblinding receipt is real progress, but its stated fields are only the authorization digest, verification result, consumed ceremony identifier, and a “genuinely final access-log checkpoint.” It does not carry the BS-L checkpoint it must extend, the chain segment or authenticated predecessor link, the exact terminal event/ordinal, or a declared terminal condition proving that both-store unsealing completed and no required event was omitted. No exact verifier symbol is named for this receipt: `verify_lock()` verifies the earlier BS-L; row O verifies the opening authorization; row P is merely said to require a receipt. “Final” therefore remains an adjective a producer can attach to an intermediate log head. A receipt containing an authenticated but truncated checkpoint satisfies the listed fields.

**Smallest sufficient repair.** Give the unblinding receipt a canonical authenticated schema that binds the BS-L checkpoint digest, the complete extending chain segment or independently verifiable predecessor chain, both store identities, destination, the ordered terminal events for authorization consumption and both-store unsealing, the exact last event/ordinal, and the terminal chain digest. Name and pin a distinct `verify_unblinding_receipt()` (or equivalent) and require row P to call it; it must refuse a missing event, broken extension, wrong store/destination, nonterminal checkpoint, replay, or absent receipt before any statistic is formed.

### 4. MAJOR — the automation inventory omits the automated archive checker

**Clause / table row at issue.** Row Q (line 105); clause 2 (lines 125–131); clause 7 (lines 159–160); Part 2 item 7 (line 188).

**Why it fails as a promise.** Row Q identifies its actor only as “automated gate inspector.” No code symbol or digest is named, no future slot is assigned to pin one, and the code-side atomic-revision list omits it. Clause 2 says every automation row is identified by a pinned symbol and then inventories existing and future automation without Q. Because Q is the producer of the BS-2f and pre-lock archive checkpoints on which `verify_lock()` relies, an operator must invent the metadata operation and transition serialization at execution time. The archive transition rule is textually specified, but its producer remains unbound.

**Smallest sufficient repair.** Name the archive-inspection/transition-check symbol, canonical metadata input and receipt serialization; assign its code and digest to BS-2k or another class-P DESIGN slot; add it to clause 2 and Part 2's code-side atomic revision; and make BS-2f/BS-L refuse checkpoints not produced under those pinned bytes.

### 5. MAJOR — the closed non-χ-bearing list classifies outcome receipts as non-outcome artifacts

**Clause / table row at issue.** Scope lines 40–51, especially the inclusion of BS-7f and BS-V at lines 45–47; rows P and S (lines 104 and 107); current §7 BS-7f/BS-V rows (current lines 627–628).

**Why it fails as a promise.** The closed list says its authenticated schemas cannot carry a per-object outcome value or a digest of a payload containing one and classifies all listed slot receipts as non-χ-bearing. Yet current BS-7f carries `beta_obs`, `p`, and the permutation-payload digest, while BS-V carries the verdict, amplitude, p, and evaluated floor. These are real-χ derivatives by the scope's first definition, not non-bearing envelopes. Their post-unblinding timing makes them lawful later artifacts, but timing does not make the scope's classification true. The same paragraph says gates and referees receive only the closed non-bearing classes, so the false classification can be used as an information-flow authorization rather than remaining harmless terminology.

**Smallest sufficient repair.** Remove BS-7f and BS-V from the non-χ-bearing class, classify them explicitly as post-unblinding outcome-bearing receipts, and authorize them only through rows P/S after the unblinding receipt and BS-V disclosure boundary. Keep schema authentication separate from outcome classification: a canonical receipt can still be χ-bearing.

### 6. MAJOR — Part 2 preserves a false §7 DESIGN inventory

**Clause / table row at issue.** Part 2 item 3 (line 184) versus current §2.7(6) (current lines 338–343) and current §7 lines 595–607 and 624.

**Why it fails as a promise.** The proposed class count is correct: removing class-P BS-L and adding class-P BS-2k leaves fourteen class-P rows. The DESIGN edit is not. Current §7's prose calls BS-2f a DESIGN slot, while §2.7 and the BS-2f row call it a value-only realised partition produced by BS-2a's frozen code. Part 2 says only to **add** BS-2a and BS-2k to the current DESIGN inventory, so literal application leaves BS-2f in the list and yields six named DESIGN slots even though one is expressly value-only. The proposed count lint checks table rows, not this value/design classification.

**Smallest sufficient repair.** Replace, rather than append to, the DESIGN inventory. The resulting list should omit BS-2f and include BS-2a and BS-2k alongside the still-design slots. Extend the linter to parse each row's VALUE/DESIGN classification and compare it with the prose inventory, not merely the P/E row count.

## Checks that held

1. **Central access attack failed.** The table preamble and clauses 1–2 bind every person and process through unblinding; rows K, L, M, and R carry the same pre-unblinding consequence. No key-holder or powerful-role carve-out reappears.
2. **Committee-path attack failed.** BS-8p/allocation → logged G views → H-only ingestion → χ-bearing label-set receipt retained in the committee store → I aggregation → BS-8f is a complete allowed path. Clause 5 preserves those authorized acts.
3. **BS-5f export attack failed.** The permitted aggregate surface now explicitly includes the bounded BS-5f Stage-C output, and J may emit it for BS-L.
4. **Lock self-dependence attack failed.** BS-L is class E, follows BS-5f, excludes itself from its preconditions, and uses a detached signature over a canonical body.
5. **Opening-authorization replay attack failed at the text-contract level.** Clause 6 binds the lock, stores, destination, ceremony ID, phase, signer, and schema, and row O refuses a consumed ID. Future implementation remains Testimony.
6. **Archive-transition attack failed at the relation level.** Clause 7 defines identity/intact-state equality and BS-2k → BS-2f → BS-L predecessor comparisons. Finding 4 concerns the unpinned producer, not the relation.
7. **Current-document lint passed only for current V15.** It reported 20 rows: 14 class P and 6 class E, with no inconsistencies. It does not integrate this candidate or check field-level information flow, receipt finality, automation-symbol completeness, or VALUE/DESIGN inventory consistency.
8. **Pinned-code reality matches the draft's future-work disclosure.** Current v9 `SLOT_SCHEMA` has neither BS-2a, BS-2k nor BS-L; `recompute_acceptance_ledger`, `verify_lock`, and an unblinding-receipt verifier do not exist. The named existing symbols in rows F, I, J, and P do exist.

## Testimony

Not independently verified: historical outcome-blindness of the redesign; any past or current access to the predecessor archive; archive seal state; enforceability of a future raw-store mediation boundary; committee isolation or memory; existence, authentication, or behavior of the future mediator, cutout/instrument runners, acceptance projection, acceptance recompute, archive checker, opening verifier, unsealing service, lock verifier, replay store, unblinding-receipt verifier, schemas, or integrated fixtures. I did not inspect any image, χ value, sealed-store payload, predecessor archive payload, key, credential, or `/Users/duhokim/NebulaMindData/`.

## Evidence ledger

- Read `BRIEF_SECTION6_REVIEW_R4.md`, then `SECTION6_DRAFT_AGY_R4.md`.
- Cross-checked `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md`, `BRIEF_DRAFT_SECTION6_R4.md`, both R3 referee reports, `tools/prereg_lint.py`, and relevant portions of `ref/successor_ref_v9.py` (`SLOT_SCHEMA`, named symbol inventory, production verdict guard).
- Ran `python3 tools/prereg_lint.py <current V15> --gates <gates>`: exit 0; 20 rows, 14 P / 6 E; no inconsistencies found. This was a current-document check, not an integrated R4 check.
- Ran no data fetch, image read, χ computation, sealed-store operation, or code mutation. The only task artifact written is this report.

**NOT CLEAR**