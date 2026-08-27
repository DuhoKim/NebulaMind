# V17 WHOLE-DOCUMENT REFEREE REPORT — GPT56

Verdict: **NOT CLEAR**. The reviewed bytes match the dispatch pin, the document is structurally complete through §11, §6.3's operative bodies are restored, §4 now carries Row J's calibration gate and post-attrition rule, the §7 counts close, and the class-P overclaim is repaired. But three core repairs are incomplete or internally broken: §2.7 still carries the live reason-(d) confidence paragraph that the V17 brief says was deleted; the new §3 scalar/profile prose bypasses the calibration-precedence branch implemented by `adjudicate_path()` and stated in §6.3; and the new outcome registry is not single-valued or exhaustive when checked against Row P and Row I. The chronology and §10 repair-trace repairs also remain only partly applied.

## Digest-first identity and structural check

- Subject: `../PREREG_SUCCESSOR_DRAFT_V17_20260827.md`.
- Brief-pinned sha256: `1a0a259a91f5a73a80fc864148e5fb6b0a2014dbf2494d243484e3948c16fce5`.
- Independently computed before opening: `1a0a259a91f5a73a80fc864148e5fb6b0a2014dbf2494d243484e3948c16fce5`.
- Result: **MATCH**. This report binds that exact digest.
- Independent line count: **782**, matching the brief. The headings run through §§0, 1, 2 (including separately headed §2.7), 3, 4, 5, 6, 7, 8, 9, 10 and 11; the final line is the expected final §11 verifier item. The drafting timeout did not truncate the visible document structure.
- Independently recomputed predecessor pins: V16 = `1b9b9486736bf734c8cb4ac8cedf54870fd179587e3e1455273ec4724132a0da`; V15 = `efb27c619c063f8f82c36a7930cf883c43823b8d17d0b4e63eb04d841035fb28`. Both match the brief's abbreviated standing pins.
- Independently recomputed §0 code pins: `successor_ref_v9.py` = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` = `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.

## Numbered findings

### 1. HIGH / BLOCKING — §2.7's advertised deletion did not land: reason (d) remains live, and the replacement threshold sentence is disjunctive

- **Section / lines:** §2.7 lines 337–373, especially 360–365 and 367–373; §7 line 675.
- **Evidence:** V17 correctly limits pre-lock reasons to (a)–(b) at lines 337–340. Nevertheless paragraph 5 still begins, verbatim, **“Reason (d) is the outcome-adjacent one”** and continues to define its confidence quantity and absence-output join at lines 360–365. V16→V17 opcode/diff inspection confirms that paragraph was not edited at all. Only paragraph 7 changed: it now says the threshold is defined as part of **“the Row P state (7) exclusion or the refused BS-2a design”** (line 373), while paragraph 6 and §7 assign the numeric threshold and authority to BS-2a.
- **Why it fails:** The V17 brief says the partial edit was completed by deleting reason (d) and its confidence threshold. It was not. The remaining paragraph is live normative prose, not history, and points to a reason absent from the exhaustive pre-lock enumeration. The replacement's “Row P ... or ... BS-2a” wording also fails to name one contract: Row P is the application state, while BS-2a is the design/producer slot. Clause 10 cannot make threshold ownership and phase depend on how a later operator resolves that “or.”
- **Smallest sufficient repair:** Delete or rewrite paragraph 5 so it describes **Row P state (7)** rather than nonexistent reason (d). Replace paragraph 7 with one subject: BS-2a alone freezes the confidence predicate/value/authority before BS-6; Row P applies that already-frozen predicate at P8; below threshold records `EXCLUDED-BY-CONFIDENCE`, and any such removal yields `INCONCLUSIVE-BY-CALIBRATION`. Preserve the current BS-6 block until that design is gated.

### 2. HIGH / BLOCKING — the newly added §3 scalar/profile branch omits calibration precedence and contradicts §6.3 and the pinned definition

