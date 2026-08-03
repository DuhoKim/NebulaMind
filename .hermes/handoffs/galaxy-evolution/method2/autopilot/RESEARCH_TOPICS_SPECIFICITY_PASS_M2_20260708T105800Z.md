# Method2 — research proposals specificity pass: receipt + verdict

Marker: AUTOPILOT_RESEARCH_TOPICS_SPECIFICITY_PASS_20260708T105800Z · Continuation: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Role: Method2 Hwao (verdict) + Goru/Kun (verification). UTC: 2026-07-08T10:58:00Z
Status: **PASS / COMPLETE**

## Files written (overwrote the prior proposal set, per order)
`…/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/`
| file | bytes | sha256(16) |
|---|---|---|
| `research-topics-from-wiki-20260708T090359Z.html` | 18812 | `41be81e62f97043a` |
| `research-topics-from-wiki-20260708T090359Z.md` | 12619 | `866d73df496e60e6` |
| `research-topic-map-20260708T090359Z.json` | 12434 | `e22b9d5ecd89c7ee` |
| `manifest-20260708T090359Z.json` | 852 | `5dbf196dbd9f41cb` |

## Required validation
- **PASS/WARN/FAIL: PASS.**
- **Proposal count: 6** (order asked 5–8).
- **Cards with each required section: 6/6** for `Research question`, `What studies already show`, `What remains unknown`, `Survey/data plan`, `Analysis/test`, `Expected result or decision point`, `Caveats` (all seven; provenance line on all 6).
- **Product claim/cite comments: 0 / 0.**
- **Static safety: PASS** — no `<script>`/`fetch`/XHR/WebSocket/handler/`<form>`/external asset; 7 links, all local, 0 external, 0 broken.
- **Hard-excluded surfaces touched: 0.**
- Named data families tied to measurements: **18** (MUSE, MaNGA, ALMA, JWST, DESI, Chandra, XMM, eROSITA, VLA, LOFAR, MeerKAT, MOSDEF, PHANGS, GAMA, COSMOS, IllustrisTNG, HORIZON-AGN, ADS) — each paired with a specific measurement, labelled proposed data.
- Jargon/IDs: none in headings; evidence IDs appear only in per-proposal provenance lines; no invention (IDs ⊆ known 36).

## Specificity proof (generic → concrete)
**Example 1 — removal vs recycling (Proposal 1).**
- *Before (general aim):* "Measure what fraction of AGN-driven outflowing gas is permanently removed versus recycled, as a function of mass and redshift."
- *After (specific):* prior finding — "quasar outflows remove gas in some high-z systems; massive-galaxy outflows can fall back before ~100 kpc; low-z low-mass winds may be too weak" → unknown — "the escaped-vs-recycled fraction, because no study ties outflow velocity to halo escape velocity across a mass/redshift sample" → measurement — "compare outflow velocity with halo escape velocity per galaxy (MUSE/MaNGA kinematics + ALMA reservoir + JWST high-z + DESI/Mg II circumgalactic gas), bin escaped fraction by mass and z" → decision — "a calibrated escaped-fraction(mass, z) curve and a threshold above which removal dominates recycling."

**Example 2 — radio-mode coupling (Proposal 3).**
- *Before (general aim):* "Establish independent, primary-observation support for jet-driven coupling to galaxy gas."
- *After (specific):* prior finding — "review synthesis + one radio-mode observation + weak-coupling caution; no measured coupling-efficiency distribution" → unknown — "the coupling-efficiency distribution across a radio-selected sample and its environment dependence" → measurement — "coupling efficiency = energy deposited in gas / jet mechanical power, from VLA/LOFAR jet power + Chandra cavity calorimetry + MaNGA jet-ISM line ratios, tested against IllustrisTNG/HORIZON-AGN priors" → decision — "a coupling-efficiency distribution (median + scatter); decide whether radio-mode is generically effective or environment-gated."

## Verdict
Each Method2 proposal now states what the source basis already shows, the exact open unknown, the specific measurement, the named data-to-measurement mapping, the deciding comparison, and a concrete decision point — no longer a general theme. Honest "proposed, not accepted" framing preserved; IDs kept to provenance. Ready for the director's cross-method rollup (6 proposals; all sections present; static PASS; 0/0 bindings). Cross-method final rollup is the director's deliverable.

## Safety ledger
- live-root: 0 · restart: 0 · DB/SQL: 0 · /api/pages / page_versions / publish: 0 · git: 0 · cockpit/global/shared-parent: 0 · cloud/OAuth: 0 · browser: 0 · cron: 0 · P3 binding: 0
