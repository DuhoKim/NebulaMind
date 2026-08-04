#!/usr/bin/env python3
"""H11 offline derivation checks for m1_rp2_environment_quenching/analysis_results.json.
Verifies internal consistency of the artifact and nearest-rounding (RCA convention)
of every rounded numeral used in the cycle-5 supplement prose. Read-only."""
import json, math, sys

ART = sys.argv[1]
MAN = sys.argv[2]
p = json.load(open(ART))
h, l = p["high_density_quenched"], p["low_density_quenched"]
ci = p["high_minus_low_ci"]
co, se = p["lpm_high_density_coeff"], p["lpm_high_density_se"]

def ck(name, cond, detail):
    print(f"{'PASS' if cond else 'FAIL'}  {name}  [{detail}]")

ck("high fraction == k/n", abs(h["fraction"] - h["k"]/h["n"]) < 1e-12, f"{h['k']}/{h['n']}={h['k']/h['n']:.10f} vs {h['fraction']}")
ck("low  fraction == k/n", abs(l["fraction"] - l["k"]/l["n"]) < 1e-12, f"{l['k']}/{l['n']}={l['k']/l['n']:.10f} vs {l['fraction']}")
ck("high se == binomial sqrt(p(1-p)/n)", abs(h["se"] - math.sqrt(h["fraction"]*(1-h["fraction"])/h["n"])) < 1e-12, f"{h['se']:.12f}")
ck("low  se == binomial sqrt(p(1-p)/n)", abs(l["se"] - math.sqrt(l["fraction"]*(1-l["fraction"])/l["n"])) < 1e-12, f"{l['se']:.12f}")
ck("quartile n == sample_rows/4", p["sample_rows"] // 4 == h["n"] == l["n"], f"{p['sample_rows']}/4 vs {h['n']},{l['n']}")
diff = h["fraction"] - l["fraction"]
ck("point diff inside bootstrap CI", ci[0] < diff < ci[1], f"diff={diff:.6f} CI=[{ci[0]:.6f},{ci[1]:.6f}] mid={(ci[0]+ci[1])/2:.6f}")
# nearest-rounding of every supplement numeral (RCA verbatim-carry convention)
ck("SUP '0.230'  == round3(high frac)", f"{h['fraction']:.3f}" == "0.230", f"{h['fraction']}")
ck("SUP '0.181'  == round3(low frac)",  f"{l['fraction']:.3f}" == "0.181", f"{l['fraction']}")
ck("SUP '[0.041, 0.059]' == round3(CI)", (f"{ci[0]:.3f}", f"{ci[1]:.3f}") == ("0.041", "0.059"), f"[{ci[0]}, {ci[1]}]")
ck("SUP '0.032' == round3(lpm coeff)",  f"{co:.3f}" == "0.032", f"{co}")
ck("SUP '0.004' == round3(lpm se)",     f"{se:.3f}" == "0.004", f"{se}")
ck("SUP '3.2 percentage-point' == round1(100*coeff)", f"{100*co:.1f}" == "3.2", f"{100*co:.5f}")
# derived diagnostics (arithmetic on artifact fields only)
z_naive = diff / math.sqrt(h["se"]**2 + l["se"]**2)
print(f"INFO  naive two-proportion z = {z_naive:.2f} (independent-binomial approx)")
print(f"INFO  LPM z = {co/se:.2f}")
print(f"INFO  adjustment attenuation = {(1 - co/diff)*100:.1f}% (raw {diff:.4f} -> adjusted {co:.4f})")
print(f"INFO  relative excess raw = {(h['fraction']/l['fraction']-1)*100:.1f}%")

# manifest scan: entries touching the environment-quenching numerals/passages
tokens = ["0.230", "0.181", "3,456", "2,710", "0.041", "0.059", "0.032",
          "10th-neighbor", "neighbor-count", "environment", "quartile", "m1_rp2", "m1\\_rp2"]
man = json.load(open(MAN))
seen = set()
def walk(o):
    if isinstance(o, dict):
        blob = json.dumps(o, ensure_ascii=False)
        if "id" in o and any(t in blob for t in tokens):
            eid = o.get("id")
            if eid not in seen:
                seen.add(eid)
                hit = [t for t in tokens if t in blob]
                s = json.dumps({k: o[k] for k in o if k in ("id","exact_string","allowed_context","artifact_field","value","kind","type","doc","count")}, ensure_ascii=False)
                print(f"MAN  {eid}  hits={hit}  {s[:360]}")
        for v in o.values(): walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
walk(man)
