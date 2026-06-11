import sys
import re

# Read original
with open("/Users/duhokim/.openclaw/workspace/galaxy_evolution_current.md", "r", encoding="utf-8") as f:
    orig = f.read()

# Read renovated
with open("/Users/duhokim/.openclaw/workspace/galaxy_evolution_renovated.md", "r", encoding="utf-8") as f:
    renov = f.read()

def parse_claims(text):
    raw_markers = re.findall(r"<!--claim:([\d,\s]+)\s*-->", text)
    all_ids = []
    for r in raw_markers:
        for val in r.split(","):
            val = val.strip()
            if val:
                all_ids.append(int(val))
    return set(all_ids), raw_markers

orig_ids, orig_markers = parse_claims(orig)
renov_ids, renov_markers = parse_claims(renov)

print("--- CLAIM MARKER VALIDATION ---")
print(f"Original Unique Claims: {len(orig_ids)} | Original Raw Markers: {len(orig_markers)}")
print(f"Renovated Unique Claims: {len(renov_ids)} | Renovated Raw Markers: {len(renov_markers)}")

# Check if any claim IDs were lost or deleted
lost_ids = orig_ids - renov_ids
if lost_ids:
    print(f"ERROR: Lost Claim IDs in renovation: {lost_ids}")
else:
    print("SUCCESS: Zero claim IDs were lost in the renovation!")

# Check matching open/close tags
def check_tags(text):
    open_tags = re.findall(r"<!--claim:([\d,\s]+)\s*-->", text)
    close_tags = re.findall(r"<!--/claim:([\d,\s]+)\s*-->", text)
    
    # Check lengths
    if len(open_tags) != len(close_tags):
        print(f"ERROR: Mismatched tag counts! Opens: {len(open_tags)} | Closes: {len(close_tags)}")
        return False
        
    for o, c in zip(open_tags, close_tags):
        o_clean = ",".join(sorted([x.strip() for x in o.split(",") if x.strip()]))
        c_clean = ",".join(sorted([x.strip() for x in c.split(",") if x.strip()]))
        if o_clean != c_clean:
            print(f"ERROR: Mismatched tags! Open: {o_clean} vs Close: {c_clean}")
            return False
            
    print("SUCCESS: Every open claim tag has a perfectly matched close tag!")
    return True

check_tags(renov)
