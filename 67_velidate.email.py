#Write a program to validate an email address using regular expressions.

import re     # import re helps us in loading Python’s re module, which is the built‑in library for regular expressions — a powerful tool to search, match, and manipulate text.


def validate_email(email):
    # Regular expression for validating an email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

# Input from user
email = input("Enter an email address: ")

# Validation
if validate_email(email):
    print("Valid email address ✅")
else:
    print("Invalid email address ❌")
