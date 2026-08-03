FABLE_HARD_BURN_H10_XPACKET_AUDIT_20260711T035354Z

# H10 — Cross-packet reproducibility + integration-order audit of P1–P4

Burn `fable-weekly-hard-burn-20260711T035354Z` · lane H10 · written 2026-07-11T04:33Z (UTC)
Audited set: prior burn `fable-weekly-burn-20260711T010503Z` packets P1–P4 + `BURN_ROLLUP.md` + `P4_CONDITION_PACKET.md` + `METER_LOG.md`; forward briefs `H1..H5_BRIEF.md` read for the consumption map only.
Method: every pinned sha256 recomputed; every file in all four packet dirs hashed (55 files); JSON deliverables re-parsed and recounted mechanically (python); headline markers checked; cross-quoted facts tabulated; prose claims spot-verified against the underlying files. Zero network calls; every input read-only.

## Overall verdict: **SAFE-TO-INTEGRATE** (in the §4 order)

Custody is perfect (14/14 pins match; 4/4 done markers exactly 0 bytes), every receipt-claimed hash/byte recomputes correctly, the cross-packet fact table has **zero disagreements**, and the findings list contains no BLOCKER and no MAJOR — only 2 MINOR process gaps and 3 NOTEs. Integration is safe provided the §4 sequencing constraints (canon adjudication before value-bearing downstream landings; serialized manifest mutation) are honored.

## 1. Reproducibility scorecard

| Packet | Inputs enumerated + pinned | Steps deterministic / re-runnable offline | Receipt hash/byte claims recompute | Score | Missing pieces |
|---|---|---|---|---|---|
| P1 `p1-rp1-invariants/` | YES — 12 sources snapshotted + hash-verified; 1 CSV hash-logged only; absolute paths given | YES — `tools/build_manifest.py` (19,178 B, pinned) shipped; manifest machine-checkable; CI/occurrence claims re-verified here | YES — all 5 artifact + 12 snapshot hashes match recomputation | **REPRODUCIBLE** | 1.1 MB CSV not copied (hash `4ea53af8…` pinned; recomputing the 4,239/2,731/1,508/26 stats needs the live runs tree) — see H10-F04 |
| P2 `p2-cycle7-source-ledger/` | YES — all 13 read sources snapshotted + hash-embedded in the ledger (`source_file_sha256`); brief hash recorded | YES — ledger counts recomputed from JSON here (50 = 4+39+7; N=13, U=26; retained = N01/N05/N07/N09/N11; 26 uncited instances) — all match | YES — all 4 artifact + 13 snapshot hashes match recomputation | **REPRODUCIBLE** | Prohibited-verb "mechanical scan" not shipped as a script (trivially re-runnable with grep; classification itself is prose judgment, fully documented fail-closed) |
| P3 `p3-m3-rt-baseline/` | PARTIAL — 15 sources hash-recorded, but only 6 snapshotted; 9 context/live files (live served RT copies, deepening HTML, director rollup, M3 status, Goru audit, 9-card seed) live in mutable trees | PARTIAL — deliverables are adjudication documents (no scripted checks); 6/6-card coverage and §0 mapping re-verified here | YES — 3 artifact + 6 snapshot hashes match; receipt correctly marks itself not-self-hashable (rollup hashed it: matches) | **PARTIALLY** | Snapshot the 9 hash-recorded-only sources for archival completeness (H10-F02); no scripted verifier |
| P4 `p4-derived-claims/` | YES — both tex sources snapshotted, hash-verified against brief pins (PASS×4 recorded); `wiki_schema.md` hash recorded as observed | MOSTLY — scripted numerals audit performed but the script was not shipped; I independently reproduced its key results (13 candidates C01–C13; corruption strings `-1.282`/`2.831`/`0.001-0.856` = 0 hits; CI string carried verbatim 7×; FLG-CI95 manifest occ = 4) | YES — 2 artifact + 2 snapshot hashes match recomputation | **REPRODUCIBLE** | Audit script absent from packet (no `tools/`) — H10-F01 |

## 2. Custody sweep — verdict CLEAN (all items)

Recomputed 2026-07-11T04:26–04:27Z. **All 14 pinned sha256 match exactly**:

| Input (prior burn root) | Pinned (H10 brief) | Recomputed | Bytes | Verdict |
|---|---|---|---:|---|
| `BURN_ROLLUP.md` | `b15afe07…4088` | same | 10,986 | CLEAN |
| P1 `INVARIANT_MANIFEST.json` | `f4eb857e…6717` | same | 51,754 | CLEAN |
| P1 `RCA_NUMERIC_DRIFT.md` | `45223b56…0096` | same | 15,941 | CLEAN |
| P1 `INTRODUCTION_LITERATURE_REFERENCE.md` | `874794a1…713d` | same | 14,196 | CLEAN |
| P1 `P1_RECEIPT.md` | `bdfebdc1…763a` | same | 7,765 | CLEAN |
| P2 `SOURCE_LEAD_LEDGER.json` | `faadcc22…ab07` | same | 48,925 | CLEAN |
| P2 `AGN_SFR_STATUS_DEBATE_MAP.md` | `8f3d3342…afee` | same | 13,706 | CLEAN |
| P2 `PRIOR_WORK_COMPARISON_CANDIDATE.md` | `2545c712…4035` | same | 9,570 | CLEAN |
| P2 `P2_RECEIPT.md` | `ddcb5eaa…4b83a` | same | 11,008 | CLEAN |
| P3 `M3_ACCEPTANCE_BASELINE.md` | `d028f3c7…d433` | same | 26,082 | CLEAN |
| P3 `RT_CARDS_DEEPENING.md` | `21564dd6…ed18` | same | 19,686 | CLEAN |
| P3 `P3_RECEIPT.md` | `70573e18…ec90b` | same | 10,475 | CLEAN |
| P4 `CLAIM_EVIDENCE_CANDIDATES.md` | `1c8d9a7d…8b39` | same | 33,940 | CLEAN |
| P4 `P4_RECEIPT.md` | `27a1efc0…9a85b` | same | 6,829 | CLEAN |

**Done markers** — all four `FABLE_BURN_Pn_DONE_20260711T010503Z` are exactly 0 bytes, sha256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (n=1..4): CLEAN.

**Beyond the pins** (adversarial extension): every remaining file in the four packet dirs was hashed and cross-checked against receipt/rollup claims — P1's 5 artifacts + 12 snapshot copies, P2's 4 + 13, P3's 3 + 6, P4's 2 + 2, plus all four ACK files. Every claimed hash/byte pair in the four receipts and in `BURN_ROLLUP.md` §3 matches recomputation, including `tools/build_manifest.py` (`0b81226d…`) and the manifest's own 12-entry `snapshot_sha256` block. Rollup §2 arithmetic re-verified: "14 receipt-claimed artifact hashes" = 5(P1)+4(P2)+3(P3)+2(P4) ✓; "15 logged burn-root polls" = 4+4+4+3 ✓. Headline top markers present on all four headline deliverables (P1 manifest JSON `marker` field, P2 ledger `marker` field, P3 baseline line 1, P4 candidates line 1) plus RCA/INTRO/deepening/debate-map companion markers ✓. Unpinned inputs recorded (also in H10 receipt): `P4_CONDITION_PACKET.md` `738af1cb…41a5` (1,892 B), `METER_LOG.md` `e1a316f9…c868d` (1,272 B), H1–H5 briefs `958a52b0…`, `e00e0272…`, `806ed10c…`, `4a556f64…`, `047a00aa…`.

## 3. Cross-packet fact table — verdict CLEAN (zero disagreements)

Every fact quoted in ≥2 places, with per-source values. AGREE = byte/number-identical everywhere it appears.