- **Section / lines:** §3 line 388; §4 lines 448–449; §6.3 lines 585–588; pinned `ref/successor_ref_v9.py` lines 1492–1496.
- **Evidence:** The new §3 sentence says `max_b |â_b - â| <= 0.03` selects scalar and **“selects the profile path otherwise.”** It does not condition either path on all `a_LB_b >= 0.85`. In contrast, restored §6.3 says scalar requires both spread `<= 0.03` and every lower bound `>= 0.85`, profile is **spread failure only**, and any lower bound `< 0.85` halts `INCONCLUSIVE-BY-CALIBRATION`. The pinned code has the same precedence: `adjudicate_path()` first raises on `min(a_lb_b) < A_FLOOR`, then and only then returns SCALAR/PROFILE by the `0.03` predicate.
- **Why it fails:** A record with spread `> 0.03` and one lower bound `< 0.85` reaches PROFILE under the new §3 sentence but reaches a calibration halt under §4/§6.3/code. This is exactly a Clause-10 forward double continuation introduced adjacent to a V16 repair. The value and equality side of `0.03` are correct, but its phase/failure precedence is not.
- **Smallest sufficient repair:** Make §3 byte-semantically match `adjudicate_path()`: first, any `a_LB_b < 0.85` → pre-unblinding `INCONCLUSIVE-BY-CALIBRATION`; only among admitted records, spread `<= 0.03` → SCALAR and spread `> 0.03` → PROFILE. Keep equality on SCALAR and state that PROFILE is not a failure.

### 3. HIGH / BLOCKING — the canonical registry fails Clause 10 in both directions against §5 and Rows I/P

- **Section / lines:** §5 lines 458–475; Row I line 527; Row P line 534; Clause 10 line 564.
- **Evidence, forward double-assignment:** §5 says `run_production_verdict()` emits **“exactly one outcome from the canonical registry”**, but the registry includes both per-attempt `EXCLUDED-BY-*` categories and run-level `INCONCLUSIVE-BY-CALIBRATION`. Row P states that an absent/non-finite/low-confidence attempt is assigned its `EXCLUDED-BY-*` state and that **any** post-unblinding removal then emits `INCONCLUSIVE-BY-CALIBRATION`. The same branch therefore reaches two listed registry categories. A run may also contain multiple excluded attempts, so the registry cannot literally be an exactly-one output surface.
- **Evidence, forward missing assignment:** Row I requires the run to fail before BS-8f if any allocated object lacks a usable finite instrument output. That proper abort has no named category in the registry. Row I's void column penalizes **failing to abort**; it does not make the required abort itself VOID. The same gap exists for §3's non-finite/degenerate fail-closed decision inputs unless they are expressly classified.
- **Evidence, reverse typing:** `EXCLUDED-BY-*` has reachable per-attempt antecedents, but those are terminal attempt states, not mutually exclusive run outcomes emitted by the one verdict path. Calling all five bullets one exactly-one registry conflates two levels.
- **Why it fails:** The V17 brief specifically requires every branch to reach exactly one category and every category to have a reachable antecedent, with the registry checked against Rows A–S and §5 both ways. The new surface neither partitions by level nor assigns every run-ending branch.
- **Smallest sufficient repair:** Split the registry into (a) an **exactly-one run outcome/refusal enum** and (b) a **many-row per-attempt terminal-state enum** carried by the adequacy receipt. State explicitly that `EXCLUDED-BY-*` is not emitted as the final run outcome; its aggregate consequence is calibration inconclusive. Add one canonical run outcome for Row I's required pre-BS-8f abort (and classify non-finite/degenerate decision-input failures), or explicitly map each to an existing category with one unambiguous rule. Then rerun the Row A–S forward/reverse table mechanically.

### 4. MEDIUM — the chronology repair was added to the banner but not applied to the fold record itself

- **Section / lines:** banner lines 7–20; fold record lines 617–620 and 621–632.
- **Evidence:** The banner now distinguishes initiation at 21:48, verdicts at 21:52:33/21:53:46, and final V16 bytes after the schema repair. Filesystem mtimes independently support the ordering of the two report files and final V16 (`21:52:33`, `21:53:46`, `22:47:17` KST). But fold-record part (b) still says **“Folded ... before R15 referee verdicts existed”** and the round “had not returned when the fold was performed,” retaining the same overloaded “folded/performed” wording the V16 review found. Part (c) still labels its state **“at the moment of folding.”**
- **Why it fails:** The brief says the fold record's chronology was split into three moments. The split exists only in the front banner; the section titled “The fold record” still conflates initiation with the final assembled byte state. This is a relocated repair, not a fully applied one.
- **Smallest sufficient repair:** Conform fold-record parts (b)–(c) to the banner: explicitly name (1) instruction/initiation before verdicts, (2) verdict arrival during assembly, and (3) final V16 bytes after the GPT56 inventory repair. Reserve “final bytes” for moment (3).

### 5. MEDIUM — §10 still makes the historical claim the brief says was removed

