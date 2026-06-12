file_path = "tasks.py"
with open(file_path, "r") as f:
    content = f.read()

import re

old_sys = """_SONNET_SECTION_SYSTEM = (
    "You are an expert astronomy wiki editor writing at graduate-textbook depth. "
    "Rewrite the given section with maximum scientific specificity. "
    "Return markdown followed by a JSON marker report. "
    "HARD REQUIREMENTS — violating any disqualifies the response:\\n"
    "  1. Minimum 400 words below the ## header.\\n"
    "  2. At least 3 quantitative facts: redshifts, masses, luminosities, "
    "percentages, timescales, temperatures, or distances with units.\\n"
    "  3. Every major claim attributed with (Author et al. YYYY) in-text.\\n"
    "  4. BANNED phrases: 'plays a crucial role', 'complex and dynamic', "
    "'plays an important role', 'is a fascinating', 'remains to be seen', "
    "'future work will', 'this page covers', 'in conclusion'.\\n"
    "  5. You MUST weave HTML claim markers (e.g. <!--claim:123-->) inline immediately after asserting any of the provided 'owned' claims.\\n"
    "  6. You MUST PRESERVE all trust/consensus HTML comments (e.g. <!--accepted-->, <!--consensus-->).\\n"
    "  7. MUST output a valid JSON report at the end wrapped in <!--marker-report ... -->.\\n"
)"""

new_sys = """_SONNET_SECTION_SYSTEM = (
    "You are an expert astronomy wiki editor writing at graduate-textbook depth. "
    "Rewrite the given section with maximum scientific specificity. "
    "Return markdown followed by a JSON marker report. "
    "HARD REQUIREMENTS — violating any disqualifies the response:\\n"
    "  1. Minimum 400 words below the ## header.\\n"
    "  2. At least 3 quantitative facts: redshifts, masses, luminosities, "
    "percentages, timescales, temperatures, or distances with units.\\n"
    "  3. Every major claim attributed with (Author et al. YYYY) in-text.\\n"
    "  4. BANNED phrases: 'plays a crucial role', 'complex and dynamic', "
    "'plays an important role', 'is a fascinating', 'remains to be seen', "
    "'future work will', 'this page covers', 'in conclusion'.\\n"
    "  5. You MUST weave HTML claim markers (e.g. <!--claim:123-->) inline immediately after asserting any of the provided 'owned' claims.\\n"
    "  6. You MUST PRESERVE all trust/consensus HTML comments (e.g. <!--accepted-->, <!--consensus-->).\\n"
    "  7. MUST output a valid JSON report at the end wrapped in <!--marker-report ... -->.\\n"
    "  8. You MUST include and assert EVERY 'Must-Keep Owned Claim'. DO NOT omit them.\\n"
)"""

content = content.replace(old_sys, new_sys)

# Also make the reject stricter so it actually pushes back on omission of must-keep.
old_reject = """                        if unaccounted:
                            logger.warning(f"[autowiki_tick] Missing must_keep claims unaccounted for in proposer: {unaccounted}")
                            proposal["reject_reason"] = "missing_must_keep_claims\""""

old_reject_sonnet = """        unaccounted = missing_must_keep - omitted_with_reason
        if unaccounted:
            logger.warning(f"[sonnet_section_rewrite] Missing must_keep claims unaccounted for: {unaccounted}")
            return {"decision": "skip", "reject_reason": "missing_must_keep_claims"}"""

new_reject_sonnet = """        if missing_must_keep:
            logger.warning(f"[sonnet_section_rewrite] Missing must_keep claims: {missing_must_keep}. Rejecting.")
            return {"decision": "skip", "reject_reason": "missing_must_keep_claims"}"""

content = content.replace(old_reject_sonnet, new_reject_sonnet)

with open(file_path, "w") as f:
    f.write(content)
print("Made prompt stricter")
