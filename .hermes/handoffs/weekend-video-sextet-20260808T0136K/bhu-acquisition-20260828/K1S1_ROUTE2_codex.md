CLASS_A_s=K1_MONOTONE_UP
CLASS_MNS=K1_MONOTONE_DOWN

Controls (printed): C1 PASS, rho_BH=4.998380e7 Msun/Mpc3 (target 5e7; ratio 1.000). C2 PASS, N_PBH=0, beta_max=0, hence f_PBH<1. C3 PASS, stellar-only dN/dlnAs=(2.853248e6,2.853555e6,2.853631e6), UP. C4 PASS, analytic=2.853657e6 versus finite=2.853631e6 (ratio .999991), both UP.

Derivatives (/Mpc3); triples use central steps (.04,.02,.01) for lnAs and Msun respectively.

|case|alpha|engine|Z/Zsun|dc|dA triple|dMNS triple|
|---|---:|---|---:|---:|---|---|
|centre|2.3|D|.505|.4833|2.853248e6,2.853555e6,2.853631e6|-1.001603e6,-.9986512e6,-1.009456e6|
|01/02|1.6|D|.01|.3/.6667|3.905756e6,3.906176e6,3.906281e6|-.8503612e6,-.8479064e6,-.8431940e6|
|03/04|1.6|D|1|.3/.6667|3.488890e6,3.489265e6,3.489359e6|-1.954648e6,-1.949567e6,-1.963010e6|
|05/06|1.6|R|.01|.3/.6667|3.468481e6,3.468854e6,3.468947e6|-.1142474e6,-.1142362e6,-.1142390e6|
|07/08|1.6|R|1|.3/.6667|3.394782e6,3.395148e6,3.395239e6|-1.269472e6,-1.273487e6,-1.273122e6|
|09/10|3.0|D|.01|.3/.6667|2.017006e6,2.017223e6,2.017277e6|-1.002976e6,-.9999438e6,-.9943524e6|
|11/12|3.0|D|1|.3/.6667|1.915137e6,1.915343e6,1.915394e6|-1.191066e6,-1.185419e6,-1.201405e6|
|13/14|3.0|R|.01|.3/.6667|1.544827e6,1.544993e6,1.545034e6|-.1124010e6,-.1123803e6,-.1123854e6|
|15/16|3.0|R|1|.3/.6667|1.807845e6,1.808039e6,1.808088e6|-.3869764e6,-.3918122e6,-.3917692e6|

Direct quadrature uses Zentner Eq.14/top-hat (L277-278), the Eisenstein-Hu transfer named at L305, and numerically differentiated Press-Schechter Eq.16-17 (L339-380). Fryer PDF pp.11-12 Eqs.5-9 is inverted on 0.001-Msun ZAMS spacing. PBH beta uses Carr Eq.101 (L1683-1687), integrated over 1-100 Msun. Declared epsilon_star=3.273e-4 is fixed and sign-neutral. All steps retain their signs; neither parameter is stationary.
