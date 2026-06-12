import re
file_path = "tasks.py"
with open(file_path, "r") as f:
    content = f.read()

# Update _SONNET_SECTION_SYSTEM to use the required footer and separate constraints
old_sys = """_SONNET_SECTION_SYSTEM = (
    "You are an expert astronomy wiki editor writing at graduate-textbook depth. "
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
)"""

content = content.replace(old_sys, new_sys)

# Now, update the user_msg formatting in sonnet_section_rewrite
# We need to query claim_section_assignments
old_query = """        page_claims = (
            db.query(ClaimModel)
            .filter(ClaimModel.page_id == page_id)
            .order_by(ClaimModel.created_at.desc())
            .limit(200)
            .all()
        )
        claims_text = "\\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in page_claims)"""

new_query = """        # Fetch owned claims
        from sqlalchemy import text
        owned_res = db.execute(text(\"\"\"
            SELECT c.id, c.trust_level, c.text 
            FROM claim_section_assignments a
            JOIN claims c ON c.id = a.claim_id
            WHERE a.page_id = :pid AND a.owner_section_key = :sec_key AND a.assignment_status = 'active'
        \"\"\"), {"pid": page_id, "sec_key": re.sub(r'[^a-z0-9\\s]', '', section_to_rewrite.lower()).replace(' ', '_').strip()}).fetchall()
        
        must_keep = [r for r in owned_res if r.trust_level in ('accepted', 'consensus')]
        optional = [r for r in owned_res if r.trust_level not in ('accepted', 'consensus')]
        
        claims_text = "Must-Keep Owned Claims:\\n" + "\\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in must_keep) + "\\n\\n"
        claims_text += "Optional Owned Claims:\\n" + "\\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in optional)
"""

content = content.replace(old_query, new_query)

# And update the prompt string
old_user_msg = """        user_msg = (
            f"Current section:\\n{current_section}\\n\\n"
            f"Key claims on this page:\\n{claims_text}\\n\\n"
            "Rewrite this section. Requirements:\\n\"\"\""
            f"{section_guidance}\n"
            "\"\"\"\n"
            f"Keep the ## header exactly as: ## {section_to_rewrite}"
        )"""

new_user_msg = """        user_msg = (
            f"Current section:\\n{current_section}\\n\\n"
            f"Claims assigned to this section:\\n{claims_text}\\n\\n"
            "Rewrite this section. Requirements:\\n\"\"\""
            f"{section_guidance}\n"
            "\"\"\"\n"
            f"Keep the ## header exactly as: ## {section_to_rewrite}\\n\\n"
            "At the end of your response, you MUST include a marker report in exactly this format:\\n"
            "<!--marker-report\\n{\\n  \\"section\\": \\"Section Name\\",\\n  \\"asserted_claim_ids\\": [123, 124],\\n  \\"omitted_owned_claim_ids\\": [{\\"id\\": 126, \\"reason\\": \\"not asserted\\"}]\\n}\\n-->"
        )"""

content = content.replace(old_user_msg, new_user_msg)

# Also need to parse the footer to check must-keep gate before accepting.
old_accept = """        new_section_text = response.content[0].text.strip()
        run = AutowikiRun("""
new_accept = """        raw_text = response.content[0].text.strip()
        
        # Parse marker-report footer
        report_match = re.search(r"<!--marker-report\\s*({.*?})\\s*-->", raw_text, re.DOTALL)
        if not report_match:
            logger.warning("[sonnet_section_rewrite] Missing marker report in footer")
            return {"decision": "skip", "reject_reason": "missing_marker_report"}
            
        try:
            import json
            report = json.loads(report_match.group(1))
        except Exception as e:
            logger.warning("[sonnet_section_rewrite] Invalid JSON in marker report")
            return {"decision": "skip", "reject_reason": "invalid_marker_report"}
            
        asserted = set(report.get("asserted_claim_ids", []))
        must_keep_ids = {r.id for r in must_keep}
        
        missing_must_keep = must_keep_ids - asserted
        # We allow omission if there's a reason, but the design doc says:
        # "reject if any must_keep_claims (accepted/consensus) are missing without a stated reason"
        omitted = report.get("omitted_owned_claim_ids", [])
        omitted_with_reason = {o["id"] for o in omitted if "id" in o and o.get("reason")}
        
        unaccounted = missing_must_keep - omitted_with_reason
        if unaccounted:
            logger.warning(f"[sonnet_section_rewrite] Missing must_keep claims unaccounted for: {unaccounted}")
            return {"decision": "skip", "reject_reason": "missing_must_keep_claims"}
            
        new_section_text = re.sub(r"<!--marker-report.*?-->", "", raw_text, flags=re.DOTALL).strip()
        
        run = AutowikiRun("""

content = content.replace(old_accept, new_accept)

with open(file_path, "w") as f:
    f.write(content)
print("Updated sonnet_section_rewrite")
