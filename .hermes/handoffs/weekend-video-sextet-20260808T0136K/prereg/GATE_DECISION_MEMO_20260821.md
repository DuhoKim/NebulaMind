REFUTED_DECISION_MEMO

# Adversarial gate — decline-to-proceed decision memo

## Verdict

The memo is **REFUTED as an accurate decision record**, although its central procedural theory survives: the frozen preregistration contains no anti-abandonment clause, no command to reach a decision region once acquisition begins, and no unconditional duty to produce an outcome. An investigator may therefore stop for an external reason without converting that reason into HC-6, F-6, or a new preregistered category. Using the footprint-aware calculation as the investigator's reason is not the same as substituting it for HC-6, provided the record continues to say that HC-6 was not executed and no frozen outcome was issued.

The memo nevertheless fails on multiple material facts. It repeats the false claim that Revision 3's current bytes were “twice gated”; it falsely says final `a` is measured by a 150-label hand-check and that `a` would have only one use; and it relies on a Revision 2 custody receipt whose principal correction is itself false. The already-published 23:12 report literally contains “The first 3 real values: zero point 27, zero point 20, and minus zero point 20.” The memo omits that disclosure, mislabels the sign-summary breach as K-8 condition 1 rather than condition 2, and says the 23:13 report followed the 22:20 authorization by 43 minutes when the interval is 53 minutes. A memo claiming to put the study's integrity failures “on its face” cannot pass while materially understating and misdescribing the published breach.

This verdict refutes the memo's factual and custody integrity. It does **not** rule that Duho lacks authority to decline the study, does not turn the footprint-aware analysis into a frozen outcome, and does not propose a remedy.

## Ranked findings

### 1. BLOCKING — Custody Revision 2 is factually refuted by the published report it claims to have searched

`CHI_CUSTODY_RECEIPT_20260821.md:10-17` says the challenging gate fabricated the `+0.27/+0.20/-0.20` disclosures, that those values “do not exist,” that the only numeric chi ever rendered is `0.013161621987819672`, and that the second named report is Tori's and has no chi content. Each proposition fails against the already-published source:

- `report-20260820T231235-hwao-report.html:2,57-58` identifies the page as **Hwao's** 23:12 report.
- Its caption at `:69-70` says verbatim: **“The first 3 real values: zero point 27, zero point 20, and minus zero point 20. One leaning each way among the confident pair.”**
- The saved authored text, `20260820T231235-hwao-report.txt:1`, contains the same sentence.
- `archive.html:154` retains the same disclosure as a published Hwao report.
- The values are ordinary prose in the report caption and authored text, not `data-t` audio cue arrays and not substring matches inside “achieves” or “chip.”

The corresponding deck omits the three values, but that does not erase them from the report page, narration text, audio, and archive. Revision 2's claimed exhaustive report/deck/archive search therefore missed the exact evidence it was written to adjudicate.

Revision 2 consequently does **not** discharge finding 4 of `GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md`, and the memo's integrity disclosure at `DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md:76-83` is incomplete. It carries only the sign summary from the 23:13 report and omits the three approximate individual values disclosed one minute earlier.

### 2. BLOCKING — the memo regresses to a process claim both predecessor gates had already rejected

The memo calls `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md` Revision 3 “twice gated and never refuted” (`DECISION_MEMO...:40`). That is false as exact-artifact custody language:

- current Revision 3 SHA-256 is `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`;
- the re-gate records that it reviewed Revision 2 SHA-256 `a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76` (`GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md:272-284`);
- the first gate predates Revisions 2 and 3;
- both footprint gates returned HOLD, not PASS;
- `GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md:73-89` and `GATE_VOID_ON_DESIGN_DEFECT_20260821.md:169-177` explicitly record that Revision 3's present bytes were not gated.

Revision 3 faithfully carries calculations and repairs derived by the prior gates, and its scientific footprint finding survives this pass. That does not make its current bytes “twice gated.” The VOID predecessor had corrected this point; the memo reintroduces it.

### 3. BLOCKING — the memo misstates the frozen hand-check and the role of `a`

The memo says the second HC-6 firing waits on “the 150-label hand-check” and describes proceeding as asking Duho to label 150 galaxies to measure an `a` whose “only use” is feeding HC-6 (`DECISION_MEMO...:27-29,51-54`). The frozen text says otherwise:

