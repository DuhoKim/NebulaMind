# Duho note — Galaxy Spin research pointers

Received 2026-08-08 ~01:45 KST, verbatim:

> Galaxy Spin
> - Ganalyzer
> - a study used DESI Legacy Survey 1.2M
> - Spin Asymmetry, A = (cw-ccw) / (cw+ccw)
>     - Dipole axis
>     cosmological parity violation
>     GRB, 1a SN, DE, quasar
>     H0 value?

## Status: RECORDED, NOT ACTED ON

This is research direction for the spin-parity lane's *science*, not a video instruction. It is
filed here so it is not lost, and flagged to Hwao/Lana rather than absorbed into a video by a Yui
seat.

## What is already established in-lane (do not re-derive)

- `A = (N_CW − N_ACW)/(N_CW + N_ACW)` is exactly the lane's frozen statistic
  (`SPIN_PARITY_CONTRACT_V1.md` §2) — Duho's definition matches the contract.
- **Ganalyzer** is Shamir's automated annotation tool; the contract's anchor block already cites
  Shamir 2012 (126,501 SDSS spirals, z<0.3, claimed parity violation, dipole at RA≈132° Dec≈32°).
  Verified against the primary source 2026-08-07.
- The **dipole axis** is specified pre-data in contract §4 (HEALPix Nside=8, ≥30 spirals/cell,
  ≥1000 label-shuffle nulls, direction is a NUISANCE parameter, not a result).
- **DESI Legacy Survey ~1.2M** is a *new* pointer. Shamir's later work (2020–2022) extends to
  ~10⁶ galaxies across SDSS/Pan-STARRS/DESI. This is NOT in the frozen anchor block and would need
  a primary-source check before any use — the anchor block has already been wrong twice
  (Land direction inverted; Longo amplitude 2.5× overstated).

## Open questions this raises — for Lana/Hwao, not for a video

The GRB / SN Ia / dark energy / quasar / H0 cluster is a much larger claim family than this lane's
frozen scope. The contract explicitly forbids phrasing any result as support for the cosmology that
motivated it, and `T3_READING.json` records that the current reading is about **Galaxy Zoo's human
classifiers**, not the sky. Extending toward H0 or parity violation across other probes is a
**new contract**, not an amendment.

**Nothing in this note may enter a weekend video candidate.** The weekend lanes improve the
presentation of results already gated; they do not add scientific claims.
