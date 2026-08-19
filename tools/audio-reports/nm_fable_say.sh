#!/bin/zsh
# nm_fable_say.sh — one audio report voice per Fable coordinator.
#   nm_fable_say.sh <hwao|tori|blanc> "report text"
# Voice + identity come from the single registry voices.json (2026-08-20; the
# old inline case-table drifted against nm_say_cast.py's). Duho 2026-08-19:
# Hwao and Tori are female, Blanc is male.
fable="${1:?fable name required: hwao|tori|blanc}"; shift
V=/Users/duhokim/HermesOps/reports/status-audio/voices.json
voice=$(python3 -c "import json,sys; v=json.load(open('$V')).get('$fable'); print(v['voice'] if v else '')")
if [[ -z "$voice" ]]; then
  echo "unknown fable: $fable (want a seat key from voices.json)" >&2; exit 2
fi
NM_SAY_VOICE="$voice" NM_SPEAKER="$fable" exec /Users/duhokim/HermesOps/scripts/nm_status_say.sh "${fable}-report" "$@"
