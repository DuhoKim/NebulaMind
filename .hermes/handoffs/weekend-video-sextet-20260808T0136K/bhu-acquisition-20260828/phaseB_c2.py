#!/usr/bin/env python3
"""Control C2: does OUR estimator on the real masked SMICA map reproduce the
literature's cut-sky S_1/2 (~1,000-1,300 uK^4)? FAIL -> STOP, per prereg."""
import numpy as np
import healpy as hp
from phaseB_pipeline import (NSIDE, LMAX, FWHM_RAD, bin_kernels, chat_bins, s_half)

def remove_monodipole(m, w):
    npix = len(m)
    vecs = np.array(hp.pix2vec(hp.npix2nside(npix), np.arange(npix))).T
    A = np.c_[np.ones(npix), vecs][w > 0]
    coef, *_ = np.linalg.lstsq(A, m[w > 0], rcond=None)
    return m - np.c_[np.ones(npix), vecs] @ coef

def main():
    print("loading mask...")
    mask_hi = hp.read_map("planck_data/COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits",
                          field=0, dtype=np.float64)
    w = (hp.ud_grade(mask_hi, NSIDE) > 0.9).astype(float)
    print(f"  f_sky(2048) = {mask_hi.mean():.4f}   f_sky(64, >0.9) = {w.mean():.4f}")

    print("loading SMICA I...")
    t_hi = hp.read_map("planck_data/COM_CMB_IQU-smica_2048_R3.00_full.fits",
                       field=0, dtype=np.float64)
    t = hp.ud_grade(t_hi, NSIDE) * 1e6                    # K_CMB -> uK
    t = hp.smoothing(t, fwhm=FWHM_RAD)
    t = remove_monodipole(t, w)
    print(f"  masked-sky rms after mono/dipole removal = {np.std(t[w>0]):.1f} uK")

    beta, kappa = bin_kernels(LMAX)
    chat = chat_bins(t, w, beta, kappa, LMAX)
    s = s_half(chat)
    print(f"\n[C2] observed cut-sky S_1/2 (this estimator) = {s:,.1f} uK^4")
    print(f"[C2] literature range (mask-dependent)       = ~1,000 - 1,300 uK^4")
    verdict = "PASS" if 700.0 <= s <= 1600.0 else "FAIL"
    print(f"[C2] -> {verdict}  (prereg: FAIL means STOP, no comparison licensed)")
    np.savez("phaseB_observed.npz", s_obs=s, chat=chat, mask=w, t=t)
    print("wrote phaseB_observed.npz")

if __name__ == "__main__":
    main()
