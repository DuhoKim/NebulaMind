All verification passes done. Supporting files are confirmed absent (mdfind, full-home ripgrep, session DB all negative), arithmetic and external primary sources checked. Writing the report.

REFEREE REPORT — RAS Techniques & Instruments
Manuscript: "A Preregistered, Blind-Validated Design for Re-Testing the Longo Spiral-Handedness Dipole — and the Human-Calibration Limit It Reveals" (PAPER_DRAFT_V2_20260901.md)
Referee posture: hostile; default REJECT; manuscript must earn otherwise.

SCOPE OF THIS REVIEW (read first)
The review bundle was incomplete. AGY_FULL_REFEREE_20260901.md, VERIFIED_NUMBERS_20260901.md and OUTLINE_AND_BRIEFS_20260901.md were not present in the working directory; I searched the host filesystem (Spotlight, full-home content search, session history) and none of the three exists on this machine. Consequently: (a) finding-by-finding verification against the previous referee's 11 findings was impossible — I verified only the four repair priorities stated in the editor's cover note; (b) no number could be checked against the verified-number table — I checked internal consistency, in-text provenance, and primary external sources instead. Items requiring the absent files are marked UNVERIFIABLE, not passed.

1. DISPOSITION OF THE PREVIOUS REFEREE'S FINDINGS (as verifiable)

F1. LANDED. Abstract and Section 2 now describe the analysed sample: 49,211 objects, Var(cos theta) = 0.7517, N_eq = 110,983, with the abstract explicitly stating "these are the figures for the sample actually analysed, not its pre-cut precursor."

F2. LANDED. The pre-cut figures (53,005 objects, 0.754664, N_eq = 120,002.9) appear only in Section 2, labelled "frozen planning selection before the later quality cut," with the explicit sentence "only the latter pair describes this paper's analysed mask." Section 4.1 repeats the reconciliation. No pre-cut figure is presented as analysed geometry anywhere I found.

F3. LANDED. The false "every stage passed" claim is gone. In its place: abstract ("its failures were caught and recorded, and the pre-image validations completed under their stated scopes passed"), Section 4.1 (blocked planner, FAIL closure), Section 4.4 (two voided go-live attempts, and the explicit injunction that "neither should be erased by saying that every stage passed"). The replacement is accurate and appropriately bounded.

F4. PARTIALLY VERIFIABLE. All four flagged figures now carry in-text provenance: 850 -> CODEX_LOW_HUMAN_OPTIONS_20260901.md; 51 (within 5,049 = 99 x 51) -> gates/CALIBRATION_ROBUSTNESS_REHEARSAL_RECEIPT_20260831.md; 8.67 million -> CODEX_EXTERNAL_LABELS_20260901.md; 120 -> CODEX_LOOSENING_COST_20260901.md. Whether they appear in the verified-number table is UNVERIFIABLE (table absent).

F5. PROCESS FINDING. A full finding-by-finding audit of all 11 previous findings could not be performed because the previous report was not supplied. The editor should not treat this review as certifying repairs beyond F1–F4.

2. OVERCLAIM

F6. PASS. I scanned abstract, introduction and conclusions as a composite, plus every result-bearing sentence, for anything quotable as a detection or physics claim. None found. Every booby-trap token is defused in situ: "REPRODUCED-LONGO" is immediately followed by "That stored label names a convention test; it is not an observational reproduction"; the 5,049-cell counterfactual carries "it was not the frozen invariance outcome and discharged no frozen edge"; the power results carry "They are not evidence about galaxy handedness"; the Longo figures carry "not results reproduced or endorsed here." Abstract, introduction and conclusions each independently restate that no label was read and no physics is reported. The composite does not exceed the parts.

F7. MAJOR (fixable). The one remaining overclaim is framing, not sentence-level: the paper elevates "the human-calibration limit" to a co-headline result (title, abstract, conclusions). But this "limit" is an arithmetic consequence of the paper's own frozen design constants (nine strata, 30-per-stratum floor, 50-decision cap), sourced entirely to internal memos. No checker was recruited, no pilot labelling run was executed, and the claim that "no available checker could complete the role" is asserted, not evidenced. As the paper itself concedes (the 120-decision breakpoint), a different estimand evades the limit entirely. The quantity demonstrated is a design requirement, not an empirical property of human calibration capacity. The paper's second "result" is therefore overclaimed in kind. Fix: reframe as a design-requirement/costing analysis, or document an actual procurement attempt.

3. NUMBERS

F8. MINOR (fixable). "The count-weighted full brick universe gave 0.445201" (Section 2) has no provenance — no receipt, no preregistration line, no citation. Every other figure I spot-checked carries an in-text source. Add provenance or delete.

F9. MINOR (fixable). 1,860 decisions is not derived in the text. The arithmetic works — (270 real + 200 synthetic + 150 mirrored) x 3 votes = 1,860, and ceil(1,860/50) = 38 checkers — but the reader cannot reproduce it from stated quantities; it rests on an internal memo. One line of derivation fixes this.

F10. PASS. Internal arithmetic verified: 99 x 51 = 5,049; 9 x max(30, 3x10) = 270; 500+200+150 = 850; 177+192+334 = 703; 984 and 996 both exceed the 962 floor; the manifest SHA-256 is a well-formed 64-hex string; Var(cos theta) = 1/3 is the correct isotropic value. External spot-checks: Longo's -0.0408 +/- 0.011 and 7.9 x 10^-4 match the primary abstract (arXiv:1104.2815) exactly; the Galaxy Zoo DESI characterisation ("model-predicted morphology vote fractions") matches Walmsley et al. 2023 ("8.7M galaxies... predicted vote fractions"). The precise "8.67 million" figure is plausible against that source but must appear in the verified-number table — UNVERIFIABLE here. Note also the sample hierarchy is internally coherent: 65,060 parent -> 53,005 planning -> 49,211 analysed.

