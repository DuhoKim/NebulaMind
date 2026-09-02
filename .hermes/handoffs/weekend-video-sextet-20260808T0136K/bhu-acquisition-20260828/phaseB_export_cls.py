#!/usr/bin/env python3
"""Phase (b) step 1: export the five freedom-map model C_l rows to one .npz.

Reuses the EXACT constructions that produced the gated numbers (never re-derives):
  - LCDM and Reading A rows: cutoffA_pvalue_shift.cl_for (the gated 6,897 / 14,000 run)
  - Reading B rows: cutoffA_norm_residual's spliced/no-splice tables + camb_cls
    (the gated 8,776.675 / 10,132.383 run)

REGRESSION GATE (register 1at rule 3 -- prove same-object before reuse): each row's
S_1/2 is recomputed with the validated operator and must match its gated value to
0.2%, else this export refuses to write.
"""

import numpy as np
from cutoffA_s12_machinery import s12_matrix, s12_from_cl
import cutoffA_pvalue_shift as pv
import cutoffA_norm_residual as nr

GATED = {                       # committed, gated values (uK^4)
    "lcdm":       34924.0,      # cutoffA_pvalue_shift run
    "A_2pi":      6897.0,
    "A_pi":       14000.0,
    "B_spliced":  8776.675,     # MONOPOLE_FIXED / NORM_RESIDUAL runs
    "B_nosplice": 10132.383,
}
TOL = 2e-3


def reading_b_cls():
    """Rebuild both Reading-B rows via codex's own functions, deepest regulator."""
    klo, db, c = nr.fixed_raw_low_table(nr.KMIN)
    ks, ds, norm, _ = nr.spliced_table(klo, db)
    kn, dn, _, _ = nr.no_splice_table(klo)
    return nr.camb_cls(ks, ds), nr.camb_cls(kn, dn)


def main():
    rows = {}
    print("building rows...")
    rows["lcdm"] = pv.cl_for(None)
    chi_s = pv.chi_S_mpc()
    rows["A_2pi"] = pv.cl_for(2 * np.pi / chi_s)
    rows["A_pi"] = pv.cl_for(np.pi / chi_s)
    rows["B_spliced"], rows["B_nosplice"] = reading_b_cls()

    # regression gate at each row's native l_max
    ok = True
    for name, cl in rows.items():
        M = s12_matrix(len(cl) - 1)
        s = s12_from_cl(cl, M)
        rel = abs(s - GATED[name]) / GATED[name]
        flag = "OK " if rel < TOL else "FAIL"
        print(f"  {name:>10}: l_max={len(cl)-1:>3}  S_1/2={s:12.3f}  "
              f"gated={GATED[name]:12.3f}  rel={rel:.2e}  {flag}")
        ok &= rel < TOL
    if not ok:
        raise SystemExit("REGRESSION GATE FAILED -- not writing the npz.")

    # pad all rows to a common l_max=191 (Nside 64 anafast range) with zeros;
    # harmless under the 160' beam (b_l^2 ~ 8e-4 already at l=191) and recorded.
    LPAD = 191
    out = {}
    for name, cl in rows.items():
        v = np.zeros(LPAD + 1)
        v[:len(cl)] = cl
        out[name] = v
    np.savez("phaseB_model_cls.npz", lmax=LPAD, **out)
    print(f"wrote phaseB_model_cls.npz (lmax={LPAD}, zero-padded above native)")


if __name__ == "__main__":
    main()
