import io,sys,re
# V38: r3c2_manifest.py gains an explicit completion token on every exit path (codex V37 F3-continued).
p=sys.argv[1]; s=io.open(p,encoding="utf-8").read()
if "MANIFEST=PASS" in s: print("manifest token already present"); sys.exit(0)
lines=s.split("\n"); n=0
for i,l in enumerate(lines):
    if "sys.exit(1)" in l and "MANIFEST=FAIL" not in l and ("ERROR=" in l or "INCOMPLETE" in l):
        lines[i]=l.replace("sys.exit(1)",'print("MANIFEST=FAIL"), sys.exit(1)' if "onerror=lambda" in l else 'print("MANIFEST=FAIL"); sys.exit(1)'); n+=1
    elif "sys.exit(1)" in l and "MANIFEST=FAIL" not in l and "symlink" in l:
        lines[i]=l.replace("sys.exit(1)",'print("MANIFEST=FAIL"); sys.exit(1)'); n+=1
    elif "sys.exit(0)" in l and "MANIFEST=PASS" not in l:
        lines[i]=l.replace("sys.exit(0)",'print("MANIFEST=PASS"); sys.exit(0)'); n+=1
s="\n".join(lines); io.open(p,"w",encoding="utf-8").write(s); print(f"manifest completion token added at {n} exit paths")
