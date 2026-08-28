# V26 WHOLE-DOCUMENT REVIEW — GPT56

Verdict: **NOT CLEAR.** The dispatched V26 bytes match the runner pin exactly. The round’s central scientific-language repair succeeds: I found no surviving affirmative claim that the catalogue-quality predicate is independent of handedness, and §2.7 explicitly says that independence conditional on position is **not established**, rather than replacing it with a confident weaker statistical claim. The whole document nevertheless remains internally non-executable. Catalogue quality is now said to be applied before BS-2f, but the closed exclusion list still forbids that reason and the post-unblinding Row-P vocabulary applies it again, where every such exclusion forces `INCONCLUSIVE-BY-CALIBRATION`. The obsolete 995/1000 Stage-P result is still presented as a PASS on the “real REDUCED geometry,” although it was computed before the geometry changed to 49,211. The V25→V26 findings mapping is absent and the named checker still fails.

## Digest first — exact comparison

I recomputed SHA-256 over the current bytes of `../PREREG_SUCCESSOR_DRAFT_V26_20260827.md` and compared all 64 hexadecimal digits with `runner_v26_chain.log` line 5:

- runner pin: `2eec8da41ee69374fcc9c3fca2de150b29c04ca7b921848e908fa97a20bffd52`
- recomputed current V26: `2eec8da41ee69374fcc9c3fca2de150b29c04ca7b921848e908fa97a20bffd52`
- comparison: **MATCH — exact 64-hex equality**

I also recomputed V25 as `50f2e53256cc79707f2a4dfbf737740e6101742deb39365498737c904aa0f59b`, exactly matching V26 lines 3–4, before using the V25→V26 diff.

## Numbered findings

### 1. CRITICAL / BLOCKING — §2.7 lines 336–343 and 380–382; §5 lines 489–491; §6.1 Rows E/P lines 539/550; Clause 10 line 580: catalogue quality occupies two phases and its P8 copy deterministically kills the run

**Why it fails.** V26 correctly moves the catalogue-quality predicate into Row E before BS-2f: §2.7 line 382, Row E line 539, Row F line 540, BS-2f line 709, and BS-5f line 711 consistently require a 49,211-row P3/P5 mask. But the old post-unblinding mechanism was not removed:

- §5 line 489 includes `EXCLUDED-BY-CATALOGUE-QUALITY` in the post-unblinding adequacy receipt and says **any** `EXCLUDED-BY-*` state emits `INCONCLUSIVE-BY-CALIBRATION`.
- Row P line 550 again tests “catalogue quality below frozen threshold” at P8, drops the row, and then applies the rule that any post-unblinding removal emits `INCONCLUSIVE-BY-CALIBRATION` with no Stage-C rerun.
- §5 line 491’s prose summary omits catalogue quality from its precedence summary and says “all others are accepted-finite,” while Row P includes an additional catalogue-quality branch.

Thus the same fixed quality cut is both the intended nonfatal constructor of the 49,211-row P3 mask and a later fatal P8 attrition branch. If Row P joins the 65,060-parent attempt set as written, the already-known catalogue-quality failures reappear and force an inconclusive run. If it joins only the 49,211 mask, its “exact-parent” language and catalogue-quality branch become false or unreachable. Clause 10’s added sentence merely asserts the correct phase; it does not repair the conflicting phase and failure effect in the operative neighbors.

**Smallest sufficient repair.** Remove catalogue-quality evaluation and `EXCLUDED-BY-CATALOGUE-QUALITY` from the post-unblinding Row-P/adequacy terminal vocabulary. Bind the pre-BS-2f Row-E receipt to a complete 65,060-row catalogue-quality partition, then make Row P’s post-unblinding attempt set exactly the already quality-passing 49,211 BS-2f IDs and reserve its fatal attrition states for genuinely post-unblinding instrument absence, non-finiteness, and confidence. Reconcile §5’s summary and Row P’s ordered list byte-for-byte.

