with open("app/models/edit.py", "r") as f:
    content = f.read()

# Make sure Vote is imported
if "from app.models.vote import Vote" not in content:
    content = content.replace("from app.models.user import User", "from app.models.user import User\nfrom app.models.vote import Vote")
    with open("app/models/edit.py", "w") as f:
        f.write(content)
    print("Fixed EditProposal models issue")
