SUPPLY_INVALID_ATTACK1_NO_TIMELIKE_KILLING

# CGATE P12 verdict

## Ruling

P12 falls on ATTACK 1.

The Tolman-Ehrenfest relation needs a timelike Killing vector for a static equilibrium state. The region used by `p12_tolman.py` is the same `exterior()` region integrated by `p6_path_transfer.py`: from the shock/junction outward in `rbar` until the terminal event `N = 1 + EPS_HZ`, with `EPS_HZ = 1e-9`. Since `A = 1 - N`, the entire numerical interval has `N > 1` and therefore `A < 0`.

In that `A < 0` region, the pinned Smoller-Temple source is explicit: `rbar` is the timelike coordinate and `tbar` is spacelike. It says the TOV metric is called TOV because its components depend only on `rbar`, "but now rbar is timelike"; it states again that "rbar is the timelike coordinate" when `A < 0`; and in the shock-matching section it states directly that `x^0 = rbar` is timelike and `x^1 = tbar` is spacelike because `N > 1`.

Thus the only coordinate-independent Killing vector supplied by the TOV ansatz in the radial-time sector, `partial_tbar`, is spacelike in the domain being integrated. The timelike direction is `partial_rbar`, but the metric functions and fluid variables depend on `rbar`, so it is not a Killing direction. The spherical Killing fields are not a substitute for a static timelike Killing vector. This is not a static exterior in the Tolman-Ehrenfest sense; it is a time-dependent interior solution written with the timelike coordinate `rbar`.

Therefore `T sqrt(-g_tt) = const` cannot be used to supply the exterior temperature profile in the P6/P12 integration domain. The fact that `B` is carried by the field equations does not make the Tolman-Ehrenfest equilibrium relation applicable there.

## Source and implementation checks

- `p6_path_transfer.py` integrates state `[pbar, N, lnB]` and stops at `N = 1 + EPS_HZ`, not outside the horizon. Its own comments identify the calculation as the `A < 0` interior.
- Smoller-Temple equation (4.1) gives `ds^2 = -B dtbar^2 + A^-1 drbar^2 + rbar^2 dOmega^2`, with `A = 1 - 2M/rbar`.
- Smoller-Temple then sets the inside-black-hole condition as `A < 0`.
- With `N = 1 - A`, the pinned equations used by P6 are exactly the `N > 1` form, including `B'/B = -(1/(N-1))(N/rbar + kappa rhobar)`.
- The source explicitly records the causal character for this same `N > 1` case: `x^0 = rbar` timelike, `x^1 = tbar` spacelike.

## Attack dispositions

ATTACK 1: kills P12. `tbar` is spacelike throughout the P6/P12 integration region, while `rbar` is timelike and not a Killing coordinate. No timelike static Killing vector is available for Tolman-Ehrenfest.

ATTACK 2: not load-bearing after ATTACK 1. `B` is the metric coefficient in `g_tbar tbar = -B` and P6 integrates the pinned `B'/B` equation with `Z = sqrt(|B|/|B_j|)`. But because `tbar` is spacelike here, `-g_tbar tbar` is not the norm of a timelike Killing vector. The Tolman exponent may be algebraically the familiar inverse square root, but it is being applied to the wrong causal object.

ATTACK 3: also adverse. Even if ATTACK 1 did not kill it, local thermal equilibrium would still be an added physical model for the pre-shock exterior medium, not a consequence of the published Smoller-Temple mechanical equation of state.

ATTACK 4: adverse as a diagnostic. The reported inward rise is the constructed `1/Z` blow-up as the integration approaches `N -> 1`; without a valid timelike Killing norm, that divergence has no Tolman-Ehrenfest temperature interpretation.

ATTACK 5: reproduced, but weak. I ran `python3 p12_tolman.py`; it exited 0 and reported `SELF-CHECKS: 4/4 passed`, with `Z` ending at `5.576940e-06` and `T/T_j = 1/Z` ending at `1.793098e+05`. These checks establish only that the script deterministically computes a profile different from the invalidated adiabatic closure. They do not test the causal prerequisite that fails above.

## Final

Tolman-Ehrenfest does not legitimately supply the missing exterior spatial temperature profile for this lane. P12 is invalid.
