file_path = "app/models/edit.py"
with open(file_path, "r") as f:
    content = f.read()

content = content.replace("class EditProposal(Base):", "from app.models.vote import Vote\n\nclass EditProposal(Base):")

with open(file_path, "w") as f:
    f.write(content)
print("Patched edit.py")
