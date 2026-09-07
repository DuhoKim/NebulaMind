import io,sys,re
# V38 (codex V37 F3-continued): EVERY subcommand prints a completion token, added once per tool at the dispatcher, so no control can
# rest on output that never announced its own completion. The token names the subcommand and its exit status; nothing else changes.
def patch(path, prefix):
    s=io.open(path,encoding="utf-8").read()
    if "def _emit(" in s: print("already tokenised:",path); return
    body=s[s.index('if __name__=="__main__":'):]
    lines=body.split("\n"); out=[]
    for l in lines:
        m=re.match(r'^(\s*)if (.*?): sys\.exit\((cmd_[a-z_]+)\((.*)\)\)\s*$', l)
        if m:
            ind,cond,fn,args=m.groups()
            out.append(f'{ind}if {cond}: _emit("{prefix}_"+"_".join(x.upper() for x in a[:1] if isinstance(x,str)) if False else "{prefix}", {fn}({args}), a)')
        else: out.append(l)
    body="\n".join(out)
    body=body.replace('print(__doc__); sys.exit(2)','print(__doc__); print("INVOCATION=REJECTED"); sys.exit(2)')
    body=re.sub(r'(print\("usage: [^\n]*?"\); sys\.exit\((\d)\))', lambda mm: mm.group(1).replace("; sys.exit(", '; print("INVOCATION=REJECTED"); sys.exit('), body)
    helper='''def _emit(prefix, rc, argv):
    """V38: one completion token per subcommand run — <PREFIX>_<SUBCOMMAND>=PASS|FAIL, printed once, whatever the exit status."""
    sub="_".join(str(x).upper().replace("-","_") for x in argv[:2] if not str(x).startswith("/") and not str(x).endswith(".json") and not str(x).endswith(".md") and not str(x).endswith(".txt"))
    print(f"{prefix}_{sub}=" + ("PASS" if rc==0 else "FAIL")); sys.exit(rc)


'''
    s=s[:s.index('if __name__=="__main__":')]+helper+body
    io.open(path,"w",encoding="utf-8").write(s); print("dispatcher tokens added:",path)
patch(sys.argv[1],"SEAT"); patch(sys.argv[2],"BATCH"); patch(sys.argv[3],"LANE")
