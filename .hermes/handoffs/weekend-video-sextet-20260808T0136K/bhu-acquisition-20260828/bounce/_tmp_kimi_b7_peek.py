#!/usr/bin/python3
"""Find how the MathJax payload for Equ35 etc. is stored in the publisher HTML."""
import re
p = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/b4_springer_access.html"
raw = open(p, encoding="utf-8", errors="replace").read()
i = raw.find('Equ35')
print("context around first Equ35:")
print(raw[i-200:i+2500])
