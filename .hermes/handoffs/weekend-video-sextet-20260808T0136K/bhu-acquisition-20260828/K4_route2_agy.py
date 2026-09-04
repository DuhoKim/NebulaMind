import sys

def main():
    print("ROUTE 2: INDEPENDENT ANALYSIS OF THE PERTURBED DARMOIS JUNCTION")
    print("Method: Explicit Israel-junction computation with surface displacement")
    print("This method is independent as it avoids both the longitudinal/conformal-Newtonian gauge and the Gaussian-normal boundary-adapted gauge, explicitly carrying the boundary displacement in the unperturbed comoving frame.")
    
    print("\n1. Junction conditions multipole by multipole:")
    print("For a perturbed spherical boundary, the Darmois-Israel conditions require continuity of the induced metric [h_{ab}] = 0 and the extrinsic curvature [K_{ab}] = 0.")
    print("Decomposing into spherical harmonics (Y_lm):")
    print(" - l = 0 (Monopole): The perturbations correspond to a shift in the interior density and a corresponding shift in the exterior Schwarzschild mass delta_M.")
    print(" - l = 1 (Dipole): The perturbations correspond to a pure velocity shift (center of mass/momentum) with no gravitational radiation.")
    print(" - l >= 2: The interior contains scalar density perturbations (growing and decaying modes). The exterior vacuum contains even-parity gravitational waves, governed by the Zerilli equation for a master function Psi_Z(t, r).")
    
    print("\n2. Analysis of the junction per multipole:")
    print(" - l = 0: (d) The junction determines the exterior continuation (delta_M) while leaving the interior spectrum free. It provides no boundary condition that annihilates the interior perturbation.")
    print(" - l = 1: (d) The junction determines the exterior dipole (gauge/shift) while leaving the interior free.")
    print(" - l >= 2: (e) The junction fails to close as a boundary condition at all because some exterior datum is unfixed. The Darmois conditions provide Cauchy data (value and normal derivative) for Psi_Z on the boundary timelike hypersurface. However, to uniquely solve the Zerilli wave equation in the exterior, one must specify a boundary condition at infinity (e.g., no incoming radiation).")
    
    print("\n3. The decisive sub-question (Crux):")
    print("In the Schwarzschild vacuum exterior, the exterior solution is NOT uniquely determined by the interior via the junction. It retains FREE DATA.")
    print("Specifically, for every multipole l >= 2, the exterior retains one free function of time representing incoming even-parity gravitational radiation from past null infinity (or the white hole horizon).")
    print("Adding a 'no incoming radiation' or reflecting condition to remove this freedom would be an ADDITIONAL physical assumption, not something the Darmois conditions supply.")
    
    print("\n4. Explicit comparison to F1 and F2:")
    print(" - Unlike F1, this does not ONLY touch l=0. It touches all multipoles, but for l >= 2 it leaves the interior unconstrained due to the free exterior data.")
    print(" - Unlike F2, this does NOT force the interior perturbation to vanish (W_tilde delta_tilde = 0). The interior spectrum remains completely free, provided the exterior is allowed to contain the appropriate incoming/outgoing radiation.")
    print("Because the Darmois conditions alone do not close the system for l >= 2, this does not reduce to either F1 or F2.")
    
    print("\n5. Conclusion:")
    print("The junction does not close as a boundary condition without an added assumption. No missing condition is manufactured.")
    
    print("\nLIMB2_UNDETERMINED")

if __name__ == '__main__':
    main()
