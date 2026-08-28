# Two-hour sibling result-candidate staging plan

Status: `PREPARED_ONLY_BUILD_FORBIDDEN`

Authority: `HWAO_TWO_HOUR_SIBLING_ORDER_20260809T1620K.md`  
Authority SHA-256: `8a062877a34d8e99727363cecee8c96b36e4ca2cc51b5fb8558a5e87aafa293f`

Prepared by Yui as sole candidate writer. This directory is planning material under `integrator/`; it is not a candidate, freeze, adjudication, acceptance, or publication packet. No render, narration synthesis, candidate copy, or candidate mutation is authorized by it.

## Current immutable method-only bases

| lane | exact base | MP4 SHA-256 | reportable |
|---|---|---|---|
| fesc | `fesc-method-overhaul-canary-20260809T1501K` | `01a4249beb2351fa25b2d2863eecb59b98dd68a53ced1dcc484ce6b723f45660` | false |
| brightend | `brightend-method-overhaul-canary-20260809T1345K` | `c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8` | false |
| mzr-anchor | `mzr-anchor-method-overhaul-canary-20260809T1406K` | `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584` | false |
| mzr-census | `mzr-census-method-overhaul-canary-20260809T0320K` | `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b` | false |

Each exact base remains untouched. Each authoritative lane root currently lacks `SOURCE_FREEZE.json`; each lane status is stale and names no current candidate. Old worker/snapshot freezes outside `lanes/<lane>/SOURCE_FREEZE.json` are non-authoritative and must not be reused to unlock a candidate.

## Absolute build precondition

Yui may create a new versioned result-bearing candidate for one lane only after Hwao points to one exact authoritative freeze whose bytes are bound to all of:

1. Goru's proposed evidence inventory and freeze;
2. Lana's independent science PASS, including direct primary-source quotation for every anchor or literature claim;
3. Kun's independent adversarial PASS;
4. Tori's independent provenance/custody PASS;
5. exact paths and SHA-256 values for the freeze and all three adjudication packets.

Missing, stale, mismatched, ambiguous, or partially adjudicated evidence means `BUILD_FORBIDDEN`. Goru cannot clear its own proposal; Hwao cannot clear it alone. Provenance or reproducibility alone is not permission. No artifact may be labelled `accepted_by_duho`.

## Accepted renderer hardening that must carry forward

Any future result-mode renderer must start from the hardened FESC renderer behavior, not from the older lane snapshots:

- reject `icon="curve"` and every unknown icon primitive;
- retain `paired_strokes` as separated equal-length horizontal strokes with no slope, order, intersection, or crossing;
- retain the progress rail's single truthful active-stage cue: one bounded breathing focus capsule, dot, and label, with no independent inter-stage fill;
- retain primitive-level badge text fitting and containment;
- keep preview/review scratch outside every candidate.

The current renderer is intentionally method-only and cannot merely have a boolean flipped. Its exact result-mode seams are:

- `Renderer.validate`: currently requires `video_reportable_now is False`; replace only in a new renderer with an authorization validator that independently hashes the authoritative freeze and all three adjudication packets.
- `chrome`: currently hardcodes `METHOD DESIGN · NO MEASURED VALUE`; result mode needs freeze-bound evidence-state copy.
- `funnel`: blank stage counts may be populated only from authorized freeze fields, preserving units and denominators.
- `estimator`: currently hardcodes `VALUE WITHHELD` and `NO SIGN SELECTED`; a result view needs an explicit freeze-bound value/sign/uncertainty representation and must preserve estimator definition.
- `controls`: currently hardcodes `DESIGN ONLY · NO OUTCOMES`; result mode may display only adjudicated control outcomes.
- `boundary`: currently divides `KNOWN NOW / NOT REPORTABLE / NEXT SCIENTIFIC GATE`; result mode needs `SUPPORTED BY THIS FREEZE / NOT SUPPORTED / NEXT GATE`, with exact scope.
- `payoff`: currently asks the question without choosing; result mode may state only Lana's bounded wording.
- `build_receipt`: currently writes `video_reportable_now:false`; a future true value must be derived from verified authorization bytes, never supplied as a free boolean.

## Required new result-mode contract

Before any render, a new spec and renderer must fail closed unless they contain and verify:

- `result_authorization.source_freeze_path` and SHA-256;
- exact Lana, Kun, and Tori packet paths and SHA-256 values;
- `result_authorization.claim_text` byte-for-byte equal to the adjudicated bounded claim;
- each rendered number mapped to an authorized freeze field and its source artifact hash;
- each primary-source/literature statement mapped to a verbatim quotation plus page/line locator and source hash;
- `video_reportable_now:true` only when all bindings pass;
- no forbidden or additional claim text outside the authorization object.

The numeric guard must be extended from source presence to exact authorized-field provenance. QA must test that every displayed/narrated value, sign, denominator, uncertainty, control outcome, and conclusion is contained in the freeze and covered by the adjudicated boundary.

## Future build protocol after clearance only

1. Create a new versioned candidate directory; never copy scratch or mutate a passing base.
2. Reconstruct inputs from the exact base spec/assets plus the cleared freeze and adjudication packets.
3. Apply only the lane delta in the corresponding plan file.
4. If any narration sentence changes, synthesize new managed Alloy audio using subscription-backed seats only and derive the timeline from the new PCM; no old timings may be retained by assumption.
5. Render serially with the hardened result-mode renderer. Preserve failed/superseded attempts outside frozen candidate trees.
6. Run encoded QA, numeric/claim authorization QA, and exact-hash receipts.
7. Tori performs decisive actual-frame review of the new exact hash.
8. Prepare—but do not apply—any public/frontend/upload/cockpit diff. Duho alone may accept exact watched bytes.

## Current gate state

`BUILD_FORBIDDEN`; no lane has cleared all three adjudications. Upload, publication, unlisting, deletion, public/frontend replacement, `paperVideos.ts`, cockpit live-root mutation, DB/SQL, deploy/restart, Git write, browser/account mutation, billing/provider/config change, secrets, cron, and metered fallback remain forbidden. Tailnet private playback is allowed only if later needed; cockpit-copy playback is not.