- full HC-1H is **850 blinded labels**: 500 real, 200 synthetic injections, and 150 mirrored re-presentations (`PREREG...V3.md:279-284`);
- the optional **150-label pilot** has only `PASS-TO-FULL-HC1H` or `INCONCLUSIVE` outcomes, and its 40 synthetics never enter final epsilon (`:331-333`);
- final `a` is the HC-1H synthetic-error-corrected attenuation estimate (`:290-300`);
- `a` is not used only by HC-6: it corrects `A_c` in F-1 (`:130-131`), enters `sigma_ours` and `sigma_comb` in F-4 (`:136-137`), enters both F-6 decision regions (`:141-145`), and sets the F-7 floor (`:146-150`).

The narrower statement that final HC-6 cannot yet fire is supportable because final accepted `N` and the full hand-checked lower-bound `a` do not yet exist. The memo's stated 150-label mechanism and single-use cost argument are not.

### 4. MATERIAL — the custody breach is quoted accurately in part but attributed and timed inaccurately

The sign-summary quotation is accurate. `report-20260820T231324-hwao-report.html:70,79` and `20260820T231324-hwao-report.deck.json:15-23` say that three galaxies were read and that there was “one leaning each way among the pair the committee was confident about.” That is a summary over chi signs.

The surrounding memo claims are inaccurate:

1. **Wrong condition.** K-8 condition 1 is the partial-tertile prohibition (`K8_CROSSING_AUTHORIZATION_20260820.md:28-31`). The no-summary rule is condition 2 (`:32-33`). The published individual values and any unblinding/publication also cross section 4's explicit non-authorization (`:46-50`).
2. **Wrong elapsed time.** K-8 is timestamped 22:20 KST (`:3-4`); the cited report is 23:13 KST (`report-20260820T231324-hwao-report.html:2,57-58`). The elapsed interval is **53 minutes**, not 43.
3. **Incomplete disclosure.** The preceding 23:12 report published three approximate individual values in addition to the sign summary.

### 5. MATERIAL/HOLD — “no discernible scientific consequence” is not established by the permitted evidence

Revision 2 accurately characterizes the 23:13 sentence as a sign summary over the confident pair and accurately notes that the sentence gives no positions, axis relation, or exact committee counts. Those facts make a demonstrated dipole/tertile consequence unlikely, and no inspected source shows that a dipole or tertile was computed.

But Revision 2's categorical statement that the disclosure “cannot bias any later analysis” (`CHI_CUSTODY_RECEIPT...:35-44`) is self-serving and not proved. It omits the three approximate individual values from the preceding report, and K-8's no-summary/no-unblinding rule is absolute precisely so materiality is not adjudicated after seeing the disclosure. The memo's softer “no discernible scientific consequence” remains **HOLD**, not a verified fact: no consequence was demonstrated, but absence of consequence cannot be established from the published surfaces and current source alone.

### 6. MATERIAL — Revision 2 introduces or repeats unsupported universal claims

The permitted source audit supports a narrower result:

- `_inference_20260820/inference_runner.py:373-442` computes and writes one chi per object and returns only processed/resumed counts;
- `_inference_20260820/chi_wrapper.py:31-72` reads only input hashes/counts and does not inspect chi values;
- `nm_report_graphics.py:354-416` counts result lines without reading their values;
- `nm_report_graphics.py:419-478` reads rows only for a single receipt card selected by `hash(seed_key) mod len(rows)`, independent of chi rank/value;
- source searches found the four named production/test files plus two synthetic rehearsal files; no matching shell/JavaScript/TypeScript/MJS source was found in the permitted trees.

That supports: **the inspected current real-data Python paths contain no chi aggregate computation.** It does not support Revision 2's universal “No code computes an aggregate. No aggregate artifact exists” (`:55-63`). The protected chi tree was not opened or listed in this pass, so its current artifact inventory remains HOLD. A filename inventory could not in any event prove that a neutral-named artifact contains no summary; the published `report-...html` files demonstrate that exact blind spot.

Revision 2's other new false/unsupported claims are:

- the three approximate values do not exist — false;
- the gate's evidence was partly fabricated — false for the published-value finding;
- the likely source was audio cue arrays — false for the literal caption/text/archive evidence;
- the report was Tori's and had no chi content — false;
- no other value, sign, count, or summary was published (`:46-53`) — false because the 23:12 report carries three approximate values and the same sign summary.

## Attack 1 — is the memo the same move a third time?

