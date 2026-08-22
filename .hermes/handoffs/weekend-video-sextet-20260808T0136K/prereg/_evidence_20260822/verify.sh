#!/bin/zsh
# Executable custody claims. Design rules, each forced by a gate refusal:
#   - this script prints its OWN sha256 and claim count at run time; the prose that cites it
#     carries neither, because a document cannot hold the digest of a file edited beside it;
#   - each claim description states what its check establishes, not what I wish it established;
#   - the scoped negative H2 names its search path in its own description;
#   - Q1 checks the companion document for universal-quantifier words, so the rule is tested
#     rather than promised. A rule I merely state, I have broken.
# Gate verdicts are NOT listed here: reading GATE_*.md makes this output change when a gate
# writes its report. Obtain them separately with:  head -1 GATE_*.md
setopt NO_NOMATCH 2>/dev/null || true
LANE="${0:A:h:h}"
SELF="${0:A}"
REPORTS=/Users/duhokim/HermesOps/reports/status-audio
DOC="$LANE/CHI_CUSTODY_20260822.md"
PASS=0; FAIL=0
claim() {
  if [[ "$3" == "$4" ]]; then printf "PASS  %-4s %s\n" "$1" "$2"; ((PASS++))
  else printf "FAIL  %-4s %s\n        expected: %s\n        actual  : %s\n" "$1" "$2" "$3" "$4"; ((FAIL++)); fi
}
h() { shasum -a 256 "$1" 2>/dev/null | cut -d' ' -f1 | cut -c1-16 }

NCLAIM=$(grep -Ec '^claim [A-Z][0-9]' "$SELF")
echo "verify.sh sha256 $(shasum -a 256 "$SELF" | cut -d' ' -f1)"
echo "claim invocations in this file: $NCLAIM"
echo

echo "== digests of four files that carry the 23:12 disclosure =="
claim S1 "shasum of that report's mp3 is 2a38a887bd897147"       2a38a887bd897147 "$(h $REPORTS/20260820T231235-hwao-report.mp3)"
claim S2 "shasum of its caption is 2c85b2028209273a"             2c85b2028209273a "$(h $REPORTS/20260820T231235-hwao-report.txt)"
claim S3 "shasum of its deck is 1da50dc6878db905"                1da50dc6878db905 "$(h $REPORTS/20260820T231235-hwao-report.deck.json)"
claim S4 "shasum of its alignment file is a9cfedc4ab127794"      a9cfedc4ab127794 "$(h $REPORTS/20260820T231235-hwao-report.times.json)"

echo "\n== strings found by grep in that one caption file =="
claim S5 "grep finds '0.834336, 0.384410, and -0.640352' once"   1 "$(grep -c '0.834336, 0.384410, and -0.640352' $REPORTS/20260820T231235-hwao-report.txt)"
claim S6 "grep finds 'One leaning each way among the confident pair' once" 1 "$(grep -c 'One leaning each way among the confident pair' $REPORTS/20260820T231235-hwao-report.txt)"
claim S7 "grep finds '2,725 galaxies measured' once"             1 "$(grep -c '2,725 galaxies measured' $REPORTS/20260820T231235-hwao-report.txt)"

echo "\n== digests and strings in two frozen documents =="
A=$LANE/K8_CROSSING_AUTHORIZATION_20260820.md
claim F1 "shasum of the K-8 authorization is c10687595f1f4313" c10687595f1f4313 "$(h $A)"
claim F2 "grep finds 'No sky statistic, no dipole' in it once"  1 "$(grep -c 'No sky statistic, no dipole' $A)"
claim F3 "grep finds 'Partial-tertile prohibition' in it once"  1 "$(grep -c 'Partial-tertile prohibition' $A)"
claim F4 "shasum of the frozen preregistration is b06901c8a0f3a057" b06901c8a0f3a057 "$(h $LANE/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md)"

echo "\n== quantities recomputed from the positions file on this run =="
claim G1 "the positions CSV has 208407 data rows" 208407 "$(( $(wc -l < $LANE/_positions_20260820/positions_parent_20260820.csv) - 1 ))"
claim G2 "geom.py recomputes var(cos theta) about Longo's axis as 0.057985" 0.057985 "$(python3 $LANE/_evidence_20260822/geom.py)"

echo "\n== two searches restricted to the handcheck/ directory =="
claim H1 "grep finds 'def _rank_tertiles' in handcheck/nm_handcheck.py once" 1 "$(grep -c 'def _rank_tertiles' $LANE/handcheck/nm_handcheck.py)"
claim H2 "grep -rl 'chi_dr10_south' under $LANE/handcheck/ lists 0 files" 0 "$(grep -rl 'chi_dr10_south' $LANE/handcheck/ 2>/dev/null | wc -l | tr -d ' ')"

echo "\n== one divergence of mine, left unrepaired on purpose =="
claim D1 "grep finds 'one galaxy at a time, 200,000 times' in that caption once" 1 "$(grep -c 'one galaxy at a time, 200,000 times' $REPORTS/20260821T151843-hwao-report.txt)"
claim D2 "its alignment file records coverage 0.9709" 0.9709 "$(python3 -c "import json;print(json.load(open('$REPORTS/20260821T151843-hwao-report.times.json'))['coverage'])")"

echo "\n== the companion document, checked against a banned wordlist =="
BANNED='every|everywhere|always|never|none|exhaustive|universal|\ball\b|\bany\b|\bcomplete\b|\bexact\b'
claim Q1 "grep -Eic on the banned wordlist in CHI_CUSTODY_20260822.md returns 0" 0 "$(grep -Eoi "$BANNED" "$DOC" 2>/dev/null | wc -l | tr -d ' ')"

echo "\n$PASS passed, $FAIL failed"
echo "SCOPE: the checks above ran. This script reports what they returned and nothing further."
echo "H2 searched $LANE/handcheck/ and reports a count for that directory."
exit $(( FAIL > 0 ))
