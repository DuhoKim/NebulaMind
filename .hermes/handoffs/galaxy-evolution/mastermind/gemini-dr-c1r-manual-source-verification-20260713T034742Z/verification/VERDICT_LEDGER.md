# VERDICT_LEDGER - Gate B source-verification (B-P3)

Packet: `gemini-dr-c1r-manual-source-verification-20260713T034742Z` - Lane: Lana (B-P3, verdict authority). Coordinator: Hwao.
Inputs (read-only, persisted Gate B store): `sources/EVIDENCE_CATALOG.json`, `sources/ROUTE_MAP.json`, `mechanical/ENTRY_SPAN_NOTES.jsonl`, `sources/text/*`, plus the acquisition/network-variance receipts. No network, no live retrieval; Goru spans are candidates, Lana decides.
**This is mechanical span-based verification, not deep expert reading. No quarantine release; changes no product/DB/wiki/trust state. Every citation stays QUARANTINED_PENDING_LOCAL_CHECK.**

## Verdict totals (reconciles to 73)

| Verdict | Count |
|---|---:|
| `SUPPORTED` | 17 |
| `SUPPORTED_WITH_SCOPE_NOTE` | 17 |
| `NOT_SUPPORTED` | 0 |
| `SOURCE_UNRESOLVED` | 1 |
| `EVIDENCE_INSUFFICIENT_ABSTRACT_ONLY` | 0 |
| `AMBIGUOUS_NEEDS_EXPERT` | 38 |
| **Total** | **73** |

## Lane x verdict

| Lane | SUP | SUP_SCOPE | NOT_SUP | SRC_UNRES | ABS_ONLY | AMBIG | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| `VERIFY_UNCERTAINTY_OR_SCOPE` | 6 | 6 | 0 | 1 | 0 | 5 | 18 |
| `VERIFY_SOURCE_FIDELITY` | 11 | 11 | 0 | 0 | 0 | 25 | 47 |
| `VERIFY_SCIENTIFIC_COMPARABILITY` | 0 | 0 | 0 | 0 | 0 | 8 | 8 |

## All 73 verdicts (source order)

