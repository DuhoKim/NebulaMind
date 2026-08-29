#!/usr/bin/env python3
"""Pre-commit control for this lane. RUN THIS BEFORE EVERY COMMIT.

Built after defect 1ag: the negative-assertion sweep existed but lived somewhere I had to remember,
and a control that is not invoked is indistinguishable from no control.

WRITTEN AS .py DELIBERATELY. The first version was check.sh and git silently ignored it: the repo's
.gitignore takes the whole .hermes tree and re-admits it by extension -- .md, .json, .txt, .html,
.yaml, .yml, .py, .tex. NOT .sh. So a control written as a shell script is invisible to every fresh
clone: present on this disk, absent from the repository, which is the SAME defect one level down.
Changing the shared ignore rule would touch other lanes; using a tracked file type costs nothing.

Two earlier defects are built in rather than written down nearby:
  1ac -- no GNU-only tools. The runner that reported "31 of 31 FAILED" wrapped everything in
         `timeout`, which macOS does not have.
  1ac -- ABORTS if zero scripts pass, because a run with no green line is reporting on itself.
"""
import os, re, subprocess, sys
HERE=os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

scripts=sorted(f for f in os.listdir(".") if re.match(r"^[ab]\d+.*\.py$", f))
ok=[]; bad=[]
for f in scripts:
    r=subprocess.run([sys.executable,f],capture_output=True)
    (ok if r.returncode==0 else bad).append(f)
print(f"battery: passed={len(ok)} failed={len(bad)}" + (f" | failing: {' '.join(bad)}" if bad else ""))
if not ok:
    print("ABORT: zero scripts passed. That is a runner fault, not "
          f"{len(scripts)} broken scripts."); sys.exit(2)

# 1ab/1ag: a chk() asserting a NEGATIVE about the record is a defect waiting to fire, because these
# scripts document a gap and close it in the same session -- so "the gap is present" is guaranteed
# to be falsified by the work the script exists to justify.
NEG=re.compile(r"(==\s*0|\bnot in\b|is None)")
flagged=[]
for f in scripts:
    src=open(f).read()
    for m in re.finditer(r"chk\(\s*(\"|')", src):
        i=m.start()+4; depth=0; j=i
        while j < len(src):
            if src[j]=="(": depth+=1
            elif src[j]==")":
                depth-=1
                if depth==0: break
            j+=1
        call=src[i:j]
        if NEG.search(call) and re.search(r"BIB|bibliograph", call):
            flagged.append((f, call.split("\n")[0][:70]))
print(f"negative-assertion sweep: {len(flagged)} check(s) assert a negative about the record")
for f,c in flagged: print(f"   {f:<34} {c}")
print("   (each must assert the REPAIRED state or a durable artifact -- never the gap)")
sys.exit(1 if bad else 0)