### 2. HIGH / BLOCKING — §2.7 lines 332–343 versus line 380 and Row E line 539: the declared closed pre-lock exclusion list still forbids the new catalogue-quality reason

**Why it fails.** Section 2.7 line 336 says pre-lock exclusion reasons are “enumerated here and nowhere else”; lines 336–339 list only missing/byte-integrity and incomplete-shape reasons, then state **“No other reason is admissible. A reason not on this list requires a new text.”** V26 is that new text, but it did not add catalogue quality to the enumerated list. Line 380 separately declares a “distinct closed catalogue-quality exclusion reason,” and Row E line 539 applies it before lock. Those statements cannot all be true. The neighboring construction-blindness rule at lines 340–343 is also scoped only to reasons (a)–(b), leaving the newly added reason outside the section’s own exhaustive predicate contract.

**Smallest sufficient repair.** Add catalogue quality as an explicit third pre-lock reason in §2.7(2), with its authenticated fields, exact three-threshold predicate, Row-E producer, terminal status, phase, and nonfatal effect. Update §2.7(3) so its construction/assumption language explicitly covers this third reason while preserving the open conditional-independence statement.

### 3. HIGH / BLOCKING — §2.6 lines 292–318 and §4 lines 448–450: Stage P was not marked superseded and the old 995/1000 result is still credited as current PASS evidence

**Why it fails.** The brief required the 995/1000 Stage-P result to be marked superseded because it was computed on the old 65,060-parent/53,005-retained geometry and cannot stand for the new 49,211 analysis mask. V26 instead retains:

- “**Stage P on the reduced set: 995/1000 … PASS**” at lines 292–297; and
- “**Measured on the real REDUCED geometry (§2.6): 995/1000, PASS**” at lines 448–450.

Neither occurrence says historical, superseded, or non-applicable to the post-quality mask. Line 318 only says candidate evidence does not fill BS-5p; that was already true before the geometry change and does not withdraw the PASS claim for the wrong population. The document’s own post-quality values are `N = 49,211`, `Var = 0.7517`, `N_eq = 110,983` (lines 461–468), not Stage P’s `n = 53,005`, `Var = 0.754664`, `N_eq = 120,003` (lines 296–297).

**Smallest sufficient repair.** Mark both 995/1000 statements explicitly **SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK**, remove current-PASS wording, and require a fresh frozen Stage-P run on the exact post-quality BS-2f geometry before BS-5p can receive power credit.

### 4. HIGH / BLOCKING — §6.3 line 611, §10 lines 814–844, `gates/FINDINGS_MAP.md`, and `tools/prereg_trace.py`: no honest V25→V26 findings mapping exists and the checker returns 16 problems

**Why it fails.** The exact V25→V26 diff changes normative §6.1, §2.7, §7, §6.3, §5, and §11 text. The current `FINDINGS_MAP.md` ends at V24→V25 and contains no V25→V26 entry. The document’s §10 ends at V23→V24, while §6.3 line 611 names only the V24→V25 mapping rather than the transition under review. Running the named checker on the pinned V26 returns:

- `MISSING: no written row for V25 → V26`;
- `NO FINDING CITED: V25 → V26 changed §6.1, §2.7, §7, §6.3 ...`; and
- fourteen historical no-finding failures despite §6.3’s claimed historical exemption;
- total: **25 computed transitions; 16 problems**.

The no-truncation repair itself is real: `tools/prereg_trace.py` lines 112–116 now emit every changed section. But the coverage contract and current-transition mapping are still not implemented coherently. The computed V25→V26 delta is: §6.1 +6/−6, preamble +4/−4, §2.7 +4/−4, §7 +2/−2, §6.3 +1/−2, §5 +1/−1, fold record +1/−1, §11 +1/−1; no §7 row-count change.

**Smallest sufficient repair.** Add and pin a human-reviewed V25→V26 sidecar mapping citing only the V25 findings actually answered by these bytes; make `prereg_trace.py --check` implement the stated predecessor-only in-band/current-transition-sidecar architecture; and encode the historical V1→V15 exemption in the checker rather than prose alone. Do not claim the mapping is enforced until the checker returns zero under that contract.

