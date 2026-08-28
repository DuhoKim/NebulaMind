SUPPLY_INVALID_ATTACK1_TBAR_SPACELIKE

# AGATE P12 verdict

## Ruling

P12 falls on Attack 1.

The region integrated by `p6_path_transfer.py` is the Smoller-Temple TOV-inside-the-black-hole region, not an exterior static region in the Tolman-Ehrenfest sense. In the actual p6 integration:

- `exterior()` starts at the shock/junction with `N_s = sqrtN(eta_e)**2`.
- It integrates outward in `rbar` only until the event `N = 1 + EPS_HZ`.
- The right-hand side explicitly guards the run as `N >= 1` and uses the pinned equations with denominators `N - 1`.

So throughout the region p6 uses, up to the terminal horizon offset, `N > 1`. Since Smoller-Temple set `N = 1 - A`, this is `A < 0`.

The pinned source is explicit about the causal character in that case. It writes the Schwarzschild-form metric as

`ds^2 = -B d tbar^2 + A^-1 d rbar^2 + rbar^2 dOmega^2`

and then states that the barred coordinate order is `(xbar^0, xbar^1) = (rbar, tbar)` because the construction is inside the black hole where `A < 0` and `rbar` is the timelike coordinate. Later, in the TOV section, it repeats that the TOV metric inside the black hole has the usual TOV radial dependence, but now `rbar` is timelike and the roles of space and time are interchanged. In the stress-tensor derivation it again identifies the comoving fluid component as lying on `rbar`, and in Lemma 2 it states directly that `xbar^0 = rbar` is timelike and `xbar^1 = tbar` is spacelike because `N > 1`.

Therefore `tbar` is spacelike in the region p12 wants to use. The coordinate-independence of the metric components in `tbar` gives a spacelike Killing vector there, not a timelike static Killing vector. Tolman-Ehrenfest in the form

`T sqrt(-g_tt) = const`

requires a timelike equilibrium vector field. P12 does not have one in the integrated region. The claimed profile `T/T_j = 1/Z` is therefore not supplied by Tolman-Ehrenfest for this model segment.

## Attack 2

`B` is the metric function appearing in Smoller-Temple's equation for the TOV metric, and p6 integrates the correct pinned equation:

`B'/B = -(1/(N - 1)) { N/rbar + kappa rhobar }`

This is the same as Smoller-Temple's equation (4.18). However, because the relevant vector is spacelike in `A < 0`, p12's use of `sqrt(|B|)` as a Tolman factor is not licensed. It is a redshift-like factor used by p6's photon-frequency calculation in the chosen coordinates; it is not the norm of a timelike static Killing vector on which Tolman-Ehrenfest can be based.

So I do not find a missing square root or a wrong differential equation. I find that the equation is being applied in the wrong causal regime.

## Attack 3

Even if Attack 1 did not kill it, local thermal equilibrium would remain an added physical assumption. It is not the same as the invalidated adiabatic carry-along law, because it is a named equilibrium condition tied to a metric symmetry rather than a single-worldline closure. But in this construction the required static timelike symmetry is absent, so the distinction cannot rescue P12.

## Attack 4

The reported inward rise is not evidence that P12 has supplied physical exterior thermodynamics. It is the built-in behavior of taking `1/Z` as `Z -> 0` near the `N -> 1` endpoint. Since the Tolman premise is unavailable in this region, that divergence is an artefact of extending the formal expression to a horizon-adjacent, non-static-inside-black-hole segment.

## Attack 5 reproduction

I ran:

`python3 p12_tolman.py`

It exited 0 with 4/4 self-checks. The run reproduced:

- `Z` from `1.000000` at the junction to `5.576940e-06` near the horizon;
- `T/T_j = 1/Z` from `1.000000` to `1.793098e+05`;
- opposite direction relative to the adiabatic closure;
- finite computed profiles for 5/5 sampled epochs.

I agree the checks are weak by design. They test determinacy, contrast with the old closure, and numerical computability. They do not test the prerequisite causal condition for Tolman-Ehrenfest. That prerequisite fails.

## Bottom line

P12 cannot supply the missing exterior temperature profile via Tolman-Ehrenfest for the region p6 integrates. The integrated region has `rbar` timelike and `tbar` spacelike. There is no timelike static Killing vector of the kind Tolman-Ehrenfest requires, so the proposal is invalid regardless of the clean p12 computation.
