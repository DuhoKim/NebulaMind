# V28 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

**NOT CLEAR.** The dispatched V28 bytes exactly match the supplied 64-hex SHA-256, the live V28 trace check exits 0, §10 describes the checker contract without claiming that the check passed, and all 26 in-band trace rows are byte-equal to an independent regeneration. The remaining blocker is in the corrected checker: its supposed current-transition sidecar branch uses `to >= subject_version`, so a later V29 makes the unchanged V28 check demand the future V28→V29 mapping. The implemented scope is therefore “current and every future transition,” not the current transition described by §10, recreating the future-dependent historical-check failure this mechanism is meant to prevent.

## Digest first — exact comparison

I computed SHA-256 over the exact current bytes of `../PREREG_SUCCESSOR_DRAFT_V28_20260827.md` and compared all 64 hexadecimal digits with the digest supplied in `BRIEF_V28_WHOLE_REVIEW.md` lines 3–5 and in the dispatch:

- supplied digest: `82cd8ac3690fb87b9cf123719cf29f8af37af70e93652ee7e8a2da2b3ee8b587`
- independently recomputed digest: `82cd8ac3690fb87b9cf123719cf29f8af37af70e93652ee7e8a2da2b3ee8b587`
- comparison: **MATCH — exact 64-hex equality over the named V28 Markdown file's current bytes**

## Required live trace check

From the assigned `gates` directory I ran the repository tool with its required positional build directory and V28 subject:

`python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_trace.py .. --check ../PREREG_SUCCESSOR_DRAFT_V28_20260827.md`

It returned exit code **0** and exactly:

```text
prereg trace check — PREREG_SUCCESSOR_DRAFT_V28_20260827.md
  27 computed transition(s); 0 problem(s)
```

The 27 computed transitions include the current V27→V28 transition checked in the sidecar; V28's in-band §10 table correctly contains 26 transitions, V1→V2 through V26→V27.

## Numbered findings

### 1. HIGH / BLOCKING — §10 lines 815–820 and `tools/prereg_trace.py` lines 261–275: the “current transition” rule also binds all future transitions

**Evidence.** Section 10 says the current transition is mapped and checked in `gates/FINDINGS_MAP.md`. The checker instead enters its sidecar branch whenever `int(r["to"]) >= subject_ver` (line 264). That predicate includes the current transition **and every later transition found in the directory**.

I tested the boundary in a removed-after-use gate-local mirror: the same V1–V28 drafts and sidecar were present, and I added a synthetic V29 draft without adding a V28→V29 sidecar mapping. Checking the unchanged V28 subject returned exit 1:

```text
prereg trace check — PREREG_SUCCESSOR_DRAFT_V28_20260827.md
  SIDECAR MISSING: V28 → V29 is the current transition and is not mapped in gates/FINDINGS_MAP.md
  28 computed transition(s); 1 problem(s)
```

V28→V29 is not the transition that created V28. The diagnostic mislabels it “the current transition,” confirming the scope error rather than merely an awkward implementation detail.

**Why it fails.** V28's contract has three disjoint scopes: historical V1→V15 exemption, in-band rows through V26→V27, and the current V27→V28 sidecar. A V28 check must not acquire new obligations when V29 or later drafts are added. As written, a historical draft's check can change from clean to failing without any change to the draft or its own current-transition mapping. That is the same stale-history shape the trace design says it exists to eliminate.

**Smallest sufficient repair.** Split the condition explicitly: require the sidecar only when `to == subject_ver`; skip rows with `to > subject_ver`. Add a canary that appends an unmapped synthetic V(n+1), checks Vn, and requires Vn to remain unaffected, while retaining the existing canary that deletion of V(n−1)→Vn fails.

## §10: contract description versus result claim

Section 10 lines 815–820 describes scope and row requirements. It does **not** state that the checker passed, returned clean, or found zero problems. A whole-document search for a checker/trace statement coupled to “pass,” “passed,” “passing,” “clean,” or “0 problem” returned zero matches. The footer's statement that the tool enforces the finding-map obligation is a capability claim, not an assertion about this run's result. I therefore find no prohibited passing-result assertion in V28.

## Regenerated-table honesty

I imported the live `tools/prereg_trace.py`, independently rebuilt every transition from the draft bytes, loaded the human findings sidecar, rendered the predecessor-only rows, and compared complete Markdown row strings—not selected fields—against V28's parsed §10 table:

```text
computed_total=27 expected_in_band=26 actual_in_band=26
full_row_byte_equality=True
```

Thus all 26 rows' predecessor digests, result digests, complete section lists, added/removed line counts, §7 row-count changes, and findings columns agree byte-for-byte with the live regeneration. This also confirms that the previously omitted V24→V25 and V25→V26 rows are present and that the table now ends at V26→V27, the subject predecessor.

Three removed-after-use mutation attacks held:

1. Removing the V24→V25 table row produced `MISSING: no §10 table row for V24 → V25`, one problem, exit 1.
2. Removing the V27→V28 sidecar mapping produced `SIDECAR MISSING: V27 → V28...`, one problem, exit 1.
3. Corrupting only the V24→V25 row's result digest produced `UNPINNED: V24 → V25 row does not carry its result digest`, one problem, exit 1.

The current sidecar line cites `GPT56-V27-1`, `GPT56-V27-2`, `GPT56-V27-3`, and `CODEX-V27-1`. I reopened both V27 reports and the exact V27→V28 document diff. Those four findings are all and only about the failed trace run, omitted in-band rows, skipped current mapping, document-wide presence/digest masking, and the overstrong V27 enforcement assertion. V28's §10 regeneration/contract edit and the checker repairs demonstrably answer those findings; the sidecar cites no unrelated scientific or design finding.