## Central question — held

1. **No affirmative independence-from-handedness claim survives.** The only occurrence tying “independent” to handedness is §2.7 line 378’s explicit open statement: “Whether the predicate is independent of handedness conditional on position … is not established.” Other uses of “independent/independently” concern brick enumeration, verification, permutation runs, or custody, not handedness.
2. **The narrow claim is actually narrow.** Section 2.7 line 378 claims only outcome-blindness with respect to this study’s unobserved χ: the columns and absolute thresholds were fixed without reading χ and before any image byte, so they cannot be tuned post hoc. It does not call that chronology statistical independence.
3. **The conditional-independence gap remains open.** The same sentence names the exact property needed by the dipole estimator, labels it “not established,” and requires either a preregistered check or a stated assumption carrying risk. I found no confident weaker statistical claim elsewhere that purports to close that gap.

## Other failed attacks / checks that held

1. **P3/P5 values propagate on the intended pre-unblinding path.** Lines 382, 461–468, 539–540, and 709–711 all use the 49,211-row mask; BS-5f uses `N_eq = 110,983`; the 65,060 parent identity is expressly retained. Finding 1 is the surviving duplicate P8 path, not absence of the repaired P3 path.
2. **BS-2a walk-back propagates across live status surfaces.** Lines 372, 537, 559, 667–668, 684, 690, and 852 consistently say DESIGN/UNFILLED or defer its code/schema. The live count says **one of fifteen** Class-P slots is filled, naming BS-2m. `tools/prereg_counts.py` independently parsed 15 Class-P and 8 Class-E rows and reported that prose and table agree. The runner log’s “One of twelve” hit comes from the explicitly historical V15 quotation at lines 654–656, not a live V26 count.
3. **First-image blocking remains explicit.** Lines 559, 580, 667–669, and the BS-2a/BS-2v/BS-6 slot dependencies keep Rows C2/E, BS-6, and the first image byte blocked.
4. **No-truncation tool repair holds.** The current trace generator has no six-section cap and emits all eight V25→V26 changed regions.
5. **Linter/count diagnostics were not mistaken for clearance.** `prereg_lint.py` still reports two old missing V2 citation-file findings; these are not V26’s central repair but remain nonzero diagnostics.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`, fetch an image byte, execute χ-bearing work, rerun Stage P, or re-query the survey.
- The physical survey chronology, catalogue semantics, reported threshold provenance, and the claim that the listed columns were measured before this study are **Testimony**. My ruling on the central question is about what V26 claims, not independent proof of that chronology.
- I did not independently recompute the 49,211/N_eq arithmetic in this round; both V25 whole-review reports record independent recounts, and V26 did not change the thresholds or printed values. I treated those reports as prior testimony and checked only V26’s propagation and phase semantics.
- Pre-existing working-tree changes and untracked files were present before this report; I did not modify the subject draft, predecessor, tools, receipts, findings map, or any file other than this report.

## Evidence ledger

Content read: `gates/BRIEF_V26_WHOLE_REVIEW.md`; `gates/runner_v26_chain.log`; the complete pinned V26 draft; the complete V25→V26 diff; `gates/V25_WHOLE_REVIEW_GPT56.md`; `gates/V25_WHOLE_REVIEW_CODEX.md`; `gates/BRIEF_V25_REPAIR.md`; `gates/FINDINGS_MAP.md`; and `tools/prereg_trace.py`.

Executed checks: absolute-path working-directory change; SHA-256 of V26 and V25; whole-document searches for independence/handedness, all population/phase values, BS-2a status/count surfaces, catalogue-quality terminal states, Stage-P claims, and mapping references; independent V25→V26 diff; `prereg_counts.py`; `prereg_lint.py`; `prereg_trace.py --check`; computed V25→V26 changed-section inventory; and scoped pre-write git status.

**NOT CLEAR**