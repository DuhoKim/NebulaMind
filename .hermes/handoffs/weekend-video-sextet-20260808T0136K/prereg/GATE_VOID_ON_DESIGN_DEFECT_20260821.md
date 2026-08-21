REFUTED_VOID_ON_DESIGN_DEFECT

# Adversarial gate — VOID-on-design-defect declaration

## Verdict

The declaration is REFUTED as a valid disposition of the frozen preregistration. The scientific design-defect allegation survives: the literal HC-6 method is footprint-blind and can PASS on this footprint, while the footprint-aware fixed-position calculation cannot reach 0.95 power even at `a = 1`. But the frozen text provides no lane- or investigator-declarable `VOID` category for a newly discovered design defect. It provides `void` only as a consequence of named events: a post-statistic parameter change under F-9/K-8, and specified HC-7 batch/measurement integrity failures. None is alleged here. Renaming the previously rejected post-freeze choice from `INCONCLUSIVE-BY-POWER` to `VOID` does not cure the choice.

A second independent refutation is factual. `CHI_CUSTODY_RECEIPT_20260821.md` does not discharge finding 4 of the prior gate. Two already-published reports disclose the first three real chi values (approximately `+0.27`, `+0.20`, `-0.20`) and a sign/committee summary. That directly contradicts the receipt's claims that exactly one individual value was published, no summary artifact exists, and the K-8 blind is intact.

The cleaner rival path in the brief is superior: preserve the literal HC-6 report, including a PASS, and let Duho decline to proceed as a human decision outside the preregistration. That records what the frozen gate says without inventing a fifth decision region or a new post-freeze `VOID` procedure.

## 1. Weakest joint — `VOID` is the refuted procedure in a different coat

### 1.1 What the frozen text actually defines

The exhaustive F-6 outcome set is (`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md:141-145`):

- `REPRODUCED-LONGO`;
- `REJECTED-AT-LONGO-AMPLITUDE`;
- `INCONCLUSIVE`;
- `INCONCLUSIVE-BY-POWER`, only if the section 5 power gate fails before unblinding, with no run.

`VOID` is not a fifth outcome and is not a status an actor may declare because a defect is disclosed. The frozen file's complete substantive uses of `void` are consequences with frozen predicates:

1. changing the output boundary, hand-check protocol, or input contract after a real-sky statistic “voids the run” (`:51-53`);
2. F-9: any parameter change after any real-sky statistic “voids the run,” with re-entry only through a new preregistration (`:156-157`);
3. HC-7: specified key/sampling/exposure failures can make an affected batch or measurement void (`:311-318`).

The declaration alleges none of those predicates. It expressly says no frozen parameter is changed, no HC-7 event occurred, and no preregistered outcome or section 5 failure is claimed (`DECLARATION_VOID_ON_DESIGN_DEFECT_20260821.md:9-14,33-46`). Therefore the frozen text supplies no route from “design defect discovered” to `VOID`.

The last paragraph does not cure this. It says the document only requests Duho's decision (`:100-103`), but the operative text already says “the run is VOID,” “this is a void,” and “The run is void” (`title`, `:43-46`, `:78-83`). Duho can decline a study; accepting a post-freeze document cannot make an unfrozen category into a preregistration event.

### 1.2 The identical post-freeze discretion remains

The prior gate held that the frozen method must be executed even when a scientifically superior footprint-aware method points elsewhere. This declaration accepts that holding, says it “needs no reading of HC-6 at all” (`:33-34`), and then reaches the same practical disposition—do not run the verdict estimator—by a new label (`:78-83`). That is still a post-freeze choice made after learning the mismatch.

The category change is substantive only in name:

| Refuted draft | Current declaration | Material substance |
|---|---|---|
| Refuses literal HC-6 because it can PASS | Says HC-6 need not be read and calls the design `VOID` | The frozen PASS-capable procedure is bypassed in both |
| Uses the footprint-aware SSE/power result to stop | Uses the same geometry/power mismatch to stop | Same evidence performs the same disposal function |
| “No run” / no dipole aggregate | “will not be run on real chi under this preregistration” | Same withheld frozen analysis |
| Acquisition continues through real chi | Acquisition continues to completion | Same data-acquisition plan |
| Estimator built and hash-frozen | Estimator built and hash-frozen | Unchanged |
| Same Longo/sky/BHU boundaries | Same Longo/sky/BHU boundaries | Unchanged in substance |
| Same contiguous-BRICKID causal narrative | Same narrative, with caveats | Unchanged core narrative |
| Draft effective only after gate and Duho | Draft effective only after gate and Duho | Same approval wrapper |

