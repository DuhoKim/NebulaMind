FABLE_HARD_BURN_H9_P4_AUDIT_20260711T035354Z

# H9 — Adversarial audit of P4's 13 claim/evidence candidates vs sources + wiki schema

- Auditor lane: H9 (independent, stretch wave), burn `fable-weekly-hard-burn-20260711T035354Z`
- Audited packet: `<prior root>/p4-derived-claims/CLAIM_EVIDENCE_CANDIDATES.md` (pinned sha256 `1c8d9a7d28566a19a957cac754a7b8c6c5981a3ad445eb3d3f9daacbd49f8b39`, 33,940 bytes — VERIFIED)
- Companion receipt audited: `P4_RECEIPT.md` (pinned sha256 `27a1efc000a6a5044e5a9a3199e3ef22dfebe9f33d522bafd8e8e98a6909a85b`, 6,829 bytes — VERIFIED)
- Schema audited against: `/Users/duhokim/NebulaMind/NebulaMind/wiki_schema.md` (working tree; sha256 at audit time `d1c04e1fcf1e9b412712d07407c42fccffcf12b5a2fc2eced59dba888594b5dd`, 6,333 bytes — identical to the hash P4 recorded, so P4 and H9 audited the same schema bytes)
- Method: byte-exact quote matching, token-aware numeral counting, manifest cross-check, arithmetic contradiction sweep — scripts and raw logs in `h9-p4-candidate-source-schema-audit/audit-work/` (`verify.py`, `verify_output.log`, `verify_manifest.py`, `verify_manifest_output.log`). Zero network calls; all inputs read-only.

## Packet verdict: **PASS**

No BLOCKER, MAJOR, or packet-side MINOR defects found. All 13 candidates trace byte-exactly to the pinned cycle-5 snapshots, respect the packet's stated conventions including both known rounding anomalies, conform to everything `wiki_schema.md` actually defines, and contain no internal contradictions (several overlapping quantities reconcile arithmetically to within rounding). One MINOR integration-side risk (H9-F02, `/wiki/interstellar-medium` page existence not confirmable offline) is already covered by P4's own gated follow-up queue; four NOTEs are cosmetic or documentation-level. Nothing requires a change to the packet before the (separately gated) integrator pass.

## Per-candidate verdict table (all 13, no sampling)

