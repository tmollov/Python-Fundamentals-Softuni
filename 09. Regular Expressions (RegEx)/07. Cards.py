import re

regex = r"([2-9]|10|[JKQA])([SHDC])"
cards = input()

matches = re.finditer(regex,cards)
for match in matches:
    print(str(match[0]), end=" ")