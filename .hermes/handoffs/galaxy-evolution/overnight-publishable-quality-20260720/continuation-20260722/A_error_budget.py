import numpy as np
rng = np.random.default_rng(20260722)  # fixed seed (Date.now-free, reproducible)

# Pollock+2026 unlensed direct-Te sample (Paper A core), read from run CSV values
# id, z, logM, logM_err, OH, OH_err
pts = [
    ("CAPERS-EGS-25297", 9.9381, 8.39, 0.03, 7.69, 0.08),
    ("JADES-GS-265801",  9.4437, 8.30, 0.03, 7.61, 0.04),
    ("CAPERS-EGS-87132", 9.3833, 8.19, 0.14, 7.53, 0.17),
    ("JADES-GN-3990",    9.3812, 8.59, 0.15, 7.57, 0.11),
    ("CAPERS-UDS-22431", 9.2717, 8.30, 0.04, 7.81, 0.11),
]
logM = np.array([p[2] for p in pts]); logM_err = np.array([p[3] for p in pts])
OH   = np.array([p[4] for p in pts]); OH_err   = np.array([p[5] for p in pts])

# Local anchor MZR predictions (published functional forms)
def curti20(lm):  # Curti+2020 MNRAS 491,944
    Z0, logM0, gamma, beta = 8.793, 10.02, 0.28, 1.2
    return Z0 - (gamma/beta)*np.log10(1 + (10**(lm-logM0))**(-beta))
def am13(lm):     # Andrews & Martini 2013 (direct-Te, measured to logM~7.4)
    Z0, logMTO, g = 8.798, 8.901, 0.640
    return Z0 - np.log10(1 + (10**logMTO/10**lm)**g)

def deficit(anchor, lm=logM, oh=OH):
    return oh - anchor(lm)

d_curti = deficit(curti20); d_am13 = deficit(am13)
mean_c, mean_a = d_curti.mean(), d_am13.mean()
print("Per-point deficit vs Curti20 :", np.round(d_curti,3))
print("Per-point deficit vs AM13    :", np.round(d_am13,3))
print(f"Population mean deficit: Curti20={mean_c:+.3f}  AM13={mean_a:+.3f}  anchor spread={abs(mean_c-mean_a):.3f} dex")

# ---- Full error budget on the POPULATION mean deficit (vs Curti20 baseline) ----
N = len(OH)
# (1) measurement: propagate OH_err and logM_err (via local MZR slope) into each point's deficit
slope_c = (curti20(logM+1e-3)-curti20(logM-1e-3))/2e-3   # dOH/dlogM of anchor at each mass
sig_meas_pt = np.sqrt(OH_err**2 + (slope_c*logM_err)**2)
sig_mean_meas = np.sqrt(np.sum(sig_meas_pt**2))/N          # measurement error on the mean
# (2) sample variance (intrinsic scatter of the 5 deficits about their mean)
samp_sd = d_curti.std(ddof=1); sig_mean_samp = samp_sd/np.sqrt(N)
# (3) leave-one-out spread (robustness of the mean)
loo = np.array([np.delete(d_curti,i).mean() for i in range(N)])
loo_spread = loo.max()-loo.min()
# (4) anchor-choice systematic (Curti20 vs AM13)
sig_anchor = abs(mean_c-mean_a)
# (5) absolute Te-scale zero-point (literature-debated), treat as 0.15 dex 1-sigma common shift
sig_Te = 0.15

# Statistical error on the mean (meas + sample, added in quadrature is double counting;
# use the larger, standard-error-of-mean from the data itself = sig_mean_samp, and report meas separately)
sig_stat = sig_mean_samp
# Combined systematic (anchor + Te scale)
sig_syst = np.sqrt(sig_anchor**2 + sig_Te**2)
sig_total = np.sqrt(sig_stat**2 + sig_syst**2)

# Bootstrap CI on the mean deficit (resample the 5 points w/ replacement, add per-point meas noise)
B=20000; boots=[]
for _ in range(B):
    idx = rng.integers(0,N,N)
    oh_b = OH[idx] + rng.normal(0,OH_err[idx])
    lm_b = logM[idx] + rng.normal(0,logM_err[idx])
    boots.append((oh_b - curti20(lm_b)).mean())
boots=np.array(boots); ci=np.percentile(boots,[2.5,50,97.5])

# Effective significance including the Te-scale systematic (matches E8 method)
eff_sigma = abs(mean_c)/sig_total

print("\n=== SYSTEMATIC ERROR BUDGET (population mean deficit, Curti20 baseline) ===")
print(f"  central deficit                 : {mean_c:+.3f} dex")
print(f"  (1) measurement (on mean)       : {sig_mean_meas:.3f} dex")
print(f"  (2) sample variance (SEM)       : {sig_mean_samp:.3f} dex   [intrinsic scatter {samp_sd:.3f}]")
print(f"  (3) leave-one-out spread        : {loo_spread:.3f} dex")
print(f"  (4) anchor choice (Curti/AM13)  : {sig_anchor:.3f} dex")
print(f"  (5) absolute Te scale (0.15)    : {sig_Te:.3f} dex   <-- dominant")
print(f"  statistical (SEM)               : {sig_stat:.3f} dex")
print(f"  systematic (anchor+Te)          : {sig_syst:.3f} dex")
print(f"  TOTAL                           : {sig_total:.3f} dex")
print(f"  bootstrap 95% CI on mean        : [{ci[0]:+.3f}, {ci[2]:+.3f}] (median {ci[1]:+.3f})")
print(f"  P(deficit<0) bootstrap          : {(boots<0).mean()*100:.1f}%")
print(f"  effective significance          : {eff_sigma:.1f} sigma  (sign secure; magnitude Te-limited)")
