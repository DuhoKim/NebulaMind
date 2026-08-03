# HWAO_PREFLIGHT_CORRECTION — prompt boundary defect fixed

Goru preflight correctly returned NOT_GREEN on one defect: in the `HWAO_ONE_CANARY_PLAN.md` §3 paste block, the prose "with nothing after it." followed the completion-marker string, so the frozen prompt's final non-empty line was prose rather than the marker `GEMINI_WEB_GE_COMPARABILITY_CANARY_DONE_20260713T160239Z`, breaking the self-verifying paste boundary the preflight lint requires.

Correction applied (the only change made): the closing sentence now reads "The last non-empty line of the report must be exactly the completion marker below, with nothing after it:" followed by the marker as the paste block's final non-empty line before the END sentinel. No other plan content, clause, marker, or boundary was modified; no browser/network action occurred.

Next step: Goru re-freezes the corrected prompt block as `prompt/GE_COMPARABILITY_CANARY.md`, records the new sha256, and reruns preflight. All other plan terms, including §11's arming conditions, stand unchanged.

HWAO_CONTENT_DR_PROMPT_BOUNDARY_CORRECTED
