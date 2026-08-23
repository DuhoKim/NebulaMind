#!/bin/zsh
# Executable custody claims, v4. THE PRINTED COMMAND IS THE EXECUTED COMMAND:
# claim() takes one string, eval-runs exactly it, and prints exactly it. Thirteen gate
# refusals traced to a description layer drifting from the checks — v3 removed prose
# descriptions and was refuted because its hand-written "command" labels were themselves
# curated. Here the label and the execution are the same bytes by construction.
# Paths are full literals inside each command: what you see is what ran, copy-pasteable.
setopt NO_NOMATCH 2>/dev/null || true
SELF="${0:A}"
PASS=0; FAIL=0
claim() {  # claim <id> <command-string> <expected>
  local got; got="$(eval "$2" 2>/dev/null)"
  if [[ "$got" == "$3" ]]; then printf "PASS  %-4s $ %s\n          -> %s\n" "$1" "$2" "$got"; ((PASS++))
  else printf "FAIL  %-4s $ %s\n          expected: %s\n          actual  : %s\n" "$1" "$2" "$3" "$got"; ((FAIL++)); fi
}
P=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg
R=/Users/duhokim/HermesOps/reports/status-audio

echo "verify.sh sha256 $(shasum -a 256 "$SELF" | cut -d' ' -f1)"
echo "claim invocations in this file: $(grep -Ec '^claim [A-Z][0-9]' "$SELF")"

echo "\n== digests (16-hex PREFIXES of sha256; the cut is in the shown command) =="
claim S1 "shasum -a 256 $R/20260820T231235-hwao-report.mp3 | cut -c1-16" 2a38a887bd897147
claim S2 "shasum -a 256 $R/20260820T231235-hwao-report.txt | cut -c1-16" 2c85b2028209273a
claim S3 "shasum -a 256 $R/20260820T231235-hwao-report.deck.json | cut -c1-16" 1da50dc6878db905
claim S4 "shasum -a 256 $R/20260820T231235-hwao-report.times.json | cut -c1-16" a9cfedc4ab127794

echo "\n== strings in the 23:12 caption =="
claim S5 "grep -c '0.834336, 0.384410, and -0.640352' $R/20260820T231235-hwao-report.txt" 1
claim S6 "grep -c 'One leaning each way among the confident pair' $R/20260820T231235-hwao-report.txt" 1
claim S7 "grep -c '2,725 galaxies measured' $R/20260820T231235-hwao-report.txt" 1

echo "\n== frozen documents the rulings rest on =="
claim F1 "shasum -a 256 $P/K8_CROSSING_AUTHORIZATION_20260820.md | cut -c1-16" c10687595f1f4313
claim F2 "grep -c 'No sky statistic, no dipole' $P/K8_CROSSING_AUTHORIZATION_20260820.md" 1
claim F3 "grep -c 'Partial-tertile prohibition' $P/K8_CROSSING_AUTHORIZATION_20260820.md" 1
claim F4 "shasum -a 256 $P/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md | cut -c1-16" b06901c8a0f3a057

echo "\n== quantities recomputed from positions on this run =="
claim G1 "echo \$(( \$(wc -l < $P/_positions_20260820/positions_parent_20260820.csv) - 1 ))" 208407
claim G2 "python3 $P/_evidence_20260822/geom.py" 0.057985

echo "\n== searches restricted to handcheck/ =="
claim H1 "grep -c 'def _rank_tertiles' $P/handcheck/nm_handcheck.py" 1
claim H2 "grep -rl chi_dr10_south $P/handcheck/ | wc -l | tr -d ' '" 0

echo "\n== gate history of the footprint finding, from the files themselves =="
claim X1 "head -1 $P/GATE_FOOTPRINT_GEOMETRY_20260821.md" HOLD_FOOTPRINT_GEOMETRY_FINDING
claim X2 "head -1 $P/GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md" HOLD_FOOTPRINT_GEOMETRY_REV2
claim X3 "grep -c 6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7 $P/GATE_FOOTPRINT_GEOMETRY_20260821.md $P/GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md | grep -c ':0\$'" 2

echo "\n== my open divergence, left unrepaired on purpose =="
claim D1 "grep -c 'one galaxy at a time, 200,000 times' $R/20260821T151843-hwao-report.txt" 1
claim D2 "python3 -c \"import json;print(json.load(open('$R/20260821T151843-hwao-report.times.json'))['coverage'])\"" 0.9709

echo "\n== publication event and served surfaces =="
claim P1 "python3 -c \"
import json
for l in open('$R/queue_ledger.jsonl'):
    r=json.loads(l)
    if r.get('event')=='publish' and '231235' in str(r.get('file','')):
        print(r.get('seq'), r.get('stamp_kst'), 'backfilled='+str(r.get('backfilled'))); break\"" "20 2026-08-20 23:12:51 KST backfilled=True"
claim P2 "shasum -a 256 $R/report-20260820T231235-hwao-report.html | cut -c1-16" 050a3f6245fc74f1
claim P3 "grep -c '0.834336, 0.384410, and -0.640352' $R/archive.html" 1
claim P4 "grep -c 'report-20260820T231235-hwao-report' $R/archive.html" 1

echo "\n== superseded forms retained on disk (the drafting history, countable) =="
claim L1 "ls $P/CHI_CUSTODY_RECEIPT_20260821*.md $P/CHI_CUSTODY_20260822_V*_SUPERSEDED.md | wc -l | tr -d ' '" 11

echo "\n== the companion document against the banned wordlist =="
claim Q1 "grep -Eoi 'every|everywhere|always|never|none|exhaustive|universal|\\ball\\b|\\bany\\b|\\bcomplete\\b|\\bexact\\b' $P/CHI_CUSTODY_20260822.md | wc -l | tr -d ' '" 0

echo "\n$PASS passed, $FAIL failed"
echo "SCOPE: the commands above ran as printed. This script reports their outputs and no more."
exit $(( FAIL > 0 ))