### Frozen completion/reporting duty

I found no frozen clause that compels the study to continue once started, requires entry into a decision region, prohibits abandonment, or makes investigator withdrawal itself an F-6 event.

What the frozen text does require is conditional:

- F-2 fixes reporting order if fixed-axis/secondary quantities are computed (`PREREG...V3.md:132-135`);
- F-6 defines the exhaustive set of **numeric or triggered outcomes** (`:141-145`);
- section 7 says all outcomes are published with the bounded receipt package (`:396-406`);
- K-8 permits incremental chi and defines conditions/stop paths (`K8...:26-56`).

None says an outcome must be manufactured when no decision statistic is run. Section 7 creates a duty to publish an outcome **if an outcome exists**; it is not an anti-abandonment clause. K-8's own stop condition confirms that an authorized run can stop before completion.

Ruling: declining is not, on the frozen text supplied, a preregistration event. The memo's outside-preregistration theory survives this attack.

### Material diff against the two refuted predecessors

| Issue | INCONCLUSIVE-BY-POWER predecessor | VOID predecessor | Current memo | Ruling |
|---|---|---|---|---|
| Frozen disposition claimed | F-6 `INCONCLUSIVE-BY-POWER` | newly declarable `VOID` | none; “Halted by investigator decision” | materially different |
| HC-6 treatment | substitutes footprint-aware failure for HC-6 | bypasses HC-6 by design-defect void | expressly leaves HC-6 unexecuted/unreinterpreted | materially different |
| Role of footprint calculation | purported gate result | purported basis for void | external reason for a human decision | materially different in legal/procedural function |
| Final estimator | no run | withheld on real chi | withheld on real chi | operationally unchanged |
| Acquisition | continues through chi | continues to completion | continues to completion | unchanged |
| Estimator build/freeze | continues | continues | continues | unchanged |
| Longo/sky/BHU boundaries | bounded | bounded | bounded | unchanged |
| Statistical defect | initially blamed footprint only | estimator/power protocol impeached | same corrected impeachment | unchanged from VOID draft |
| Approval wrapper | gate + Duho | gate + Duho | gate + Duho | unchanged |
| Custody treatment | lane-wide blind unverified | falsely said intact | discloses one breach but omits the three values | changed, but still factually incomplete |

The memo is therefore **not merely a relabelled F-6/VOID outcome**. Its decisive change is removal of any preregistration disposition. The same operational stopping choice remains, but preregistration does not require investigators to have identical external reasons for continuing or stopping.

### Is relying on the substituted calculation as the reason the same defect?

No. A non-frozen analysis cannot decide HC-6 or F-6, but the frozen text does not regulate every reason an investigator may have for stopping. The memo explicitly says HC-6 was not executed, identifies the footprint calculation as the external reason, and issues no F-6 result. That is not substitution inside the frozen gate.

This ruling is narrow. The footprint calculation cannot be represented as an HC-6 failure or PASS, and it does not make the factual errors elsewhere in the memo acceptable.

### HC-6 PASS and power-number audit

This attack fails:

- the memo does **not** assert the required second/realized HC-6 PASS;
- it explicitly says the second firing has not occurred;
- the freeze-time `power ~= 1.0000`, `N=130,076`, `a=0.999711`, and `A_eff=0.04077642` match `GORU_BS8_POWER_RECEIPT_20260814.md:1-25` and frozen HC-6 (`PREREG...V3.md:319-329`);
- `sim_power.py:5-9,76-92,96-106` confirms uniform-sphere generation, two-sided analytical power logic, and the `mean(cos^2)=1/3` assumption;
- the footprint numbers `Var(c)=0.057985`, `36,253`, `4.4888`, and required `4.7351` match Revision 3 and its re-gate. Independent arithmetic reproduced `36,253.2129786752`, equal-power multiplier `5.748649095532`, and one-sided requirement `4.735085933119`.

The memo's power figures are sourced rather than fabricated. Its hand-check description is the separate failure in finding 3.

## Attack 2 — defined consequence of the K-8 breach

### What was breached

- The sign summary breaches K-8 **condition 2**, not condition 1 (`K8...:32-33`).
- The three approximate values and the sign summary are also incompatible with section 4's non-authorization of unblinding and publication (`:46-50`).
- The published pages are unlisted artifacts outside frozen F-10(a)'s closed package (`PREREG...V3.md:159-162`).

### Does K-8 define a study disposition for that breach?

