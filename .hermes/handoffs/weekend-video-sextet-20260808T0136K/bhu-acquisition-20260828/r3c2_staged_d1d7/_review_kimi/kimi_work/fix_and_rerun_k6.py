import pathlib, subprocess
D2 = pathlib.Path("out/m3src")
(D2/"bt1.txt").write_text("bt1\nIntro.\nWe take q = 9 from bt3\n")
(D2/"bt3.txt").write_text("bt3\nq = 9 here.\n")
SEAT = "../../r3c2_ledger_tools_STAGED.py"
r = subprocess.run(["/usr/bin/python3","-E",SEAT,"validate","out/k6seat/ledger_b1.json","out/m3src"],capture_output=True,text=True)
print("$ /usr/bin/python3 -E r3c2_ledger_tools_STAGED.py validate out/k6seat/ledger_b1.json out/m3src")
print(r.stdout+r.stderr)
print("[exit",r.returncode,"]")