## Clause 10, both directions, and threshold/phase/effect sweep

No new Clause-10 blocker was found. The V27→V28 document diff changes only the title and §10; the conduct, lifecycle, registry, threshold, and standing-state text is otherwise held.

- **Forward termination:** Rows A–S retain named phases, prerequisites, emissions, and forbidden effects. Row J terminates calibration failure as `INCONCLUSIVE-BY-CALIBRATION` and Stage-C failure as `INCONCLUSIVE-BY-POWER`; Row I terminates missing allocated output before BS-8f; Row P closes zero, duplicate, orphan, malformed, absent, non-finite, low-confidence, and accepted-finite states in precedence order; post-unblinding removal terminates as calibration-inconclusive with no Stage-C rerun.
- **Reverse reachability:** §7.1 still enumerates the stable `VOID` antecedents, and the orphan `VOID-6.1C2-ATTESTATION-FAIL` has zero occurrences. Clause 10 line 580 does not pretend the reverse carrier exists: it says reverse reachability is unresolved, Clause 10 is not executable, and BS-6 plus the first image byte remain blocked pending a pinned converter covering every antecedent. That is honest unresolved standing state, not false closure.
- **Catalogue thresholds:** `flux_ivar_r > 8.4000532`, `psfsize_r < 1.5699703`, and `nobs_r >= 3` remain pre-BS-2f/P2–P3 catalogue-quality predicates with nonfatal ordinary exclusion; later movement after inference/first real χ is a VOID condition.
- **Calibration/path thresholds:** any `a_LB_b < 0.85` halts pre-unblinding as calibration-inconclusive; the complementary `>= 0.85` permits Stage C. Spread `<= 0.03` selects scalar and `> 0.03` selects profile; spread is not a failure. Aggregate non-finite/degenerate input is validated before the comparison and terminates calibration-inconclusive, apart from Row I's separately named missing-output halt.
- **Power thresholds:** Stage P and Stage C retain 1,000 trials with the exact `x >= 962` PASS boundary (961 fails), one-sided 95% lower bound `>= 0.95`, and success p `< 0.001`. Stage P's 995/1000 is explicitly superseded/non-applicable to the 49,211 mask and cannot fill BS-5p. Stage-C threshold or self-verification failure halts pre-unblinding as power-inconclusive. The locked-mask `N_eq >= 100,000` floor is evaluated before a real statistic; failure has the same power-inconclusive effect.
- **Numeric verdict thresholds:** only the post-unblinding numeric helper can emit `REPRODUCED-LONGO` for p `< 0.001` plus the stated sign, three-sigma amplitude band, and evaluated detection floor; `REJECTED-AT-LONGO-AMPLITUDE` requires p `> 0.05` and the strict amplitude upper bound `< 0.0408`; every other numeric result is `INCONCLUSIVE`. Boundary equality therefore falls into neither strict p branch unless the other explicit region applies, as intended.

The held §2.7 sentence at line 378 is byte-for-byte equal between V27 and V28 and still says conditional independence is **not established**. `prereg_counts.py` reports 15 class-P and 8 class-E rows with only BS-2m claimed filled; `prereg_lint.py` reports 23 §7 data rows and no inconsistencies. Stage P remains superseded/non-applicable on both surfaces, and the first-image block remains explicit.

## Failed attacks / checks that held

1. Subject-substitution attack failed: the exact V28 bytes match the supplied digest.
2. Live-check attack failed on the present tree: the required check genuinely exits 0 with zero reported problems.
3. Table-fidelity attack failed: all complete in-band rows are byte-equal to regeneration, including both endpoints and uncapped section lists.
4. Missing-row, cross-row result-digest masking, and missing-current-sidecar canaries all fired exactly once.
5. Prohibited pass-claim search failed: §10 describes the contract and does not claim this invocation passed.
6. Sidecar-semantic attack failed: all four V27 IDs cited by V27→V28 concern only the trace/checker defect this delta addresses.
7. Held-state attacks failed: the conditional-independence limitation, Stage-P supersession, closed catalogue-quality vocabulary, orphan-ID removal, 15/8 slot counts, unresolved BS-2v, and first-image block remain intact.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`, fetch or authorize an image byte, run Stage P, execute inference, unblind anything, or mutate git.
- Survey provenance, source-data truth, 49,211/N_eq measurements, and scientific citation claims remain **Testimony** in this pass. I checked the document's values, neighboring phase/effect rules, and internal closure, not the prohibited data tree.
- Temporary gate-local mutation mirrors and the audit helper were removed after use. The subject, predecessors, checker, sidecar, source artifacts, and receipts were not modified. This report is the only durable write by this seat.

## Evidence ledger

Content read: `BRIEF_V28_WHOLE_REVIEW.md`; the complete pinned V28 subject across §§0–11; `tools/prereg_trace.py`; `gates/FINDINGS_MAP.md`; `V27_WHOLE_REVIEW_CODEX.md`; and `V27_WHOLE_REVIEW_GPT56.md`. Read-only comparisons/executions: exact V28 SHA-256; exact V27→V28 diff; required live trace check; complete generated-row equality; missing-row/current-sidecar/own-result-digest/future-transition mutation canaries; line-378 equality; orphan, Stage-P, first-image, and prohibited pass-claim searches; `prereg_counts.py`; and `prereg_lint.py`. Initial invocations using nonexistent gate-local `tools/prereg_trace.py` paths and an incomplete argument list failed before the successful documented invocation; no result from those failures was credited.

**NOT CLEAR**