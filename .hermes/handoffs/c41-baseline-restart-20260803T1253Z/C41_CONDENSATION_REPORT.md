# C41 Condensation Report — 80 entries + 149 links + the 146-hit signal → K = 7 axes

- Lane: `c41-baseline-restart-20260803T1253Z` · compiled 2026-08-04 14:23 KST
- Author: Lana (no-overclaim lane). Hwao synthesis-reviews, Kun red-teams, Tori receipts; the
  author certifies nothing she writes.
- Inputs (read-only), pinned:
- `C41_LEDGER.jsonl` sha256 `e2938298dc9ee43b19ce1961fab45f3dc26db43d1e64147635b8c6dcdc2fbedf` (mtime 2026-08-04 14:11 KST, post-applier-v8)
- `C41_STANCE_MATRIX.jsonl` sha256 `59b61d7cc9f28253192954a1fab7355bc362da797464d22ec9fc5c354a122f6b` (Kun, Step 5)
- `VERIFICATION_STATUS_PATCH.jsonl` sha256 `bcfbeb0befdbc014477cd5d05ee1090326f80b6bfc0c4237da939d2dd977c8e2` (Kun, Step 5)
- `STEP0_FROZEN_QUESTION.md` sha256 `9ac5ca1f6321e2808eec3b9c2d38b8e616e0a9d774f4f277469c38fadbf789e1` (frozen)
- **Output: K = 7 named status/debate axes** (A1–A7), nested under / crossing the 3 frozen
  super-axes. K is an output of the rules below, not a target.

## The signal chain (every number stated for what it is)

`nDebates = 146` on the Lab's Ranking page is `round(strict_tension x size)` over the 1,317(+21
July-delta) C41 member titles/abstracts — a disagreement-**lexicon hit count**, not a count of real
controversies (plan, Kun F5). The chain from that signal to this report:

1. 1,317+21 cluster members → Step-1 executable selection protocol → **80 papers** (frozen lists,
   `SELECTION_SHAS.txt`).
2. 80 papers → Step-3/4 extraction + composition → **80 ledger entries** (one per paper; 149
   `same_axis` links), of which **76 carry claims** and 4 are honest zeros
   (`NO_CLAIM_RECOVERABLE`).
3. Step-5 adversarial stance verification (Kun): **76 verified_consistent + 4 verified_no_claim,
   zero failures** (stance matrix + patch, pinned above).
4. This condensation: 76 claims → **K = 7 axes**, of which **6 entries carry mechanical debate
   markers** (R3 below) and **4 axes contain live cross-paper conflict clusters** with
   stance-verified entries on both sides (A1, A3, A4, and — asymmetrically — A2), one axis is
   two-sided at the assumption level (A6), and two are one-sided-plus-open (A5, A7).

The 146-hit signal was the reason to attack C41; K = 7 is what that signal condenses to once
claims are extracted, bound to spans, and stance-verified. `nDebates` was signal; the map is the
measurement.

## Merge rules — determinism scoped honestly (AGN-pilot patch #2 imported by design)

