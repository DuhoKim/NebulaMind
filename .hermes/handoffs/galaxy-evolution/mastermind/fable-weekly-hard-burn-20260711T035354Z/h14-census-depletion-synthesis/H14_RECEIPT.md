# H14 receipt — census + depletion deep synthesis

Burn `fable-weekly-hard-burn-20260711T035354Z` · lane H14 · ACK 2026-07-11T04:25:40Z · finalized 2026-07-11T04:36Z (inside the 04:45Z absolute stop; receipt written in the reserved final window).

## Status: COMPLETE

All five task items delivered in priority order in `MULTIPHASE_CENSUS_DEPLETION_SYNTHESIS.md`: (1) full artifact anatomy + unit audit for both artifacts (all stored fractions/SEs/ratio recomputed and matched); (2) claim inventories for m3_p1 and m3_p2 across supplement + flagship with manifest IDs and A/B/C grades (no X-grade claims found; all grade-B nearest-rounding derivations shown per RCA convention); (3) joint synthesis with 8-row consistency table, degeneracy-budget arithmetic (10^0.6586 = 4.556×), and tension list (no numeric tension; one naming tension T1); (4) confounders per topic, each marked addressable-now vs GATED; (5) dependency-ordered falsifiable predictions P0→P3, all runner/network/DB actions marked GATED. Stretch item (cycle-6/7 diff) not attempted — clock.

## Custody table (pinned vs recomputed sha256 — every input used)

| input | pinned (brief) | recomputed | verdict |
|---|---|---|---|
| h5…/m3_p1_multiphase_census/analysis_results.json | e711563011102657b6d5cab279c1b2ab7ed087dfc734e50932ad4edfe90d0683 | same | MATCH (verified before read) |
| h5…/m3_p2_gas_depletion_efficiency/analysis_results.json | 42965b6f359c23b56098f5f9845561f4a4a2ba81e1e00df09fbae4acf3bcc2d9 | same | MATCH (verified before read) |
| prior…/supplementary_denominator_atlas.tex | a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71 | same | MATCH (verified before read) |
| prior…/rp1_flagship_polished.tex | 63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384 | same | MATCH (verified before read) |
| prior/INVARIANT_MANIFEST.json | f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717 | same | MATCH (verified before read) |
| prior/RCA_NUMERIC_DRIFT.md | 45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096 | same | MATCH (verified before read) |
| prior/INTRODUCTION_LITERATURE_REFERENCE.md | 874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d | same | MATCH (verified; not needed by the synthesis — no external-value slots were used; GATED status respected) |
| prior/P1_RECEIPT.md | bdfebdc10c3166f045e3d3f9edf9804c87ee546d2f0cfd664e83930020fe763a | same | MATCH (verified; cited only as pointer for stretch-item hashes) |
| prior…/provenance/REAL_DATA_SOURCE_CUSTODY.json | 92c0f786c6ba2ded5f7e036cc3c775c43d3f71567223bd28f5d3f1a158d50c6d | same | MATCH (verified; chain of record) |

All nine hashes recomputed with `shasum -a 256` at 2026-07-11T04:26Z, before any input was read. No mismatches; no fallback to live sprint/runs trees (the `source_sample`/`figure_pdf` paths inside the artifacts point at the live runs tree and were treated as opaque strings, never opened).

## Produced files (all inside `<root>/h14-census-depletion-synthesis/`)

| file | bytes | sha256 |
|---|---|---|
| H14_ACK.md | 73 | c1d28d8cd9b8a8c546d385c0d08ca9b49f44671731e3e05be7d73b8afb836f5a |
| tools/joint_crosscheck.py | 4985 | ab5d222f4b43435d6662d61d0b58e89fdd43b4eabca8c0b8d5b86257c41c4654 |
| MULTIPHASE_CENSUS_DEPLETION_SYNTHESIS.md | 23333 | 756cfcf35c53c4d15d8cfca5710e876878cef0904c7e4b85a380ce8015f9531d |
| H14_RECEIPT.md | (this file — self-hash not representable) | — |
| FABLE_HARD_BURN_H14_DONE_20260711T035354Z | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 (empty-file sha256) |

## Poll log (GLOBAL_STOP / HOLD_5H)

| UTC | GLOBAL_STOP_20260711T035354Z.md | HOLD_5H_20260711T035354Z.md |
|---|---|---|
| 2026-07-11T04:25:40Z (ACK) | absent | absent |
| 2026-07-11T04:31:25Z (between anatomy and synthesis) | absent | absent |
| 2026-07-11T04:36:14Z (finalize) | absent | absent |

## Safety attestation

- Writes confined to `<root>/h14-census-depletion-synthesis/` (5 files listed above; plus the `tools/` subdirectory). Nothing written anywhere else; no STOP/HOLD files created; T0.md, briefs/, other h* subdirs, prior burn root, repo/runner/live files untouched.
- Under `h5-supplement-value-verification/` only the two files inside `sources-snapshot/` named in the brief were read (after hash verification); nothing else under h5 was accessed.
- All snapshot and original input files untouched (read-only access; hashes above prove content identity).
- No banned action: no network/browser, no runner/candidate writes, no DB/API/wiki publication, no deploy/restart, no git commands, no cron/launchd/background jobs, no billing/account/credential access, no cloud/GCP. Only local reads, sha256 recomputation, one offline python3 helper run, and writes inside the own subdir.
- No live-tree fallback: snapshot inputs only, per directive.

FABLE_HARD_BURN_H14_DONE_20260711T035354Z