4. RASTI CONFORMANCE

F11. MAJOR (fixable; converts to REJECT if unresolved). Data Availability contains the unresolved placeholder "A public repository identifier should be inserted before submission." For this manuscript that is not a clerical gap — it is the central defect. Every substantive claim is receipt-backed, and not one receipt, manifest, checkpoint or memo is inspectable by the reader. A preregistration-and-provenance paper whose provenance is a set of private file paths is unfalsifiable in every particular. Deposit the archived package (Zenodo or equivalent) with a cited DOI. Absent that, my recommendation converts to REJECT without further review.

F12. FIXABLE (must fix). The manuscript ends with an author-side certification block: "SEAT: CODEX / VERSION: PAPER-V2 / VERDICT: REPAIRED / COUNT: 11." The authors' own agent declaring the referee's findings repaired, inside the submission, is self-certification and has no place in the manuscript. Remove it. Its presence also indicates the draft was never cleaned for submission.

F13. TRIVIAL. The AI disclosure refers to "Section [6]" — an unresolved cross-reference marker. Should read "Section 6."

F14. PASS. Abstract: 216 words, single paragraph (limit 250). Keywords: 5 (required 3–6). Conclusions is the last numbered section (Section 8). Acknowledgements, Data availability, Conflict of interest, References are unnumbered and follow it. AI disclosure is present within Methods (Section 4), is unusually candid, and correctly states no AI system is an author. References are in acceptable MNRAS-style format; the three cited works check out bibliographically.

5. RESEARCH OR PROJECT REPORT

F15. FIXABLE. Scholarship: the factual claims about external catalogues — GZ1 containing direction votes, GZ DESI's 8.67M predicted-fraction rows, "modern Galaxy Zoo products encode winding tightness rather than winding direction" — rest on the internal memo CODEX_EXTERNAL_LABELS_20260901.md and cite none of the underlying catalogue papers (Walmsley et al. 2023 is absent from a reference list that totals three entries). The "reviewed here" scoping is honest but points at an invisible review. Add citations for the catalogues actually assessed, and minimal methodology citations (permutation/exact-power testing, preregistration practice).

F16. CONDITIONAL PASS. On the real bar: the repaired draft argues and evidences a thesis rather than chronicling activity. The declined 208,407-object predecessor is deployed as negative evidence for the design thesis; the bounded validation results are presented with their scopes as part of the result; the halt is quantified. That is argument, not diary. Residue remains: the Section 3 audit inventory (703/84/177/192/334) is bookkeeping that evidences process hygiene more than any claim, and the entire evidentiary base is internal documents. It crosses the research bar, narrowly, and only stays across it if F11 and F15 are resolved — an uninspectable internal record is a project report's evidence, not a paper's.

6. WHAT I WOULD REJECT ON

Fatal as submitted, if uncured in revision:
- F11 (unverifiable evidentiary core; no public archive). This alone justifies rejection of a provenance-centred paper if not cured.
- F7 (headline "limit" is design arithmetic + unevidenced procurement claim). If the authors insist on the current framing, I reject on overclaim of the second result.
Fixable by revision: F4-table-confirmation, F8, F9, F12, F13, F15.
Not reject-worthy: F1–F3, F6, F10, F14 (landed/passed).

7. REQUIRED BEFORE RECONSIDERATION
1. Deposit the frozen package and all cited receipts/memos; cite the DOI in Data Availability (F11).
2. Reframe the calibration result as a design requirement, or evidence the procurement claim (F7).
3. Delete the self-verdict block (F12).
4. Add catalogue and methodology citations; specify which GZ products were reviewed (F15).
5. Source or cut 0.445201 (F8); show the 1,860 derivation (F9); fix "Section [6]" (F13).
6. Supply the verified-number table and the previous referee report to the reviewer so F4 and F5 can be closed.

8. QUESTIONS TO AUTHORS
Q1. What is the relationship between the 984-success "eligible prefix" battery and the 996-success "final re-pass"? Same trials re-run? Was the re-pass itself frozen before execution, and what defined "eligible" checkpoint batteries? Any post-hoc selection here would reopen the exact-power claim.
Q2. Was any checker recruitment or pilot labelling actually attempted? If yes, document it; if no, justify "could not be supplied."
Q3. Provide the archive DOI.

SUMMARY
The named repairs landed: the analysed 49,211 / 0.7517 / 110,983 figures now anchor abstract and leverage section, pre-cut figures are labelled, the "every stage passed" falsehood is replaced with an accurate bounded statement, and the four orphaned numbers carry sources. Overclaim control at sentence level is genuinely good — I could not extract a quotable detection claim. Structure conforms to RASTI. What prevents acceptance is not the repair job but the paper's foundations as submitted: nothing it asserts is inspectable (F11), and its second headline result claims more than its evidence kind supports (F7). Both are curable in one revision. Under a hostile mandate this manuscript has earned exactly one step above rejection, contingent on the conditions above; failure on F11 converts this to REJECT.

SEAT: KIMI
VERSION: FULL-REFEREE-V2
VERDICT: MAJOR-REVISION
COUNT: 16
