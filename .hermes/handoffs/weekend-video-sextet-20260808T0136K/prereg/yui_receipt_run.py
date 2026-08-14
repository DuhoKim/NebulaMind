import hashlib, json, sys
import numpy as np
sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/yui_identity")
from w_chi import synth_spiral, synth_disk, mirror, w, N

M = "LONGO-AMPLITUDE-FREEZE-M1"
def seed(i): return int.from_bytes(hashlib.sha256(f"{M}||{i}".encode()).digest()[:8], "big") % (2**63)
def params(i):
    r = np.random.default_rng(seed(i))
    return (int(r.choice([1,-1])), float(r.uniform(10,40)), float(r.uniform(0,60)),
            float(np.exp(r.uniform(np.log(2),np.log(50)))))
def manifest(tag, idxs, gen):
    h = hashlib.sha256()
    for i in idxs: h.update(hashlib.sha256(gen(i).astype(np.float64).tobytes()).digest())
    return {"tag": tag, "n": len(idxs), "manifest_sha256": h.hexdigest()}

res = {"master_seed": M}
res["train_manifest"] = manifest("train-20000", range(20000),
    lambda i: synth_spiral(*params(i), seed=seed(i)))
null_imgs = lambda i: synth_disk(params(i)[2], params(i)[3], seed=seed(1_000_000+i))
res["null_manifest"] = manifest("null-8000", range(8000), null_imgs)
res["heldout_manifest"] = manifest("heldout-12000", range(12000),
    lambda i: synth_spiral(*params(2_000_000+i), seed=seed(2_000_000+i)))

# tau on nulls (secondary deterministic instrument, float64 spike path)
chi = lambda x: (w(x) - w(mirror(x)))/2.0
null_abs = np.array([abs(chi(null_imgs(i))) for i in range(8000)])
tau = float(np.quantile(null_abs, 0.995))
# retention on heldout, per S/N bin
edges = [2,5,10,20,50.0001]; bins = {f"{edges[k]}-{edges[k+1]:.0f}": [0,0] for k in range(4)}
acc_tot = n_tot = 0
for i in range(12000):
    p = params(2_000_000+i); x = synth_spiral(*p, seed=seed(2_000_000+i))
    a = abs(chi(x)) > tau; n_tot += 1; acc_tot += a
    for k in range(4):
        if edges[k] <= p[3] < edges[k+1]:
            bins[list(bins)[k]][1] += 1; bins[list(bins)[k]][0] += a; break
r_hat = acc_tot/n_tot
z = 1.6449  # one-sided 95% Wilson lower bound
den = 1+z*z/n_tot; ctr = r_hat + z*z/(2*n_tot)
lo = (ctr - z*np.sqrt(r_hat*(1-r_hat)/n_tot + z*z/(4*n_tot*n_tot)))/den
res["secondary_retention"] = {"tau": tau, "retention_central": r_hat,
    "retention_lower95": float(lo), "n": n_tot,
    "by_snr": {k: {"retention": (v[0]/v[1] if v[1] else None), "n": v[1]} for k,v in bins.items()}}

# receipts on production raster + float32 inference dtype
def chi32(x):
    x32 = x.astype(np.float32)
    return (np.float32(w(x32)) - np.float32(w(mirror(x32)))) / np.float32(2.0)
b32 = lambda f: int(np.float32(f).view(np.uint32))
r1 = r2 = 0
for i in range(200):
    x = synth_spiral(*params(3_000_000+i), seed=seed(3_000_000+i)).astype(np.float32)
    r1 += (mirror(mirror(x)).tobytes() == x.tobytes())
    r2 += (b32(chi32(x if False else np.fliplr(x))) == b32(np.float32(-chi32(x))))
sym = synth_disk(30.0, 1e9, seed=7); sym = ((sym+mirror(sym))/2).astype(np.float32)
c = chi32(sym); cm = chi32(np.fliplr(sym))
res["receipts_production_raster_float32"] = {
    "R1_mirror_involution_byte_exact": f"{r1}/200",
    "R2_antisymmetry_bit_exact": f"{r2}/200",
    "R3_signed_zero": {"chi_sym": float(c), "chi_mirror_bits": hex(b32(cm)),
        "neg_chi_bits": hex(b32(np.float32(-c))), "value_equal": bool(cm == -c),
        "bit_equal": b32(cm) == b32(np.float32(-c))}}
out = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/receipt_results.json"
json.dump(res, open(out,"w"), indent=1)
print(json.dumps({k:v for k,v in res.items() if "manifest" not in k}, indent=1))
