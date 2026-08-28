# V10 FREEZE — tight three-seat confirmation

Status: `FROZEN_V10_AWAITING_TIGHT_THREE_SEAT_EXACT_HASH_CONFIRMATION`

Render authority: **false**. No audio, frames, render, upload, publication, or acceptance is authorized until `preflight_gate_v10.py` exits 0 against three current unconditional verdicts.

## Exact V10 review targets

- Narration: `4324c9b73de038e760c67e80fee70b60656599cf22d95cb1d92167e818f5ef75`
- Storyboard: `dc853f90c3299c5e1c051c0c37a45b6612f5418eaa9bbaad63608fd10ec56ae9`
- Claim ledger: `aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa`
- Graphics specification: `e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e`

## Exact audit controls

- `V10_WPM_AUDIT.json`: `5ca591ca336e991381662d865a9cb8a3434829d097af73427d0c3c32b6457678`
- `V10_SHORTHAND_AUDIT.json`: `ec8a8d2095785b0db936fbdd009da0872a086d9a5acb82c3b02b9bfb2095224c`
- `V10_BUILD_VERIFICATION.json`: `814f2f7374239ac5756f7492d425db93d868826ab427aa04c0aa42a244352667`
- `V10_DELTA_RECEIPT.json`: `e3fab1248e7511cc7cbf1bac56e5b3d5c89d2b9fcbe40cb33640d277976df643`

## Exact V9→V10 delta

Authored changes:

1. `cards[3].heading`
   - old: `One CNS chain puts a low ceiling on neutron-star mass`
   - new: `One cosmological-natural-selection chain puts a low ceiling on neutron-star mass`
2. `cards[3].planned_seconds`: `41` → `48`

Derived consistency change:

3. `estimated_duration_seconds`: `392` → `399`, exactly the new sum of all card durations.

The standalone narration changes only the Card-04 assertion heading. All spoken narration is unchanged from V9. The claim ledger and graphics specification remain byte-identical. Every other card field is unchanged.

## Shorthand result

- Viewer-facing `CNS`: zero occurrences.
- Card 04 shows the full name at card start; no renderer-only exception remains.
- Remaining lexical initialisms: `BHU`, `CW/CCW`; their synchronized first-reveal constraints remain encoded in `V10_SHORTHAND_AUDIT.json`.
- Scientific shorthand constraints remain for `~`, `M☉`, `≳`, `±`, `68.3%`, `95.4%`, and `≠`.

## All-card WPM audit

Contract band: 120–135 WPM. Planned runtime: 399 seconds.

Two transparent planning proxies are published because Lana disclosed that whitespace tokens undercount some spoken compounds:

| Card | Seconds | Whitespace proxy | Spoken-compound proxy |
|---|---:|---:|---:|
| 01 | 35 | 154.29 HIGH | 154.29 HIGH |
| 02 | 36 | 140.00 HIGH | 136.67 HIGH |
| 03 | 39 | 133.85 IN | 135.38 HIGH |
| 04 | 48 | 123.75 IN | 126.25 IN |
| 05 | 51 | 97.65 LOW | 100.00 LOW |
| 06 | 29 | 126.21 IN | 124.14 IN |
| 07 | 29 | 140.69 HIGH | 140.69 HIGH |
| 08 | 35 | 120.00 IN | 121.71 IN |
| 09 | 27 | 131.11 IN | 135.56 HIGH |
| 10 | 36 | 108.33 LOW | 110.00 LOW |
| 11 | 34 | 116.47 LOW | 121.76 IN |

Robust outliers under both proxies:

- High: Cards 01, 02, 07.
- Low: Cards 05, 10.

Tokenizer-sensitive cards:

- Card 03: in-band by whitespace; 135.38 high by spoken-compound proxy.
- Card 09: in-band by whitespace; 135.56 high by spoken-compound proxy.
- Card 11: low by whitespace; 121.76 in-band by spoken-compound proxy.

Nothing outside Card 04 was silently retimed. These findings require explicit seat adjudication. Text proxies do not replace final encoded per-card speech-duration measurement.

## Required tight verdict form

Each of `LANA_CONFIRM_V10.md`, `GORU_CONFIRM_V10.md`, and `KUN_CONFIRM_V10.md` must:

- bind all four exact V10 review-target hashes;
- bind the exact WPM-audit and shorthand-audit hashes;
- provide standalone `VERDICT: PASS` or `VERDICT: PASS_FOR_RENDER`;
- contain these exact disposition lines:

```text
DELTA_DISPOSITION: PASS_EXACT_V9_TO_V10_TWO_REPAIRS
WPM_AUDIT_DISPOSITION: ACCEPT_V10_TIMING_AS_PLANNED_FOR_RENDER
SHORTHAND_AUDIT_DISPOSITION: PASS_NO_CNS_EXCEPTION
```

Any `PASS WITH`, conditional pass, HOLD, or FAIL marker blocks. On three unconditional exact confirmations, authority is limited to local deterministic rendering: no paid generation, upload, publication, or acceptance.
