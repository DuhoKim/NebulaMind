#!/bin/zsh
# Shim so nm_referee_dispatch.sh can drive a codex seat instead of agy, WITHOUT changing the wrapper.
# The wrapper's access-proof computation and quarantine logic are preserved exactly; only the engine changes.
# Accepts and discards agy-specific flags; forwards --add-dir as --cd and the -p prompt to `codex exec`.
prompt=""; cd_dir=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    -p) prompt="$2"; shift 2 ;;
    --add-dir) [[ -z "$cd_dir" ]] && cd_dir="$2"; shift 2 ;;
    --print-timeout) shift 2 ;;
    --dangerously-skip-permissions) shift ;;
    *) shift ;;
  esac
done
exec /Users/duhokim/.local/bin/codex exec --dangerously-bypass-approvals-and-sandbox --cd "$cd_dir" "$prompt"