Material improvements do exist: the current declaration retracts the F-6 outcome claim, correctly states that Revision 3's present bytes were not gated, and correctly impeaches the estimator/power protocol rather than blaming the footprint alone. Those corrections do not create a frozen `VOID` procedure.

## 2. Literal HC-6 execution and the rival path

### 2.1 The literal method can report PASS

The pinned source does exactly what the declaration says:

- uniform-sphere generation: `costheta = np.random.uniform(-1, 1, N)` (`../spike/sim_power.py:5-9`);
- two-sided analytical p-value: `p_val = 2 * (1 - stats.norm.cdf(z))` (`:76-92`);
- sphere normalization: `mean(cos^2) = 1/3` (`:96-106`).

HC-6 freezes direct analytical evaluation of that logic at `A_eff=(2a-1)*0.0408` and the bound/realized `N`, then re-evaluation by the same method at the lower-bound hand-check `a` (`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md:319-329`). It does not name accepted-position variance or SSE as an input.

I executed the literal two-sided normal calculation at the frozen minima `N=100,000`, `a_LB=0.85`:

- `A_eff = 0.02856000`;
- `sigma_D = sqrt(1/(3N)) = 0.001825741858`;
- two-sided `alpha=0.001` critical z = `3.290526731492`;
- noncentrality = `5.214318747449`;
- noncentrality required for 0.95 power = `4.935380358443`;
- power = `0.972809670700`;
- literal result: **PASS**.

The associated HC-5 break-even at `N=100,000` is `a_gate=0.831276856886`, below the independently frozen `0.85` quality floor. Thus, conditional on the other HC-5 floors and the `N_accepted >= 100,000` requirement passing, the literal uniform-sphere HC-6 calculation passes even at its least favorable permitted `N,a` pair. At the parent count `N=208,407`, the same literal calculation gives power `0.999988674934` at `a=0.85`.

The final realized HC-6 record cannot yet be produced because realized accepted `N` and the hand-checked lower-bound `a` do not yet exist. That uncertainty does not defeat the declaration's narrower existential claim that the frozen gate can PASS on this footprint. It can, and the minimum-permitted calculation demonstrates it.

### 2.2 Defect claim ruling

The design-defect claim is true in the narrow form that matters: literal HC-6 is blind to footprint geometry and therefore can certify its assumed uniform-sphere power without certifying fixed-position power on the measured footprint. The independently gated geometry gives `Var(c)=0.05798463739809634`, versus `1/3`, and an equal-power multiplier `1/(3 Var(c))=5.748649095532`. The footprint-aware upper-bound calculation remains below 0.95 power even at `a=1`.

The sentence “A gate that cannot fail for the reason it exists is not a gate” is rhetorically broader than the evidence. HC-6 can fail for low `N` or low `a`; what it cannot detect is inadequate accepted-position leverage. This imprecision does not refute the defect, but neither does the defect authorize `VOID`.

### 2.3 Rival-path ruling

The rival path is cleaner than declaring void. Literal execution preserves the preregistered record, including a PASS if that is what the frozen method reports. Duho's subsequent decision not to proceed is an investigator decision outside F-6: it does not assert a frozen outcome, does not reinterpret HC-6, and does not manufacture a declarable `VOID`. This conclusion answers the brief's stated rival-path comparison; it is not a proposed redesign or estimator remedy.

## 3. `CHI_CUSTODY_RECEIPT_20260821.md` does not discharge prior finding 4

### 3.1 Artifact inventory — PARTIAL and presently unreconciled

A names/counts-only directory listing of `/Users/duhokim/NebulaMindData/chi_dr10_south/` found exactly three directories in the walk and the same top-level item names the receipt lists:

- top level: `results.jsonl`, `chi_heartbeat.json`, `chi_wrapper.log`;
- `_wrapper/`: `batch_manifest.txt`;
- `receipts/`: per-object receipt files.

