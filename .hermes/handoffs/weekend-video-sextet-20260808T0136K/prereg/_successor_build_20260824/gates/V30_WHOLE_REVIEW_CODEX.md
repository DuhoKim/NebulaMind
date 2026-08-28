# V30 WHOLE-DOCUMENT REFEREE REVIEW — CODEX

## Verdict

**NOT CLEAR.** I independently verified the named V30 bytes, diffed them against the exact V29 bytes I previously cleared, read all 878 lines of V30, checked the added literature against the cited arXiv records, and ran all three required tools. The Land null is a legitimate and useful counter-anchor, and the surrounding wording does not dishonestly imply that this preregistration expects a null or brush the null aside. Two blockers remain: the new 15%-versus-4% sentence compares a direction-independent handedness excess with a dipole amplitude and thereby implies estimator danger that the cited number does not establish; independently, the required trace checker fails with two concrete transition-custody defects. This verdict does not authorize any run, image acquisition, unblinding, or other blocked work.

## Digest and predecessor comparison

Subject: `../PREREG_SUCCESSOR_DRAFT_V30_20260827.md`

- supplied V30 SHA-256: `e81becce1b19d88a302ce7004e930467d9b12b24828bcfe037913a2eb978fecc`
- independently recomputed V30 SHA-256: `e81becce1b19d88a302ce7004e930467d9b12b24828bcfe037913a2eb978fecc`
- comparison: **MATCH — exact 64-hex equality over the named current V30 bytes**
- supplied predecessor V29 SHA-256: `542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343`
- independently recomputed predecessor V29 SHA-256: `542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343`
- comparison: **MATCH — the predecessor is the exact V29 byte state previously cleared by CODEX**

The unified diff contains only the V29→V30 retitle and the three new §1 paragraphs, with their separating blank lines. No pre-existing normative text changed. In particular, V29's §1 scope block (V29 lines 125–127) is byte-identical at V30 lines 131–133, and V29 §2.7 line 378 is byte-identical at V30 line 384.

## Numbered findings

### 1. HIGH / BLOCKING — §1 line 120 — the “nearly four times” comparison conflates a monopole with a dipole

**Why it fails.** The arithmetic itself is correct: `15 / 4.08 = 3.676470588235`. The quantities are not commensurate in the way the prose uses them. Longo's `0.0408` is the coefficient of a direction-dependent `cos θ` dipole term. The approximately 15% Galaxy Zoo 1 figure is a direction-independent net excess of one assigned winding sense—a classification-bias intercept. V30 says that this bias “was nearly four times the signal being sought” and immediately uses that ratio to convert the mirror test into a prerequisite. A constant intercept can be large without contaminating the centred dipole slope. The lane's own `FRAMING_LEVERAGE_IS_IDENTIFIABILITY_20260828.md` states exactly that distinction: flat classification bias is the intercept, a true dipole is the slope, and leverage separates them. The 15% observation is good evidence that this classification task can carry a substantial parity-label bias and therefore supports an antisymmetry audit; its magnitude does not establish a 3.7× threat to the dipole estimator. Only a position-dependent bias component aligned with `cos θ` would do that work, and the cited 15% aggregate does not measure such a component.

**Smallest sufficient repair.** Remove the direct 15%-versus-4.08% ratio and the claim that it is “nearly four times the signal.” Retain the honest provenance and motivate BS-3 qualitatively, while stating the estimand distinction. For example: “A later reanalysis reports an approximately 15% uncorrected net handedness asymmetry in Galaxy Zoo 1. That task-specific bias motivates making the mirror/antisymmetry audit a prerequisite. The aggregate is a monopole and is not directly comparable to Longo's 0.0408 dipole amplitude; bias threatens the dipole estimate only to the extent that it varies with position along the tested axis.”

### 2. HIGH / BLOCKING — §10 lines 819–861 and `gates/FINDINGS_MAP.md` — the required trace check fails

**Why it fails.** I ran the required checker rather than accepting testimony. It exited 1 and reported exactly:

```text
prereg trace check — PREREG_SUCCESSOR_DRAFT_V30_20260827.md
  MISSING: no §10 table row for V28 → V29
  SIDECAR MISSING: V29 → V30 is the current transition and is not mapped in gates/FINDINGS_MAP.md
  29 computed transition(s); 2 problem(s)
```

This is not inherited from the cleared V29 execution: the same checker passed V29 with 28 transitions and zero problems. Under V30's own §10 contract, V28→V29 is now a predecessor transition and must be represented in-band, while V29→V30 is the current transition and must be mapped in the external sidecar. The current `FINDINGS_MAP.md` ends at `V28→V29: CODEX-V28-1`; it has no V29→V30 entry.

**Smallest sufficient repair.** In the next document revision, add the generated V28→V29 row to the §10 table with its own predecessor/result digests, section delta, row counts, and finding mapping. Add an externally grounded V29→V30 entry to `gates/FINDINGS_MAP.md` naming the human motivation direction and/or exact review finding that justified the §1 addition. Re-run `tools/prereg_trace.py --check` and require exit 0 before re-review.

## Added-motivation adjudication

1. **Null-as-motivation attack — held, apart from Finding 1.** The Land paragraph is a real counter-anchor rather than a decorative citation. It gives the null first, quotes the directly checked abstract, and preserves the immediate scope statement that this preregistration tests Longo's published fixed-axis amplitude—not Shamir and not whether the sky is isotropic. The document's symmetric decision regions still permit reproduction, rejection at the Longo amplitude, or inconclusive outcome. A fresh reader is not told that the study expects a null, nor is the null brushed aside.

