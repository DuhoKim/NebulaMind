import re

with open('../PREREG_SUCCESSOR_DRAFT_V26_20260827.md', 'r') as f:
    text = f.read()

text = text.replace("pending the refused BS-2a design.", "pending the DESIGN, defined, UNFILLED BS-2a design.")
text = text.replace("pending the refused BS-2a design", "pending the DESIGN, defined, UNFILLED BS-2a design")
text = text.replace("the refused BS-2a design.", "the DESIGN, defined, UNFILLED BS-2a slot.")
text = text.replace("the refused BS-2a design", "the DESIGN, defined, UNFILLED BS-2a slot")
text = text.replace("already-unfilled BS-2a design", "DESIGN, defined, UNFILLED BS-2a design")

# Also, ensure section 11 "already-refused" is replaced.
text = text.replace("already-refused BS-2a design", "DESIGN, defined, UNFILLED BS-2a design")

# One of fifteen class-P slots is filled
# Original text in V25 says:
# "One of fifteen class-P slots is filled (BS-2m)." (Wait, let's check V25 exact text)

with open('../PREREG_SUCCESSOR_DRAFT_V26_20260827.md', 'w') as f:
    f.write(text)
