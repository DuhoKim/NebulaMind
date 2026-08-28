#!/usr/bin/env python3
"""Identity unit test + tau calibration on synthetics. Section 10 item 1 runner.

Reports, bit-exactly:
  A. chi(mirror(x)) vs -chi(x) over the full synthetic grid — bit-pattern comparison.
  B. The signed-zero edge case on an exactly mirror-symmetric image.
  C. A deliberately broken mirror (interpolating reflection) — where the identity fails
     in practice and by how much.
  D. mirror(mirror(x)) == x bit-identity, and w determinism across repeated calls.
  E. tau calibration on armless-disk nulls; abstention + sign accuracy on spirals; dA_raw.
"""
from __future__ import annotations

import json
import sys

import numpy as np

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
                   "weekend-video-sextet-20260808T0136K/spike/yui_identity")
from w_chi import N, bits, chi, mirror, synth_disk, synth_spiral, w  # noqa: E402

OUT = ("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
       "weekend-video-sextet-20260808T0136K/spike/yui_identity/results.json")

PARITIES = (1, -1)
PITCHES = (10.0, 17.5, 25.0, 32.5, 40.0)
INCLS = (0.0, 25.0, 45.0, 60.0)
SNRS = (2.0, 5.0, 10.0, 25.0, 50.0)
SEEDS = tuple(range(5))

res = {"grid": {"parities": PARITIES, "pitches_deg": PITCHES, "incls_deg": INCLS,
                "snrs": SNRS, "seeds": SEEDS, "n_images": 0, "image_side": N}}

# ---- A. identity over the grid --------------------------------------------
n = exact = value_equal = 0
worst = 0.0
mm_exact = True
w_repeat_exact = True
per_image = []
for parity in PARITIES:
    for pitch in PITCHES:
        for incl in INCLS:
            for snr in SNRS:
                for seed in SEEDS:
                    x = synth_spiral(parity, pitch, incl, snr,
                                     seed=hash((parity, pitch, incl, snr, seed)) & 0x7FFFFFFF)
                    m = mirror(x)
                    c1, c2 = chi(x), chi(m)
                    n += 1
                    bit_ok = bits(c2) == bits(-c1)
                    exact += bit_ok
                    value_equal += (c2 == -c1)
                    worst = max(worst, abs(c2 + c1))
                    mm_exact &= (mirror(m).tobytes() == x.tobytes())
                    if seed == 0:
                        w_repeat_exact &= (bits(w(x)) == bits(w(x)))
                    per_image.append({"parity": parity, "pitch": pitch, "incl": incl,
                                      "snr": snr, "seed": seed, "chi": c1,
                                      "bit_exact": bool(bit_ok)})
res["grid"]["n_images"] = n
res["A_identity"] = {
    "bit_exact_count": exact, "of": n,
    "value_equal_count": value_equal,
    "max_abs_chi_m_plus_chi": worst,
    "mirror_mirror_bit_identical_all": bool(mm_exact),
    "w_deterministic_on_repeat": bool(w_repeat_exact),
}

# ---- B. signed-zero edge case on an exactly symmetric image ----------------
sym = synth_disk(30.0, 1e9, seed=7)          # armless: w(x) == w(mirror(x)) candidates
sym = (sym + mirror(sym)) / 2.0              # force exact mirror symmetry
c_sym, c_msym = chi(sym), chi(mirror(sym))
res["B_signed_zero"] = {
    "chi_symmetric_image": c_sym,
    "chi_of_its_mirror": c_msym,
    "neg_chi_bits": hex(bits(-c_sym)),
    "chi_mirror_bits": hex(bits(c_msym)),
    "bit_exact": bits(c_msym) == bits(-c_sym),
    "value_equal": c_msym == -c_sym,
}

# ---- C. broken mirror: interpolating reflection ---------------------------
try:
    from scipy.ndimage import affine_transform

    def bad_mirror(img):
        # reflection about a line 0.25 px off the array centreline -> forces resampling
        return affine_transform(img, [[1.0, 0.0], [0.0, -1.0]],
                                offset=[0.0, (N - 1) + 0.5], order=1, mode="nearest")

    viol = []
    for parity in PARITIES:
        for snr in (5.0, 50.0):
            x = synth_spiral(parity, 25.0, 25.0, snr, seed=11)
            viol.append(abs(chi(bad_mirror(x)) + chi(x)))
    res["C_broken_mirror"] = {
        "transform": "affine reflection displaced 0.25 px from the grid centreline, "
                     "bilinear interpolation (order=1)",
        "abs_violation_min": min(viol), "abs_violation_max": max(viol),
        "n_cases": len(viol),
    }
except ImportError:
    res["C_broken_mirror"] = {"skipped": "scipy unavailable"}

# ---- E. tau calibration + abstention on synthetics ------------------------
null_chi = []
for incl in INCLS:
    for snr in SNRS:
        for seed in range(12):
            null_chi.append(abs(chi(synth_disk(incl, snr, seed=1000 + seed))))
null_chi = np.array(null_chi)
tau = float(np.quantile(null_chi, 0.995))

sp = [p for p in per_image]
accept = [p for p in sp if abs(p["chi"]) > tau]
correct = [p for p in accept if np.sign(p["chi"]) == np.sign(p["parity"])]
by_snr = {}
for snr in SNRS:
    g = [p for p in sp if p["snr"] == snr]
    a = [p for p in g if abs(p["chi"]) > tau]
    c = [p for p in a if np.sign(p["chi"]) == np.sign(p["parity"])]
    by_snr[str(snr)] = {"abstention": 1 - len(a) / len(g),
                        "sign_accuracy_accepted": (len(c) / len(a)) if a else None}

# dA_raw: the raw estimator's own flip-imbalance (brief §3), on the full spiral grid
sgn_sum = []
for parity in PARITIES:
    for pitch in PITCHES:
        for incl in INCLS:
            for snr in SNRS:
                for seed in SEEDS:
                    x = synth_spiral(parity, pitch, incl, snr,
                                     seed=hash((parity, pitch, incl, snr, seed)) & 0x7FFFFFFF)
                    sgn_sum.append((np.sign(w(x)) + np.sign(w(mirror(x)))) / 2.0)
res["E_calibration"] = {
    "tau_frozen_from": "99.5th percentile of |chi| on 240 armless-disk nulls (synthetic only)",
    "tau": tau,
    "overall_abstention_spirals": 1 - len(accept) / len(sp),
    "overall_sign_accuracy_accepted": len(correct) / len(accept) if accept else None,
    "by_snr": by_snr,
    "dA_raw_mean": float(np.mean(sgn_sum)),
    "dA_raw_note": "mean(sign(w(x))+sign(w(mirror(x))))/2 over all synthetic spirals — "
                   "the raw estimator's own flip-imbalance before antisymmetrization",
}

json.dump(res, open(OUT, "w"), indent=1)
print(json.dumps({k: v for k, v in res.items() if k != "grid"}, indent=1)[:2400])
print("n_images:", n)
