import re
file_path = "injector.py"
with open(file_path, "r") as f:
    content = f.read()

# Let's see how they get injected in content
# Around line 140
