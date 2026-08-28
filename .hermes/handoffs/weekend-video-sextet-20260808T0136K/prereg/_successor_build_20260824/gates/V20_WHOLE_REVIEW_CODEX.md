# V20 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

**NOT CLEAR.** V20's new sentence at §5 line 473 accurately inventories the values that the pinned `run_production_verdict()` can return, but §5 still makes a false present-tense guard claim immediately above it: the runner does not require or verify BS-L or the one-use unblinding receipt. The purported unresolved-work inventory and the V19→V20 repair trace omit that missing capability. Separately, V20 honestly says `VOID` is non-executable, but does not make `VOID` conversion a BS-6 prerequisite or even carry it into §11; Clause 10 reverse reachability therefore remains unclosed without the required explicit block.

## Digest and subject identity

I compared the live bytes of `../PREREG_SUCCESSOR_DRAFT_V20_20260827.md` with the brief's expected SHA-256 `607df3dd5b022a299162dac501b9c5766dda87bac8b3ba1cea11a105efa00261`. `shasum -a 256` returned exactly `607df3dd5b022a299162dac501b9c5766dda87bac8b3ba1cea11a105efa00261`: **MATCH**. I did this before opening the draft.

I also compared the live `../ref/successor_ref_v9.py` bytes with V20 §0's pin. `shasum -a 256` returned `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`, exactly the pin at V20 line 78: **MATCH**.

## Numbered findings

### 1. HIGH / BLOCKING — §5 lines 458–473: the return inventory is true, but the adjacent present-tense guard inventory is false and the unresolved list is incomplete

V20 line 461 says that `run_production_verdict()` "requires and verifies the canonical BS-L artifact and the one-use unblinding receipt." It does neither.

Mechanical comparison performed:

- I parsed `successor_ref_v9.py` and compared the signature and call set of `run_production_verdict()` at code lines 1591–1625 with V20's §5 claims.
- The parsed arguments returned were `mask`, `cal`, `authorization_path`, `authorization_sha256`, `n_receipts`, `n_parent`, and `stage_c_receipt`. There is no BS-L or unblinding-receipt argument.
- The parsed call set returned `require_environment`, `require_authorization`, `require_complete_sample`, `require_sealed`, `adjudicate_path`, `perm_record`, `_decide_from`, and utility calls. It returned **zero** `verify_lock` calls and **zero** unblinding-named calls.
- Direct source inspection agrees: lines 1596–1605 check environment, authorization, sample completeness, sealed-mask type, and a BS-5f envelope bound to the mask; they do not inspect BS-L or an unblinding receipt.

The central return-value claim itself held. I compared every return in code lines 1591–1625 and the called decision helper at lines 1561–1588 with V20 line 473. The AST returned three runner return sites: Stage-C false → `INCONCLUSIVE-BY-POWER` (1611–1612), `N_eq < 100000` → `INCONCLUSIVE-BY-POWER` (1615–1616), and `_decide_from(...)` (1621–1625). The helper's verdict literals returned exactly `REPRODUCED-LONGO`, `REJECTED-AT-LONGO-AMPLITUDE`, and `INCONCLUSIVE`. Thus line 473's list of return values is exact; the defect is that §5's capability inventory still claims unimplemented guards, while line 473's "Unresolved required implementation" list omits those guards.

This also makes §10 lines 800 and 802 overclaim the V19 finding's repair: the text was narrowed to the true return set, but it did not mark the missing BS-L/unblinding guard capability as unresolved.

**Smallest sufficient repair:** At line 461, replace the present-tense statement with an explicit required-but-unimplemented guard. Add BS-L verification and authenticated one-use unblinding-receipt verification to line 473's unresolved implementation list. Keep the exact return-value sentence.

### 2. HIGH / BLOCKING — §5 line 471, §6.1 Clause 10 line 566, §7 lines 675–701, §11 lines 814–822: `VOID` has no reverse-reachable producer and is not made a BS-6 prerequisite

Clause 10 requires every branch of every row to terminate in a stated outcome. Rows A–O and Q–R contain forbidden-act/protocol/digest/non-finite branches whose stated lifecycle category is `VOID`. V20 now honestly says at line 471 that `VOID` "is not yet executable" and at line 473 that `VOID` conversion is unresolved. That honesty fixes the false producer claim, but does not close reverse reachability.

The brief permits this unfinished state only if the document says plainly both that reverse reachability does not yet resolve and that BS-6 remains blocked because of it. V20 does not make that connection:

- The banner's generic statement at lines 30–32 says BS-6 remains blocked among carried items, but does not say `VOID`/Clause 10 is a reason.
- The explicit BS-6 block at §7 line 677 is attached to the refused BS-2a design.
- The §11 code-side inventory lists schemas, `verify_lock`, Row J, mediation, C2/integrity, unblinding verifiers, and aggregate validation, but contains no `VOID` conversion implementation item and no pre-BS-6 gate for it.

Therefore forbidden/failure branches are named but not executable, and the programme's binding-slot graph does not prevent BS-6 on that ground. This is an unfinished preregistration/programme boundary, not a demand that the current draft pretend the mechanism exists.

**Smallest sufficient repair:** State explicitly in §5/Clause 10 that reverse reachability through `VOID` is unresolved and that BS-6/first-image-byte remains blocked until a gated `VOID` converter covers every enumerated forbidden/protocol/digest/non-finite branch. Add that converter, fixtures, and its pre-BS-6 dependency to §11 and §7. Do not invent a producer name as if implemented.

## Clause 10 and threshold audit

I read §§0–11 in both directions: row branch → lifecycle outcome and outcome → named branch/phase.

