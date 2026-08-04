import numpy as np
# Paper B: massive-galaxy abundance vs TNG. Excess is "erased" by a downward stellar-mass
# shift dlogM = log10(f) / |s|, where f = observed/TNG number-density ratio at fixed M*,
# and s = dlog n / dlog M* (massive-end SMF slope). Systematic M* budget ~1 dex (DR2 consensus).
BUDGET = 1.0   # dex, plausible M* systematic budget (SED spread, IMF, LRD/AGN, Eddington bias)

# Observed excess factors across redshift (from B's cited data):
excess = {"z~5-6 (Weibel, ~2.7x)": 2.7, "z~7-9 (Labbe candidates, ~13x)": 13.0,
          "conservative 2x": 2.0, "extreme 20x": 20.0}
# Massive-end simulated SMF slope range (steeper -> easier to erase)
slopes = [-1.4, -1.6, -1.8, -2.0]

print("dlogM* required to erase the excess (dex);  * = within ~1 dex budget")
print(f"{'excess':30s} " + " ".join(f"s={s:+.1f}" for s in slopes))
for lab,f in excess.items():
    row=[]
    for s in slopes:
        dM = np.log10(f)/abs(s)
        row.append(f"{dM:5.2f}{'*' if dM<=BUDGET else ' '}")
    print(f"{lab:30s} " + " ".join(f"{r:>6s}" for r in row))

print("\nInterpretation:")
for lab,f in excess.items():
    worst = np.log10(f)/1.4  # shallowest slope = hardest to erase
    verdict = "WITHIN budget (no robust tension)" if worst<=BUDGET else "EXCEEDS budget (residual tension)"
    print(f"  {lab:30s}: worst-case dlogM={worst:.2f} dex -> {verdict}")
