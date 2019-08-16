import re

regex = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
sentence = input()

matches = re.findall(regex,sentence)
for match in matches:
    print(match, end=" ")