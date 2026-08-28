# Tori encoded-frame sweep — FESC presentation correction

Status: `PASS`

Candidate: `fesc-method-overhaul-canary-20260809T1501K`  
Exact MP4 SHA-256: `01a4249beb2351fa25b2d2863eecb59b98dd68a53ced1dcc484ce6b723f45660`

Evidence:
- Final 2-fps decoded sweep: 473 encoded frames, ten contact sheets, all visually inspected.
- Full-resolution encoded regate: 5.052, 118.000, and 222.410 seconds.
- `FRAME_INDEX.json` SHA-256: `24b59c940447328855784b133fe2d893c23ed3a65a4bd82c27d7f7668880d76a`.
- Exact-time sheet SHA-256: `01f7ffeaee9df1510db6eb25d67126eab83401eedf884cf2424aefb4a53fd29f`.
- Mechanical rail audit over all 473 sampled frames: zero active-stage mismatches and zero off-dot/inter-stage cyan-fill frames.

Defect verdicts:
- Progress rail: `CLOSED`. Each section has exactly one truthful, locally bounded active-stage capsule/dot/label. Nothing fills or travels between stages. MOTIVATION, SOURCE, and SCIENCE agree at the three reported times.
- Introduction collision: `CLOSED`. Pill text remains padded inside the pill and visibly separated from both paired-stroke glyphs.
- Whole-deck collision sweep: `CLOSED`. Every encoded 2-fps frame was inspected; no pill/card/title/citation/caption/graphic collision or clipping survived. The additional discipline title-stack collision found pre-render is also closed.
- Crossing-curve class: `CLOSED_WITHOUT_REGRESSION`. All eight glyph sites remain separated equal-length horizontal paired strokes; no order or intersection is encoded.

Retained-content verdict:
- Lane-specific introduction and both-channel conditional motivation survive.
- Equal-height declared calculation-arm peak and no-result geometry survive.
- Symbolic estimator remains value/sign/result-withheld.
- Method-design banner, controls, tied-hands discipline, science boundary, and payoff close survive.

The preserved rejected attempt `d0dd0327…` is off-candidate in the durable audit workspace; it held only the motion gate after rail-fill removal. No candidate or audit scratch used `/tmp`, and no scratch was placed inside the candidate.

External gates remain closed: no upload, publication, public/shared MP4, frontend/public, `paperVideos.ts`, cockpit, DB, deploy, or Git action.
