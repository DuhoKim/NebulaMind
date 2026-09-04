LIMBA_NOT_PERTURBATIVE

# Codex blind-seat result

The script restates and evaluates entry 10's ultrarelativistic, kinetic-equilibrium relations. Its receipt is:

```text
SYMBOLIC_RATIO: R(T) = alpha*h_n^2*T^2/h_* = (9/16)*kappa*h_n^2*T^2/h_*.
TEMPERATURE_SCALING: R(T) is proportional to T^2 when h_* and h_n are constant.
BOUNCE_SUBSTITUTION: R(T_cr) = (alpha*h_n^2/h_*)*[2*h_*/(3*alpha*h_n^2)] = 2/3.
R_AT_BOUNCE_EXACT=2/3
R_AT_BOUNCE_DECIMAL=0.666666666667
INTERPRETATION: 2/3 is fixed by construction from the source's da/dT=0 condition and Eq. (16); it is not an independent measurement.
DISTINCTION: Eq. (16)'s minimum-scale-factor condition fixes R=2/3; equality |epsilon_tilde|=epsilon would instead define R=1 and is not the cited Eq. (16) condition.
```

The inputs are `epsilon_tilde=-alpha*n^2`, `alpha=(9/16)kappa` (entry 10 L116-L118), `epsilon=h_*T^4` and `n=h_nT^3` with the stated effective degree counts (L152-L159, L166-L168), and `T_cr^2=2h_*/(3alpha h_n^2)` from `da/dT(T_cr)=0` (L177-L193). Thus the cited minimum-scale-factor condition fixes `R(T_cr)=2/3` algebraically. This is a construction, not a measurement. In particular, the separate condition `|epsilon_tilde|=epsilon` would give `R=1`, but that is not entry 10's cited Eq. (16) condition.

Away from the bounce, the script chooses `T=T_cr/100`, a named representative of the `T << T_cr` radiation-dominated regime identified at entry 10 L193-L194. It prints:

```text
AWAY_ALGEBRA: R(T)/R(T_cr)=(T/T_cr)^2, so R(T_cr/100)=(2/3)*(1/100)^2=1/15000.
R_AWAY_EXACT=1/15000
R_AWAY_DECIMAL=0.000066666667
DECLARED_THRESHOLD=1/10
AWAY_CONCLUSION: R=1/15000 is below the declared 1/10 threshold, so the interaction is perturbative at this named scale by that criterion.
THRESHOLD_TEST: |R(T_cr)|=2/3 >= 1/10 is True.
LIMB_A_FIRES=YES
OUTCOME_CLASS=K3S3_NOT_PERTURBATIVE
CONCLUSION: the interaction is not a small perturbation where the source's bounce/minimum-scale-factor chain operates; limb B must not run.
```

The preregistered threshold therefore fires. The outcome is `K3S3_NOT_PERTURBATIVE`; no Hartree-Fock coefficient is derived.

Controls printed by the script:

```text
C4_EXPANSION_PARAMETER_COMPUTED=PASS
C1_FREE_LIMIT_MATCHES_K3S2=NOT RUN
C2_INTERACTION_DELETED=NOT RUN
C3_FOUR_TERMS_SEPARATE=NOT RUN
C5_MAP_DERIVED=NOT RUN
C6_BOTH_OBJECTS_REPORTED=NOT RUN
C7_NO_PRINTED_COEFF_INPUT=NOT RUN
```

No tier, warrant token, standing, or stamp is changed.
