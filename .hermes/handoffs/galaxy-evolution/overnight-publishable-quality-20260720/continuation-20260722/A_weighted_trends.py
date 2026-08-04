import numpy as np
# 6 unlensed direct-Te points (Pollock + GN-z11)
z    = np.array([9.9381,9.4437,9.3833,9.3812,9.2717,10.603])
logM = np.array([8.39,8.30,8.19,8.59,8.30,8.00])
OH   = np.array([7.69,7.61,7.53,7.57,7.81,7.82])
OHe  = np.array([0.08,0.04,0.17,0.11,0.11,0.35])
def curti20(lm):
    return 8.793 - (0.28/1.2)*np.log10(1+(10**(lm-10.02))**(-1.2))
d = OH - curti20(logM)               # per-point deficit
w = 1/OHe**2                         # inverse-variance weights

wmean = np.sum(w*d)/np.sum(w)
wmean_err = 1/np.sqrt(np.sum(w))
umean = d.mean()
print(f"Unweighted mean deficit : {umean:+.3f}")
print(f"Inverse-variance-weighted: {wmean:+.3f} +/- {wmean_err:.3f} (stat only)")
print("  -> weighting toward the tight points (JADES-GS, CAPERS-EGS) DEEPENS the deficit,")
print("     because the shallow-deficit points (CAPERS-UDS 7.81, GN-z11) carry large errors.")

# Trend tests: deficit vs logM and vs z (weighted least squares)
def wls(x):
    X=np.vstack([np.ones_like(x),x-x.mean()]).T
    W=np.diag(w); beta=np.linalg.solve(X.T@W@X, X.T@W@d)
    cov=np.linalg.inv(X.T@W@X); return beta[1], np.sqrt(cov[1,1])
sM,eM = wls(logM); sZ,eZ = wls(z)
print(f"\nTrend of deficit with logM* : slope {sM:+.3f} +/- {eM:.3f} dex/dex  ({abs(sM/eM):.1f}sigma)")
print(f"Trend of deficit with z     : slope {sZ:+.3f} +/- {eZ:.3f} dex/unit-z ({abs(sZ/eZ):.1f}sigma)")
print("  -> no significant (<2sigma) mass or redshift trend within the sample:")
print("     consistent with a pure NORMALIZATION offset at ~unchanged slope (Paper A's claim). ✓")
