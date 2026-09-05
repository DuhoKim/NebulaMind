import os, re
T = open('../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md').read()
cited = set(os.path.basename(m.group(1)) for m in re.finditer(r'`([^`\s]+?\.(?:pdf|txt|html|json|tex))`', T))
cited = [b for b in cited if '*' not in b] + ['1309.1487.pdf']
idx = {}
for root, dirs, files in os.walk('../'):
    if 'venv' in root or 'node_modules' in root: continue
    for f in files: idx.setdefault(f, []).append(os.path.join(root, f))
cols = {k: v for k, v in idx.items() if k in cited and len(v) > 1}
for k, v in cols.items(): print(k, v)
if not cols: print('NO COLLISIONS')
