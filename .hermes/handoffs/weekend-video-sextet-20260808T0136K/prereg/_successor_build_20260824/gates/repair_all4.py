import re

with open('../PREREG_SUCCESSOR_DRAFT_V26_20260827.md', 'r') as f:
    text = f.read()

text = text.replace("7. **The exclusion predicate (BS-2a) is FILLED.**", "7. **The exclusion predicate (BS-2a) is DESIGN, defined, UNFILLED.**")

with open('../PREREG_SUCCESSOR_DRAFT_V26_20260827.md', 'w') as f:
    f.write(text)
