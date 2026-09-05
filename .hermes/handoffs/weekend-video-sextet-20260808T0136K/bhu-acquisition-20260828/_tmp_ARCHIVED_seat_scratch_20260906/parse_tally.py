import re

with open('../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md', 'r') as f:
    B = f.read()

cut = B.find("## Ranked:")
st = [(m.start(), int(m.group(1))) for m in re.finditer(r"^\*\*(\d{1,2})\. ", B[:cut], re.M)]
blocks = {n: B[p:(st[i + 1][0] if i + 1 < len(st) else cut)] for i, (p, n) in enumerate(st)}

tallies = {}
for n, b in blocks.items():
    mm = re.search(r"Testability: \*\*([A-Z-]+)\*\*", b)
    if mm:
        tier = mm.group(1)
        tallies[tier] = tallies.get(tier, 0) + 1
        if tier == "THEORETICAL-OBSTRUCTION" or tier == "UNREAD":
            print(f"Entry {n}: {tier}")

print(tallies)
print("Total:", sum(tallies.values()))
