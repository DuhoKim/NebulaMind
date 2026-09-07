SIGN_CHECK=DISCREPANCY

Referee note, 2026-09-07. Everything below is derived only from the equations quoted in the
brief. Notation: kappa = 8 pi G; alpha_A = (9/16) kappa (Source A, c = hbar = 1);
alpha_B = kappa (hbar c)^2 / 32 (Source B). Algebra was machine-checked with sympy.


QUESTION 1 — Sign of the torsion correction to the pressure

Source A (tildes = corrections). Eq. (10) reads
    eps_tilde = -p_tilde = -alpha_A n^2
i.e.  eps_tilde = -alpha_A n^2   and   p_tilde = +alpha_A n^2.
Because A's tildes are the corrections themselves, A's effective totals are
    eps_tot = eps + eps_tilde = eps - alpha_A n^2,
    p_tot   = p + p_tilde     = p + alpha_A n^2.
This conversion is pinned by A itself, not assumed: Eq. (11) contains exactly
(eps - alpha n^2) and Eq. (12) contains exactly (p + alpha n^2). Both match.
    => A's pressure correction:  Delta_p_A = +alpha_A n^2 = +(9/16) kappa n^2.  POSITIVE.

Source B (tildes = effective totals). Eq. (1): p_tilde = p - alpha_B n_f^2.
    => B's pressure correction:  Delta_p_B = -alpha_B n_f^2 = -(kappa (hbar c)^2 / 32) n_f^2.  NEGATIVE.

Agreement: NO. After converting both to the same (effective-total) convention, the two
pressure corrections have opposite signs. For the record, the density corrections
(-alpha n^2 in both papers) DO agree in sign; the disagreement is only in the pressure term.


QUESTION 2 — Torsion contribution as a fluid: w and a-scaling

Source A: eps_s = -alpha_A n^2, p_s = +alpha_A n^2.
    w_A = p_s / eps_s = -1.