| id | lane | code | idx | verdict | tier |
|---|---|---|---|---|---|
| M001 | UNC | UNCERTAINTY_CHECK | 3 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M002 | UNC | UNCERTAINTY_CHECK | 4 | `SUPPORTED` | T2_FULL_TEXT |
| M003 | UNC | UNCERTAINTY_CHECK | 4 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M004 | UNC | UNCERTAINTY_CHECK | 4 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M005 | UNC | UNCERTAINTY_CHECK | 7 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M006 | UNC | UNCERTAINTY_CHECK | 7 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M007 | UNC | UNCERTAINTY_CHECK | 14 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M008 | UNC | UNCERTAINTY_CHECK | 14 | `SUPPORTED` | T2_FULL_TEXT |
| M009 | UNC | UNCERTAINTY_CHECK | 17 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M010 | UNC | UNCERTAINTY_CHECK | 19 | `SUPPORTED` | T2_FULL_TEXT |
| M011 | UNC | UNCERTAINTY_CHECK | 21 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M012 | UNC | UNCERTAINTY_CHECK | 25 | `SUPPORTED` | T2_FULL_TEXT |
| M013 | UNC | UNCERTAINTY_CHECK | 27 | `SUPPORTED` | T2_FULL_TEXT |
| M014 | UNC | UNCERTAINTY_CHECK | 28 | `SUPPORTED` | T2_PUBLISHER_FULL_TEXT_HTML |
| M015 | UNC | UNCERTAINTY_CHECK | 10 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M016 | UNC | UNCERTAINTY_CHECK | 20 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M017 | UNC | UNCERTAINTY_CHECK | 34 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M018 | UNC | UNCERTAINTY_CHECK | - | `SOURCE_UNRESOLVED` | NONE |
| M019 | FID | CITED_CELL_CLAIM_REVIEW | 1 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M020 | FID | CITED_CELL_CLAIM_REVIEW | 1 | `SUPPORTED` | T2_FULL_TEXT |
| M021 | FID | CITED_CELL_CLAIM_REVIEW | 3 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M022 | FID | CITED_CELL_CLAIM_REVIEW | 3 | `SUPPORTED` | T2_FULL_TEXT |
| M023 | FID | CITED_CELL_CLAIM_REVIEW | 4 | `SUPPORTED` | T2_FULL_TEXT |
| M024 | FID | CITED_CELL_CLAIM_REVIEW | 4 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M025 | FID | CITED_CELL_CLAIM_REVIEW | 4 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M026 | FID | CITED_CELL_CLAIM_REVIEW | 6 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M027 | FID | CITED_CELL_CLAIM_REVIEW | 7 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M028 | FID | CITED_CELL_CLAIM_REVIEW | 7 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M029 | FID | CITED_CELL_CLAIM_REVIEW | 7 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M030 | FID | CITED_CELL_CLAIM_REVIEW | 7 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M031 | FID | CITED_CELL_CLAIM_REVIEW | 12 | `SUPPORTED` | T2_FULL_TEXT |
| M032 | FID | CITED_CELL_CLAIM_REVIEW | 11 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M033 | FID | CITED_CELL_CLAIM_REVIEW | 11 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M034 | FID | CITED_CELL_CLAIM_REVIEW | 14 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M035 | FID | CITED_CELL_CLAIM_REVIEW | 14 | `SUPPORTED` | T2_FULL_TEXT |
| M036 | FID | CITED_CELL_CLAIM_REVIEW | 15 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M037 | FID | CITED_CELL_CLAIM_REVIEW | 14 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M038 | FID | CITED_CELL_CLAIM_REVIEW | 17 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M039 | FID | CITED_CELL_CLAIM_REVIEW | 19 | `SUPPORTED` | T2_FULL_TEXT |
| M040 | FID | CITED_CELL_CLAIM_REVIEW | 20 | `SUPPORTED` | T2_FULL_TEXT |
| M041 | FID | CITED_CELL_CLAIM_REVIEW | 17 | `SUPPORTED` | T2_FULL_TEXT |
| M042 | FID | CITED_CELL_CLAIM_REVIEW | 21 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M043 | FID | CITED_CELL_CLAIM_REVIEW | 22 | `SUPPORTED` | T2_FULL_TEXT |
| M044 | FID | CITED_CELL_CLAIM_REVIEW | 22 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M045 | FID | CITED_CELL_CLAIM_REVIEW | 21 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M046 | FID | CITED_CELL_CLAIM_REVIEW | 25 | `SUPPORTED` | T2_FULL_TEXT |
| M047 | FID | CITED_CELL_CLAIM_REVIEW | 26 | `SUPPORTED` | T2_FULL_TEXT |
| M048 | FID | CITED_CELL_CLAIM_REVIEW | 25 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M049 | FID | CITED_CELL_CLAIM_REVIEW | 26 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M050 | FID | CITED_CLAIM_REVIEW | 32 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT_BIBLIOGRAPHICALLY_RESOLVED |
| M051 | FID | CITED_CLAIM_REVIEW | 22 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M052 | FID | CITED_CLAIM_REVIEW | 34 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M053 | FID | CITED_CELL_CLAIM_REVIEW | 35 | `AMBIGUOUS_NEEDS_EXPERT` | NONE |
| M054 | FID | CITED_CELL_CLAIM_REVIEW | 36 | `AMBIGUOUS_NEEDS_EXPERT` | NONE |
| M055 | FID | CITED_CELL_CLAIM_REVIEW | 37 | `AMBIGUOUS_NEEDS_EXPERT` | NONE |
| M056 | FID | CITED_CELL_CLAIM_REVIEW | 36 | `AMBIGUOUS_NEEDS_EXPERT` | NONE |
| M057 | FID | CITED_CELL_CLAIM_REVIEW | 10 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M058 | FID | CITED_CELL_CLAIM_REVIEW | 36 | `AMBIGUOUS_NEEDS_EXPERT` | NONE |
| M059 | FID | CITED_CELL_CLAIM_REVIEW | 11 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M060 | FID | CITED_CELL_CLAIM_REVIEW | 22 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M061 | FID | CITED_CELL_CLAIM_REVIEW | 26 | `SUPPORTED_WITH_SCOPE_NOTE` | T2_FULL_TEXT |
| M062 | FID | CITED_CLAIM_REVIEW | 30 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M063 | FID | CITED_CLAIM_REVIEW | 36 | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M064 | FID | CITATION_QUALITY_REVIEW | 1,2,3,4,5,6,7,8... | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M065 | FID | SOURCE_FIDELITY_REVIEW | 1,2,3,4,5,6,7,8... | `AMBIGUOUS_NEEDS_EXPERT` | T2_FULL_TEXT |
| M066 | CMP | COMPARISON_LABEL_REVIEW | 27 | `AMBIGUOUS_NEEDS_EXPERT` | NONE |
| M067 | CMP | COMPARISON_LABEL_REVIEW | 28 | `AMBIGUOUS_NEEDS_EXPERT` | NONE |
| M068 | CMP | COMPARISON_LABEL_REVIEW | 10 | `AMBIGUOUS_NEEDS_EXPERT` | NONE |
| M069 | CMP | COMPARISON_LABEL_REVIEW | 11 | `AMBIGUOUS_NEEDS_EXPERT` | NONE |
| M070 | CMP | COMPARISON_LABEL_REVIEW | 15 | `AMBIGUOUS_NEEDS_EXPERT` | NONE |
| M071 | CMP | COMPARISON_LABEL_REVIEW | 20 | `AMBIGUOUS_NEEDS_EXPERT` | NONE |
| M072 | CMP | COMPARISON_LABEL_REVIEW | 30 | `AMBIGUOUS_NEEDS_EXPERT` | NONE |
| M073 | CMP | COMPARISON_LABEL_REVIEW | 30 | `AMBIGUOUS_NEEDS_EXPERT` | NONE |

