# The flatness gap, closed — and my first explanation of it was wrong
(2026-08-27. Supersedes the explanation in LAMBDA_TAU_CLOSURE.md, which was already withdrawn
after REGATE3 finding 2.)

## The puzzle

The blind seat's dipole coefficient is essentially FLAT across eight orders of magnitude in its
grey-opacity parameter λ (0.6272 → 0.6153, a 2% drift) while its crossing temperature swings
from 0.08 to 1.51 over the same range. My first explanation — that it held the exterior fixed
across directions — was refuted by the gate: its code builds profiles at three crossing epochs
and finite-differences them, exactly as mine does. So the flatness needed a real explanation.

## The measurement that closes it

Scaling opacity ALONE by a multiplier K, holding profile, source and geometry fixed, and
splitting the crossing factor into its amplitude (value at the centre) and its **shape** (the
ratio across directions, which is what a normalised dipole actually sees):

| K | amplitude at centre | shape R(+1)/R(−1) |
|---|---|---|
| 0.01 | 0.099051 | 0.997726210 |
| 0.1 | 0.176060 | 0.997729299 |
| 1 | 0.311689 | 0.997759674 |
| 10 | 0.531781 | 0.998017645 |
| 100 | 0.742938 | 0.998857603 |

**The amplitude changes by 7.5×; the shape changes by 0.11%.** The crossing factor is very
nearly separable — amplitude(opacity) × shape(epoch) — and a sky-mean-normalised dipole divides
the amplitude out entirely. Hence flatness.

The residual is not zero and it grows with opacity (0.99773 → 0.99886), which is why their
surface drifts by 2% rather than being exactly constant. Order-consistent: 0.11% shape drift
over my four decades against their 2% over eight.

## Why mine is NOT flat, from the same measurement

Their λ is an **opacity-only** knob — the profile behind it is unchanged. My w is not: varying
it changes the opacity, the profile, the depth-redshift AND the source law together. Opacity
alone leaves the epoch-shape almost untouched (0.11%); w moves the shape substantially, and the
dipole follows.

**So there was never a contradiction.** Two knobs, one opacity-only and one that moves
everything, behaving exactly as they should. My coefficient's swing with w and their
coefficient's flatness with λ are the same physics seen through different parameters.

## Status

- Flatness gap: **CLOSED**, by measurement rather than inference.
- My earlier explanation (fixed exterior): **wrong, withdrawn, and now replaced** — I inferred
  it from the shape of their output instead of reading their code, and this closure is what the
  reading should have produced the first time.
- Nothing here bears on the epoch ruling: the null's location remains undetermined by the
  pinned theory, for the separate thermodynamic reason both engines gave.
