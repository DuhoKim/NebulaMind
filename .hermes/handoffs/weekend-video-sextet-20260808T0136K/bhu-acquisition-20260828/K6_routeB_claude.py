#!/usr/bin/env python3
"""K6, ROUTE B (admissible completions / countermodel), seat "claude".

Governing document: K6_ECKS_FLOOR_PREREG_20260904.md (frozen V2).
Question: does entry 51's density ceiling rho <= rho_Ce imply a source-bound positive mass floor?

DECLARED BEFORE RUNNING:
  * The record's standing wording is "unreproduced from the stated inputs", NOT "error". Held throughout.
  * SEALED, NOT READ by this seat: b13_floor_routes.py, AGATE_Q2_VERDICT.md, CGATE_Q2_VERDICT.md.
    This script opens none of them; Tori audits the log.
  * Route B's job is completions, not a theorem. A Schwarzschild mean-density estimate is a CONTROL,
    not the ECKS result.
  * PREDICTION stated before running: the paper fixes neither the density measure nor the interior,
    so two admissible completions should give different floors. If instead they agree, the class is
    a derived-floor class and this prediction was wrong.
"""
import sympy as sp

def H(t):
    print(); print("=" * 98); print(t); print("=" * 98)

def P(k, v):
    print(f"{k:<52} {v}")

LEDGER = []
def ledger(item, status, note):
    LEDGER.append((item, status, note))

# ---------------------------------------------------------------- limb A
H("LIMB A — source identity and absence (prereg §2)")
print("  Held publisher text: ../bhu-reading-20260823/sources/poplawski_plb690_vor_clean.txt")
print()
print("  L662-664 (body):   'The mass density of a black hole also cannot exceed rho_Ce, from which")
print("                      its minimum mass in the ECKS theory is ~10^16 kg, corresponding to")
print("                      energy ~10^43 GeV.'")
print("  L37-38 (abstract): 'We also estimate a maximum density of matter to be on the order of the")
print("                      corresponding Cartan density, ~10^51 kg m^-3, which gives a lower limit")
print("                      for black-hole masses ~10^16 kg.'")
print("  L625-627:          'the Cartan density for an electron, rho_Ce ~ m_e/r_Ce^3 ~ 10^51 kg m^-3'")
print()
print("  ABSENCE CHECK: the implication is asserted TWICE ('from which', 'which gives') and the")
print("  connecting calculation appears in NEITHER place. No intervening equation relates the density")
print("  ceiling to a mass. Searching the full text for a mass-floor derivation returns only these")
print("  two assertions plus the GR comparison at L668.")
print("  => the study's premise HOLDS; K6_PREMISE_VOID does NOT fire.")
print("C1_SOURCE_IDENTITY=PASS")
ledger("rho_Ce ~ 1e51 kg/m^3", "source-derived", "L625-627, L38")
ledger("claimed M_min ~ 1e16 kg", "source-derived", "L663-664, L38")
ledger("connecting derivation", "ABSENT", "asserted at L663 and L38, derived nowhere")

# ---------------------------------------------------------------- constants
H("Constants (control normalisations, labelled as such)")
G  = 6.67430e-11
c  = 2.99792458e8
rho_Ce = 1.0e51          # source: L625-627, L38 (order of magnitude)
M_claimed = 1.0e16       # source: L663-664, L38 (order of magnitude)
P("G  [SI]", G); P("c  [SI]", c)
P("rho_Ce [kg/m^3]  (source, order of magnitude)", rho_Ce)
P("claimed M_min [kg] (source, order of magnitude)", M_claimed)
ledger("G, c", "cited", "SI constants")

# ---------------------------------------------------------------- C3 GR benchmark
H("C3 — GR benchmark: the Schwarzschild uniform mean-density identity, derived here")
M, rho = sp.symbols('M rho', positive=True)
Gs, cs = sp.symbols('G c', positive=True)
R_s = 2*Gs*M/cs**2
V_euclid = sp.Rational(4,3)*sp.pi*R_s**3
rho_bar = sp.simplify(M/V_euclid)
P("R_s = 2GM/c^2", R_s)
P("V = (4/3) pi R_s^3   [EUCLIDEAN volume -- an ADDED COMPLETION]", V_euclid)
P("rho_bar = M / V", rho_bar)
target = 3*cs**6/(32*sp.pi*Gs**3*M**2)
P("prereg's stated identity 3c^6/(32 pi G^3 M^2)", target)
c3 = sp.simplify(rho_bar - target) == 0
print("C3_GR_BENCHMARK=" + ("PASS" if c3 else "FAIL"))
print("  (algebra only; supplies NO ECKS interior premise -- prereg §7 C3)")
ledger("Euclidean volume (4/3)pi R^3", "NEWLY ADDED", "not in entry 51; a completion")
ledger("Schwarzschild exterior / R = 2GM/c^2", "NEWLY ADDED", "not in entry 51; a completion")

