# V27 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

**NOT CLEAR.** The dispatched V27 bytes exactly match the runner pin, all three ordered document repairs landed, and §2.7 line 378 is byte-for-byte unchanged from V26. The blocker is §10's new assertion that findings mapping is enforced: the actual V27 checker run is nonzero, the V27 table stops two predecessor transitions early, the current V26→V27 sidecar mapping is absent, and the checker does not enforce its own stated current-transition sidecar rule. Its zero result on V26 is therefore not evidence for the contract §10 claims.

## Digest first — exact comparison

I computed SHA-256 over the exact current bytes of `../PREREG_SUCCESSOR_DRAFT_V27_20260827.md` and compared all 64 hexadecimal digits with the `V27 PINNED sha256` value on line 5 of `runner_v27_chain.log`:

- runner pin: `e801a18bb7c489f0e4924695a13ba2f97f65a1b768c6dcc54a515cd5b31fb064`
- recomputed V27: `e801a18bb7c489f0e4924695a13ba2f97f65a1b768c6dcc54a515cd5b31fb064`
- comparison: **MATCH — exact 64-hex equality**

## Numbered findings

### 1. HIGH / BLOCKING — §10 lines 813–845, §6.3 line 611, `gates/FINDINGS_MAP.md`, and `tools/prereg_trace.py` lines 200–245 — the claimed mapping enforcement is not the described three-rule contract

**Why it fails.** V27 line 815 says: in-band coverage stops at the subject's predecessor; the current transition is mapped in `gates/FINDINGS_MAP.md`; and V1→V15 are exempt by a named checker rule. Only the historical exemption is actually enforced as stated.

1. Running the checker against V26 with the required positional arguments returns zero: `26 computed transition(s); 0 problem(s)`. But `main()` skips every transition whose destination is at or above the subject version (lines 205–207 and 234–238). For subject V26, that skips V25→V26—the transition the sidecar is supposed to own. An in-memory canary removed exactly the V25→V26 sidecar entry and reran the real `main()`; it still returned `0 problem(s)` and return code 0. Thus the named current-transition mapping is not enforced.
2. The written-row test searches the entire draft for a transition token (lines 208–210), not the §10 table. V27's actual §10 table has 23 rows and ends at V23→V24. It has no V24→V25 row and no V25→V26 row. The prose token `V24→V25` at line 611 falsely satisfies the check for that missing table row.
3. Running the checker against the V27 subject returns nonzero: `MISSING: no written row for V25 → V26`; `26 computed transition(s); 1 problem(s)`; exit 1.
4. `FINDINGS_MAP.md` ends at V25→V26. It has no V26→V27 mapping, although that is V27's current transition under the document's own sidecar rule.

The tool comments describe the desired three-part architecture, but comments are not enforcement. The zero V26 result is produced while the current mapping is skipped and an in-band row is accepted from unrelated prose. Therefore §10's unqualified “The findings mapping is enforced” assertion exceeds the check.

**Smallest sufficient repair.** Parse transition rows only from the §10 table; require actual in-band rows through V25→V26 for V27; require exactly the subject's current V26→V27 transition in `gates/FINDINGS_MAP.md`; and add a canary that removes each required in-band/current mapping one at a time and proves exactly that transition fires. Do not retain the enforcement claim until the checker exits zero on V27 under those tests.

## The three ordered repairs — independently checked against V27 bytes

1. **Catalogue quality: LANDED and internally consistent on the assigned seam.** Section 2.7 lines 336–343 now enumerates catalogue quality as pre-lock reason (c) and extends the sign-blind construction rule to (a)–(c). Row E line 539 names exact authenticated fields `flux_ivar_r`, `psfsize_r`, `nobs_r`, source digest `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3`, one-to-one keys `brickid`,`objid`, the BS-2a pinned verifier, P2–P3 phase, and nonfatal ordinary-exclusion effect. Section 5 line 489 and Row P line 550 remove `EXCLUDED-BY-CATALOGUE-QUALITY` from P8 precedence/fatal states and carry catalogue quality only as an already-resolved pre-lock status that cannot create a P8 removal. Absence, non-finiteness, and low confidence remain distinct post-unblinding states. Clause 10 line 580 and BS-2f line 709 use the same phase/effect.
2. **Stage P: LANDED.** Both live 995/1000 surfaces are explicitly `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK` (lines 292 and 448), no longer claim PASS, and lines 318 and 450 say exactly that BS-5p cannot be filled until Stage P is rerun on the actual post-exclusion mask. The historical geometry and thresholds remain labeled as historical evidence rather than current power credit.
3. **False closure/orphan VOID ID: LANDED.** The preamble no longer says VOID reachability is repaired. `VOID-6.1C2-ATTESTATION-FAIL` has zero occurrences and is absent from §7.1; Row C2's two surviving antecedents correspond to `VOID-6.1C2-CLASSIFIER` and `VOID-6.1C2-FIELD-OUTSIDE`. Clause 10 line 580 still explicitly says reverse reachability is unresolved, clause 10 is not executable, and BS-6/the first image byte remain blocked. The same first-byte block remains at lines 667–668 and in the BS-2a/BS-2v slot dependencies.

