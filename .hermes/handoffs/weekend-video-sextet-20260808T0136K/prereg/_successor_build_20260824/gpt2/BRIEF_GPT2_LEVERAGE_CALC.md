# GPT2 BRIEF — independent leverage/selection calculator (blind double)

You are seat gpt2 in Hwao's successor-build lane. You are the second, independent implementation
of a calculation another seat has already implemented. You must work from THIS SPEC ONLY.

**FORBIDDEN: do not open, read, list, or search `_successor_instrument_20260823/` or any file
outside your own directory except this brief.** The point of your existence is that your numbers
come from the spec, not from the other implementation. If your numbers later disagree with the
other seat's, that disagreement is the product — do not try to find their code to reconcile.

## Spec

Axis: unit vector n̂ at ICRS (α, δ) = (217.0°, 32.0°).

For a sky position (ra, dec) in degrees, its unit vector is
u = (cos δ cos α, cos δ sin α, sin δ) with α=ra, δ=dec in radians; cosθ = u · n̂.

Inputs (your script's interface): arrays `ra_deg`, `dec_deg`, `n_gal` (galaxy count at each
position; positions represent brick centres).

Quantities, all count-weighted over galaxies (a brick with n_gal galaxies contributes n_gal
copies of its cosθ):
- `mean_c` = weighted mean of cosθ; `var_c` = weighted variance (population form, divide by
  total N, not N−1).
- `leverage` = N_total * var_c.
- `N_eq` = 3 * leverage  (full-sphere-equivalent count; requirement: N_eq ≥ 100,000).

Selection rule POLAR(q): sort bricks by |cosθ| DESCENDING; accept bricks in that order,
accumulating galaxies, until accepted galaxies ≥ q * N_total; report for the accepted set:
N_accept, var_c(accepted), leverage(accepted), N_eq(accepted).

## Fixtures (synthetic; generate with a fixed seed, numpy allowed)

1. 200,000 points uniform on the full sphere (n_gal=1 each): var_c must approach 1/3
   (report the value; tolerance ±0.01).
2. Uniform on the sphere restricted to |cosθ| > 0.8 about n̂: var_c analytic =
   (1 + 0.8 + 0.64)/3 = 0.813333…; report measured vs analytic.
3. Uniform restricted to |cosθ| < 0.2: var_c analytic = 0.2²/3 = 0.013333…; report measured
   vs analytic.
4. POLAR(0.25) applied to fixture 1 must select points with high |cosθ| and its var_c must
   exceed 0.75 (report the value).

## Deliverables (write ONLY inside `gpt2/`)

1. `calc_leverage.py` — the implementation, pure Python + numpy, deterministic (fixed seed).
2. `fixture_results.txt` — produced by RUNNING the script (`python3 calc_leverage.py` prints
   the fixture table); paste nothing by hand.
3. `DONE_GPT2.md` — receipt: the exact command run, `shasum -a 256 calc_leverage.py
   fixture_results.txt` (one file per line), and one paragraph stating any spec ambiguity you
   had to resolve and how. No claims of the form "matches the other implementation" — you have
   never seen it.

## Hard boundaries

- Write only inside `gpt2/`. Temp files: `gpt2/_tmp_*`. No network access needed or allowed.
- No API keys. Do not touch `/Users/duhokim/NebulaMindData/`.
- Last file written = `DONE_GPT2.md` (completion marker).
