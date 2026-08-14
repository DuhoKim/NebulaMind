import hashlib, json, math, sys, time
import numpy as np, torch, torch.nn as nn
sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/spike/yui_identity")
from w_chi import synth_spiral, synth_disk, N
P="/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg"
M="LONGO-AMPLITUDE-FREEZE-M1"
def seed(i): return int.from_bytes(hashlib.sha256(f"{M}||{i}".encode()).digest()[:8],"big")%(2**63)
def params(i):
    r=np.random.default_rng(seed(i))
    return (int(r.choice([1,-1])),float(r.uniform(10,40)),float(r.uniform(0,60)),float(np.exp(r.uniform(np.log(2),np.log(50)))))
def spi(i): return synth_spiral(*params(i),seed=seed(i))
torch.manual_seed(20260812)
class Blk(nn.Module):
    def __init__(s,ci,co,st):
        super().__init__(); s.c1=nn.Conv2d(ci,co,3,st,1,bias=False); s.b1=nn.BatchNorm2d(co)
        s.c2=nn.Conv2d(co,co,3,1,1,bias=False); s.b2=nn.BatchNorm2d(co)
        s.sh=nn.Sequential() if st==1 and ci==co else nn.Sequential(nn.Conv2d(ci,co,1,st,bias=False),nn.BatchNorm2d(co))
    def forward(s,x): 
        import torch.nn.functional as F
        return F.relu(s.b2(s.c2(F.relu(s.b1(s.c1(x)))))+s.sh(x))
class Trunk(nn.Module):
    def __init__(s):
        super().__init__(); L=[nn.Conv2d(1,32,3,1,1,bias=False),nn.BatchNorm2d(32),nn.ReLU()]
        w=[32,64,128,256]
        for k in range(4):
            L+=[Blk(w[max(k-1,0)] if k else 32,w[k],1 if k==0 else 2),Blk(w[k],w[k],1)]
        s.f=nn.Sequential(*L,nn.AdaptiveAvgPool2d(1),nn.Flatten(),nn.Linear(256,1))
    def forward(s,x): return s.f(x).squeeze(-1)
dev="mps" if torch.backends.mps.is_available() else "cpu"
net=Trunk().to(dev); opt=torch.optim.Adam(net.parameters(),1e-3)
NT=20000; B=100; t0=time.time()
for ep in range(2):
    perm=np.random.default_rng(1000+ep).permutation(NT)
    for bi in range(NT//B):
        idx=perm[bi*B:(bi+1)*B]
        xs=np.stack([spi(int(i)) for i in idx]).astype(np.float32)
        ys=np.array([params(int(i))[0] for i in idx],dtype=np.float32)
        x=torch.from_numpy(xs)[:,None].to(dev)
        z=net(x)-net(torch.flip(x,dims=[3]))            # chi_net*2
        loss=nn.functional.softplus(-torch.from_numpy(ys).to(dev)*z).mean()
        opt.zero_grad(); loss.backward(); opt.step()
net.eval().cpu(); torch.set_num_threads(1)
def chi_net(a32):
    with torch.no_grad():
        x=torch.from_numpy(a32)[None,None]
        return np.float32((net(x).item()-net(torch.flip(x,dims=[3])).item())/2.0)
def gen32(g): return g.astype(np.float32)
nul=lambda i: synth_disk(params(i)[2],params(i)[3],seed=seed(1_000_000+i))
na=np.array([abs(chi_net(gen32(nul(i)))) for i in range(8000)])
tau=float(np.quantile(na,0.995))
edges=[2,5,10,20,50.0001]; bins={f"{edges[k]}-{int(edges[k+1])}":[0,0,0] for k in range(4)}
acc=n=corr=0
for i in range(12000):
    p=params(2_000_000+i); c=chi_net(gen32(synth_spiral(*p,seed=seed(2_000_000+i))))
    a=abs(c)>tau; n+=1; acc+=a
    if a and np.sign(c)==p[0]: corr+=1
    for k in range(4):
        if edges[k]<=p[3]<edges[k+1]:
            key=list(bins)[k]; bins[key][1]+=1; bins[key][0]+=a
            if a and np.sign(c)==p[0]: bins[key][2]+=1
            break
r=acc/n; z=1.6449; den=1+z*z/n
lo=((r+z*z/(2*n))-z*math.sqrt(r*(1-r)/n+z*z/(4*n*n)))/den
b32=lambda f:int(np.float32(f).view(np.uint32))
r1=r2=0
for i in range(200):
    x=gen32(synth_spiral(*params(3_000_000+i),seed=seed(3_000_000+i)))
    r1+=(np.fliplr(np.fliplr(x)).tobytes()==x.tobytes())
    r2+=(b32(chi_net(np.ascontiguousarray(np.fliplr(x))))==b32(np.float32(-chi_net(x))))
sym=synth_disk(30.0,1e9,seed=7); sym=gen32((sym+np.fliplr(sym))/2)
c0=chi_net(sym); cm=chi_net(np.ascontiguousarray(np.fliplr(sym)))
wh=hashlib.sha256(b"".join(p.detach().numpy().astype("<f4").tobytes() for p in net.parameters())).hexdigest()
res={"train_minutes":round((time.time()-t0)/60,1),"device":dev,"tau":tau,
 "retention_central":r,"retention_lower95_one_sided":lo,"n_heldout":n,
 "sign_accuracy_accepted":(corr/acc if acc else None),
 "by_snr":{k:{"retention":v[0]/v[1] if v[1] else None,"n":v[1],
              "sign_acc":(v[2]/v[0] if v[0] else None)} for k,v in bins.items()},
 "weights_sha256_canonical":wh,
 "receipts_float32":{"R1":f"{r1}/200","R2":f"{r2}/200",
   "R3":{"chi_sym":float(c0),"mirror_bits":hex(b32(cm)),"neg_bits":hex(b32(np.float32(-c0))),
         "value_equal":bool(cm==-c0)}}}
json.dump(res,open(P+"/train_results.json","w"),indent=1)
torch.save(net.state_dict(),P+"/weights_frozen.pt")
res["weights_file_sha256"]=hashlib.sha256(open(P+"/weights_frozen.pt","rb").read()).hexdigest()
json.dump(res,open(P+"/train_results.json","w"),indent=1)
print(json.dumps(res,indent=1))