- **Section / line:** §10 line 769.
- **Evidence:** The exact sentence remains: **“V15 → V16 ... applied its conforming edits to §2.5, §2.7, §4, §5, and §7.”** The V16→V17 diff proves the §4 text was first added in V17, and Finding 1 proves the §2.7 edit is still incomplete. No V17 repair-trace entry exists.
- **Why it fails:** The brief says §10's false claim was removed. It was not; V17 made the present §4 surface conforming without changing the false historical assertion about V16. The restored §6.3 one-change/trace clause requires each V17 change to map finding → change, yet §10 contains no V16→V17 trace for the 13 changed hunks.
- **Smallest sufficient repair:** Replace the historical sentence with a V15→V16 entry that states what actually landed and remained open, then add a V16→V17 table mapping each V16 finding to the actual hunk. Do not mark §2.7 or the registry closed until Findings 1 and 3 are repaired.

## Seven advertised V16 repairs — applied disposition

1. **§6.3 operative bodies — HOLDS.** Seven bare titles became 38 lines of operative text; the universal post-first-real-χ change/void rule is in V17 lines 590–593, and Row P now cites current §6.3 rather than V15 line numbers. The bodies have normative force.
2. **§4/Row-J conformance — PARTIAL.** The actual §4 calibration gate and pre-attrition-only/no-rerun text landed at lines 448–454. The promised removal of §10's false V15→V16 claim did not (Finding 5).
3. **§2.7 completion — FAILS.** Reason (d) remains at lines 360–365; only the old BS-3 sentence was replaced, and its replacement is still ambiguous (Finding 1).
4. **§7 count — HOLDS.** Direct table parsing yields 14 Class-P rows and 8 Class-E rows, matching line 669; BS-2f is Class E and value-only.
5. **Outcome/refusal registry — PRESENT BUT DOES NOT HOLD.** The labels are collected, but run outcomes and per-attempt states are not disjoint and Row I has no category (Finding 3).
6. **Three-moment chronology — PARTIAL.** The banner is split; the fold record remains overloaded (Finding 4).
7. **Two smaller overclaims — PARTIAL.** The class-P completion sentence is correctly narrowed at line 319. The `0.03` scalar/profile value, phase and equality side were added, but its calibration precedence is wrong (Finding 2).

## Clause 10 whole-document audit — both directions

### Forward: branch → exactly one category

Branches that held under attack include: BS-1 A/B and date fallback; exact-mode `<=16` versus production mode; manifest equality/refusal; Row J's all-bins `>=0.85` admission versus any-bin `<0.85` halt; exactly 1,000 trials, 962/1,000, self-verification fail/pass; Row O one-use/replay; Row P's precedence among zero/duplicate/extra/malformed/absent/non-finite/low-confidence/accepted-finite; zero versus any post-unblinding removals; and numeric p/band/floor residuals.

Forward closure fails at three concrete branches: (i) low calibration plus spread failure gets PROFILE in §3 but calibration halt in §6.3/code; (ii) each Row-P exclusion gets both an `EXCLUDED-BY-*` registry category and a run-level calibration-inconclusive category; (iii) Row I's required missing/non-finite allocated-output abort has no registry category. The confidence predicate also remains incompletely seated by Finding 1.

### Reverse: category → reachable antecedent

The three numeric verdicts, two named pre-statistic inconclusives, four Row-P accounting refusals, three Row-P terminal exclusion labels, and VOID all have at least one textual antecedent. Reverse closure nevertheless fails as an **exactly-one run registry** because the `EXCLUDED-BY-*` antecedents are per-attempt states that necessarily coexist with the run's calibration-inconclusive outcome; they are not alternative final run outcomes. Conversely, the Row-I abort antecedent has no category. The registry must be typed by level before reverse reachability proves exhaustiveness.

## Threshold sweep — value, phase, failure effect

### Thresholds that held

- Release resolution date **2026-09-05**: earlier confirmed DR11 availability → A; otherwise on date → B; later waiting requires amendment.
- Catalog cuts: `0 <= z < 0.15`; shape sum `< 0.1836734693877551` / `b/a > 0.4`; `r < 17.7`; `shape_r > 1.5` are single-valued in prose. Their external predecessor-source provenance was not re-fetched in this no-fetch gate.
- Planning: exact mode `<=16`; retention `floor(0.8572*n)`; `N_eq >=100,000`; `L_plan = 1.2*L_min_plan`; values agree with pinned v9.
- Stage power: floor `0.85`; 1,000 trials; 962 passes and 961 fails; self-verification `refuted`/`nonconservative` fails closed; Stage-C failure → `INCONCLUSIVE-BY-POWER`; protocol deviation → VOID. The known Stage-P shared-null/exact-null implementation conflict remains prominently blocked rather than claimed repaired.
- Production/statistical: 100,000 permutations; reproduction `p < 0.001`; rejection `p > 0.05`; equality falls to numeric `INCONCLUSIVE`; Longo amplitude `0.0408`; three-sigma bands; detection multiplier `3.09`; values agree with pinned v9.
- Calibration allocation: at least 10 per non-empty joint cell and at least 30 real labels per live inherited stratum; infeasibility fails rather than shrinking.
- Post-unblinding attrition: zero removals may proceed; one or more removals → `INCONCLUSIVE-BY-CALIBRATION`; no Stage-C rerun.

