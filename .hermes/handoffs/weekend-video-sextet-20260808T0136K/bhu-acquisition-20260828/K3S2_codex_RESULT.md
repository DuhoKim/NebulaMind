K3S2_EXCHANGE_NEGLIGIBLE

# Codex route-1 seat result

The executable calculation uses medium normal ordering (the `T=mu=0` vacuum is subtracted), metric `diag(+---)`, and `epsilon_0123=+1`. It derives from the source definitions that `s_ij u^j=0` and `1/2 s_ij s^ij=|s_vec|^2`, with signed ratio `+1`.

For a periodic comoving cell `V=ell^3`, the unpolarized Hartree term is exactly zero. Spatial coarse-graining projects the Fock line onto equal momentum modes. With `I1_r=integral d^3p/(2pi)^3 f_r` and `I2_r=integral d^3p/(2pi)^3 f_r^2`, including `r=+1` particles and `r=-1` antiparticles, the script obtains

`n=2 N_f (I1_+ + I1_-)`,

`Fock=-(3/2) N_f (I2_+ + I2_-)/V = -(3/4)(n/V) R`,

where `R=(I2_+ + I2_-)/(I1_+ + I1_-)` and `0<=R<=1`. Thus exchange is never larger than order `n/V` and vanishes in the thermodynamic limit at fixed density. At `T->0`, `R=1` in both `p_F<<m` and `p_F>>m`; at `T->infinity` at fixed `n`, `R->0` in both mass regimes. The script separately prints the operator self term `(3/4)n/V`, before printing the sum.

The derived Fermi-sea count is `n=N_f p_F^3/(3 pi^2)`, hence `p_F=(3 pi^2 n/N_f)^(1/3)`. No printed closure coefficient is used in this derivation.

Both printed relations are contradicted by this state and observable: neither the spin-fluid `1/8 n^2` relation (source line 121) nor the Dirac `3/4 n^2` relation (source line 113) is derived, because no `n^2` term survives. The exact O4 map makes this conclusion common to both scalars.

All eight preregistered controls print `PASS`. The executable output is the receipt for every algebraic and limiting claim above.
