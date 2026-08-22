import csv, math, os
RA_L, DEC_L = 216.984434295527, 32.060611193471
rl, dl = math.radians(RA_L), math.radians(DEC_L)
p = os.path.join(os.path.dirname(__file__), "..", "_positions_20260820", "positions_parent_20260820.csv")
s = s2 = 0.0; n = 0
with open(p) as f:
    for r in csv.DictReader(f):
        ra, dec = math.radians(float(r["ra"])), math.radians(float(r["dec"]))
        c = math.sin(dec)*math.sin(dl) + math.cos(dec)*math.cos(dl)*math.cos(ra-rl)
        s += c; s2 += c*c; n += 1
print(f"{s2/n - (s/n)**2:.6f}")
