import re

regex = r"\b(?:0x)?[0-9A-F]+\b"
numbers = input()

matches = re.findall(regex,numbers)
for match in matches:
    print(str(match), end=" ")