# H9 receipt — adversarial audit of P4's 13 claim/evidence candidates vs sources + wiki schema

status: COMPLETE

- Brief: `<root>/briefs/H9_BRIEF.md`, burn `fable-weekly-hard-burn-20260711T035354Z`
- t_ack: 2026-07-11T04:13:19Z · t_end: 2026-07-11T04:36Z — inside both caps (ACK+35min = 04:48Z; absolute stop 04:45:00Z; final-5-min reserve respected, finalization began 04:35:03Z)
- Headline verdict: **PASS** — 0 BLOCKER, 0 MAJOR, 1 MINOR (integration-side, already gated), 4 NOTE. See `P4_CANDIDATE_SOURCE_SCHEMA_ADVERSARIAL_AUDIT.md`.

## Input custody

| Input | Expected (pinned) | Recomputed at read time | Bytes | Verdict |
|---|---|---|---|---|
| `<prior root>/p4-derived-claims/CLAIM_EVIDENCE_CANDIDATES.md` | `1c8d9a7d28566a19a957cac754a7b8c6c5981a3ad445eb3d3f9daacbd49f8b39` | same | 33940 | PASS |
| `<prior root>/p4-derived-claims/P4_RECEIPT.md` | `27a1efc000a6a5044e5a9a3199e3ef22dfebe9f33d522bafd8e8e98a6909a85b` | same | 6829 | PASS |
| `/Users/duhokim/NebulaMind/NebulaMind/wiki_schema.md` (unpinned, live working tree) | n/a — record at read time | `d1c04e1fcf1e9b412712d07407c42fccffcf12b5a2fc2eced59dba888594b5dd` | 6333 | RECORDED (equals hash P4 recorded → no schema drift between P4 and H9) |
| `<prior root>/P4_CONDITION_PACKET.md` (unpinned) | n/a — record at read time | `738af1cbba1d315b6e85f3aec443be34b7c2bec374316db260b4ec1461a741a5` | — | RECORDED |

Additional read-only files recomputed for check 6 (results in the headline's Check-6 table, all PASS): the two `sources-snapshot/*.tex` snapshots (`63b3920e…9384` / 23917 B, `a4e3d66c…dc71` / 37532 B), their live cycle-5 originals in the runner tree (hash-identical), `p1-rp1-invariants/INVARIANT_MANIFEST.json` (`f4eb857e…6717`, 51754 B), `p1-rp1-invariants/INTRODUCTION_LITERATURE_REFERENCE.md` (`874794a1…713a`, 14196 B), `P4_ACK.md` (`cda7b641…d147`, 410 B), `FABLE_BURN_P4_DONE_20260711T010503Z` (0 B). No pinned-hash mismatch occurred; fail-closed path not triggered.

## Produced files (all inside `<own>` = `<root>/h9-p4-candidate-source-schema-audit/`)

| File | Bytes | sha256 |
|---|---|---|
| `H9_ACK.md` | 74 | `4403bf02c34127305f179551c207aaff8ea06ba070490fae826669650b7d8225` |
| `P4_CANDIDATE_SOURCE_SCHEMA_ADVERSARIAL_AUDIT.md` | 23765 | `85e2eb7955cc67f9c41c6945b8bcad69fcf069bfc8670239c1635a923cf7a11b` |
| `audit-work/verify.py` | 11523 | `f802338b52c016d1b634fa6be9663dead955275007d5419932f9753afe7a0ee4` |
| `audit-work/verify_output.log` | 18592 | `76108262a348b2e977a0be21d4868df9a5a10bd0d789a8b4515d0ee7807d86d3` |
| `audit-work/verify_manifest.py` | 3583 | `b3a54095edc8d8748b054c8bc4d64efe1e0f6e1c61dba599be1c4ce9b131daf6` |
| `audit-work/verify_manifest_output.log` | 5124 | `cf64f117818fbeb840dd94e126322d96f94ed4953caad6bec6d7712da29c471a` |
| `H9_RECEIPT.md` | (this file — not self-hashed) | — |
| `FABLE_HARD_BURN_H9_DONE_20260711T035354Z` | 0 (empty marker) | — |

Note on the two script logs: `verify_output.log` contains one FAIL line and `verify_manifest_output.log` contains three FAIL lines — all four are verifier-side artifacts (a slash-joined id-regex glitch and naive substring counts for `numeric_token` entries), each re-run and PASSED in the corrected pass; documented in the headline (Check 2.4/2.5). Zero packet-side check failures.

## Poll log (stop/hold)

| When (UTC) | `GLOBAL_STOP_20260711T035354Z.md` | `HOLD_5H_20260711T035354Z.md` |
|---|---|---|
| 2026-07-11T04:13:19Z (ACK) | absent | absent |
| 2026-07-11T04:25:39Z (post-read, pre-mechanical) | absent | absent |
| 2026-07-11T04:30:25Z (post-manifest-pass) | absent | absent |
| 2026-07-11T04:35:03Z (pre-receipt final) | absent | absent |

## Safety attestation

- Writes confined to `<own>` (`h9-p4-candidate-source-schema-audit/`): ACK, headline, receipt, done marker, and `audit-work/` scripts+logs. No writes anywhere else on the machine; no STOP/HOLD files created; T0.md, `briefs/`, other `h*` subdirs untouched and unread.
- Prior burn root read-only throughout (verified inputs only; no file created/modified there). Live runner tree touched read-only (two `shasum` recomputes of the cycle-5 tex originals for custody check 6). Repo `wiki_schema.md` read-only.
- Zero network calls; external sources (ADS/arXiv/DOIs) marked UNVERIFIABLE-OFFLINE in the headline, never fetched. No runner/candidate writes, no DB/API/wiki publication, no deploy/restart, no git, no cron/launchd/background jobs, no billing/credentials, no cloud/GCP.

FABLE_HARD_BURN_H9_DONE_20260711T035354Z
