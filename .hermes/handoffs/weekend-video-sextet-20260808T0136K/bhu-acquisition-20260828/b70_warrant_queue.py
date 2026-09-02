#!/usr/bin/env python3
"""B70 -- warrant-audit queue (WARRANT_AUDIT_PREREG_20260903.md). Reuses b69's frame, mapping and density; a
warrant receipt is WARRANT_<n>_*.md in this directory. Moves no tier."""
import os, re, json, importlib.util
_HERE=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location("b69", os.path.join(_HERE,"b69_depth_queue.py"))
src=open(os.path.join(_HERE,"b69_depth_queue.py")).read()
# reuse FRAME, MAP, NO_TEXT, Q, SRC by exec of the definitions only (up to the checks)
ns={"__file__": os.path.join(_HERE,"b69_depth_queue.py")}; exec(src.split("checks=[]")[0], ns)
FRAME,MAP,NO_TEXT,SRC=ns["FRAME"],ns["MAP"],ns["NO_TEXT"],ns["SRC"]
Q=re.compile(r"\d[\d.,]*\s*(M☉|M_\{?\\?odot|Msun|Mpc|kpc|Gpc|km|GeV|MeV|eV|K\b|σ|sigma|%|Gyr|yr|cm|kg|Hz)|[=<>≃≈≲≳]\s*-?\d")   # same density regex as b69
files=set(os.listdir(_HERE))
def warranted(n): return any(re.match(rf"^WARRANT_{n}_",f) for f in files)
CAL=[7,31,51,44,1]
rows=[]; unmapped=[]
for n in FRAME:
    if n not in MAP: unmapped.append((n,NO_TEXT.get(n,"no mapping"))); continue
    f,tok=MAP[n]; p=os.path.join(SRC,f)
    if not os.path.exists(p): unmapped.append((n,"file missing")); continue
    lines=open(p,encoding="utf-8",errors="replace").read().split("\n")
    q=sum(1 for l in lines if Q.search(l)); rows.append((n, warranted(n), 100.0*q/max(1,len(lines)), f))
queue=[r for r in rows if not r[1]]
queue=sorted([r for r in queue if r[0] in CAL], key=lambda r: CAL.index(r[0]))+sorted([r for r in queue if r[0] not in CAL], key=lambda r:(-r[2], r[0]))
done=sorted(r[0] for r in rows if r[1])
print(f"warrant audit: frame {len(FRAME)} | warranted {len(done)}: {done} | queue {len(queue)} | unmapped {[u[0] for u in unmapped]}")
for r in queue[:8]: print(f"  next: entry {r[0]:2d} density {r[2]:5.1f} {r[3]}")
json.dump({"queue":[r[0] for r in queue],"done":done,"unmapped":unmapped}, open(os.path.join(_HERE,"warrant_queue_state.json"),"w"), indent=1)
raise SystemExit(0)
