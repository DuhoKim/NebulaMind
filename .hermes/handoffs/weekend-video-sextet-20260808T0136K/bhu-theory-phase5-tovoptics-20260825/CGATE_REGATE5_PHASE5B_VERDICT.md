HOLD_HAWKING_DEGENERACY_OVERCLAIM

# CGATE REGATE5 Phase 5b Verdict

## Ruling

HOLD. The REGATE4 repairs reproduce, and the reduced optical claim set is mostly in the right
shape, but the new Hawking closure overclaims its load-bearing argument. The p9 calculation
shows an exact factor of two between the naive Schwarzschild Hawking temperature of the
critical-density Hubble mass and the Gibbons-Hawking temperature associated with H0. A factor
of two is not a degeneracy in the discriminating-measurement sense. If both quantities were
well-defined observables and were measurable with unlimited precision, they would be
distinguishable.

That does not reopen Hawking radiation as a usable route. The stronger objections in p9 still
stand: the audited Smoller-Temple model does not supply the horizon thermodynamics being
computed, its horizon is white-hole oriented in the cited construction, T0 is an assigned input
rather than an output, the naive thermal scale is about 1e-30 K, and the Wien wavelength is
larger than the observable region. But the receipt and closed-routes register make the exact
factor-of-two comparison do more work than it can bear. They need to say "same H-scale/order
and not a distinctive prediction once the missing thermodynamics are admitted", not "no
horizon-temperature measurement can discriminate" on the basis of an exact half.

## Reproduction

Executed from this directory with the requested environment:

| artifact | observed exit | gate reading |
|---|---:|---|
| `p1c_rigorous_sweep.py` | 0 | repaired high-w endpoint reproduces; 10/10 |
| `p6_path_transfer.py` | 0 | nan defect repaired; stale P6 table is disclosed in receipt |
| `p7_signed_sweep.py` | 0 | closure-conditional root reproduces at w = 0.0407786 |
| `p8_thick_limit.py` | 1 | genuine negative/not-nested check, not a script defect |
| `p9_hawking.py` | 0 | arithmetic reproduces; interpretation overclaims |
| `p10_flatness_redo.py` | 1 | expected anchor mismatch from f=1e-3 vs f=1e-4; negative result is honest |
| `p11_claim1_boost.py` | 0 | boost-threshold calculation reproduces; 8/8 |

The two non-zero exits are acceptable as negative findings. p8 exits 1 because its resolved
K=10 row is not nested with the seat null under the script's own 2% test. p10 exits 1 because
the c1 anchors quoted by the prior gate came from f=1e-4 while the redo brief asked for
x/R=1e-3; the discrepancy is disclosed and does not weaken the Claim 5 withdrawal.

## Claim Adjudication

Claim 1: PASS in the narrowed two-part form. The causal event-horizon statement is
definition-level and separate from redshift suppression. For the redshift calculation, p11's
local orthonormal Doppler bound is legitimate as an upper bound on emitter velocity effects:
with comoving Z ~ sqrt(N-1), the bolometric factor behaves as `(D_max Z)^4`, and the sharp
condition is `gam^2 (N-1) -> 0`, equivalently `gam = o((N-1)^(-1/2))`. Bounded boost is a
clean sufficient public qualifier. Singular emissivity remains uncovered and must stay named.

Claim 2: PASS in the carried comoving-fluid scope. I found no reason to disturb the invariant
optical-depth cancellation. It depends on the absorber being the pinned comoving fluid and on
monotone rbar over the segment; it is not a general non-comoving-absorber statement.

Claim 3: CARRIED PASS. Nothing in this re-gate attacks `beta_rel = -1/sqrt(N)`.

Claim 4: CONDITIONAL/LOW-VALUE PASS only in the restated form. "The two tested closures each
contain a cancellation, at different locations" is true and not vacuous, because it records two
specific source-map experiments and their roots. It is also not a model finding. Do not promote
it beyond a closure-conditional receipt sentence.

Claim 5: WITHDRAWN remains correct. p10 confirms the relevant small residual and signed c1 are
not flat in the sense previously claimed. The f=1e-3/f=1e-4 documentation slip is harmless to
the ruling.

## Repair Checks

p1c: repaired. Terminating at `N=1+eps` is a valid endpoint-limit repair; the high-w tau
converges to 0.036958 and is cross-confirmed by p6's independent integrator.

p6: repaired with disclosure. All reported dipole rows now have finite tau. The earliest
eta-grid failure remains outside the claimed repair and is stated in-run.

p7: repaired. It inherits p6's change and still prints the conditionality block. The root did
not move.

p8: repaired but conservative. The script no longer reports bracket-truncation nans as absent
roots and no longer cites under-resolved high-K rows. The floor-based K_MAX = 18.42 rule may
discard some recoverable information: K=100 could likely be probed with an adaptive bracket
that avoids unresolved low-w evaluations. That is over-conservative, not a false positive. The
surviving p8 claim should remain scoped to the resolved rows; it does not settle the true
asymptotic thick limit.

Stale numbers: the important stale P6 headline is now caught and explicitly withdrawn inside
`P6_RECEIPT.md`. `FLATNESS_GAP_CLOSED.md` remains a withdrawn stale document and should not be
quoted as current. I did not find another live receipt that silently reasserts the withdrawn
P6 1-in-1107/2832 headline as current.

## Required Repair

Repair p9 and `BHU_CLOSED_ROUTES.md` by demoting the exact factor-of-two point. The defensible
statement is that the naive Schwarzschild Hawking calculation is not a distinctive,
source-pinned BHU prediction and is observationally unusable; it is not that an exact factor of
two is itself a no-discrimination degeneracy for an ideal horizon thermometer.

After that repair, I would expect this reduced Phase 5b to pass in the limited sense described
in the kickoff: not model exclusion, not model silence, but an underdetermination finding for
optical tests plus a properly scoped closure of the Hawking route.