The following threshold/value/phase/failure-effect bindings held in the text:

- Numeric decision at P8: `p < 0.001`, Longo sign, `|Â_L−0.0408| ≤ 3σ_comb`, and evaluated `3.09·σ_ours(a_LB)` floor → `REPRODUCED-LONGO`; `p > 0.05` and `|Â_L|+3σ_ours < 0.0408` → rejection; complement → numeric `INCONCLUSIVE`.
- Pre-unblinding calibration at P5: any `a_LB_b < 0.85` → `INCONCLUSIVE-BY-CALIBRATION`; only the complement reaches Stage C. Spread `≤ 0.03` selects scalar and `> 0.03` profile; profile is not a failure.
- Stage C at P5: fewer than 962 of 1,000 successes, or `refuted`/`nonconservative` self-verification failure → `INCONCLUSIVE-BY-POWER`; complementary PASS alone reaches BS-5f/BS-L.
- Production runner: failed BS-5f and `N_eq < 100000` each return `INCONCLUSIVE-BY-POWER` before the real statistic.
- Row I: missing allocated usable finite output → `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT` before BS-8f.
- Row P at P8: zero/duplicate/orphan/malformed records map to the four accounting outcomes; absence/non-finiteness/low confidence create per-attempt exclusion states, and any post-unblinding removal maps to the single run-level `INCONCLUSIVE-BY-CALIBRATION` with no Stage-C rerun.

Forward/reverse closure fails only where Finding 2 states: branches assigned to the non-executable `VOID` category do not yet have an executable terminator or a pre-BS-6 dependency.

## §10 repair-trace comparisons

I compared the complete line sequences of each adjacent version with Python `difflib.SequenceMatcher(autojunk=False)`; below are the returned hunk and changed-line counts and the content result relevant to each trace.

1. **V16→V17:** 14 non-equal hunks; 27 old lines and 60 new lines. The comparison returned restoration of the §6.3 bodies, the Row-P citation change to §6.3, the §4 calibration/pre-attrition additions, candidate-evidence narrowing, the 0.03 rule, and the registry gathering. For the count repair specifically, V16 line 636 and V17 line 669 both returned the identical text `One of fourteen class-P slots is filled`; only Class E changed `7` → `8`. V20 lines 776–780 now describe this accurately.
2. **V17→V18:** 13 non-equal hunks; 15 old lines and 35 new lines. The comparison returned the single BS-2a threshold authority, removal of stale reason-(d) wording, calibration-before-spread precedence, run/per-attempt registry split with Row-I abort, fold chronology changes, removal of the false V15→V16 historical claim, and insertion of both traces. V20 lines 782–789 accurately describe these edits.
3. **V18→V19:** 8 non-equal hunks; 11 old lines and 19 new lines. The comparison returned the lifecycle-registry producer rewrite, the then-narrowed runner sentence, non-finite split, the two V16→V17 trace expansions, the V17→V18 label repair, and insertion of the V18→V19 trace. V20 lines 791–795 accurately describe the byte changes.
4. **V19→V20:** 8 non-equal hunks; 7 old lines and 19 new lines, totaling the brief's 26 changed lines. The comparison returned the added `N_eq`/Stage-C producers, non-executable `VOID` sentence, exact runner-return sentence, corrected Class-E-only trace, new V19→V20 table, and aggregate-validation §11 item. The byte-change map is accurate, but trace rows A/C's claim that the capability repair is exact/complete fails for the independent code comparison in Finding 1.

## Failed attacks / points that held

- **Pinned identity held:** V20, V19, V18, V17, V16, `successor_ref_v9.py`, and `closure_worker_v9.py` all returned the hashes stated by their immediate pins/§0. In particular, V19 returned `b7deb106...e63b`, V18 `ce144dc2...02f4`, V17 `1a0a259a...fce5`, V16 `1b9b9486...a0da`, and the worker `28f8e1f9...a5959`.
- **Central return set held:** no sixth returned verdict was found in `run_production_verdict()` or `_decide_from`; the exact returned set is the three numeric outcomes plus two power branches.
- **Power-producer exhaustiveness held:** the lifecycle registry now names Row J plus the production runner's Stage-C and `N_eq` guards.
- **Row-I overlap repair held:** the calibration aggregate category expressly excludes Row-I missing allocated outputs, leaving one run-level antecedent per stated category.
- **No invented orchestration symbol found:** a content search for `orchestrat` in V20 returned zero occurrences. The newly named `validate_calibration_aggregates` is explicitly required future implementation, not claimed present code.
- **Adjacency held except as found above:** the V19→V20 diff is limited to the declared 26 changed lines, and no unrelated body change appeared.

## Testimony / unverified assertions

I did not independently reconstruct the historical fold times, authorization chronology, prior referee verdict timestamps, real-geometry measurements, or prior source-verification claims. Those remain testimony for this review. I did not read `/Users/duhokim/NebulaMindData/`, fetch anything, execute a real-data run, or inspect stale sibling-order artifacts.

## Evidence ledger and constraints

Read content: `BRIEF_V20_WHOLE_REVIEW.md`; the complete V20 draft; `successor_ref_v9.py` lines 40–89, 1095–1139, 1485–1519, and 1540–1690; adjacent V16–V20 files through line-level comparisons. Name-only discovery: the versioned preregistration filenames. Commands: `pwd`; SHA-256 comparisons; AST signature/call/return extraction; four adjacent-version sequence comparisons; bounded content searches. No network, fetch, real-data access, source-document mutation, git mutation, or write outside this required report occurred.

**NOT CLEAR**