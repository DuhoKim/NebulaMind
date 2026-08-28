#!/usr/bin/env python3
"""Synthetic checks of KNOWN form, for measuring a11's classifier against ground truth."""
import re
T = open("/etc/hostname").read() if False else "sample text with 3.5 x 10^4 and Lambda"
checks = []
def chk(name, pred, detail=""): checks.append((name, pred, detail))

# GROUND TRUTH: TAUTOLOGY -- nothing varies
chk("c1 tautology", abs(-1.0 - 0.0 + 1.0) < 1e-12)

# GROUND TRUTH: LITERAL -- constants only
chk("c2 literal", 63.0 > 20.0 * 1.5)

# GROUND TRUTH: STRING -- direct membership on source
chk("c3 string direct", "Lambda" in T)

# GROUND TRUTH: STRING -- membership via an intermediate variable (codex's flagged case)
flag = "Lambda" in T
chk("c4 string via variable", flag)

# GROUND TRUTH: STRING -- regex search via variable
m = re.search(r"Lambda", T)
chk("c5 regex via variable", m is not None)

# GROUND TRUTH: COMPUTED -- arithmetic on a parsed value
val = float(re.search(r"(\d\.\d)", T).group(1))
chk("c6 computed from parse", abs(val * 2.0 - 7.0) < 1e-9)

# GROUND TRUTH: MIXED -- count of matches compared to a threshold
n = len(re.findall(r"\d", T))
chk("c7 count vs threshold", n > 2 and "Lambda" in T)

# GROUND TRUTH: STRING -- boolean built in a loop from membership
ok = True
for w in ("Lambda", "sample"):
    if w not in T: ok = False
chk("c8 loop flag from membership", ok)