No explicit one.

K-8 maps consequences only for particular predicates:

- any **parameter change** after first real chi invokes F-9 and voids the run (`K8...:20-24`);
- an apparent inverted polarity triggers HOLD, and a confirmed post-chi defect requiring a sign change invokes F-9 (`:37-39`);
- gated-code changes are parameter changes (`:40-42`);
- named program refusals stop the run and go to Duho (`:43-44`).

It does not say that any breach of condition 1 or 2 automatically yields VOID, hard INCONCLUSIVE, INCONCLUSIVE-BY-POWER, an HC-7 trigger, or authorization revocation.

F-9 does not supply the missing consequence: publication/inspection of values is a breach, but the permitted record does not establish that a parameter changed. F-6 does not supply it either: no numeric outcome exists and no section 4/6 INCONCLUSIVE trigger is met. HC-7 concerns missing stratum counts, broken random-within-stratum sampling, compromised key, machine/instrument signs visible **to the checker**, and synthetic/repeat identity exposure (`PREREG...V3.md:311-318`); the published report does not establish any of those predicates.

F-10 makes the publication forbidden, and `PREREG...V3.md:472-474` says its violation class is caught by K-8 after a real-sky statistic. But F-10 expressly adds “no new kill switch,” and neither F-10 nor K-8 maps this publication breach to a study outcome independent of F-9's parameter-change predicate. Treating a violation of the boundary as though it necessarily amended the boundary would be an inference, not frozen text. Under the brief's default, that inference is HOLD.

Ruling: the breach is real and load-bearing for custody, but the supplied frozen text defines **no automatic study disposition** for it. No legitimate frozen VOID/INCONCLUSIVE outcome can be invoked from this breach alone.

## Attack 3 — Revision 2 correction audit

| Revision 2 claim | Independent ruling |
|---|---|
| `+0.27/+0.20/-0.20` do not exist | **FALSE** — literal in 23:12 report caption, authored text, and archive |
| likely audio-time-cue false positives | **FALSE** — evidence is prose, not cue arrays |
| named report is Tori's and has no chi | **FALSE** — page and archive identify Hwao and contain chi prose |
| 23:13 sign-summary quotation | **ACCURATE** |
| summary covers confident pair of two objects | **ACCURATE as written** |
| no values/positions/axis relation in the 23:13 sentence | **ACCURATE for that sentence**, but omits 23:12 numeric disclosure |
| cannot bias later analysis | **UNSUPPORTED categorical claim** |
| no current production path computes real-chi aggregate | **SUPPORTED for inspected Python paths** |
| no code/aggregate artifact exists anywhere | **UNSUPPORTED universal; artifact inventory HOLD** |
| no other value/sign/count/summary published | **FALSE** |

Revision 2 therefore introduces new unsupported claims and fails its stated purpose as a correction.

## Attack 4 — integrity sweep

### Quotations and source characterizations

- **“one leaning each way among the pair the committee was confident about” — ACCURATE.** Present in the 23:13 HTML and deck.
- **“43 minutes after K-8” — FALSE.** 22:20 to 23:13 is 53 minutes.
- **K-8 “condition 1” attribution — FALSE.** No-summary is condition 2.
- **Uniform `costheta` and `mean(cos^2)=1/3` — ACCURATE.** Present in `sim_power.py`.
- **No current/final HC-6 PASS — ACCURATE.** The memo records only the earlier BS-8 power calculation.
- **Revision 3 “twice gated” — FALSE for current bytes.** Both predecessor gates had already said so.

### Estimator/power protocol impeached; mechanics not

This paragraph holds. Frozen F-1 is `A_hat=3*D_hat`; Revision 3 shows that normalization does not transfer to the measured footprint's second moment. F-4 and F-7 use the same uniform-sphere `1/3` structure, and `sim_power.py` is two-sided while F-3 is one-sided. The assigned evidence does not impeach the classifier weights, tau, antisymmetry mechanics, committee mechanics, or hand-check harness mechanics. The memo correctly separates statistical machinery from instrument mechanics.

### BHU paragraph

This attack fails. The current brief and predecessor gate briefs establish Duho's 2026-08-21 confirmation that the lane is in the BHU programme as scope/motivation. The frozen headline separately says the Longo-amplitude test does not test BHU (`PREREG...V3.md:84-86`). The memo states both scope and non-inference and claims no outcome, so it neither erases programme scope nor promotes this lane into evidence for or against a BHU model.