### Threshold defects

- Confidence: the numeric value is intentionally unresolved, but owner/definition wording remains stale/disjunctive; phase and effect therefore do not close (Finding 1).
- Scalar/profile `0.03`: value, phase and equality side are added, but the any-bin `<0.85` failure effect does not take precedence in §3 (Finding 2).
- Missing/non-finite allocated calibration output and non-finite/degenerate decision inputs are fail-closed but lack a canonical final category (Finding 3).

## Fold record and overclaim check

- Independently verified: V15/V16/V17 hashes above; report-file mtimes for CODEX and GPT56; final V16 mtime after both; V17 final mtime `23:03:30 KST`; §6.3 operative restoration; direct 14/8 slot-table counts.
- The raw 21:48 Duho instruction was not independently available in the inspected artifact set, so its authority/time remains **Testimony**. The later filesystem ordering is verified.
- The document continues to state prominently that it is a draft, nothing is in force, BS-2a is refused/unfilled, Rows C2/E cannot run, BS-6 and the first image byte are blocked, Stage P is not in definitional code, and `verify_lock()`/unblinding mechanisms remain required but unimplemented. Those limitations held under attack.
- The remaining overclaims are specific: advertised deletion of reason (d); advertised exactly-one registry closure; advertised three-moment fold-record repair; and §10's claim that §4 was already applied in V16.

## Failed attacks / credited surfaces

1. Tried to find a digest or line-count mismatch: neither exists.
2. Tried to find structural truncation from the drafting timeout: all 13 `## §` headings/section surfaces are present and §11 ends on the same verifier inventory item described by the brief.
3. Tried to reopen the §6.3 bare-title defect: the operative calibration, void, trace, custody and blind-double bodies are restored; Row P cites the current section.
4. Tried the §4 calibration boundary: `<0.85` halts, equality `>=0.85` admits; the pre-attrition-only and no-rerun consequence is now local to §4.
5. Recounted §7 mechanically: 14 Class-P and 8 Class-E rows match the prose; BS-2a/BS-2k are the DESIGN inventory and BS-2f remains value-only Class E.
6. Tried to recover the class-P completion overclaim: line 319 now correctly calls the measurements candidate evidence and says they fill no unreceipted slot.
7. Tried to bypass BS-L/unblinding/final-mask guards through §5: the required guard surface is named at document-contract level; implementation remains honestly unresolved.
8. Tried equality seams at `0.03`, `0.85`, 962, `0.001` and `0.05`: their individual equality sides are stated consistently. The blocking `0.03` issue is precedence, not its equality side.

## Testimony / limits

- BS-2a's three-seat refusal; standing findings 1, 2, 2b and 3; historical geometry/count results; Stage-P measurement; source-citation verification; archive seal state; and the raw 21:48 instruction were not independently re-executed here.
- Future `verify_lock()`, `verify_unblinding_receipt()`, canonical schemas, Row-J guard, mediator, C2 worker, acceptance recomputation, replay verifier and adequacy verifier remain required work, not executed protection.
- No `/Users/duhokim/NebulaMindData/` content was read. Nothing was fetched. No secrets or χ-bearing material were inspected.

## Evidence ledger and custody

Content read included: `BRIEF_V17_WHOLE_REVIEW.md`; the complete pinned V17 subject; V16 through the complete V16→V17 diff; V15 targeted §6.3 source passages; both V16 whole-document referee reports; R15 CODEX/GPT56 report passages; and pinned v9 constants, `adjudicate_path()` and decision logic.

Independent checks included: sha256 of V17/V16/V15 and pinned code; line count and section-heading parse; whole-file V16→V17 opcode/diff inventory; direct Class-P/Class-E table parsing; registry-token inventory; targeted stale-reason/threshold/registry searches; pinned-code threshold and precedence comparison; file mtime ordering; and a forward/reverse branch walk across §§0–11 and Rows A–S.

No source, code, preregistration draft, data artifact, prior report, or gate brief was modified. This report is the sole intended write by GPT56.

**NOT CLEAR**