## Required carry-forward and threshold/phase/effect sweep

- V26 line 378 and V27 line 378 compare **exactly equal** as complete strings. The sentence still claims only outcome-blind chronology, explicitly says independence from handedness conditional on position is **not established**, and requires either a preregistered check or a stated assumption with risk. I found no surviving `independent of handedness` affirmative claim.
- The catalogue thresholds remain exactly `flux_ivar_r > 8.4000532`, `psfsize_r < 1.5699703`, `nobs_r >= 3`; their phase is pre-BS-2f/P2–P3 and their failure effect is nonfatal catalogue-quality exclusion into the 49,211-row mask.
- Instrument absence, non-finiteness, and low confidence remain P8 post-unblinding removals; any such removal yields `INCONCLUSIVE-BY-CALIBRATION` with no Stage-C rerun.
- Stage-P `x ≥ 962 of 1,000` remains the planning threshold, but the 995/1000 result is superseded for the operative mask and supplies no BS-5p value.
- Stage C remains on the locked 49,211-row mask with `N_eq = 110,983`; calibration lower-bound failure `< 0.85` halts pre-unblinding as `INCONCLUSIVE-BY-CALIBRATION`; fewer than 962/1,000 or self-verification failure halts as `INCONCLUSIVE-BY-POWER`.
- Numeric decision thresholds remain phase-separated in §5: p < 0.001 for `REPRODUCED-LONGO`, p > 0.05 plus the amplitude bound for `REJECTED-AT-LONGO-AMPLITUDE`, and all other numeric results `INCONCLUSIVE`.
- `prereg_counts.py` reports 15 class-P and 8 class-E rows, one filled slot BS-2m, with prose matching the table. `prereg_lint.py` reports 23 data rows and no inconsistencies. These checks do not cure finding 1 because neither enforces the trace-sidecar contract.

## Failed attacks / checks that held

1. Subject substitution failed: the current V27 digest matches the dispatch pin exactly.
2. The conditional-independence modality attack failed: line 378 is unchanged and remains explicitly open.
3. The catalogue double-removal attack failed: no `EXCLUDED-BY-CATALOGUE-QUALITY` or “catalogue quality below frozen threshold” survives in P8.
4. The Stage-P stale-PASS attack failed: both 995/1000 surfaces are superseded/non-applicable and BS-5p is blocked pending rerun.
5. The orphan-ID attack failed: the C2 attestation ID and false preamble closure phrase both have zero occurrences.
6. Standing state held: BS-2a is DESIGN/UNFILLED; BS-2v and findings 1, 2, 2b and 3 remain unresolved; Rows C2/E cannot run; BS-6 and the first image byte remain blocked; one of fifteen class-P slots is filled.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`, fetch or authorize any image byte, run Stage P, execute inference, or touch χ-bearing work.
- Survey provenance, threshold-source authenticity, the reported 49,211/N_eq measurements, and scientific citation claims are **Testimony** in this pass. I checked their document-level values, phases, effects, and neighboring clauses, not external survey/data truth.
- I did not modify the subject, predecessors, checker, findings map, receipts, or code. The only intended lane write is this report.

## Evidence ledger

Content read: `BRIEF_V27_WHOLE_REVIEW.md`; `runner_v27_chain.log`; the complete pinned V27 draft across §§0–11; both V26 whole-review reports; `gates/FINDINGS_MAP.md`; and the complete repository `tools/prereg_trace.py` source. Programmatic/read-only checks: SHA-256 of V27; exact V26→V27 diff; exact line-378 equality; whole-document searches for catalogue-quality phase/effect, Stage-P status, independence language, reverse reachability, orphan IDs, and first-byte blocks; actual §10-row parsing; `prereg_counts.py`; `prereg_lint.py`; checker runs on V26 and V27; and an in-memory removal canary for the V25→V26 sidecar mapping.

**NOT CLEAR**