#!/usr/bin/env python3
"""Build frozen per-cluster centroids in the native 2560-d embedding space, for
cheap incremental nearest-centroid assignment of new papers. Read-only on the
frozen snapshot; writes centroids_v2.npy + centroids_meta.json. Also calibrates
the assign / drift thresholds from the member-to-own-centroid cosine distribution."""
import json, numpy as np, os
ENG=os.path.dirname(os.path.abspath(__file__))
meta=json.load(open(f"{ENG}/embed_meta.json")); N,D=meta["n"],meta["dim"]
X=np.memmap(f"{ENG}/emb_qwen4b.f32",dtype=np.float32,mode="r",shape=(N,D))
bibs=json.load(open(f"{ENG}/bibcodes.json")); idx={b:i for i,b in enumerate(bibs)}
labels=json.load(open(f"{ENG}/cluster_labels_v2.json"))
clusters=sorted({c for c in labels.values() if c!=-1})
cents=np.zeros((len(clusters),D),np.float32); order=[]
memcos={}  # per-cluster member-to-centroid cosine distribution
for k,c in enumerate(clusters):
    rows=[idx[b] for b,l in labels.items() if l==c and b in idx]
    V=np.asarray(X[rows],np.float32); V/= (np.linalg.norm(V,axis=1,keepdims=True)+1e-9)
    m=V.mean(0); m/= (np.linalg.norm(m)+1e-9); cents[k]=m; order.append(int(c))
    memcos[int(c)]=(V@m)
np.save(f"{ENG}/centroids_v2.npy",cents)
# calibrate: TAU_ASSIGN ~ 10th pct of member cosines (global), TAU_DRIFT ~ 3rd pct
allcos=np.concatenate(list(memcos.values()))
tau_assign=float(np.percentile(allcos,10)); tau_drift=float(np.percentile(allcos,3))
percl={str(c):{"n":int(len(v)),"p10":round(float(np.percentile(v,10)),3),
               "p50":round(float(np.median(v)),3)} for c,v in memcos.items()}
json.dump({"n_clusters":len(clusters),"dim":D,"order":order,
           "tau_assign":round(tau_assign,3),"tau_drift":round(tau_drift,3),
           "structure_as_of":"2026-07-18","note":"centroids in native 2560-d; nearest-centroid assign is an approximation of the UMAP+HDBSCAN manifold clustering — drift only FLAGS for a supervised re-cluster."},
          open(f"{ENG}/centroids_meta.json","w"),indent=1)
print(f"centroids_v2.npy: {cents.shape}  TAU_ASSIGN={tau_assign:.3f}  TAU_DRIFT={tau_drift:.3f}")
print("global member-cosine: p50=%.3f p10=%.3f p3=%.3f"%(np.median(allcos),tau_assign,tau_drift))
