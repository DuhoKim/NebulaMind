#!/usr/bin/env python3
"""K5 Limb A blind-seat report for the codex seat."""

PINNED = frozenset({"M", "alpha", "distance"})


def require_pinned(name: str) -> None:
    """Physically halt the amplitude path when an unpinned input is requested."""
    if name not in PINNED:
        raise RuntimeError(f"AMPLITUDE_PIPELINE_HALTED: unpinned input requested: {name}")


REPORT_PREFIX = """LIMBA_AMPLITUDE_FREE
QUESTION: Does entry 21's construction fix ringdown strain amplitude from (M, alpha, distance) alone?

SOURCE BASIS:
- Entry 21 L245 identifies a linear perturbation analysis about the static equilibrium of Eqs. (4)-(7).
- Entry 21 L250 gives the homogeneous Regge-Wheeler-type equation for axial modes, Eq. (27).
- Entry 21 L269 gives the scattering potential, Eq. (28), determined by the static background.
- Entry 21 L365 reports the quasi-normal-mode frequencies in Table 1.
- Entry 21 L395 reports the fundamental-frequency band; this is spectral information, not amplitude information.
- Entry 21 L400 says excitation factors following a binary merger still have to be calculated.

CHAIN TO OBSERVABLE STRAIN:
- DERIVED: static equilibrium metric and matter profile. Entry 21 supplies Eqs. (4)-(7), identified at L245; (M, alpha) select the background within the construction.
- DERIVED: axial linear wave operator and scattering potential. Entry 21 supplies Eqs. (27)-(29) at L250 and L269.
- DERIVED: complex quasi-normal frequencies and hence oscillation and damping scales. Entry 21 supplies its calculation and Table 1 at L365.
- FREE: merger perturbation/source or equivalent initial data. The static construction supplies no binary-merger mass ratio, spins, orbit, perturbation history, or initial master-field data.
- FREE: excitation coefficient C_n for each mode. It is a functional of the merger source/initial data and of the chosen mode-normalisation convention; the physical product C_n phi_n is not fixed by the static background.
- FREE: source ringdown amplitude in h_source(t) = sum_n C_n phi_n exp(-i omega_n t). Frequencies omega_n do not determine coefficients C_n.
- DERIVABLE CONDITIONALLY: propagation to the detector scales an already-fixed source waveform by the distance and applies detector response. Distance cannot create the missing source normalisation; response would additionally require observational geometry not present in the pinned set.

DERIVATION ATTEMPT:
Let L[M, alpha] phi_n = 0 denote the homogeneous mode equation supplied by entry 21. If phi_n is a solution, lambda*phi_n is also a solution for every nonzero constant lambda. Boundary conditions select omega_n but do not select lambda. A physical merger waveform requires either an inhomogeneous source L psi = S_merger or initial data for psi and its time derivative. Projecting those data onto the modes supplies C_n. Neither S_merger nor those initial data are functions fixed by (M, alpha, distance) in the static construction. The first required independent variable is C_n, equivalently the merger source/initial perturbation data on which C_n depends. The attempted derivation therefore stops before any strain normalisation is assigned.

NON-CONFLATION:
- Statement about computation: entry 21 explicitly says at L400 that the excitation factors have to be calculated; the paper does not compute them.
- Statement about determination: independently, homogeneity gives a scaling freedom, and the pinned static parameters provide neither a merger source nor initial perturbation data. This proves that the construction does not fix the physical normalisation.
- CONCLUSION BASIS: the verdict rests on the second statement, not merely on the paper's omission stated in the first.

STANDARD ESCAPE:
Entry 21 supplies no numerical-relativity merger calibration for this de Sitter-core model; L400 instead identifies calculation of its post-merger excitation factors as outstanding. A radiated-energy fraction calibrated from ordinary general-relativistic binary-merger simulations would introduce merger/calibration information outside (M, alpha, distance). It would be an added assumption, not a derivation from this construction.

MECHANICAL RESULT:
An exact amplitude formula using only (M, alpha, distance) cannot be completed. The residual freedom is the merger-dependent mode excitation C_n, or equivalently the source/initial perturbation data. No strain, efficiency, or normalisation is manufactured.
"""

REPORT_SUFFIX = """C5_AMPLITUDE_PROVENANCE=PASS
C1_TABLE1_REPRODUCED=NOT RUN
C2_SCHWARZSCHILD_LIMIT=NOT RUN
C3_DETECTOR_CONTROL=NOT RUN
C4_DISTINGUISHABILITY_DELETION=NOT RUN
FINAL: LIMBA_AMPLITUDE_FREE
"""


def main() -> None:
    print(REPORT_PREFIX, end="")
    try:
        require_pinned("C_n")
    except RuntimeError as exc:
        print(str(exc))
    else:
        raise AssertionError("C5 failed to halt on an unpinned amplitude input")
    print(REPORT_SUFFIX, end="")


if __name__ == "__main__":
    main()
