#Write a py program to find all occurrences of a pattern in a string using regular expressions. 

import re

# Input string and pattern
text = input("Enter the string: ")
pattern = input("Enter the pattern to search: ")

# Find all occurrences
matches = re.findall(pattern, text)

# Output results
if matches:
    print(f"Pattern '{pattern}' found {len(matches)} time(s):")
    for i, match in enumerate(matches, start=1):
        print(f"{i}. {match}")
else:
    print(f"No occurrences of pattern '{pattern}' found.")
