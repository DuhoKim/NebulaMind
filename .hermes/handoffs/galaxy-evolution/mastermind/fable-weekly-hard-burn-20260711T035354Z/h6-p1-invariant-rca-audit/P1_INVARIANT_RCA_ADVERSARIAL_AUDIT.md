FABLE_HARD_BURN_H6_P1_AUDIT_20260711T035354Z

# H6 — Adversarial audit of the P1 invariant manifest + RCA packet

- Burn: `fable-weekly-hard-burn-20260711T035354Z`, lane H6, brief `H6_BRIEF.md`
- Audited packet: `fable-weekly-burn-20260711T010503Z/p1-rp1-invariants/` (4 pinned inputs, sha256-verified before use — see `H6_RECEIPT.md`)
- Method: fully offline, read-only. All 105 manifest entries mechanically recounted against the packet's own hash-verified `sources-snapshot/` copies of cycles 5/6/7 with an independent implementation of the manifest's `check_rule`; every derivable number recomputed; raw custody artifacts (flagship `analysis_results.json`, m3_p3 `analysis_results.json`, matched-pairs CSV) re-read and re-hashed; every file listed in `P1_RECEIPT.md` re-hashed. Audit tooling + raw output: `tools/h6_audit.py`, `tools/h6_audit_output.txt` (this lane's dir).

## Packet verdict: **PASS-WITH-FIXES**

The packet's core claims are correct and custody is flawless: cycle 5 satisfies all 105 manifest entries at exactly the expected counts; every raw-artifact value cited by the RCA is byte-exact against the custody-hashed artifacts; the three drift groups D1/D2/D3 reproduce mechanically; all four cycle-7 control-reuse statistics recompute exactly from the custody CSV; all 18 receipt hash/byte claims and all 12 snapshot hashes verify. One MAJOR defect (the RCA's headline carry counts 102/105 and 103/105 are wrong under the manifest's own rule), two MINOR manifest-entry defects (identifier-digit contamination of token counts, contradicting the manifest's own exclusions), and one MINOR spec defect (the near-miss clause is not machine-enforceable as written) should be fixed before the GATED integrator handoff. Nothing found undermines the root-cause statement or the verbatim-carry rule.

## Findings table

