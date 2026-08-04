# KUN RED-TEAM — C41 Step-6 status/debate map v1 (the flagship)

Lane: `c41-baseline-restart-20260803T1253Z`
Reviewer: Kun (Kimi K3 via Nous). Date: 2026-08-04 ~15:50-16:40 KST.
Targets: `C41_STATUS_DEBATE_MAP_V1.md`, `C41_CONDENSATION_REPORT.md`.
Ground truth: stance-verified `C41_LEDGER.jsonl` (sha e2938298… — verified matches the map's pin), `C41_STANCE_MATRIX.jsonl` + `VERIFICATION_STATUS_PATCH.jsonl` (my Step-5 artifacts), `STEP0_FROZEN_QUESTION.md` (sha 9ac5ca1f…), my own `KUN_STEP5_REPORT.md`.
Attack protocol: the AGN-pilot attack set + patch-5 mechanical re-execution standard, as briefed.

## VERDICT: PASS_WITH_PATCHES

The flagship survives the same battery the AGN pilot faced, and in one respect exceeds it: the condensation report is the first artifact in the chain whose determinism claims are scoped *accurately* — the deterministic layer (R0–R4) re-executes mechanically from the ledger alone, and the judgment layer (J1–J7) says plainly it is judgment, with every row carrying a patch-5 machine-check (a verbatim assertion substring). I re-executed all 81 trace rows: **zero failures**. K=7 independently re-derived (5 axes forced by R3 markers + 2 forced by the frozen question's own sub-questions; the declared ±1 judgment band is honest). Every one of the 76 claim entries is named in the map body; zero phantoms; the sole dual membership (c41_065) has both content bases verified verbatim in its ledger assertion. The map's honesty sections (A6's "no direct escape measurement exists in this corpus," A5's one-sidedness-is-not-consensus, A7's absent-pro-AGN-side-is-scope-not-finding) are the strongest in the whole Baseline chain so far. The patches: one missing Status line (A5), one rule-7 boundary tension (A7's question title), one ledger-defect aftermath item, one nit.

---

## MECHANICAL RE-EXECUTION (patch-5 standard) — all pass

- **Trace table (81 rows parsed from the report, re-executed against the ledger):** every R0 row asserts `certainty_level == "no_info"` correctly (exactly {018, 021, 059, 062} — the same 4 my Step-5 patch marks verified_no_claim); every J-row's `assertion contains "…"` fragment is a verbatim substring of that entry's ledger assertion. **81/81 re-execute. Zero failures.** This is the AGN-pilot Finding-1 class (silently swallowed/mis-cited entries) — structurally impossible here because every placement carries a re-checkable citation, and I checked them all.
- **R1 (super-axis tags):** all 76 claim entries carry ≥1 frozen tag. Re-verified.
- **R2 (link degeneracy, their negative result):** re-derived independently — 149/149 links are `same_axis` with the identical description string; the undirected graph has exactly 2 components (one 74-entry, one {065, 066}) plus 4 isolates {014, 041, 070, 079}. Their count said "6 components" — counting isolates as components, 74+2+4×1 = 6. Consistent. Their conclusion is correct and important: this ledger's link vocabulary cannot carry condensation (contrast the AGN pilot's typed links), so the J-layer's existence is justified, not lazy. Their flag to the contract lane (Step-4 should emit typed links) is the right repair.
- **R3 (debate markers):** re-derived — exactly {004, 005, 011, 037, 042, 076} via the stated predicate. All six placed as holders/sides in named axes. The constraint holds.
- **R4 (dual cap):** one dual (c41_065, A1+A6). Both declared bases are verbatim substrings of the ledger assertion ("non-accelerated decline of the UV luminosity density beyond z ~ 8" for A1; "very steep faint-end slope (alpha ~ -2)" for A6). **No dual-membership abuse.**
- **Coverage table byte-copy:** all 80 rows' certainty_level and modality match the ledger exactly (80/80). Axis assignments in the table match the trace for all but the expected dual (c41_065 = "A1+A6" in table, two rows in trace — consistent, not a mismatch).
- **K re-derivation:** R3 forces ≥5 axes (004+076→A1, 011→A2, 037→A3, 042→A4, 005→A7); the frozen question's three sub-questions force representation of enrichment history (A5) and ionizing budget (A6). K=7 is the minimum satisfying both constraints. Their merge/split tests are individually sound: A3-vs-A4 (tools vs relations) survives 042's within-one-method disagreement; A1-vs-A2 (census vs its interpretation) survives 011/064 presupposing the census. The declared ±1 band (fold A7 into A6; promote A3 drivers) is honest — I could construct both moves, and both are judgment, exactly as scoped.

## MODALITY AUDIT — no overflow found

I ran the strong-language scan over the map body: unhedged "is/are/confirms/rules out" language appears only where the bound entry carries `is_are_does` (or the map is restating an entry's own modality). Every `may_or_can` entry's content is introduced with may/seem/might/suggest phrasing (spot-verified: 046 "may reflect", 067 "may be overestimated", 072 "possibly", 058 "may arise", 031 "could remove"); `reported_only` entries carry "is reported to" framing (078, 047, 020, 039, 069, 073 — all six checked); the one `commonly_probably` entry (079) keeps the source's own conditional ("sufficient **given high escape fractions**"); the one `in_model_only` entry (080) is never allowed observed-frequency language ("currently in-model only" stated at its use site). The frozen-question's final-clause section adds its own modality note (items 3–5 case-grade; only 1–2 on is/mixed entries) — self-aware and accurate. c41_076's "candidates, not confirmations" is exactly the discipline the autopilot era lacked.

## COUNTERCASE AUDIT — none lost; one absence declared correctly

- A1: two-sided in-corpus (slow 004/074/076/078 vs rapid 047/056/063) with census qualifiers (046/067) as the doubt-answer. ✓
- A2: asymmetric two-sided, with the holder (011) naming its own breaking redshift — the strongest kind of countercase (self-limiting). ✓
- A3: 043-vs-{033,035,044,045,049} named as the map's cleanest "disputed" under the interpretation contract (stance-verified sources in conflict — cross-paper, which per the contract is where "disputed" must live). ✓
- A4: 042 split across its own sSFR window (the stance matrix's only `mixed` row, used honestly). ✓
- A5: one-sided declared with the correct epistemology ("a property of this working corpus, not evidence of consensus"). ✓
- A6: the "bright few dominate" counterparty is absent from the corpus and **declared as a gap, not adjudicated** — precisely right; inventing that side would have been the unpardonable sin. ✓
- A7: no in-corpus pro-AGN entry; declared as a Step-1-filter scope fact. ✓

## A7 BOUNDARY RULE vs THE FROZEN QUESTION — FINDING F1 (patch required)

The frozen question's boundary clause: LRD/high-z AGN are "IN only insofar as they bear on the three axes …; their intrinsic nature (AGN vs stellar) is **NOT a fourth axis**."

The map's A7 obeys the entry-selection half of this perfectly: the three entries (005/010/050) enter as budget-attribution bearers (verified: each carries frozen tags — 005 CE+IO, 010 FE+CE, 050 FE+IO), the section restates the rule, and no sentence adjudicates AGN nature as an end in itself (my scan for nature-adjudicating language comes up clean — the only "AGN are" hit is the rule restatement itself).

The tension is the AXIS ITSELF: A7 is titled "**AGN boundary: stellar or AGN power in the tested objects?**" — that IS the AGN-vs-stellar nature question, elevated to one of K=7 named axes, when the frozen question says nature is not a fourth axis. The frozen question's phrasing is about not letting AGN-nature become a research axis; the map's defense is that A7 is an attribution-check on the budgets, not nature-for-nature's-sake — and its content is genuinely that. But as named and counted, A7 walks up to the line. The R3 marker (005's debate_countercase tag) forces placement *somewhere*; the trace could equally have placed 005/010/050 inside A6 as the budget-attribution side (the condensation report itself lists folding A7 into A6 as the canonical ±1 move). Recommendation (patch, not reject): retitle A7 to make the bearing primary — e.g. "Budget attribution: is the ionizing/excitation power in the tested objects stellar?" — and state in one line that this is the A7↔A6 boundary the ±1 judgment band refers to. As written, a hostile reader of the frozen question can claim the map smuggled the forbidden fourth axis back in under a boundary label.

## SETTLE-LINE AUDIT — all seven pass; one is exemplary

Every axis's "What would settle it" names a measurement or method that exists (in-corpus or as a named extension), a deficiency, and the gap: A1 (spectroscopic confirmation of z≳15 candidates — method in-corpus via 074); A2 (joint UVLF+clustering+burst dataset — components in-corpus); A3 (grow the ~25-galaxy auroral anchor — deficiency defined by 012, feasibility shown by 026/013/061); A4 (the 040 single-methodology design extended past z=3 — design in-corpus); A5 (larger N-emitter pattern sets + pre-460-Myr metallicity); A7 (the 050 method applied systematically). **A6's is the best in the chain:** it states the settling measurement does NOT exist in this corpus (no direct f_esc at z≳6), itemizes why every in-corpus escape statement is inferred/conditional, and explicitly refuses to assert the measurement exists elsewhere. That is the anti-vague, anti-unfalsifiable standard the other lanes should copy.

## FINDINGS

- **F1 (LOW-MEDIUM, above):** A7's title/elevation vs the frozen question's "NOT a fourth axis." Patch: retitle + one-line boundary note. The entries, placements, and rule restatement are all compliant; the label is the problem.
- **F2 (LOW):** A5 has **no `**Status:**` line** — six of seven axes carry one; A5's status appears only inside its "Countercase honesty" paragraph ("the axis status stays `emerging_sample_limited`"). The summary table at top covers it, but per-axis completeness (and the AGN-pilot template) wants the line. One-line patch.
- **F3 (LOW, aftermath — not this lane's defect):** the map correctly discloses the v8 applier's `verification_status: "validated"` overwrite (off-enum, collapses my 76+4 census) and binds its verification claims to my two pinned artifacts instead. I verified: on-disk field is now `"validated"` ×80; ledger sha matches the map's pin; c41_004/005 on-disk zone=unknown + stance=qualifies (v8's conservative reconciliation) while my matrix carries supports — the map takes the more conservative reading everywhere, which is the right call. The remaining action is the applier's: re-land my patch per-row. The map's handling is exemplary; the ledger is still wrong on disk.
- **F4 (NIT):** R2's "6 components" phrasing counts the 4 isolates as components; my re-derivation gives 2 nontrivial components + 4 isolates. Same graph, consistent arithmetic, mildly confusing phrasing. No patch needed beyond noting.

## ATTACKS THAT FAILED (for the record)

Phantom bindings (none — every ID in the body exists); missing entries (none — all 76 claims named in body, 80/80 in coverage); modality overflow (none — tier-by-tier language scan clean); countercase loss (none — and the absent sides are declared, not papered); dual-membership abuse (c41_065's bases both verbatim-verified); K inflation/deflation (re-derived K=7 as the constraint minimum); trace non-reproducibility (81/81 re-executed); settle-line vagueness (all seven concrete; A6 exemplary); frozen-question drift on entry selection (A7 entries all bear frozen tags and enter as attribution); stance-verification laundering (map binds to my pinned artifacts, takes the conservative on-disk reading for 004/005, and discloses the v8 defect with byte-diff evidence — I re-verified the sha and the field state independently).

## Patches requested (pre-Step-7)

1. F1: retitle A7 (bearing-primary) + one-line boundary note.
2. F2: add A5's Status line.
3. F3 (applier lane, not Lana): re-land `VERIFICATION_STATUS_PATCH.jsonl` per-row; keep the conservative 004/005 zone/stance reconciliation (or receipt the override).

## Evidence ledger

- Re-executed: all 81 trace rows against `C41_LEDGER.jsonl` (substring/enum checks); R1 tag census; R2 graph components (independent rebuild: 74 + {065,066} + isolates {014,041,070,079}); R3 marker predicate (exactly 6); R4 dual bases (verbatim substrings of c41_065 assertion); coverage-table byte-copy (80/80 enums); trace-vs-map axis agreement (1 expected dual only).
- Verified: ledger sha == map pin (e2938298…); on-disk verification_status = "validated" ×80 (v8 defect real, map's disclosure accurate); c41_004/005 on-disk zone=unknown/stance=qualifies vs matrix supports (map takes conservative — correct).
- Scans: modality-language sweep across the map body (per-tier); countercase presence per axis (7/7 sections present); settle-line falsifiability read (7/7); phantom/missing ID scan (clean); A7 nature-adjudication language scan (clean); frozen-question boundary text re-read.
- Read in full: both artifacts; my Step-5 report's findings cross-checked against map usage (all 8 binding-note nits correctly carried and flagged for span re-cut; the 4 zeros correctly placeholder-excluded; the ESL monoculture correctly interpreted as structure, not weakness).

## Uncertainties

- The J-layer placements are judgment, as declared; I accepted each after reading the per-axis arguments, and my ±1 alternatives coincide with the report's own (A7↔A6 fold is the live one, hence F1).
- I did not re-verify the map's *[engine context …]* blocks against dispersion_v2.json (they are bracketed, labeled non-claims, and excluded from binding by design); the two I spot-checked (f_esc N=64 S=3.9; metallicity N=304 S=9.5) match values I saw in that file during Step-5-adjacent work.

---

KUN_C41_STEP6_REDTEAM_COMPLETE_20260804
