import json, pathlib
W = pathlib.Path(__file__).resolve().parent / "work"
log = json.loads((W / "command_log.json").read_text())
for e in log:
    if any("b_sel_seedless" in c for c in e["cmd"]):
        print("CMD tail:", " ".join(e["cmd"][-10:]))
        print("RC:", e["rc"])
        for l in e["stdout"].splitlines():
            if l.startswith("FAIL:") or l.startswith("C6_AUDIT_SAMPLE"):
                print(l)
art = json.loads((W / "b_C6_seedless.json").read_text())
print("artefact C6_AUDIT_SAMPLE:", art["C6_AUDIT_SAMPLE"])
print("artefact audited:", art["audited"])
print("artefact selection:", json.dumps(art["selection"], sort_keys=True))
