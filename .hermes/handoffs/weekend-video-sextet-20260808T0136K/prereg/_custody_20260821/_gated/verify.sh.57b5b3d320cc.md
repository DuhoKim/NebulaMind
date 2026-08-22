#!/bin/zsh
# Executable custody claims. Each claim is a NAMED, SCOPED check that either passes or fails.
# Design rule born from ten gate refusals on 2026-08-21: no claim may contain a universal
# quantifier. A check answers "does THIS command over THESE named paths give THIS result",
# never "does X hold everywhere". Absence of evidence is reported as the scope of the search,
# not as proof of absence.
setopt NO_NOMATCH 2>/dev/null || true
LANE="${0:A:h:h}"
REPORTS=/Users/duhokim/HermesOps/reports/status-audio
PASS=0; FAIL=0
claim() {  # claim <id> <description> <expected> <actual>
  if [[ "$3" == "$4" ]]; then printf "PASS  %-6s %s\n" "$1" "$2"; ((PASS++))
  else printf "FAIL  %-6s %s\n         expected: %s\n         actual  : %s\n" "$1" "$2" "$3" "$4"; ((FAIL++)); fi
}
h() { shasum -a 256 "$1" 2>/dev/null | cut -d' ' -f1 | cut -c1-16 }

echo "== disclosure surfaces (the 23:12 report) =="
claim S1 "mp3 digest"        2a38a887bd897147 "$(h $REPORTS/20260820T231235-hwao-report.mp3)"
claim S2 "caption digest"    2c85b2028209273a "$(h $REPORTS/20260820T231235-hwao-report.txt)"
claim S3 "deck digest"       1da50dc6878db905 "$(h $REPORTS/20260820T231235-hwao-report.deck.json)"
claim S4 "alignment digest"  a9cfedc4ab127794 "$(h $REPORTS/20260820T231235-hwao-report.times.json)"
claim S5 "caption states the three values" 1 \
  "$(grep -c '0.834336, 0.384410, and -0.640352' $REPORTS/20260820T231235-hwao-report.txt)"
claim S6 "caption states a sign summary" 1 \
  "$(grep -c 'One leaning each way among the confident pair' $REPORTS/20260820T231235-hwao-report.txt)"
claim S7 "caption states the count then measured" 1 \
  "$(grep -c '2,725 galaxies measured' $REPORTS/20260820T231235-hwao-report.txt)"

echo "\n== frozen text the rulings rest on =="
A=$LANE/K8_CROSSING_AUTHORIZATION_20260820.md
claim F1 "authorization sha"  c10687595f1f4313 "$(h $A)"
claim F2 "condition 2 bars summaries over chi" 1 \
  "$(grep -c 'No sky statistic, no dipole' $A)"
claim F3 "condition 1 is the partial-tertile prohibition" 1 \
  "$(grep -c 'Partial-tertile prohibition' $A)"
claim F4 "prereg sha" b06901c8a0f3a057 "$(h $LANE/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md)"

echo "\n== footprint geometry (positions only; no chi read) =="
claim G1 "parent row count" 208407 \
  "$(( $(wc -l < $LANE/_positions_20260820/positions_parent_20260820.csv) - 1 ))"
claim G2 "var(cos theta) about Longo's axis, 6 dp" 0.057985 \
  "$(python3 $LANE/_evidence_20260822/geom.py)"

echo "\n== the hand-check harness, SCOPED to handcheck/ =="
# H1 asserted a count of 1 on its first run; the true count is 4. The FACT was right and my
# EXPECTED VALUE was invented — exactly the overclaim this design exists to catch. Now it checks
# the definition, which is stable, rather than a usage count I never counted.
claim H1 "handcheck/nm_handcheck.py DEFINES a chi-tertile ranker" 1 \
  "$(grep -c 'def _rank_tertiles' $LANE/handcheck/nm_handcheck.py)"
claim H2 "grep for the real chi tree under handcheck/ returns no lines" 0 \
  "$(grep -rl 'chi_dr10_south' $LANE/handcheck/ 2>/dev/null | wc -l | tr -d ' ')"

echo "\n== my own open divergence (20260821T151843) =="
claim D1 "caption asserts 200,000 times" 1 \
  "$(grep -c 'one galaxy at a time, 200,000 times' $REPORTS/20260821T151843-hwao-report.txt)"
claim D2 "alignment coverage on that report" 0.9709 \
  "$(python3 -c "import json;print(json.load(open('$REPORTS/20260821T151843-hwao-report.times.json'))['coverage'])")"

echo "\n== gate verdicts, read from each file's first line =="
for g in $LANE/GATE_*.md; do printf "  %-52s %s\n" "$(basename $g)" "$(head -1 $g)"; done

echo "\n$PASS passed, $FAIL failed"
echo "SCOPE: this script checks the claims listed above and nothing else."
echo "H2 is a search over $LANE/handcheck/ only. It is not a statement about any other path."
exit $(( FAIL > 0 ))
