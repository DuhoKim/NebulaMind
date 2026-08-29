#!/usr/bin/env python3
"""B13 -- trying to FIND Poplawski's 1e16 kg, not merely to fail to reproduce it.

The two gate seats split on whether the floor is an arithmetic error (AGATE) or stacked
order-of-magnitude estimates that must not be called one (CGATE). Both inverted the SAME route --
Schwarzschild mean density -- and got 2.7e14 kg. One failed route is weak evidence: the author may
simply have used a different one. So this file tries every route the paper's own quantities admit.

NEW INPUT, which neither seat used: the paper DEFINES the Cartan radius, eq. (33),
    m / r_C^3  ~  (G/c^4) (hbar / r_C^3)^2     =>     r_C = [ G hbar^2 / (c^4 m) ]^(1/3)
so rho_Ce does not have to be taken at the rounded 1e51 it is quoted at. It can be computed.

THIS FILE DECIDES NOTHING. The error-vs-estimate call is filed for Duho in
OPEN_QUESTIONS_FOR_DUHO.md. What it does is make that call better informed, by establishing
whether the discrepancy is an artefact of one arbitrary route choice or survives all of them.
"""
import math, sys, re
S="../bhu-reading-20260823/sources/"
P=" ".join(open(S+"0910.1181_clean.txt").read().split())
G=6.67430e-11; c=2.99792458e8; hbar=1.054571817e-34; me=9.1093837015e-31
TARGET=1e16
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B13 -- can Poplawski's 1e16 kg be reached from his own quantities?"); print("="*98)

print("\n1. THE CARTAN RADIUS, FROM THE PAPER'S OWN EQUATION (33)")
r_Ce = (G*hbar**2/(c**4*me))**(1.0/3.0)
rho_precise = me/r_Ce**3
print(f"   r_Ce = [G hbar^2 / (c^4 m_e)]^(1/3) = {r_Ce:.3e} m     (paper: '~10^-27 m')")
print(f"   rho_Ce = m_e / r_Ce^3               = {rho_precise:.3e} kg/m^3  (paper: '~10^51')")
chk("COMPUTED: the paper's own eq. (33) reproduces the Cartan radius it quotes, so its inputs are "
    "internally consistent and can be used at full precision",
    abs(math.log10(r_Ce)+27) < 0.5 and "10 − 27" in P.replace("−","−"),
    f"{r_Ce:.2e} m against the paper's stated ~1e-27 m -- agreement to a factor of 2. The rounded "
    f"1e51 both seats used is 9x below the value eq. (33) actually gives")

print("\n2. EVERY ROUTE FROM A DENSITY TO A MINIMUM BLACK-HOLE MASS")
def M_from(rho, form):
    if form=="mean":  return math.sqrt(3*c**6/(32*math.pi*G**3*rho))   # M/(4/3 pi r_s^3)
    if form=="nogeo": return math.sqrt(c**6/(8*G**3*rho))              # M/r_s^3, factors dropped
rows=[]
for label,rho in [("paper's quoted rho ~1e51", 1e51), ("rho from eq.(33), exact", rho_precise)]:
    for form,fname in [("mean","M/(4/3 pi r_s^3)"),("nogeo","M/r_s^3, no geometry")]:
        M=M_from(rho,form); rows.append((label,fname,M))
# a different criterion entirely: horizon shrinks to the Cartan radius
M_rs = r_Ce*c**2/(2*G); rows.append(("r_s(M) = r_Ce","horizon = Cartan size",M_rs))
print(f"   {'density used':<26} {'criterion':<24} {'M_min':>12} {'vs 1e16 kg':>12}")
for lab,f,M in rows:
    print(f"   {lab:<26} {f:<24} {M:>12.2e} {TARGET/M:>11.3g}x")
best=min(rows,key=lambda r: abs(math.log10(r[2]/TARGET)))
print(f"\n   closest of all routes: {best[1]} on {best[0]} -> {best[2]:.2e} kg, "
      f"still {TARGET/best[2]:.0f}x below the printed floor")