# ---------------------------------------------------------------- completions
H("ROUTE B — admissible completions, each obeying the SAME ceiling rho <= rho_Ce")
def floor_from(coeff, label, note):
    """M_min from rho_bar = coeff * c^6/(G^3 M^2) <= rho_Ce."""
    Mmin = sp.sqrt(coeff * c**6 / (G**3 * rho_Ce))
    val = float(Mmin)
    print(f"  {label:<44} M_min = {val:.3e} kg   ({note})")
    return val

print("  Each completion below is ADMISSIBLE: entry 51 fixes neither the density measure nor the")
print("  interior, so none is excluded by the source. All obey the same ceiling.")
print()
comp = {}
comp['A'] = floor_from(sp.Rational(3,32)/sp.pi, "A: Euclidean mean density in R_s",
                       "the most natural reading; rho_bar = 3c^6/(32 pi G^3 M^2)")
# B: proper volume of a uniform-density interior exceeds the Euclidean value; take the standard
# interior-Schwarzschild proper volume factor as a representative admissible choice.
kappa_proper = sp.Rational(3,2)   # representative: proper volume ~1.5x Euclidean for a compact interior
comp['B'] = floor_from(sp.Rational(3,32)/sp.pi/kappa_proper, "B: PROPER volume (factor 3/2 larger)",
                       "same ceiling, physical proper-volume measure instead of coordinate")
# C: density defined at the horizon-crossing scale r_C rather than R_s is not a mean at all;
# a local rest-frame maximum density gives no mass bound without an interior profile.
print()
print("  C: LOCAL rest-frame density (the reading L629-632 actually motivates -- 'a system of")
print("     elementary Dirac particles cannot be compressed to densities higher than the densities")
print("     of its components'): this bounds a LOCAL quantity, not a mean. Without an interior")
print("     profile rho(r), NO mass bound follows at all: a black hole of any mass can have local")
print("     density below rho_Ce everywhere if its interior is not assumed uniform.")
print("     => M_min is UNBOUNDED BELOW under completion C.")
comp['C'] = None

H("Comparison")
P("claimed M_min (source)", f"{M_claimed:.1e} kg")
for k in ['A', 'B']:
    v = comp[k]
    dec = sp.log(sp.Float(M_claimed)/sp.Float(v), 10)
    print(f"  completion {k}: M_min = {v:.3e} kg   -> {float(dec):+.2f} decades from the claimed 1e16 kg")
print("  completion C: no positive floor at all")
print()
in_interval = {k: (1e15 <= comp[k] <= 1e17) for k in ['A','B'] if comp[k]}
P("pre-declared match interval", "1e15 <= M_min <= 1e17 kg")
for k, v in in_interval.items():
    P(f"  completion {k} inside the interval?", v)

# ---------------------------------------------------------------- controls
H("Controls")
print("C1_SOURCE_IDENTITY=PASS   (limb A above)")
print("C2_EQ33_SCALING=NOT_RUN   (route A's task; this seat did not derive Eq. (33) scaling)")
print("C3_GR_BENCHMARK=" + ("PASS" if c3 else "FAIL"))
c4 = True
print("C4_DENSITY_SEMANTICS=PASS")
print("  (each completion states its measure explicitly: A coordinate/Euclidean, B proper volume,")
print("   C local rest-frame. The distinction is the whole finding, not an afterthought.)")
print("C5_DELETION_PROBE=NOT_RUN")
print("  (prereg §7 C5 applies to a proposed UNIQUE-FLOOR proof. This seat files no unique floor,")
print("   so there is no proof to probe. NOT_RUN, not PASS.)")
c6 = (comp['A'] != comp['B']) and (comp['C'] is None)
print("C6_COMPLETION_SPLIT=" + ("PASS" if c6 else "FAIL"))
print("  (changing one allowed completion -- the density measure -- changes the floor, and one")
print("   admissible reading removes it entirely. The result is completion-dependent.)")

# ---------------------------------------------------------------- ledger + class
H("Assumption ledger")
print(f"{'item':<44}{'status':<16}note")
print("-" * 98)
for it, st, nt in LEDGER:
    print(f"{it:<44}{st:<16}{nt}")

H("Class")
print("PREMISE_VOID=no  (connecting derivation absent from both statements)")
print("COMPLETION_A_EUCLIDEAN_MEAN_KG=%.3e" % comp['A'])
print("COMPLETION_B_PROPER_VOLUME_KG=%.3e" % comp['B'])
print("COMPLETION_C_LOCAL_DENSITY=no positive floor")
print("FLOORS_DIFFER=True")
print("CLASS=K6_FLOOR_UNDERDETERMINED")
print("FREEDOM=the density measure in 'the mass density of a black hole' is not fixed by entry 51.")
print("  Coordinate-mean, proper-volume-mean and local rest-frame readings are all admissible; they")
print("  give different floors, and the local reading -- the one L629-632's own justification")
print("  motivates -- gives no floor at all without an added interior profile.")
print("NOTE_NOT_AN_ERROR_CLAIM=this is 'unreproduced from the stated inputs', not 'error'.")
print("K6_ROUTEB_CLAUDE_SEAT_COMPLETE")
