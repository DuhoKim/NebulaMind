# P1 receipt — RP-1 numeric-invariant packet

- brief: `HWAO_FABLE_BURN_P1_BRIEF_20260711T010503Z`
- status: **COMPLETE**
- t_ack: 2026-07-11T01:36:41Z (T0_lane)
- t_end: 2026-07-11T02:13Z
- pane id: %184 (`lana-fable-burn-p1:0.0`)
- timeline: finished at T0+~37 min (target was T0+75; hard cap T0+150 / clock stop 03:50:00Z — not approached)

## Artifact table (in `p1-rp1-invariants/`)

| file | bytes | sha256 |
|---|---:|---|
| `P1_ACK.md` | 566 | `c3d072cbddf68964d9749cb6eb767555d9a1d465d61d802d9c11d02bcdeb423b` |
| `INVARIANT_MANIFEST.json` (105 entries) | 51,754 | `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717` |
| `RCA_NUMERIC_DRIFT.md` | 15,941 | `45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096` |
| `INTRODUCTION_LITERATURE_REFERENCE.md` | 14,196 | `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d` |
| `tools/build_manifest.py` (supporting; generated the manifest + cross-cycle check) | 19,178 | `0b81226d406326f263f08b4e3b316d8d946e6d0c48f5677b539209ff5c420122` |
| `FABLE_BURN_P1_DONE_20260711T010503Z` | 0 | (empty marker, created after this receipt) |

## Source snapshot table (originals read-only; copies under `sources-snapshot/`, byte-identical, verified)

Sprint root `S = …/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z`; runs root `R = …/aas-autopilot/runs`. Snapshot taken 01:39:35Z, before the runner's ≈01:46:31Z cycle slot. The 8 brief-listed files first, then 4 custody-chain extras (see deviations):

| original absolute path | sha256 |
|---|---|
| `S/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex` | `63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384` |
| `S/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex` | `a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71` |
| `S/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex` | `55c497ffcc00c56953ab84a2ebb1bc2e375c6d68523958b733cc51439fe09c80` |
| `S/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex` | `38bb60c135eec8c7cecc0b39cfbd55cced65f00cdbbb00922cefa5b87c450d05` |
| `S/candidates/cycle_06_package/CYCLE_06_literature_AUDIT.json` | `8080d24568c089c44d9e3b821068882a1f45d87441ad45573aaf6fd33f5fa4d1` |
| `S/candidates/cycle_07_package/flagship_rp1/aastex/rp1_flagship_polished.tex` | `5fc4fea3fa270472f9d2885b68ac1c97c8292111b60d73f275a41adb101c963b` |
| `S/candidates/cycle_07_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex` | `9e99adc72d1a0b939253a8ae337ea0d620fcccc3dc8e279133a0b177689ac0fb` |
| `S/candidates/cycle_07_package/CYCLE_07_introduction_AUDIT.json` | `51204dd2b1027e3be25b57385a8367cd9f52bd45c0a3a3d06425c4a9e213c034` |
| `S/candidates/cycle_05_package/provenance/REAL_DATA_SOURCE_CUSTODY.json` | `92c0f786c6ba2ded5f7e036cc3c775c43d3f71567223bd28f5d3f1a158d50c6d` |
| `S/candidates/cycle_05_package/CYCLE_05_tables_figures_AUDIT.json` | `79d6dd688fedaf95101fa4ce2f164244726a1c35cf0db8443c8024512a8c0178` |
| `R/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json` (= custody hash) | `668ad7a67290600ff5028ae587d32ef239a09bd8627a480539f37e1927d659df` |
| `R/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p3_simulation_validation/analysis_results.json` (= custody hash) | `6f289f8c68da425eb3d8005e673bf5c5c02cf917eaa2bc6feedd053535de8f52` |

Hash-verified but not copied (1.1 MB CSV; statistics recomputed read-only): `R/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv` = `4ea53af867cccccb2b68b81557ff84fe90ec3f13e0512ffbdc977fa7216996fd` (= custody hash).

## Findings summary (≤10 lines)

