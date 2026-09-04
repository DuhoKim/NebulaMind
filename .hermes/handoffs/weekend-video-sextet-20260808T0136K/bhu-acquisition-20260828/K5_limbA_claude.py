#!/usr/bin/env python3
"""K5 limb A, seat "claude": does entry 21's construction FIX the ringdown strain amplitude?

Governing document: K5_LISA_FORECAST_PREREG_20260904.md (frozen V2), §1 limb A.
The prereg's test is mechanical: write the exact derivation fixing the amplitude strictly from
the pinned parameters (M, alpha, distance) with NO new free variables, or conclude it is free.

This script is the seat's whole claim: anything not printed below is not claimed.

DECLARED BEFORE RUNNING:
  * Pinned parameter set: (M, alpha, distance). Nothing else may enter.
  * NO NETWORK, NO FETCH, NO LISA PRODUCT. Limb A is decided before acquisition.
  * The two statements "entry 21 does not compute the excitation factors" and "the construction
    does not fix them" are addressed SEPARATELY below; the prereg names conflating them as the
    error to avoid.
  * Limb A does not reach C1, C2, C3 or C4; they are NOT RUN, not passes.
"""
import sympy as sp

def H(t):
    print(); print("=" * 98); print(t); print("=" * 98)

def P(k, v):
    print(f"{k:<50} {v}")

M, alpha, D = sp.symbols('M alpha D', positive=True)
PINNED = {'M', 'alpha', 'D'}

# ------------------------------------------------------------------ 1. the chain
H("1. The chain from entry 21's static equilibrium to a detector strain")
chain = [
    ("1", "static equilibrium interior solution rho(r), p(r)",
     "DERIVED", "entry 21 Eqs. (4)-(7), L245"),
    ("2", "axial perturbation equation and its scattering potential V(r)",
     "DERIVED", "entry 21 L250 (perturbation ansatz), L269 (potential, positive => stable)"),
    ("3", "quasi-normal-mode FREQUENCIES omega_n (real and imaginary parts)",
     "DERIVED", "entry 21 Table 1 L365; Figures 4-5 L271, L367; band statement L395"),
    ("4", "excitation FACTORS B_n (residues of the Green's function at the QNM poles)",
     "DERIVABLE", "fixed in principle by the SAME potential V(r) as step 2; entry 21 does not compute them (L400)"),
    ("5", "excitation COEFFICIENTS C_n = B_n x (overlap with the initial data of the ringing event)",
     "FREE", "requires the initial data of the perturbing event -- a binary merger (L400 names 'following a binary merger')"),
    ("6", "ringdown strain at the source, h_source ~ sum_n C_n exp(-i omega_n t)",
     "FREE", "inherits the freedom of step 5"),
    ("7", "strain at the detector h = h_source x (source-frame to detector-frame factors) / D",
     "DERIVABLE", "given h_source and a pinned cosmology; the 1/D scaling is standard"),
]
print(f"{'#':<3}{'link':<62}{'status':<12}source")
print("-" * 98)
for n, what, status, src in chain:
    print(f"{n:<3}{what:<62}{status:<12}{src}")

# ------------------------------------------------------------------ 2. the two statements, kept apart
H("2. The two statements the prereg forbids conflating")
print("  STATEMENT 1: 'entry 21 does not compute the excitation factors.'")
print("    TRUE, and the paper says so itself at L400: the excitation factors 'have to be")
print("    calculated. This is an involved task, that this work urges the community to perform.'")
print("    A full-text search of the source finds no computation of them; the only other")
print("    occurrences of 'excitation' are a reference title in the bibliography (L753-754).")
print()
print("  STATEMENT 2: 'the construction does not FIX the amplitude.'")
print("    This does NOT follow from statement 1, and this seat does not rest on statement 1.")
print("    It rests on step 5 of the chain above:")
print("      - the excitation FACTORS B_n are properties of the scattering potential V(r), which")
print("        entry 21 does supply, so they are DERIVABLE from the pinned parameters (M, alpha);")
print("      - but the observable amplitude is C_n = B_n x <initial data>, and the initial data of")
print("        a binary merger is NOT contained in a STATIC EQUILIBRIUM solution. Entry 21's model")
print("        (Eqs. 4-7, L245) describes an equilibrium configuration, not a merger.")
print("    So the freedom is in the SOURCE of the ringing, not in the paper's diligence.")
CONCLUSION_RESTS_ON = "statement 2 (structural), not statement 1 (bibliographic)"
P("this seat's conclusion rests on", CONCLUSION_RESTS_ON)

