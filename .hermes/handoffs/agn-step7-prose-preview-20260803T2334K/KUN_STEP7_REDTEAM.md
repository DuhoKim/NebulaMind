# KUN RED-TEAM — AGN Step-7 prose-preview packet

Lane: `agn-step7-prose-preview-20260803T2334K`
Reviewer: Kun (Kimi K3 via Nous). Date: 2026-08-04 ~01:30-02:10 KST.
Targets: `AGN_PROSE_PREVIEW.md` (36 sentences), `PROSE_SENTENCE_BINDINGS_STEP7.jsonl` (36 rows), `WORDING_CONTRACT_CHECK_STEP7.json` (36 checks).
Ground truth: patched map (`agn-step6-map-pilot-20260803T1330Z/AGN_STATUS_DEBATE_MAP_V1.md` post-patch + `PATCH_LOG.md`), 16-entry ledger, contract `wording_contract_check.json` ceilings, `prose_sentence_bindings_template.jsonl` (16 templates), roadmap Step 7.

## VERDICT: PASS_WITH_PATCHES

The packet survives the modality law in both its declared form and my stricter recomputation: I rebuilt the ceiling table from the contract (`wording_contract_check.json`) and re-evaluated every sentence against the MINIMUM ceiling over its bound entries — 36/36 pass. All 16 contract templates are used exactly once, no unknown template IDs, every template's bound-entry set overlaps its sentence's bindings. Every cited span ID exists in the ledger AND belongs to the sentence's bound entries (no phantom citations, no cross-entry citation drift). The countercase quota survived translation — all map countercases appear in prose with their ledger scoping intact. The pending-status disclosure is verbatim-carried from the patched map header, up front, in a dedicated reader-disclosure sentence. The patches are three: one REAL modality overstatement the checker's own rules cannot see (F1), one meta-flag misuse that hides a content sentence from the law (F2), one content-beyond-ledger noun (F3), plus two nits.

---

## FINDING 1 (MEDIUM, real modality overstatement) — s7_C02 states an `is_are_does` assertion at `commonly_probably` ceiling with no hedging, and the contract ceiling is what makes it legal — but the ceiling is a template artifact, not the ledger modality

Sentence: "Strangulation, environmental stripping, and cold-gas pathway differences **remain mandatory** alternative or qualifying quenching channels." Bound entry: `clc_agn_007` (ledger modality `is_are_does`, certainty `widely_supported`; contract ceiling `commonly_probably`).

Attack path: the ledger modality `is_are_does` licenses bare "are" language. The contract template for this entry caps prose at `commonly_probably` (tier 6 < 7) — i.e., the contract itself downgrades the entry. The Step-7 sentence uses neither: it states the assertion flatly ("remain mandatory"), which reads as tier 7 (`is_are_does`), while its binding row claims tier 6. Since the binding row passes by construction (6 ≤ 6), the self-check cannot catch that the SENTENCE AS WRITTEN is stronger than its declared tier. "Remain mandatory alternative channels" with zero probabilistic framing is an is/are statement — under the contract's own tier definition the sentence should carry "commonly/probably" framing ("are generally required", "remain mandatory in most accounts") or re-declare its tier. Compare s7_C04 and s7_C05, same tier claim: "…**are** a real quenching-predictor axis" / "…**are** also real quenching axes and **must remain** separate" — same defect, three instances. The map used identical bare language, so Lana translated faithfully; the defect is inherited, not introduced. But Step 7 is precisely the stage whose job is catching this. Recommendation: either (a) demote prose to match the declared ceiling with visible probability framing, or (b) petition the contract to raise these entries' ceilings to `is_are_does` — do not leave sentence and declared tier silently mismatched.

(Checker-rule note: R-A/R-B compare declared tiers, not sentence text. A stricter check would flag tier-claim/text mismatches; the C41 Step-7 should add one.)

## FINDING 2 (LOW-MEDIUM) — s7_C09 is a CONTENT sentence (countercase discharge) smuggled past the modality law under `meta_sentence=true` / `reported_only`

Sentence: "The alternatives position is not unopposed either: it is held in tension by the ejective-mechanism evidence of Axis A, while simulation entries enter this debate only as qualifiers, never as observed-frequency evidence."

