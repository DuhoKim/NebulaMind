import re
file_path = "pipeline.py"
with open(file_path, "r") as f:
    content = f.read()

# Add logging
content = content.replace("stats.status = \"committed\"", "log.info(f\"pipeline: page_id={page_id} committed {stats.asserted_count}/{stats.total_claims} assertions\")\n    stats.status = \"committed\"")

with open(file_path, "w") as f:
    f.write(content)