# ------------------------------------------------------------------ 3. the mechanical attempt
H("3. The mechanical attempt required by the prereg: express h in (M, alpha, D) alone")
print("  Attempting h_detector = f(M, alpha, D) ...")
B_n = sp.Function('B')(M, alpha)          # derivable from V(r)
epsilon = sp.Symbol('epsilon_0')           # the initial perturbation amplitude / radiated fraction
h = B_n * epsilon * M / D
P("h_detector (symbolic, best obtainable)", h)
free_syms = {str(x) for x in h.free_symbols} - {str(sp.Function('B')(M, alpha).func)}
extra = sorted(s for s in free_syms if s not in PINNED)
P("pinned set", sorted(PINNED))
P("symbols appearing that are NOT pinned", extra)
NEW_VARIABLE = extra[0] if extra else None
P("NEW INDEPENDENT VARIABLE introduced", NEW_VARIABLE)
print()
print("  epsilon_0 is the amplitude of the perturbation that rings the object -- equivalently the")
print("  fraction of the mass radiated in the ringdown. It depends on the merger dynamics, which")
print("  entry 21 does not model. It is NOT a function of (M, alpha, D).")
print()
print("  THE DERIVATION CANNOT BE COMPLETED. It halts at exactly one new variable.")
DERIVATION_COMPLETED = False
P("derivation completed without new free variables?", DERIVATION_COMPLETED)

# ------------------------------------------------------------------ 4. the standard escape, ruled on
H("4. The standard escape: calibrate the radiated fraction against numerical relativity")
print("  In general relativity, ringdown amplitudes are routinely set by calibrating the radiated-")
print("  energy fraction against numerical-relativity merger simulations (a few per cent of the")
print("  total mass for comparable-mass binaries).")
print()
print("  Does such a calibration exist for THIS model? NO. It would require merger simulations of")
print("  de Sitter-core regular black holes in this theory. Entry 21 provides a static equilibrium")
print("  and a linear perturbation spectrum about it; it does not simulate a merger, and this seat")
print("  found no such simulation cited in the source.")
print()
print("  Would importing the general-relativity value be a DERIVATION from the construction?")
print("  NO -- it would be an ADDED ASSUMPTION, and a strong one: the radiated fraction depends on")
print("  the merger dynamics and the horizon/surface structure, which is exactly what this model")
print("  changes. Importing it would assume the answer to the question the model exists to raise.")
ESCAPE_IS_ASSUMPTION = True
P("importing the GR-calibrated fraction is an added assumption", ESCAPE_IS_ASSUMPTION)
P("the prereg forbids manufacturing one", "yes (§9); none is manufactured here")

# ------------------------------------------------------------------ 5. controls
H("5. Controls")
c5 = (not DERIVATION_COMPLETED) and (NEW_VARIABLE is not None)
print("C5_AMPLITUDE_PROVENANCE=" + ("PASS" if c5 else "FAIL"))
print("  (operational test per prereg §6: the pipeline halts when a variable outside the pinned")
print("   set (M, alpha, D) is requested. It halted, at epsilon_0. No external amplitude was")
print("   injected to get past it.)")
print()
print("NOT RUN, and NOT passes -- these belong to limbs B and C, which this limb does not reach:")
for c in ["C1_TABLE1_REPRODUCED", "C2_SCHWARZSCHILD_LIMIT", "C3_DETECTOR_CONTROL",
          "C4_DISTINGUISHABILITY_DELETION"]:
    print(f"  {c}=NOT_RUN")

# ------------------------------------------------------------------ 6. class
H("6. Class")
print("LISA_PRODUCT_FETCHED=no")
print("NETWORK_USED=no")
print("DERIVATION_HALTS_AT=" + str(NEW_VARIABLE))
print("EXCITATION_FACTORS_STATUS=DERIVABLE from the pinned potential, not computed by entry 21 (L400)")
print("EXCITATION_COEFFICIENTS_STATUS=FREE, requires merger initial data absent from a static equilibrium")
print("CONCLUSION_RESTS_ON=" + CONCLUSION_RESTS_ON)
print("CLASS=LIMBA_AMPLITUDE_FREE")
print("CONSEQUENCE=limb B (LISA acquisition) and limb C (the ~15 seat-day pipeline) are NOT run;")
print("  K5 files K5_AMPLITUDE_FREE, which prereg §4 gives precedence over classes 1, 2 and 3.")
print("SECOND_INSTANCE=this is the corpus's SECOND 'amplitude irreducibly free' finding, after the")
print("  cutoff amplitude in PROGRAM_A_FREEDOM_MAP_20260902.md -- a pattern, not a coincidence.")
print("K5_LIMBA_CLAUDE_SEAT_COMPLETE")