| Candidate | Traceability (quotes/lines) | Conventions (units/uncert./estimate-pref.) | Schema (wiki_shape vs wiki_schema.md) | Contradiction sweep | Notes |
|---|---|---|---|---|---|
| P4-C01 | CLEAN — 3/3 spans byte-exact @ FLG:13,57,74 | CLEAN — CI carried verbatim; anomaly-canonical `-1.283`; preferred-estimate rule stated | CLEAN — all 10 fields; galaxy/AGN/Current Research; 3 see_also | CLEAN — 8,146 consistent w/ C02/C03; 60,000 w/ all | H9-F04 (NOTE: 60,000/DR17 on cited lines, outside quoted spans) |
| P4-C02 | CLEAN — 2/2 spans byte-exact @ FLG:39,31 | CLEAN | CLEAN — Physical Properties legal | CLEAN — 39,553+12,234+8,146+67 = 60,000 exactly | H9-F02 (see_also `interstellar-medium`) |
| P4-C03 | CLEAN — 1/1 span byte-exact @ FLG:39 | CLEAN — separations w/ units, no-caliper rationale carried | CLEAN | CLEAN — 100% = 8,146/8,146; brackets C01 | — |
| P4-C04 | CLEAN — 2/2 spans byte-exact @ FLG:31 | CLEAN — diagnostics-not-results framing carried | CLEAN — Open Questions legal | CLEAN — 60,000/249,917 = 0.24008 ≈ 24.0% | — |
| P4-C05 | CLEAN — 2/2 spans byte-exact @ FLG:32,33 | CLEAN — `1.2--6.5` range dash verbatim | CLEAN | CLEAN — kpc span consistent w/ z-range/fiber | H9-F03 (receipt maps FLG:32/33/25; candidate cites 32/33) |
| P4-C06 | CLEAN — 2/2 spans byte-exact @ SUP:92,93 | CLEAN — `0.032 +/- 0.004` carried exactly; proxy-not-density framing | CLEAN — galaxy-clusters target legal | CLEAN — 3,456/15,000=0.2304→0.230; 2,710/15,000=0.1807→0.181; diff 0.049 ∈ [0.041,0.059]; 15,000 = 60,000/4 | — |
| P4-C07 | CLEAN — 1/1 span byte-exact @ SUP:103 | CLEAN — mass cut w/ units | CLEAN | CLEAN — 0.607×5,695 ≈ 3,457 ≤ 0.430×9,298 ≈ 3,998 (subset ordering holds) | — |
| P4-C08 | CLEAN — 1/1 span byte-exact @ SUP:114 | CLEAN | CLEAN | CLEAN — 4,440/60,000 = 0.0740 exactly; 0.074 vs C11's 0.136–0.418 reconciled (different definition family — see check log 5.7) | H9-F02 (see_also) |
| P4-C09 | CLEAN — 1/1 span byte-exact @ SUP:125 | CLEAN | CLEAN | CLEAN — 0.509−0.367 = 0.142 ∈ [0.112,0.170]; 0.367 ≤ 0.430 (C07) ≤ 0.509 | H9-F05 (NOTE: caveat's 55-arcsec has no in-candidate line ref) |
| P4-C10 | CLEAN — 2/2 spans byte-exact @ SUP:136 | CLEAN — both S/N-cut spacing variants correctly distinguished (SUP-SNCUT-B) | CLEAN — galaxy-formation target legal | CLEAN — Table-4 mass-bin marginals give first-bin-above-0.5 = 11.0–12.5 and BPT peak 0.520 in that bin | — |
| P4-C11 | CLEAN — 1/1 span byte-exact @ SUP:147 | CLEAN | CLEAN — Open Questions legal | CLEAN — 0.418/0.136 = 3.074 → 3.1; 8,146/60,000 = 0.1358 → matches tracer-lo 0.136 | H9-F02 (see_also) |
| P4-C12 | CLEAN — 4/4 spans byte-exact @ SUP:158 | CLEAN — erg/s catalog scale, dex offset, IMF-scale caveat carried | CLEAN — but target page slug is the H9-F02 slug | CLEAN — 6,729 vs C07's 5,695 explicitly non-conflated (note-specific denominator, both in source and candidate) | H9-F02 (target `/wiki/interstellar-medium`) |
| P4-C13 | CLEAN — 1/1 span byte-exact @ SUP:169 | CLEAN — spans bullet-anchored, NOT table-re-derived (cycle-6 failure class avoided); whole-row invariance rule stated | CLEAN | CLEAN — mass-bin marginals recomputed from Table 4 reproduce spans: low-sSFR [0.0050, 0.7293] ↔ 0.005–0.729; BPT [0.0029, 0.5203] ↔ 0.003–0.520; max BPT 0.520 = C10's peak | — |

Traceability totals: 23/23 quoted evidence spans byte-identical substrings of their cited snapshot lines (zero drift, zero line-number errors). All claim_text digit-runs (13/13 candidates) are present on the candidate's own cited lines.

## Findings table

| ID | Severity | Where (file + line/quote) | What / why it matters | Proposed disposition |
|---|---|---|---|---|
| H9-F01 | NOTE | `wiki_schema.md` (whole file, 6,333 bytes) vs brief check 4 | The schema file defines article structure, categories, cross-link and reference rules — it contains **no** claim/evidence table structure, no evidence typing, and no trust/stance fields. "Claim/evidence structure required by wiki_schema.md" is therefore only auditable as: category legality, slug format, target section legality, ≥3 see_also, reference format, attribution plan. DB-level ingestibility (claim_id/evidence_ids/page_version_fk/publish_state typing, trust/stance representability) is not decidable from this file; the packet correctly holds all such fields as `OFFLINE_PLACEHOLDER` (13/13 verified) and P4_RECEIPT Ambiguity 3 already discloses this. | No packet change. The gated integrator pass must validate against the live DB models, not this schema file. |
| H9-F02 | MINOR | `CLAIM_EVIDENCE_CANDIDATES.md` — C12 `proposed_page_slug: /wiki/interstellar-medium` (line 379); same slug in see_also of C02 (line 76), C05 (line 168), C08 (line 260), C11 (line 351) | `interstellar-medium` is schema-legal (named example topic of the `galaxy` category, wiki_schema.md line 60) but is **not** on the coverage map's 33-topic COVERED list (wiki_schema.md lines 107–140; DB has 44 pages total, so the page may exist among the 11 non-predefined ones — UNVERIFIABLE-OFFLINE). P4_RECEIPT's phrase "slugs proposed here were chosen from `wiki_schema.md` coverage list" is imprecise for this one slug. If an integrator trusted the slug blindly, C12 could target a nonexistent page. | At the gated integrator pass: confirm the page exists (or create it per schema) before registering C12; otherwise retarget C12 to a covered page (e.g. `/wiki/nebulae`). Risk already fenced by P4's own GATED follow-up item on slug registration. |
| H9-F03 | NOTE | `P4_RECEIPT.md` line 39 ("P4-C05 — flagship FLG:32/33/25") vs C05 evidence block (candidates lines 174–176: cites 32, 33 only) | Receipt's candidate map credits line 25 to C05, but the candidate cites only 32/33. C05's qualitative sentence "Single-fiber measurements can miss extended star-forming disks" is verbatim FLG line 25 wording. Purely qualitative — no numeral affected; conventions' numeral rule not triggered. | Cosmetic. On any future packet revision, add FLG:25 as evidence 3 of C05 (or drop "25" from the receipt map line). |
| H9-F04 | NOTE | C01 claim_text (candidates line 48): `60,000`, `DR17`; similarly DR17 in C02 (line 80), C04 (line 141) | These claim_text numerals are not inside any quoted evidence span of their candidate, but each IS present on the candidate's cited snapshot lines (60,000 on FLG:13 and FLG:74; DR17 on FLG:13/31) and each is manifest-mapped (FLG-60000, FLG-DR17) in the numerals_check. Consistent with the packet's §Conventions numeral scope; flagged because a stricter quote-only reading of "explicit source + line reference" would want the value inside a quoted span. | No change required. Optionally extend C01 evidence 1 to include the abstract's opening sentence on revision. |
| H9-F05 | NOTE | C09 caveats (candidates line 301): "55-arcsec fiber-collision bias" | The 55-arcsec figure appears in C09's caveat with no line reference inside C09; its support lives in C06-E2 (SUP:93, byte-verified), SUP:13 and SUP:24, and C09's own cited line 125 states the ranking is "the same projected-neighbor ranking described in the relative neighbor-count baseline above". Caveats are outside the §Conventions manifest-numeral rule (claim_text + quoted spans only). | No change required. Optionally add "(see C06 evidence 2, SUP:93)" to the caveat on revision. |

No H9 finding is BLOCKER or MAJOR. Census deviation (the one pre-declared MAJOR class) did not occur.

## Full check log (clean checks included)

### Check 0 — Input custody (fail-closed gate)
- 0.1 PASS `CLAIM_EVIDENCE_CANDIDATES.md` recomputed sha256 `1c8d9a7d…f8b39` = pinned; 33,940 bytes.
- 0.2 PASS `P4_RECEIPT.md` recomputed sha256 `27a1efc0…9a85b` = pinned; 6,829 bytes.
- 0.3 RECORDED `wiki_schema.md` sha256 `d1c04e1f…5dd` (6,333 bytes) — unpinned live file; equals the hash P4_RECEIPT recorded, so schema drift between P4 and H9 is excluded.
- 0.4 RECORDED `P4_CONDITION_PACKET.md` sha256 `738af1cbba1d315b6e85f3aec443be34b7c2bec374316db260b4ec1461a741a5` (read for context; conditions internally consistent with T0 plan; no candidate references it for values).

### Check 1 — Census
- 1.1 PASS exactly 13 `candidate_id:` lines; ids P4-C01…P4-C13 in order, no gaps, no duplicates (candidates lines 34…402).
- 1.2 PASS 13 `## P4-Cnn` section headings; coverage note's own "13 candidates" claim consistent.
- Verdict: CLEAN. (Deviation here would have been MAJOR; none.)

### Check 2 — Per-candidate source traceability (all 13; no sampling)
- 2.1 PASS snapshot custody: `sources-snapshot/rp1_flagship_polished.tex` sha256 `63b3920e…9384` (23,917 B) and `sources-snapshot/supplementary_denominator_atlas.tex` sha256 `a4e3d66c…dc71` (37,532 B) equal both the packet's §Provenance table AND the live cycle-5 originals in the runner tree (read-only recompute) — so snapshot line anchors are cycle-5 line anchors.
- 2.2 PASS 23/23 quoted evidence spans are byte-identical substrings of exactly the cited snapshot lines (script check; per-span PASS lines in `verify_output.log`): C01 FLG:13,57,74 (3) · C02 FLG:39,31 (2) · C03 FLG:39 (1) · C04 FLG:31×2 (2) · C05 FLG:32,33 (2) · C06 SUP:92,93 (2) · C07 SUP:103 (1) · C08 SUP:114 (1) · C09 SUP:125 (1) · C10 SUP:136×2 (2) · C11 SUP:147 (1) · C12 SUP:158×4 (4) · C13 SUP:169 (1). Includes the FLG-ROW-057 table row carried as one backticked string.
- 2.3 PASS claim_text numeral support: for every candidate, every digit-run in claim_text (comma-normalized) appears on that candidate's cited snapshot lines (13/13 PASS; the only values outside quoted spans are H9-F04's 60,000/DR17, still on cited lines).
- 2.4 PASS manifest mapping: all 65 distinct manifest entry ids referenced by the candidates exist in `INVARIANT_MANIFEST.json` (105 entries total, ids unique; manifest sha256 `f4eb857e…6717` matches the packet's §Provenance claim). The slash-joined mentions `FLG-DR17/SUP-DR17`, `FLG-OIII/FLG-NII` and the family globs `SUP-RUNID*`, `SUP-SHA-*` in prose all resolve to real entries.
- 2.5 PASS occurrence counts: for all 65 referenced entries, `exact_string` occurrences in the snapshots equal `occurrences_expected` — 62 via plain substring count; 3 (`SUP-CELLS` "15"=4, `SUP-CELL-MIN` "50"=5, `SUP-HALF` "0.5"=1) via the manifest's own `match_mode: numeric_token` (token-boundary count), exactly as the candidates' "(numeric_token)" tags disclose.
- 2.6 PASS whole-row invariants relevant to the packet: FLG-ROW-057 and SUP-ROW-176…SUP-ROW-190 (all 15 target-vector rows) `exact_string` byte-match their snapshot lines — C13's whole-row invariance caveat is accurate.
- 2.7 UNVERIFIABLE-OFFLINE (listed, not fetched; no network permitted): external literature references named in the tex bibliographies (ADS/arXiv/DOIs, e.g. `2005MNRAS.362...25B`, `10.1093/mnras/stac532`) — the packet quotes **no** quantitative value from them (verified: every claim numeral maps to FLG/SUP manifest entries), and P4's follow-up queue already gates any network verification. Cycle-5 custody JSON artifacts named inside the tex (e.g. `SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json`, `m1_rp2…m3_p3/analysis_results.json`, `provenance/REAL_DATA_SOURCE_CUSTODY.json`) are cited by the SOURCE as its own provenance, are not quoted numerically by the candidates, are outside P4_RECEIPT's file list, and were not probed by H9 (runner tree touched read-only only for the two tex originals in 2.1/6.x).
- Verdict: CLEAN (with the scope lines above).

### Check 3 — Conventions compliance
- 3.1 PASS LaTeX-escape rule applied as stated: evidence quotes carry `95\%`, `S/N$\geq3$`, `1.2--6.5`, `0.02<z<0.12`, `\(\log M_\star \geq 10.8\)`, `0.032 +/- 0.004` byte-verbatim; claim_texts render markup with digits identical (spot-verified across all 13).
- 3.2 PASS range dashes and intervals carried exactly: `1.2--6.5`, `11.0--12.5`, `[11.0,12.5]`, `[-1.334,-1.283]`, `0.005-0.729`, `0.003-0.520`, `[0.041, 0.059]`, `[0.112, 0.170]`.
- 3.3 PASS known rounding anomaly 1 (FLG-CI95): canonical `[-1.334,-1.283]` carried in C01 (3 evidence spans + claim_text); the manifest-documented re-derived corruption signature `-1.282` / `[-1.334,-1.282]` has **0 hits** in snapshots and candidates.
- 3.4 PASS known rounding anomaly 2 (SUP-ROW-188): snapshot line 188 carries canonical `2.830`; re-rounded `2.831` has 0 hits anywhere. C13 correctly anchors spans to the artifact result bullet (SUP:169), and the cycle-6 corrupted table-derived span strings `0.001-0.856` / `0.001-0.610` have 0 hits in snapshots and candidates.
- 3.5 PASS estimate-preference rule: C01/C03 carry the preferred-variant definition (with replacement, no caliper, 100% coverage) and label it "preferred"; no candidate promotes a non-preferred or parent-cascade value to a result (C04 explicitly carries the diagnostics-not-results framing).
- 3.6 PASS units and uncertainty: dex offsets with bootstrap 95% CIs (C01), medians with quartile fractions and bootstrap intervals (C06/C09), `erg/s` catalog scale with model-dependence caveat (C12), mass cut in `log M*` (C07/C12); the `s^{-1}` unit digits treated as manifest-excluded identifier notation per §Conventions.
- 3.7 PASS association-only wording contract: no "establishes/demonstrates/proves" or causal phrasing in any claim_text; every candidate carries scope caveats (fiber-centered / morphology-uncontrolled / selection-limited / non-volume-complete) where overread was possible; grep for the banned verbs over claim_texts: 0 hits.
- 3.8 PASS `verification: LOCAL_ONLY` present on all 13.
- Verdict: CLEAN.

### Check 4 — Schema conformance (`wiki_schema.md`)
- 4.1 PASS wiki_shape completeness: all 10 fields (page_id, claim_id, evidence_ids, page_version_fk, publish_state, category, proposed_page_slug, proposed_section, see_also, references) present in 13/13.
- 4.2 PASS DB-resident fields are `OFFLINE_PLACEHOLDER` in 13/13 (page_id, claim_id, evidence_ids, page_version_fk, publish_state) — no real DB ids/foreign keys/publish states leaked into offline staging.
- 4.3 PASS category legality: `galaxy` ×13; every proposed target topic (AGN, Galaxy Clusters, Galaxy Formation, Interstellar Medium) is a schema-listed `galaxy` example topic.
- 4.4 PASS target sections all belong to the schema's required article structure: Current Research ×9, Physical Properties ×2, Open Questions ×2. (No candidate targets Overview/Discovery & History/See Also/References — appropriate for research-derived claims.)
- 4.5 PASS slug format `/wiki/kebab-case` in all page + see_also slugs; see_also count = 3 in 13/13 (meets "at least 3"); cross-category links present (dark-matter, stellar-evolution) per the schema's encouragement; galaxy-page link templates (→ cosmology/stellar) satisfied by C10/C13 (dark-matter, stellar-evolution links).
- 4.6 PASS references format: shared [S1]/[S2] lines follow the schema's "Author, I. (Year). Title. Journal. DOI" pattern with `DOI: OFFLINE_PLACEHOLDER` (honest for unpublished offline manuscripts); every candidate cites exactly one of [S1]/[S2] correctly matching its source (C01–C05→S1, C06–C13→S2 — verified).
- 4.7 PASS attribution plan: packet Conventions carry the schema's required attribution note template for the gated integration step.
- 4.8 FINDING (H9-F01, NOTE): the schema defines no claim/evidence/trust/stance structures — that part of check 4 is not decidable from `wiki_schema.md`; nothing in the packet violates what the file does define. No candidate is ingestion-illegal against the schema file itself.
- 4.9 FINDING (H9-F02, MINOR): `/wiki/interstellar-medium` absent from the coverage map's covered list; page existence UNVERIFIABLE-OFFLINE (DB has 44 pages vs 33 predefined topics). All other 8 distinct slugs used (active-galactic-nuclei, galaxy-clusters, galaxy-formation, quasars, stellar-evolution, dark-matter, milky-way, nebulae) are on the covered list.
- 4.10 PASS coverage-map slug spot-check: bidirectional-link preference and page-existence checks beyond the coverage list require the live DB — correctly deferred to the gated integrator pass by the packet itself.
- Verdict: CLEAN with H9-F01 (premise limitation) and H9-F02 (integration-side risk, gated).

### Check 5 — Internal contradiction sweep (cross-candidate quantities)
- 5.1 PASS denominator census: 39,553 + 12,234 + 8,146 + 67 = 60,000 exactly (C02 ↔ C01/C03/C04/C06/C08/C11/C13 shared denominator).
- 5.2 PASS coverage identity: 8,146 of 8,146 = 100% (C03); same 8,146 as C01 pairs and C02 census; 60,000/249,917 = 0.24008 → 24.0% (C04).
- 5.3 PASS environment quartiles: 15,000 = 60,000/4; 3,456/15,000 = 0.2304→0.230; 2,710/15,000 = 0.1807→0.181; 0.230−0.181 = 0.049 ∈ [0.041, 0.059]; 0.032 → 3.2 pp (C06 internal).
- 5.4 PASS maintenance-heating subset ordering: BPT among massive low-sSFR (0.607×5,695 ≈ 3,457) ≤ BPT in massive subset (0.430×9,298 ≈ 3,998) (C07 internal consistency).
- 5.5 PASS radio-jet quartiles: 0.509−0.367 = 0.142 ∈ [0.112, 0.170]; overall massive fraction 0.430 (C07) lies between quartile values 0.367–0.509 (C09 ↔ C07).
- 5.6 PASS C07 (5,695) vs C12 (6,729) "massive low-sSFR" counts differ **by design**: both the source (SUP:158) and C12's claim_text/caveats carry the explicit note-specific non-conflation sentence; BPT fractions 0.607 vs 0.549 attach to their respective denominators. Not a contradiction.
- 5.7 PASS C08 (high-excitation prevalence 0.074) vs C11 (tracer prevalence range 0.136–0.418): different definition families — C11's census ranges over "simple optical tracer definitions" of the broad family (its floor 0.136 matches the strict broad-BPT class: 8,146/60,000 = 0.1358), while C08's 4,440 high-excitation subset is not one of those tracer definitions (separate artifact m2_p1 vs m3_p1). No candidate claims the range covers subsets. Not a contradiction.
- 5.8 PASS C13 spans ↔ Table 4 ↔ C10: recomputing mass-bin marginals from the 15 snapshot rows (lines 176–190; N-sum = 60,000 exactly) gives low-sSFR span [0.0050, 0.7293] ↔ claimed 0.005–0.729 and BPT span [0.0029, 0.5203] ↔ claimed 0.003–0.520 (within 3-dp rounding of rounded cells); first mass bin with low-sSFR fraction > 0.5 is 11.0–12.5 (0.729; the 10.5–11.0 marginal is 0.392) and BPT incidence peaks in 11.0–12.5 at 0.520 — independently reproducing C10's two claims. The finer mass×z cells (0.856/0.610 at line 188) exceed the mass-bin spans at cell granularity, exactly as the source's tablecomments and C13's caveat describe; the bullet-anchored spans are the mass-bin marginals, so no contradiction.
- 5.9 PASS tracer ratio: 0.418/0.136 = 3.074 → "3.1" (C11 internal, matches SUP-TRACER-RATIO).
- 5.10 PASS aperture geometry sanity: 3-arcsec at 0.02<z<0.12 ↔ 1.2–6.5 kpc is standard-cosmology consistent (≈0.40–2.2 kpc/arcsec), FLG:25 carries the identical pairing.
- Verdict: CLEAN — zero cross-candidate contradictions; three potentially-colliding overlaps (5.6, 5.7, 5.8) each carry explicit in-packet disambiguation.

### Check 6 — Receipt custody recheck (`P4_RECEIPT.md`, every listed file recomputed)
| File (as listed by P4_RECEIPT) | Receipt claim | H9 recompute | Verdict |
|---|---|---|---|
| `P4_ACK.md` | 410 B, `cda7b641…d147` | 410 B, `cda7b641d2bc14da8a51b76e7a4dfe7d913fd97d6319a672a0e96d2d20ddc147` | PASS |
| `CLAIM_EVIDENCE_CANDIDATES.md` | 33940 B, `1c8d9a7d…f8b39` | 33,940 B, same | PASS |
| `sources-snapshot/rp1_flagship_polished.tex` | 23917 B, `63b3920e…9384` | 23,917 B, same | PASS |
| `sources-snapshot/supplementary_denominator_atlas.tex` | 37532 B, `a4e3d66c…dc71` | 37,532 B, same | PASS |
| `FABLE_BURN_P4_DONE_20260711T010503Z` | 0 B marker | 0 B (sha256 = empty-file hash `e3b0c442…`) | PASS |
| Source: runner `…/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex` | `63b3920e…9384` | same (23,917 B) | PASS |
| Source: runner `…/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex` | `a4e3d66c…dc71` | same (37,532 B) | PASS |
| Source: `p1-rp1-invariants/INVARIANT_MANIFEST.json` | `f4eb857e…6717` | same (51,754 B) | PASS |
| Source: `p1-rp1-invariants/INTRODUCTION_LITERATURE_REFERENCE.md` | `874794a1…713a` | same (14,196 B) | PASS |
| Source: `wiki_schema.md` (recorded, unpinned) | `d1c04e1f…5dd` | same (6,333 B, still current in working tree) | PASS |
- 6.11 PASS receipt's scripted-count claims independently reproduced on the snapshots: `[-1.334,-1.283]`=4, `-1.309`=6, `8,146`=9 (plain; braced `8{,}146` is the separate FLG-8146-BRACED entry), `60,000`=11, `249,917`=1, `24.0\%`=1, `39,553`=1, `12,234`=1, `0.0045`=1, `0.00021`=1, `1.2--6.5`=2, `0.02<z<0.12`=2 — all exact.
- 6.12 PASS receipt's corruption-signature claims reproduced: re-rounded CI (`-1.282`) 0 hits; `2.831` 0 hits; cycle-6 spans `0.001-0.856`/`0.001-0.610` 0 hits — across both snapshots AND the candidates file.
- 6.13 FINDING (H9-F03, NOTE): receipt's candidate map line for P4-C05 says "FLG:32/33/25" while the candidate cites 32/33 only (details in findings table).
- Verdict: CLEAN (one NOTE).

## Bottom line

The P4 candidate set survives an adversarial pass intact: **PASS**. Every number a wiki reader would see traces byte-exactly to hash-verified cycle-5 sources; both historical corruption modes (re-derived CI bound, table-derived spans) are provably absent; the overlapping quantities across candidates reconcile arithmetically; and the wiki shaping violates nothing `wiki_schema.md` defines. The single action item before integration is H9-F02: confirm (or create) the `/wiki/interstellar-medium` page at the already-gated integrator pass.

FABLE_HARD_BURN_H9_P4_AUDIT_20260711T035354Z
