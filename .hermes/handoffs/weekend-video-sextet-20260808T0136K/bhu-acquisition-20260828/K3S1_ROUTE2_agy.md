ACCESS_SHA=9ff4b0f41796fa8449a6b4980a324cedccf2c94c7503581c42ec86f6a5072698
HEADLINE=CLOSURE_SCALING_FAILS
OBJECT_FLUID=CLOSURE_SCALING_FAILS
OBJECT_DIRAC=CLOSURE_SCALING_FAILS

Controls:
C1: s_i s^i = 3/4.
C2: s_z = n/2, s_i s^i = n^2/4 + n/(2V).
C3: Restoring units yields (\hbar c n)^2 to match energy density \kappa s^2.
C4: Deletion probe (using polarized ensemble) changes BOTH objects from CLOSURE_SCALING_FAILS to an n^2 scaling, as predicted before running.

Derivations:
Unpolarized state: \rho = \frac{1}{2}|\uparrow\rangle\langle\uparrow| + \frac{1}{2}|\downarrow\rangle\langle\downarrow| = \frac{1}{2}\mathbf{I}.
Tr(\rho S_i S_j) = \frac{1}{4}\delta_{ij}; Tr(\rho S_i)Tr(\rho S_j) = 0.
Macroscopic spin density: \hat{s}_i = \frac{1}{V} \sum_A S_i^{(A)}.
(i) Pseudovector: \langle \hat{s}_i \hat{s}^i \rangle = \frac{1}{V^2} \sum_{A,B} \langle S_i^{(A)} S_i^{(B)} \rangle. Cross-terms vanish since Tr(\rho S_i) = 0. Auto-terms give N(3/4)/V^2 = \frac{3}{4}\frac{n}{V}. Scaling is n, not n^2.
(ii) Fluid: §1 equates s_{ijk} = s_{ij} u_k = -\epsilon_{ijkl} s^l \implies s_{ij} = -\epsilon_{ijkl} s^l u^k. Thus \frac{1}{2} s_{ab} s^{ab} = -s_k s^k = \mathbf{s}^2. The operator is identical to (i), yielding \frac{3}{4}\frac{n}{V}.

Prescriptions for n^2 closures:
3/4: Define macroscopic square as n^2 \langle \mathbf{s}_{micro}^2 \rangle.
1/8: Treat the unpolarized fluid as a 50/50 mixture of two fully polarized non-interfering fluids and sum their macroscopic squared spins: (n/2)^2/4 + (n/2)^2/4 = 1/8 n^2.
The pinned definitions fix neither prescription.