Continuity: d(eps_s)/dt = -3 H (1 + w_A) eps_s = 0  =>  eps_s = const, i.e. eps_s ~ a^0.
But the model's eps_s = -alpha_A n^2 with n ~ a^-3 would require eps_s ~ n^2 ~ a^-6.
a^0 vs a^-6: INCONSISTENT.
Exactly where: with p_s = -eps_s the torsion fluid does no work, so its own continuity
equation forces d(n^2)/dt = 0 — a spin-squared density cannot redshift. A avoids this only
because its actual conservation law is the FIRST LAW FOR THE TOTAL FLUID,
d[(eps - alpha n^2) a^3] = -(p + alpha n^2) d(a^3), which conserves matter+torsion jointly
with energy exchange between them. (Check: with eps = h_star T^4, p = eps/3, n = h_n T^3,
E = eps_tot gives dE = (4 h_star T^3 - 6 alpha h_n^2 T^5) dT and E + P = eps + p =
(4/3) h_star T^4; then dE + 3(E+P) da/a = 0 divided by 4 h_star T^4 gives
dT/T - (3 alpha h_n^2 / (2 h_star)) T dT + da/a = 0, exactly A's Eq. (14).) The price of
that exchange is visible in A's own Eq. (15): at high T the exponential factor makes
a T != const, so n = h_n T^3 is NOT proportional to a^-3. So under the assumption
n ~ a^-3, A's torsion fluid violates its own continuity equation; A stays internally
consistent only by giving up n ~ a^-3.

Source B: eps_s = -alpha_B n_f^2, p_s = -alpha_B n_f^2.
    w_B = p_s / eps_s = +1  (stiff).
Continuity: eps_s ~ a^(-3(1+1)) = a^-6 ~ n_f^2 with n_f ~ a^-3. CONSISTENT, exactly,
with no exchange term needed.


QUESTION 3 — B's criterion  -kappa (eps_tilde + 3 p_tilde)/2 > 2 sigma^2,
with p = eps/3, eps > 0, sigma^2 >= 0.

(a) B's signs (Eq. 1):
    eps_tilde + 3 p_tilde = (eps - alpha_B n_f^2) + 3 (p - alpha_B n_f^2)
                          = eps + 3p - 4 alpha_B n_f^2
                          = 2 eps - 4 alpha_B n_f^2        (p = eps/3).
    LHS = -(kappa/2)(2 eps - 4 alpha_B n_f^2) = kappa (2 alpha_B n_f^2 - eps).
    Criterion:  kappa (2 alpha_B n_f^2 - eps) > 2 sigma^2.
    Since sigma^2 >= 0, a necessary condition is
        n_f^2 > eps / (2 alpha_B) = 16 eps / (kappa (hbar c)^2),
    and then the shear must satisfy
        sigma^2 < (kappa/2)(2 alpha_B n_f^2 - eps) = kappa^2 (hbar c)^2 n_f^2 / 32 - kappa eps / 2.
    => The inequality CAN hold: dense enough spin (n_f^2 above threshold) and shear below
       the stated bound. Singularity avoidance is possible with B's signs.

(b) A's pressure sign instead (totals eps - alpha n^2, p + alpha n^2):
    eps_tot + 3 p_tot = (eps - alpha_A n^2) + 3 (p + alpha_A n^2)
                      = eps + 3p + 2 alpha_A n^2
                      = 2 eps + 2 alpha_A n^2 > 0  for all eps > 0, n.
    LHS = -(kappa/2)(2 eps + 2 alpha_A n^2) = -kappa eps - (9/16) kappa^2 n^2 < 0.
    The criterion demands this strictly negative number exceed 2 sigma^2 >= 0.
    => The inequality can NEVER hold, for any n, eps > 0, or sigma^2 >= 0. With A's
       pressure sign, B's singularity-avoidance mechanism is impossible.


QUESTION 4 — Which convention is the standard Einstein-Cartan result

Source B's. In standard Einstein-Cartan theory torsion is algebraically (not dynamically)
coupled to spin; solving the torsion equation and substituting back shifts the effective
energy density AND the effective pressure by the SAME negative, spin-squared term,
Delta_eps = Delta_p = -(positive constant) <spin^2>. The torsion contribution is therefore
a stiff (w = +1) fluid scaling as a^-6, and its negative density is what permits a bounce
— exactly B's Eq. (1) structure. Reference: F. W. Hehl, P. von der Heyde, G. D. Kerlick,
J. M. Nester, "General relativity with spin and torsion: Foundations and prospects",
Rev. Mod. Phys. 48, 393 (1976), spinning-fluid/EC-cosmology section. Confidence note: the
sign structure (equal negative corrections to density and pressure, w = +1, a^-6) is the
standard, widely quoted result; the numerical coefficient depends on the spin-averaging
convention, which is also why A's (9/16) kappa and B's kappa (hbar c)^2/32 differ — that
coefficient difference is not at issue here. A's pressure sign (+alpha n^2, i.e. w = -1
for the torsion piece) is not the standard EC spin-fluid result.


QUESTION 5 — Genuine discrepancy, or reconcilable convention difference?

GENUINE DISCREPANCY, in the pressure-correction sign only.

The one convention difference between the papers (tilde = correction vs tilde = total) has
already been removed in Q1 before comparing, and the conversion is not a matter of
interpretation: A's own Eqs. (11) and (12) fix its effective totals unambiguously as
eps - alpha n^2 and p + alpha n^2. After conversion, A adds +alpha n^2 to the pressure
while B adds -alpha_B n_f^2: opposite signs. No relabeling can flip a sign, so the
difference is physical, not notational.

The consequences seen in Q2-Q3 are correspondingly physical: A's sign makes the torsion
piece a w = -1 fluid, which cannot redshift as a^-6 under its own continuity equation
(A only stays consistent by abandoning n ~ a^-3, as its Eq. (15) shows), and it makes
B's singularity-avoidance criterion unsatisfiable for any parameters; B's signs are
internally consistent, match the standard EC result, and allow the bounce criterion to
hold. The density-correction signs agree between the two papers; the alpha coefficients
differ ((9/16) kappa vs kappa (hbar c)^2/32), which is a separate, spin-averaging
convention matter and does not bear on the sign discrepancy.
