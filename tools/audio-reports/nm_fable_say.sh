#!/bin/zsh
# nm_fable_say.sh — one audio report voice per Fable coordinator (2026-08-19).
#   nm_fable_say.sh <hwao|tori|blanc> "report text"
# Wraps nm_status_say.sh: same timestamped mp3s, same latest.mp3 + listen page,
# but each coordinator is recognizable by ear. Voices are OpenAI TTS voices
# (gateway covered by the Nous sub; no key touched here).
# Duho 2026-08-19: Hwao and Tori are female, Blanc is male.
#   hwao  -> shimmer (female, composed — DESI captain)
#   tori  -> nova    (female, bright — BHU lane)
#   blanc -> onyx    (male, deep — OPS)
fable="${1:?fable name required: hwao|tori|blanc}"; shift
case "$fable" in
  hwao)  voice=shimmer ;;
  tori)  voice=nova    ;;
  blanc) voice=onyx    ;;
  *) echo "unknown fable: $fable (want hwao|tori|blanc)" >&2; exit 2 ;;
esac
NM_SAY_VOICE="$voice" exec /Users/duhokim/HermesOps/scripts/nm_status_say.sh "${fable}-report" "$@"
