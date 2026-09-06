#!/bin/zsh
# Flag-translating shim so nm_referee_dispatch.sh can drive the codex CLI.
# It changes ONLY the invocation syntax. Every guarantee of the wrapper is untouched:
# the wrapper still prepends the ACCESS PROOF demand, still computes the target's true
# SHA-256 itself, still greps the returned report for that exact value, and still
# quarantines the report as *_INVALID_NO_ACCESS.md and exits 3 if the proof is absent.
# This is not a bypass of the access-proof control; it is a different engine behind it.
#
# Why codex for seat B: the kimi route was dispatched three times and returned no verdict
# each time. Its hermes session had `execute_code` and `terminal` BLOCKED by tool policy,
# so it could not hash pins or run fixtures -- items the brief requires. codex is a
# different engine from seat A (agy/Gemini) and can run commands.
# 2026-09-06 09:46 KST (Duho via Blanc: "use astra for both"): model pinned to gpt-6-astra; codex-cli
# updated in place 0.146.0 -> 0.153.4 by Blanc. Every run stamps <report>.engine with CLI version,
# model and UTC so the register can show WHICH engine produced WHICH verdict. Reports before this
# stamp were produced by codex-cli 0.146.0 with the previous model (not recorded at run time).
MODEL="gpt-6-astra"
set -u
prompt=""; lane="$PWD"
while [[ $# -gt 0 ]]; do
  case "$1" in
    -p) prompt="$2"; shift 2 ;;
    --add-dir) lane="$2"; shift 2 ;;
    --dangerously-skip-permissions) shift ;;
    --print-timeout) shift 2 ;;   # codex has no equivalent flag
    *) shift ;;
  esac
done
ver=$(/Users/duhokim/.local/bin/codex --version 2>/dev/null | head -1)
report=$(print -r -- "$prompt" | grep -oE "write your full report to the file [^ ]+" | head -1 | awk '{print $NF}')
stamp="ENGINE: ${ver:-codex-cli unknown} model ${MODEL} dispatched $(date -u +%FT%TZ)"
[[ -n "$report" ]] && print -r -- "$stamp" > "${report}.engine"
print -r -- "[codex-shim] $stamp report=${report:-?}" >&2
exec /Users/duhokim/.local/bin/codex exec -m "$MODEL" \
     --dangerously-bypass-approvals-and-sandbox --skip-git-repo-check \
     -C "$lane" "$prompt" < /dev/null