| id | severity | where (file, line/quote) | what is wrong | proposed disposition |
|---|---|---|---|---|
| H6-F01 | **MAJOR** | `RCA_NUMERIC_DRIFT.md` §2 line 27: "102 carry unchanged into cycle 6 and 103 into cycle 7 (occurrence-for-occurrence)"; repeated in `P1_RECEIPT.md` finding 6 | Recounting all 105 entries with the manifest's own `check_rule` gives: cycle 6 fails **13** entries (92/105 pass): FLG-CI95, FLG-ROW-057, SUP-BPT-PEAK (1 of 2 `0.520` occurrences lost with the D3 span rewrite), SUP-SPAN-QUENCH, SUP-SPAN-BPT, SUP-ROW-059…066 (8 layout-broken rows RCA §2.4 itself describes). Cycle 7 fails **3** (102/105): FLG-CI95, FLG-ROW-057, SUP-ROW-188. Even under the RCA's implicit value-level semantics the numbers are wrong (cycle 6 = 100/105, cycle 7 = 102/105): the RCA missed that whole-row invariant FLG-ROW-057 embeds the drifted CI in both cycles, and that D3 collaterally drops a SUP-BPT-PEAK occurrence. The qualitative D1/D2/D3 story and all drift locations are correct and complete; only the entry arithmetic is wrong — notable because §1 claims the cross-check "was done mechanically" | Correct §2 headline and receipt finding 6 to 92/105 (c6) and 102/105 (c7) rule-level — or state the grouping semantics and give 100/105, 102/105 value-level; list FLG-ROW-057 and SUP-BPT-PEAK explicitly as D1/D3 collateral |
| H6-F02 | MINOR | `INVARIANT_MANIFEST.json` entry SUP-CELLS ("15", occurrences_expected 4, lines [42,63,66,169]) | The line-42 occurrence is the substring `15` inside the SHA-256 hex `…8fae7d15e70…` of the radio-jet custody row (letters are not blockers under the `numeric_token` rule). It is not a "mass-redshift cells" occurrence, and the manifest's own `exclusions` say digits inside identifiers are not numeric invariants. Genuine occurrences are 3 (lines 63, 66, 169) | Regenerate with a tokenizer that rejects alphanumeric-adjacent matches (not just digit/comma/dot); set occurrences_expected 3, drop line 42. Latent fragility: any declared hash change in SUP-ROW-042 would silently break the "15" count |
| H6-F03 | MINOR | `INVARIANT_MANIFEST.json` entry SUP-CELL-MIN ("50", occurrences_expected 5, anchor line 22, allowed_context "minimum cell occupancy n >= 50") | Both line-22 occurrences are digits inside structural-quantity identifiers — `\(R_{90}/R_{50}\)` and `\texttt{petroR50}` — not the n≥50 threshold; the entry's anchor line contradicts its own allowed_context, and 2 of its 5 counted occurrences violate the manifest's exclusions (which name `R90/R50, petroR50/petroR90` verbatim). Genuine occurrences: lines 63, 66, 169 | Same tokenizer fix; set occurrences_expected 3, lines [63,66,169] |
| H6-F04 | MINOR | `INVARIANT_MANIFEST.json` `check_rule` (line 16), clause 2 (near-miss) | Not machine-enforceable as written for short-template kinds: a naive digit-wildcard reading flags 29 entries in clean cycle 5 itself (every 3-dp fraction sees ~75 digit-variants; SUP-ENV-CI `[0.041, 0.059]` and SUP-JET-CI `[0.112, 0.170]` are mutual "variants"; adjacent Table-4 rows are digit-variants of each other) because "same context" is never operationalized. It works only where the template is long (it does catch D1 `[-1.334,-1.282]` ×4, the drifted FLG-ROW-057, and D2's `2.831` row — verified). Also the kind list {ci_interval, point_estimate, fraction, table_row} omits range/dex/percent/count, so a D3-class rewrite that ADDS a table-derived span beside the carried artifact span (kind=range) is outside clause-2 scope | Operationalize context (e.g. variant must lie on a line whose non-digit skeleton matches the entry's anchor line, or within the sentence matching allowed_context), extend the kind list, or mark clause 2 as human-review guidance and rely on clause 1 (which caught every real drift) |
| H6-F05 | NOTE | `RCA_NUMERIC_DRIFT.md` §3.3 line 104 "cycle 7's base was byte-clean cycle 5 (SHA-verified)"; E4 line 88 | The lineage claim is not reproducible from the packet — no hash of cycle 7's *input* exists, only of its output. In-packet corroboration is real and I verified it (the 4 flagship bibitems cycle 6 deleted are present again in cycle 7; D3 span reverted; SUP-ROW-059…066 are back to the 3-column cycle-5 form), but the alternative lineage (cycle 7 built from cycle 6 + re-derivation) also reproduces every observation, since re-derivation from the m3_p3 bullet regenerates `0.005-0.729`/`0.003-0.520` regardless of base. Root cause is unaffected either way; only E4's "independent reproduction" strength leans on the lineage | Soften "SHA-verified" to "consistent with the byte evidence (bibitems, D3 reversal, table layout)" or cite runner-side lineage evidence |
| H6-F06 | NOTE / UNVERIFIABLE-OFFLINE | `INTRODUCTION_LITERATURE_REFERENCE.md` §1.3, SUP:103 vs SUP:158 | "9,298 emission-line galaxies, of which 5,695 are low-sSFR" (m1_rp3, log M*≥10.8) vs "the massive low-sSFR denominator contains 6,729 galaxies" (m3_p2, same 10.8 cut per SUP-MASSCUT) — two same-sounding populations 1,034 apart, never reconciled anywhere in the packet (presumably different low-sSFR thresholds per pilot; m1_rp3/m3_p2 artifacts were custody-hash-verified but not value-verified by P1 — its own GATED item 6). This is exactly the kind of apparent inconsistency a re-deriving prose writer might silently "fix" | Add one reconciliation sentence to the reference block (and/or to the two entries' allowed_context) stating the two denominators use different low-sSFR definitions, so prose lanes don't harmonize them |
| H6-F07 | NOTE | `P1_RECEIPT.md` finding 4; RCA header line 4 vs receipt t_end | "The only two audit/canon strings that are NOT nearest-roundings … are exactly the two that 'drift'" — overstated: D3's four span numerals also drifted (cycle 6) with no rounding anomaly; receipt finding 3 discloses D3, so this is imprecision, not concealment. Cosmetic: RCA self-dated "≈02:15Z" vs receipt `t_end 02:13Z`; receipt "T0+~37 min" silently means T0_lane (=t_ack), not burn T0 | Reword finding 4 ("the only two rounding-class drifts…"); minor timestamp tidy-up |
| H6-F08 | NOTE | `RCA_NUMERIC_DRIFT.md` §5 quick check (line 123) | `grep -F -c` counts matching *lines*, not occurrences — correct for the CI string (4 distinct lines) but the "analogously for every manifest entry" generalization undercounts entries with multiple same-line occurrences (FLG-UNCLASS `67` ×2 on line 39, SUP-CELL-MIN ×2 on line 22, FLG-8146 ×3 on line 39). `INTRODUCTION_LITERATURE_REFERENCE.md` §4 carries the correct `grep -o | wc -l` caveat; RCA §5 does not | Copy the §4 caveat into RCA §5 |

No BLOCKER findings. No evidence of fabrication, hash mismatch, or unsupported causal leap anywhere in the packet.

## Full check log

### Check family 1 — Manifest integrity → **DEFECT (MINOR: F02, F03, F04)**

| check | verdict | evidence |
|---|---|---|
| Valid JSON | CLEAN | parses; `entry_count` 105 == len(entries) 105 |
| Unique invariant ids | CLEAN | 105 unique, no duplicates |
| Required fields on every entry | CLEAN | id/file/line/exact_string/kind/allowed_context/match_mode/lines/occurrences_expected present on all 105 |
| Legal status values consistent | CLEAN | match_mode ∈ {substring: 97, numeric_token: 8}; kind ∈ 20 values (count 17, table_row 32, fraction 13, threshold 6, percent 5, dex 4, range 4, ci_interval 3, aperture 3, run_identifier 3, +8 others ×1–2); usage consistent with content (FLG-SEP-Z kind "other" = dimensionless redshift — acceptable) |
| Value + units + provenance per entry | CLEAN | every entry has exact_string (value), kind+allowed_context (units/meaning), file+line(s) (source); 9 entries additionally carry artifact_full_precision + artifact_field; base anchored by 12-hash `snapshot_sha256` block |
| Anchor line ∈ lines[]; occurrences_expected ≥ len(lines) | CLEAN | holds for all 105 |
| Duplicate / contradictory entries | CLEAN | no duplicate (file, exact_string) pairs; shared strings across files (60,000 / 8,146 / DR17 / run-IDs / [-1.334,-1.283] components) mutually consistent; `known_rounding_anomalies` block agrees with FLG-CI95 and SUP-ROW-188 entries and with the RCA |
| Token-count semantics | **DEFECT** | F02 (SUP-CELLS counts "15" inside a SHA-256 hex), F03 (SUP-CELL-MIN counts "50" inside `R_{50}`/`petroR50`) — both contradict the manifest's own exclusions list |
| check_rule enforceability | **DEFECT** | F04: clause 1 precise and verified; clause 2 ("no near-miss variant … same context") under-specified — naive implementation fails clean cycle 5 itself (29 entries), and the kind list omits range/dex/percent/count |
| Manifest self-consistency vs base | CLEAN | recount vs cycle-5 snapshot: **all 105 entries found at exactly occurrences_expected** (not merely ≥) — the gate passes its base with zero slack, so deletions are detectable too |

### Check family 2 — Arithmetic recompute → **CLEAN** (13/13 derivable numbers; miscount F01 charged to family 3/4)

| recompute | result |
|---|---|
| 39,553 + 12,234 + 8,146 + 67 = 60,000 (denominator census sums to cache) | PASS |
| 60,000 / 249,917 = 24.0% coverage (1 dp) | PASS |
| 3,456/15,000 = 0.230; 2,710/15,000 = 0.181 (env fractions, 3 dp) | PASS |
| 0.230 − 0.181 = 0.049 ∈ [0.041, 0.059] (env bootstrap interval brackets point diff) | PASS |
| 0.032 coefficient ↔ 3.2 percentage points | PASS |
| 4,440/60,000 = 0.074 (high-excitation fraction) | PASS |
| 0.509 − 0.367 = 0.142 ∈ [0.112, 0.170] (jet interval brackets point diff) | PASS |
| 0.418/0.136 = 3.07 → 3.1 (tracer ratio, 1 dp) | PASS |
| 2,731 + 1,508 = 4,239 (control reuse partition) | PASS |
| reuse feasibility: 8,146 − 2,731 = 5,415 uses over 1,508 controls, max 26 (2×1508 ≤ 5415 ≤ 26×1508) | PASS |
| CI rounding: raw [-1.3341385500000003, -1.2821399375] → nearest 3 dp [-1.334, **-1.282**]; canon upper -1.283 = floor-toward-−∞ only (inward/narrowing, anti-conservative) — anomaly exactly as manifest/RCA state | PASS |
| -1.308887 → -1.309; 0.00446 → 0.0045; 0.000210795 → 0.00021 (E2 companions nearest-round) | PASS |
| Table 4: all 15 n exact vs raw cells; 45 value cells nearest-rounded except **exactly one** — line 188 u−r raw 2.83066 → nearest 2.831, displayed 2.830 (E3's "only non-nearest cell" claim verified exhaustively) | PASS |
| Spans: artifact ranges [0.005283…, 0.729234…]/[0.002703…, 0.520208…] → 0.005-0.729 / 0.003-0.520 (canon); table-derived min/max → 0.001-0.856 / 0.001-0.610 (cycle-6 D3 values) — both referents reproduce | PASS |

### Check family 3 — RCA causal chain → **CLEAN with one NOTE (F05)**

| claim | verdict | evidence |
|---|---|---|
| E1: raw CI = [-1.3341385500000003, -1.2821399375] in flagship artifact | CONFIRMED | read from snapshot artifact whose sha256 = custody value 668ad7a6… (recomputed); byte-exact vs manifest artifact_full_precision |
| E2: canon -1.283 is the sole non-nearest flagship value | CONFIRMED | all companion values nearest-round (family 2); "-1.283 producible only by floor" verified |
| E3: 2.830 is the sole non-nearest cell of the 15×3 table | CONFIRMED | exhaustive recompute vs `target_vector_cells` (family 2) |
| E4: identical -1.282 in two independent cycles ⇒ deterministic re-derivation | CONFIRMED mechanism / NOTE on lineage | `[-1.334,-1.282]` ×4, zero canon occurrences, in both cycle 6 and 7 snapshots (recount); lineage sub-claim "cycle 7 from byte-clean cycle 5" is F05 — corroborated (bibitems restored ✓ verified, D3 reversed ✓, atlas rows 3-col ✓) but not hash-provable from the packet; root cause survives either lineage |
| E5: cycle-7 control-reuse stats derive from the custody CSV | CONFIRMED exactly | CSV live hash = custody 4ea53af8…; 8,146 data rows; control_specObjID: unique 4,239, once 2,731, reused 1,508, max reuse 26 — all four exact |
| E6: cycle-6 spans are table min/max | CONFIRMED | table-derived spans recompute to 0.001-0.856 / 0.001-0.610 exactly |
| E7: drift set = {canon} ∖ {nearest-rounded artifact values} | CONFIRMED | recount failure sets are exactly D1+D2 (+D3 referent change) and their row/occurrence collateral |
| Audit-failure custody (§1): c5 blockers []/missing []/fatal 0; c6+c7 missing ["[-1.334,-1.283]"], blockers ["numeric invariants missing"], fatal 1 | CONFIRMED | read from the three snapshot audit JSONs |
| §2.4 bibitem claims | CONFIRMED | tex recount: ellison2021/harrison2017/strateva2001/mendel2014 flg 1→0→1 across c5/6/7; cidfernandes2011/mcnamara2007 sup 1→0→1 (flagship copies retained in c6); dawson2013/dominguezsanchez2018 sup 0→0→2; undefined_citations [] in all three audits |
| §2.5 new-numeral claims | CONFIRMED | E5 recompute above |
| Unsupported leaps / circular reasoning / ignored alternative causes | NONE FATAL | each E-item independently grounded in hash-verified bytes; the one alternative not discussed (cycle-7-from-cycle-6 lineage) does not change the root cause (F05); "not fabrication / not typo / not lineage corruption" (§3.3) each backed by verified evidence |
| Headline carry counts (§2) | **DEFECT** | F01 — see findings table |

### Check family 4 — Cross-doc consistency (manifest ↔ RCA ↔ reference block incl. EXT-1…EXT-4) → **DEFECT (MAJOR: F01) + NOTES (F06, F07, F08)**

| check | verdict |
|---|---|
| D1/D2/D3 values and locations: manifest entries + notes ↔ RCA §2 ↔ recount of snapshots | CLEAN (identical everywhere: `[-1.334,-1.283]`→`[-1.334,-1.282]` at flagship 13/57/65/74 both cycles; 2.830→2.831 line 188 cycle 7 only; spans line 169 cycle 6 only) |
| known_rounding_anomalies ↔ FLG-CI95/SUP-ROW-188 entries ↔ RCA E2/E3 | CLEAN |
| Manifest `snapshot_sha256` (12) ↔ receipt source-snapshot table (12) | CLEAN — 12/12 identical |
| INTRODUCTION_LITERATURE_REFERENCE numerals ↔ manifest | CLEAN — every quoted numeral in §§1–3 appears in the manifest with identical formatting (manual cross-read; canon `-1.283` and `2.830` correctly insisted upon in §0) |
| EXT-1…EXT-4 slots | CLEAN — all four slots are placeholders with named works only (Ellison 2011, Schawinski 2010, Bluck 2014, Piotrowska 2022); zero external quantitative values anywhere in the block; all four cite keys exist in the cycle-5 flagship bibliography (verified in snapshot); GATED conditions (verify + register) stated |
| INTRO_LIT bibliography rule "cycle 7 re-added them" ↔ RCA §2.4 | CLEAN (verified true in tex; wording differs but facts agree) |
| RCA §2 carry counts ↔ manifest check_rule ↔ recount | **DEFECT — F01** |
| SUP:103 (5,695) vs SUP:158 (6,729) massive low-sSFR populations | NOTE / UNVERIFIABLE-OFFLINE — F06 |
| Receipt finding 4 "exactly the two" ↔ RCA D3 | NOTE — F07 |
| RCA §5 quick-check grep semantics ↔ INTRO_LIT §4 checklist | NOTE — F08 |

### Check family 5 — Receipt custody recheck → **CLEAN (18/18 claims + 13 observational)**

| group | result |
|---|---|
| Pinned packet inputs (brief) | 4/4 sha256 recomputed = pinned (manifest f4eb857e…, RCA 45223b56…, intro-lit 874794a1…, receipt bdfebdc1…) |
| Receipt artifact table | 6/6 bytes+sha match: P1_ACK.md (566, c3d072cb…), INVARIANT_MANIFEST.json (51,754), RCA (15,941), INTRO_LIT (14,196), tools/build_manifest.py (19,178, 0b81226d…), done marker (0 bytes) |
| Snapshot copies under `sources-snapshot/` | 12/12 sha256 = receipt-claimed original hashes (byte-identical claim verified) |
| Custody JSON cross-refs | c5 flagship/supplement hashes + both artifact hashes + CSV hash all PRESENT in REAL_DATA_SOURCE_CUSTODY.json |
| Live originals (observational — not a packet claim at audit time) | 13/13 still match receipt hashes as of 2026-07-11T04:2xZ (candidates ×10, runs ×2, CSV) — no post-packet drift of sources |
| Receipt poll log, GATED queue, deviations | plausible and internally consistent; timestamp nits in F07 |

## Bottom line

The P1 packet survives an adversarial recount essentially intact: its custody chain is perfect, its evidence chain E1–E7 reproduces from raw bytes, its manifest passes its own base package with zero slack, and its three drift groups are real, complete, and correctly diagnosed as re-derivation-vs-frozen-canon livelock. Before the GATED integrator handoff: fix the F01 carry-count arithmetic in RCA §2 / receipt finding 6, regenerate SUP-CELLS and SUP-CELL-MIN with an identifier-safe tokenizer (F02/F03), and either operationalize or demote the near-miss clause (F04). F05–F08 are wording/documentation polish. Verdict: **PASS-WITH-FIXES**.

FABLE_HARD_BURN_H6_P1_AUDIT_20260711T035354Z