1. Drift confirmed exactly as recon stated: flagship `[-1.334,-1.283]` → `[-1.334,-1.282]` at lines 13/57/65/74 in BOTH cycles 6 and 7; both audits fail on that one string.
2. Additional drift recon missed: cycle-7 supplement line 188 table cell `2.830 → 2.831` (audit-invisible today).
3. Additional numeric change recon missed: cycle-6 supplement line 169 replaced artifact-anchored spans `0.005-0.729`/`0.003-0.520` with table-derived `0.001-0.856`/`0.001-0.610` (referent change; audit-invisible).
4. Root cause (custody-verified): prose phases re-derive numerals from the raw artifacts and nearest-round them; the raw CI upper bound is `-1.2821399375` → `-1.282`, and the raw u−r cell is `2.83066` → `2.831`. The only two audit/canon strings that are NOT nearest-roundings of their artifacts are exactly the two that "drift".
5. Cycle 7's four brand-new numerals (4,239/2,731/1,508/26 control-reuse stats) recompute exactly from the custody CSV — the rewriter derives from data, it does not confabulate; recon's "from memory" is amended to "re-derived from artifacts" (RCA §3).
6. Invariant manifest built from clean cycle 5: 105 entries (73 scalars + 32 table rows) across flagship + supplement; 102/105 carry unchanged into cycle 6, 103/105 into cycle 7; every discrepancy is accounted for above (or is benign layout/addition, RCA §2.4).
7. Latent canon inconsistency flagged for adjudication: canon `-1.283`/`2.830` vs artifact-nearest `-1.282`/`2.831` (GATED — canon+audit-list+manifest must change together or not at all).
8. Verbatim-carry rule written (RCA §5) + invariant-safe introduction/literature reference block with GATED external-value slots.

## Deviations from brief / ambiguities resolved

- **Extra read-only sources beyond the 8 listed** (custody receipt, cycle-5 audit, two runs-tree artifact JSONs, one CSV): read to confirm root cause as §1 of the brief asks; each verified against custody SHA-256 before use; four snapshotted into `sources-snapshot/`, CSV hash-logged only. No writes anywhere outside `p1-rp1-invariants/`; no process/runner interaction; `cycle_08_package` (if any) ignored as instructed.
- **Supporting files in write dir** (`tools/`, `sources-snapshot/` extras): kept for reproducibility.
- **First snapshot attempt failed cleanly** (zsh word-splitting; cp copied nothing); retried with an array — snapshot completed 01:39:35Z, before the runner's next slot, hashes verified.
- **Recon hypothesis amended, not contradicted** (finding 5): the brief anticipated "regenerate from memory"; evidence shows regeneration grounded in the artifacts. All safety boundaries §7 respected; no conflicts between disk state and brief encountered.

## Follow-up queue (each item GATED — needs separate Duho approval)

1. GATED — integrator handoff of `INVARIANT_MANIFEST.json` into the sprint's pre-audit flow (RCA §5.6 gate in the cycle loop).
2. GATED — canon adjudication of `-1.283` vs `-1.282` and `2.830` vs `2.831`: pick a rounding convention, then update manuscript + runner audit invariant list + manifest atomically.
3. GATED — extend the runner's audit `numeric_invariants` list beyond the single CI string (at minimum the D2/D3 strings; ideally the manifest).
4. GATED — patch the prose-phase prompt/config (runner-owned) to embed the verbatim-carry rule.
5. GATED — fill literature EXT-1..EXT-4 quantitative slots (needs network/ADS verification, then manifest registration).
6. GATED — value-level verification of the remaining seven topic artifacts against supplement prose (this packet verified custody SHAs for all, full values for m3_p3 + flagship only).

## Coordination-file checks (burn root; `GLOBAL_STOP_20260711T010503Z.md` / `HOLD_5H_20260711T010503Z.md`)

| time (UTC) | result |
|---|---|
| 2026-07-11T01:36:41Z (ACK) | neither present |
| 2026-07-11T01:49:36Z | neither present |
| 2026-07-11T02:07:35Z | neither present |
| 2026-07-11T02:12:21Z (pre-receipt) | neither present |

FABLE_BURN_P1_DONE_20260711T010503Z