| # | Fact | P1 | P2 | P3 | P4 | Rollup / other | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | Cycle-5 flagship tex sha256 | `63b3920e…` (receipt, manifest, snapshot recomputed) | `63b3920e…` (receipt, ledger, snapshot recomputed) | — | `63b3920e…` (receipt, snapshot recomputed, 23,917 B) | rollup §2 "three lanes" | AGREE |
| 2 | Cycle-5 supplement tex sha256 | `a4e3d66c…` (37,532 B) | — | — | `a4e3d66c…` (37,532 B) | rollup §2 "two lanes" | AGREE |
| 3 | Canonical CI string | `[-1.334,-1.283]`, drift `→ -1.282` at FLG lines 13/57/65/74, cycles 6+7 (RCA; manifest FLG-CI95, occ 4, anomaly entry) | quoted verbatim in V01; "character-for-character" vs cycle-5 tex | — | carried verbatim 7×; re-rounded form 0 hits (recounted here: 0) | rollup §5 | AGREE |
| 4 | Median offset `-1.309` | manifest FLG-MEDIAN-OFFSET + FLG-ROW-057 | V01 quote | — | occurrences_expected 6 (receipt) | — | AGREE |
| 5 | Headline pair count `8,146` | manifest FLG-8146 occ 9, SUP-8146 occ 1 | — | — | receipt: `8,146`=9 | rollup "8,146-pair" | AGREE |
| 6 | Manifest = 105 entries = 73 scalars + 32 table rows | receipt + RCA line 23/27; JSON recount here: 105 entries, 32 `table_row`, 73 others, 0 dup ids | — | — | numerals check keyed to manifest ids | rollup §3/§5; H3 brief "105 entries" | AGREE |
| 7 | Carry stats 102/105 (c6), 103/105 (c7) | receipt finding 6; RCA line 27 verbatim | — | — | — | — | AGREE |
| 8 | Ledger 50 leads = 4 VERIFIED_LOCAL + 39 NEEDS_NETWORK (13 N + 26 U) + 7 REJECTED | — | receipt; JSON `counts`; my recount of 50 `classification` values: 4/39/7; prefixes V4/N13/U26/R7 | — | — | rollup §5 "(4/39/7)" | AGREE |
| 9 | Retained leads = N01, N05, N07, N09, N11 (all NEEDS_NETWORK) | — | receipt + ledger + debate map §3 | — | — | H1 brief "5 retained leads first" | AGREE |
| 10 | 26 UNCITED_NOT_USABLE instances = acceptance.json count | — | receipt "26/26"; ledger flag `uncited_label_count_matches_acceptance_json: true`; U-recount 26 | — | — | — | AGREE |
| 11 | Comparison candidate uses only the 5 retained leads + RP-1 numbers; Gatto/Piotrowska/Tempel excluded | — | receipt ambiguity 3; PW doc: N01/N05/N07/N09/N11 in §1–§2 (lines 17–21); N03/N04/N08/N10 only in §4 "Explicitly excluded" (lines 43–45) | — | — | — | AGREE |
| 12 | 6/6 RT cards, baseline + deepening, with §0 six→three mapping | — | — | receipt table; 6 `### Card` entries per doc recounted; §0 present | — | rollup §5 | AGREE |
| 13 | 13 claim candidates P4-C01…C13 | — | — | — | receipt list; doc recount 13 ids/13 headings | rollup §3/§5; H4 brief | AGREE |
| 14 | Cycle-6 referent swap: `0.005-0.729`/`0.003-0.520` → `0.001-0.856`/`0.001-0.610` (SUP line 169); SUP-ROW-188 `2.830 → 2.831` | RCA + receipt findings 2–3; manifest anomaly SUP-ROW-188 | — | — | corruption strings 0 hits (recounted: 0) | rollup §5 | AGREE |
| 15 | P4 condition: weekly 9% / 5h 27% at 02:16:37Z, before 03:15Z latest start | — | — | — | receipt late-start guard PASS (ACK 02:22:04Z) | condition packet = METER_LOG 02:16:37Z row, identical values | AGREE |
| 16 | Final meter 5h 30% / weekly 10% at 02:34:34Z; trajectory 12→30 / 6→10 | — | — | — | — | rollup §4 = METER_LOG rows 1 and 5 (02:35:18Z row, identical values) | AGREE |
| 17 | Lane timelines: ACKs 01:36:41 / 01:36:41 / 01:47:52 / 02:22:04Z; ends 02:13 / 02:03:53 / 02:04 / 02:33:00Z | receipts | receipts | receipts | receipts | rollup §1 identical; elapsed "~37/27/16/11 min" all consistent at minute precision (see H10-F03) | AGREE |
| 18 | All four receipts end with their exact done-marker line; markers 0-byte | receipt | receipt | receipt | receipt | rollup §2; recomputed here | AGREE |

## 4. Integration-order plan (all steps GATED on separate Duho approval — nothing here executes anything)

Dependency-safe order for landing P1–P4 outputs downstream. "Lands" = the gated integrator pass applies it; this document integrates nothing.

