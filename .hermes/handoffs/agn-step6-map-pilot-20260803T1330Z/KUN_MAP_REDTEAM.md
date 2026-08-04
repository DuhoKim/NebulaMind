# KUN RED-TEAM — AGN Step-6 pilot (status/debate map v1 + condensation report)

Target lane: `.hermes/handoffs/agn-step6-map-pilot-20260803T1330Z/` (Lana)
Artifacts attacked: `AGN_STATUS_DEBATE_MAP_V1.md`, `CONDENSATION_REPORT.md`
Ground truth: `docs/claim_ledger_contract_v1_agn_20260703T0830Z/artifacts/` — ledger (16 entries, read in full), stance matrix (45 rows, read in full), enums, seed, wording-contract check; roadmap § Step 6 (lines 400–428).
Reviewer: Kun on Hermes via Nous `moonshotai/kimi-k3`. Date: 2026-08-04 ~02:40-03:20 KST. FINDINGS ONLY.

**Overall verdict: PASS_WITH_PATCHES.** I independently re-executed the condensation rules against the ledger link graph, cross-checked every entry binding, every status enum, every modality ceiling, every cited span/paper/number I could check, and re-derived K. The map is honest, the bindings are real, the seed departures are justified, and I could not construct a missed axis. What follows are the defects I DID find — three structural (R5's citation is wrong for 009/010 and one entry silently unaccounted; the "no semantic judgment" claim overshoots; verification_status hygiene), then smaller items, then the attacks that FAILED (so the crew knows what was tried).

---

## FINDING 1 (MEDIUM) — R5's own placement citation is wrong for 009 and 010, and R5 silently swallows one entry it never names

The condensation report states R5 = "A remaining entry linked to an axis seed only by `qualifies`, `contradicts`, or `same_axis` joins that axis as a named side/countercase," and the trace table records:
- `clc_agn_007` → C via "same_axis → C seed" — VERIFIED correct (007 same_axis→2299_003).
- `clc_agn_009` → C via "same_axis/qualifies → C seed" — **wrong as stated**: 009's links are same_axis→**010** (not the seed) and qualifies→2299_003. The same_axis leg of the citation does not exist; the placement actually rests on the `qualifies` leg alone.
- `clc_agn_010` → C — same defect mirrored (same_axis→009, qualifies→2299_003).

This is not cosmetic: R5's wording claims each placed entry is "linked to an axis SEED," and the trace cites the wrong link type. Worse, under the stated rule, **clc_agn_005 also satisfies R5** (it is linked to C-seed 2299_003 by `qualifies`) — so R4's precedence over R5 is load-bearing for Axis D's existence, and the precedence chain "R1 > R3 > R2 > R4 > R5" is what saves the partition. But then notice what R4 leaves behind: **clc_agn_008 is the only entry whose placement citation includes evidence from OUTSIDE the ledger's link graph** — its stance-matrix `contradicts` row is cited in the trace (the ledger itself carries contradicts→clc_agn_001 in 008's links, so the placement is still defensible via the ledger alone: qualifies→2299_003 — but the trace as written leans on the stance matrix, contradicting the report's header claim "Condensation uses ONLY the ledger's own structure").

Bottom line: the PARTITION is right (I re-derived it independently — see Failed Attacks), but the report's provenance for it is sloppy in three places (009, 010 link-type mis-citation; 008 provenance outside the ledger). If these rules are the template for the C41 Step-6 at ~10× volume, the citations must be machine-checkable or the trace will rot silently.

## FINDING 2 (MEDIUM) — "No semantic judgment enters except where a rule names it" overclaims; R4's "distinct question" test is semantic judgment, and it did real work twice

The report's header says semantic judgment enters only via R4's named exception, "which is then justified from link topology." But:
- R4's application to 005+006 is justified by the shared `retention` tag plus a question-phrasing argument ("A asks whether AGN can remove gas … D asks whether removal happened"). That phrasing IS the semantic judgment; the link topology (006 qualifies→005; 006 same_axis→001) alone would equally support folding 005/006 into Axis A as qualifiers — 006 literally carries a same_axis link into A's membership. The decision to elevate D is the right call (seed Step-6 grouping anticipates "limitations"; folding a scale-separated two-sided debate into A would hide it), but it is a judgment, and the report's claim of near-determinism is overstated.
- The "re-running the rules on the same ledger yields the same partition" line is true only because R4's question test happened to be resolved this way once. The rules as written are not deterministic for a fresh reader: R4 vs R5 precedence on 005 depends on accepting D's "distinct question," which the rules don't formalize.

Patch: reword the header to "deterministic except R4's distinct-question test, whose application is argued per-case and reviewable" — which is what actually happened, and is fine.

## FINDING 3 (LOW-MEDIUM) — All 16 entries carry verification_status `pending`; the map surfaces this only in a closing footnote

The map's final line discloses it ("All verification_status values in the source ledger are `pending`"), and LANA_REPORT flags it as ambiguity #1. But the map's own header advertises "Source of ALL claim content" and enum discipline without noting at the top that the underlying ledger is unverified-pending by its own field. A reader consuming Axis A's `widely_supported` label could miss that every bound entry is `pending`. The status enums are ledger-carried so this is not a modality violation — it's a prominence issue: the disclosure belongs in the header block, not line 268. (For the C41 track, Step 5's stance verification is precisely what flips this field — the pilot shows why that stage must not be skipped.)

## FINDING 4 (LOW) — Axis A's status presentation technically obeys the letter of the enum law while bending its spirit

Axis A lists ejective `widely_supported` / maintenance `contradicted_or_model_dependent` as per-side labels with no axis-level label, justified as "sides sit at different enum levels." Legally clean. But the seed named one axis status (`widely_supported_scoped` — off-enum, correctly replaced). The map's resolution (per-side labels) is the right repair, yet it means the summary table row for A is the only row whose "Status" cell is not a single enum value — a downstream consumer parsing the table for axis→status mapping will get two values for A and one for everything else. Minor structural inconsistency; recommend the table carry "per-side (see axis)" in A's cell explicitly. (It nearly does — "per side where sides differ" is in the header — so this is close to a non-finding; recording it for the C41 template.)

## FINDING 5 (LOW) — Two micro-inaccuracies in evidence narration

(a) Axis A "Best evidence" says the ejective side rests on "multiple scoped samples plus case" citing 2024NatAs + 2024MNRAS + 2014A&A under `clc_agn_001`, but the map's own countercase paragraph then treats the 10× SFR case as within `clc_agn_001`'s spans — ledger confirms the NatAs span IS in both 001 and 2299_001 (verified), so this is consistent, but the phrase "multiple scoped samples" oversells slightly: two of the three cited papers are the same journal-year family of the z~2–3 Na I D work, and the third (2014A&A) is `interpretation` zone, not `finding`. The ledger itself sets sample_size `multiple_scoped_samples_plus_case`, so the map is quoting the ledger — the oversell originates in the ledger's dimension, which the pilot correctly did not fix (report-don't-fix). Noting for the C41 corpus-protocol stage: sample_size dimensions should name count explicitly.
(b) Axis B map text says child 2's "half of profiles blueshifted ≥100 km/s" — initially suspected as imported from outside the ledger; RESOLVED on full-quote re-check: span_2024MNRAS_528_4976D_03 carries "Half of the absorption profiles are blueshifted by at least 100 km s−1" verbatim. The map is ledger-bound here. (Kept as a record of an attack that failed on completion of the check.)

## FINDING 6 (NIT) — Condensation report arithmetic: "K = 4 (seed, reproduced by R1) + 1 (R4 split) = 5" is right, but R1's description says simulation_cap entries "seed a fourth axis (E)" while the trace places 011 via R1 and 004 via R6 — meaning E's seed is 011 alone, and 004 joins by constraint. Consistent, but R1's text ("Entries tagged simulation_cap seed a fourth axis") reads as if both seed it. Trivial wording.

---

## ATTACKS THAT FAILED (verified defenses — the map got these right)

1. **Entry-binding attack.** Every entry ID named in the map exists in the ledger; all 16 appear exactly once in the coverage table plus the declared dual membership (004 in A+E). I re-checked the table mechanically: 16/16 certainty_level and modality values in the map's §6 table are byte-identical to the ledger. No phantom IDs, no dropped entries, no axis statements floating free of IDs.
2. **Modality-overflow attack.** I scanned every axis's position statements against bound entries' ledger modality: `may_or_can` entries are only ever stated as can/may; the D'Eugenio guard row is stated at `shows_can_occur` ("shows that … can occur"); 004/011 content is always "in simulations / under model assumptions"; the three `is_are_does` entries (007/009/010) are the only ones stated in bare "are" language — and the ledger indeed licenses `is_are_does` for exactly those. One borderline: Axis C's "must remain separate" (010) is stronger than "is" — but it quotes the ledger's own assertion wording ("must remain separate from central/BH predictors"), so it's ledger-carried, not map-added. No overflow found.
3. **Seed-departure attack.** All three departures are real, declared, and justified: (i) seed omits 008 — TRUE (seed axis lists contain no 008); adding it to C is forced by its qualifies→2299_003 link and its status as the corpus's only direct contradicts-stance observational row toward AGN-driver readings. (ii) seed omits 005/006 — TRUE; R4 split justified above. (iii) seed's `widely_supported_scoped` is genuinely NOT in `ledger_enums.json` certainty_level (enum list verified: established, widely_supported, emerging_sample_limited, actively_debated, contradicted_or_model_dependent, no_info) — replacing it was mandatory under the brief's enum-only rule. All seed reader-guards (never-universal, do-not-average, D'Eugenio exclusion, in-model-only cap, alternatives-visible) are verifiably restated in the map.
4. **Merge-rule-violation attack.** I re-executed R1–R6 against the raw link graph: R1 seeds {2299_001→A, 2299_002→B, 2299_003→C, 011→E}; R2 merges {001→A via generalizes-link with 2299_001 (present in both directions), 002→B, 002a/002b→B (specializes links verified)}; R3 override for 003 (risk_flags literally contains CASE_ROW_NOT_PREVALENCE_ANCHOR; its specializes→2299_001 pull toward A is real and correctly overridden — placement in B matches the seed too); R5 places 007/008/009/010→C (all four have direct links to 2299_003 — verified); R6 dual-membership for 004 (same_axis→001 AND simulation_cap tag — verified; and no other entry satisfies the dual condition: I checked all 16). Same partition. K=5 re-derived independently.
5. **Missed-axis attack.** Candidates I tried to construct: (a) a "tracer systematics" axis from 002a-vs-002b (17% vs 46%) — fails because the ledger encodes this WITHIN B via parent-child specializes links and the do-not-average verification note, not as an inter-entry debate; the map's dispersion paragraph handles it at exactly the ledger's level. (b) A "source-access/strength" axis — the ledger's source_access is uniform (`full_text`) on the contested entries; nothing to condense. (c) Splitting Axis E's "simulation support" from "simulation cap" — the ledger has one entry (011) plus 004's dual membership; a second axis would have exactly one member and no second side. No missed axis survives.
6. **Stance-matrix attack.** 45 rows; the three `contradicts` rows are 008's (toward AGN-driver), and two against 2299_003 (2015Natur + 2016MNRAS) — the map's Axis-C countercase section accounts for both (008 named; 2015Natur's row sits inside 007's "alternative channels" position, which the seed's reader guard explicitly frames as same_axis, not contradiction). The map's claim that 008 is the corpus's only direct contradicts-stance observational countercase toward the ejective mechanism is accurate per the matrix.
7. **Factual spot-checks that PASSED.** 17%/MOSDEF/z=1.4–3.8 (assertion match; span _03 finding-zone supports), 46%/113/massive/z~2 (assertion match), 3–100 M⊙/yr (span _05 quote verified verbatim), "ten times higher than the SFR … direct evidence for ejective SMBH feedback" (span _07 verbatim), 456-galaxy low-z sample for 008 (span _01 quote verified), 26,000 SDSS spectra in 007's Nature span (verified), EDGE-CALIFA + four-best-spaxel for 006 (spans _04/_05 verified), 007/009/010 bibcode lists (exact match), 004's corpus_gap_annotation (X-ray cavity/bubble gap, capped, do-not-reopen — map represents it faithfully including "queued … explicitly not to be filled inside this run"), 2022MNRAS.512.1052P entering 009 only at `qualifies` (verified against its span stance).
8. **Countercase-quota attack (roadmap Step-6 pass condition).** For each `widely_supported` label in the map (A-ejective, 007, 009, 010) I checked the "who would disagree, in-corpus?" answer exists: A→008 (contradicts, in-corpus); 007→ held by Axis A/E rows; 009↔010 mutual binding. The quota is met with in-corpus citations, not hand-waves.

## Patches requested (before this template is reused for C41 Step 6)

1. Fix R5's trace citations for 009/010 (drop the phantom same_axis→seed leg) and restate 008's provenance as ledger-only (qualifies→2299_003 suffices; the stance-matrix row is corroboration, not placement basis).
2. Reword the condensation header: determinism claimed for R1/R2/R3/R5/R6; R4 is argued per-case.
3. Move the verification_status=`pending` disclosure into the map's header block.
4. ~~Resolve Finding 5(b)~~ — RESOLVED during red-team: the ≥100 km/s figure is ledger-carried (span _03). No patch needed.
5. C41-template note: make trace-table citations mechanically checkable (entry, rule, link type, target) so a Goru-style checker can re-execute without semantic reads.

## Evidence ledger

Read in full (content): `AGN_STATUS_DEBATE_MAP_V1.md`, `CONDENSATION_REPORT.md`, `LANA_BRIEF.md`, `LANA_REPORT.md` (head), `claim_status_ledger.jsonl` (all 16 entries, all fields incl. every link target, every span quote for cited spans, verification notes, risk_flags, corpus_gap_annotation), `claim_source_stance_matrix.jsonl` (all 45 rows; all 3 contradicts rows isolated), `ledger_enums.json` (all vocabularies), `status_debate_map_seed.json` (full), `wording_contract_check.json` (structure + first templates), roadmap § Step 6 (lines 400–428).
Computed independently: full link-graph dump per entry; re-execution of R1–R6 → same partition, K=5; coverage-table certainty+modality byte-comparison (16/16 match); span-quote verification for every numeric claim in the map (17%, 46%, 3–100, 10×, 456, 26,000, four-spaxel, ≥100 km/s — all found verbatim in ledger spans); enum membership of `widely_supported_scoped` (absent — seed defect confirmed); dual-membership condition check across all 16 entries (only 004 qualifies).

## Uncertainties

- Whether Lana intended "multiple scoped samples plus case" as a quote of the ledger's certainty_dimensions (it is one — so Finding 5a is a ledger-dimension note, not a map error; stated as such).
- The seed's provenance (who authored it, whether its omissions were deliberate test scaffolding) — treated as given; departures judged on merit, not intent.

---

KUN_AGN_MAP_REDTEAM_COMPLETE_20260803
