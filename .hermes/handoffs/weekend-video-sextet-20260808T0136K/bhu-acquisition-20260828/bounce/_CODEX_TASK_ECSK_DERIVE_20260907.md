# BOUNDED CODEX TASK — derive the spin-fluid effective stress-energy from the ECSK action (Tori, 2026-09-07)

The question is decided by DERIVATION, not by citation: in Einstein-Cartan-Sciama-Kibble gravity, what sign does the spin-spin
contact term contribute to the EFFECTIVE PRESSURE, relative to its contribution to the effective energy density?

## Boundaries
- Write ONLY under `bounce/`. No pinned census file, no kit, no census version. No Hwao data.
- You are DERIVING. Do not settle the question by quoting either Poplawski paper, and do not consult
  `KIMI_SIGN_CHECK_20260907.md` or `B1_DERIVATION_20260907.md` — an independent seat has already answered separately and I am
  comparing the two. Standard textbook/review results may be CITED as a check on your own derivation, never as its substitute.

## Derive, showing every step
1. Start from the ECSK action: Einstein-Hilbert with the Riemann-Cartan curvature scalar plus a minimally coupled matter action
   with spin. State the signature, the sign conventions for the curvature and for kappa, and the definition of the spin tensor
   you use. These conventions are where sign errors hide: state them explicitly and carry them through.
2. Vary with respect to the torsion (contortion). Show that the torsion field equation is ALGEBRAIC and solve it for the torsion
   in terms of the spin tensor.
3. Substitute back to obtain the effective Einstein equation in terms of the Levi-Civita (Riemannian) curvature plus terms
   QUADRATIC in the spin tensor. Print that effective stress-energy tensor explicitly.
4. Specialise to a Weyssenhoff-type spin fluid of unpolarised spin-1/2 particles with the isotropic average <s^2> and number
   density n, in a homogeneous cosmology. Read off the effective energy density correction and the effective pressure
   correction. State the equation-of-state parameter w = p_s/eps_s of the spin contribution.
5. CONSISTENCY CHECK, done as a derivation not an assertion: with n proportional to a^-3, does your (eps_s, p_s) pair satisfy
   the continuity equation eps_s_dot + 3 H (eps_s + p_s) = 0? Show the algebra. If it does not, your derivation is wrong or the
   spin contribution is not separately conserved — say which, and show why.
6. Do the algebra symbolically where it helps (sympy), in `bounce/ecsk_derive.py`, printing the effective density and pressure
   corrections and w. The script must run as `/usr/bin/python3 ecsk_derive.py` and write nothing outside `bounce/`.

## Output: `bounce/ECSK_DERIVATION_20260907.md` and `bounce/ecsk_derive.py`
The write-up states: the conventions chosen; the derived effective stress-energy; eps_s, p_s and w; the continuity check with
its algebra; and a single explicit sentence of the form "the derivation gives the effective pressure correction the SAME sign as
/ the OPPOSITE sign to the effective density correction". Then, and only then, name which published convention that supports.
State any step where a different convention choice would flip the answer. Print both files' sha256 and the derived w as your
final answer.
