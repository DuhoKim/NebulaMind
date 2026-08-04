import numpy as np
rng = np.random.default_rng(20260722)

# 5 Pollock unlensed + GN-z11 (independent, highest-z direct-Te, Curti+2023/Cameron+2023)
base = [
    ("CAPERS-EGS-25297", 9.9381, 8.39, 0.03, 7.69, 0.08),
    ("JADES-GS-265801",  9.4437, 8.30, 0.03, 7.61, 0.04),
    ("CAPERS-EGS-87132", 9.3833, 8.19, 0.14, 7.53, 0.17),
    ("JADES-GN-3990",    9.3812, 8.59, 0.15, 7.57, 0.11),
    ("CAPERS-UDS-22431", 9.2717, 8.30, 0.04, 7.81, 0.11),
]
gnz11 = ("GN-z11", 10.603, 8.00, 0.20, 7.82, 0.35)  # unlensed, direct-Te [OIII]4363

def curti20(lm):
    Z0, logM0, gamma, beta = 8.793, 10.02, 0.28, 1.2
    return Z0 - (gamma/beta)*np.log10(1 + (10**(lm-logM0))**(-beta))

def budget(pts, label):
    logM=np.array([p[2] for p in pts]); logM_err=np.array([p[3] for p in pts])
    OH=np.array([p[4] for p in pts]);   OH_err=np.array([p[5] for p in pts])
    N=len(OH)
    d=OH-curti20(logM); mean=d.mean()
    slope=(curti20(logM+1e-3)-curti20(logM-1e-3))/2e-3
    sem=d.std(ddof=1)/np.sqrt(N)
    loo=np.array([np.delete(d,i).mean() for i in range(N)]); loo_spread=loo.max()-loo.min()
    sig_Te=0.15; sig_anchor=0.040
    sig_total=np.sqrt(sem**2+sig_anchor**2+sig_Te**2)
    B=20000; boot=[]
    for _ in range(B):
        i=rng.integers(0,N,N)
        boot.append(((OH[i]+rng.normal(0,OH_err[i]))-curti20(logM[i]+rng.normal(0,logM_err[i]))).mean())
    boot=np.array(boot); ci=np.percentile(boot,[2.5,97.5])
    print(f"[{label}] N={N}  mean deficit={mean:+.3f}  SEM={sem:.3f}  LOO_spread={loo_spread:.3f}"
          f"  total_err={sig_total:.3f}  95%CI=[{ci[0]:+.3f},{ci[1]:+.3f}]  P(<0)={ (boot<0).mean()*100:.1f}%"
          f"  eff_sigma={abs(mean)/sig_total:.1f}")
    return mean,d

print("GN-z11 deficit vs Curti20:", round((7.82-curti20(np.array([8.0]))[0]),3), "dex (large err ±0.35)")
budget(base, "Pollock-only")
budget(base+[gnz11], "Pollock + GN-z11")
