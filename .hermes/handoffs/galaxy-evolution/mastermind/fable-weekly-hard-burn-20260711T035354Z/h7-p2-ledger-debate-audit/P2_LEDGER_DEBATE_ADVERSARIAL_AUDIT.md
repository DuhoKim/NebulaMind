FABLE_HARD_BURN_H7_P2_AUDIT_20260711T035354Z

# H7 — Adversarial audit of the P2 source ledger + debate map

Burn `fable-weekly-hard-burn-20260711T035354Z` · lane H7 · audited packet: `fable-weekly-burn-20260711T010503Z/p2-cycle7-source-ledger/`
Audit window: 2026-07-11T04:13:19Z → 2026-07-11T04:36Z (UTC). Zero network calls; read-only on every input; lead content verification explicitly OUT of scope (internal integrity only, per brief).

## Packet verdict: **PASS-WITH-FIXES**

The packet's load-bearing claims all survive adversarial recomputation: every status count is exactly right (including the 39 `NEEDS_NETWORK_VERIFICATION` / 5 retained figures downstream lanes were given), every custody hash matches, every spot-checked quote is verbatim in the pinned snapshots, and the map/candidate never contradict the ledger. Two MINOR precision defects (one unsupported qualifier in the gated candidate, one out-of-bounds citation index in the ledger) and two NOTEs should be fixed before integrator use; none changes any count, priority, or classification.

## Findings table

| ID | Severity | Location | What is wrong | Why it is wrong | Proposed disposition |
|---|---|---|---|---|---|
| H7-F01 | MINOR | `PRIOR_WORK_COMPARISON_CANDIDATE.md` §1, para 3: "median $\log_{10}$ sSFR of -14.85 dex for IllustrisTNG **centrals** piling up at an imposed SFR floor" | The population qualifier "centrals" has no on-disk support outside the rejected report. Its only occurrence on disk is RAW:55 ("green-valley centrals"), i.e. the rejected sidecar report itself. The cited ledger entry N05 (quoting CORR:51/91) never says "centrals"; the TORI:37 attestation says only that the abstract "reports the TNG and EAGLE medians … and explicitly frames them as simulation/preprint results"; the debate map (§3.3, D5) also omits it. | The candidate's own fail-closed inclusion rule: content "appears below **only if an on-disk record beyond the rejected sidecar report itself supports it**." A qualifier sourced solely from rejected material slipped into candidate prose, and N05's `network_pass_must_confirm` does not ask the future verification pass to check the "centrals" framing — so the defect would survive verification unnoticed. | Strike "centrals" (e.g. "for IllustrisTNG's green-valley population") **or** keep it and add the centrals framing to N05's `network_pass_must_confirm`. |
| H7-F02 | MINOR | `SOURCE_LEAD_LEDGER.json` lead R05, `local_basis`: "GEMINI_WEB_OUTPUT_CORRECTED.acceptance.json blocking_failures[2]" | Recomputed against the hash-pinned snapshot: `blocking_failures` has exactly 2 elements, indices 0 and 1. The "establishes an empirical baseline" failure is element **[1]** ("The corrected report still says the association establishes an empirical baseline…"). `blocking_failures[2]` is out of bounds under JSON's 0-based bracket notation. | A custody ledger's pointer into a hash-pinned file must resolve. Read charitably as 1-based ("failure #2") it matches, and the substance of R05 is unambiguous (`prohibited_establishes_empirical_baseline_count: 1` also confirms), but bracket notation in a JSON-referencing ledger reads as a 0-based index and dangles. | Correct to `blocking_failures[1]` (or prose: "the second blocking failure"). |
| H7-F03 | NOTE | `AGN_SFR_STATUS_DEBATE_MAP.md` (whole document) | R05 and R07 are the only 2 of 50 ledger ids never referenced in the map. All 48 others are covered explicitly or by the `U01–U26` range plus the §6.8 "Remaining N- and U-entries" catch-all. | No contradiction — R-entries need no network verification (all seven `network_pass_must_confirm` fields say "Nothing…"), so their absence from the §6 queue is correct. But R07 (raw report's 6.7 kpc vs tex's `1.2--6.5 kpc`) is directly germane to §1's fiber-scale bullet, which quotes `1.2--6.5 kpc` without flagging the rejected variant, and R05 (the "establishes" wording that collapsed the corrected report) would fit §5's misreadings list. | Optional completeness edit: cite R07 at the §1 fiber-scale bullet and add R05 to §5. No downstream lane is misled as-is. |
| H7-F04 | NOTE | Ledger V01 vs map §1 / candidate §1–§2 (`8,146` pairs) | The pair count `8,146` is asserted in map and candidate under VERIFIED_LOCAL tags, but no V-entry's `exact_claim`/`local_basis` covers the pair count itself (V01's quotes are truncated before it). | Support actually exists and was verified by this audit: `8,146` appears verbatim in pinned TEX:13 ("yields 8,146 pairs"), TEX:57 (table row), and TEX:74 ("8,146-pair") — 5 occurrences in the tex snapshot; the map §1 quote of TEX:13 is character-for-character. So the number is tex-grounded, merely not ledger-itemized; a strict reader of the ledger alone cannot see the pair count is verified. | Extend V01's `exact_claim`/`local_basis` to include the pair count (trivial edit; no value change). |

