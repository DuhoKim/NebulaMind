# CODEX referee report — preregistration text V14

## Verdict basis

The claim can fail: §5 gives a conjunctive `REPRODUCED-LONGO` region, a distinct `REJECTED-AT-LONGO-AMPLITUDE` region, and an explicit residual `INCONCLUSIVE` region. §1 also correctly limits the interpretation: this is not a test of isotropy, A ≈ 0.02, Shamir, or BHU. The quoted reference-code digests match the files, and the exact Stage-P receipt matches the quoted 995/1000, 6,445 bricks, n = 53,005, Var(c) = 0.754663898..., and N_eq = 120002.8798.... Those parts did not break under my checks.

The text is nevertheless not an executable freeze promise. The V14 lock repair creates a new self-cycle, its receipt remains schema-free in the definitive code, the universal void rule voids the expressly required exceptions, and retrospective blinding of the already-completed redesign is still not established.

## Findings

1. **BLOCKING — BS-L is a member of the set whose completion BS-L itself certifies.**

   **Section / sentence.** §6.1(1), lines 473–488, defines the primary lock as the moment when “every class-P slot holds a receipt” and says BS-L seals that moment. §7, line 607, places **BS-L inside the Class-P table**. Line 29 separately says the text becomes a preregistration only when every class-P slot holds a receipt.

   **Why this fails as a promise.** To issue BS-L, every Class-P receipt must already exist; because BS-L is Class P, that condition includes BS-L. The V13/V14 split therefore moved the old BS-V cycle onto BS-L instead of removing it. The timing is also wrong: BS-L is blocked by post-inference BS-5f, so treating it as a freeze prerequisite makes the “before any real datum/image byte” freeze impossible. An operator must choose which clause to waive.

   **Smallest sufficient repair.** Move BS-L to Class E; define its precondition as all Class-P slots **other than BS-L**, plus BS-5f and the named fixed inputs; and make the initial preregistration freeze depend only on genuine pre-execution Class-P slots and Duho’s freeze signature.

2. **BLOCKING — the new lock has no binding schema in the code, while the old verdict slot still claims to be the lock.**

   **Section / sentence.** §6.1(1) says BS-L must name the key-holder roster, accepted-mask digest, calibration-record digest, decision-input digests, and access-log digest. §0 says code defines all digest serializations and code wins. In `ref/successor_ref_v9.py`, lines 185–205, `SLOT_SCHEMA` has no `BS-L` entry; my literal search found zero occurrences of `"BS-L"`. Worse, `receipt()` lines 208–224 validates a field set only when the slot is already in `SLOT_SCHEMA`, so an unrecognised `BS-L` accepts an arbitrary field set. §7 line 607 names no implementing code symbol. Meanwhile §7 line 628 still defines BS-V as “**verdict + primary lock**,” despite §6.1 repeatedly saying BS-V is not the lock.

   **Why this fails as a promise.** A conforming operator can create a canonical-looking `receipt("BS-L", ...)` that omits the roster or any digest named in prose, then invoke §0’s code precedence. A later operator can also cite the still-binding BS-V table row for a second lock definition. The claimed BS-5f → BS-L → unblinding → BS-V sequence cannot be receipted unambiguously end to end.

   **Smallest sufficient repair.** Add BS-L’s exact field set and validation to the pinned implementation, pin and gate the changed bytes, name its producer symbol in §7, add refusal fixtures for every missing/extra field and wrong dependency, and delete “+ primary lock” from BS-V’s content.

3. **BLOCKING — the universal void rule voids the exceptions required to finish the run.**

   **Section / sentence.** §6.1(2) says no person or process may inspect any χ-bearing object or derivative before BS-L. §6.1(3) then requires four pre-lock automation exceptions and a hand-check committee that views χ-bearing cutouts. But §6.1(5), lines 535–536, says **“Any pre-lock access voids the run — authorised or not”** with no exception. The committee clause also says members “take no part in filling,” while §7 line 625 makes the committee a co-producer of BS-8f.

   **Why this fails as a promise.** The instrument and hand-check work required to produce BS-8f/BS-5f necessarily occurs before BS-L. Under the literal void rule, performing that required work voids the run; not performing it prevents BS-5f and therefore BS-L. The committee simultaneously must and must not help fill BS-8f. Calling §6.1(3) “exceptions” is not enough because (5) expressly includes authorised access.

   **Smallest sufficient repair.** Define a closed set of permitted pre-lock operations, actors, inputs, outputs, and log events; state that only those exact operations do not trigger the void; make every other pre-lock access void the run; and allow committee members to contribute sealed labels/BS-8f only while barring every **other** slot or role.

4. **BLOCKING — the enumerated automation set omits the required calibration computation and does not actually identify all four implementations.**

   **Section / sentence.** §6.1(3), lines 509–520, claims the complete set is the instrument, cutout producer, Stage-C runner, and acceptance-ledger recompute, “each ... identified by the pinned code symbol implementing it.” But §6.2 lines 561–565 requires `accuracy_from_handcheck()` to consume the pre-lock hand-check/instrument agreement information and produce BS-8f; §4 requires BS-8f before Stage C and BS-L. That process is not in the exception list. The cutout producer and instrument are generic descriptions here, not named pinned symbols; §7 gives BS-3 no symbol and leaves BS-9 as an unfilled design.

   **Why this fails as a promise.** Running the mandatory BS-8f computation is forbidden by the universal ban and void rule, while omitting it blocks Stage C. Generic role names also leave open which executable may touch sealed material, the exact researcher/process discretion the exception list is supposed to close.

   **Smallest sufficient repair.** Add the BS-8f calibration producer (and any necessary sealed label-ingest/display process) to the closed exception set, name an exact pinned symbol/digest for every exception, specify its allowed read/write surface, and gate fixtures proving that no other executable can access the store.

