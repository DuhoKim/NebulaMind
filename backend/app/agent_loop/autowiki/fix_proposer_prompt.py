import re
file_path = "proposers.py"
with open(file_path, "r") as f:
    content = f.read()

# Modify propose_section_rewrite signature
old_sig = """def propose_section_rewrite(
    page_content: str, section_header: str, program: str, claims_text: str = ""
) -> ProposalResult:"""
new_sig = """def propose_section_rewrite(
    page_content: str, section_header: str, program: str, owned_claims_text: str = "", context_claims_text: str = ""
) -> ProposalResult:"""
content = content.replace(old_sig, new_sig)

# Modify AstroSage system prompt
old_sys = """    system = (
        "You are an astronomy wiki editor writing at graduate-textbook depth. "
        "Rewrite the given section with maximum scientific specificity. "
        "Return markdown only (no JSON wrapper). "
        "HARD REQUIREMENTS — violating any disqualifies the response:\\n"
        "  1. Minimum 400 words below the ## header.\\n"
        "  2. At least 3 quantitative facts: redshifts, masses, luminosities, "
        "percentages, timescales, temperatures, or distances with units.\\n"
        "  3. Every major claim attributed with (Author et al. YYYY) in-text.\\n"
        "  4. BANNED phrases: 'plays a crucial role', 'complex and dynamic', "
        "'plays an important role', 'is a fascinating', 'remains to be seen', "
        "'future work will', 'this page covers', 'in conclusion'.\\n"
        "  5. You MUST weave HTML claim markers (e.g. <!--claim:123-->) inline immediately after asserting any of the provided key claims.\\n"
        "  6. You MUST PRESERVE any existing <!--claim:xxx--> markers from the current section."
    )"""
new_sys = """    system = (
        "You are an astronomy wiki editor writing at graduate-textbook depth. "
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
content = content.replace(old_sys, new_sys)

# Modify user prompt
old_user = """    user = (
        f"Program:\\n{program[:400]}\\n\\n"
        f"Current section:\\n{current_section}\\n\\n"
        f"Key claims on this page:\\n{claims_text}\\n\\n"
        "Rewrite this section. Requirements:\\n\"\"\""
        f"{section_guidance}\n"
        "\"\"\"\n"
        f"Keep the ## header exactly as: {section_header}"
    )"""
new_user = """    user = (
        f"Program:\\n{program[:400]}\\n\\n"
        f"Current section:\\n{current_section}\\n\\n"
        f"Owned claims for this section:\\n{owned_claims_text}\\n\\n"
        f"Context claims (DO NOT force into this section):\\n{context_claims_text}\\n\\n"
        "Rewrite this section. Requirements:\\n\"\"\""
        f"{section_guidance}\n"
        "\"\"\"\n"
        f"Keep the ## header exactly as: {section_header}\\n\\n"
        "At the end of your response, you MUST include a marker report in exactly this format:\\n"
        "<!--marker-report\\n{\\n  \\"section\\": \\"Section Name\\",\\n  \\"asserted_claim_ids\\": [123, 124],\\n  \\"omitted_owned_claim_ids\\": [{\\"id\\": 126, \\"reason\\": \\"not asserted\\"}]\\n}\\n-->"
    )"""
content = content.replace(old_user, new_user)

with open(file_path, "w") as f:
    f.write(content)
print("Updated propose_section_rewrite")
