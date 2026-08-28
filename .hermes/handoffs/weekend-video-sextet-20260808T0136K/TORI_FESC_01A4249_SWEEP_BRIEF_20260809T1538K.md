# Tori brief — one decisive exact-hash FESC presentation sweep

- Marker: `TORI_FESC_01A4249_SWEEP_BRIEF_20260809T1538K`
- Coordinator authority: `HWAO_FESC_PRESENTATION_FIX_ORDER.md`
- User continuation authority: `USER_GO_NEXT_AUTO_SEQ_20260809T1530K.md`
- Candidate: `integrator/canaries/fesc-method-overhaul-canary-20260809T1501K/`
- Exact MP4 SHA-256: `01a4249beb2351fa25b2d2863eecb59b98dd68a53ced1dcc484ce6b723f45660`
- Independent Tori write scope: append exactly one labelled section to `reviews/TORI_SIBLING_ROLLOUT.md` and write exact-hash evidence only under `reviews/tori-sibling-evidence/01a4249b/`.

## Why this is a bounded manual recovery, not a duplicate dispatch

Hwao's `watch_fesc2.py` saw the first in-progress encode `d0dd0327…` before a freeze receipt existed and exited fail-closed with code 2. It did not remain alive to see the final frozen `01a4249…` encode. `fesc2.log` records `freeze: ABSENT` and `HELD -- not dispatching Tori`; the `tori-overhaul` pane is independently verified idle with no FESC sweep section. `watch_tori_fesc.py` only waits for a Tori section and does not dispatch. Therefore this is the one intended Tori sweep from Hwao's order.

## First-class charges

1. Independently hash the MP4 and require exact equality with `POST_ENCODE_FREEZE.json`, `build_receipt.json`, and the candidate receipt. Reject any mismatch.
2. Decode the actual H.264/AAC bytes through EOF. Bind all evidence and the appended verdict to exact hash `01a4249…`.
3. Review actual encoded frames across the whole runtime, not only text/spec/self-QA. The candidate's integrator-authored `TORI_FRAME_SWEEP_QA.md`, self-QA, numeric guard, OCR booleans, and icon counts are evidence only, never independent authority.
4. Progress rail: require the active dot, label, and local focus cue to identify one truthful current stage everywhere. There must be no contradictory inter-stage fill, second position, clipping, or collision with caption/citation. Explicitly inspect 5.052 s (MOTIVATION), 118.000 s (SOURCE), and 222.410 s (SCIENCE), then sweep the full runtime.
5. Text/graphics collision: verify `ONE APPARENT MISMATCH · TWO EXPLANATIONS` clears both paired-stroke glyphs at 5.052 s and sweep the entire deck for equivalent pill/badge/title/card/caption collisions.
6. Global geometry: no readable scientific order, crossing, trend, selected sign/value, result-like point/curve/band/axis/legend, or explanation selection anywhere. The eight paired-stroke glyphs must remain separated, equal-height, non-intersecting, and non-ordering.
7. Retention: lane introduction; conditional motivation in both channels before technical content; lane-specific discriminant as the longest/peak move; withheld estimator; design-only controls; `METHOD DESIGN · NO MEASURED VALUE`; discipline/boundary/payoff close.
8. Boundary: re-read `lanes/fesc/STATUS.json` or the current mapped lane status and prove `SOURCE_FREEZE.json` absent. No scientific result is authorized; `video_reportable_now=false`.
9. Audio/sync: independently verify narration/timeline identity, delivered WPM, loudness/true peak, A/V alignment, and a private/local playback through EOF. No publication or copy to shared/public roots.
10. Custody: do not modify the candidate, predecessor, public/shared video roots, renderer source outside evidence, cockpit, frontend, DB, deployment, or Git. Rehash protected MP4s at closure.

## Output contract

Append one timestamped section with:

- exact hash and candidate identity;
- `PASS_METHOD_ONLY_LOCAL_CANARY` or `HOLD`;
- explicit rail and collision findings;
- global geometry and boundary disposition;
- exact media/frame/audio measurements;
- evidence paths and protected-root closure;
- closed-gate statement.

Finish the pane response with exactly one standalone marker:

- `TORI_FESC_01A4249_PASS`
- or `TORI_FESC_01A4249_HOLD`