### “Acquisition continues”

Absent an F-6 outcome, continued incremental acquisition does not conflict with F-6's `INCONCLUSIVE-BY-POWER -> no run` clause. K-8 expressly authorizes per-object chi to accumulate incrementally and contemplates a complete accepted population (`K8...:28-33,52-56`). The memo's “acquisition runs to completion” is therefore not internally contradictory merely because the investigator declines the final preregistered analysis.

The post-breach status is less certain. K-8 defines no automatic revocation for a condition-2/publication breach, so the text does not establish that acquisition must stop; it also does not affirmatively re-clear custody after the breach. Continuation is therefore not refuted by F-6, but clean post-breach authorization remains HOLD on the supplied text.

## Failed attacks

- **Anti-abandonment attack failed:** no frozen clause compels completion or entry into a decision region.
- **Third-label attack failed:** the memo removes the F-6/VOID disposition rather than renaming it.
- **Reason-as-substitution attack failed:** an external investigator reason is not an HC-6 input or result.
- **Power fabrication attack failed:** the memo's power and geometry numbers trace to the frozen receipt, source, Revision 3, and prior gates.
- **Current-HC-6-PASS attack failed:** no second/final PASS is claimed.
- **Automatic frozen-consequence attack failed:** the K-8 summary/publication breach has no explicit VOID/INCONCLUSIVE/HC-7 consequence absent a parameter change or named HC-7 predicate.
- **Sign-summary quotation attack failed:** the quoted words are present in both published HTML and deck.
- **Estimator/mechanics separation attack failed:** the impeachment paragraph is accurately scoped.
- **BHU-boundary attack failed:** programme scope and evidentiary non-inference are both preserved.
- **Abstract acquisition/F-6 attack failed:** no F-6 outcome means no F-6 “no run” clause is triggered.

These failed attacks establish that an accurately written decline memo could be procedurally coherent. They do not save this memo's false hand-check, gate-custody, timing, condition-attribution, and disclosure claims.

## Evidence ledger and hard boundaries

Read as content:

- `DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md` — SHA-256 `a683bc9424f26fdeabccd414aecdc0b67f08bab86307015e68294612d6a7a5bb`;
- both refuted predecessor declarations;
- both predecessor declaration gates;
- `CHI_CUSTODY_RECEIPT_20260821.md` Revision 2 — `efe21670670210c1dd1fe04821652e856903af844593695c320a4b229d322a4c`;
- `CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md` — `7617ae7f0935b634e0052267dcf4afa5a6857bad0c08850b531d357d8a3c1d6e`;
- `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md` Revision 3 — `6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7`;
- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` — `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`;
- `K8_CROSSING_AUTHORIZATION_20260820.md` — `c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`;
- `GORU_BS8_POWER_RECEIPT_20260814.md` and `../spike/sim_power.py`;
- current inference runner, wrapper, tests, synthetic rehearsal references, and `nm_report_graphics.py`;
- already-published `report-20260820T231235-hwao-report.html`, its authored text/deck, `report-20260820T231324-hwao-report.html`, its deck, `report-20260821T004950-hwao-report.html`, its deck, and `archive.html` around the relevant entries.

Mechanical checks:

- exact filename inventory of named gate inputs;
- read-only git status scoped to `prereg/` before the pass;
- SHA-256 recomputation for the memo and principal gate artifacts;
- programmatic headings/text-diff diagnostics across all three disposition drafts;
- source searches for `chi_dr10_south|chi_value` across Python and shell/JavaScript/TypeScript/MJS files in the permitted trees;
- published HTML/deck/archive searches for the approximate values, sign summary, exemplar value, and raw bits;
- independent timing arithmetic (22:20 to 23:13 = 53 minutes);
- independent normal-critical-value and footprint-equivalent arithmetic.

Boundary statement: no path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened, listed, searched, or read. No chi value was obtained from that tree and no statistic over chi was computed. Every chi disclosure cited here came from already-published HTML/text/deck/archive artifacts. `SUCCESSOR_SCOPE_20260821.md` was not opened or reviewed. No remedy is proposed. Two permitted launcher logs, `_tmp_gate_memo_stdout.log` and `_tmp_gate_memo_stderr.log`, were born at 18:58:54 KST; their contents were not read in this pass. Under `prereg/`, this gate's only substantive deliverable write is this report file.
