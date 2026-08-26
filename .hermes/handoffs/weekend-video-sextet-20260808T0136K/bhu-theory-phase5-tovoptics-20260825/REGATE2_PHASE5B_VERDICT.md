HOLD_P5_REMAINS_A_SINGLE_SCREEN_MODEL_NOT_THE_AUTHORISED_PATH_TRANSFER

# Phase 5b second re-gate

## Verdict

The new P5 result is numerically reproducible for the model actually coded, and its central correction is valid for a single moving screen: if transmitted and locally emitted radiation share one bulk Doppler factor, that factor multiplies both terms. Under that reduced model the dipole coefficient really does approach 0.2461 and the crossing-normalised bound really does relax from 2.2065e-3 to 5.5166e-3.

That does not pass the phase gate. Both P5 implementations replace the authorised path transfer with a direction-independent scalar optical depth and a source evaluated at the junction. They do not integrate emission from a range of depths, do not carry the depth-dependent emitter velocity/redshift/source temperature, do not carry tau(mu,x), and do not solve the pure-scattering end of A4. Consequently they do not establish a universal saturation floor or a bound over the authorised A1-A6 ranges. The blind double independently reproduces the same reduced screen model, not the missing transfer.

There is also a custody failure in the P1c repair: the receipt says the calculation was reformulated to integrate pbar, but the delivered `p1c_rigorous_sweep.py` still integrates rhobar with the singular 1/w equation. It reproduces the exact self-refutation described in the kickoff, then nevertheless reports 5/5 checks passed.

## Blocking findings

### 1. P5 does not implement the required path transfer

Fact: the authorised P2 deliverable is

`I_obs = I_bg exp(-tau) + integral S exp(-tau') d tau'`

with absorption and emission carried along the path (`PHASE5B_PLASMA_BRIEF.md:35-43`).

Fact: `p5_joint_exclusion.py:52-58` instead evaluates

`D_junction(mu) * [exp(-tau) + (1-exp(-tau)) * v(eta_crossing)^(1/4)]`

using one scalar `tau`, one crossing-local velocity, and one crossing-local source temperature. The script never consumes an exterior A6 profile or P1c output; its only physical input is the Phase-4 orbit table (`p5_joint_exclusion.py:29-35`).

Fact: the independent implementation makes the same reduction. `compute_blind_p5.py:98-113` uses one `Crossing`, one scalar `tau`, and `q = v_crossing^(1/4)`. Its brief explicitly requested a scalar sweep in tau; it did not require the missing depth-resolved transfer (`BRIEF_GPT1_BLIND_P5.md:35-46`). Agreement between the two codes therefore verifies the common screen approximation, not the authorised functional.

Inference: the claimed full-range result is not established. For distributed emission the observed source term has the form schematically

`integral g(s,mu) S_comoving(s,mu) exp[-tau(s,mu)] d tau`,

where the emitter-to-observer frequency factor `g`, source function, and optical-depth accumulation can vary with depth. A single junction factor can be pulled outside only after proving those depth dependencies collapse to a common factor. Neither receipt nor script supplies that proof.

### 2. The 0.2461 saturation floor is a property of the fixed crossing-source model, not a demonstrated physical lower bound

At large scalar tau the coded formula reduces exactly to

`D_junction(mu) * v(eta_crossing(mu))^(1/4)`.

Thus 0.2461 is the dipole of that chosen crossing-local product. An optically thick path instead exposes a tau-of-order-one emitting layer. Its epoch, radius, fluid velocity, gravitational/frequency shift, and source temperature need not equal their junction values. Moving the photosphere through the exterior can weaken or strengthen the angular derivative; without the A6 profile and transfer solution, even the direction of the bias from using the junction value is not bounded.

This directly answers the kickoff's depth and epoch attacks: putting D outside the bracket is correct for a one-zone screen whose transmitted and emitted components share one velocity, but it is not established for emission originating over a range of depths. Holding `Tbar/T_FRW = v^(1/4)` at the crossing creates the reported saturation endpoint. Sampling a range of source epochs is not implemented, so 0.2461 cannot be promoted to a universal physical floor.

### 3. Direction-dependent optical depth and the A4 source range remain absent

Fact: every sky direction in both P5 codes receives the same input `tau`. Neither computes `tau(mu,x)` from a null path. The first-order angular derivative of the optical depth is therefore set to zero by construction, although it can contribute to the off-centre dipole.

Fact: the phase authorises A4 from LTE blackbody through pure scattering and requires the finding to survive all assumption ranges (`PHASE5B_PLASMA_BRIEF.md:21-31`). P5 uses only the energy-ceilinged thermal source. The blind code's `lambda=0` endpoint is a pure absorber/no-emission screen, not a Thomson-scattering transfer solution with angular redistribution (`compute_blind_p5.py:98-113`). It therefore does not close the pure-scattering endpoint.

