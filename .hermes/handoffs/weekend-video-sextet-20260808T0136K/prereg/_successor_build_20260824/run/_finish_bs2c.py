import sys, json, hashlib, importlib.util, time
from pathlib import Path
sys.path.insert(0, 'gates')
import numpy as np
t0 = time.time()
p = Path('real/real_oracle_dr10.npz')
sha = hashlib.sha256(p.read_bytes()).hexdigest()
assert sha == "01b8b4ecd7da6dc31654881ea4ea6713b0c06464c752d1e7e4de0028cce2103a", f"oracle sha {sha}"
oracle = np.load(p)
spec = importlib.util.spec_from_file_location("coh", "gates/count_oracle_harness.py")
coh = importlib.util.module_from_spec(spec); spec.loader.exec_module(coh)
_plan, bs2c = coh.production_build_plan(oracle["brickid"], oracle["c"], oracle["n_eligible"],
                                        grouped_sum=832393, ungrouped_total=832393)
Path('run/classp_candidates/BS-2c.json').write_text(json.dumps(bs2c, indent=2, sort_keys=True, default=str) + "\n")
print(f"BS-2c written in {time.time()-t0:.1f}s; keys={sorted(bs2c)[:8]}")
