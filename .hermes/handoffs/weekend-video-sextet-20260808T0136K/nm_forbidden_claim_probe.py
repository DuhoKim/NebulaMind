#!/usr/bin/env python3
"""Measure what the forbidden-claim patterns miss, so nobody mistakes them for coverage.

The BHU standing rule is a phrase: "BHU is falsified" would be false and is never said.
Patterns can only narrow the search space for it. This probes them with paraphrases that
assert the same claim and prints the miss rate as a number.

Exit 1 only if a MUST-CATCH probe stops being caught — a regression guard on the patterns.
Misses are expected and reported, not failed: a wordlist has no natural end (Hwao, Q1/CANNOT).
Add paraphrases freely; the coverage figure updates.
"""
import re, sys

FORBIDDEN = re.compile(r"\b(?:BHU|black[- ]hole[- ]universe)\b[^.]{0,40}\b(?:falsifi|refut|disprov)", re.I)
VERBS = re.compile(r"\b(?:falsified|refuted|disproved|vindicated|confirmed|proven)\b", re.I)

MUST_CATCH = [
    "BHU is falsified by the pulsar data",
    "the black-hole-universe idea is refuted",
    "cosmological natural selection is vindicated by this",
]
ASSERTS_ANYWAY = [
    "nothing in the family survives contact with the data",
    "the black-hole-universe programme is dead",
    "no version of this cosmology can now be sustained",
    "the whole line is finished as a physical hypothesis",
    "every branch of it fails its own test",
    "BHU cannot be true given these masses",
    "the idea does not survive the neutron-star measurements",
    "we can close the book on universes inside black holes",
]


def caught(s):
    return bool(FORBIDDEN.search(s) or VERBS.search(s))


def main():
    fails = [s for s in MUST_CATCH if not caught(s)]
    missed = [s for s in ASSERTS_ANYWAY if not caught(s)]
    print(f"  must-catch: {len(MUST_CATCH)-len(fails)}/{len(MUST_CATCH)} caught")
    for s in fails:
        print(f"    REGRESSION, no longer caught: {s}")
    print(f"  paraphrases: {len(ASSERTS_ANYWAY)-len(missed)}/{len(ASSERTS_ANYWAY)} caught "
          f"-> {len(missed)} assert the forbidden claim and pass undetected")
    for s in missed:
        print(f"    missed: {s}")
    print("\n  COVERAGE IS NOT COMPLETENESS. These patterns narrow a search space; they do not")
    print("  bound one. Do not cite a clean pattern run as evidence that nothing was said.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
