import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.page import WikiPage, PageVersion
from app.models.agent import Agent # Import Agent to resolve SQLAlchemy ForeignKey dependency

db = SessionLocal()

# Read renovated content
with open("/Users/duhokim/.openclaw/workspace/galaxy_evolution_renovated.md", "r", encoding="utf-8") as f:
    renovated_content = f.read()

# Fetch page
page = db.query(WikiPage).get(57)
if not page:
    print("Page 57 not found!")
    sys.exit(1)

# Find highest version number
max_version = db.query(PageVersion).filter(PageVersion.page_id == 57).order_by(PageVersion.version_num.desc()).first()
next_version_num = (max_version.version_num + 1) if max_version else 1

print(f"Current highest page version: {max_version.version_num if max_version else 0}")
print(f"Creating new PageVersion: {next_version_num}...")

# Create new version
new_version = PageVersion(
    page_id=57,
    version_num=next_version_num,
    content=renovated_content,
    editor_agent_id=None, # System/Curator
)
db.add(new_version)

# Update page content
page.content = renovated_content

# Commit changes
db.commit()

print(f"SUCCESS: Page 57 has been updated in the database to Version {next_version_num}!")
db.close()
