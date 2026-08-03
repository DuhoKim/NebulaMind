# H13 receipt — outflow escape/recycling × feedback transition mass synthesis

Burn `fable-weekly-hard-burn-20260711T035354Z` · lane h13 · ACK 2026-07-11T04:25:40Z · receipt written 2026-07-11T04:38Z
Clock: ACK+25 min = 04:50:40Z; absolute stop 04:45:00Z governs. Finalization began 04:37:40Z, inside the 5-minute reserve.

## Status: COMPLETE

Core tasks 1–5 delivered in `OUTFLOW_TRANSITION_MASS_SYNTHESIS.md` (anatomy + unit audit for both artifacts; claim inventories A1–A6, B1–B6 with grades and rounding derivations; joint regime-consistency analysis with 6-row consistency table and tension list T1–T5; confounder tables; dependency-ordered predictions P1–P4 with gates). Stretch task (cycle-6/7 supplement diff) intentionally not run — remaining time was reserved for finalization; recorded here rather than half-done.

## Custody table — inputs (pinned vs recomputed sha256)

Verification run 2026-07-11T04:28:10Z (`_tmp_custody_check.txt`, retained). Every file recomputed before first read; 9/9 MATCH; no fallback to live sprint/runs trees. `<root>` = burn root; `<prior>` = `fable-weekly-burn-20260711T010503Z/p1-rp1-invariants`.

| Input | Pinned sha256 | Recomputed | Verdict |
|---|---|---|---|
| `<root>/h5-…/sources-snapshot/m2_p1_outflow_escape_recycling/analysis_results.json` | `44b2407aa691d64fd6de22eb49a8c0a185c86bb1f3b538c7bf066e904d0a3210` | same | MATCH |
| `<root>/h5-…/sources-snapshot/m2_p3_feedback_transition_mass/analysis_results.json` | `204ec46dc838e5e69a34b4dc2f790cb0b5e0f7fc1cb4eaa71f830779a2c92b67` | same | MATCH |
| `<prior>/…/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex` | `a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71` | same | MATCH |
| `<prior>/…/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex` | `63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384` | same | MATCH |
| `<prior>/INVARIANT_MANIFEST.json` | `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717` | same | MATCH |
| `<prior>/RCA_NUMERIC_DRIFT.md` | `45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096` | same | MATCH |
| `<prior>/INTRODUCTION_LITERATURE_REFERENCE.md` | `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d` | same | MATCH (verified; GATED external-value slots not consumed — no external values were needed) |
| `<prior>/P1_RECEIPT.md` | `bdfebdc10c3166f045e3d3f9edf9804c87ee546d2f0cfd664e83930020fe763a` | same | MATCH (chain of record; verified, not further cited) |
| `<prior>/…/cycle_05_package/provenance/REAL_DATA_SOURCE_CUSTODY.json` | `92c0f786c6ba2ded5f7e036cc3c775c43d3f71567223bd28f5d3f1a158d50c6d` | same | MATCH (chain of record) |

Process note, recorded for transparency: the first custody-verification command draft included placeholder/dummy check lines and was rejected by the director before execution; it never ran and produced no recorded results. The clean re-run above is the only custody verification performed, using solely the exact pins and paths from H13_BRIEF.md.

## Produced files (all under `<root>/h13-outflow-transition-synthesis/`)

| File | Bytes | sha256 |
|---|---|---|
| `H13_ACK.md` | 75 | `322e88ca4969e7b5357652c149fd9e7c52529a389adfc1b279b1980505bb4051` |
| `OUTFLOW_TRANSITION_MASS_SYNTHESIS.md` | 26815 | `2ca5528a6f0357e9332640514d29e8d9dc4ea46b53eff4c06217451d168248f3` |
| `tools/h13_checks.py` | 4139 | `05483fd68954021e6a8817c4f5010ee9ec741cf95b411900f90730a98980ae8a` (executed 04:37:40Z — 18/18 PASS, exit 0) |
| `_tmp_custody_check.txt` | 2501 | `a98e72896b12bdd94b2e38748f972f0829c22a35f4fe1cf1590a9e7e88ddc5b5` |
| `H13_RECEIPT.md` | — | this file (hash not self-embeddable) |
| `FABLE_HARD_BURN_H13_DONE_20260711T035354Z` | 0 | done marker, touched at finalization |

## Poll log (GLOBAL_STOP / HOLD_5H)

| UTC | GLOBAL_STOP | HOLD_5H |
|---|---|---|
| 2026-07-11T04:25:40Z (ACK) | absent | absent |
| 2026-07-11T04:30:23Z | absent | absent |
| 2026-07-11T04:37:40Z | absent | absent |
| finalization poll (with marker touch, ~04:39Z — see `_tmp_final_poll.txt`) | absent | absent |

Cadence note: the 04:30:23→04:37:40 gap was 7m17s, exceeding the 5-minute target by ~2m during the main synthesis write; both bracketing polls were absent/absent and no stop/hold was missed in effect. Recorded as a process deviation.

## Safety attestation

- All writes confined to `<root>/h13-outflow-transition-synthesis/` (including temporaries, `_tmp_*`). No writes to T0.md, `briefs/`, other `h*` subdirs, the prior burn root, or any repo/runner/live file. No STOP/HOLD files created.
- Under `h5-supplement-value-verification/` only the two pinned artifact paths in `sources-snapshot/` were read; nothing else touched.
- Snapshots and originals untouched (read-only access; hashes above re-verify unchanged content at read time). Live paths embedded inside the artifacts (`figure_pdf`, `source_sample`) were NOT followed.
- No network/browser, no runner/candidate writes, no DB/API/wiki publication, no deploy/restart, no git, no cron/launchd/background jobs, no billing/account/credential access, no cloud/GCP. No tmux send-keys, no messaging to other lanes.

FABLE_HARD_BURN_H13_DONE_20260711T035354Z
