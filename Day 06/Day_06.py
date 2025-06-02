# ✅ Day 06: Random Password Generator using Modules

import random
import string

def generate_password(length=8):
    # Combine all possible characters: letters, digits, punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly pick characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# 🔄 Generate and display the password
print("🔐 Your Random 8-Character Password is:")
print(generate_password())