However, the current receipt-file count is **39,135**, not the receipt's **39,137** (`CHI_CUSTODY_RECEIPT_20260821.md:17-21`). The receipt is a timestamped snapshot, so a later count cannot by itself prove its historical count false; but it supplies no immutable inventory binding the alleged 39,137 files and no deletion/reconciliation record. Its count cannot be independently reproduced now. The claimed `39,135` row count in `results.jsonl` was deliberately not checked because the brief forbids opening that file. It remains HOLD.

The inventory establishes names, not absence of a statistic hidden under a neutral filename. It cannot by itself prove “per-object records only.”

### 3.2 Negative sweep — does not prove the stated universal

The receipt says every filename hit for `dipole`, `tertile`, `aggregate`, `strata`, `A_hat`, or `verdict` across NebulaMindData and the whole lane belongs to one of three categories (`:25-35`). My names-only rerun found:

- zero matching names under `/Users/duhokim/NebulaMindData`;
- 177 matching names in the whole weekend-video lane.

Those lane hits are not all in the three stated categories; they also include BHU phase files, integrator products, C41 QA verdicts, research-source figures, and review artifacts. They are not thereby real-chi aggregates, but the receipt's exhaustive classification is false as written. More importantly, a filename sweep cannot exclude a real-chi summary stored under a neutral name such as `report-...html`. That exact failure occurred here.

### 3.3 Four code paths — current production sources are aggregate-free, but the universal is overstated

The four-file statement (`:37-48`) mixes different classes:

- `inference_runner.py` is the per-object producer, not a reader of a fixed chi tree;
- `chi_wrapper.py` reads the ledger but uses only `input_tensor_sha256` and counts;
- `test_inference_runner.py` uses synthetic test fixtures;
- `nm_report_graphics.py` is the real external reader.

A source search for `chi_dr10_south|chi_value` found six Python files, not four: the four named files plus `_rehearsal_20260820/run_rehearsal.py` and `verify_rehearsal.py`. The rehearsal files are synthetic and do not reference the real chi tree, so they do not show a real-sky aggregate; they do refute the literal claim that only four files reference either token. No matching shell, JavaScript, TypeScript, or MJS code was found in `prereg/` or HermesOps.

Direct source audit did confirm the narrower current-code claims:

- `inference_runner.py:373-442` computes/writes one chi per input and only returns processed/resumed counts;
- `chi_wrapper.py:31-72` parses ledger rows only to collect input hashes and count objects;
- `pipeline_chain()` counts ledger lines and does not inspect chi values (`nm_report_graphics.py:354-416`);
- `receipt_card()` loads every ledger row, selects `rows[h % len(rows)]` from a seed-derived index, and renders one selected value (`:419-478`). The selection is independent of value and is not an order statistic.

This supports “the inspected current Python paths contain no chi aggregate.” It does not support “no code path in existence computes one,” especially in light of the published artifacts below.

### 3.4 Single published value and no-summary claims — REFUTED by published reports

The named exemplar exists and contains the exact value/raw bits stated by the receipt. Searching the status-audio archive found that exact value in the report page and its archive embedding, which are two surfaces carrying one disclosure.

But an earlier already-published report directly contradicts the receipt:

- `report-20260820T231235-hwao-report.html:70` says: “**The first 3 real values: zero point 27, zero point 20, and minus zero point 20. One leaning each way among the confident pair.**”
- `report-20260820T231324-hwao-report.html:70,79` repeats the aggregate disclosure: “**3 galaxies were read tonight, one leaning each way among the pair the committee was confident about**.”
- `archive.html:153-154` retains both reports.

These are not synthetic rehearsals: both reports expressly call them the first real measurements. The first report publishes three approximate individual real chi values. Both publish a sign/committee summary over multiple real measurements. Therefore all of the following custody-receipt claims fail:

- “no ... summary over real-sky chi exists” (`CHI_CUSTODY_RECEIPT_20260821.md:8-9`);
- “Exactly one individual chi value has been published” (`:8-9,60-69`);
- “No other individual value has been rendered anywhere” (`:67-69`);
- the declaration's inherited claim that the blind is intact (`DECLARATION_VOID_ON_DESIGN_DEFECT_20260821.md:53-59`).

