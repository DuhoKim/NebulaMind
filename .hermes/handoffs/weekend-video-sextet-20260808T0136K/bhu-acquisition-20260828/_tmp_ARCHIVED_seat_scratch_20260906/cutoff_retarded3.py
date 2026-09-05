import numpy as np
import camb

pars = camb.CAMBparams()
pars.set_cosmology(H0=67.4, ombh2=0.0224, omch2=0.120, mnu=0.06, omk=0, tau=0.054)
pars.InitPower.set_params(As=2.1e-9, ns=0.965, pivot_scalar=0.05)
pars.set_for_lmax(2500, lens_potential_accuracy=0)
pars.WantTransfer = True
results = camb.get_results(pars)

cls = results.get_total_cls(2500, CMB_unit='muK')

trans = results.get_cmb_transfer_data()
q = trans.q
ells = trans.L
delta_T = trans.delta_p_l_k[0, :, :]

l_idx = 2
L = ells[l_idx]
integrand = delta_T[l_idx, :]**2 * (2.1e-9 * (q/0.05)**(0.965-1)) / q
cl_trans = np.trapz(integrand, q) * (2.7255e6)**2

print("L:", L)
print("cl_raw (TxT, l(l+1)/2pi):", cls[L, 0])
print("cl_trans (integral):", cl_trans)
print("ratio:", cls[L, 0] / cl_trans)
print("L*(L+1)/2pi:", L*(L+1)/(2*np.pi))

