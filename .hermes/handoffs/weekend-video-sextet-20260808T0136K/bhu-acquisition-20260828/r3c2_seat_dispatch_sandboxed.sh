#!/bin/zsh
# r3c2_seat_dispatch_sandboxed.sh — shim for nm_referee_dispatch.sh (AGY=this): runs the codex seat INSIDE a macOS sandbox
# (r3c2_seat_sandbox.sb) that permits file reads only under the seat's working directory and the binary's own needs, denies the
# lane and everything else, and keeps the network for the model. Model pinned to gpt-6-astra (Duho 09:46 KST). stdin closed.
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
SB="$(dirname "$0")/r3c2_seat_sandbox.sb"
exec /usr/bin/sandbox-exec -D WORKDIR="$cd_dir" -f "$SB" /Users/duhokim/.local/bin/codex exec --dangerously-bypass-approvals-and-sandbox -m gpt-6-astra --cd "$cd_dir" "$prompt" < /dev/null
