import re

with open('../PREREG_SUCCESSOR_DRAFT_V26_20260827.md', 'r') as f:
    text = f.read()

text = text.replace("BS-2a is **FILLED**, so processes requiring it (Rows C2, E) can now run.", "BS-2a is **DESIGN, defined, UNFILLED**, so processes requiring it (Rows C2, E) cannot run yet.")

with open('../PREREG_SUCCESSOR_DRAFT_V26_20260827.md', 'w') as f:
    f.write(text)
