#!/usr/bin/env python3
"""K3 step 3 limb A receipt, codex blind seat.

Prediction fixed before evaluation: only C4 is run in limb A. C1, C2, C3,
C5, C6, and C7 are NOT RUN if the declared threshold fires.
"""

from fractions import Fraction


def main() -> None:
    threshold = Fraction(1, 10)
    away_fraction = Fraction(1, 100)

    print("REGIME: ultrarelativistic matter in kinetic equilibrium (entry 10 L152).")
    print("SOURCE_DEFINITION: epsilon_tilde = -p_tilde = -alpha*n^2; alpha = (9/16)*kappa (entry 10 L116-L118).")
    print("SOURCE_DEFINITION: epsilon(T) = (pi^2/30)*g_*(T)*T^4 = h_* T^4 (entry 10 L152-L153, L166-L167).")
    print("SOURCE_DEFINITION: n(T) = (zeta(3)/pi^2)*g_n(T)*T^3 = h_n T^3 (entry 10 L154-L159, L166-L167).")
    print("SOURCE_DEFINITION: g_* = g_b + (7/8)g_f and g_n = (3/4)g_f; only fermions contribute to torsion (entry 10 L156-L159).")
    print("SOURCE_DEFINITION: h_* and h_n are treated as constant over the temperature range considered (entry 10 L166-L168).")
    print("SOURCE_BOUNCE: da/dT(T_cr)=0 and T_cr^2 = 2*h_*/(3*alpha*h_n^2); a_cr=a(T_cr)>0 is the smallest allowed scale factor (entry 10 L177-L193, Eq. 16-Eq. 17).")
    print("ALGEBRA: R(T) = |epsilon_tilde|/epsilon = alpha*n(T)^2/epsilon(T).")
    print("ALGEBRA: R(T) = alpha*[(zeta(3)/pi^2)g_n T^3]^2 / [(pi^2/30)g_* T^4].")
    print("SYMBOLIC_RATIO: R(T) = alpha*h_n^2*T^2/h_* = (9/16)*kappa*h_n^2*T^2/h_*.")
    print("TEMPERATURE_SCALING: R(T) is proportional to T^2 when h_* and h_n are constant.")

    r_bounce = Fraction(2, 3)
    print("BOUNCE_SUBSTITUTION: R(T_cr) = (alpha*h_n^2/h_*)*[2*h_*/(3*alpha*h_n^2)] = 2/3.")
    print(f"R_AT_BOUNCE_EXACT={r_bounce.numerator}/{r_bounce.denominator}")
    print(f"R_AT_BOUNCE_DECIMAL={float(r_bounce):.12f}")
    print("INTERPRETATION: 2/3 is fixed by construction from the source's da/dT=0 condition and Eq. (16); it is not an independent measurement.")
    print("DISTINCTION: Eq. (16)'s minimum-scale-factor condition fixes R=2/3; equality |epsilon_tilde|=epsilon would instead define R=1 and is not the cited Eq. (16) condition.")

    r_away = r_bounce * away_fraction**2
    print("AWAY_SCALE: choose T=T_cr/100, a representative T << T_cr point in the radiation-dominated regime identified at entry 10 L193-L194.")
    print("AWAY_ALGEBRA: R(T)/R(T_cr)=(T/T_cr)^2, so R(T_cr/100)=(2/3)*(1/100)^2=1/15000.")
    print(f"R_AWAY_EXACT={r_away.numerator}/{r_away.denominator}")
    print(f"R_AWAY_DECIMAL={float(r_away):.12f}")
    print(f"DECLARED_THRESHOLD={threshold.numerator}/{threshold.denominator}")
    print("AWAY_CONCLUSION: R=1/15000 is below the declared 1/10 threshold, so the interaction is perturbative at this named scale by that criterion.")

    fires = abs(r_bounce) >= threshold
    print(f"THRESHOLD_TEST: |R(T_cr)|=2/3 >= 1/10 is {fires}.")
    print("LIMB_A_FIRES=YES")
    print("OUTCOME_CLASS=K3S3_NOT_PERTURBATIVE")
    print("CONCLUSION: the interaction is not a small perturbation where the source's bounce/minimum-scale-factor chain operates; limb B must not run.")
    print("C4_EXPANSION_PARAMETER_COMPUTED=PASS")
    print("C1_FREE_LIMIT_MATCHES_K3S2=NOT RUN")
    print("C2_INTERACTION_DELETED=NOT RUN")
    print("C3_FOUR_TERMS_SEPARATE=NOT RUN")
    print("C5_MAP_DERIVED=NOT RUN")
    print("C6_BOTH_OBJECTS_REPORTED=NOT RUN")
    print("C7_NO_PRINTED_COEFF_INPUT=NOT RUN")
    print("SCOPE: no tier, warrant token, standing, or stamp is changed.")


if __name__ == "__main__":
    main()
