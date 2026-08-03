# H15 receipt — cross-topic claim ontology, debate graph, research-program sequencing

Burn `fable-weekly-hard-burn-20260711T035354Z` · lane H15 · ACK 2026-07-11T04:25:40Z · finalized 2026-07-11T04:41Z (inside cap: ACK+25min = 04:50:40Z, absolute stop 04:45:00Z governs).

## Status: COMPLETE

All three task tiers delivered (ontology, debate graph with adjudication notes, sequencing program) plus both stretch items (m3_p3 context node folded in as SIM-C01 with edges; cycle-6/7 prose-drift effects annotated in notes T3/T4). Graph machine-validated: `tools/validate_graph.py` → VALIDATION OK (40 nodes, 19 edges, 4 contradicts, no dangling refs, counts consistent).

## Input custody (pinned vs recomputed sha256 — every input recomputed BEFORE reading; all 15 MATCH)

| input | pinned = recomputed sha256 | bytes | verdict |
|---|---|---|---|
| h5 snapshot `m1_rp2_environment_quenching/analysis_results.json` | `c0421620f67f3c227955affa3f4c1876cb85f8b31874d219f2cd2e35a7f9cec0` | 2155 | OK |
| h5 snapshot `m1_rp3_maintenance_heating/analysis_results.json` | `06291f82c3fbe0f7fe84f7249568882ca4fa44972bcc25a55e367ef1fdcc7e6e` | 1998 | OK |
| h5 snapshot `m2_p1_outflow_escape_recycling/analysis_results.json` | `44b2407aa691d64fd6de22eb49a8c0a185c86bb1f3b538c7bf066e904d0a3210` | 1827 | OK |
| h5 snapshot `m2_p2_radio_jet_environment/analysis_results.json` | `4e1ff701bb5b98af4945d5adad2e543e00005e1ab3907e8fae7d15e70c93e351` | 1957 | OK |
| h5 snapshot `m2_p3_feedback_transition_mass/analysis_results.json` | `204ec46dc838e5e69a34b4dc2f790cb0b5e0f7fc1cb4eaa71f830779a2c92b67` | 2112 | OK |
| h5 snapshot `m3_p1_multiphase_census/analysis_results.json` | `e711563011102657b6d5cab279c1b2ab7ed087dfc734e50932ad4edfe90d0683` | 2375 | OK |
| h5 snapshot `m3_p2_gas_depletion_efficiency/analysis_results.json` | `42965b6f359c23b56098f5f9845561f4a4a2ba81e1e00df09fbae4acf3bcc2d9` | 2101 | OK |
| prior `…/supplementary_denominator_atlas.tex` (cycle-5) | `a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71` | 37532 | OK |
| prior `…/rp1_flagship_polished.tex` (cycle-5) | `63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384` | 23917 | OK |
| prior `INVARIANT_MANIFEST.json` | `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717` | 51754 | OK |
| prior `RCA_NUMERIC_DRIFT.md` | `45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096` | 15941 | OK |
| prior `INTRODUCTION_LITERATURE_REFERENCE.md` | `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d` | 14196 | OK (custody-verified; GATED external-value slots referenced only via P1 queue item 5; no content relied on) |
| prior `P1_RECEIPT.md` (cited in deliverables) | `bdfebdc10c3166f045e3d3f9edf9804c87ee546d2f0cfd664e83930020fe763a` | 7765 | OK |
| prior custody `REAL_DATA_SOURCE_CUSTODY.json` | `92c0f786c6ba2ded5f7e036cc3c775c43d3f71567223bd28f5d3f1a158d50c6d` | 8504 | OK (chain of record; cited via RCA custody rows) |
| prior `m3_p3_simulation_validation/analysis_results.json` (context node) | `6f289f8c68da425eb3d8005e673bf5c5c02cf917eaa2bc6feedd053535de8f52` | 5079 | OK |

Verification command preserved as `tools/verify_inputs.sh`; full OK-per-file output observed 2026-07-11T04:26Z. No mismatch, no absence, no fallback to live sprint/runs trees (snapshots only).

## Produced files (all under `<root>/h15-cross-topic-ontology/`)

| file | bytes | sha256 |
|---|---|---|
| `H15_ACK.md` | 73 | `9ad2d0d1430353ea36a09f75c8e7a830175ae73efff5ff4ebe4627d92e6a4195` |
| `CROSS_TOPIC_CLAIM_ONTOLOGY.md` (headline) | 15943 | `0534872b02935448ff9eee1b2f0fa6f9002cea76cdad63f9a7e3bf6430931764` |
| `CLAIM_GRAPH.json` | 17505 | `5a64bc2d2df3aed27a689fe71bfc6bed11d915e340a0ef5609e2d7664812a098` |
| `tools/verify_inputs.sh` | 378 | `acfafcafc212d441acf6f311ec7a0368d0d027b38fdeccaacf967481bd0c7bf0` |
| `tools/validate_graph.py` | 1029 | `7a0e280d89b10c8add231f1c7d8f66e3c06341b55c4836e2687d706c7c792f67` |
| `H15_RECEIPT.md` | (this file) | (n/a — cannot self-hash) |
| `FABLE_HARD_BURN_H15_DONE_20260711T035354Z` | 0 | (0-byte marker, written immediately after this receipt) |

## Poll log (GLOBAL_STOP / HOLD_5H, both filenames checked each time)

| UTC | GLOBAL_STOP | HOLD_5H |
|---|---|---|
| 2026-07-11T04:25:40Z (ACK) | absent | absent |
| 2026-07-11T04:34:08Z | absent | absent |
| 2026-07-11T04:39:12Z | absent | absent |
| 2026-07-11T04:40:39Z (final, pre-receipt) | absent | absent |

## Safety attestation

- Writes confined to `<root>/h15-cross-topic-ontology/` only (ACK, two deliverables, two tools scripts, this receipt, done marker). No writes to T0.md, `briefs/`, other `h*` subdirs, the prior burn root, repo, runner, or any live file. No STOP/HOLD files created.
- Under `h5-supplement-value-verification/` only `sources-snapshot/<topic>/analysis_results.json` were read (the permitted exception); nothing else under h5 touched. H11–H14 outputs not read.
- All inputs read from snapshots after per-file sha256 recomputation matched the pinned values; snapshots and originals untouched (read-only access).
- No network/browser, no runner/candidate writes, no DB/API/wiki publication, no deploy/restart, no git commands, no cron/launchd/background jobs, no billing/account/credential access, no cloud/GCP. Every proposed runner/network/DB action in the sequencing program is marked GATED for Duho.

FABLE_HARD_BURN_H15_DONE_20260711T035354Z
