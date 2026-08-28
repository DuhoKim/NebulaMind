# OCR support check — v4 critical static states

Tool: Tesseract 5.5.2, full-frame `--psm 6` on S01 and S04–S08.

This is supporting evidence only; full-resolution visual review remains authoritative because mathematical subscripts and thin plot labels are lossy under generic full-frame OCR.

## Critical-token recovery

### S01

Recovered the plain-language opening question, the escape-fraction definition (“share of ionizing photons that get out of galaxies”), required-versus-proxy-based comparison, and `model propagation; no new measurement`.

Verdict: PASS.

### S04

Recovered:

- `The closure envelope leaves zero at z = 8.045`
- `Two different crossings`
- `z_c = 8.045`
- `finite-MC 16-84%: 8.030-8.059`
- `z_m = 6.328`
- `not the headline criterion`
- `16th percentile reaches the zero line`
- `lower edge touches Delta = 0`

Verdict: PASS.

### S05

Recovered:

- `Conditional shortfall rises with redshift`
- `z = 7` / `66% with Delta > 0`
- `z = 8` / `83% with Delta > 0`
- `z = 9` / `93% with Delta > 0`
- `conditional model mass, not real-world probability`

Verdict: PASS.

### S06

Recovered:

- `A separate no-tail run moves the crossing earlier`
- `Separate no-tail run`
- `ONE PRIOR FAMILY`
- `remove the JWST-motivated SFRD tail; draws unpaired`
- `z_c = 7.615; finite-MC 16-84%: 7.602-7.631`
- `z_c = 8.045; SFRD tail retained`
- `earlier crossing means closure gets harder`

Generic OCR does not cleanly preserve every rotated inline plot label, but the same values are recovered from the external rail and are clearly readable in full-resolution visual review.

Verdict: PASS.

### S07

Recovered:

- `A dominant omission sits outside this Monte Carlo`
- `Boundary, not inventory`
- `PROPAGATED EXAMPLES`
- `ionizing efficiency; IGM clumping; SFRD priors`
- `DOMINANT OMISSION`
- `do low-z proxy calibrations transport to z > 6?`
- `NOT EXHAUSTIVE`
- `other structural assumptions also remain unpropagated`
- `no survey measurement in this study`

Verdict: PASS.

### S08

Recovered:

- `A conditional crossing, with a clear next measurement`
- `FINDING`
- `closure envelope leaves zero at z_c = 8.045`
- `EVIDENCE`
- `lower Delta edge crosses zero`
- `finite-MC 16-84%: 8.030-8.059`
- `BOUNDARY`
- `frozen low-z anchors; no new measurement`
- `NEXT TEST`
- `measure proxy transport at high redshift`

Verdict: PASS.

## Limit of this check

No encoded MP4 exists in the worker lane, so this OCR result proves only that source-resolution v4 PNGs expose the critical text. Hwao's encoded silent canary still requires OCR/visual review from extracted encoded frames.
