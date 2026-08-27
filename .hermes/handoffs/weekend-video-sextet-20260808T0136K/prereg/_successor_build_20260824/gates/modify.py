import re

with open('SECTION6_DRAFT_AGY_R9.md', 'r') as f:
    content = f.read()

# Update title
content = content.replace('# §6 DRAFT — AGY SEAT, NINTH PASS (R9),', '# §6 DRAFT — AGY SEAT, NINTH PASS B (R9B),')

# Update BRIEF reference
content = content.replace('BRIEF_DRAFT_SECTION6_R9.md', 'BRIEF_DRAFT_SECTION6_R9B.md')

# Add Clause 10
clause_text = "10. **Branch termination.** Every branch of every row must terminate in one stated outcome, because a branch whose consequence depends on a judgement made later is not terminated.\n\n### §6.2"
content = content.replace('### §6.2', clause_text)

# Add item 11 to Part 5
part5_addition = "\n11. **R9B Addition.** ADDITION. Added Clause 10 establishing that every branch of every row must terminate in one stated outcome."
content += part5_addition + "\n"

with open('SECTION6_DRAFT_AGY_R9B.md', 'w') as f:
    f.write(content)

