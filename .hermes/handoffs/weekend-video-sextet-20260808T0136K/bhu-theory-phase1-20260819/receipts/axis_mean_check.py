"""Receipt: the paper's mean preferred axis alpha=197+-47, delta=34+-3 from the three cited
fitted axes (217,32), (132,32), (243,39); JADES (gal4) supplies no axis. Also Eq (7)-(8):
angle between (197,34) and the SMAC bulk-flow apex (128,-41)."""
import numpy as np
alphas = np.array([217.0, 132.0, 243.0]); deltas = np.array([32.0, 32.0, 39.0])
print(f"mean alpha = {alphas.mean():.1f} (paper: 197);  mean delta = {deltas.mean():.1f} (paper: 34)")
print(f"population std alpha = {alphas.std(ddof=0):.1f} (paper: +-47); std of mean = {alphas.std(ddof=1)/np.sqrt(3):.1f}")
print(f"population std delta = {deltas.std(ddof=0):.1f} (paper: +-3)")
def unit(a, d):
    a, d = np.radians(a), np.radians(d)
    return np.array([np.cos(d)*np.cos(a), np.cos(d)*np.sin(a), np.sin(d)])
S = sum(np.outer(unit(a, d), unit(a, d)) for a, d in zip(alphas, deltas))
w, V = np.linalg.eigh(S)
ax = V[:, -1]
ra = np.degrees(np.arctan2(ax[1], ax[0])) % 360
dec = np.degrees(np.arcsin(ax[2]/np.linalg.norm(ax)))
print(f"proper 3D axial mean: alpha = {ra:.1f}, delta = {dec:.1f} (vs naive per-coordinate 197.3, 34.3)")
a1, d1, a2, d2 = map(np.radians, (197.0, 34.0, 128.0, -41.0))
cosc = np.sin(d1)*np.sin(d2) + np.cos(d1)*np.cos(d2)*np.cos(a1 - a2)
print(f"cos c = {cosc:.3f} (paper: -0.143);  c = {np.degrees(np.arccos(cosc)):.1f} deg (paper: 98.2)")