1. **Canon adjudication decision** (`-1.283` vs `-1.282`, `2.830` vs `2.831`) — P1 RCA/receipt follow-up 2, rollup item 3c, prepared by H3 §c. **Hard prerequisite for steps 2, 3, 6, 7**: it can flip two canonical strings that the audit list, the H1 queue values, and P4's candidate payloads carry verbatim. Must change manuscript + runner audit `numeric_invariants` + manifest **atomically** (all three or none).
2. **Manifest registration** — land P1 `INVARIANT_MANIFEST.json` (105 entries, post-adjudication values) into the sprint pre-audit flow (rollup item 3a; H3 §a mapping). Prereq: step 1. This is the base of all later numeric verification; all later manifest mutations are append-only against this registered base.
3. **Runner audit-list extension + verbatim-carry prompt patch** (rollup items 3b/3c; H3 §a/§b). Prereq: steps 1–2 (entries derive from the registered manifest). Runner tree remains read-only until this gated pass itself.
4. **Network verification pass** (rollup item 1; H1 workplan): P2's 39 NEEDS_NETWORK leads in debate-map §6 priority order (5 retained leads first), P1 EXT-1…EXT-4, P3 per-card network items, P4 enrichment values. Prereq to *start*: none (network gate approval only). Prereq to *register adopted values*: step 2 (external_reference entries append to the registered manifest — single mutation stream, serialized after step 2).
5. **P2 comparison-candidate integration** into any candidates/ tree (rollup item 3 final clause; H3 §d). Hard prereqs: step 4 (its cited leads N01/N05/N07/N09/N11 upgraded — the doc's own GATE note requires this) **and** step 3 (audit list live so its numerals are guarded). 
6. **Wiki/DB ingestion of P4's 13 candidates** (rollup item 4; H4 dry-run plan): resolve real page ids/slugs, replace the 68 `OFFLINE_PLACEHOLDER` fields, publish under idempotency checks. Prereqs: steps 1–2 (candidates carry the canonical CI string verbatim 7× — ingesting before adjudication risks publishing a string the canon then flips). Step 4 is a prereq only for external-value enrichment, not for base ingestion.
7. **Value-level verification of the remaining 7 topic artifacts** (rollup item 5; H5). Read-only; can start anytime. Its manifest **add-candidates** land append-only after step 2, serialized with step 4's external entries (one manifest-mutation queue).
8. **Process adoption** (rollup item 6): ledger-first requirement for future Gemini Web packets — folds into the H2 contract and future Hwao briefs; no artifact lands.

**Cycles:** none. The only potential cycle (manifest registration ↔ network-pass registration stubs) resolves by fixing the direction: base manifest first (step 2), external/add entries append-only afterwards (steps 4/7).

**H1–H5 forward-lane consumption map** (from their briefs only; every pinned hash in H1–H5 matches my recomputed values — no cross-brief pin disagreement):

| Lane | Consumes | Feeds plan step |
|---|---|---|
| H1 network-verification workplan | P2 ledger + debate map §6; P1 INTRO (EXT-1…4) + manifest; P3 baseline + deepening; P4 candidates | 4 |
| H2 Gemini REQ contract | P3 baseline (§4) + deepening + P3 receipt (+ REQ snapshot `b3488701…`) | 8 / gated sidecar run (rollup item 2) |
| H3 runner-integration packet | P1 manifest + RCA + INTRO; P2 comparison candidate (sequencing only) | 1, 2, 3, 5 |
| H4 wiki dry-run plan | P4 candidates + P4 receipt; repo `wiki_schema.md` + backend (read-only) | 6 |
| H5 supplement value verification | P1 receipt (snapshot itemization) + RCA + manifest + supplement snapshot `a4e3d66c…` | 7 |

**Ordering hazards between the running lanes' future outputs** (flagged, not defects):
- **HZ-1 (H3 × H1):** H1's queue rows record the "exact claim/value at stake" using current canon (`-1.283`, `2.830`). If step 1 adjudicates toward artifact-nearest values after H1's stubs are written, stub *values* go stale while ids stay valid. Disposition: at gate time, replay H1 stubs against the post-adjudication manifest before executing.
- **HZ-2 (H3 × H4):** H4's payloads embed P4's verbatim CI string (7 occurrences). Same staleness risk; hence step 6 sits after steps 1–2. Disposition: H4 plan should carry a "re-validate payload numerals against registered manifest" gate-time step.
- **HZ-3 (H1 × H5):** both propose manifest additions (external_reference vs add-candidates). Disposition: single serialized append queue with dedup at gate time.
- **HZ-4 (H2 independent):** no shared surface with H1/H3/H4/H5 outputs; its only coupling is process (step 8) and the P3 baseline. No hazard.

## 5. Gap sweep — rollup promises vs packet deliveries

- Every rollup §5 claim traced to a delivered artifact: P1 drift lines/RCA/105-manifest/verbatim-carry rule (RCA §5)/reference block (EXT-1…4 present) ✓; P2 50-lead 4/39/7 ledger + R07 fiber-scale rejection + debate map + comparison candidate ✓; P3 6/6 floors+reject-if+deepening + REQ contract-gap finding (baseline §4) + §0 lineage mapping ✓; P4 13 candidates + scripted-audit results (independently re-reproduced here) ✓.
- Rollup §3 inventory vs disk: exact match, including snapshot counts 12/13/6/2 and every hash. Nothing delivered is omitted from the rollup inventory; nothing inventoried is missing on disk. CLEAN.
- Rollup §2 verification claims re-verified (14 hashes, 15 polls, 4 markers, 4 headline top-markers): all reproduce. CLEAN.
- **Coverage gap (not a defect):** rollup follow-up item 6 (process adoption) has no forward H-lane — H1–H5 map 1:1 to items 1–5. Item 6 is explicitly "via a fresh Hwao brief", so the gap is by design; recorded so it isn't lost.
- Rollup §2 runner-liveness claims (PID 45665 state, elapsed 14:52:32) and §4 pane counts: UNVERIFIABLE-OFFLINE at H10 time (live observations from 02:39Z; re-probing the runner is outside this lane's read-only/no-liveness scope and would prove nothing about the burn-time claim). Internal consistency across preflight/condition/meter/rollup rows: CLEAN.

## 6. Findings table

| id | severity | where (file / line / quote) | what & why wrong | proposed disposition |
|---|---|---|---|---|
| H10-F01 | MINOR | `p4-derived-claims/P4_RECEIPT.md` — "Numerals check summary": "Scripted audit at 02:31:19Z…" | The audit script itself is not in the packet (no `tools/`, unlike P1). The receipt's per-string counts are therefore re-derivable only by re-authoring the script (I reproduced the key counts independently — they hold). Weakens turnkey reproducibility, not correctness. | Gated integrator pass (H4 execution) should regenerate and ship the numerals-audit script; future packet briefs: require `tools/` for any "scripted" claim. |
| H10-F02 | MINOR | `p3-m3-rt-baseline/P3_RECEIPT.md` source table (15 rows) vs `sources-snapshot/` (6 files) | 9 read sources are hash-recorded but not snapshotted, several in mutable trees (`frontend/public/…`, `static-publish…/live-root-before/…`, method3/autopilot). If those trees change, P3's reads can no longer be byte-re-verified from the packet alone. | Optional archival top-up in a gated pass; no integration impact (deliverable hashes verify; recorded hashes suffice while trees are unchanged). |
| H10-F03 | NOTE | `BURN_ROLLUP.md` §1 row P1: "~37 min / 75 target" | 01:36:41Z→02:13Z is ≈36.3 min if the minute-precision end is 02:13:00. Cosmetic rounding at minute-granularity timestamps. | None (record). |
| H10-F04 | NOTE | `p1-rp1-invariants/P1_RECEIPT.md`: "Hash-verified but not copied (1.1 MB CSV…)" | Deliberate size-based omission; recomputing the 4,239/2,731/1,508/26 control-reuse stats needs the live CSV at `4ea53af8…`. Disclosed, hash-pinned — reproducibility caveat only. | None; H5/H3 gated passes should re-verify the CSV hash before relying on those stats. |
| H10-F05 | NOTE | `METER_LOG.md` rows 01:52:12Z / 02:08:03Z: "retained last visible value" | Mid-burn 5h meter points are retained (possibly stale) readings, disclosed in-row; rollup §4 trajectory anchors on the two fresh OAuth endpoints (12%→30%, 6%→10%), which is sound. | None (record; keep using fresh-endpoint anchoring). |

No BLOCKER. No MAJOR. Checks 2 (custody), 3 (fact table), and 5 (gap sweep, except the two UNVERIFIABLE-OFFLINE live-state claims) are CLEAN throughout.

— end of audit —
FABLE_HARD_BURN_H10_XPACKET_AUDIT_20260711T035354Z