5. **BLOCKING — the prerequisite inventory and DESIGN/VALUE classification contradict the operative table.**

   **Section / sentence.** §7 lines 595–600 says the DESIGN slots are “BS-2f, BS-5p, BS-8p and BS-9” and that one of twelve Class-P slots is filled. Yet §2.7 lines 338–343 and §7 line 606 say **BS-2a** is DESIGN and Class P, while §7 line 624 says **BS-2f is value-only and Class E**. I mechanically counted **14 rows** in the current Class-P table, including BS-L, not twelve (and not fifteen).

   **Why this fails as a promise.** DESIGN slots require a new text and fresh gate, whereas VALUE slots allow mechanical filling. Misclassifying BS-2a/BS-2f therefore changes whether an outcome-adjacent acceptance rule can be introduced by receipt or requires a new preregistration. The false count also understates current incompleteness and makes “every class-P slot” an unstable referent.

   **Smallest sufficient repair.** After correcting BS-L’s class, generate one authoritative slot inventory from the table; name BS-2a, BS-5p, BS-8p, and BS-9 as DESIGN if that is the intended set; keep BS-2f explicitly Class-E/value-only; and state the resulting exact total and filled count consistently everywhere.

6. **BLOCKING — the already-completed redesign has no retrospective blinding proof.**

   **Section / sentence.** Lines 23–29 say this draft is not in force. §2.6 says the real geometry/selection was run on 2026-08-25. §6.1(6) offers as proof only that the redesign artifacts contain no χ-derived quantity, and voids the licence if such a quantity is later found in the path.

   **Why this fails as a promise.** A geometry-only artifact proves what was written to the artifact, not what its designers or key holders had already read from the predecessor’s sealed 208,405 measurements. Someone could have seen those outcomes, then produce a byte-perfect geometry-only selection while complying with every prospective V14 access rule (which was not yet in force). No required slot binds the predecessor-store access log, key-holder roster, or attestations over the interval ending at the already-completed selection.

   **Smallest sufficient repair.** Add a Class-P retrospective custody/blinding receipt that identifies every redesign participant and predecessor key holder, binds the predecessor access-log digest from sealing through selection, records all successful/refused access, and requires no relevant outcome access before the geometry artifacts were fixed. Any unlogged interval or relevant read must void reuse of this redesign.

7. **MAJOR — the V14 artifact still identifies and narrates itself as V13.**

   **Section / sentence.** The file named `PREREG_SUCCESSOR_DRAFT_V14_20260827.md` is headed “DRAFT V13.” Its opening blockquote says “V13 repairs...” and says KIMI’s round-3 report had not landed and would fold into V14, even though the body later contains a “V14 CORRECTION.” §7 also labels BS-L “NEW IN V13.”

   **Why this fails as a promise.** Readers outside the room cannot tell from the document’s own identity whether this is the V13 subject, the promised V14 incorporating the missing report, or a partially copied transition. A future signature or citation by version name can bind the wrong represented state even if a digest later disambiguates the bytes.

   **Smallest sufficient repair.** Rename the heading and opening status to V14, replace the obsolete “will fold into V14” chronology with the actual incorporated findings, and retain V13 history only as explicitly historical text.

## Open blocker explicitly carried, not credited as repaired

Stage P remains dual-valued exactly as disclosed: §0 and pinned v9 implement the shared-null route, while §2.6 says the intended promise is exact per-trial nulls in an external harness. This openness does invalidate a freeze of V14 itself: implementing the exact route changes the definitive code digest, requires new fixtures/gates, and produces a new text subject. The exact receipt verifies the measured 995/1000 result, but it does not close the promise.

## Researcher degrees of freedom inventory

- The DR11/DR10.1 branch is open but closed by an objective availability/date rule; Branch A correctly voids the Branch-B pin and forces a fresh text gate.
- BS-1b’s product paths/columns/join keys, BS-2a’s confidence/retry/evidence design, BS-5p’s exact implementation, BS-8p’s hand-check plan, and BS-9’s production input path remain open before data access but are supposed to close through DESIGN gates. Finding 5 must be repaired so none can be misfilled as a value.
- BS-3’s numeric confidence threshold is stated, but the confidence quantity/recompute path remains a BS-2a design obligation.
- The selection has no producer receipt and the production-scale vectorized implementation is not frozen; the text discloses both. They remain prerequisites, not established results.
- Post-inference acceptance, exclusions, ties, and verdict boundaries are otherwise closed in prose: terminal status partition, four exclusion reasons, evidence recomputation, exact p-value inequalities/ties, and a residual inconclusive region are explicit.

## Testimony

- I did not independently re-verify the Longo bibliographic quotation or sign-convention mapping from the publication; those remain testimony for this review.
- I verified the on-disk hashes of `successor_ref_v9.py` and `closure_worker_v9.py` against §0, the KIMI closure-report digest quoted in §0, and the numerical fields of `STAGEP_EXACT_RECEIPT_20260826.json`. I did not rerun the 431-second Stage-P measurement.
- Whether a complete predecessor-store access log or retrospective participant attestations exist elsewhere is not established here. Finding 6 is that V14 does not require or bind them, not testimony that no such external records exist.

Blocking findings: 1 (BS-L self-cycle/class), 2 (schema-free BS-L and stale BS-V lock), 3 (exceptions voided), 4 (incomplete/unidentified exception processes), 5 (contradictory slot inventory), 6 (retrospective blinding gap), plus the explicitly carried Stage-P dual definition.

**NOT CLEAR**