Consequence: treating opacity as a free scalar from zero to infinity does not make the opacity question moot. It spans scalar attenuation strength while omitting the spatial/profile/source degrees of freedom that the phase was commissioned to carry.

### 4. The delivered P1c artifact contradicts its receipt and passes a false check

Fact: `P1C_RECEIPT.md:20-31` says the singularity was removed by integrating pbar and reports low-w results through tau=2.594.

Fact: the delivered `p1c_rigorous_sweep.py:48-79` still evolves `rhobar` and uses

`rhobarp = (... - wprime*rhobar) / w`.

It contains no pbar-state reformulation. On this gate's environment it printed `n/a` for every low-w bang-bang run, computed `SUP` only from the high-w values, and then found an interior power-law tau of 0.166931 greater than its asserted supremum 0.055259. Despite that direct contradiction it printed:

- `PASS A2 the bracket bounds EVERY junction-consistent closure`
- `RIGOROUS BOUND ... tau <= 5.5259e-02`
- `5/5 checks passed`

The A2 check is hard-coded true at `p1c_rigorous_sweep.py:109-111`; it does not test whether the bracket contains the interior result. The run also emitted an invalid fractional-power warning rather than rejecting the unphysical state fail-closed.

The kickoff candidly withdraws the false bound, but the named executable artifact has not been repaired to match the replacement receipt. The tau=2.594 table is therefore not reproducible from the delivered P1c script.

## Cluster A disposition

- **A1:** Labelling a solver-located endpoint as numerical is acceptable as description, but it does not define or exhaust the authorised closure class. The low-w endpoint remains singular/uncomputed in the delivered artifact.
- **A3:** The old power-law maximisation is moot only if a valid joint transfer covers every closure profile. P5 does not do so, because it discards the A6 profile and replaces it with scalar tau. A3 is therefore not a blocker in its old grid-search form, but its underlying profile dependence has not disappeared.
- **A5:** The trapezoid/trapz shim works here. `python3 p1c_rigorous_sweep.py` executed under Python 3.9.6, NumPy 1.26.4, and SciPy 1.13.1. Execution alone is not closure: the run reproduced the stale singular algorithm and its false-positive checks.
- **A6:** Not discharged. P5 spans values of a scalar tau but does not carry the authorised A6 spatial profiles through direction-dependent optical depth and distributed emission.

## Receipt claims that exceed the scripts

The following statements in `P5_JOINT_RECEIPT.md` are too strong for the delivered artifacts:

1. “one transfer, every opacity” and “over the FULL opacity range” — the code is one constant-tau screen transfer, not the authorised path transfer.
2. “D multiplies the entire beam” — demonstrated only after assigning all emission the junction-frame factor; not derived for emitters at different depths.
3. “opacity ... never removes it, at any opacity” — true inside the reduced LTE screen model, not established across A4-A6.
4. “the exclusion does not depend on resolving the opacity” — scalar opacity need not be resolved inside the reduced model, but the exterior profile/source transfer still must be.
5. `P5_CROSSCHECK.md` calling the result “CONFIRMED” — the double confirms the same reduced functional and cannot validate omitted dimensions.

## Reproduction and failed attacks

Positive evidence retained:

- `python3 p5_joint_exclusion.py` ran successfully and reproduced 4/4 checks, including c1=0.61525 at tau=0, c1=0.24609 at tau=20, and bounds 2.2065e-3 to 5.5166e-3.
- The B1 conversion arithmetic in `P5_CROSSCHECK.md` is consistent: the two implementations agree after converting their radius conventions.
- Monopole normalisation and application of a common Doppler factor to both terms are correct within the single-zone model.
- The p1c compatibility shim fixes the prior NumPy `trapezoid` execution failure.
- The withdrawals in the kickoff and P1c receipt correctly acknowledge that the former thin-exterior and no-photosphere claims are false.

These failed attacks establish that the reported P5 numbers are honest outputs of the code. They do not cure the model-to-brief mismatch.

## Required closure

1. Deliver the pbar-based P1c implementation actually described by `P1C_RECEIPT.md`, with fail-closed state checks and a test that rejects any claimed envelope smaller than an evaluated interior member.
2. Carry an authorised A6 exterior profile into `tau(mu,x)` and into a depth-resolved source integral.
3. Propagate the emitter-to-observer frequency factor and source temperature at each emission depth; then determine or bound the optically thick tau-of-order-one surface rather than assigning it junction values.
4. Cover the A4 pure-scattering endpoint with a scattering transfer calculation, not a zero-emission absorber surrogate.
5. Blind-double that full functional, then report whether a nonzero minimum dipole coefficient survives all authorised profiles and source histories.
