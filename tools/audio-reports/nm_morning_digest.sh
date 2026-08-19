#!/bin/zsh
# nm_morning_digest.sh — the first sound of the day (2026-08-20).
#   nm_morning_digest.sh <speaker> "digest text"
# Renders one reading in the speaker's registered voice and publishes it
# FORCE-LIVE (bypasses quiet hours — use only at/after the morning boundary).
# Quiet overnight readings stay in the queue for the archive page; this digest
# is the human-facing summary of them.
speaker="${1:?speaker required}"; shift
NM_FORCE_LIVE=1 exec /Users/duhokim/HermesOps/scripts/nm_fable_say.sh "$speaker" "$@"