2. **Primary-source fidelity attack — held.** arXiv:0803.3247's current abstract states a sample of approximately 37,000 spirals, “consistent with statistical isotropy,” “no significant dipole signal, and thus no evidence for overall preferred handedness,” and that other results “may also be affected and explained by a bias effect.” V30 line 118 reproduces these claims faithfully and identifies the source as a counter-anchor.

3. **15% provenance-label attack — held as provenance, not as interpretation.** arXiv:2302.06530's body explicitly describes the original Galaxy Zoo manual-annotation difference as approximately 15%. V30 does not pretend that number was read from Land's body; it says it comes from a later reanalysis. The adjacent next paragraph identifies arXiv:2302.06530. That disclosure is honest and sufficient to locate the number. Finding 1 is about what V30 infers from the number, not whether the number was fabricated or misattributed.

4. **Unresolved subset-size attack — held.** A whole-file search for `91,303`, `91,303` without punctuation, `11,000`, `11,000` without punctuation, `~11`, and `≈11` returned zero matches. Neither disputed subset-size figure appears in V30. The only new Land sample size is the approximately 37,000 figure present in the primary abstract.

5. **“The literature is split” tilt attack — held.** The ordering gives the null the fuller treatment, then describes the later result with the appropriately attributed verb “argues.” arXiv:2302.06530's abstract does report non-randomness, dipole fits at 2.33σ–3.97σ, and agreement with other methods. Calling the record “split” is even-handed enough; it neither promotes the reanalysis to settled fact nor treats the Land null as dispositive.

## Whole-document attacks that held

1. **Standing-state honesty held.** V30 remains explicit that it is a draft not in force; BS-2a is DESIGN/UNFILLED; exactly one of fifteen class-P slots is filled; BS-2v and findings 1, 2, 2b and 3 remain unresolved; Rows C2 and E cannot run; Stage P remains `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK`; BS-5p remains unfillable pending rerun; and BS-6 plus the first image byte remain blocked.

2. **§1 scope preservation held.** The added motivation does not broaden the estimand. The original three-line scope block is byte-identical after the insertion and still excludes testing Shamir, A≈0.02, BHU, or whether the sky is isotropic.

3. **§2.7 conditional-independence disclosure held.** The required V29 line 378 survives byte-identically as V30 line 384: conditional independence of the catalogue-quality predicate from handedness given position is “not established,” with the check-or-stated-assumption duty preserved.

4. **Clause 10 and execution-block posture held at prose level.** V30 still says `VOID` reverse reachability is unresolved, Clause 10 is not executable, and BS-6/first image byte remain blocked. This does not cure the separate transition-trace failure in Finding 2.

5. **Population/power/calibration boundaries held.** The 49,211-row mask, `N_eq = 110,983`, 1,000-trial Stage P/C contract, `x ≥ 962` pass boundary, pre-unblinding `a_LB_b < 0.85` calibration halt, and no post-attrition Stage-C rerun remain unchanged from the exact V29 bytes previously cleared.

## Required tool runs

All commands were run from the assigned absolute `gates` directory.

### `tools/prereg_lint.py`

Command:

```text
python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py ../PREREG_SUCCESSOR_DRAFT_V30_20260827.md --gates .
```

Exit code 0; stdout:

```text
prereg lint — PREREG_SUCCESSOR_DRAFT_V30_20260827.md
  §7 data rows: 23 (15 class P, 8 class E) — 22 carry a BS- identifier
  no inconsistencies found (all 6 checks demonstrated they can fail)
```

### `tools/prereg_lint.py --self-test`

Command:

```text
python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py ../PREREG_SUCCESSOR_DRAFT_V30_20260827.md --gates . --self-test
```

Exit code 0; stdout:

```text
prereg lint self-test — PREREG_SUCCESSOR_DRAFT_V30_20260827.md
  OK   check_repair_citations: control fires
  OK   check_prose_counts: control fires
  OK   check_class_agreement: control fires
  OK   check_lock_identity: control fires
  OK   check_list_numbering: control fires
  OK   check_slots_exist: control fires
  self-test: 6 controls, 0 failure(s)
```

### `tools/prereg_trace.py --check`

Command:

```text
python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_trace.py .. --check ../PREREG_SUCCESSOR_DRAFT_V30_20260827.md
```

Exit code 1; stdout is quoted in Finding 2. This is independently blocking.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch or authorize any image byte, run Stage P/C, execute inference, unblind anything, modify V29 or V30, or mutate git.
- Survey custody, the historical assertion that no image byte was fetched, the measured 49,211/`N_eq` values, and implementation claims outside the required checkers remain **Testimony** in this pass.
- I verified the Land and McAdam–Shamir literature statements against the public arXiv abstract/full-text surfaces. I did not independently reproduce their analyses.
- The repository already had extensive unrelated modified and untracked state. This report is my only intended durable write.

## Evidence ledger

Content read: `BRIEF_V30_REVIEW.md`; all 878 lines of V30; the exact V29 predecessor; the V29 CODEX whole-document review; `FRAMING_LEVERAGE_IS_IDENTIFIABILITY_20260828.md`; relevant `FINDINGS_MAP.md` entries; arXiv:0803.3247 abstract; arXiv:2302.06530 abstract and relevant full-text passages.

Independent executions: V30 and V29 SHA-256; unified V29→V30 diff; byte comparisons of the §1 scope block and V29 line 378/V30 line 384; whole-file searches for the disputed subset sizes and all new motivation terms; `15/4.08`; required lint; required lint self-test; required trace check; pre-write git status.

**NOT CLEAR**