Two layers. The **deterministic layer** re-executes mechanically from `C41_LEDGER.jsonl` alone;
the **judgment layer** is semantic, is named as such, and is argued per-case — but every judgment
placement in the trace table still carries a **machine-checkable citation** (AGN-pilot patch #5):
a verbatim substring of the entry's own ledger `assertion` field, verifiable without semantic
reads.

### Deterministic rules

- **R0 — Placeholder exclusion.** `certainty_level == "no_info"` → the entry joins no axis and is
  listed in the coverage table as a placeholder. Yields exactly {c41_018, c41_021, c41_059,
  c41_062} — the same 4 rows `VERIFICATION_STATUS_PATCH.jsonl` marks `verified_no_claim`. (The
  on-disk `verification_status` field cannot serve as the predicate — see the defect note below —
  so R0 binds to the certainty enum, which v8 did not touch.)
- **R1 — Super-axis binding.** `tags ∩ {formation_efficiency, chemical_enrichment,
  ionizing_output}` → the entry reports under those frozen super-axes. All 76 claim entries carry
  ≥1 frozen tag (checked; multi-tag entries report under each). The three super-axes come from the
  frozen question; they are super-structure, not members of K.
- **R2 — Link-graph degeneracy (a negative result stated as a rule).** Links are used only as an
  R1 consistency signal; **no sub-axis placement cites a link.** Evidence, mechanical: 149/149
  links have `type: same_axis`; every link description is the identical string "Shares the same
  major axis tag."; the undirected link graph has 2 nontrivial components plus 4 isolates
  (6 components total when isolates are counted as components) — one 74-entry mixed component,
  {c41_065, c41_066}, and the isolates {c41_014, c41_041, c41_070, c41_079} — whose composition
  tracks tag co-occurrence chains through entry ordering, not question structure. Contrast the AGN
  pilot, where `specializes`/`qualifies`/`contradicts` links carried the condensation (rules
  R2/R5 there); this ledger's link vocabulary never rises above tag-derived `same_axis`, so those
  rules have nothing to grip. Flagged for the contract lane: Step-4 link generation should emit
  typed links if Step-6 is to condense from topology.
- **R3 — Debate-marker extraction.** An entry is debate-bearing iff `modality == "mixed_debated"`
  OR `certainty_level == "actively_debated"` OR `tags ∩ {tension_reported, debate_countercase} ≠
  ∅`. Yields exactly **{c41_004, c41_005, c41_011, c41_037, c41_042, c41_076}**. Constraint on
  the judgment layer: every debate-bearing entry must be placed inside a named axis as holder or
  side. Satisfied: 004, 076 → A1; 011 → A2; 037 → A3; 042 → A4; 005 → A7.
- **R4 — Dual-membership cap.** At most two axes per entry; every dual placement is declared with
  both content bases. Applied once: **c41_065** (A1 basis: "non-accelerated decline of the UV
  luminosity density beyond z ~ 8"; A6 basis: "very steep faint-end slope (alpha ~ -2)").
  Cross-references in the map are notes, not membership.

### Judgment layer (J1–J7) — named as judgment

Grouping the 76 claims into question-axes is semantic: this ledger's links carry no structure
(R2), so — unlike the AGN pilot — the partition below R1 cannot be re-derived from topology. What
IS mechanical: (a) the R3 constraint above; (b) every J-row citation in the trace table is a
verbatim substring of the ledger `assertion` field. A checker re-executes the entire trace with
field lookups and substring tests only. The per-axis grouping arguments live in the map's axis
sections; a reviewer is entitled to accept or reject each.

**Checker semantics** (executed pre-ship, 0 failures; lane temp `_tmp_lana_step6_check.py`): for
each trace row — R0 rows: assert `ledger[entry].certainty_level == "no_info"`; J rows: assert the
quoted fragment is a substring of `ledger[entry].assertion`. Coverage: all 76 claims placed ≥
once; the only multi-placement is c41_065 (R4). R3: all six markers placed.

## Assignment trace (every entry, its rule, its machine check)

| entry_id | rule | machine check (re-executable) | axis |
|---|---|---|---|
| c41_001 | J5 | `assertion contains "sub-solar S/O and Ar/O"` | A5 |
| c41_002 | J3 | `assertion contains "Abundance Discrepancy Factor"` | A3 |
| c41_003 | J6 | `assertion contains "non-zero ionizing photon escape fractions"` | A6 |
| c41_004 | J1 | `assertion contains "mild UV luminosity function evolution towards z~12"` | A1 |
| c41_005 | J7 | `assertion contains "inconsistent with model tracks produced by AGN-NLR ionization"` | A7 |
| c41_006 | J3 | `assertion contains "[Si III] 1893 emission line"` | A3 |
| c41_007 | J5 | `assertion contains "bursty star formation on 10 Myr vs 100 Myr timescales"` | A5 |
| c41_008 | J4 | `assertion contains "scaling relations between stellar mass, oxygen abundance, and star-formation rate"` | A4 |
| c41_009 | J3 | `assertion contains "choice of fitting parameterization"` | A3 |
| c41_010 | J7 | `assertion contains "arguing against the presence of an AGN"` | A7 |
| c41_011 | J2 | `assertion contains "constant star-formation-efficiency prediction up to z = 12"` | A2 |
| c41_012 | J3 | `assertion contains "Auroral-line detections at z > 3"` | A3 |
| c41_013 | J5 | `assertion contains "460 Myr after the Big Bang"` | A5 |
| c41_014 | J6 | `assertion contains "blue UV continuum slopes (beta = -2.3 to -2.7)"` | A6 |
| c41_015 | J3 | `assertion contains "O32, Ne3O2, O3N2, and O3S2 display large scatter"` | A3 |
| c41_016 | J5 | `assertion contains "conveyor-belt episode"` | A5 |
| c41_017 | J5 | `assertion contains "N-emitter GN-z9p4"` | A5 |
| c41_018 | R0 | `certainty_level == "no_info"` | excluded (placeholder) |
| c41_019 | J5 | `assertion contains "gas bridge connecting the main system"` | A5 |
| c41_020 | J4 | `assertion contains "challenge the fundamental metallicity relation"` | A4 |
| c41_021 | R0 | `certainty_level == "no_info"` | excluded (placeholder) |
| c41_022 | J2 | `assertion contains "THESAN simulation"` | A2 |
| c41_023 | J3 | `assertion contains "the direct method remains an important and successful tool"` | A3 |
| c41_024 | J3 | `assertion contains "ionization correction factors"` | A3 |
| c41_025 | J5 | `assertion contains "12+log(O/H) = 7.16"` | A5 |
| c41_026 | J3 | `assertion contains "auroral [O III] 4363 line"` | A3 |
| c41_027 | J4 | `assertion contains "Local Volume mass-metallicity relation"` | A4 |
| c41_028 | J5 | `assertion contains "local analogues of high-redshift galaxies"` | A5 |
| c41_029 | J3 | `assertion contains "inconsistent with the z ~ 0 reference sample"` | A3 |
| c41_030 | J5 | `assertion contains "previous star formation lasting several tens of Myr"` | A5 |
| c41_031 | J2 | `assertion contains "top-heavy IMF raising the theoretical O/Fe limit"` | A2 |
| c41_032 | J3 | `assertion contains "R23 calibration is inconsistent"` | A3 |
| c41_033 | J3 | `assertion contains "underestimates metallicity by 0.05-0.1 dex"` | A3 |
| c41_034 | J3 | `assertion contains "H II-region conditions"` | A3 |
| c41_035 | J3 | `assertion contains "N2S2 and N2O2 inconsistent"` | A3 |
| c41_036 | J4 | `assertion contains "fundamental metallicity relation (FMR)"` | A4 |
| c41_037 | J3 | `assertion contains "strong-line metallicity relations remain valid in the high-redshift universe"` | A3 |
| c41_038 | J3 | `assertion contains "BPT-diagram offset of z ~ 2 galaxies"` | A3 |
| c41_039 | J4 | `assertion contains "star-forming main sequence"` | A4 |
| c41_040 | J4 | `assertion contains "mass-metallicity relation with consistent selection"` | A4 |
| c41_041 | J6 | `assertion contains "leakage of ionizing radiation"` | A6 |
| c41_042 | J4 | `assertion contains "Andrews & Martini (2013) stellar mass-metallicity relation"` | A4 |
| c41_043 | J3 | `assertion contains "do not strongly evolve with redshift"` | A3 |
| c41_044 | J3 | `assertion contains "indicator-dependent disagreement persists"` | A3 |
| c41_045 | J3 | `assertion contains "often mutually inconsistent"` | A3 |
| c41_046 | J1 | `assertion contains "rapid decline in the observed star-formation-rate density at z > 8"` | A1 |
| c41_047 | J1 | `assertion contains "deficit of z ~ 10 galaxies"` | A1 |
| c41_048 | J4 | `assertion contains "median metallicity of 12+log(O/H) = 8.34"` | A4 |
| c41_049 | J3 | `assertion contains "disagree systematically as a function of metallicity"` | A3 |
| c41_050 | J7 | `assertion contains "rule out an AGN as the dominant source of ionizing photons"` | A7 |
| c41_051 | J6 | `assertion contains "luminous-compact-galaxy population"` | A6 |
| c41_052 | J4 | `assertion contains "mass-metallicity relation at z >~ 3 remain poorly constrained"` | A4 |
| c41_053 | J4 | `assertion contains "low-mass, high-redshift mass-metallicity relation agrees with extrapolations"` | A4 |
| c41_054 | J4 | `assertion contains "spatially resolved (annular) abundance estimates"` | A4 |
| c41_055 | J4 | `assertion contains "consistent with the z <= 2.2 mass-metallicity relation"` | A4 |
| c41_056 | J1 | `assertion contains "ruling out a non-evolving UV luminosity function"` | A1 |
| c41_057 | J4 | `assertion contains "systematically lower gas-phase metallicity"` | A4 |
| c41_058 | J3 | `assertion contains "high ionization parameter"` | A3 |
| c41_059 | R0 | `certainty_level == "no_info"` | excluded (placeholder) |
| c41_060 | J3 | `assertion contains "faint rest-frame optical lines"` | A3 |
| c41_061 | J3 | `assertion contains "first direct-method metallicity measurement at z > 1"` | A3 |
| c41_062 | R0 | `certainty_level == "no_info"` | excluded (placeholder) |
| c41_063 | J1 | `assertion contains "decreases significantly from z ~ 9 to z ~ 12"` | A1 |
| c41_064 | J2 | `assertion contains "constant star-formation-efficiency model"` | A2 |
| c41_065 | J1 | `assertion contains "non-accelerated decline of the UV luminosity density beyond z ~ 8"` | A1 |
| c41_065 | J6 | `assertion contains "very steep faint-end slope (alpha ~ -2)"` | A6 |
| c41_066 | J6 | `assertion contains "required to reionize the Universe"` | A6 |
| c41_067 | J1 | `assertion contains "contamination rate from dusty z < 5 galaxies"` | A1 |
| c41_068 | J2 | `assertion contains "tension between theory and observations at z > 4 has been largely resolved"` | A2 |
| c41_069 | J6 | `assertion contains "z_reion ~= 10.6 +/- 1.2"` | A6 |
| c41_070 | J6 | `assertion contains "complete reionization by z ~ 6"` | A6 |
| c41_071 | J1 | `assertion contains "no evidence of a fundamentally different shape"` | A1 |
| c41_072 | J6 | `assertion contains "very blue UV continuum slopes (median beta <~ -2.5)"` | A6 |
| c41_073 | J2 | `assertion contains "Bursty star formation"` | A2 |
| c41_074 | J1 | `assertion contains "UV luminosity function evolves slowly at high redshift"` | A1 |
| c41_075 | J5 | `assertion contains "Grand Challenge"` | A5 |
| c41_076 | J1 | `assertion contains "clear tension with pre-JWST theoretical predictions"` | A1 |
| c41_077 | J4 | `assertion contains "inconsistent with the equilibrium conditions underlying the local fundamental metallicity relation"` | A4 |
| c41_078 | J1 | `assertion contains "challenged traditional theoretical models"` | A1 |
| c41_079 | J6 | `assertion contains "sufficient to reionize the Universe given high escape fractions"` | A6 |
| c41_080 | J2 | `assertion contains "star-formation duty cycle"` | A2 |

Coverage: 76/76 claims assigned; 1 dual membership (c41_065, declared under R4); 4 placeholders
excluded by R0; 0 unaccounted. (AGN-pilot Finding 1 — a silently swallowed entry — is structurally
impossible here: the checker fails on any claim entry absent from the trace.)

## Which entries merged where, which stand alone

- **Two-sided conflict clusters (stance-verified entries on opposing sides):** A1 (slow-evolution
  004/074/076/078 vs rapid-decline 047/056/063, + census qualifiers 046/067/071/065); A3
  (calibrations-shift 006/015/032/033/035/044/045/049 vs calibrations-workable 043/023/024, holder
  037); A4 (framework-holds 036/053/055/027/057 vs deviations 020/077, with 042 split across its
  own sSFR window); A2 (sufficiency-to-a-horizon 011/022/064/068 vs modification-invoked
  031/073/080 — asymmetric: the dispute is where sufficiency ends, not a flat contradiction).
- **Two-sided at the assumption level:** A6 (budget sufficient under stated assumptions 065/066/079
  vs residual tension 070/069; escape evidence case-level only: 003/041).
- **One-sided-plus-open (declared):** A5 (early-enrichment knowns 001/007/013/017/025/028/030 +
  frame-holder 075 + channel-exclusion 016 with no in-corpus defender of the excluded channel;
  019 peripheral gas-supply case — the weakest placement in the map, flagged as such); A7 (three
  case-level AGN exclusions 005/010/050; no in-corpus pro-AGN counterparty).
- **Nothing dropped:** the 4 placeholders are excluded by rule and listed; every other entry is in
  the trace.

## K as an output

K = 7 = **5 axes anchored by R3 debate markers** (A1 ← 004+076, A2 ← 011, A3 ← 037, A4 ← 042,
A7 ← 005) **+ 2 axes anchored by the frozen question's own sub-questions** (A5 ← enrichment
histories, A6 ← ionizing budget) with ≥2 members each and their weaker two-sidedness declared.

Merge tests (why not fewer): A1/A2 — A2's entries accept A1's census while disputing its physics
(011 and 064 presuppose the measured SFRD/UVLF); folding would hide that the census and its
interpretation are separately contested. A3/A4 — A4's dispute survives inside a single calibration
choice (042's disagreement is within one method), while A3's is about the tools themselves. A5 vs
A3/A4 — A5's members assert histories (time-domain), not relations or tools. A6/A7 — sufficiency
vs source attribution; A7 is additionally boundary-ruled by the frozen question (LRD/AGN nature is
not a fourth axis; the entries enter only as budget-attribution bearers). Split tests (why not
more): splitting A3 into scatter-vs-drivers fails — 029/035/038 carry both contents; splitting A6
into production vs escape fails in-corpus — 079 couples them and the escape side alone would have
no second side; splitting A1's existence-of-evolution from pace fails — 056 (evolution exists) is
accepted by both sides, so it anchors, not divides.

**Honest determinism scope:** under a different judgment layer K could shift by ±1 (e.g., folding
A7 into A6, or promoting A3's driver entries). The R3 constraint bounds it from below at 5; the
trace + per-axis arguments make every such move reviewable. Re-running R0/R1/R2/R3/R4 yields the
same result mechanically; re-running J1–J7 yields the same result only for a reader who accepts
the recorded arguments — exactly the AGN pilot's R4 situation, generalized, and said plainly this
time.

## Structural honesty findings (for the applier and contract lanes)

**Ledger-on-disk verification-status defect (disclosed, not fixed — applier lane to repair):**
`step4_v8_applier.py` (ran 2026-08-04 14:11 KST, mid-Step-6) wrote `verification_status: "validated"`
into all 80 entries — a value that is not a contract enum and that ignores the patch's own per-row
`new` values, collapsing Kun's 76 `verified_consistent` / 4 `verified_no_claim` distinction. The
authoritative per-entry verification census lives in the two Kun artifacts pinned above (both carry
76 + 4, zero failures). Byte-diff against the pre-v8 backup (`_tmp_goru_v7_backup/`) confirms v8
touched ONLY `verification_status`, `verification_note`, `binding_note`, and the c41_004/c41_005
evidence-span zone/stance fields; `assertion`, `links`, `tags`, `modality`, `certainty_level`,
`epistemic_type`, `source_bibcodes` are byte-identical — so every content binding below is
unaffected. Per this lane's report-don't-fix discipline the ledger was not edited; the applier
should re-land the patch honoring `new` per row.

- **ESL monoculture:** 75/76 claims carry `emerging_sample_limited`; the one exception is c41_004
  (`actively_debated`). This is what a one-claim-per-paper, single-span-single-source ledger should
  look like (Kun, Step 5) — but it means certainty enums carry almost no debate structure here;
  debate structure lives in modality (`mixed_debated` x5), the two marker tags, and cross-paper
  conflicts. The map's status labels are correspondingly flat, and per the interpretation contract
  a claim counts as **disputed** only where stance-verified sources conflict — which is
  cross-paper, i.e., exactly the clusters named above.
- **c41_004/c41_005 span stance now `qualifies` on-disk** (v8's zone reconciliation + rule-7 cap)
  while the stance matrix carries `supports` for both. The map takes the more conservative
  on-disk reading wherever those two entries appear.