The custody receipt also misattributes its quotation. K8 condition 1 is specifically the partial-tertile prohibition (`K8_CROSSING_AUTHORIZATION_20260820.md:28-31`). “No sky statistic, no dipole, no summary over chi” is condition 2 (`:32-33`), and “unblinding anything” is separately not authorized in section 4 (`:46-50`). The receipt combines these and attributes the composite to condition 1 (`CHI_CUSTODY_RECEIPT_20260821.md:76-80`).

The published disclosures do not establish that a dipole or tertile was computed, and I found no evidence of either. They do establish inspection/publication of individual values and a multi-object summary, which is enough to defeat the receipt's stated custody result and the declaration's blind-intact premise.

## 4. “Acquisition continues” against F-6 and K8

The current declaration no longer claims an F-6 outcome or HC-6 failure. Therefore F-6's `INCONCLUSIVE-BY-POWER → no run` clause is not triggered by the declaration as written. Incremental per-object chi acquisition is expressly authorized by K8 conditions 1-2, provided there is no partial tertile, aggregate/summary, or unblinding and the gated-code/stop conditions hold (`K8_CROSSING_AUTHORIZATION_20260820.md:26-44`). In that abstract procedural sense, “acquisition continues” is no longer internally inconsistent with F-6.

The live custody predicate is not cleared, however. The published three-value and sign/committee disclosures violate K8's no-summary/no-unblinding boundary. The assigned record does not establish a parameter change, so this gate does not convert that disclosure into an F-9 void. It does mean the declaration cannot truthfully use “the blind ... is intact” to support continued custody. Whether continuation remains authorized after that breach is HOLD on the assigned text.

## 5. Integrity sweep

### 5.1 Quotations and source characterizations

- “the same analytical method” is exact frozen wording (`PREREG...V3.md:327-329`).
- The prior gate's “conservative outcome” reasoning is preserved accurately in substance (`GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md:37-45`).
- `costheta = np.random.uniform(-1, 1, N)` and the `mean(cos^2) = 1/3` comment are present in `sim_power.py:5-9,96-106`.
- The declaration's claim that `sim_power.py` is two-sided while F-3 is one-sided is exact (`sim_power.py:76-92`; preregistration `:134-135`).
- The K8 condition-1 attribution inherited from the custody receipt is inaccurate, as detailed above.

### 5.2 Self-correction 1 — Revision 3's current bytes were not gated: ACCURATE

Current SHA-256 values independently computed:

- Revision 3 finding: `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`;
- first gate: `1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1`;
- re-gate: `aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b`.

The re-gate records the finding bytes it reviewed as `a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76` (`GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md:272-284`), not the current Revision 3 hash. It gated Revision 2 and returned HOLD. The first gate predates Revision 2/3 and also returned HOLD. The declaration now states this correctly (`DECLARATION_VOID...md:48-51`). “Supporting, twice-gated” remains loose artifact language, but the immediately following exact-byte correction prevents the previous false claim.

### 5.3 Self-correction 2 — estimator/power protocol is impeached: ACCURATE

Revision 3 and the two prior gates support all three limbs:

- F-1's `3*D_hat` normalization does not transfer to the measured footprint's second moment;
- F-4 and F-7 inherit the uniform-sphere `1/3` machinery;
- the power source is two-sided while frozen F-3 is one-sided.

The current wording properly limits what remains untouched to classifier mechanics, tau, antisymmetry receipts, committee, and hand-check mechanics. It no longer says the statistical estimator/power protocol or custody chain is unimpeached.

### 5.4 “What is NOT claimed”

- **Longo:** the boundary holds, but its rationale says the instrument “could not reach the preregistered power” (`DECLARATION_VOID...md:63-64`). That is overbroad because literal preregistered HC-6 reaches PASS; only the footprint-aware scientific-power calculation cannot reach 0.95. The declaration itself proves this distinction.
- **Sky:** properly bounded and consistent with the canonical sentence.
- **BHU:** properly bounded. The frozen headline says the test does not test BHU (`PREREG...V3.md:84-86`), while the prior gate records Duho's 2026-08-21 confirmation that the lane is inside the BHU programme as scope/motivation, not evidence for or against a BHU model (`GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md:104-116`). The current paragraph states both facts and neither erases scope nor promotes this result.
- **Instrument mechanics versus statistics:** accurately separated, subject to the failed custody claim elsewhere.

