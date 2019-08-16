import re

regex = r"(^|(?<=\s))(-*[0-9]+\.*[0-9]*)($|(?=\s))"
numbers = input()

matches = re.findall(regex,numbers)
for match in matches:
    print(match[1], end=" ")