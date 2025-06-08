import re

def is_valid_gmail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    if re.match(pattern, email):
        return "✅ Valid Gmail ID"
    else:
        return "❌ Invalid Gmail ID"

# Test cases
emails = ["me@gmail.com", "you@outlook.com", "fake@gmail", "hi@gmail.com", "hello@@gmail.com", "dhanashree@outlook.com", "check123*_@gmail.com", "dhanashreesr@gmail.com", "deepika123@gmail.com"]
for e in emails:
    print(f"{e} → {is_valid_gmail(e)}")
