import json, pathlib, subprocess
K = pathlib.Path(__file__).resolve().parent
H = K.parent
W = K / "work"
SEAT = H / "r3c2_ledger_tools_STAGED.py"
PY = "/usr/bin/python3"

def run(*a):
    r = subprocess.run([PY, "-E", str(SEAT), *[str(x) for x in a]], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr

# attack v2: custodian-side cooperation. Seedless selection (correct digests retained,
# audited/sampled emptied, k zeroed) + a FRESH stage-2 seal over the empty re-derivation file.
s2new = W / "b_stage2_attack.txt"
rc, out = run("audit", "seal-rederivation", W / "b_rd_empty.json", s2new)
print("seal-rederivation over empty rd rc:", rc, out.strip().splitlines()[:1])
rc, out = run("audit", "compare", W / "b_stage1.txt", W / "b_aud_c.json", W / "b_aud_x.json",
              W / "b_sealed_c.json", W / "b_sealed_x.json", W / "f_sealed_l.json",
              W / "b_sel_seedless.json", s2new, W / "b_rd_empty.json", W / "b_C6_seedless2.json")
print("ATTACK v2 (seedless selection, seals all matching) rc:", rc)
for l in out.splitlines():
    if l.startswith("FAIL:") or l.startswith("C6_AUDIT_SAMPLE"):
        print(l)
art = json.loads((W / "b_C6_seedless2.json").read_text())
print("artefact: audited =", art["audited"], "| C6_AUDIT_SAMPLE =", art["C6_AUDIT_SAMPLE"])
print("selection recorded in artefact:", json.dumps(art["selection"], sort_keys=True))

# control v2b: same but audited_ids lists a claim with no re-derivation supplied (seedless too)
selx = json.loads((W / "b_sel_seedless.json").read_text())
selx["audited_ids"] = ["c1"]   # claim an audit happened, supply nothing
selx_p = W / "b_sel_seedless_claim.json"
selx_p.write_text(json.dumps(selx, indent=1, sort_keys=True))
rc, out = run("audit", "compare", W / "b_stage1.txt", W / "b_aud_c.json", W / "b_aud_x.json",
              W / "b_sealed_c.json", W / "b_sealed_x.json", W / "f_sealed_l.json",
              selx_p, s2new, W / "b_rd_empty.json", W / "b_C6_seedless3.json")
print("CONTROL v2b (seedless, claims c1 audited but no re-derivation) rc:", rc)
for l in out.splitlines():
    if l.startswith("FAIL:") or l.startswith("C6_AUDIT_SAMPLE"):
        print(l)