No BLOCKER or MAJOR findings. In particular, **no count mismatch of any kind was found** (the brief's designated MAJOR-defect trigger).

## Recomputed count table (claimed vs recounted)

| Quantity | Ledger `counts` block | `P2_RECEIPT.md` | Debate map | Recounted by H7 | Verdict |
|---|---|---|---|---|---|
| Total leads | 50 | 50 | — (n/a) | **50** (JSON array length) | MATCH |
| `VERIFIED_LOCAL` | 4 | 4 | V01–V04 used in §1 | **4** (V01–V04) | MATCH |
| `NEEDS_NETWORK_VERIFICATION` | 39 | 39 ("N01–N13 … U01–U26") | 5 retained + N03/N04/N08/N10 + `U01–U26` | **39** (N=13 + U=26) | MATCH — brief's downstream figure confirmed |
| `REJECTED` | 7 | 7 | R01–R04, R06 cited | **7** (R01–R07) | MATCH |
| Retained leads | `["N01","N05","N07","N09","N11"]` | 5 listed, same ids | §3 lists the same 5 | **5**; notes-flagged set identical; "k of 5" numbering 1–5 matches map §3 order and INTEG:53–57 | MATCH — brief's downstream figure confirmed |
| `UNCITED_NOT_USABLE` instances | 26 (+ `matches_acceptance_json: true`) | 26/26 | `U01–U26` | **26** U-entries, instance numbering 1/26…26/26 sequential; acceptance.json `uncited_not_usable_label_count` = **26** | MATCH |
| Sum check | 4+39+7 = 50 | same | — | **50** | MATCH |

## Full check log (all six families)

### Check 1 — Ledger integrity: **CLEAN**
- Valid JSON (parses; single top-level object; `leads` array of 50 objects).
- Lead ids unique, zero duplicates; per-prefix contiguous from 01 (V:4, N:13, U:26, R:7) and in file order.
- Status vocabulary: only the 3 legal values occur; prefix↔classification mapping (V→VERIFIED_LOCAL, N/U→NEEDS_NETWORK_VERIFICATION, R→REJECTED) holds for all 50.
- Field structure: no missing/unexpected fields on any lead. Invariant `local_basis == null ⇔ local_basis_reason present` holds for all 50 (V/R carry non-null `local_basis`; N/U carry null + reason). `network_pass_must_confirm` is null exactly on the 4 VERIFIED_LOCAL leads and non-empty on all others (R-entries state "Nothing…" explicitly — intentional, not orphaned).
- No empty `source_ref`/`exact_claim`/`notes`. Actionability: every lead identifies its source (URL, arXiv id, VizieR id, or named-paper/“unattributed at RAW/CORR line N” with a locate-a-citation action for N12/N13/U11/U12). Repeat-source cross-references (U07/U13/U22, U08/U14/U23, U09/U15/U24, U10/U16/U25, U01/U17, U04/U11/U20, U05/U06/U12/U21) are mutually consistent via `network_pass_must_confirm` "Same as …" chains.
- U-entry "label instance k/26" numbering: sequential 1–26, each equal to its id number.

### Check 2 — Count recompute: **CLEAN** (table above)
- Every count asserted anywhere in the packet was recomputed and matches. The two numbers downstream lanes were told — **39** `NEEDS_NETWORK_VERIFICATION` leads and **5** retained prioritized leads — are both exactly correct against the ledger, the map, the receipt, and (for the 26 U-instances feeding the 39) the pinned `acceptance.json`.
- Cross-file identity: ledger `source_file_sha256` block ≡ receipt snapshot table (all 13 rows) ≡ recomputed hashes.
- `uncited_label_count_matches_acceptance_json: true` re-verified against the snapshot acceptance.json (26 = 26). `prohibited_establishes_empirical_baseline_count: 1` matches R05's substance.

### Check 3 — Debate map §6 priority order + bidirectional references: **CLEAN** (with NOTE H7-F03)
- map→ledger: zero dangling references (every `[VNUR]\d\d` token in map, candidate, and receipt exists in the ledger).
- ledger→map: after accounting for the explicit `U01–U26` range and the §6.8 "Remaining N- and U-entries per `SOURCE_LEAD_LEDGER.json`" catch-all, only R05 and R07 are never referenced (H7-F03, NOTE — correct exclusion from the verification queue, since no R-entry has anything to verify).
- §6 order: items 1–7 (N01, U19, N09, N07, N05, N11, N08) are distinct, all exist, no duplicates; item 8 is a deterministic catch-all (ledger file order) over exactly the remaining 32 N/U leads. The order is total and deterministic. No contradiction with the retained-lead "k of 5" numbering (an identity, not a priority) or with any other packet statement. R01 appears inside item 1 as context ("documents the R01 misquote"), not as a queue entry.

### Check 4 — Stance integrity: **CLEAN**
- Inline status tags: every `[CLASSIFICATION — id]` tag in map and candidate mechanically matches the ledger classification of that id (zero mismatches).
- Both-sides check: no source is cited on opposite sides of the same claim without explicit reconciliation. The two candidates were examined: (a) Gatto nuclear excess (+0.21 dex, N03) vs Gatto global below-MS (N04) — D1 explicitly presents them as the same lead's aperture-dependent facets and frames sign-flip-across-apertures as the open question; (b) Ellison optical deficit (N01) vs Ellison IR enhancement ~1.5× (N02) — the ledger records the in-source reconciliation (RAW:21's "profound dichotomy based on selection wavelengths") and the map uses only N01.
- Arithmetic spot-check: D1's "+0.21 dex" = −1.34 − (−1.55) ✓.
- Wording-contract sweep (map + candidate, mechanical grep for establish/confirm/demonstrat/prove/settle): every occurrence is mention-not-use (prohibition lists), negation ("unsettled", "No side is settled"), or quoted rejected material; zero own-voice violations. The ledger's own prose is covered by its declared `quoting_note`; N11's paraphrase of TORI:39 even avoids importing TORI's own "establish".

