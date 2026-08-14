# Supersession notice: `03_joined_survival_losses_footprint.adql`

Status: **DO NOT EXECUTE / NEVER EXECUTED**

Reason: the draft included aggregate `cos(theta)` and `cos(theta)^2` projections relative to the Longo axis. Even though they were drafted as a footprint-variance diagnostic, they are sky statistics. Duho explicitly forbade any dipole or sky statistic under the parent-row-count authorization.

Custody facts:

- The draft was created locally but was never submitted to TAP or any other query service.
- It returned zero rows because it was never run.
- It exported no identifiers, positions, catalogue rows, images, chirality, handedness, or sky result.
- It is retained only as an append-only record of the caught pre-execution defect.
- The aggregate runner is hardened to reject `SIN`, `COS`, `RADIANS`, and `COSTHETA` tokens.
- The replacement partition query reports counts only. Operational `BRICKID` ranges are disjoint database addends, not a sky-variance analysis.

Footprint variance remains **NOT COUNTED** because Goru did not freeze a non-sky-stat footprint partition or variance definition, and defining one at query time would violate both preregistration custody and Duho's sky-stat prohibition.
