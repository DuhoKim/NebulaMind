import re
file_path = "tasks.py"
with open(file_path, "r") as f:
    content = f.read()

# Update claim fetch to use claim_section_assignments
old_fetch = """        rows = db.execute(
            text(
                "SELECT id, text, trust_level, section, order_idx "
                "FROM claims "
                "WHERE page_id = :pid AND status != 'rejected' "
                "ORDER BY order_idx ASC NULLS LAST"
            ),
            {"pid": page_id},
        ).fetchall()

        claims = [
            {
                "id": r[0],
                "text": r[1],
                "trust_level": r[2],
                "section": r[3],
                "order_idx": r[4],
            }
            for r in rows
        ]"""

new_fetch = """        # If section_key is provided, we only need to repair that section's owned claims.
        # But run_pipeline expects all page claims? Actually, run_pipeline aligns the whole page.
        # Let's fetch assigned claims. If section_key is provided, we might want to filter, but 
        # run_pipeline currently runs on the whole page content. We will just pass the owner_section_key
        # as 'section' so run_pipeline can use it for matching.
        query = \"\"\"
            SELECT c.id, c.text, c.trust_level, a.owner_section_key, c.order_idx
            FROM claims c
            JOIN claim_section_assignments a ON c.id = a.claim_id
            WHERE c.page_id = :pid AND c.status != 'rejected' AND a.assignment_status = 'active'
        \"\"\"
        params = {"pid": page_id}
        if section_key:
            query += " AND a.owner_section_key = :sec_key"
            params["sec_key"] = section_key
            
        query += " ORDER BY c.order_idx ASC NULLS LAST"
        
        rows = db.execute(text(query), params).fetchall()

        claims = [
            {
                "id": r[0],
                "text": r[1],
                "trust_level": r[2],
                "section": r[3], # actually owner_section_key
                "order_idx": r[4],
            }
            for r in rows
        ]"""

content = content.replace(old_fetch, new_fetch)
with open(file_path, "w") as f:
    f.write(content)
print("Patched tasks.py claim fetch")
