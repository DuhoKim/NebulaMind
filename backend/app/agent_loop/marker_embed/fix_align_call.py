import re
file_path = "pipeline.py"
with open(file_path, "r") as f:
    content = f.read()

# Fix the alignment target
old_align2 = """        # If we have section_key (we are repairing a specific section), we only align against that section block
        target_sentences = []
        if section_key:
            target_sentences = [(sent, claim_section) for sent in split_sentences(section_block)]
        else:
            target_sentences = all_sentences_with_sections
            
        alignment = align_claim_multipass(claim_text, section_block, target_sentences)"""

new_align2 = """        # If we have section_key (we are repairing a specific section), we only align against that section block
        if section_key and section_key != claim_section:
            # We are repairing a specific section, and this claim doesn't belong to it. 
            # But the caller already filtered claims by section_key if it was provided!
            pass
            
        target_sentences = split_sentences(section_block)
        page_sentences = [s[0] for s in all_sentences_with_sections]
            
        alignment = align_claim_multipass(
            claim_id=claim_id,
            claim_text=claim_text,
            trust_level=trust_level,
            section_title=claim_section,
            section_candidates=target_sentences,
            page_candidates=page_sentences
        )"""

content = content.replace(old_align2, new_align2)

with open(file_path, "w") as f:
    f.write(content)
print("Patched align_claim_multipass call")