## Review notes (load-bearing)
- **M018 SOURCE_UNRESOLVED** - no source bound in the captured unit; not borrowed (rule 3).
- **M050 capped SUPPORTED_WITH_SCOPE_NOTE** - index 32 resolved via index-33 full text; verbatim note '32->33 same-work bibliographic mapping; byte identity unproven' carried per Hwao disposition; bare SUPPORTED unreachable through a cross-index mapping.
- **M044 (FLAMINGO emergent) - potential contradiction**: the retrieved span shows cluster gas-mass-fraction data used as a calibration target, conflicting with the claim that cluster relations were 'strictly excluded from calibration'. Surfaced for expert review; the FLAMINGO calibration-vs-emergent (kSZ) dispute is the standing suspect.
- **M027 / M037 - possible calibration-vs-result mischaracterization** (SIMBA GSMF as emergent agreement vs claimed calibration target; ROMULUS blastwave feedback reproduction vs claimed dwarf calibration).
- **M059 spurious match** - the mechanical span hit the word 'emergent' in the radiative-transfer sense (emergent luminosity), not an EMERGENT calibration status.
- **M064 / M065 document-level** - citation-quality and source-fidelity across all 37 indices; not certifiable from one bibliography span (rule 6). Known risks: OpenAIRE aggregator (idx27), project/data pages (idx2/8/13, true-tier, confined here).
- **M066-M073 comparability** - all AMBIGUOUS_NEEDS_EXPERT with per-entry semantic assessments; the uniform MATCHED_SELECTIONS across all eight rows is token-satisficing. **M072 (FLAMINGO kSZ) and M073 (BAHAMAS) share source index 30** - a shared, probably mis-attributed citation cannot establish selection commensurability for two different simulations.
- **Fail-closed posture**: doubt resolved to the lower verdict; abstract-only never yields SUPPORTED* (no entry was abstract-only - all resolved sources were T2 full text); no NOT_SUPPORTED asserted because a failed mechanical span search cannot prove a claim absent/contradicted (that needs expert reading) - such cases are AMBIGUOUS_NEEDS_EXPERT.

## Evidence-path custody correction (pre-B-P4)

An independent pre-B-P4 path audit (root cause recorded in `sources/SUPPLEMENTAL_CONTAMINATION_CORRECTION.json`) found that the supplemental resolver had attached a spurious, unrelated (wrong-topic particle-physics) arXiv review as an extra full-text candidate for source indices 1, 3, and 4, after an OUP 403/Cloudflare page title produced a false ADS discovery result.

**Correction (custody only):** the wrongly-attached idx01 supplemental text candidate has been removed from every `evidence_paths` array - all 13 entries where it appeared: **M001-M004, M019-M025, M064, M065** (it appeared three times within each of M064/M065). No scientific verdict, source quotation, rationale, scope note, ID, source order, or verdict total changed. Distribution preserved: **17 SUPPORTED / 17 SUPPORTED_WITH_SCOPE_NOTE / 1 SOURCE_UNRESOLVED / 38 AMBIGUOUS_NEEDS_EXPERT / 0 NOT_SUPPORTED / 0 abstract-only**.

Every affected non-document entry retained its correct index-aligned OUP/ADS T2 full text (the `idx01`/`idx03`/`idx04` `*_ads_arxiv_pdf_*` candidate), from which Goru's spans and Lana's quotations were already drawn; M064/M065 retain 40+ correct paths each. The quarantined text, its raw PDF, its per-index metadata, and their sha256 hashes are retained only for audit per the correction manifest and are deliberately not reproduced anywhere in these deliverables. Legitimate supplemental full-text files for other source indices are unaffected. (M050 continues to use index 33's full text for index 32 under the documented 32->33 mapping, unchanged.)

LANA_GATE_B_VERDICTS_DONE_20260713T034742Z
LANA_GATE_B_VERDICTS_CUSTODY_CORRECTED_20260713T034742Z
