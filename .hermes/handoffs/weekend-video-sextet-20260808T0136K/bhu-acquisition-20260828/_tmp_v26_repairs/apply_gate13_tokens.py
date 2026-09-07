import io,sys
# V38: every subcommand that serves as control evidence prints a COMPLETION TOKEN (codex V37 F3-continued: "a subcommand without a
# completion token must gain one before serving as control evidence"). Two lacked one: lane `compute` and `r3c2_manifest.py`.
lane,man=sys.argv[1],sys.argv[2]
s=io.open(lane,encoding="utf-8").read()
LANE_DONE = "COMPUTE=PASS" in s   # idempotent: the lane half may already be applied
def rl(a,b,n=1):
    if LANE_DONE: return
    global s; assert s.count(a)==n,(a[:70],s.count(a)); s=s.replace(a,b)
rl('''    for c,v in sorted(out_claims.items(),key=lambda kv:str(kv[0])): print(f"{c}\\trests_on={v['rests_on']}\\troot_origins={v['root_origins']}"+("\\tDISPUTED" if v.get("DISPUTED") else ""))
    return 0''','''    for c,v in sorted(out_claims.items(),key=lambda kv:str(kv[0])): print(f"{c}\\trests_on={v['rests_on']}\\troot_origins={v['root_origins']}"+("\\tDISPUTED" if v.get("DISPUTED") else ""))
    print("COMPUTE=PASS"); return 0''')
# every failing return of cmd_compute prints COMPUTE=FAIL
import re
out=[]
for line in s.split("\n"):
    if re.search(r'^\s+if .*print\("FAIL:.*; return 1', line) and "COMPUTE=FAIL" not in line and "def cmd_merge" not in line:
        pass
    out.append(line)
s="\n".join(out)
if not LANE_DONE:
    for a,b in [('print("FAIL: ledger carries alternative branches but no provenance_graphs (a mixed PRIMARY/ALT view is not a seat-supplied graph; compute accepts merge output)"); return 1',
                 'print("FAIL: ledger carries alternative branches but no provenance_graphs (a mixed PRIMARY/ALT view is not a seat-supplied graph; compute accepts merge output)"); print("COMPUTE=FAIL"); return 1'),
                ('print("FAIL: more than two provenance graphs"); return 1','print("FAIL: more than two provenance graphs"); print("COMPUTE=FAIL"); return 1'),
                ('print("FAIL: a provenance graph does not cover the merged input_id set"); return 1','print("FAIL: a provenance graph does not cover the merged input_id set"); print("COMPUTE=FAIL"); return 1'),
                ('if probs: [print(f"FAIL: provenance graph {gi}: {p_}") for p_ in probs]; return 1','if probs: [print(f"FAIL: provenance graph {gi}: {p_}") for p_ in probs]; print("COMPUTE=FAIL"); return 1'),
                ('except ValueError as e: print("FAIL:",e); return 1','except ValueError as e: print("FAIL:",e); print("COMPUTE=FAIL"); return 1'),
                ('if extra: print("FAIL: ledger claims that are not included candidates:",extra); return 1','if extra: print("FAIL: ledger claims that are not included candidates:",extra); print("COMPUTE=FAIL"); return 1'),
                ('if len(out_claims)!=len(inc): print(f"FAIL: rests_on rows {len(out_claims)} != included denominator {len(inc)}"); return 1','if len(out_claims)!=len(inc): print(f"FAIL: rests_on rows {len(out_claims)} != included denominator {len(inc)}"); print("COMPUTE=FAIL"); return 1')]:
        assert s.count(a)==1,("compute token",a[:60]); s=s.replace(a,b)
io.open(lane,"w",encoding="utf-8").write(s)
m=io.open(man,encoding="utf-8").read()
assert m.count("MANIFEST=PASS")==0 and m.count("MANIFEST=FAIL")==0
pairs=[('print(f"ERROR={root}: root is a symlink or not a directory (refused)"); sys.exit(1)','print(f"ERROR={root}: root is a symlink or not a directory (refused)"); print("MANIFEST=FAIL"); sys.exit(1)'),
       ('onerror=lambda e: (print(f"ERROR={e.filename}: {e.strerror}"), sys.exit(1))','onerror=lambda e: (print(f"ERROR={e.filename}: {e.strerror}"), print("MANIFEST=FAIL"), sys.exit(1))'),
       ('print(f"ERROR={os.path.relpath(os.path.join(dirpath, dn), root)}: symlinked directory (refused)"); sys.exit(1','print(f"ERROR={os.path.relpath(os.path.join(dirpath, dn), root)}: symlinked directory (refused)"); print("MANIFEST=FAIL"); sys.exit(1'),
       ('print(f"FILES={len(rows)}\nMANIFEST_SHA256=INCOMPLETE ({errors} unreadable)"); sys.exit(1)','print(f"FILES={len(rows)}\nMANIFEST_SHA256=INCOMPLETE ({errors} unreadable)"); print("MANIFEST=FAIL"); sys.exit(1)'),
       ('print(f"FILES={len(rows)}\nMANIFEST_SHA256={m}"); sys.exit(0)','print(f"FILES={len(rows)}\nMANIFEST_SHA256={m}"); print("MANIFEST=PASS"); sys.exit(0)')]
n=0
for a,b in pairs:
    if m.count(a)==1: m=m.replace(a,b); n+=1
    else: print("  manifest pattern not unique/absent:",a[:60])
i2=m.find('print(f"ERROR={os.path.relpath(p, root)}: symlink or non-regular entry')
assert i2>0
j2=m.index("sys.exit(1",i2); m=m[:i2]+m[i2:j2].replace('"); sys.exit','"); print("MANIFEST=FAIL"); sys.exit') + m[j2:] if False else m
# the remaining single-file symlink refusal
a3='symlink or non-regular entry (the manifest pins regular files only)"); sys.exit(1)'
if m.count(a3)==1: m=m.replace(a3,'symlink or non-regular entry (the manifest pins regular files only)"); print("MANIFEST=FAIL"); sys.exit(1)'); n+=1
io.open(man,"w",encoding="utf-8").write(m); print(f"completion tokens added: COMPUTE (lane), MANIFEST ({n} sites)")