The `0.7 TB` figure remains HOLD. The declaration says it is not relied upon (`:94-98`) but still uses it in the operative acquisition rationale (`:78-83`). Disclaiming reliance does not verify the number. It is not needed for this verdict.

## 6. Failed attacks

- **Scientific-defect attack failed:** the footprint/statistical-machinery mismatch is real.
- **Literal-PASS attack failed:** the frozen two-sided method reports power `0.972809670700` even at `N=100,000`, `a=0.85`.
- **Geometry-number attack failed:** `5.7486` is the correct full-sphere equal-power multiplier for the frozen harness comparison.
- **Revision-status correction attack failed:** current Revision 3 bytes truly were not gated.
- **Estimator-impeachment correction attack failed:** the current declaration accurately broadens the defect beyond the footprint alone.
- **Abstract acquisition/F-6 attack failed:** once no F-6 outcome is claimed, F-6's no-run clause is not triggered.
- **BHU-boundary attack failed:** programme scope and evidentiary non-inference are both stated.

These failed attacks do not rescue the declaration because the declarable-`VOID` procedure is absent and the custody premise is factually false.

## 7. Evidence ledger and hard boundaries

Read as content:

- `DECLARATION_VOID_ON_DESIGN_DEFECT_20260821.md` — SHA-256 `e55460743358bbb0b8c16b8d99e5f4260d0f57a88096dc2c0328f6a675b805ba`;
- `DECLARATION_INCONCLUSIVE_BY_POWER_20260821_REFUTED.md` — `af51507a43fcdee4e53b51502c332e3624611bb27de6d0bede120b33c8b38ebb`;
- `GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md` — `94ac81d7bef75b8a7daca1abd515ceff4fff31c6f21d2c2ce7375027d9c4e79e`;
- `CHI_CUSTODY_RECEIPT_20260821.md` — `7617ae7f0935b634e0052267dcf4afa5a6857bad0c08850b531d357d8a3c1d6e`;
- `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md` Revision 3 — `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`;
- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` — `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`;
- `K8_CROSSING_AUTHORIZATION_20260820.md` — `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`;
- both footprint gate reports;
- `../spike/sim_power.py` and `GORU_BS8_POWER_RECEIPT_20260814.md` for literal HC-6 source/receipt verification;
- `_inference_20260820/inference_runner.py`, `chi_wrapper.py`, and relevant synthetic test/rehearsal references;
- `/Users/duhokim/HermesOps/scripts/nm_report_graphics.py`;
- the already-published status reports `report-20260820T231235-hwao-report.html`, `report-20260820T231324-hwao-report.html`, `report-20260821T004950-hwao-report.html`, and archive search results.

Mechanical checks:

- byte diff of the refuted and current declarations;
- SHA-256 computation for all named gate inputs and both footprint gates;
- literal two-sided HC-6 normal-power evaluation at frozen minima and parent-count examples;
- names/counts-only chi-tree inventory;
- names-only negative sweep across NebulaMindData and the whole weekend-video lane;
- source searches for chi-tree/value references across Python, shell, JavaScript, TypeScript, and MJS;
- exact-value, raw-bit, receipt-card, and prior-disclosure searches across the published report archive;
- read-only git status before the pass.

Boundary statement: no file under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened or read. Only directory names and file counts were listed; no chi value was obtained from that tree and no statistic was computed from it. All chi values cited in this report came from already-published HTML reports, as the brief permits. `SUCCESSOR_SCOPE_20260821.md` was not opened or reviewed. No remedy or estimator redesign is proposed. No analysis temp was created by the audit commands. The permitted launcher/session logs `_tmp_gate_void_stdout.log` and `_tmp_gate_void_stderr.log` were born at 18:34:33 KST, before the report write at 18:44:10; the zero-byte stderr log remained unchanged while the launcher updated stdout. Under `prereg/`, this gate's substantive deliverable write was only `GATE_VOID_ON_DESIGN_DEFECT_20260821.md`.