### Check 5 — `PRIOR_WORK_COMPARISON_CANDIDATE.md` consistency with the ledger: **DEFECT (MINOR, H7-F01)**; otherwise clean
- Row set ≡ retained set: comparison rows are exactly RP-1 + N01/N05/N07/N09/N11; §4 exclusions are exactly the complement (N03/N04, N08, N10, U01–U26, R01–R07) — no overlap, no gap.
- Numeric fidelity: `-1.309`, `[-1.334,-1.283]`, `8,146`, `-0.06`, `-14.85`, `-11.71`, `1,123,718`, `0.02<z<0.12`, `J/ApJS/196/11`, WHAN `3 Å` all agree verbatim with ledger/map and with pinned snapshot lines (see Check 6/spot-checks). All `-0.12` and `6.7 kpc` occurrences are mention-not-use (retraction/exclusion lists).
- Attestation-level claims ("abstract level" for N01/N05/N07, "page level" for N09) match TORI:30/36/37/38 wording.
- Non-commensurability labels present at every absolute quantity; status tags travel with every row and paragraph.
- Defect: the "centrals" qualifier (H7-F01) — sourced only from the rejected raw report, contrary to the candidate's own inclusion rule.

### Check 6 — Receipt custody recheck: **CLEAN**
Every file `P2_RECEIPT.md` lists was recomputed (sha256 + bytes where claimed):
- Artifact table: `P2_ACK.md` 612 B `7635…95f670` ✓; `SOURCE_LEAD_LEDGER.json` 48925 B `faad…ab0d07` ✓; `AGN_SFR_STATUS_DEBATE_MAP.md` 13706 B `8f3d…0aafee` ✓; `PRIOR_WORK_COMPARISON_CANDIDATE.md` 9570 B `2545…414035` ✓; done marker 0 B (sha256 = empty-input digest `e3b0…52b855`) ✓.
- All 13 `sources-snapshot/` hashes ✓ (and identical to the ledger's embedded `source_file_sha256` block).
- Source-table live originals (brief, 2 integration files, wording-contract verdict, 9 outputs-dir files, cycle-5 flagship tex): all recomputed hashes match the receipt's claims — the live files are additionally *still* byte-identical to the snapshots at audit time (no drift since P2 ran).
- H7's own input custody: all four pinned input hashes matched before use (see `H7_RECEIPT.md`).

### Snapshot quote spot-checks performed under Checks 1/4/5 (all PASS)
Verbatim-substring verification against the hash-pinned snapshots: TEX:13 (full map §1 quote incl. `8,146 pairs`), TEX:19 (S/N bias + 60,000 subset), TEX:22 (`cidfernandes2011` citation), TEX:25 (`1.2--6.5 kpc`), TEX:34 (`specsfr_tot_p50`), TEX:50 (estimand definition quote), TEX:57 (table row), TEX:74 (`8,146-pair`, "currently indistinguishable…"); the map's "fixed 60,000-galaxy DR17 cache" is tex-grounded (TEX:13/19/22/31/34/74). CORR:45/51/53/57/59/61/63/79/85/87/89/91/95/97/99/101/103/105/107/121/131/133/135/137, CORR odd lines 23–41 and 139–161 all carry `UNCITED_NOT_USABLE` as the ledger claims. RAW:3/21/43/55/67/83/115/135/157 match the quoted claims (incl. both `1.2 kpc` and `6.7 kpc` on RAW:115, and the 25-percent misquote on RAW:21). TORI:30/36/37/38/39/40 and INTEG:24/31/53–57 match every ledger attestation citation checked. UNVERIFIABLE-OFFLINE: nothing in the six families — the only intrinsically offline-unverifiable material (whether external papers actually say what the leads record) is out of audit scope by the brief's own boundary.

## Method + safety
Mechanical checks: `audit_checks.py` (in this directory) — JSON structure, counts, id sets, cross-references, tag consistency, verb sweep. Hash recomputation and line spot-checks: `shasum -a 256`, `wc -c`, `awk`/`sed`/`grep`/`python3` one-shots, all read-only. No file outside `h7-p2-ledger-debate-audit/` was created or modified; zero network calls; prior burn root untouched (read-only).
