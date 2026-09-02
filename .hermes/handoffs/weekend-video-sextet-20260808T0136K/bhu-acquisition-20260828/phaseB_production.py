#!/usr/bin/env python3
"""Phase (b) production MC: 5 freedom-map rows x 2000 masked skies, prereg'd.
Output: percentiles only (prereg section 5). Seeds recorded. C3 reductio applies
to the LCDM row's reporting: a percentile, never a refutation."""
import numpy as np
import healpy as hp
from phaseB_pipeline import (NSIDE, LMAX, bin_kernels, chat_bins, s_half, synth)
from phaseB_c2 import remove_monodipole

N_SKY = 2000
SEEDS = {"lcdm": 100000, "A_2pi": 200000, "A_pi": 300000,
         "B_spliced": 400000, "B_nosplice": 500000}

def main():
    d = np.load("phaseB_model_cls.npz")
    obs = np.load("phaseB_observed.npz")
    s_obs, w = float(obs["s_obs"]), obs["mask"]
    beta, kappa = bin_kernels(LMAX)
    out = {}
    print(f"observed cut-sky S_1/2 = {s_obs:.1f} uK^4; f_sky={w.mean():.4f}; n={N_SKY}/row")
    for name, seed0 in SEEDS.items():
        s = np.empty(N_SKY)
        for i in range(N_SKY):
            t = synth(d[name], seed0 + i)
            t = remove_monodipole(t, w)
            s[i] = s_half(chat_bins(t, w, beta, kappa, LMAX))
        p = float(np.mean(s <= s_obs))
        out[name] = s
        print(f"  {name:>10}: median={np.median(s):10.0f}  5th pct={np.percentile(s,5):9.0f}  "
              f"P(S<=obs)={p*100:6.2f}%   [seed {seed0}]", flush=True)
    np.savez("phaseB_production.npz", s_obs=s_obs, **out)
    print("wrote phaseB_production.npz -- percentiles only; interpretation returns to Duho")

if __name__ == "__main__":
    main()