chk("COMPUTED: NO route built from the paper's own quantities lands within an order of magnitude "
    "of 1e16 kg -- so the gap is not an artefact of choosing the wrong one",
    all(abs(math.log10(M/TARGET)) > 1.0 for _,_,M in rows),
    f"the nearest is {best[2]:.2e} kg ({math.log10(TARGET/best[2]):.2f} decades short); the "
    f"furthest is off by many more. Both seats tested only the first row")

print("\n3. WHICH DIRECTION THE REFINEMENT MOVES IT -- and it moves the WRONG way")
M_q = M_from(1e51,"mean"); M_p = M_from(rho_precise,"mean")
print(f"   on the quoted rho 1e51   M_min = {M_q:.2e} kg   -> {TARGET/M_q:.0f}x below the printed floor")
print(f"   on the exact rho {rho_precise:.1e}  M_min = {M_p:.2e} kg   -> {TARGET/M_p:.0f}x below")
chk("COMPUTED: using the paper's exact Cartan density instead of its rounded one makes the "
    "discrepancy LARGER, not smaller",
    TARGET/M_p > TARGET/M_q,
    f"{TARGET/M_q:.0f}x becomes {TARGET/M_p:.0f}x. The most obvious way the gap could have been an "
    f"artefact of rounding is therefore ruled out -- it runs the other way")

print("\n4. WHAT DENSITY WOULD BE NEEDED, stated as the size of the thing to be explained")
rho_needed = 3*c**6/(32*math.pi*G**3*TARGET**2)
print(f"   to get M_min = 1e16 kg the mean-density criterion needs rho = {rho_needed:.3e} kg/m^3")
print(f"   the paper's quoted rho_Ce is {1e51/rho_needed:.0f}x higher "
      f"({math.log10(1e51/rho_needed):.2f} decades)")
print(f"   the paper's exact  rho_Ce is {rho_precise/rho_needed:.0f}x higher "
      f"({math.log10(rho_precise/rho_needed):.2f} decades)")
chk("COMPUTED: the density discrepancy is 3-4 decades, which is more than the passage's hedging "
    "language conventionally covers",
    math.log10(rho_precise/rho_needed) > 3.0,
    f"{math.log10(rho_precise/rho_needed):.2f} decades. 'on the order of' and '~' are normally "
    f"read as within a decade, occasionally two. THIS IS THE OBSERVATION THAT BEARS ON THE SPLIT, "
    f"and it is presented as an observation -- the call is Duho's, not this file's")

print("""
5. WHAT I STILL CANNOT DO, and it is why this does not close the question

   I CANNOT SHOW WHAT POPLAWSKI DID. Ruling out every route I can construct is not the same as
   proving no route exists. He may apply the density bound to a quantity I have not thought of --
   the matter's proper density rather than the hole's mean density, a configuration that is not
   a Schwarzschild hole, or a step carried over from a reference I have not pinned. The paper
   states the two numbers consecutively and shows nothing between them.

   SO THE HONEST FINDING IS NARROWER THAN "HE IS WRONG": the printed floor does not follow from
   the printed density by any route reconstructible from this paper, the shortfall is 3-4 decades
   in density, and refining his inputs widens it. Whether that is called an error remains a
   judgement about how this programme speaks about other people's work -- open question 2, Duho's.

   AND THE ROUTE'S STRENGTH DOES NOT WAIT ON IT. b12 already records entry 51's PBH route as
   conditional, with the forbidden band given at both 2.00 and 0.43 decades. This file adds a
   THIRD candidate below both: on the exact Cartan density the floor is ~9e16 g, which sits BELOW
   the open window's lower edge entirely and would leave no forbidden band inside it at all.
""")
M_exact_g = M_p*1e3
print(f"   floor on the exact Cartan density: {M_exact_g:.2e} g   vs window lower edge 1.00e+17 g")
print(f"   -> forbidden band inside the window: {'NONE' if M_exact_g <= 1e17 else 'some'}")
chk("COMPUTED: on the exact density the floor falls below the open window entirely, so the third "
    "candidate removes the PBH band rather than shrinking it",
    M_exact_g <= 1e17,
    f"{M_exact_g:.2e} g < 1e17 g. Recorded so that no reader takes b12's two-decade band as the "
    f"only possibility on the table -- there are now three, and they disagree about whether the "
    f"route exists at all")
n=sum(1 for _,o,_ in checks if o)
print(f"\nSELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
