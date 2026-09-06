import io,sys
# V34 (codex V33 F1): merge serialises its output with sorted object keys (recursively, json.dumps sort_keys), so the merged bytes
# cannot expose the first-supplied seat's member order when canonical keys tie. Single enforcement point unchanged: merge.
p=sys.argv[1] if len(sys.argv)>1 else "r3c2_lane_tools.py"; s=io.open(p,encoding="utf-8").read()
a='pathlib.Path(out).write_text(json.dumps({"records":out_recs},indent=1)); print(f"merged {len(out_recs)} records; origin disagreements={ndis}"); return 0'
assert s.count(a)==1
s=s.replace(a,'pathlib.Path(out).write_text(json.dumps({"records":out_recs},indent=1,sort_keys=True)); print(f"merged {len(out_recs)} records; origin disagreements={ndis}"); return 0  # PROBE:SPI_SORTED_BYTES (V34)')
io.open(p,"w",encoding="utf-8").write(s); print("gate9 repair applied to",p)