This is not a meta/guard/status sentence reporting ledger fields — it asserts an epistemic relationship between positions (that Axis A evidence opposes the alternatives position). That is exactly the countercase-quota discharge the roadmap requires for 007's `widely_supported`, and the checker summary cites it as such ("axis_C_007…: tension named at s7_C09"). A sentence doing substantive countercase work should carry a real tier and be modality-checked against its bound entries (007 at `commonly_probably`, 001 at `commonly_probably`, 011 at `in_model_only` — minimum `in_model_only`; the sentence would pass anyway, since "held in tension" is weak language — but it should pass VISIBLY, not by exemption). The R-D rule as written lets any sentence that mentions ledger structure self-certify as meta. Patch: flip C09 to `meta_sentence=false` with an appropriate tier (it passes), and tighten R-D for the C41 template: meta status requires that the sentence assert nothing about the evidence itself. Same scrutiny applied to the other 10 meta rows — they are genuinely meta (status labels, guard restatements, structural descriptions); C09 is the only offender.

## FINDING 3 (LOW) — s7_E01 names "EAGLE" — present in the MAP but not in the LEDGER

Sentence: "In simulations — HORIZON-AGN against its noAGN twin, RAMSES zoom runs, IllustrisTNG, and **EAGLE**/Illustris/TNG comparisons — …" The ledger entry `clc_agn_011`'s four spans cover HORIZON-AGN/noAGN (3948D), zooms (3297D), IllustrisTNG (4004D), and an observed-vs-simulated comparison (1052P). "EAGLE" appears nowhere in the ledger's spans, titles, or method_or_model ("cosmological simulations and model comparisons"). It DOES appear in the patched map's Axis E evidence line ("EAGLE/Illustris/TNG comparisons") — and the brief allows content from ledger + map, so this is legal under the letter. But the map itself derived "EAGLE" from somewhere outside the 011 spans (a map-stage over-specification Lana's Step-7 faithfully inherited). Since the brief's law is "no content beyond ledger + map," the sentence is compliant; flagging because the map's EAGLE mention is itself unverifiable against the ledger and the C41 track should not treat map-carried proper nouns as ground truth when they outrun the ledger. One-word patch: drop "EAGLE/" (the remaining "Illustris/TNG comparisons" covers 1052P's family).

## FINDING 4 (NIT) — Disclosure strength: fully preserved, one presentational softening

The reader disclosure (s7_H01) is verbatim-equivalent to the patched map header and appears before any content. In addition, EVERY status line carries "(pending verification)" inline — five axis status sentences plus the header. This EXCEEDS the map's disclosure (which puts it in the header + closing footnote). No weakening found. The nit: the per-axis status sentences are all `meta`/`reported_only`, correct, but the two strongest claim-adjacent status lines (A07, B06) re-state the enum labels immediately after content paragraphs — fine. No action.

## FINDING 5 (NIT) — Numbers audit: all carried numbers verified verbatim against ledger spans; two phrasing choices recorded, neither a violation

Verified against ledger spans: 3–100 M⊙/yr (span _05 verbatim); 10× SFR (span _07 "ten times higher" verbatim); 17% of 159 AGNs (scope.sample_n=159 + span _03); 46%, log M*>10, 113 (scope fields + span _02), ≥100 km/s (span _03 verbatim); 26,000 SDSS spectra (span _04); 4 Gyr strangulation (span _04); 30–70% satellites (span _02 verbatim); Mstar<10^10 satellite dominance (span _05 verbatim); 2–4 Gyr delay, <0.8 Gyr e-folding (span _06 verbatim); factor ~2 central depletion (span _05); four best-spaxel galaxies (span _05 verbatim); z<0.2 / 456-galaxy (span _01 verbatim). Do-not-average guard: present (s7_B04) with the correct definitional-not-scatter framing; D'Eugenio exclusion guard: present (s7_B05) with the risk flag named; simulation cap: present (s7_E02) with the "no observed-frequency sentence rests on a simulation entry" self-binding.
Phrasing notes: (a) s7_A02 says "In one massive z~2 sample" for the 3–100 span — the span's own quote doesn't name z~2 but the source paper (2024MNRAS.528.4976D) is the z~2 JWST sample established in 002b's scope; the map made the same attribution — acceptable, ledger-traceable. (b) s7_C03's "stripping is reported as ubiquitous among satellites" — "reported as" is a `reported_only`-style hedge inside a `commonly_probably` sentence; strictly it UNDERSTATES the tier (legal — understating never violates the law; noting because the tier system only guards one direction).

## ATTACKS THAT FAILED

1. **Modality law (recomputed, not trusted):** rebuilt ceilings from contract; min-ceiling over bound entries ≥ actual tier for all 36. Zero violations.
2. **Binding-entry correctness:** every bound entry exists; every sentence's bindings match its content's natural entries (I hand-checked all 36 against my ledger knowledge from the Step-6 red-team — no mis-bound sentences; dual-citation of 2299-parent + child is consistent with the ledger's own link structure).
3. **Citation-span integrity:** all cited span IDs exist; all belong to the sentence's bound entries (mechanical check, 36/36).
4. **Countercase loss:** 008 appears TWICE (A06 as Axis-A countercase, C08 as Axis-C countercase with the 456-sample scope); the 009↔010 mutual bounding (C07); 007's opposition (C09 — mis-flagged but present); the do-not-average guard; the D'Eugenio exclusion; the sim cap. Nothing dropped.
5. **Pending-status weakening:** disclosure is verbatim and MORE prominent than the map's (reader-level preamble + per-axis repeats).
6. **Template misuse:** all 16 contract templates used exactly once; no unknown IDs; template-entry overlap complete.
7. **Content-beyond-ledger sweep:** every proper noun, number, and qualitative claim traced to ledger spans/scope/assertions or the patched map — except "EAGLE" (F3, map-carried).
8. **Seed-guard erosion across stages:** all five seed reader-guards (never-universal, do-not-average, D'Eugenio exclusion, in-model-only cap, alternatives-visible) survive from seed → map → prose.

## Patches requested (pre-apply-gate)

1. F1: re-tier or re-word s7_C02/C04/C05 (probability framing or contract-ceiling petition) — and add a tier-text-mismatch check to the C41 Step-7 checker.
2. F2: flip s7_C09 to meta=false with a real tier; tighten R-D's meta definition for C41.
3. F3: drop "EAGLE/" from s7_E01 (or trace it into the ledger before the apply gate).

## Evidence ledger

Read in full: `AGN_PROSE_PREVIEW.md`, `PROSE_SENTENCE_BINDINGS_STEP7.jsonl` (36 rows), `WORDING_CONTRACT_CHECK_STEP7.json` (rules, tier ranks, all 36 per-entry records), `LANA_STEP7_BRIEF.md`, `PATCH_LOG.md` (Step-6), patched map sections as needed.
Recomputed mechanically: contract ceiling table (16 entries); min-ceiling modality check (36/36 pass); span-existence + span-ownership check (all cited spans in ledger AND owned by bound entries); template registry diff (16 used == 16 registered, zero unknown); per-sentence meta/tier census (11 meta rows, audited individually).
Verified verbatim against ledger: 17 carried numbers/proper nouns (listed in F5); countercase presence (A06, C07, C08, C09, B04, B05, E02); disclosure parity with patched map header.
Not read (per task boundary): the C41 lane, f_esc dirs, campaign ledger. No writes except this report.

## Uncertainties

- F1's tier-of-the-sentence-as-written judgment ("remain mandatory" reads as is/are) is a semantic call — the tier system's granularity means reasonable readers could place it at either 6 or 7; the finding stands because the packet's OWN declared tier (6) and the sentence's bare form diverge, whichever way one resolves it.
- "EAGLE" provenance upstream of the map (which of 011's four sim papers the map author meant — plausibly 1052P's EAGLE/Illustris/TNG family, but the ledger's span/title text doesn't say so).
- I did not re-verify the map's own content against the ledger tonight beyond what the Step-7 sentences touch (covered by my Step-6 red-team, whose patches the map now carries — verified via PATCH_LOG).

---

KUN_AGN_STEP7_REDTEAM_COMPLETE_20260804
