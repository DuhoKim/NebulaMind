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
# claim <id> <command-string> <expected> <actual>
# The second argument is the COMMAND ITSELF, shown verbatim. Twelve gate refusals traced to
# descriptions claiming more than their checks establish; a printed command cannot.
claim() {
  if [[ "$3" == "$4" ]]; then printf "PASS  %-4s [ %s ] -> %s\n" "$1" "$2" "$4"; ((PASS++))
  else printf "FAIL  %-4s [ %s ]\n        expected: %s\n        actual  : %s\n" "$1" "$2" "$3" "$4"; ((FAIL++)); fi
}
h() { shasum -a 256 "$1" 2>/dev/null | cut -d' ' -f1 | cut -c1-16 }

NCLAIM=$(grep -Ec '^claim [A-Z][0-9]' "$SELF")
echo "verify.sh sha256 $(shasum -a 256 "$SELF" | cut -d' ' -f1)"
echo "claim invocations in this file: $NCLAIM"
echo

echo "== digests of four files that carry the 23:12 disclosure =="
claim S1 "shasum -a256 231235.mp3 | cut -c1-16"       2a38a887bd897147 "$(h $REPORTS/20260820T231235-hwao-report.mp3)"
claim S2 "shasum -a256 231235.txt | cut -c1-16"             2c85b2028209273a "$(h $REPORTS/20260820T231235-hwao-report.txt)"
claim S3 "shasum -a256 231235.deck.json | cut -c1-16"                1da50dc6878db905 "$(h $REPORTS/20260820T231235-hwao-report.deck.json)"
claim S4 "shasum -a256 231235.times.json | cut -c1-16"      a9cfedc4ab127794 "$(h $REPORTS/20260820T231235-hwao-report.times.json)"

echo "\n== strings found by grep in that one caption file =="
claim S5 "grep -c '0.834336, 0.384410, and -0.640352' 231235.txt"   1 "$(grep -c '0.834336, 0.384410, and -0.640352' $REPORTS/20260820T231235-hwao-report.txt)"
claim S6 "grep -c 'One leaning each way...' 231235.txt" 1 "$(grep -c 'One leaning each way among the confident pair' $REPORTS/20260820T231235-hwao-report.txt)"
claim S7 "grep -c '2,725 galaxies measured' 231235.txt"             1 "$(grep -c '2,725 galaxies measured' $REPORTS/20260820T231235-hwao-report.txt)"

echo "\n== digests and strings in two frozen documents =="
A=$LANE/K8_CROSSING_AUTHORIZATION_20260820.md
claim F1 "shasum -a256 K8_CROSSING_AUTHORIZATION | cut -c1-16" c10687595f1f4313 "$(h $A)"
claim F2 "grep -c 'No sky statistic, no dipole' K8_AUTH"  1 "$(grep -c 'No sky statistic, no dipole' $A)"
claim F3 "grep -c 'Partial-tertile prohibition' K8_AUTH"  1 "$(grep -c 'Partial-tertile prohibition' $A)"
claim F4 "shasum -a256 PREREG_V3 | cut -c1-16" b06901c8a0f3a057 "$(h $LANE/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md)"

echo "\n== quantities recomputed from the positions file on this run =="
claim G1 "wc -l positions_parent.csv minus header" 208407 "$(( $(wc -l < $LANE/_positions_20260820/positions_parent_20260820.csv) - 1 ))"
claim G2 "python3 geom.py  (recomputes from positions)" 0.057985 "$(python3 $LANE/_evidence_20260822/geom.py)"

echo "\n== two searches restricted to the handcheck/ directory =="
claim H1 "grep -c 'def _rank_tertiles' handcheck/nm_handcheck.py" 1 "$(grep -c 'def _rank_tertiles' $LANE/handcheck/nm_handcheck.py)"
claim H2 "grep -rl chi_dr10_south handcheck/ | wc -l" 0 "$(grep -rl 'chi_dr10_south' $LANE/handcheck/ 2>/dev/null | wc -l | tr -d ' ')"

echo "\n== one divergence of mine, left unrepaired on purpose =="
claim D1 "grep -c 'one galaxy at a time, 200,000 times' 151843.txt" 1 "$(grep -c 'one galaxy at a time, 200,000 times' $REPORTS/20260821T151843-hwao-report.txt)"
claim D2 "python3 read coverage from 151843.times.json" 0.9709 "$(python3 -c "import json;print(json.load(open('$REPORTS/20260821T151843-hwao-report.times.json'))['coverage'])")"

echo "\n== publication event and served surfaces (restored; a gate found them dropped) =="
claim P1 "python3 read ledger publish row for 231235" "20|2026-08-20 23:12:51 KST" \
  "$(python3 -c "
import json
for l in open('$REPORTS/queue_ledger.jsonl'):
    r=json.loads(l)
    if r.get('event')=='publish' and '231235' in str(r.get('file','')):
        print(f\"{r.get('seq')}|{r.get('stamp_kst')}\"); break")"
claim P2 "shasum -a256 report-231235.html | cut -c1-16" 050a3f6245fc74f1 \
  "$(h $REPORTS/report-20260820T231235-hwao-report.html)"
# archive.html is VOLATILE — rebuilt on each index change (Blanc), so its digest is pinned
# nowhere; the claim is that the page SERVES the values, which survives rebuilds.
claim P3 "grep -c 0.834336 archive.html" 1 "$(grep -c '0.834336' $REPORTS/archive.html)"

echo "\n== the companion document, checked against a banned wordlist =="
BANNED='every|everywhere|always|never|none|exhaustive|universal|\ball\b|\bany\b|\bcomplete\b|\bexact\b'
claim Q1 "grep -Eoi BANNED_WORDLIST CHI_CUSTODY.md | wc -l" 0 "$(grep -Eoi "$BANNED" "$DOC" 2>/dev/null | wc -l | tr -d ' ')"

echo "\n$PASS passed, $FAIL failed"
echo "SCOPE: the checks above ran. This script reports what they returned and nothing further."
echo "H2 searched $LANE/handcheck/ and reports a count for that directory."
exit $(( FAIL > 0 ))
